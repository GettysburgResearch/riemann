# L-16216 — Dunster's uniform PSWF asymptotics cover the complete polylogarithmic frame

Claim ID: `L-16216`  
Status: **PROVED PRIMARY-SOURCE UNIFORMITY TRANSFER; CCM NORMALIZATION/ALIAS GATES REMAIN**  
Authoring agent: `gpt56-pro-09-h`  
Created: 2026-07-31  
Depends on: Dunster, *Asymptotics of Prolate Spheroidal Wave Functions*, arXiv:1601.00699, Section 6; `L-16213`; the exact scale relation `gamma=2 pi lambda^2` in CCM equation (7.9)  
Scope: the growing-mode uniformity clauses in `L-16212/L-16215/T-16204`

## 1. The apparent growing-mode problem

The positive prolate route uses the even Fourier-prolate indices

\[
 \mathcal I_\lambda
 =\{0,4,8,\ldots,4(M_\lambda+1)\},
 \qquad
 M_\lambda=O((\log\lambda)^2).                           \tag{L-16216.1}
\]

The CCM prolate parameter is exactly

\[
 \boxed{\gamma_\lambda=2\pi\lambda^2.}                  \tag{L-16216.2}
\]

Earlier claims correctly observed that a theorem proved only for each fixed
mode cannot automatically be used on the whole growing packet. The primary
Dunster theorem, however, is substantially more uniform than a fixed-mode
statement.

## 2. Dunster's actual uniform range

Fix `delta in (0,1)`. The summary in Section 6 of Dunster states that the
angular and radial asymptotic results are uniformly valid as `gamma->infinity`
for bounded order `m` and integer degree `n` satisfying

\[
 0\le m\le n\le {2\over\pi}\gamma(1-\delta).             \tag{L-16216.3}
\]

For the present order-zero packet, `m=0`. From (L-16216.1)--(L-16216.2),

\[
 {\max\mathcal I_\lambda\over\gamma_\lambda}
 =O\!\left({(\log\lambda)^2\over\lambda^2}\right)
 \longrightarrow0.                                      \tag{L-16216.4}
\]

Consequently, for every fixed `delta in (0,1)`, all modes in
`mathcal I_lambda` satisfy (L-16216.3) for sufficiently large `lambda`.

Thus:

\[
 \boxed{
 \text{Dunster's uniform radial and angular PSWF estimates apply
 simultaneously to every mode in }\mathcal I_\lambda.}  \tag{L-16216.5}
\]

The growing window `O(log^2 lambda)` is not close to the boundary of Dunster's
range; it occupies a vanishing fraction of it.

## 3. Uniform radial approximation

In Dunster's notation, the radial PSWF has the uniform approximation

\[
 \operatorname{Ps}_n^m(x,\gamma^2)
 =\mathcal A_{n,m,\gamma}(x)
 \left[J_m(\gamma\xi(x))+O(\gamma^{-1})\operatorname{env}J_m(\gamma\xi(x))\right]
 \tag{L-16216.6}
\]

for `1<x<infinity`, with the normalization factors `p_n^m(gamma)` and
`q_n^m(gamma)` given explicitly in equations (6.6)--(6.7). By (L-16216.5),
the error constant is uniform over the complete packet (L-16216.1), after one
fixed `delta` is chosen.

The angular approximations and the implicit separation-parameter equation
(6.4) have the same mode uniformity. Near the angular endpoint, the Bessel form
(6.8) is uniform; in the interior, the parabolic-cylinder form (6.9) is uniform.

This does not by itself identify the CCM-normalized leakage profile, but it
removes `n`-uniformity as a separate asymptotic obstruction.

## 4. Matrix accumulation lemma

Let `Y` be a Hilbert space and let

\[
 \phi_{k,\lambda},\phi^0_{k,\lambda}\in Y,
 \qquad1\le k\le m_\lambda,                              \tag{L-16216.7}
\]

be actual and leading profile columns. Let `Phi_lambda,Phi_lambda^0` be their
synthesis maps from `C^(m_lambda)` to `Y`. Suppose

\[
 \|\phi_{k,\lambda}-\phi^0_{k,\lambda}\|_Y
 \le\varepsilon_\lambda                                 \tag{L-16216.8}
\]

uniformly in `k`, and

\[
 \|\phi^0_{k,\lambda}\|_Y\le B.                         \tag{L-16216.9}
\]

Then

\[
 \boxed{
 \|\Phi_\lambda-\Phi_\lambda^0\|_{\rm op}
 \le\sqrt{m_\lambda}\,\varepsilon_\lambda,}             \tag{L-16216.10}
\]

and

\[
 \boxed{
 \left\|
 \Phi_\lambda^*\Phi_\lambda
 - (\Phi_\lambda^0)^*\Phi_\lambda^0
 \right\|_{\rm op}
 \le
 2B m_\lambda\varepsilon_\lambda
 +m_\lambda\varepsilon_\lambda^2.}                      \tag{L-16216.11}
\]

### Proof

For `c in C^(m_lambda)`, Cauchy--Schwarz gives

\[
 \left\|\sum_kc_k(\phi_k-\phi_k^0)\right\|
 \le\varepsilon_\lambda\sum_k|c_k|
 \le\sqrt{m_\lambda}\varepsilon_\lambda\|c\|_2,
\]

which proves (L-16216.10). The column bound gives

\[
 \|\Phi_\lambda^0\|_{\rm op}\le B\sqrt{m_\lambda}.
\]

Expand

\[
 \Phi^*\Phi-(\Phi^0)^*\Phi^0
 = (\Phi-\Phi^0)^*\Phi^0
  +(\Phi^0)^*(\Phi-\Phi^0)
  +(\Phi-\Phi^0)^*(\Phi-\Phi^0)
\]

and use (L-16216.10). QED.

If the leading profile Gram already has a dimension-free upper bound, one may
replace `B sqrt(m_lambda)` above by that synthesis bound and improve the first
term to `O(sqrt(m_lambda) epsilon_lambda)`.

## 5. Dunster errors are collectively negligible

For the radial error in (L-16216.6), take

\[
 \varepsilon_\lambda=O(\gamma_\lambda^{-1}).             \tag{L-16216.12}
\]

With

\[
 m_\lambda=O((\log\lambda)^2),
 \qquad
 \gamma_\lambda=2\pi\lambda^2,                          \tag{L-16216.13}
\]

(L-16216.11) gives

\[
 \boxed{
 m_\lambda\varepsilon_\lambda
 =O\!\left({(\log\lambda)^2\over\lambda^2}\right)
 \longrightarrow0.}                                     \tag{L-16216.14}
\]

The weaker angular endpoint error `O(gamma^(-2/3) log gamma)` also satisfies

\[
 m_\lambda\gamma_\lambda^{-2/3}\log\gamma_\lambda
 =O\!\left({(\log\lambda)^3\over\lambda^{4/3}}\right)
 \longrightarrow0.                                      \tag{L-16216.15}
\]

More generally, every fixed polynomial in packet dimension and frame
condition number is absorbed by any fixed positive power of `gamma_lambda`,
because `m_lambda` and the frame condition number in `L-16215` are
polylogarithmic.

Therefore no hidden `m_lambda` accumulation can destroy the published PSWF
asymptotic errors on the required diagonal.

## 6. Consequences for the current gate list

This closes one previously open clause in the positive-frame program:

1. **Mode uniformity:** closed by Dunster's range and (L-16216.4).
2. **Accumulation over the growing frame:** closed by (L-16216.10)--(L-16216.15).

The load-bearing remaining source-level obligations are narrower:

1. match Dunster's angular/radial normalizations `p_n^0,q_n^0` to the exact
   CCM `L2` normalization and Fourier eigenvalue `chi_n(lambda)`;
2. derive the uniform concentration-defect ratios used in `L-16215` from that
   normalization;
3. propagate the radial formulas through the complete arithmetic Poisson sum,
   retaining every nonstationary alias endpoint;
4. prove the global fold-variation and horizontal-strip budgets of `L-16210`;
5. transport the resulting profile Gram through the exact consecutive-triple
   radical repair.

The phrase “uniform prolate asymptotics on `n<=O(log^2 lambda)`” should no
longer be listed as an independent missing theorem. The primary source already
supplies a much larger uniform degree window.

## 7. Proof boundary

- The range comparison and matrix accumulation estimates are exact.
- Dunster's error orders and uniform degree range are imported from the primary
  source.
- The CCM-to-Dunster normalization and the concentration-eigenvalue identity
  are not supplied by this lemma.
- The arithmetic alias/fold profile theorem remains open.
- No RH proof is claimed at this stage.
