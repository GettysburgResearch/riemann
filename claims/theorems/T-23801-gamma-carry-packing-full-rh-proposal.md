# T-23801 — Gamma–carry packing full proposal for the Riemann hypothesis

Claim ID: `T-23801`  
Title: Finite Gamma–carry minorants give a nonnegative entropy packing, the sharp prime ramp, and RH  
Status: **FULL PROPOSED PROOF — FGCM IS THE SINGLE LOAD-BEARING REVIEW HINGE**  
Authoring agent: `gpt56-pro-09-u`  
Created: 2026-08-07  
Issue: #238  
Dependencies: `L-23801`--`L-23807`; square-screw formula `T-19801`; upper-envelope Landau transfer in `T-20205`  
Scope: complete elementary-facing RH proposal; not an accepted proof until FGCM is proved

## 1. Proof spine

The proposed proof is

```text
exact average carry matrix
-> continuum carry probability law
-> finite nonnegative Gamma-carry convolution minorants
-> explicit nonnegative finite carry packing
-> binomial entropy mass 4 sqrt(X)-X^o(1)
-> sharp lower bound for the complete prime-power ramp
-> subexponential upper envelope for the zeta screw function
-> Landau pole exclusion
-> RH.
```

Every arrow after the finite minorant theorem is proved exactly in the cited
files. The sole arithmetic hinge is `FGCM` from `L-23807`: construct
nonnegative finite-horizon profiles `b_X` satisfying the convolution and sharp
mass budgets (L-23807.4)--(L-23807.7).

The global Gamma–carry factorization

\[
 a(t)\ge0\quad(t\ge0)
 \tag{T-23801.1}
\]

for the explicit Möbius–Riesz density in `L-23805.7` is a canonical stronger
certificate, not a mandatory strengthening of the final theorem.

## 2. Exact finite carry factorization

For

\[
 G_n={1\over n+1}\sum_{j=0}^n\log\binom nj,
\]

`L-23801` proves

\[
 G_n=\sum_{q=p^k\le n}\Lambda(q)\beta_{nq},
 \tag{T-23801.2}
\]

where every `beta_(nq)>=0`. It also proves

\[
 G_n\ge {n\over2}-C\log(n+1).
 \tag{T-23801.3}
\]

Thus any nonnegative packing beneath the carry columns immediately gives a
lower bound for the complete prime-power ramp.

## 3. The canonical global factor

Let

\[
 p(t)=2e^{-t}K(e^t)
\]

be the explicit carry-law density of `L-23804`, and let

\[
 g(t)={t\over4}e^{-t/2}
\]

be the `Gamma(2,1/2)` density. The quotient of their Laplace transforms is

\[
 A(s)={(s+1)(s+2)
  \over8s(s+\tfrac12)^2\zeta(s+1)}.
 \tag{T-23801.4}
\]

Its physical inverse is

\[
 \boxed{
 \begin{aligned}
 a(t)=\sum_{n\le e^t}{\mu(n)\over n}
 \bigg[&1-{7\over8}e^{-(t-\log n)/2}\\
       &-{3\over16}(t-\log n)e^{-(t-\log n)/2}
 \bigg].
 \end{aligned}}
 \tag{T-23801.5}
\]

If this density is nonnegative with the declared subcritical tail moments, then
`L-23806` supplies `FGCM` by truncation. More generally, `FGCM` permits
level-dependent positive profiles with slack and therefore does not require a
global convolution factor.

## 4. Explicit finite packing

Assume `FGCM` at level `X`, with certificate `b_X`. Define

\[
 d_X(n)=8\sqrt X\int_n^{n+1}
 y^{-2}b_X(\log(X/y))dy,
 \qquad2\le n<X,
 \tag{T-23801.6}
\]

and `d_X(X)=0`. `L-23807` proves exactly

\[
 d_X(n)\ge0,
 \tag{T-23801.7}
\]

and

\[
 \sum_{n=q}^Xd_X(n)\beta_{nq}
 \le {1\over\sqrt q}\log{X\over q}
 \qquad(2\le q\le X).
 \tag{T-23801.8}
\]

The proof uses the exact identity

\[
 \beta_{nq}=K_-((n+1)/q)
\]

and the fact that the endpoint sample is the minimum of the continuum carry
kernel on the complete unit cell. No Riemann-sum asymptotic or sign-changing
correction appears.

## 5. Sharp entropy lower bound

The two `FGCM` mass budgets give

\[
 \boxed{
 \sum_{n=2}^Xd_X(n)G_n
 \ge4\sqrt X-X^{o(1)}.}
 \tag{T-23801.9}
\]

Combining (T-23801.2), (T-23801.7), and (T-23801.8),

\[
 \boxed{
 \mathcal P(X)
 :=\sum_{q=p^k\le X}{\Lambda(q)\over\sqrt q}
 \log{X\over q}
 \ge4\sqrt X-X^{o(1)}.}
 \tag{T-23801.10}
\]

The constant four is exact. It is not obtained from the prime-number theorem:
it is the product of the continuum carry mass `1/2`, the shape-two gamma
normalization suggested by `L-23805`, and the entropy main term `n/2`.

## 6. Square-screw upper envelope

Set

\[
 X=N^2.
\]

The exact square-screw scalar of `T-19801` is

\[
 \begin{aligned}
 \mathscr S(N)={}&4(N+N^{-1}-2)-\mathcal P(N^2)\\
 &+\log N\,[\psi(1/4)-\log\pi]\\
 &-{1\over4}
 \left[N^{-1}\Phi(N^{-4},2,1/4)-\Phi(1,2,1/4)\right].
 \end{aligned}
 \tag{T-23801.11}
\]

It equals the zeta screw function at the square sample:

\[
 \mathscr S(N)=\Psi(2\log N).
 \tag{T-23801.12}
\]

Equation (T-23801.10) gives

\[
 \boxed{
 \Psi(2\log N)\le N^{o(1)}.}
 \tag{T-23801.13}
\]

The remaining gamma/Lerch terms are logarithmic or bounded and are absorbed by
the subpolynomial envelope.

## 7. Passage from samples to the half-line

The unconditional explicit-formula derivative bound is

\[
 |\Psi'(t)|\le C(1+t)^A e^{t/2}.
 \tag{T-23801.14}
\]

Adjacent square samples satisfy

\[
 2\log(N+1)-2\log N\asymp N^{-1}=e^{-t/2}.
 \tag{T-23801.15}
\]

Therefore (T-23801.13) and the mean-value theorem give, for every `delta>0`,

\[
 \boxed{
 \Psi(t)\le C_\delta(1+t)^{B_\delta}e^{\delta t}
 \qquad(t\ge0).}
 \tag{T-23801.16}
\]

This is the upper-envelope counterpart of the square-sampling theorem.

## 8. Landau pole exclusion

The one-sided Fourier--Laplace identity is

\[
 \int_0^\infty\Psi(t)e^{izt}dt
 =-{1\over z^2}{\xi'\over\xi}(1/2-iz).
 \tag{T-23801.17}
\]

Fix `delta>0`. Add a sufficiently large positive polynomial multiple of
`e^(delta t)` and one compactly supported correction so that

\[
 H_\delta(t)=P_\delta(t)e^{\delta t}-\Psi(t)
\]

is nonnegative on the full half-line. Landau's one-sign theorem forces its
Laplace convergence boundary to be a genuine singularity unless the meromorphic
continuation is holomorphic farther left. There is no positive-real Xi zero, so
(T-23801.17) excludes every zero with

\[
 \Re\rho>{1\over2}+\delta.
\]

Letting `delta` tend to zero and applying functional-equation symmetry yields

\[
 \boxed{\mathrm{RH}.}
 \tag{T-23801.18}
\]

This is the same exact upper-envelope transfer isolated in `T-20205`; no zero
ordinate or finite verified-height hypothesis enters.

## 9. Review firewall

A reviewer should attack the proposal in the following order.

1. Verify the carry Mellin identity `L-23804.4` and probability law.
2. Verify the finite minorant-to-packing theorem `L-23807`.
3. Attack `FGCM`: every convolution reset, mass deficit, and exponential first
   moment must be source bound.
4. If global GCF is proposed as the producer, verify the quotient and physical
   density `L-23805.4`--`L-23805.7` and its tail moments.
5. Confirm the endpoint sampling inequality `beta<=K` in `L-23804.3`.
6. Check the square-screw normalization and upper-envelope Landau orientation.
7. Require the first fixed-ratio Mertens/Farey cell as a mutation: a proof that
   forgets Möbius signs or takes total variation before recombination must fail.

## 10. Relationship to the balanced Type-II core

The canonical transform (T-23801.4) contains the same reciprocal-zeta channel as
the balanced Möbius packets in PRs #158/#233 and the first Farey/Mertens cell in
PR #229. `FGCM` is the weakest positive-minorant projection of that core found
in this pass.

Its potential advantage is compression: all Type-I and endpoint bookkeeping has
collapsed into one scalar convolution budget. A proof may use a direct finite
LP recurrence, quotient-layer recombination, reflected Selberg, or BTP without
proving positivity of every packet coordinate.

## 11. Exact status

```text
carry matrix and entropy identity             proposed exact
continuum carry Mellin/probability law         proposed exact
Gamma/carry quotient and density              proposed exact
finite Gamma-carry minorants FGCM              OPEN / LOAD BEARING
FGCM -> exact finite sharp packing             proposed complete
sharp packing -> screw upper envelope -> RH    proposed complete
accepted proof of RH                           NO
```

This is a full, unmistakable proof proposal with one explicitly isolated finite
positive-minorant theorem. It should be reviewed as a candidate completion, not
cited as an established proof until FGCM survives independent proof.
