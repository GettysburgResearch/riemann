# M-105390 — Hostile review contract for growing-prefix Xi capacity

Claim ID: `M-105390`  
Status: **REVIEW PROTOCOL**  
Created: 2026-08-23  
Normative compact-cell theorem: `L-105387`  
RH status: **unproved**

## Publication correction

`L-105386` contains a malformed display delimiter and is non-normative. The
clean compact-cell theorem is `L-105387`. All review and theorem dependencies
must use the corrected ID.

## Review order

1. Recheck the relative concentration estimate

   \[
   E|U/\omega_r-1|=O((r\omega_r)^{-1/2}).
   \]

2. Verify the weighted exponential version used on a fixed complex-height
   strip.
3. Check that the growing-window error is

   \[
   O((1+Y_r)/\sqrt{r\omega_r}).
   \]

4. On every critical circle, verify a cell-index-independent lower bound for
   the sine/cosine limiting derivative.
5. Check that uniqueness plus conjugation symmetry forces each actual zero to
   be real.
6. Recompute the scaled residue and atom formulas uniformly through the
   growing prefix.
7. Reconstruct the reciprocal-square Vandermonde determinant and the tail
   exponent

   \[
   d_{k,a}=3k(k-1)+2+2a.
   \]

8. Verify both error balances after taking

   \[
   J_r=r^{\gamma_k},
   \qquad
   \gamma_k<1/[2(3k(k-1)+5)].
   \]

## Quantifier firewall

The theorem proves

```text
for every fixed k and every admissible gamma_k,
all sufficiently high r have a safe first floor(r^gamma_k) prefix.
```

It does not prove:

```text
one gamma works uniformly in k;
all critical cells are real;
the omitted critical tail is dominated;
or one derivative threshold works at every matrix order.
```

## Replay boundary

`X-105390` authenticates only exact rational reciprocal-square Gram and
exponent algebra. It does not replay:

- the Xi real-saddle concentration;
- the growing complex-strip approximation;
- Rouché localization of actual Xi critical cells;
- the complete critical tail.

## Scientific boundary

```text
growing real negative central prefix             PROVED / REVIEW REQUIRED
trigonometric tail polynomial margin              PROVED EXACT
growing-prefix capacity domination                PROVED / REVIEW REQUIRED
omitted tail capacity                              OPEN
all-order simultaneous capacity                    OPEN
low-order descent                                  OPEN
Riemann Hypothesis                                 UNPROVEN
```
