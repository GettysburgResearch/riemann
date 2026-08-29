# Smoke timing notes (provisional)

Recorded before the hour-budget scaled runs. Numbers are wall-clock on this VM
and should be re-measured elsewhere.

| Comp | Smoke cell | Observed | Scaled plan | Naive EST |
|---|---|---|---|---|
| C1 | `Fwin(1,j)` | ~0.07s/coeff | 14 `(alpha,N)` pairs, N≤8 | ~3–8 min |
| C1 | Sturm N=5 | ≪0.1s | same | not the bottleneck |
| C1 | sampled vs windowed @ (1.0,4) | sampled deficit 4, windowed 0 | keep side-by-side | — |
| C2 | `build_Ea(R=2,a=5,m=3)` | ~0.09s | 4×5 ladder, m=6 + proxy | ~1–2 min |
| C3 | cell a=5 / a=6.5 | 0.12s / 1.7s | cap `exp(2a)≤2.5e5` | ~1–5 min |
| C4 | full old grid | 0.5s | denser e/β/h grid | <5s |
| C5 | M=80, notches 0..10 | 4s | M=120, notches 0..20 | ~15–40s |

These are planning aids only.
