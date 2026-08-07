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
4. `L-23805-gamma-carry-convolution-factorization.md`
5. `L-23806-gamma-carry-factor-gives-sharp-finite-packing.md`
6. `T-23801-gamma-carry-packing-full-rh-proposal.md`
7. `X-23801-gamma-carry/`
8. the final report and integration handoff.

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

### C. Gamma quotient

Verify the gamma transform, the quotient

\[
A(s)={(s+1)(s+2)\over8s(s+1/2)^2\zeta(s+1)},
\]

the removable value `A(0)=1`, and every coefficient in the inverse density.
The term entering at `t=log n` must be exactly `mu(n)/(8n)`.

### D. GCF

This is the sole substantive sign theorem. A reviewer should:

1. search quotient layers for a negative endpoint or critical value;
2. verify any proposed direct coupling at the level of Laplace transforms and
   independence;
3. demand all-order control, not a finite moment table;
4. mutate the first fixed-ratio Mertens cell;
5. reject total-variation, unsigned sieve, or phase-blind proofs.

A counterexample to `a(t)>=0` rejects the proposal. A correct proof of GCF is a
new proof of RH through the remaining exact arrows.

### E. Finite packing

Check that the cell average is over `[n,n+1]`, that `d_X(X)=0`, and that the
change of variables gives exactly `q^-1/2(c*kappa)(log(X/q))`. No asymptotic
quadrature error is permitted.

### F. Entropy rate

Verify both exponential-moment losses. The proof needs only

\[
A(-\eta)<\infty,
\qquad0<\eta<1/2,
\]

under GCF. Confirm that the entropy correction is `X^epsilon`, not a fixed
fraction of `sqrt(X)`.

### G. Landau orientation

The carry packing gives a lower bound for the prime ramp and therefore an
**upper** bound for the screw function. The final transfer must use the
upper-envelope Landau theorem. Reversing this orientation invalidates the
proof.

## Required classifications

Use the following status boundary.

```text
finite carry and Mellin identities       verify independently
GCF density sign                         accept / reject separately
conditional packing and RH deduction     do not reject merely because GCF is hard
accepted RH proof                         only if GCF and every transfer pass
```

A repair of GCF after a counterexample is a new proposal and cannot
retroactively verify the frozen theorem.
