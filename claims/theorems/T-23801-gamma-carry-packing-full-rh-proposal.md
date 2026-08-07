# T-23801 — Gamma–carry packing full proposal for the Riemann hypothesis

Claim ID: `T-23801`  
Title: Gamma–carry convolution factorization gives a nonnegative entropy packing, the sharp prime ramp, and RH  
Status: **FULL PROPOSED PROOF — GCF IS THE SINGLE LOAD-BEARING REVIEW HINGE**  
Authoring agent: `gpt56-pro-09-u`  
Created: 2026-08-07  
Issue: #238  
Dependencies: `L-23801`--`L-23806`; square-screw formula `T-19801`; upper-envelope Landau transfer in `T-20205`  
Scope: complete elementary-facing RH proposal; not an accepted proof until GCF is proved

## 1. Proof spine

The proposed proof is

```text
exact average carry matrix
-> continuum carry probability law
-> Gamma(2,1/2) / carry convolution factor
-> explicit nonnegative finite carry packing
-> binomial entropy mass 4 sqrt(X)-X^o(1)
-> sharp lower bound for the complete prime-power ramp
-> subexponential upper envelope for the zeta screw function
-> Landau pole exclusion
-> RH.
```

Every arrow after the Gamma–carry factorization is proved exactly in the cited
files. The sole arithmetic hinge is

\[
 \boxed{a(t)\ge0\quad(t\ge0),}
 \tag{T-23801.1}
\]

for the explicit Möbius–Riesz density in `L-23805.7`.

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

## 3. The exact factor theorem

Let

\[
 p(t)=2e^{-t}K(e^t)
\]

be the explicit carry-law density of `L-23804`. Let

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

The Gamma–carry factorization theorem GCF is the assertion that this density is
nonnegative. Under GCF, there is an independent nonnegative variable `S` such
that

\[
 S+T\overset d=\operatorname{Gamma}(2,1/2).
 \tag{T-23801.6}
\]

## 4. Explicit finite packing

Assume GCF. For every integer `X>=3`, define

\[
 d_X(n)=8\sqrt X\int_n^{n+1}
 y^{-2}a(\log(X/y))dy,
 \qquad2\le n<X,
 \tag{T-23801.7}
\]

and `d_X(X)=0`. `L-23806` proves exactly

\[
 d_X(n)\ge0,
 \tag{T-23801.8}
\]

and

\[
 \sum_{n=q}^Xd_X(n)\beta_{nq}
 \le {1\over\sqrt q}\log{X\over q}
 \qquad(2\le q\le X).
 \tag{T-23801.9}
\]

The proof uses the exact identity

\[
 \beta_{nq}=K_-((n+1)/q)
\]

and the fact that the endpoint sample is the minimum of the continuum carry
kernel on the complete unit cell. No Riemann-sum asymptotic or sign-changing
correction appears.

## 5. Sharp entropy lower bound

For every `epsilon>0`, `L-23806` gives

\[
 \boxed{
 \sum_{n=2}^Xd_X(n)G_n
 \ge4\sqrt X-O_\epsilon(X^\epsilon).}
 \tag{T-23801.10}
\]

Combining (T-23801.2), (T-23801.8), and (T-23801.9),

\[
 \boxed{
 \mathcal P(X)
 :=\sum_{q=p^k\le X}{\Lambda(q)\over\sqrt q}
 \log{X\over q}
 \ge4\sqrt X-O_\epsilon(X^\epsilon).}
 \tag{T-23801.11}
\]

The constant four is exact. It is not obtained from the prime-number theorem:
it is the product of the continuum carry mass `1/2`, the gamma shape-two
normalization, and the entropy main term `n/2`.

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
 \tag{T-23801.12}
\]

It equals the zeta screw function at the square sample:

\[
 \mathscr S(N)=\Psi(2\log N).
 \tag{T-23801.13}
\]

Equation (T-23801.11) gives, for every `epsilon>0`,

\[
 \boxed{
 \Psi(2\log N)\le C_\epsilon N^\epsilon.}
 \tag{T-23801.14}
\]

The remaining gamma/Lerch terms are only logarithmic or bounded and are absorbed
by the arbitrarily small power.

## 7. Passage from samples to the half-line

The unconditional explicit-formula derivative bound is

\[
 |\Psi'(t)|\le C(1+t)^A e^{t/2}.
 \tag{T-23801.15}
\]

Adjacent square samples satisfy

\[
 2\log(N+1)-2\log N\asymp N^{-1}=e^{-t/2}.
 \tag{T-23801.16}
\]

Therefore (T-23801.14) and the mean-value theorem give, for every `delta>0`,

\[
 \boxed{
 \Psi(t)\le C_\delta(1+t)^{B_\delta}e^{\delta t}
 \qquad(t\ge0).}
 \tag{T-23801.17}
\]

This is the upper-envelope counterpart of the square-sampling theorem.

## 8. Landau pole exclusion

The one-sided Fourier--Laplace identity is

\[
 \int_0^\infty\Psi(t)e^{izt}dt
 =-{1\over z^2}{\xi'\over\xi}(1/2-iz).
 \tag{T-23801.18}
\]

Fix `delta>0`. Add a sufficiently large positive polynomial multiple of
`e^(delta t)` and one compactly supported correction so that

\[
 H_\delta(t)=P_\delta(t)e^{\delta t}-\Psi(t)
\]

is nonnegative on the full half-line. Landau's one-sign theorem forces its
Laplace convergence boundary to be a genuine singularity unless the meromorphic
continuation is holomorphic farther left. There is no positive-real Xi zero, so
(T-23801.18) excludes every zero with

\[
 \Re\rho>{1\over2}+\delta.
\]

Letting `delta` tend to zero and applying functional-equation symmetry yields

\[
 \boxed{\mathrm{RH}.}
 \tag{T-23801.19}
\]

This is the same exact upper-envelope transfer already isolated in `T-20205`;
no zero ordinate or finite verified-height hypothesis enters.

## 9. Review firewall

A reviewer should attack the proposal in the following order.

1. Verify the carry Mellin identity `L-23804.4` and the probability law.
2. Verify the quotient and physical density `L-23805.4`--`L-23805.7`.
3. Attack GCF directly on every quotient layer using `L-23805.11`--`L-23805.12`.
4. Confirm the exact endpoint sampling inequality `beta<=K` in `L-23804.3`.
5. Reconstruct the finite packing and entropy estimates in `L-23806`.
6. Check the square-screw normalization and the upper-envelope Landau
   orientation.
7. Require the first fixed-ratio Mertens/Farey cell as a mutation: a proof of
   GCF that forgets Möbius signs or takes total variation before recombination
   must fail.

## 10. Relationship to the balanced Type-II core

The transform (T-23801.4) contains the same reciprocal-zeta channel as the
balanced Möbius packets in PRs #158/#233 and the first Farey/Mertens cell in PR
#229. GCF is a scalar, shape-two-smoothed projection of that core.

The proposal's potential advantage is that all Type-I, endpoint, and scale
bookkeeping has already collapsed into one elementary probability factor. A
proof may therefore attack a one-variable density, an all-order Hausdorff
sequence, or a direct coupling instead of the complete Heath--Brown packet
dictionary.

## 11. Exact status

```text
carry matrix and entropy identity             proposed exact
continuum carry Mellin/probability law         proposed exact
Gamma/carry quotient and density              proposed exact
density nonnegativity GCF                      OPEN / LOAD BEARING
GCF -> explicit finite sharp packing           proposed complete
sharp packing -> screw upper envelope -> RH    proposed complete
accepted proof of RH                           NO
```

This is a full, unmistakable proof proposal with one explicitly isolated
arithmetic theorem. It should be reviewed as a candidate completion, not cited
as an established proof until GCF survives independent proof.
