"""Fits for the scaling laws.  Parses out_all.txt PART 1."""
import re, sys, math

txt = open('/tmp/claude-0/-home-user-riemann/8aa2c694-669d-5c54-ab29-9ac46b683161/scratchpad/det/out_all.txt').read()
part1 = txt.split('### PART 1x')[0]

rows = []
for m in re.finditer(r"N=\s*(\d+) dim=\s*\d+ dps=\s*\d+ mu\*=\s*[\d.]+ inertia=\([^)]*\)\s+"
                     r"lmax=([\d.e+-]+) lmin0=([\d.e+-]+) kappa=\S+\s+delta_c=([\d.e+-]+)\s+"
                     r"det16=([\d.e+-]+) det30=([\d.e+-]+) det50=([\d.e+-]+)", part1):
    rows.append(dict(N=int(m.group(1)), lmax=float(m.group(2)), lmin=float(m.group(3)),
                     dc=float(m.group(4)), d16=float(m.group(5)),
                     d30=float(m.group(6)), d50=float(m.group(7))))

def lstsq(xs, ys, deg):
    n = deg + 1
    A = [[sum(x ** (i + j) for x in xs) for j in range(n)] for i in range(n)]
    b = [sum(y * x ** i for x, y in zip(xs, ys)) for i in range(n)]
    for i in range(n):
        p = max(range(i, n), key=lambda r: abs(A[r][i]))
        A[i], A[p] = A[p], A[i]; b[i], b[p] = b[p], b[i]
        for r in range(i + 1, n):
            f = A[r][i] / A[i][i]
            for c in range(i, n):
                A[r][c] -= f * A[i][c]
            b[r] -= f * b[i]
    c = [0] * n
    for i in reversed(range(n)):
        c[i] = (b[i] - sum(A[i][j] * c[j] for j in range(i + 1, n))) / A[i][i]
    return c

def rms(xs, ys, c):
    return math.sqrt(sum((y - sum(ci * x ** i for i, ci in enumerate(c))) ** 2
                         for x, y in zip(xs, ys)) / len(xs))

Ns = [r['N'] for r in rows]
print("N :", Ns)
for key, name in (('lmin', 'log10 lambda_min(unperturbed)'),
                  ('dc', 'log10 delta_c'),
                  ('d16', 'log10 delta_det(16 digits)'),
                  ('d30', 'log10 delta_det(30 digits)'),
                  ('d50', 'log10 delta_det(50 digits)')):
    ys = [math.log10(r[key]) for r in rows]
    print("\n%s" % name)
    print("  values      :", " ".join("%8.4f" % y for y in ys))
    print("  diffs (dN=2):", " ".join("%8.4f" % (ys[i+1]-ys[i]) for i in range(len(ys)-1)))
    c1 = lstsq(Ns, ys, 1); c2 = lstsq(Ns, ys, 2)
    print("  linear   : %.4f + %.4f N        rms %.4f" % (c1[0], c1[1], rms(Ns, ys, c1)))
    print("  quadratic: %.4f + %.4f N + %.5f N^2   rms %.4f"
          % (c2[0], c2[1], c2[2], rms(Ns, ys, c2)))

print("\n--- headline ratios ---")
print(" N   delta_c        sqrt(lmin/lmax)   dc/naive     det16/delta_c   |Re rho-1/2| at dc   at det16")
for r in rows:
    naive = math.sqrt(r['lmin'] / r['lmax'])
    print(" %-3d %.4e     %.4e        %.3e    %.3e       %.3e            %.3e"
          % (r['N'], r['dc'], naive, r['dc']/naive, r['d16']/r['dc'],
             r['dc']/1.5, r['d16']/1.5))

print("\n--- digits of working precision needed to see the transition at delta_c ---")
print(" N   log10(kappa)=log10(lmax/lmin)   det50==delta_c ?")
for r in rows:
    k = math.log10(r['lmax']/r['lmin'])
    print(" %-3d %8.2f                        %s"
          % (r['N'], k, "yes" if abs(r['d50']/r['dc']-1) < 0.02 else "no (x%.2g)" % (r['d50']/r['dc'])))
