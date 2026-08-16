# R-94100 — An exact all-row native compiler is the full SHARP positivity theorem, not a composition lemma

Claim ID: `R-94100`  
Status: **PROVED EXACT CONE EQUIVALENCE / FAIL-CLOSED SEPARATOR**  
Created: 2026-08-16  
Frozen reconstruction target: PR #511 at `6ece82279cb03474ebc79914db572f6ff095d238`  
Review inputs: PRs #512, #514, #516, #521, #525, #527  
RH status: **unproved**

## 1. The native row

For an integer endpoint `X`, the exact native Möbius component row is

\[
 c_X(j)=\sum_{k\le X/j}\frac{\mu(k)}{\sqrt k}Q_{X/k}(j),
 \qquad j\ge2.
 \tag{R-94100.1}
\]

The frozen native-normalization theorem gives, for this same row,

\[
 C_{c_X}=w_X,
 \qquad
 \Xi_{c_X}=\Omega_X,
 \qquad
 \mathcal H(c_X)=J_\Lambda(X).
 \tag{R-94100.2}
\]

No coefficientwise sign is implied by these identities.

## 2. Exact all-row preservation has no hidden freedom

Suppose a proposed joint source-to-physical compiler has a positive output
measure and therefore a coefficientwise nonnegative physical row `d_X`. Assume
that the certificate claims exact equality in **every** component-row
coordinate:

\[
 d_X(j)=c_X(j)
 \qquad(j\ge2).
 \tag{R-94100.3}
\]

Then necessarily

\[
 \boxed{c_X(j)\ge0\quad(j\ge2).}
 \tag{R-94100.4}
\]

Conversely, if (R-94100.4) holds, the row itself is a nonnegative physical row
and already has every exact ordinary, radix-four and score coordinate in
(R-94100.2). Thus, at component-row scope,

\[
 \boxed{
 \text{positive exact all-row realization of the native datum}
 \iff c_X\ge0.
 }
 \tag{R-94100.5}
\]

Source labels, Hall incidences, least-prime owners, parity channels, child
histories and endpoint fibres can document a representation. They cannot alter
this cone equivalence after exact row equality is required.

## 3. Exact Farkas separator

If one coordinate is negative, say

\[
 c_X(j_0)<0,
\]

then the coordinate functional

\[
 \ell_{j_0}(d)=d(j_0)
\]

belongs to the dual cone of nonnegative rows and satisfies

\[
 \ell_{j_0}(d)\ge0
 \quad\text{for every positive physical row }d,
 \qquad
 \ell_{j_0}(c_X)<0.
 \tag{R-94100.6}
\]

This is an exact one-coordinate Farkas separator. No higher-dimensional LP,
new source ownership convention, or quantizer can remove it.

## 4. Consequence of the negative oriented-child coordinate

Reviews #512/#514 and the live source registry in PR #521 prove that the
actual oriented rough-child aggregate has negative ordinary response at
`q=2`. Hence it cannot enter the positive physical cone as a separate branch.
It must first cancel against the finite forcing in the signed paired source.

After that cancellation, however, an exact compiler preserving every row is
again required to output precisely `c_X`. Therefore joint cancellation repairs
the **normalization order**, but it does not make the final row-positive theorem
a formal consequence of source splitting.

## 5. Why this is RH-bearing

If (R-94100.4) held for all sufficiently large `X`, then the native row itself
would be feasible with zero native deficit:

\[
 J_\Lambda(X)-\mathcal H(c_X)=0.
\]

The frozen one-sided endpoint consumer would then yield the proposed RH
conclusion. Thus an unconditional exact all-row compiler is already a complete
producer theorem of the project; it cannot be imported as harmless glue.

## 6. Correct replacement target

A noncircular producer must relax exact row equality. It should construct a
nonnegative row `d_X` satisfying

\[
 \Xi_{d_X}\le\Omega_X,
 \qquad
 C_{d_X}\le w_X,
\]

and make the weighted native deficit

\[
 \sum_qY_4(q)[\Omega_X(q)-\Xi_{d_X}(q)]
\]

small. The endpoint-scale compiler in `L-94100--L-94102` does this without
branchwise Möbius realization, Target-Lorenz tails, activation-cell
quantization, or rough-child promotion.

```text
negative oriented child -> branchwise positive row      IMPOSSIBLE
joint cancellation before positive observation           NECESSARY
exact final equality in every component row              EQUIVALENT TO c_X>=0
negative coordinate                                      EXACT FARKAS SEPARATOR
capacity-subordinate positive minorant                    CORRECT RELAXATION
Riemann Hypothesis                                        UNPROVED
```
