# Lane 3 checkpoint 3 — independent saturation verification (saturation.py, saturation_results.json)

Own implementation, own algebra path (NOT the orchestrator's): exact split
T(d) = 4 sqrt(x)/d - 3/sqrt(d) and Q_Y(j) = 4 C_j sqrt(Y) + R_j(Y), giving the
exact cancellation-free identities
    4 sqrt(x) Delta1 = 3 Delta2   (from demand equality; Delta2 = sum_e theta/sqrt(e) - sum_o 1/sqrt(o))
    M_sc = -(3/4) Delta2
    M_j  = 3 C_j Delta2 + [sum_e theta R_j(x/e)/sqrt(e) - sum_o R_j(x/o)/sqrt(o)]
    =>  M_j = dR_j - 4 C_j M_sc   (verified 0.00e+00 at every x)
H exact from longdouble prefix tables to 1e7; expansion H = 4 sqrt(Y)
+ zeta(1/2) log Y + zeta'(1/2) + E(Y) beyond, with E measured from the table:
E(1e3) = -2.635e-6, E(1e4) = -8.333e-8, E(1e5) = -2.635e-9, E(1e6) = -8.458e-11
— the ratio is exactly 10^{3/2} = 31.6 per decade: E(Y) = -(1/12) Y^{-3/2} (1+o(1)),
which is precisely the Euler-Maclaurin boundary term f'(Y)/12 = -Y^{-3/2}/12 for
f(m) = m^{-1/2} log(Y/m) (f(Y) = 0 kills the half-integer wobble; check:
(1/12)*1e3^{-3/2} = 2.64e-6 vs measured 2.635e-6). So the [expansion lemma]
has a clean proved form with remainder O(Y^{-3/2}); error contribution to the
saturation margins < 1e-9.
Q knot-form validated against the direct gamma-sum at 14 scattered (Y,j) points
to <= 5.7e-14.

## Results vs orchestrator's claims — ALL CONFIRMED

| x     | M_2 (mine)  | orch    | M_3 (mine) | orch | M_sc (mine) | orch    |
|-------|-------------|---------|------------|------|-------------|---------|
| 1e26  | 1471.1659   | 1471    | 538.6998   | 539  | 13.903914   | 13.9039 |
| 1e28  | 1609.7685   | 1610    | 589.3748   | 589  | 13.903914   |         |
| 1e30  | 1748.3711   | 1748.37 | 640.0498   | 640  | 13.903914   |         |
| 1e34  | 2025.5764   | 2026    | 741.3997   | 741  | 13.903914   |         |

- Sliver: threshold even e* = 1110 (the 132nd smallest even), full-filled = 131,
  sliver (theta < 1) = 131072 - 131 = 130941 evens, theta*(1110) = 0.419882603,
  all x-independent from 1e26 on. CONFIRMED (130941 / 1110). Limiting threshold
  independently from the 1/e-prefix crossing of S1o: index 132, e = 1110,
  prefix-excess 5.226e-4 (comfortably nonzero -> threshold index is stable).
- B^s_infinity = +0.0022144 = prod_{p<=61}(1 - p^{-1/2}) = 0.0022144006. CONFIRMED (+0.002214).
- TB at 1e30 = 5.263494e14 = 0.5263 sqrt(x): CONFIRMED L-105031(f) slope 0.5263.
- Frozen x = 1e6: M_2 = 106.1986, M_3 = 39.3933, M_sc = 10.7443 — CONFIRMS
  L-105031(f)'s m_2 = 106.2, m_3 = 39.4, m_sc = 10.7 (threshold e* = 899,
  sliver 3289 of 3408 evens).
- Exact affine law at saturation (theta frozen): M_j(x) = sigma_j Delta2 log x + const,
  sigma_j = A_j/sqrt(j) - B_j/sqrt(j+1) + C_j(zeta(1/2) - sum_{m<=j+1} m^{-1/2}):
  sigma_2 = -1.623491, sigma_3 = -0.593570; slopes sigma_j*Delta2 = 30.0993 (j=2),
  11.0039 (j=3) — matches "30.1 log x" and "11.0 log x", and my computed
  increments are EXACTLY affine: 138.6026 per 2 decades (j=2, all three gaps),
  50.675 per 2 decades (j=3).

## Numerical honesty note (replay-relevant)

My first run had M_2(1e34) = 2030.72 (wrong by ~5): the expansion branch formed
H_exp(Y) - 4 sqrt(Y) with 4 sqrt(Y) ~ 4e17, a catastrophic float64 cancellation
(ulp ~ 64 per term). Fix: never form 4 sqrt(Y) in the expansion branch — use
H - 4 sqrt(Y) = zeta(1/2) log Y + zeta'(1/2) + E directly. After the fix all
values agree with the orchestrator's 40-dps computation to every displayed digit.
ANY replay fixture at x >= 1e30 must either use >= 40-dps arithmetic or the
cancellation-free restructuring; naive float64 on the raw margin formula loses
~3-16 absolute digits (terms ~ 4 sqrt(x)/d vs margin ~ 1e3).
