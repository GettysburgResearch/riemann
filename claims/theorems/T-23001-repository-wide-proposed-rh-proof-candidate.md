# T-23001 — Repository-wide proposed RH proof candidate

Claim ID: `T-23001`  
Title: Dyadic screw renormalization plus a critical signed-correlation estimate implies the Riemann Hypothesis  
Status: **PROPOSED PROOF CANDIDATE — GAP/BLOCKED AT `L-23002`; RH IS NOT CLAIMED PROVED**  
Authoring agent: `gpt56-pro-09-o`  
Created: 2026-08-07  
Purpose: one review-ready proof spine consolidating the repository's global work without converting an open arithmetic lemma into a theorem

## 1. Frozen source snapshot

This candidate was assembled from the following exact branch snapshots:

| Route | Frozen source |
|---|---|
| square screw / critical sampling | PR #202, head `946721e3ef90cfa4070cb69c3a6367fe73119c22` |
| square-support D-0001 coordinate | PR #208, head `23076476739340c4e357c55cb3a31994bac755d3` |
| terminal-prime / prime-only Hardy energy | PR #216, head `b76eef1b769584aa9d66d082bfc6634126f986a2` |
| completed annihilator / Brownian variance defect | PR #217, head `61c6f1129eb2848ce30750ec51c257945a7351c7` |
| Haar, r-adic, transport, and real-axis hierarchy | PR #218, head `5fade63daa279fe6003b66f3763ca3bf05fd912d` |
| prime-power convex polygon | PR #219, head `2ff77e656fa9f002248afbc4bd064f23491e9766` |
| signed semiprime dispersion | PR #222, head `bd2a1ce27dea41d32f53688609385cbd38c1559a` |
| semiprime H1 / vertical pole tomography | PR #224, head `ca40331114e74b57c1a805a0f1b1b008e70c7404` |
| analytic-totient critical energy | PR #226, head `53f2cba370fa518d5d12488b5b9948c1826bba88` |

Later mutable heads do not inherit the statements below automatically.

## 2. The screw function

Use the Nakamura--Suzuki normalization

\[
 \Psi(t)=-g_\zeta(t)
\]

and its unilateral transform

\[
 \boxed{
 \int_0^\infty\Psi(t)e^{izt}\,dt
 =-{1\over z^2}{\xi'\over\xi}\left({1\over2}-iz\right),
 \qquad \operatorname{Im}z>{1\over2}.}
 \tag{T-23001.1}
\]

For an integer `r>=2`, define

\[
 \boxed{
 \mathcal D_r(t)=r^2\Psi(t)-\Psi(rt).}
 \tag{T-23001.2}
\]

Under RH, the paired zero expansion gives

\[
 \mathcal D_r(t)
 =2\sum_{\gamma>0}{m_\gamma\over\gamma^2}
 \left[r^2(1-\cos\gamma t)-(1-\cos r\gamma t)\right]
 \ge0,
 \tag{T-23001.3}
\]

because `|sin(rx)|<=r|sin x|`. The Fejer--Gram factorization on PR #218
makes (T-23001.3) a finite sum of explicit screw squares.

## 3. Pole exposure

The transform of (T-23001.2) is

\[
 \boxed{
 \int_0^\infty\mathcal D_r(t)e^{izt}\,dt
 ={r\over z^2}
 \left[
  {\xi'\over\xi}\left({1\over2}-{iz\over r}\right)
  -r{\xi'\over\xi}\left({1\over2}-iz\right)
 \right].}
 \tag{T-23001.4}
\]

Suppose the bracket is holomorphic in `Im z>0`. If

\[
 \rho={1\over2}+w,
 \qquad \operatorname{Re}w>0,
\]

is a zero of multiplicity `m`, the pole at `z=iw` can cancel only if

\[
 {1\over2}+{w\over r}
\]

is also a zero of the same multiplicity. Iteration gives distinct zeros
converging to `1/2`, impossible for the nonzero entire function `xi`.
Therefore holomorphy of (T-23001.4) in the complete upper half-plane implies RH.

The field-separated pin of the later PR #218 continuation gives an alternate
exposure mechanism: one arbitrarily small coefficient outside the base
coefficient field makes every parent residue nonzero without a descendant
argument. The present proof spine does not require that strengthening.

## 4. Landau lower-envelope transfer

The exact prime/Lerch formula gives

\[
 |\Psi'(t)|\ll(1+t)e^{t/2}
\]

between prime knots, and hence

\[
 |\mathcal D_r'(t)|\ll_r(1+t)e^{rt/2}.
 \tag{T-23001.5}
\]

If, for every `epsilon>0`,

\[
 \mathcal D_r(t)
 \ge-C_\varepsilon(1+t)^{B_\varepsilon}e^{\varepsilon t}
 \tag{T-23001.6}
\]

eventually, add a positive exponential-polynomial and a compact correction to
make a nonnegative function. Landau's one-sign theorem forces its Laplace
abscissa to be a singularity on the positive real Laplace axis. The meromorphic
right side of (T-23001.4) has no such real-axis singularity. Therefore its
abscissa is at most `epsilon`; letting `epsilon` decrease to zero gives
holomorphy in `Im z>0`, and Section 3 gives RH.

At the critical mesh

\[
 t_n={2\log n\over r},
\]

one has

\[
 t_{n+1}-t_n=O(n^{-1})=O(e^{-rt_n/2}).
\]

Thus sample-to-continuum interpolation costs only a polynomial. Subject to the
independent review of this Landau argument, the proposed criterion is

\[
 \boxed{
 \mathrm{RH}
 \iff
 \bigl(-\mathcal D_r(2\log n/r)\bigr)_+=n^{o(1)}.}
 \tag{T-23001.7}
\]

## 5. Dyadic first-knot renormalization

Set

\[
 a=\log2,
 \qquad
 I_r=\left[a,a+{a\over r}\right],
 \qquad
 J_r=[ra,(r+1)a].
\]

The physical cells `J_r` tile the complete tail and correspond to the dyadic
prime blocks

\[
 [2^r,2^{r+1}].
\]

The small-scale ramp on `I_r` contains only `q=2`. Let

\[
 a_2={\log2\over\sqrt2}
\]

and define

\[
 \widetilde{\mathcal D}_r(t)
 =\mathcal D_r(t)+r^2a_2(t-a).
 \tag{T-23001.8}
\]

The added term is nonnegative and at most `O(r)`. It cancels the small-scale
`q=2` ramp exactly. Writing

\[
 \Psi(T)=F(T)-G(T),
 \qquad
 G(T)=\sum_q{\Lambda(q)\over\sqrt q}(T-\log q)_+,
\]

and

\[
 H_r(T)=F(T)-r^2F(T/r),
\]

one has on `J_r`

\[
 \boxed{
 \widetilde{\mathcal D}_r(T/r)=G(T)-H_r(T).}
 \tag{T-23001.9}
\]

Every remaining prime coefficient is nonnegative.

## 6. Finite knot reduction

The exact curvature formula is

\[
 F''(t)=e^{t/2}-{e^{-5t/2}\over1-e^{-2t}},
\]

with

\[
 F'''(t)>0.
\]

Thus `F''` is strictly increasing and

\[
 H_r''(T)=F''(T)-F''(T/r)>0.
\]

Between consecutive prime-power knots, `G` is affine, so

\[
 (G-H_r)''=-H_r''<0.
\]

Therefore the minimum on a dyadic block is attained at the two endpoints or at
a prime-power knot. Each level is a finite, complete arithmetic object.

## 7. Exact transport-minus-curvature identity

At a prime-power knot `T_j=log q_j`, define

\[
 A_j=\sum_{q\le q_j}{\Lambda(q)\over\sqrt q},
 \qquad
 B_j=\sum_{q\le q_j}{\Lambda(q)\log q\over\sqrt q},
\]

\[
 \tau_{r,j}=(H_r')^{-1}(A_j),
 \qquad
 P_{r,j}=H_r^*(A_j)-B_j.
\]

Fenchel duality gives the exact identity

\[
 \boxed{
 \widetilde{\mathcal D}_r(T_j/r)
 =P_{r,j}-D_{H_r}(T_j,\tau_{r,j}).}
 \tag{T-23001.10}
\]

The reserve evolves by the equal-mass transport ledger

\[
 \boxed{
 P_{r,q}-P_{r,p}
 =\int_{A_p}^{A_q}
   \left[(H_r')^{-1}(A)-\nu_{\rm pp}(A)\right]dA.}
 \tag{T-23001.11}
\]

If

\[
 m_r=\inf_{J_r}H_r''>0,
\]

then

\[
 \boxed{
 D_{H_r}(T_j,\tau_{r,j})
 \le{[A_j-H_r'(T_j)]^2\over2m_r}.}
 \tag{T-23001.12}
\]

Equations (T-23001.10)--(T-23001.12) are exact. They identify the required sign
as a one-sided transport reserve paying a curvature-normalized centered
prime-mass square.

## 8. The proposed closing lemma

Invoke `L-23002`:

\[
 \max_{T\in\mathcal K_r}
 \bigl(-\widetilde{\mathcal D}_r(T/r)\bigr)_+
 \le C_\varepsilon e^{\varepsilon r},
 \tag{T-23001.13}
\]

where `mathcal K_r` consists of the two endpoints and every prime-power knot in
`J_r`.

The repository's exact dictionaries identify (T-23001.13) with the same critical
signed-correlation gate appearing as:

- the common-cell balanced semiprime estimate of PRs #216/#222;
- the locally uniform vertical prime-energy estimate of PR #224;
- the local-to-Bohr analytic-totient estimate of PR #226;
- the one-sided Selberg transport inequality of `L-23002`.

`L-23001` supplies a positive Hankel adjoint inverse for every real exponential,
but `R-23001` proves that the naive compact stop-loss adjoint is not positive
Hankel. Thus the remaining step is a genuine signed near-resonance theorem, not
a missing ODE manipulation.

## 9. Completion of the proof conditional on `L-23002`

Assume (T-23001.13). By the knot reduction, the same lower envelope holds on the
whole dyadic cell. Removing the correction in (T-23001.8) costs only `O(r)`, so

\[
 \mathcal D_r(t)\ge-e^{o(r)}
 \qquad(t\in I_r).
\]

For every sufficiently large `T`, choose the unique `r` with

\[
 T\in[ra,(r+1)a]
\]

and put `t=T/r`. Then

\[
 \Psi(T)
 \le r^2\Psi(t)+e^{o(r)}=e^{o(T)},
\]

because `t` remains in a fixed compact interval and `r asymp T`.
The upper-envelope version of Landau's theorem applied to `-Psi` makes
`xi'/xi` holomorphic to the right of the critical line. Functional-equation
symmetry gives RH.

Equivalently, use the lower-envelope form for the pinned or r-adic defect and
the pole-exposure argument of Sections 3--4.

Thus

\[
 \boxed{
 L\text{-23002}\quad\Longrightarrow\quad\mathrm{RH}.}
 \tag{T-23001.14}
\]

## 10. Independent consistency checks

The repository provides several non-equivalent-looking checks on the same final
conclusion:

1. `T-21702` expresses the off-line defect as a strictly positive sum
   \[
   4\sum_{\delta>0,\gamma>0}
   m_\rho{\gamma^2-\delta^2\over(\gamma^2+\delta^2)^2};
   \]
2. PR #217 identifies this with a Brownian/gamma-perpetuity variance defect;
3. PR #208 identifies the square screw as the constant D-0001 coordinate;
4. PR #219 identifies the screw depth with a prime-prefix convex-polygon deficit;
5. PR #216 identifies the rightmost-zero exponent with a positive prime-pair
   Hardy energy;
6. PR #226 identifies the same exponent with a positive analytic-totient second
   moment.

These checks support the normalization map. None proves `L-23002`.

## 11. Why this is not yet a proof of RH

The proof above has one explicit unproved input: `L-23002`. The repository has
closed its diagonal, exact-resonance, far-frequency, finite-algebra, and
normalization components, but not the critical signed near-resonance estimate.

It would be mathematically incorrect to replace `L-23002` by:

- an entrywise absolute-value bound;
- a standard large-sieve estimate with its extra critical power;
- a finite positive computation;
- a density-one or almost-every-line vertical estimate;
- the compact stop-loss Hankel shortcut refuted by `R-23001`;
- an RH-conditional zero representation.

Accordingly, this file is a **review-ready proposed proof spine with one boxed
open lemma**, not a public proof announcement.

## 12. Reviewer checklist

1. Reconstruct the screw/Laplace normalization and every factor of `r`.
2. Audit the Landau one-sign correction and sample-to-continuum transfer.
3. Check the first-knot correction and endpoint stitching.
4. Check the Legendre/Bregman orientation and inverse-derivative domains.
5. Independently normalize the Selberg equation used in `L-23001`.
6. Verify the exact-resonance/Jordan and semiprime dictionaries.
7. Attack `L-23002` directly; do not infer it from any finite ladder.
