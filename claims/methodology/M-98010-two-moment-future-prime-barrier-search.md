# M-98010 — Two-moment future-prime barrier search after one-switch collapse

Status: **BINDING SEARCH AND FALSIFICATION PROTOCOL**  
Created: 2026-08-18  
Depends on: `L-98010`–`L-98012`, PRs #589, #590, #594, #596  
RH status: **unproved**

## 1. Exact compressed state

For a finite installed-prime product `P` and cutoff `K`, put

\[
A_P(K)=\sum_{\substack{d\mid P\\d<K}}{\mu(d)\over d},
\qquad
B_P(K)=\sum_{\substack{d\mid P\\d<K}}{\mu(d)\over\sqrt d},
\]

and normalize

\[
U_P(K)=\sqrt K\,A_P(K),
\qquad
V_P(K)=B_P(K).
\]

For `K=X/Y`, the one-switch target prefix is exactly

\[
\boxed{
\mathcal T_P(X;Y)=4\sqrt Y\,U_P(K)-3V_P(K).
}
\tag{M-98010.1}
\]

Thus the complete nonnegative-hinge marginal state is two-dimensional.

## 2. Exact future-prime recurrence

If `p` is not installed, then

\[
A_{Pp}(K)=A_P(K)-p^{-1}A_P(K/p),
\]

\[
B_{Pp}(K)=B_P(K)-p^{-1/2}B_P(K/p).
\]

After the normalization in (M-98010.1), both coordinates obey the same parity child operator:

\[
\boxed{
U_{Pp}(K)=U_P(K)-p^{-1/2}U_P(K/p),
}
\tag{M-98010.2}
\]

\[
\boxed{
V_{Pp}(K)=V_P(K)-p^{-1/2}V_P(K/p).
}
\tag{M-98010.3}
\]

Consequently

\[
\boxed{
\mathcal T_{Pp}(X;Y)
=\mathcal T_P(X;Y)
-p^{-1/2}\mathcal T_P(X/p;Y).
}
\tag{M-98010.4}
\]

This is the literal source recurrence. No reserve summand, parity-blind child, or fixed aperture is introduced.

## 3. Search object

Search for an explicit barrier

\[
\mathfrak B(P,K,Y)=\alpha(P,K,Y)U_P(K)-\beta(P,K,Y)V_P(K)
+\mathfrak R(P,K,Y)
\]

with the following fail-closed requirements:

1. `mathfrak B>=0` at every terminal state;
2. the coefficients and reserve `mathfrak R` are explicit functions of the future-prime quotient profile;
3. prime adjoining satisfies
   \[
   \mathfrak B(Pp,K,Y)
   \ge
   \mathfrak B(P,K,Y)
   -p^{-1/2}\mathfrak B(P,K/p,Y)
   +\mathfrak G_{P,p}(K,Y),
   \]
   with `mathfrak G>=0` or an exact Type-I/Type-II decomposition;
4. at the physical observation,
   \[
   \mathfrak B(P,K,Y)\le\mathcal T_P(X;Y);
   \]
5. every activation side and strict cutoff `d<K` is retained.

The tautological choice `mathfrak B=mathcal T` is forbidden as a claimed construction.

## 4. Candidate coordinates to test

The smallest serious state family is

```text
U_P(K), V_P(K);
least unused prime;
logarithmic budget log K;
future reciprocal mass sum_{p<=K} 1/p;
first active divisor on each side of K;
one strict-boundary overshoot coordinate.
```

Before adding any further coordinate, produce an exact finite separator showing that the smaller state cannot distinguish two source histories requiring different Bellman actions.

## 5. Required mutation suite

Every proposed barrier must be tested against:

```text
PR #596 p=67 crossing near X=160.375;
PR #561 odd-history witness X=61841;
PR #578 moving-cutoff depth-eight failure;
all fixed even-depth negative-current examples;
future-prime states with empty small-prime cube;
strict left and right activation limits;
permutation of installed primes that preserves the final product but changes ownership history.
```

A barrier that uses only a fixed positive angle, total unsigned mass, local Julia trace, or a source-blind square norm is rejected before large computation.

## 6. Type-II handoff

If the Bellman error is not pointwise nonnegative, expand it before absolute values and sort it into

```text
diagonal;
activation boundary;
large gcd / near diagonal;
small reduced variable Type I;
balanced separated coprime Type II.
```

A bridge to PR #590 or PR #595 is accepted only if it gives a literal coefficient identity from the remaining error to the published kernels, including all scale factors and boundary terms.

## 7. Stopping rule

The search succeeds only with an explicit proved barrier. It fails productively when it returns one exact minimal separator. Numerical positivity over a finite horizon, a trained coefficient vector, or an abstract Bellman fixed point is reconnaissance rather than closure.
