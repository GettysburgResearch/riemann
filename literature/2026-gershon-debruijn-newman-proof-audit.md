# Audit note — Gershon (2026), *The De Bruijn-Newman Constant Is Zero*

Status: **PREPRINT PROOF CLAIM NOT ACCEPTED — TWO LOAD-BEARING LARGE-ORDER STEPS FAIL THEIR DECLARED SCOPE**  
Auditor: `gpt56-sol`  
Date: 2026-08-08  
Source: Avi Gershon, *The De Bruijn-Newman Constant Is Zero*, Preprints.org 202604.1513.v1, posted 2026-04-22. The server labels this version non-peer-reviewed.

## 1. Why this paper matters

Rodgers--Tao prove the unconditional inequality

\[
\Lambda_{\rm dBN}\ge0.
\]

RH is equivalent to

\[
\Lambda_{\rm dBN}\le0.
\]

Therefore a correct proof of the preprint's claimed upper bound

\[
\Lambda_{\rm dBN}\le0
\]

would settle RH.  The claim deserves immediate examination rather than dismissal by status alone.

The present note audits only two load-bearing passages in the all-order Toeplitz-minor argument.  It does not assess every finite computation or earlier log-concavity theorem in the preprint.

## 2. First fatal source-type error: Taylor coefficients of an entire function cannot have nearest-pole geometric asymptotics

The preprint defines

\[
g(z)=\sum_{m\ge0}\gamma_m z^m=\Xi(\sqrt z).
\]

The function `g` is entire.  Lemma 10 nevertheless states, after invoking the Hadamard product for `g`, that the Taylor coefficients satisfy an expansion of the form

\[
\gamma_m
 =R_1\rho_1^m+R_2\rho_2^m
  +O(\delta_3^m\rho_1^m),
\qquad
\rho_k=|z_k|^{-1},
\]

where `z_k` are zeros of `g` and `rho_1>0` is the inverse modulus of the nearest zero.

This is incompatible with the Cauchy--Hadamard theorem.  Since `g` is entire, its Taylor series has infinite radius of convergence, hence

\[
\boxed{
\limsup_{m\to\infty}|\gamma_m|^{1/m}=0.
}
\]

A nonzero leading term `R_1 rho_1^m` with `rho_1>0` would instead force a positive root limsup.  Hadamard factorisation controls zeros of the entire function; it does **not** turn the Taylor coefficients of the entire function into a nearest-pole expansion.

The geometric pole expansion belongs to the reciprocal series

\[
{1\over g(z)}=\sum_{m\ge0}\eta_m z^m,
\]

whose radius of convergence is the distance to the nearest zero of `g`.  The preprint itself correctly uses this reciprocal sequence in its Jacobi complementary-minor identity (Proposition 17) and later Binet--Cauchy expansion.  Thus Lemma 10 has switched the source type from `eta_m` to `gamma_m` at exactly the place where its claimed exponential-in-`n` spectral separation is needed.

### Consequence

The displayed deduction

```text
all Toeplitz entries gamma_(n+i-j)
  share a nearest-zero geometric factor rho_1^n
-> C_s(n)=C_s(infinity)+O(delta^n)
```

is not proved.  In particular the `n>=100` argument of Proposition 22, which invokes Lemma 10 to replace the complete dissipation bank by an `n`-independent spectral limit with an error below `10^-34`, loses its stated justification.

## 3. Second scope failure: the reciprocal-series Binet--Cauchy tail assumes the global zero ordering that RH is supposed to prove

The complementary-minor identity itself is valuable and correctly typed:

\[
D_r(n)
=(-1)^{rn}\gamma_0^{r+n}
\det(\eta_{r+i-j})_{0\le i,j<n}.
\]

For fixed `n`, a partial-fraction/Binet--Cauchy analysis of `eta_k` can be based on poles of `1/g`, i.e. zeros of `g`.

The preprint's Lemma 11 writes these poles globally as

\[
\rho_m=-1/t_m^2
\]

and uses the `n` largest real negative inverse zeros

\[
\rho_1,\ldots,\rho_n
\]

to obtain a positive dominant Vandermonde term and the asymptotic ratio

\[
L_r(n)
\sim C_n\left({t_{n+1}\over t_n}\right)^{2r}.
\]

This representation is legitimate only while the relevant zeros of `g` are known to lie on the negative real axis.  Verified critical-line zeros provide such information through a very large but **finite** range.  For arbitrary `n`, however, asserting that the first `n+1` zeros of `g` admit an ordering by positive real ordinates `t_m` with

\[
z_m=-t_m^2
\]

is exactly a real-zero assertion for the zero set of `g`.  A hypothetical off-critical zeta zero gives a nonreal zero of `g` and breaks the real-negative spectral ordering used in the positivity argument.

The preprint later applies this `t_n/t_(n+1)` tail for unrestricted `n` in the all-order coverage.  The finite verified-zero range does not justify that cofinal step.

### Consequence

The reciprocal-series repair does not rescue the global proof as written.  It gives a valid tail mechanism only at indices for which the necessary real-zero input has independently been certified.  Extending it to every `n` would assume the zero geometry being proved.

## 4. What survives and what does not

This audit does **not** refute the following components merely by association:

- strict log-concavity of the Riemann--Jacobi kernel;
- finite interval certifications claimed in the paper, subject to independent replay;
- the Jacobi complementary-minor identity itself;
- finite use of verified critical zeros;
- Rodgers--Tao's theorem `Lambda_dBN>=0`.

It does reject the manuscript's current all-order closure:

```text
Lemma 10 nearest-zero asymptotic for gamma_m      FALSE AS STATED
Lemma 11 unrestricted real-negative zero ordering  CIRCULAR BEYOND VERIFIED RANGE
Proposition 22 global spectral separation          NOT ESTABLISHED
Theorem 11 all Toeplitz minors positive             NOT ESTABLISHED BY THIS ARGUMENT
Lambda_dBN=0 / RH                                  NOT ESTABLISHED BY THIS PREPRINT
```

## 5. Possible noncircular repair target

There is one interesting direction worth separating from the failed proof.

The Desnanot--Jacobi hierarchy defines dissipation constants `C_s(n)`.  If one could prove **without using zeros of `g`** a uniform summability estimate

\[
\boxed{
\sum_{s\ge1}C_s(n)\le C
\quad\text{for all sufficiently large }n,
}
\]

then the paper's first-level velocity lower bound `mu_1(n) \asymp 1/n` together with

\[
|\log\Theta_s(n)|\lesssim {C_s(n)\over n^2}
\]

would yield an unconditional positive velocity for large `n`; a finite certified region could then in principle finish the Toeplitz criterion.

The paper proves only a uniform *individual* `O(n^-2)` smoothness bound at finitely stated levels and obtains summability from the zero-based spectral tail.  A zero-free proof of summability is therefore a genuinely new theorem, not a textual repair.

## 6. Repository implication

The agentic-polymath project should not treat the 2026 preprint as an external completion of RH.  Its useful lesson is architectural:

```text
finite DJ/Toeplitz algebra            potentially reusable;
reciprocal-series complementary minor correctly typed;
source-blind nearest-zero tail        forbidden;
cofinal closure must be zero-free or source-specific.
```

This matches the repository's own repeated firewall: a contraction or spectral-gap argument may not import the RH zero geometry into the theorem whose purpose is to prove RH.
