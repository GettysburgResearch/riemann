# R-32401 — Coefficient-blind Brownian frame bounds lose a full power

Claim ID: `R-32401`  
Title: The centered-interval normal form has linear worst-case energy even on the formal odd-source cone, so the remaining estimate must use the cross-scale arithmetic pairing  
Status: **PROPOSED COMPLETE EXACT SCOPE REFUTATION**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-08  
Dependencies: `L-32401`  
Scope: refutes coefficient-blind Bessel/frame closures; does not refute the actual prime-power source estimate

## 1. A top-half formal source

Let `X=8M` with `M>=2`. Put

\[
 \mathcal A_X
 =\{n:\; 3X/4<n<X,\ n\text{ odd}\}.
\]

Define a finite coefficient vector

\[
 c(n)=\mathbf1_{n\in\mathcal A_X}.
\tag{R-32401.1}
\]

Every active index is odd and lies above `X/2`; in particular its doubled
partner lies outside the endpoint. Thus (R-32401.1) belongs to the formal
positive odd-source cone underlying the exact source pattern of `L-32401.7`.

For `n in A_X`, `n/X>3/4`, so

\[
 J_{n/X}(\theta)=1
\]

whenever

\[
 |\theta-1/2|<1/4.
\tag{R-32401.2}
\]

Therefore on an interval of theta-length `1/2`,

\[
 \left|\sum_n c(n)J_{n/X}(\theta)\right|
 =|\mathcal A_X|.
\tag{R-32401.3}
\]

The interval `(6M,8M)` contains at least `M-1` odd integers, so

\[
 |\mathcal A_X|\ge M-1\ge X/16
\qquad(M\ge2).
\tag{R-32401.4}
\]

Hence the normalized physical energy obeys

\[
 \boxed{
 {1\over X}\int_0^1
 \left|\sum_nc(n)J_{n/X}(\theta)\right|^2d\theta
 \ge {X\over512}.
 }
\tag{R-32401.5}
\]

## 2. The natural diagonal budget stays bounded

On the same vector,

\[
 \sum_{n\le X}{|c(n)|^2\over n}
 \le {4\over3X}|\mathcal A_X|
 \le {1\over3}.
\tag{R-32401.6}
\]

Consequently no coefficient-independent estimate of the form

\[
 {1\over X}\int
 \left|\sum_nc_nJ_{n/X}\right|^2
 \le X^{o(1)}\sum_n{|c_n|^2\over n}
\tag{R-32401.7}
\]

can hold, even after restricting to nonnegative coefficients on odd source
indices. The required Bessel constant is `Omega(X)`.

## 3. Dyadic multiscale variants do not repair the obstruction

Any multiscale square which includes the current endpoint `X` with a
nonnegative coefficient inherits (R-32401.5). Thus summing energies over
`X,X/2,X/4,...` cannot produce a coefficient-blind polylogarithmic frame bound
against the same diagonal budget.

The exact actual source escapes this example only because the top-half odd
prime-power weights are rigidly coupled to negative doubled weights at lower
scales and to the prime distribution itself. Those correlations must remain
inside the proof before a norm is taken.

## 4. Consequence for PR #325

`L-32401` is an exact coordinate simplification, not a generic frame theorem.
The Brownian/min kernel makes the remaining arithmetic more visible but does not
make it automatically small.

A valid `NTBR` proof must therefore exploit the exact

```text
odd prime power  +log p
paired double    -log p
```

source together with the source-convolved Selberg identities. It may not
replace that source by an arbitrary coefficient vector or invoke a generic
Brownian Bessel estimate.

## 5. Proof boundary

Refuted:

- coefficient-blind single-scale Brownian frame closure;
- the corresponding nonnegative odd-source-cone closure;
- any nonnegative multiscale sum containing the current scale as a workaround.

Not refuted:

- the actual arithmetic `c_2` source;
- source-specific signed dyadic recombination;
- `NTBR`;
- RH.