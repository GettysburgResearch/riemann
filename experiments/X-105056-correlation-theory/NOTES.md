# Lane M: Drift Mechanism PLAN
1. Read context: L-105053, O-105054, T-105051, X-105053 ANALYSIS + code.
2. Untruncated model g = mu*eta, DS zeta^{-1/2}: verify multiplicativity, g(p^k) values.
3. Derive Euler product for A_{a,b}(s) = sum_q g(qa)g(qb) q^{-s}, (a,b)=1: local factors.
4. Check convergence at s=1: diagonal series sum g(q)^2/q behaves like zeta(s)^{1/4}-ish -> divergent? compute exponent exactly.
5. If divergent, correlation constants need renormalization (ratio to diagonal); derive C_{a,b} as limit/Euler product.
6. Numerics: verify local factors + C_{a,b} vs direct sums.
7. Drift sum Sigma_drift over (a,b)=1, 1/4<a/b<4 with R kernel; convergence, compute, compare to O ~ -2.3.
8. Truncation transfer h_U vs g: correction structure, numeric test U in {10,21,46,100}.
9. Assemble O(X) = drift + Err decomposition; record honest caveats.
10. Final: STATEMENTS PROVED + numbers.

## Run 1 (model.py) CONFIRMED
- Identity f_p(x;alpha)=g_alpha*2F1(alpha-1/2,-1/2;alpha+1;x): err 2e-23. c_1=0 exactly => F_11 = zeta^{1/4} G, G conv Re s>1/2.
- G(1)=0.9184884, C_SD=G(1)/Gamma(5/4)=1.0133339. A_11(Q)/(C_SD (log Q)^{1/4}) = 1.0104 -> 1.0063 (Q=1e4->2e6). SD law verified.
- Factorization F_ab/F_11 = rho_ab(s): relerr 9e-6 (s=1.5), <6e-4 (s=1.25) [truncation-limited]. Ratio law at s=1: 0.5% match.
- SIGN LAW verified: sign rho = (-1)^{omega(ab)}. INVARIANCE: rho_{a,b} = varrho(ab), multiplicative in the product.
- EXACT second moment: int R v e^{v/2} dv = (8-6 sqrt2) log 2 = -0.336371... (closed form, was numeric-only). Proof: Phi(s)=int R e^{sv} dv = hatA_-(s)hatA_-(-s); Phi'(1/2) = hatA_-'(1/2) hatA_-(-1/2), hatA_-'(1/2)=2(1-2^{-1/2})log2, hatA_-(-1/2)=2(1-sqrt2).

## Run 2 (drift.py)
- Sabs(P) ~ (1.8 rising) * P/log^2 P: ABSOLUTE DIVERGENCE of naive drift sum confirmed (also proved via prime skeletons + PNT).
- SIGNED Sdrift(P): peaks +0.842 at P=4, then decays monotonically: 0.398(32), 0.274(64), 0.212(128), 0.150(256), 0.095(600) ~ P^{-0.4}-ish.
  Signed skeleton sum looks conditionally convergent to ~0 (or small >=0 limit) -- NOT to -2.3. Negativity is NOT low-torsion drift.

## Run 3 (trunc.py) + closed forms
- Elliptic forms verified 25 digits: diag=(2/pi)[2E-(1-m)K]; g-eta=(2/pi)E; eta-eta=(2/pi)K.
- D replays deposited table at X=1e3,1e4,1e5,1e6 (U=10,21,46,100). Sign law transfers 39/40 (exception (4,1), smallest |varrho|).
- Truncated ratios U-dependent, O(1)-off varrho => Xi_U correction real. O^hi(P) signed: positive at P<=8, negative by P=64 at all X.
- DEPOSIT DRAFT: DEPOSIT-M-drift-mechanism.md (T-M1..T-M8, C-M4, O-M6, L-M7). Convergent-drift mechanism REFUTED (T-M5);
  correlation law (log Q)^{1/4} with finite-product constants varrho(ab), sign (-1)^{omega(ab)}.
