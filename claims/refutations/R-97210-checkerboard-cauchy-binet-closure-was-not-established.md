# R-97210 — The advertised checkerboard/Cauchy–Binet/full-Hall closure was not established

Claim ID: `R-97210`  
Status: **EXACT INTERFACE REFUTATION AND PUBLICATION RECONCILIATION**  
Created: 2026-08-17  
Frozen publication: PR #567 at `50e596560b4f6f423e87fd6718d74913d863df99`  
RH status: **unproved**

An earlier assistant response described a stronger packet with:

1. a literal-history incidence matrix \(H_X\);
2. a terminal target/scalar matrix \(K_X\) satisfying checkerboard inequalities;
3. a Cauchy–Binet passage to a root matrix \(M_X=H_XK_X\);
4. a global Hall coefficient vector proving the \(5{:}3\) scalar nonnegative.

No theorem files or authenticated certificate for items 2–4 were published.
PR #567 deliberately retracts to `GPHT* / TFPE / ACBI` **OPEN**.

Two asserted implications in the unpublished description are invalid without
additional hypotheses.

## 1. Unique ownership does not imply nonnegative incidence minors

The nonnegative one-owner matrix

\[
H=
\begin{pmatrix}
0&1\\
1&0
\end{pmatrix}
\]

has exactly one nonzero entry in each source column, but

\[
\det H=-1.
\]

Hence “one terminal owner per source column” does not imply that every minor is
zero or a positive monomial. A compatible order-preservation or sign-regularity
theorem is required.

## 2. Positive leaf coordinates do not imply a terminal checkerboard

The matrix

\[
K=
\begin{pmatrix}
1&2\\
2&1
\end{pmatrix}
\]

has strictly positive target and scalar coordinates in every row, yet

\[
\det K=-3.
\]

Therefore canonical leafwise positivity, even when valid, does not imply the
cross-leaf determinant inequalities required by the proposed checkerboard.

## 3. Cauchy–Binet is conditional, not corrective

For \(M=HK\), Cauchy–Binet is exact. It gives a sign conclusion only after the
relevant minors of both factors have compatible signs. With \(H=I_2\) and the
positive-entry matrix \(K\) above,

\[
\det(HK)=\det K=-3.
\]

Thus Cauchy–Binet cannot manufacture the missing terminal or owner-order signs.

## 4. Global Hall remains a separate arithmetic inequality

Even a totally nonnegative target/scalar matrix would not by itself prove that
the available even target capacity reaches the complete odd demand inside the
coefficient box. The exact finite problem is the Lorenz/fractional-knapsack
inequality in `L-97211`; uniform validity is precisely the open producer
`GPHT*`, equivalently the `TFPE/ACBI` frontier recorded in PR #564.

```text
parity-covariant owner ledger                  exact
owner-incidence total nonnegativity            not derived; naive inference false
terminal checkerboard                          not derived
Cauchy–Binet identity                          exact conditional algebra
global Hall / Lorenz arithmetic inequality     open / RH-bearing
PR #567                                        intentional fail-closed retraction
Riemann Hypothesis                             unproved
```
