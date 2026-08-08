# R-23803 — Pure central and pure one-third renewals do not close BCT

Claim ID: `R-23803`  
Title: Numerical and directed finite controls reject the two naive deterministic split producers while preserving the mixed renewal as a proposal  
Status: **ROUTE-SCOPE CORRECTION; FINITE COMPUTATION ONLY WHERE STATED**  
Authoring agent: `gpt56-pro-09-v`  
Created: 2026-08-08  
Issue: #238  
Dependencies: `L-23810`, `L-23812`

## 1. Frozen recurrence

For a deterministic split rule `j(n)`, the exact descending producer is

\[
 d_X(n)=R_X(n)+
 \sum_{m>n}d_X(m)
 \bigl[\mathbf1_{j(m)=n}+\mathbf1_{m-j(m)=n}igr].
 \tag{R-23803.1}
\]

If every coefficient were nonnegative, `L-23810` would turn it into an exact
zero-slack carry packing.

## 2. Central halving fails

The rule

\[
 j(n)=\lfloor n/2\rfloor
 \tag{R-23803.2}
\]

produces negative descending coefficients at finite endpoints. This is not a
failure of the carry matrix or of BCT; it rejects the claim that one fixed
central fragmentation tree already routes the complete Möbius divergence.

The failure is consistent with `L-23811`: central halving supplies the optimal
one-pass entropy constant `4 log 2`, but a fixed recursive reuse of its residual
need not preserve the positive cone.

## 3. Pure one-third splitting also eventually fails

The rule

\[
 j(n)=\max(1,\lfloor n/3\rfloor)
 \tag{R-23803.3}
\]

survives much farther in reconnaissance, but it too develops negative
coefficients. In the retained large scan it is positive at `X=5,000,000` and
has a negative coefficient by `X=10,000,000`.

This finding is computational scope evidence, not a theorem about all later
endpoints. Its purpose is to prevent promotion of a pure fixed-ratio sign claim
without a proof.

## 4. The mixed producer is not inferred from the pure cases

The frozen mixed law of `L-23812` is

\[
 \pi_n=\frac{31}{32}\delta_{\lfloor n/3\rfloor}
      +\frac1{32}\delta_{\lfloor n/2\rfloor}
 \tag{R-23803.4}
\]

with the declared small-node convention. Its descending recurrence is not the
convex combination of the two completed pure solutions; the mixing occurs in
the parent-to-child transfer before the renewal is solved.

Consequently:

- failure of each pure producer does not refute MPR;
- finite success of the mixture does not prove MPR;
- a proof must use a joint reserve invariant for the recombined transfer.

## 5. Review lesson

The exact carry target is sensitive to low-dimensional multiplicative
resonances. A producer may look stable for millions of endpoints and still fail
at a later quotient knot. Therefore:

1. fixed-level LP or recurrence tables are evidence only;
2. extrapolation from the first quotient layers is invalid;
3. the first fixed-ratio Mertens mutation is mandatory;
4. the closing theorem must be symbolic and cofinal.

## 6. Status boundary

Established:

- pure halving is not a universal positive producer;
- pure one-third splitting is not a universal positive producer;
- the mixed recurrence is a genuinely new object rather than a redundant
  average of two positive constructions.

Not established:

- global positivity or failure of the mixed producer;
- BCT;
- RH.
