# T-32301 — Square-root hinge average-carry proposal for the Riemann Hypothesis

Claim ID: `T-32301`  
Title: A single finite triangular sign theorem for square-root hinge targets yields an exact nonnegative prime-ramp carry saturation and RH  
Status: **FULL CONDITIONAL PROPOSAL — SHARP OPEN / RH UNPROVED**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-08  
Dependencies: `L-32303`; PR #295 `L-29203`; elementary carry/binomial and square-screw/Landau consumers already isolated in the repository

## 1. Why this proposal is a shake-up

The recent full-proposal sequence repeatedly propagated the complete logarithmic target through analytic, boundary, source, and Pascal states.  Exact refutations showed that generic endpoint atomization and generic weighted-BV contraction are the wrong invariants.

This proposal changes the order of the proof:

```text
resolve the logarithm into positive endpoint-vanishing hinges first;
solve each hinge by one finite upper-triangular carry system;
only then superpose completed nonnegative flows.
```

There is no propagated logarithmic boundary state in the proposed proof.

## 2. Exact finite theorem

For every endpoint `T>=3`, define

\[
h_T(q)=q^{-1/2}-T^{-1/2}
\qquad(2\le q\le T),
\]

and the average carry matrix

\[
\beta_{nq}
=\frac{\lfloor n/q\rfloor[q-1-(n\bmod q)]}{n+1}.
\]

Let `c_T(n)` be the unique triangular inverse

\[
h_T(q)=\sum_{n=q}^{T}c_T(n)\beta_{nq}.
\tag{T-32301.1}
\]

The sole new theorem is

> **SHARP — Square-root Hinge Average-Row Positivity.**  For every integer `T>=3`,
> \[
> \boxed{c_T(n)\ge0\qquad(2\le n\le T).}
> \tag{T-32301.2}
> \]

No asymptotic qualifier occurs in SHARP.  It is a finite inequality involving floors, Möbius inversion, rational arithmetic, and square roots.

## 3. SHARP produces the full finite carry flow

For each row `n`, place mass

\[
\frac{c_T(n)}{n+1}
\]

on every split `[n,j]`, `0<=j<=n`.  By the definition of `beta`, the complete carry load is exactly `h_T`.

Thus SHARP gives a nonnegative finite carry saturation for every hinge.  No repair, negative-part estimate, or cycle optimization remains.

## 4. Positive hinge synthesis of the critical target

PR #295 proves exactly

\[
w_X(q)=q^{-1/2}\log(X/q)
=\sum_{T=3}^{X}\lambda_{X,T}h_T(q),
\qquad\lambda_{X,T}\ge0.
\tag{T-32301.3}
\]

Superpose the hinge flows with these nonnegative coefficients.  The result is an exact nonnegative carry saturation of `w_X` at every finite endpoint.

Consequently the carry/binomial identity gives

\[
\sum_{p^a\le X}
\frac{\Lambda(p^a)}{\sqrt{p^a}}
\log\frac X{p^a}
=\sum_n d_X(n)G_n,
\tag{T-32301.4}
\]

with `d_X(n)>=0` and the exact carry constraints.

The existing entropy estimate for the average binomial rows supplies the sharp archimedean main term.  In the repository normalization this yields

\[
\boxed{
\sum_{p^a\le X}
\frac{\Lambda(p^a)}{\sqrt{p^a}}
\log\frac X{p^a}
\ge4\sqrt X-O(\log^B X)
}
\tag{T-32301.5}
\]

with the lower-order ledger already isolated on the carry route.

## 5. RH conclusion

At square endpoints, the source-pinned square-screw identity converts (T-32301.5) into the required subpolynomial upper envelope for the zeta screw function.  Critical square sampling and the one-sided Laplace/Landau theorem exclude every nontrivial zero with real part greater than `1/2`; functional-equation symmetry excludes the reflected half.

Therefore

\[
\boxed{
\mathrm{SHARP}
\Longrightarrow
\text{exact nonnegative carry saturation}
\Longrightarrow
\text{sharp prime ramp}
\Longrightarrow
\mathrm{RH}.
}
\tag{T-32301.6}
\]

This is the complete conditional proof chain.

## 6. Directed finite evidence

`X-32301` uses no floating-point arithmetic.  It encloses every `1/sqrt(n)` between rational endpoints with common denominator `10^30`, computes the multiples-Möbius state, and evaluates the exact adjoint numerator for every coefficient.

It certifies strict positivity for every `2<=n<T` at

```text
T = 100,
    1,000,
    10,000,
    100,000,
    1,000,000,
```

with `c_T(T)=0` exactly.

The smallest certified coefficient is always the penultimate one in this nomination.  At `T=1,000,000` its directed lower bound is

\[
\frac{499999874999937499958499731000000}
     {999997000002000000000000000000000000000000}>0.
\]

These finite certificates are deliberately not promoted to SHARP.

## 7. Weaker fallback theorem

If SHARP fails at some endpoint, the exact static reduction `L-32302` remains available.  It is enough to prove polylogarithmic optimized Cycle Debt for the stopped half-power targets

\[
p_Q(q)=q^{-1/2}\mathbf1_{q\le Q}.
\]

Positive logarithmic superposition then gives polylogarithmic critical Cycle Debt and the same RH consumer.

Thus the proposal has two nested research targets:

```text
strong target:  SHARP, zero debt for every square-root hinge;
weak target:    polylog debt for every stopped half-power prefix.
```

The strong target is preferred because it yields an elementary nonnegative flow with no downstream cycle optimization.

## 8. Exact firewalls

The proof may not use any of the following rejected shortcuts:

1. a universal weighted-BV contraction (`R-32301` gives an exact counterexample);
2. conversion of a coherent boundary to isolated divisor-source atomic norm;
3. source coefficients treated as edge coefficients;
4. finite positivity extrapolated to all `T`;
5. generic convexity of the target asserted to imply triangular inverse positivity;
6. a reviewer-supplied proof of SHARP.

A genuine completion must prove (T-32301.2) symbolically for every endpoint.

## 9. Exact status

```text
average-carry matrix identity                    PROPOSED COMPLETE EXACT
positive square-root hinge decomposition          IMPORTED / PROPOSED COMPLETE
triangular hinge inverse formula                  PROPOSED COMPLETE EXACT
directed sign certificates through T=10^6         VERIFIED FINITE
SHARP all-endpoint positivity                     OPEN / RH-BEARING
SHARP -> critical carry saturation                COMPLETE CONDITIONAL
carry saturation -> sharp prime ramp -> RH         INHERITED CONDITIONAL CHAIN
Riemann Hypothesis                                UNPROVED
```

This is a full conditional proposal, not an unconditional RH proof.  Reviewers should review a future proof of SHARP, not be asked to supply it.
