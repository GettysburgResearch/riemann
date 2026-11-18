"""Compare the LMFDB degree 6/7 extract to the corrected PARI tables."""
import argparse
from collections import defaultdict
import gzip
import json
from pathlib import Path
import subprocess

# Bounds in PARI's README are strict. The LMFDB extract may stop sooner.
PARI_LIMITS = {
    (6, 0): 200000, (6, 2): 400000, (6, 4): 1000000, (6, 6): 10000000,
    (7, 1): 600000, (7, 3): 1800000, (7, 5): 12000000, (7, 7): 150000000,
}


def run_gp(gp, commands):
    result = subprocess.run([gp, "-fq"], input="\n".join(commands)+"\n", text=True,
                            capture_output=True, check=True)
    if result.stderr:
        raise RuntimeError(result.stderr)
    replies = [json.loads(line) for line in result.stdout.splitlines()]
    assert len(replies) == len(commands)
    return iter(replies)


def compare(lmfdb_dir, pari_dir, gp, degree, real, pari_limit):
    upper = min(pari_limit-1, {6: 2300000, 7: 4300000}[degree])
    complex_places = (degree-real)//2
    pari, lmfdb = defaultdict(list), defaultdict(list)
    with gzip.open(pari_dir/f"T{degree}{real}.gp.gz") as rows:
        for line in rows:
            disc, coefficients, _, _ = json.loads(line)
            if abs(disc) <= upper:
                pari[abs(disc)].append(list(reversed(coefficients)))
    for row in json.loads((lmfdb_dir/f"n{degree}-r{complex_places}.json").read_text()):
        disc = int(row["label"].split(".")[2])
        if disc <= upper:
            lmfdb[disc].append(row["coeffs"])

    # Two LMFDB septics occur at discriminants entirely absent from the PARI file.
    extra_discs = {1328121, 1771597} if (degree, real) == (7, 3) else set()
    assert lmfdb.keys() - pari.keys() == extra_discs and not pari.keys() - lmfdb.keys()
    for disc in extra_discs:
        coefficients, = lmfdb[disc]
        command = f"K=nfinit(Polrev({coefficients}));print([K.disc,K.sign]);"
        assert next(run_gp(gp, [command])) == [disc, [real, complex_places]]

    commands, sizes = [], []
    identical = 0
    for disc, polynomials in pari.items():
        available = lmfdb[disc].copy()
        unresolved = []
        for coefficients in polynomials:
            if coefficients in available:
                available.remove(coefficients)
                identical += 1
            else:
                unresolved.append(coefficients)
        assert len(available) == len(unresolved)
        if unresolved:
            sizes.append(len(unresolved))
            for coefficients in unresolved:
                commands.append(f"V={coefficients}; W={available};"
                                "print(vector(#W,j,if(nfisisom(Polrev(V),Polrev(W[j]))==0,0,1)));")
    replies = run_gp(gp, commands)
    for size in sizes:
        matrix = [next(replies) for _ in range(size)]
        assert all(sum(row) == 1 for row in matrix) and all(sum(col) == 1 for col in zip(*matrix))
    print(degree, real, upper, identical, len(commands), len(extra_discs))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("lmfdb_directory", type=Path)
    parser.add_argument("pari_directory", type=Path)
    parser.add_argument("--gp", default="gp")
    args = parser.parse_args()
    for (n, r1), bound in PARI_LIMITS.items():
        compare(args.lmfdb_directory, args.pari_directory, args.gp, n, r1, bound)
