# O-105056 — Pair-correlation Euler theory for the HHFE off-diagonal: exact skeleton constants, sign law, and refutation of the convergent-drift mechanism

Claim ID: `O-105056`
Status: **PROVED (T-M1..T-M3, T-M5, L-M7: exact/elementary; C-M4 modulo cited Selberg–Delange, EXTERNAL-CLASSICAL; T-M8 per fixed U) + LABELED DATA — RH not assumed, not claimed; gate HHFE102010 remains OPEN**
Created: 2026-08-23
Agent: claude (lane M, program A2; hostile-reviewed pre-deposit, FIX_FIRST findings applied)
Depends on: `L-103100`–`L-103102` @ PR #702 `89f995450977c3590aada0c1447a7e6af7fcd9ac`; `L-105053`, `O-105054`, `T-105051` @ `claude/riemann-proof-review-8nz34i`.
Replay: `experiments/X-105056-correlation-theory/` (model.py, drift.py, trunc.py; model_consts.json, drift_partial.json, trunc_results.json).
RH status: **unproved, not addressed**

Notation: eta(p^k) = C(2k,k)4^{-k} = (1/2)_k/k!; h_U = (mu 1_{>U}) * eta; g := mu * eta
(full Mobius, untruncated), Dirichlet series zeta(s)^{-1/2}; R = ratio-four kernel;
O = off-diagonal Gram sum, O = H - D exactly (deposited).

## T-M1 (untruncated model is multiplicative; local values). PROVED, elementary.
g is multiplicative with g(p^k) = (-1/2)_k/k! = (-1)^k binom(1/2,k): g(p) = -1/2,
g(p^2) = -1/8, g(p^3) = -1/16, g(p^4) = -5/128; g(p^k) < 0 for ALL k >= 1 and
|g(p^k)| ~ k^{-3/2}/(2 sqrt(pi)). [Local factor of zeta^{-1/2} is (1-p^{-s})^{1/2}.]

## T-M2 (exact Euler factorization of the pair correlation). PROVED.
For (a,b) = 1, Re s > 1:
  F_{a,b}(s) := sum_{q>=1} g(qa) g(qb) q^{-s} = prod_p f_p(s; v_p(a)+v_p(b)... )
factors over primes ((a,b)=1 means at each p at most one of the exponents is nonzero), with
  f_p(s; alpha) = sum_{j>=0} g(p^{j+alpha}) g(p^j) p^{-js}
                = g(p^alpha) * 2F1(alpha - 1/2, -1/2; alpha+1; p^{-s}).
Proof of the hypergeometric identity: g_{j+alpha} g_j = g_alpha * (alpha-1/2)_j (-1/2)_j
/ ((alpha+1)_j j!) by (-1/2)_{j+alpha} = (-1/2)_alpha (alpha-1/2)_j and (j+alpha)! =
alpha! (alpha+1)_j. QED. [Verified to 2e-23.]
Closed elliptic forms (parameter m = p^{-s}): diagonal alpha=0 factor
= (2/pi)[2E(m) - (1-m)K(m)]; also sum_j g_j eta_j m^j = (2/pi)E(m),
sum_j eta_j^2 m^j = (2/pi)K(m). [Verified to 25 digits.]
Hence, with the DIAGONAL series F_{1,1}(s) = zeta(s)^{1/4} G(s),
  G(s) = prod_p (1-p^{-s})^{1/4} 2F1(-1/2,-1/2;1;p^{-s})  (abs. conv. Re s > 1/2,
  since the log of each factor is O(p^{-2s}); the linear coefficient cancels exactly
  because g(p)^2 = 1/4),
we get the SKELETON CONSTANTS as a finite product depending only on n = ab:
  F_{a,b}(s) = varrho(ab; s) F_{1,1}(s),
  varrho(n; s) = prod_{p^alpha || n} r_p(alpha; s),
  r_p(alpha; s) = g(p^alpha) 2F1(alpha-1/2,-1/2;alpha+1;p^{-s}) / 2F1(-1/2,-1/2;1;p^{-s}).
INVARIANCE: varrho depends only on the product ab, not on the split (a,b).
Values at s=1: r_2(1) = -0.4129175, r_3(1) = -0.4406339, r_5(1) = -0.4636767,
r_p(1) -> -1/2 (p -> inf); G(1) = 0.9184884.
[Numerics: F_{a,b}/F_{1,1} vs varrho at s=1.5: rel. err <= 3e-5; s=1.25: <= 6e-4,
truncation-limited; 10 skeletons incl. prime powers.]

## T-M3 (sign law). PROVED.
For 0 < x < 1 and alpha >= 1, 2F1(alpha-1/2, -1/2; alpha+1; x) > 0 by the Euler
integral 2F1(-1/2, a; c; x) = [Gamma(c)/(Gamma(a)Gamma(c-a))] int_0^1 t^{a-1}
(1-t)^{c-a-1} (1-xt)^{1/2} dt with a = alpha - 1/2 > 0, c - a = 3/2 > 0; the diagonal
factor is >= 1 trivially. Hence sign r_p(alpha; s) = sign g(p^alpha) = -1 and
  sign varrho(ab; s) = (-1)^{omega(ab)}   (omega = number of distinct primes),
for every real s in (1/2, infty), every skeleton. A Liouville-like sign in omega, NOT Omega.

## C-M4 (correlation ratio law; Selberg–Delange, cited standard). 
Since F_{a,b} = varrho(ab;s) zeta^{1/4} G with varrho, G analytic and SD-admissible
in Re s > 1/2 (finite product resp. abs. conv. Euler product), Selberg–Delange
(Tenenbaum II.5) gives, for each fixed (a,b) = 1, as Q -> infty:
  A_{a,b}(Q) := sum_{q<=Q} g(qa)g(qb)/q = varrho(ab;1) * C_SD * (log Q)^{1/4} (1 + O(1/log Q)),
  C_SD = G(1)/Gamma(5/4) = 1.0133339.
THE CORRELATION IS NOT A CONSTANT: it grows like (log Q)^{1/4} — the branch exponent
is g(p)^2 = 1/4, answering the orchestrator's question (series DIVERGES at s = 1).
[Verified: A_{1,1}(Q)/(C_SD (log Q)^{1/4}) = 1.0104, 1.0081, 1.0066, 1.0063 at
Q = 1e4, 1e5, 1e6, 2e6; ratios A_{a,b}/A_{1,1} match varrho(ab;1) to ~0.5%.]

## T-M5 (REFUTATION of the convergent-drift mechanism). PROVED (uses PNT only).
The naive drift sum DIVERGES ABSOLUTELY:
  sum_{(a,b)=1, a != b, 1/4 < a/b < 4} |R(log(a/b))| (ab)^{-1/2} |varrho(ab;1)| = +infty.
Proof: restrict to prime skeletons (p, p'), p' in (1.05p, 1.35p): there
R >= R(log 1.35) = 0.755 > 0 (the interval avoids R's zero at v* = 3log2/(3+sqrt2)
= log 1.6024); |varrho(pp')| = |r_p(1) r_{p'}(1)| >= r_2(1)^2 > 0.17; each term
>= c/p; PNT gives >> p/log p primes p' in the window, so the p-block contributes
>> 1/log p, and sum_p 1/log p diverges. QED.
CONSEQUENCE: no absolutely convergent skeleton-constant "Sigma_drift" exists; the
measured O ~ -2.3 CANNOT be an absolutely convergent low-torsion drift sum. The
absolute skeleton mass to cutoff P grows ~ (1.1..1.8) P/log^2 P (measured, drift.py),
matching the divergence rate.

## O-M6 (signed skeleton sum; measured, labeled data).
S(P) := sum_{max(a,b)<=P} R(log a/b)(ab)^{-1/2} varrho(ab;1) (coprime, a != b):
+0.572 (P=2), peak +0.842 (P=4), then monotone decay: +0.398 (32), +0.274 (64),
+0.212 (128), +0.150 (256), +0.095 (600); ~ P^{-0.4} over the sampled range.
The signed sum appears CONDITIONALLY convergent (in max-order summation) to a small
limit near 0 — compatible with a skeleton-level echo of the kernel zero
(int R e^{+-v/2} dv = 0 kills the leading smooth-density term of the b-sum), but the
smooth-density calculus is NOT valid at this depth (it wrongly predicts growth);
no analytic value of lim S(P) is claimed.

## L-M7 (exact kernel second moment; closed form for a deposited numeric). PROVED.
  int_R R(v) e^{v/2} v dv = (8 - 6 sqrt 2) log 2 = -0.3363714163...
Proof: Phi(s) := int R(v) e^{sv} dv = hatA_-(s) hatA_-(-s) (autocorrelation);
Phi'(1/2) = hatA_-'(1/2) hatA_-(-1/2) since hatA_-(1/2) = 0; hatA_-'(1/2)
= 2(1 - 2^{-1/2}) log 2 (differentiate the vanishing factor), hatA_-(-1/2)
= 2(1 - sqrt 2). Product = -2 sqrt2 (sqrt2 - 1)^2 log 2 = (8 - 6 sqrt2) log 2. QED.
[Matches the deposited numeric -0.3364; quad check 1e-15.]

## T-M8 (truncation transfer: universality class is preserved per fixed U). PROVED per fixed U.
h_U = g - g_U^-, g_U^-(n) = sum_{d<=U, d|n} mu(d) eta(n/d) (finite sum). For fixed
(a,b) = 1 and fixed U, expanding F^{hh}_{a,b}(s) = sum_q h_U(qa)h_U(qb)q^{-s} into
gg, g-eta (cross), eta-eta pieces and reducing each d,d'-term by the substitution
q = (d/(d,b)) t to a shifted two-variable correlation, the local diagonal series are
  gg: 2F1(-1/2,-1/2;1;x) -> zeta^{1/4};  g-eta: (2/pi)E(x)-series 2F1(-1/2,1/2;1;x),
  linear coeff g(p)eta(p) = -1/4 -> zeta^{-1/4};  eta-eta: (2/pi)K, coeff +1/4 -> zeta^{1/4}.
Hence F^{hh}_{a,b}(s) = zeta(s)^{1/4}[varrho(ab;s)G(s) + Xi_U(a,b;s)]
+ zeta(s)^{-1/4} Psi_U(a,b;s) with Xi_U (from eta-eta) and Psi_U (from cross) FINITE
sums of SD-admissible Euler-type products: the truncated fiber correlations obey the
SAME (log Q)^{1/4} law with U-modified skeleton constants; the cross terms are
O((log Q)^{-1/4}), i.e. truncation changes constants, never the universality class.
NOT claimed: uniformity in U (the coupled regime U = X^{1/3}, Q ~ N/max(a,b) is not
covered by fixed-U SD asymptotics — honest gap, stated).
[Numerics, trunc.py, U in {10,21,46,100}: sign law transfers to A^h_{a,b}/A^h_{1,1}
in 38/40 skeleton-U cases (exceptions: (4,1) — smallest |varrho| = 0.0955 — violating at BOTH X = 1e4 (+0.0525) and X = 1e6 (+0.0144); hostile-review data correction of the earlier 39/40 count);
magnitudes are U-dependent and O(1)-off varrho (e.g. (2,1): -0.10..-0.23 vs -0.41),
consistent with Xi_U != 0; D replay-matches the deposited table at all four X.]

## Assembly (the honest decomposition; nothing beyond deposited strength claimed).
Exact and deposited: O(X) = -D(X) + H(X), D > 0 explicit and subpower (L-103101),
H = (1/2pi) int w |P|^2 >= 0. The PROVABLY SIGNED main term of O is -D(X); the
fluctuation object is H itself, and bounding H is the gate — not claimed.
What this lane adds structurally:
(i) the exact skeleton ledger O = sum_{(a,b)=1, a!=b} R(log a/b)(ab)^{-1/2} A^h_{a,b},
with the untruncated law A ~ varrho(ab) C_SD (log Q)^{1/4}: EVERY FIXED skeleton class
is polylog-small; power-scale mass is carried only by the ~N-sized skeleton COUNT
(wall-consistent, O-105054);
(ii) the measured skeleton-cumulative O^hi(P) at X = 1e3..1e6 starts POSITIVE
(+0.44, +0.73 at P = 2, 4, X=1e6 — same sign as, and size within a factor ~2 of, the model's S(P) times the
A^h_{1,1} scale ~ 1.6) and turns negative only as P grows into the core
(-0.89 at P = 64, X = 1e6): the negativity of O is NOT low-torsion drift; it
accumulates in the near-coprime core, exactly where L-105053 localizes the gate;
(iii) T-M5 closes the door on any "convergent drift constant" explanation; with
O-M6 the surviving mechanism-shape is: smooth multiplicative skeleton model
conditionally near 0, negativity = -D + (H small), H's smallness = gate strength.
RH not addressed. No unconditional bound on H or Err is claimed anywhere above.

## Falsifiers
Any skeleton with sign varrho != (-1)^{omega(ab)} (breaks T-M3); a numerically
convergent A_{a,b}(Q) (breaks C-M4); absolute convergence of the drift sum under
any summation order (breaks T-M5); int R v e^{v/2} dv != (8-6 sqrt2) log 2;
a (log Q)^{beta} law with beta != 1/4 for truncated fibers at fixed U (breaks T-M8).
