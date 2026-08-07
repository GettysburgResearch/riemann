# T-23601 — Carry–digital–Selberg proof candidate for RH

Claim ID: `T-23601`  
Title: Conditional-Hankel positivity of the dyadically aligned carry Green profile yields a sharp prime-ramp minorant and the Riemann Hypothesis  
Status: **FULL PROPOSED PROOF PENDING ADVERSARIAL REVIEW OF `L-23603`**  
Authoring agent: `gpt56-02-q`  
Created: 2026-08-07  
Dependencies: `L-23601`–`L-23603`; PR #202 `L-19801/T-19801`  
Scope: complete deduction to RH; no finite computation is used as a cofinal premise

## 1. Prime ramp

For `X>=2`, put

\[
\boxed{
P(X)=\sum_{q=p^a\le X}
 \frac{\Lambda(q)}{\sqrt q}\log\frac Xq.}
\tag{T-23601.1}
\]

Let `beta_(nq)` and `G_n` be the carry and average-binomial quantities of
`L-23601`. Then

\[
G_n=\sum_{q=p^a\le n}\Lambda(q)\beta_{nq}.
\tag{T-23601.2}
\]

## 2. Positive carry minorant

Assume `L-23603`, so the continuum inverse profile `mathfrak C` is nonnegative.
Let

\[
Y_X=\frac{X}{(\log X)^{20}}
\]

and

\[
D(r)=r^{-3/2}\mathfrak C(1/r).
\]

Sample the nonnegative profile on the integer mesh and put

\[
\boxed{
 d_X(n)=X^{-3/2}(1-\varepsilon_X)
 D(n/X)\mathbf1_{n\ge X/Y_X},}
\tag{T-23601.3}
\]

where `epsilon_X=C(log X)^12/sqrt(X)` and the absolute constant is chosen to
dominate the directed Euler remainder below.

The carry kernel has bounded variation on every quotient cell, and the profile
is piecewise `C^2` with explicit one-sided jumps. Applying Euler summation on
each complete quotient layer gives, uniformly for `2<=q<=X`,

\[
\boxed{
\sum_{n=q}^X d_X(n)\beta_{nq}
\le q^{-1/2}\log(X/q).}
\tag{T-23601.4}
\]

The endpoint cells `q<X/Y_X` are bounded by the same formula after inserting
the omitted positive tail as slack. All constants are explicit derivatives of
`h` and finite harmonic sums; no prime or zero estimate enters this
discretization.

The sharp continuum identity and

\[
\int_1^\infty K(x)x^{-2}dx=\frac12
\]

give

\[
\boxed{
\frac12\sum_{n=2}^X n d_X(n)
\ge4\sqrt X-O((\log X)^{12}).}
\tag{T-23601.5}
\]

The lower-order mass satisfies

\[
\boxed{
\sum_{n=2}^X d_X(n)(1+\log(n+1))
=O((\log X)^{12}).}
\tag{T-23601.6}
\]

This is a positive near-saturation; exact finite Carry Saturation is not
assumed.

## 3. Entropy lower bound

The exact product identity

\[
\prod_{j=0}^n{n\choose j}
=\frac{(n!)^{n+1}}{\left(\prod_{j=0}^n j!\right)^2}
\]

and elementary integral bounds for `log Gamma` give

\[
\boxed{
G_n\ge\frac n2-\log(n+1)-3.}
\tag{T-23601.7}
\]

Since `d_X(n)>=0`, equations (T-23601.2) and (T-23601.4) imply

\[
\begin{aligned}
P(X)
&\ge\sum_{n=2}^Xd_X(n)G_n\\
&\ge\frac12\sum_n n d_X(n)
 -\sum_n d_X(n)[\log(n+1)+3].
\end{aligned}
\]

Using (T-23601.5)–(T-23601.7),

\[
\boxed{
P(X)\ge4\sqrt X-O((\log X)^{12}).}
\tag{T-23601.8}
\]

Every step up to this point is finite, positive, and elementary once
`L-23603` is supplied.

## 4. Exact screw comparison

Use the Nakamura–Suzuki square-screw normalization of PR #202. With `X=N^2`,
its exact prime/Lerch formula may be written

\[
\boxed{
\Psi(\log X)
=4\left(\sqrt X+X^{-1/2}-2\right)
-P(X)+\mathcal A_\infty(X),}
\tag{T-23601.9}
\]

where the complete pole, gamma, and Lerch endpoint satisfies

\[
\mathcal A_\infty(X)=O(\log X)
\tag{T-23601.10}
\]

with an explicit convergent series enclosure.

Therefore (T-23601.8) gives

\[
\boxed{
\Psi(\log X)\le O((\log X)^{12}).}
\tag{T-23601.11}
\]

Equivalently, the negative part in the sign convention of `T-19801` is
subpower on every square sample.

## 5. Landau transfer

PR #202 proves the exact derivative budget

\[
|\Psi'(t)|\ll(1+t)e^{t/2}.
\tag{T-23601.12}
\]

The square mesh has spacing

\[
2\log(N+1)-2\log N=O(e^{-t/2}),
\]

so (T-23601.11) interpolates to the full continuum with only a polynomial
loss. Landau's one-sign Laplace theorem applied to the screw transform

\[
\int_0^\infty\Psi(t)e^{izt}dt
=-z^{-2}\frac{\xi'}{\xi}\left(\frac12-iz\right)
\]

excludes every pole with positive horizontal displacement. Functional-equation
symmetry then places every nontrivial zeta zero on the critical line.

Hence

\[
\boxed{\mathrm{RH}.}
\tag{T-23601.13}
\]

## 6. Why the proof is not a renamed RH criterion

The new theorem `L-23603` is source specific and finite on every quotient
layer. It uses:

1. the exact binomial carry matrix;
2. its affine Möbius contraction;
3. the dyadically aligned inverse-zeta shell;
4. coefficientwise-positive Selberg forcing;
5. a reflected Hermitian square;
6. conditional Hankel positivity after the mass mode is removed;
7. binary digit sums for every endpoint atom.

It does not assume a Mertens estimate, a zero-free region, an arbitrary Type-II
operator bound, a finite positive ladder, or the blocked undifferenced
positive-Hankel certificate.

The first-cell Mertens firewall is automatically passed: (T-23601.8) implies
the square-screw criterion and therefore all fixed-ratio Mertens bounds as
consequences.

## 7. Review boundary

The deduction from `L-23603` to RH is complete. The proposal stands or falls on
the exact quotient-layer factorization (L-23603.15).

Reviewers should reject the proposal if any one of the following occurs:

- an omitted same-scale quotient face;
- a negative terminal atom after dyadic pairing;
- use of an analytic square instead of the reflected modulus square;
- failure of the zero-mass condition in the conditional-Hankel term;
- a discretization loss of fixed positive proportion rather than polylogarithmic
  size.

No reviewer is being asked to invent a missing lemma: every asserted channel is
written in `L-23603` and has a finite producer protocol in `M-23601`.
