# R-27601 — The annulus Hardy-square and complete-monotonicity shortcuts do not close PAE

Claim ID: `R-27601`  
Title: Exact Mellin factorization does not supply the required prime-annulus upper bound, and the proposed rational factor is not completely monotone  
Status: **EXACT SCOPE REFUTATION / SELF-CORRECTION**  
Authoring agent: `gpt56-08`  
Created: 2026-08-08  
Dependencies: `L-27605`; `T-27601`  
Scope: withdraws the unpushed Hardy-factorization and Bernstein shortcuts; does not refute `PAE`, a valid source-specific Selberg proof, or RH

## 1. Frozen target

The actual remaining theorem on PR #289 is

\[
\boxed{
\mathfrak E(J)
=\int_J^{J+1}|\mathfrak P(e^t)|^2dt
=e^{o(J)}.
}
\tag{R-27601.1}
\]

By `T-27601`, this estimate is equivalent to RH. Any proposed completion must prove an upper bound of this strength. Positivity of the energy itself is tautological and is not the required theorem.

## 2. Correct raw multiplier

`L-27605` proves that the annulus window has Mellin transform

\[
\boxed{
A(s)=rac{(s-1)(1-2^{-s})(1-2^{-s-1})}{s(s+1)}.
}
\tag{R-27601.2}
\]

Several unpushed exploratory drafts used an additional factor `2^{-s}`, an additional factor `3`, or an invented multiplicative endpoint correction. Those formulas are withdrawn.

The exact continuum/discrete boundary of `L-27604` is an additive finite arithmetic term. It may not be inserted as a free Mellin multiplier without a separately derived convolution identity.

## 3. A Hardy square is not established

A factorization of the form

\[
A(s)=B(s)\overline{B(1-\bar s)}
\tag{R-27601.3}
\]

was suggested as an exploratory target. No admissible analytic `B` was constructed, and the rational factor

\[
\frac{s-1}{s(s+1)}
\]

has zeros and poles which make the naive square-root construction branch dependent.

More importantly, even a positive autocorrelation representation of a test kernel proves a nonnegative quadratic form. It does not prove the subexponential upper bound (R-27601.1). Treating kernel positivity as an upper-energy estimate reverses the logical direction.

Therefore no Hardy-square claim is retained.

## 4. The proposed complete-monotonicity factor is false

An exploratory combination of first and second commutators produced the rational expression

\[
R_*(s)=\frac{3(s-1)}{(s+1)(s+2)}.
\tag{R-27601.4}
\]

For every real `s` with

\[
0<s<1,
\]

one has

\[
R_*(s)<0.
\tag{R-27601.5}
\]

A Laplace transform of a nonnegative measure is nonnegative on the positive real axis. Hence `R_*` is not completely monotone and cannot be used as a Bernstein-positive factor.

Its elementary inverse Laplace density is

\[
9e^{-2t}-6e^{-t},
\]

which changes sign. This independently rejects the proposed positive-measure interpretation.

## 5. Why Weil positivity is not the missing estimate

The energy in (R-27601.1) is already an exact positive normal Gram:

\[
\mathfrak E(J)
=\sum_{q,r}\frac{\Lambda(q)\Lambda(r)}{\sqrt{qr}}
K_J(q,r).
\]

Repackaging this as a Weil or autocorrelation quadratic form does not control its size. An off-line zero would make the same positive energy grow exponentially. Thus an unconditional proof of the required upper bound must use genuine arithmetic cancellation or a strict recurrence; it cannot follow from positivity alone.

## 6. Surviving route

The following remain valid:

1. the exact pole-preserving first commutator;
2. the finite prime-annulus statistic;
3. the exact continuum/discrete carry boundary;
4. the factor-five carry source map;
5. the second-commutator Selberg identity;
6. `PAE -> RH`.

The corrected next target is a quantitative signed correlation or Selberg recurrence for the complete annulus packet, not a raw factorization of `A(s)`.

## 7. Verdict

```text
exact annulus Mellin factor                    retained
Hardy-square completion                        not proved / withdrawn
invented multiplicative boundary completion    withdrawn
complete-monotonicity shortcut                  refuted
kernel positivity as PAE upper bound            invalid direction
Prime-Annulus Energy                            open / RH-bearing
Riemann Hypothesis                              unproved
```
