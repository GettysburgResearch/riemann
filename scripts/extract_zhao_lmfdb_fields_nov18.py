"""Extract degree 5–8 tables from Zenodo 24323763's nf_fields.txt.zst.

Usage: python scripts/extract_zhao_lmfdb_fields_nov18.py nf_fields.txt.zst OUT_DIR
Data are from the LMFDB Collaboration, https://doi.org/10.5281/zenodo.24323763,
CC BY-SA 4.0. Coefficient vectors are in ascending order.
"""
import argparse
import hashlib
import json
import subprocess
from pathlib import Path

COMPRESSED_SHA256 = "eb006d5a10c4153a0a8ce98ee0004b8d826f40d2d6e5c1fbe1fc8974a3b04016"
TOTAL_ROWS = 22_444_816
LIMITS = {5: 1_100_000, 6: 2_300_000, 7: 4_300_000, 8: 5_100_000}
SIGNATURES = {5: range(3), 6: range(4), 7: range(4), 8: (3, 4)}


def extract(archive, directory):
    with archive.open("rb") as source:
        if hashlib.file_digest(source, "sha256").hexdigest() != COMPRESSED_SHA256:
            raise ValueError("Compressed archive does not match the published LMFDB manifest")
    fields = {(n, r): [] for n, signatures in SIGNATURES.items() for r in signatures}
    degree_bounds = {str(n).encode(): bound for n, bound in LIMITS.items()}
    with subprocess.Popen(["zstd", "-dc", archive], stdout=subprocess.PIPE) as process:
        rows = process.stdout
        schema = rows.readline().decode("ascii").strip().split("|")
        rows.readline()
        assert rows.readline().strip() == b""
        assert schema[4] == "coeffs" and schema[6:8] == ["degree", "disc_abs"]
        label_col, signature_col = (schema.index(k) for k in ("label", "r2"))
        count = 0
        for row in rows:
            count += 1
            first = row.split(b"|", 8)
            limit = degree_bounds.get(first[6])
            if limit is None or int(first[7]) > limit:
                continue
            cols = row.split(b"|")
            n, r2 = int(first[6]), int(cols[signature_col])
            if (n, r2) not in fields:
                continue
            label = cols[label_col].decode("ascii")
            coefficients = [int(c) for c in first[4].removeprefix(b"{").removesuffix(b"}").split(b",")]
            degree, real, disc, index = (int(s) for s in label.split("."))
            assert degree == n and real == n - 2*r2 and disc == int(first[7]) and index > 0
            assert len(coefficients) == n+1 and coefficients[-1] == 1
            fields[n, r2].append({"label": label, "coeffs": coefficients})
        assert process.wait() == 0 and count == TOTAL_ROWS
    directory.mkdir(parents=True, exist_ok=True)
    for (n, r2), group in fields.items():
        assert len(group) == len({row["label"] for row in group})
        group.sort(key=lambda row: tuple(int(x) for x in row["label"].split(".")))
        payload = (json.dumps(group, separators=(",", ":"))+"\n").encode()
        path = directory / f"n{n}-r{r2}.json"
        pending = path.with_suffix(".partial")
        pending.write_bytes(payload)
        pending.replace(path)
        print(n, r2, len(group), hashlib.sha256(payload).hexdigest(), flush=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("archive", type=Path)
    parser.add_argument("directory", type=Path)
    args = parser.parse_args()
    extract(args.archive, args.directory)
