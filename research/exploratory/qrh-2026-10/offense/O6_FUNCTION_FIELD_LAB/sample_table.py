"""sample_table.py -- summarize lab_sample outputs: R(d) = mean|A_u(d)|^2 / mean #{n sqfree,(n,u)=1}
over uniformly sampled rows of exact degree m (each row exact; the mean is a Monte Carlo estimate,
standard error from the sample variance).  Usage: python3 sample_table.py samp_*.txt
"""
import sys, math
for p in sys.argv[1:]:
    lines = [l for l in open(p) if l.strip()]
    hdr = lines[0]
    q = int(hdr.split()[1].split('=')[1]); m = int(hdr.split()[2].split('=')[1])
    print(f'\n{hdr.strip()}')
    print('| d | rho=m/d | R = M2/Diag | std.err | max |A|^2/q^d |')
    print('|---|---|---|---|---|')
    for l in lines[1:]:
        t = l.split(); d = int(t[0]); N = int(t[1]); S1, S2, SC, mx = map(float, t[2:6])
        if d < m - 1:
            continue
        mean = S1 / N; var = max(S2 / N - mean * mean, 0.0); se = math.sqrt(var / N)
        c = SC / N
        print(f'| {d} | {m/d:.2f} | {mean/c:.3f} | {se/c:.3f} | {mx:.3g} |')
