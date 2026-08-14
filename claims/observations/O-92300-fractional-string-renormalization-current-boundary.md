# O-92300 — Fractional-string renormalization: current boundary

Claim ID: `O-92300`  
Status: **RESEARCH BOUNDARY / NO RH CLAIM**  
Created: 2026-08-14  
RH status: **unproved**

## Closed or proposed complete on this branch

```text
safe Xi admittance, after t=x^2u scaling
    -> universal u^(-1/2) limit;

first 1/log x correction
    -> drift inside the passive family u^(-alpha_x);

limiting derivative Hankel matrix
    -> explicit beta-(alpha+1,1-alpha) moment matrix;

alpha=1/2 determinant
    -> 2^(-n(2n-1));

fixed matrix order
    -> eventually positive on the safe tail;

growing order
    -> proposed positive through
       n <= c sqrt(log x/loglog x);

finite-order completion
    -> refuted by an exact delayed-witness control.
```

## New geometric picture

A possible off-line zero

\[
\rho=\frac12+a+ib
\]

creates, at the natural squared scaling `x=b`, a pole at

\[
-1-2ia/b+O(b^{-2}).
\]

Thus it sits in a shrinking boundary layer around the negative-real cut of the
fractional-string limit.  Every fixed-order safe test converges before reaching
that layer.

## Highest-priority live theorem

Construct a source-ordered positive Krein-string/Herglotz realization that is
uniform at imaginary distance `O(1/x)` from the cut.  In the notation of
`T-92300`, prove `NCFSC`.

The most promising consumers are:

1. a pair-adapted nonconfluent Cauchy/Loewner packet;
2. a near-cut Schur complement of the completed arithmetic Julia cascade;
3. a rational boundary microscope whose source norm remains positive;
4. a direct coupling between the prime Poisson-Fock output and the homogeneous
   fractional string.

## Firewalls

```text
more fixed derivatives                         insufficient;
more adjacent 2x2 Hankel minors                 insufficient;
ordinary concavity                              insufficient;
any prescribed finite Loewner order             insufficient;
compact-subset asymptotics away from the cut    insufficient.
```

The full near-cut Pick/Herglotz sign remains RH-equivalent.
