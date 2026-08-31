"""C5: the graph mechanism telescope (programme #763).

Enumerates cubic graphs, certifies the purity/Ramanujan mechanism exactly
per graph, correlates it with structure, and runs deterministic rewiring
walks in which every departure/reentry of the critical-circle property is
EXACT (Sturm-certified) — the discrete, fully provable mirror of the
Epstein moduli walks.

ENUMERATION SCOPE (stated honestly): all HAMILTONIAN connected cubic
graphs on n = 4..12 vertices, generated as an n-cycle plus a perfect
matching of chords (every Hamiltonian cubic graph arises this way),
deduplicated by dihedral symmetry, exact characteristic polynomial, and
brute isomorphism inside residual collision classes; PLUS the named
non-Hamiltonian additions (Petersen is Hamiltonian-free... it is
NON-Hamiltonian and added explicitly). NOT claimed exhaustive over all
connected cubic graphs (bridged non-Hamiltonian examples exist from
n = 10); the atlas records its own scope.

Everything exact: Fraction arithmetic, Sturm certificates. Writes
graphs/telescope.json and graphs/walks.json. rh_established = false.
"""
import itertools
import json
import sys
import time
from fractions import Fraction as Fr

sys.path.insert(0, '.')
from core.exact import (charpoly_of_matrix, count_real_roots_in, poly_eval,
                        elementary_from_power_sums)

Q = 2  # cubic: q + 1 = 3


def say(m):
    print(f"[{time.strftime('%H:%M:%S')}] {m}", flush=True)


# ---------------- generation: chord diagrams ------------------------------

def perfect_matchings(points):
    if not points:
        yield []
        return
    a = points[0]
    for i in range(1, len(points)):
        b = points[i]
        rest = points[1:i] + points[i + 1:]
        for m in perfect_matchings(rest):
            yield [(a, b)] + m


def diagram_to_adj(n, chords):
    A = [[0] * n for _ in range(n)]
    for i in range(n):
        j = (i + 1) % n
        A[i][j] = A[j][i] = 1
    for (a, b) in chords:
        if A[a][b]:
            return None            # chord parallel to a cycle edge: multi
        A[a][b] = A[b][a] = 1
    return A


def canon_diagram(n, chords):
    """Minimal representative of the chord set under the dihedral group."""
    best = None
    cs = [tuple(sorted(c)) for c in chords]
    for r in range(n):
        for flip in (False, True):
            img = []
            for (a, b) in cs:
                a2 = (a + r) % n if not flip else (-a + r) % n
                b2 = (b + r) % n if not flip else (-b + r) % n
                img.append((min(a2, b2), max(a2, b2)))
            key = tuple(sorted(img))
            if best is None or key < best:
                best = key
    return best


def is_isomorphic_brute(A, B):
    n = len(A)
    idx = list(range(n))
    for perm in itertools.permutations(idx):
        ok = True
        for i in range(n):
            for j in range(i + 1, n):
                if A[i][j] != B[perm[i]][perm[j]]:
                    ok = False
                    break
            if not ok:
                break
        if ok:
            return True
    return False


# ---------------- exact structural invariants -----------------------------

def girth(A):
    n = len(A)
    best = None
    for s in range(n):
        dist = {s: 0}
        parent = {s: -1}
        queue = [s]
        while queue:
            v = queue.pop(0)
            for w in range(n):
                if not A[v][w]:
                    continue
                if w not in dist:
                    dist[w] = dist[v] + 1
                    parent[w] = v
                    queue.append(w)
                elif parent[v] != w:
                    c = dist[v] + dist[w] + 1
                    best = c if best is None else min(best, c)
    return best


def diameter_and_connected(A):
    n = len(A)
    diam = 0
    for s in range(n):
        dist = {s: 0}
        queue = [s]
        while queue:
            v = queue.pop(0)
            for w in range(n):
                if A[v][w] and w not in dist:
                    dist[w] = dist[v] + 1
                    queue.append(w)
        if len(dist) < n:
            return None, False
        diam = max(diam, max(dist.values()))
    return diam, True


def bipartite(A):
    n = len(A)
    color = {0: 0}
    queue = [0]
    while queue:
        v = queue.pop(0)
        for w in range(n):
            if A[v][w]:
                if w not in color:
                    color[w] = 1 - color[v]
                    queue.append(w)
                elif color[w] == color[v]:
                    return False
    return True


def squares_poly(A):
    """Monic polynomial with roots = squares of adjacency eigenvalues,
    via power sums tr(A^{2k})."""
    n = len(A)
    A2 = [[sum(A[i][t] * A[t][j] for t in range(n)) for j in range(n)]
          for i in range(n)]
    Ak = [[Fr(1) if i == j else Fr(0) for j in range(n)] for i in range(n)]
    tr2 = []
    for _ in range(n):
        Ak = [[sum(Ak[i][t] * A2[t][j] for t in range(n)) for j in range(n)]
              for i in range(n)]
        tr2.append(sum(Ak[i][i] for i in range(n)))
    e2 = elementary_from_power_sums(tr2, n)
    p2 = [Fr(0)] * (n + 1)
    p2[n] = Fr(1)
    for i, ei in enumerate(e2, start=1):
        p2[n - i] = (-1) ** i * ei
    return p2


def purity_certificate(A):
    """(ramanujan: bool, n_untempered: int) — Sturm-certified. Untempered
    count = #distinct eigenvalue-squares strictly inside (4q, (q+1)^2);
    endpoint roots (trivial ±3, and ±2sqrt2 boundary) subtracted exactly."""
    p2 = squares_poly(A)
    cnt = count_real_roots_in(p2, 4 * Q, (Q + 1) ** 2)
    if poly_eval(p2, (Q + 1) ** 2) == 0:
        cnt -= 1
    return (cnt == 0), cnt


def atlas_row(name, A, scope):
    diam, conn = diameter_and_connected(A)
    if not conn:
        return None
    ram, nunt = purity_certificate(A)
    return {"name": name, "n": len(A), "scope": scope,
            "girth": girth(A), "diameter": diam,
            "bipartite": bipartite(A),
            "ramanujan": ram, "untempered_squares": nunt}


# ---------------- named graphs -------------------------------------------

def petersen():
    E = set()
    for i in range(5):
        E |= {(i, (i + 1) % 5), (i + 5, (i + 2) % 5 + 5), (i, i + 5)}
    A = [[0] * 10 for _ in range(10)]
    for (i, j) in E:
        A[i][j] = A[j][i] = 1
    return A


def gp(n, k):
    """Generalized Petersen GP(n,k)."""
    A = [[0] * (2 * n) for _ in range(2 * n)]
    for i in range(n):
        for (a, b) in ((i, (i + 1) % n), (n + i, n + (i + k) % n),
                       (i, n + i)):
            A[a][b] = A[b][a] = 1
    return A


# ---------------- rewiring walks -----------------------------------------

def walk(A0, steps):
    """Deterministic UNBIASED 2-swap walk: at each step apply the
    lexicographically first swap (a,b),(c,d) -> (a,c),(b,d) that keeps the
    graph simple, 3-regular, and connected — chosen WITHOUT looking at the
    spectrum (so the path is not event-seeking) — then certify the purity
    status exactly (one Sturm certificate per step). Departure/reentry
    events are recorded as they occur along the path; a rotating offset on
    the edge list keeps the walk from undoing its own last swap."""
    A = [row[:] for row in A0]
    n = len(A)
    hist = []
    ram, nunt = purity_certificate(A)
    hist.append({"step": 0, "ramanujan": ram, "untempered": nunt,
                 "swap": None})
    for s in range(1, steps + 1):
        edges = [(i, j) for i in range(n) for j in range(i + 1, n) if A[i][j]]
        off = (7 * s) % len(edges)          # deterministic rotation
        edges = edges[off:] + edges[:off]
        applied = None
        for (a, b) in edges:
            for (c, d) in edges:
                if len({a, b, c, d}) < 4 or A[a][c] or A[b][d]:
                    continue
                A[a][b] = A[b][a] = 0
                A[c][d] = A[d][c] = 0
                A[a][c] = A[c][a] = 1
                A[b][d] = A[d][b] = 1
                _, conn = diameter_and_connected(A)
                if conn:
                    applied = [a, b, c, d]
                    break
                A[a][c] = A[c][a] = 0
                A[b][d] = A[d][b] = 0
                A[a][b] = A[b][a] = 1
                A[c][d] = A[d][c] = 1
            if applied:
                break
        if not applied:
            break
        r2, u2 = purity_certificate(A)
        rec = {"step": s, "ramanujan": r2, "untempered": u2, "swap": applied}
        if u2 > nunt:
            rec["event"] = "departure"
        elif u2 < nunt:
            rec["event"] = "reentry"
        hist.append(rec)
        ram, nunt = r2, u2
    return hist


# ---------------- main ----------------------------------------------------

def main():
    atlas = []
    say("enumeration: Hamiltonian cubic via chord diagrams, n = 4..12")
    for n in (4, 6, 8, 10, 12):
        seen_diagrams = set()
        classes = []          # (charpoly_tuple, adj)
        for m in perfect_matchings(list(range(n))):
            key = canon_diagram(n, m)
            if key in seen_diagrams:
                continue
            seen_diagrams.add(key)
            A = diagram_to_adj(n, m)
            if A is None:
                continue
            cp = tuple(charpoly_of_matrix(A))
            dup = False
            for (cp2, B) in classes:
                if cp2 == cp and is_isomorphic_brute(A, B):
                    dup = True
                    break
            if not dup:
                classes.append((cp, A))
        say(f"  n={n}: {len(classes)} Hamiltonian cubic classes")
        for i, (cp, A) in enumerate(classes):
            row = atlas_row(f"ham_cubic_n{n}_{i}", A,
                            "exhaustive Hamiltonian cubic (chord diagrams)")
            if row:
                atlas.append(row)

    say("named non-Hamiltonian addition: Petersen")
    atlas.append(atlas_row("petersen", petersen(), "named addition"))

    say("parametrized families: GP(n,k), n <= 12")
    for n in range(5, 13):
        for k in range(1, n // 2 + (0 if n % 2 == 0 else 1)):
            if k == 0 or (n % 2 == 0 and k == n // 2):
                continue
            row = atlas_row(f"GP({n},{k})", gp(n, k), "GP family")
            if row:
                atlas.append(row)

    with open("graphs/telescope.json", "w") as f:
        json.dump({"scope_note": ("Hamiltonian cubic exhaustive n<=12 via "
                                  "chord diagrams + named additions + GP "
                                  "family; NOT exhaustive over all connected "
                                  "cubic (bridged non-Hamiltonian exist from "
                                  "n=10)"),
                   "rows": atlas, "rh_established": False}, f, indent=1)
    ram = sum(1 for r in atlas if r["ramanujan"])
    say(f"atlas: {len(atlas)} graphs, {ram} Ramanujan")

    say("rewiring walks (unbiased deterministic; seeds' status certified at "
        "step 0, not assumed)")
    walks = {}
    for name, seed in (("walk_from_GP(12,1)", gp(12, 1)),
                       ("walk_from_GP(12,5)", gp(12, 5)),):
        say(f"  walk {name}")
        walks[name] = walk(seed, 25)
    with open("graphs/walks.json", "w") as f:
        json.dump({"note": ("deterministic 2-swap walks; every step's "
                            "purity status is Sturm-certified exact — "
                            "departure/reentry events are provable facts "
                            "about specific graph pairs"),
                   "walks": walks, "rh_established": False}, f, indent=1)
    for name, h in walks.items():
        ev = [x for x in h if x.get("event")]
        say(f"  {name}: {len(h)-1} steps, events: "
            f"{[(x['step'], x['event']) for x in ev]}")
    say("C5 done")


if __name__ == "__main__":
    main()
