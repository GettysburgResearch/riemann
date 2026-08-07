# L-15113 — Kernel-pinned inertia transfer for canonical Loewner matrices

Claim ID: `L-15113`  
Status: **PROVED FINITE-DIMENSIONAL PERTURBATION LEMMA**  
Authoring agent: `gpt56-04-f`  
Created: 2026-07-31  
Dependencies: Weyl's eigenvalue perturbation inequality; `L-15111`  
Scope: transport a surrogate/root-census result to an exact windowed target without root finding  
Related counterexample candidates: none

## 1. Motivation

PR #173 produced a useful high-precision census for a full-sample surrogate, but the production target consists of windowed or smoothly localized Fourier coefficients. A numerical resemblance between the two coefficient vectors is not a proof that their interpolation polynomials have the same number of nonreal roots.

The canonical Loewner matrix of `L-15111` gives the correct bridge. Its inertia counts nonreal conjugate pairs, it has an exact target kernel, and its entries depend only on `P,P',P''` at the finite nodes. This lemma supplies a directed perturbation criterion preserving that inertia.

## 2. Kernel-pinned inertia theorem

Let

\[
 H_0=H_0^{\mathsf T}\in\mathbb R^{n\times n}
\]

have inertia

\[
 \operatorname{Inertia}(H_0)=(n_+,n_-,1).
\]

Assume every nonzero eigenvalue of `H_0` has absolute value at least `m>0`:

\[
 \operatorname{spec}(H_0)\cap(-m,m)=\{0\}.
 \tag{L-15113.1}
\]

Let `H=H^T` satisfy

\[
 \|H-H_0\|_2\le\varepsilon<m
 \tag{L-15113.2}
\]

and suppose `H` has a known nonzero kernel vector:

\[
 Hv=0,
 \qquad v\ne0.
 \tag{L-15113.3}
\]

Then

\[
 \boxed{
 \operatorname{Inertia}(H)=(n_+,n_-,1).}
 \tag{L-15113.4}
\]

### Proof

Order eigenvalues increasingly. When `n_->0`,

\[
 \lambda_{n_-}(H_0)\le-m,
 \qquad
 \lambda_{n_-+1}(H_0)=0.
\]

If `n_+>0`, also

\[
 \lambda_{n_-+2}(H_0)\ge m.
\]

Weyl's inequality and (L-15113.2) give

\[
 \lambda_{n_-}(H)<0,
 \qquad
 \lambda_{n_-+2}(H)>0.
\]

Thus `H` has at least `n_-` negative eigenvalues and at most `n_-+1` nonpositive eigenvalues. Since (L-15113.3) supplies a zero eigenvalue, it cannot have `n_-+1` negative eigenvalues, and it cannot have more than one zero. Hence it has exactly `n_-` negatives and one zero; all remaining eigenvalues are positive.

If `n_-=0`, Weyl gives `lambda_2(H)>0`; the known zero then excludes a negative eigenvalue and excludes a second zero. The negative-semidefinite endpoint is analogous. QED.

The known kernel is load bearing. Without it, a perturbation of a singular matrix can move the zero eigenvalue to either sign.

## 3. Entrywise interval corollary

Suppose a symmetric exact matrix `H` has directed entry enclosures

\[
 H_{ij}\in[(H_0)_{ij}-r_{ij},(H_0)_{ij}+r_{ij}],
 \qquad r_{ij}=r_{ji}\ge0.
\]

Put

\[
 \varepsilon_{\rm row}
 =\max_i\sum_j r_{ij}.
 \tag{L-15113.5}
\]

Then

\[
 \|H-H_0\|_2
 \le\|H-H_0\|_\infty
 \le\varepsilon_{\rm row}.
 \tag{L-15113.6}
\]

Therefore the inertia is certified whenever

\[
 \boxed{\varepsilon_{\rm row}<m}
 \tag{L-15113.7}
\]

and the exact kernel identity is independently known.

This replaces interval root finding by one exact midpoint inertia, one spectral moat, and one entrywise radius ledger.

## 4. Canonical Loewner specialization

Let `p` be an exact finite target, let

\[
 P(s)=\sum_jp_j\phi_j(s),
\]

and assume the node intervals prove

\[
 0\notin P(\lambda_i)
 \qquad(1\le i\le n).
 \tag{L-15113.8}
\]

Define, with outward interval arithmetic,

\[
 b_i=-\frac{P'(\lambda_i)}{P(\lambda_i)},
 \qquad
 a_i=\frac{P'(\lambda_i)^2-P(\lambda_i)P''(\lambda_i)}{P(\lambda_i)^2},
 \tag{L-15113.9}
\]

and

\[
 Q^{\rm can}_{ij}
 =\begin{cases}
 (b_i-b_j)/(\lambda_i-\lambda_j),&i\ne j,\\
 a_i,&i=j.
 \end{cases}
 \tag{L-15113.10}
\]

The exact algebra in `L-15111` gives

\[
 Q^{\rm can}p=0.
 \tag{L-15113.11}
\]

Hence any rational center matrix and radius ledger satisfying (L-15113.7) certifies the exact canonical inertia. In particular:

- reference inertia `(n-1,0,1)` proves the exact target polynomial has only simple real roots;
- reference inertia `(r+c,c,1)` proves the exact polynomial has exactly `c` nonreal conjugate pairs.

No approximate root location enters the proof object.

## 5. Coefficient-to-Loewner radius

Let `p^0` be a reference coefficient vector and suppose

\[
 |p_j-p_j^0|\le\tau_j.
 \tag{L-15113.12}
\]

Because `P` and all of its derivatives are linear in the coefficients,

\[
 \boxed{
 |P^{(q)}(\lambda_i)-P_0^{(q)}(\lambda_i)|
 \le
 \sum_j\tau_j\,|\phi_j^{(q)}(\lambda_i)|,
 \qquad q=0,1,2.}
 \tag{L-15113.13}
\]

All quantities on the right are exact for rational nodes. Directed division in (L-15113.9)--(L-15113.10) then supplies the matrix radii in Part 3.

For the centered Fourier projection of an even target `K` on `[-ell,ell]`, the exact coefficient and the full-transform surrogate differ by the tail:

\[
 \begin{aligned}
 p_n^{\rm win}
 &=\frac{(-1)^n}{\sqrt{2\ell}}
   \int_{-\ell}^{\ell}K(t)e^{-i\pi nt/\ell}\,dt,\\
 p_n^{\rm full}
 &=\frac{(-1)^n}{\sqrt{2\ell}}
   \int_{\mathbb R}K(t)e^{-i\pi nt/\ell}\,dt,
 \end{aligned}
\]

so

\[
 \boxed{
 |p_n^{\rm win}-p_n^{\rm full}|
 \le
 \frac1{\sqrt{2\ell}}
 \int_{|t|>\ell}|K(t)|\,dt.}
 \tag{L-15113.14}
\]

For a smooth cutoff `chi_ell`, replace the tail by

\[
 \frac1{\sqrt{2\ell}}
 \int_{\mathbb R}|1-\chi_\ell(t)|\,|K(t)|\,dt.
 \tag{L-15113.15}
\]

The exact Hermite target has a super-Gaussian bound for these integrals. Equations (L-15113.13)--(L-15113.15) are therefore a direct proof interface from the radical-tail theorem to canonical Loewner inertia.

## 6. Separation from the arithmetic scalar gate

Canonical inertia decides whether an arbitrary positive special completion exists. It does **not** decide whether the actual arithmetic target-pinned line passes.

After Part 4, production must still form the actual arithmetic pencil

\[
 T_p(c)=A_p+cB_p
\]

or the actual source thresholds of `L-15109`. The outputs must be retained separately:

```text
canonical_inertia_verdict
arithmetic_scalar_threshold_verdict
```

A positive first verdict and a negative second verdict are logically consistent, as the exact four-node example in `R-15103` demonstrates.

## 7. Proof-producing protocol

For one selected support and band:

1. produce directed intervals for the actual windowed/smooth-cutoff coefficients;
2. form interval values of `P,P',P''` at every node;
3. build a rational center canonical Loewner matrix and symmetric radii;
4. certify its exact midpoint inertia and nonzero spectral moat;
5. apply (L-15113.7), using the exact kernel identity;
6. only then evaluate the actual arithmetic scalar thresholds.

The full-sample surrogate from PR #173 can be used as a midpoint nomination, but only the actual-target radius ledger may transfer its inertia.

## Gap audit

1. A small coefficient tail need not give a small Loewner radius near a node where `P(lambda_i)` is tiny; the directed denominators in (L-15113.9) are essential.
2. A midpoint eigengap is not a proof unless its lower moat is exact or directed.
3. The theorem preserves inertia, not root locations.
4. Repeated roots correspond to extra canonical nullity and necessarily violate the strict moat condition.
5. The scalar Finsler gate remains source dependent and is not implied by the result.