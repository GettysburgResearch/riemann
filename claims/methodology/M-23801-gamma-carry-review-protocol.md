# M-23801 — Adversarial review protocol for the Gamma–carry proposal

Claim ID: `M-23801`  
Status: **REVIEW PROTOCOL**  
Authoring agent: `gpt56-pro-09-u`  
Created: 2026-08-07  
Issue: #238

## Frozen review order

Review the proposal in this order.

1. `L-23801-carry-matrix-and-binomial-entropy-ledger.md`
2. `L-23803-mobius-adjoint-decoder-for-carry-elimination.md`
3. `L-23804-continuum-carry-kernel-and-probability-law.md`
4. `L-23807-finite-gamma-carry-minorant.md`
5. `L-23805-gamma-carry-convolution-factorization.md`
6. `L-23806-gamma-carry-factor-gives-sharp-finite-packing.md`
7. `T-23801-gamma-carry-packing-full-rh-proposal.md`
8. `X-23801-gamma-carry/`
9. the final report and integration handoff.

The primary hinge is `FGCM` in `L-23807`. Global GCF in `L-23805` is a
canonical stronger producer and should be reviewed separately.

## Load-bearing checks

### A. Carry normalization

Reconstruct from floors that

\[
\beta_{nq}=K_-((n+1)/q)
\]

and that the right endpoint is the minimum of `K(y/q)` on `[n,n+1]`. A wrong
integer convention reverses the packing inequality at every reset knot.

### B. Mellin constant

Reconstruct

\[
\int_1^\infty K(x)x^{-s-2}dx
={s\zeta(s+1)\over(s+1)(s+2)}
\]

and in particular the exact mass `1/2`. Any factor-of-two error destroys the
archimedean constant four.

### C. Finite minorant theorem `FGCM`

A production certificate must give a nonnegative `b_X` on `[0,log(X/2)]` and
prove all three quantitative statements:

\[
(8e^{\cdot/2}b_X)*\kappa(t)\le t,
\]

\[
1-\int b_X\le X^{-1/2+o(1)},
\]

\[
X^{-1}\int e^tb_X(t)dt\le X^{-1/2+o(1)}.
\]

Reviewers should reject:

- checking only a finite grid without monotonicity/interval closure;
- omitting a reset knot of `K`;
- an `O(1)` or fixed-power mass deficit;
- a profile with hidden negative cells;
- extrapolation from finitely many successful `X`.

A counterexample to one proposed producer does not reject the abstract `FGCM`
route; it rejects that producer. A proof that no `FGCM` certificate can exist at
some level rejects the frozen full proposal.

### D. Canonical global GCF producer

If global GCF is used, verify the gamma transform, the quotient

\[
A(s)={(s+1)(s+2)\over8s(s+1/2)^2\zeta(s+1)},
\]

the removable value `A(0)=1`, and every coefficient in the inverse density.
The term entering at `t=log n` must be exactly `mu(n)/(8n)`.

Then:

1. search quotient layers for a negative endpoint or critical value;
2. verify any proposed coupling at the level of Laplace transforms and
   independence;
3. demand all-order control, not a finite moment table;
4. require the subcritical tail moments needed to truncate GCF into FGCM;
5. mutate the first fixed-ratio Mertens cell;
6. reject total-variation, unsigned sieve, or phase-blind proofs.

Global density positivity is stronger than the finite theorem. It should not be
silently assumed merely because extensive numerical layers are positive.

### E. Finite packing

Check that the cell average is over `[n,n+1]`, that `d_X(X)=0`, and that the
change of variables gives exactly

\[
q^{-1/2}(c_X*\kappa)(\log(X/q)).
\]

No asymptotic quadrature error is permitted.

### F. Entropy rate

For the finite route, verify that the two declared mass budgets give both

\[
\frac12\sum n d_X(n)\ge4\sqrt X-X^{o(1)}
\]

and

\[
\sum d_X(n)=X^{o(1)}.
\]

The latter is needed to absorb the logarithmic entropy loss. A fixed fraction
of `sqrt(X)` is not sufficient.

### G. Landau orientation

The carry packing gives a lower bound for the prime ramp and therefore an
**upper** bound for the screw function. The final transfer must use the
upper-envelope Landau theorem. Reversing this orientation invalidates the
proof.

## Required classifications

Use the following status boundary.

```text
finite carry and Mellin identities       verify independently
FGCM finite minorants                     accept / reject as primary hinge
GCF global density                        optional stronger producer
conditional packing and RH deduction     review independently of FGCM difficulty
accepted RH proof                         only if one cofinal FGCM construction passes
```

A repair of the finite minorant after a counterexample is a new proposal and
cannot retroactively verify the frozen theorem.
