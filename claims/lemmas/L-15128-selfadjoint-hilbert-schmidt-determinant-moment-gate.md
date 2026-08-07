# L-15128 — Self-adjoint Hilbert–Schmidt determinant calculus and the exact moment gate

Claim ID: `L-15128`  
Status: **PROVED OPERATOR-THEORETIC LEMMA; NO RIEMANN MOMENT MATCH CLAIMED**  
Authoring agent: `gpt56-04-f`  
Created: 2026-08-01  
Dependencies: standard Carleman--Fredholm determinant theory; spectral theorem for compact self-adjoint operators  
Scope: audited/recovered core of the July 2026 Shimizu determinant proposal  
Related counterexample candidates: none

## 1. Setup

Let `K=K*` be Hilbert--Schmidt on a separable Hilbert space. Define, for centered
variable `w=s-1/2`,

\[
 D_K(w)=\det{}_2(I+iwK),
 \qquad
 F_K(w)=e^{a+bw}D_K(w).
 \tag{L-15128.1}
\]

Here `a,b` are arbitrary constants. The regularized determinant is well-defined
for every Hilbert--Schmidt operator.

## 2. Entire function and zero geometry

The function `D_K` is entire. If the nonzero eigenvalues of `K`, repeated with
multiplicity, are `lambda_j`, then

\[
 D_K(w)=\prod_j(1+iw\lambda_j)e^{-iw\lambda_j}.
 \tag{L-15128.2}
\]

Consequently every zero of `F_K` has the form

\[
 \boxed{w=i/\lambda_j,\qquad \lambda_j\in\mathbb R\setminus\{0\}.}
 \tag{L-15128.3}
\]

Thus every zero of `s -> F_K(s-1/2)` lies on `Re s=1/2`.

The exponential factor changes neither the zero set nor multiplicities.

## 3. Exact logarithmic moments

For

\[
 |w|\,\|K\|<1,
\]

one has the absolutely convergent expansion

\[
 \boxed{
 \log D_K(w)
 =\sum_{m=2}^\infty
   \frac{(-1)^{m-1}}m
   (iw)^m\operatorname{Tr}(K^m).}
 \tag{L-15128.4}
\]

Indeed, `K^m` is trace class for every `m>=2`, and the scalar expansion of
`log(1+z)-z` may be summed over the spectrum.

Hence, for every `m>=2`,

\[
 \boxed{
 \partial_w^m\log F_K(0)
 =(m-1)!(-1)^{m-1}i^m\operatorname{Tr}(K^m).}
 \tag{L-15128.5}
\]

In particular,

\[
 \boxed{
 \operatorname{Tr}(K^{2r})
 =\frac{(-1)^{r+1}}{(2r-1)!}
   \partial_w^{2r}\log F_K(0).}
 \tag{L-15128.6}
\]

If `F_K` is even, all odd trace moments `Tr(K^(2r+1))`, `r>=1`, vanish.

## 4. Stieltjes moment constraints

Put

\[
 s_r=\operatorname{Tr}(K^{2r+2})
 =\sum_j\lambda_j^2(\lambda_j^2)^r.
 \tag{L-15128.7}
\]

This is the moment sequence of the finite positive measure

\[
 \nu_K=\sum_j\lambda_j^2\delta_{\lambda_j^2}
 \quad\text{on }[0,\|K\|^2].
 \tag{L-15128.8}
\]

Therefore, for every finite vector `c`,

\[
 \boxed{
 \sum_{p,q}c_p\overline{c_q}s_{p+q}\ge0,
 \qquad
 \sum_{p,q}c_p\overline{c_q}s_{p+q+1}\ge0.}
 \tag{L-15128.9}
\]

Equivalently, every ordinary and shifted Hankel matrix formed from `s_r` is
positive semidefinite. These are exact necessary audit gates for any claimed
self-adjoint determinant model.

They are not sufficient by themselves to identify an entire target with the
determinant.

## 5. Hilbert--Schmidt limits

Let `K_M=K_M*` be finite rank and suppose

\[
 \|K_M-K\|_2\to0.
 \tag{L-15128.10}
\]

Then:

1. `det_2(I+iwK_M) -> det_2(I+iwK)` locally uniformly in `w`;
2. for every fixed `m>=2`,
   
   \[
   \boxed{\operatorname{Tr}(K_M^m)\to\operatorname{Tr}(K^m).}
   \tag{L-15128.11}
   \]

For the second assertion, telescope `K_M^m-K^m`; in each term place the
Hilbert--Schmidt difference and one further factor in `S_2`, with all remaining
factors in operator norm. Uniform `S_2` boundedness follows from convergence.
The first assertion is the standard continuity of `det_2` in the
Hilbert--Schmidt norm.

Thus a finite-rank compression programme is valid only after an actual
`S_2`-Cauchy estimate has been proved.

## 6. Exact equivalence with RH at the target-identification level

Let

\[
 \Xi_c(w)=\xi(1/2+w).
\]

If there exist `K=K* in S_2` and constants `a,b` such that

\[
 \boxed{
 \Xi_c(w)=e^{a+bw}\det{}_2(I+iwK)
 \quad(w\in\mathbb C),}
 \tag{L-15128.12}
\]

then RH follows immediately from (L-15128.3).

Conversely, under RH, list the positive ordinates `gamma>0` with multiplicity
and define a diagonal compact self-adjoint operator with paired spectrum

\[
 \lambda=\pm1/\gamma.
 \tag{L-15128.13}
\]

The classical zero count gives

\[
 \sum_{\gamma>0}\gamma^{-2}<\infty,
\]

so `K in S_2`. Pairing the two determinant factors gives

\[
 (1+iw/\gamma)e^{-iw/\gamma}
 (1-iw/\gamma)e^{iw/\gamma}
 =1+w^2/\gamma^2.
\]

The centered Hadamard product therefore yields (L-15128.12), with the harmless
central scalar exponential fixed by normalization.

Consequently:

\[
 \boxed{
 \text{existence of an exact self-adjoint Hilbert--Schmidt determinant model
 for }\xi
 \Longleftrightarrow \mathrm{RH}.}
 \tag{L-15128.14}
\]

The operator construction is useful only if the target identity is proved
without importing a condition equivalent to RH.

## 7. Proof boundary

The following parts of the July 2026 proposal are accepted here:

- self-adjoint `S_2` determinant calculus;
- zero geometry;
- finite-rank `S_2` limit;
- moment and Hankel constraints;
- identity-theorem closure after a genuine local logarithmic-derivative identity.

This lemma does **not** accept the paper's finite-window comparison as a proof of
the target identity. That step is audited in `R-15106`.
