"""row_anatomy.py -- per-row anatomy of the exact lab moments (EXACT inputs, float summaries).
Reads a lab_core per-row dump (lines: k idx is6 a0,b0 a1,b1 ... with A_u(d) = +-(a_d + b_d omega)).
For rows of exact degree k and each d: the share of M2 carried by the top 1% / top 10% rows, the median
and mean of |A_u(d)|^2/q^d, and the mean after removing rows whose sequence |A_u(d)|^2/q^d is periodic-
bounded (special members are detected as rows with max_d |A_u(d)|^2/q^d >= T, T given).
Usage: python3 row_anatomy.py q dump k dlist T
"""
import sys
import statistics as st
q = int(sys.argv[1]); path = sys.argv[2]; K = int(sys.argv[3]); ds = [int(x) for x in sys.argv[4].split(',')]; T = float(sys.argv[5])
rows = []
for line in open(path):
    t = line.split()
    if int(t[0]) != K:
        continue
    co = [tuple(map(int, x.split(','))) for x in t[3:]]
    rows.append([(a * a - a * b + b * b) / q ** d for d, (a, b) in enumerate(co)])
print(f'q={q} rows of exact degree {K}: {len(rows)}')
dmax = len(rows[0]) - 1
special = [r for r in rows if max(r[K:]) >= T]
print(f'rows with max_(d>={K}) |A|^2/q^d >= {T}: {len(special)} ({100*len(special)/len(rows):.2f}%)')
print('| d | mean |A|^2/q^d | median | top1% share of M2 | top10% share | mean without flagged rows |')
print('|---|---|---|---|---|---|---|')
for d in ds:
    v = sorted((r[d] for r in rows), reverse=True)
    tot = sum(v)
    n1 = max(1, len(v) // 100); n10 = max(1, len(v) // 10)
    gen = [r[d] for r in rows if max(r[K:]) < T]
    print(f'| {d} | {tot/len(v):.3f} | {st.median(v):.3f} | {sum(v[:n1])/tot:.3f} | {sum(v[:n10])/tot:.3f} | {sum(gen)/max(1,len(gen)):.3f} |')
