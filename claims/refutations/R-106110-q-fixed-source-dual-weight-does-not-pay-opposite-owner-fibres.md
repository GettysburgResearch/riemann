# R-106110 — A Q-fixed source-dual weight does not pay the opposite-owner fibre count

Claim ID: `R-106110`  
Programme aliases: `LFAM1.DUAL_OWNER_AMPLIFICATION_FIREWALL`, `LFAM2.Q_FIBRE_DIMENSION`, `STRESS.OPPOSITE_OWNER_COHERENCE`  
Status: **PROVED EXACT SOURCE-WEIGHT FIREWALL; THE `L-106094` DIAGONAL CLASSIFICATION AND THE DISTINCT-ANCHOR-ONLY FRONTIER OF THE FIRST `T-106090` ARE WITHDRAWN**  
Created: 2026-08-25  
Depends on: `L-106090--L-106094`, `R-106090`; parent `L-102956--L-102959`, `T-102990`  
Programme issues: #743, #736, #737  
RH status: **unproved**

The first version of `T-106090` correctly amplified the left least-discrepancy
anchor before taking a family square, but it froze the opposite semiprime owner
product `Q` and then summed the resulting positive moments with external
weight

\[
 g^2\ell Q.
\]

That construction is a valid sufficient condition if its whole moment is
separately proved.  The error was the stronger claim that its complete
same-anchor diagonal had already been paid, leaving only distinct anchors.

## 1. Exact fibre-dimension obstruction

For one fixed anchor, common core and conductor, let `z_Q` denote the scalar
Mellin--Gauss amplitude of the opposite-owner fibre `Q`.  The literal
semiprime owner coefficient contributes `Q^{-1/2}`, so the fixed-fibre energy
has the natural scale

\[
 |z_Q|^2\asymp {e_Q\over Q}
\]

with `e_Q` source-normalized independently of that reciprocal owner weight.
The Q-fixed moment uses

\[
 \sum_Q Q|z_Q|^2=\sum_Q e_Q.
\tag{R-106110.1}
\]

Thus the external source-dual factor `Q` cancels the only reciprocal owner
weight before the opposite-owner fibres are assembled.  A fixed-fibre bound
`e_Q\ll X^{o(1)}` leaves the full number of admissible `Q` fibres.

This is not a bookkeeping issue.  Take `N` distinct formal owner fibres and
put

\[
 z_{Q_j}=Q_j^{-1/2}e
\]

for one unit vector `e`.  Then

\[
 \sum_j |z_{Q_j}|^2=\sum_j{1\over Q_j},
\]

which is at most polylogarithmic for semiprime owner products, whereas

\[
 \sum_j Q_j|z_{Q_j}|^2=N.
\tag{R-106110.2}
\]

No local long-core theorem can convert (R-106110.2) to a subpower bound
without a collective estimate in `Q`.

## 2. Why the original current does not require this loss

The physical triangular current contains the coherent sum

\[
 \sum_Q z_Q
\]

before a square is taken.  Therefore the source-faithful positive completion
is

\[
 \left|\sum_Q z_Q\right|^2,
\tag{R-106110.3}
\]

not the source-blind diagonalization `sum_Q Q|z_Q|^2`.  The cross-`Q` terms in
(R-106110.3) are genuine arithmetic correlations; they must be retained inside
the principal/nonprincipal L-family member.

A scalar Cauchy step

\[
 \left|\sum_Q z_Q\right|^2
 \le \left(\sum_Q{1\over Q}\right)
      \left(\sum_Q Q|z_Q|^2\right)
\]

is formally correct, but it moves the hard opposite-owner coherence into a
positive moment whose diagonal is power-sized.  It is not a closure.

## 3. Exact status correction

The following parts of the first `T-106090` packet survive:

```text
least-discrepancy triangular incidence                 PROVED EXACT
strict roughness of the opposite reduced core          PROVED EXACT
fixed-Q even-character family                          PROVED EXACT
fixed-Q automatic long-core estimate                   PROVED
left-anchor amplification before the family square     PROVED EXACT
```

The following promotions do not survive:

```text
L-106094 complete same-anchor diagonal                  WITHDRAWN
LDRPCX106090 distinct-anchor-only principal gate        NOT THE FULL REMAINDER
LDRNEX106090 distinct-anchor-only nonprincipal gate     NOT THE FULL REMAINDER
```

Only the literal atomic diagonal, where both the anchor and opposite-owner
source atom agree, is automatically paid.  Same-anchor/different-`Q`,
different-anchor/same-`Q`, and fully distinct correlations all remain unless
removed by a separate source-faithful renewal or family theorem.

## 4. Required repair

The opposite-owner sum must be placed inside the family amplitude before the
square:

```text
sum_Q inside Z_(g,ell,sigma,h)(t)
  -> additive/Gauss family identity
  -> square once
  -> sum only the common-core and conductor source-dual weights.
```

This dual-amplified construction is `L-106110--L-106113` and `T-106110`.

## Binding consequence

```text
Q-fixed moment as a separately assumed theorem       still sufficient but overstrong
claimed paid Q-fixed diagonal                        refuted
one-sided anchor amplification                       incomplete
left-anchor AND opposite-owner amplification         required
Riemann Hypothesis                                    unproved
```
