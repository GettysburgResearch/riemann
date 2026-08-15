# L-92883 — One positive reserve pays every physical root correction at logarithmic native cost

Claim ID: `L-92883`
Status: **PROVED COST COMPILATION ON THE FROZEN SOURCE-RESERVE AND ROOT-MASS INPUTS — REVIEW REQUIRED**
Created: 2026-08-15
Primary inputs: `L-91378`, `L-91385`, `L-91733`, `L-91734`, `L-91737`, `L-91843`, `L-92882`
RH status: **unproved**

## 1. Positive unused-source reserve

The sequential ledger expresses the unused detail vector `r_X` as the observation of disjoint positive source packets produced by thinning, omissions, activation collars, retained-cell comparison and terminal reserve. Denote their sum by `R_X^phys`.

Because these packets are disjoint subpackets of the retained positive root source,

\[
m(R_X^{\rm phys})
\le
m(P_X^{\rm ret})<3020
\]

by `L-91737`.

## 2. Exact native dual pairing

By `L-91378`,

\[
\langle Y_4,r_X\rangle
=
\mathcal H(R_X^{\rm phys}).
\]

The zero-row positive-packet estimate `L-91385` gives

\[
\mathcal H(R_X^{\rm phys})
\le
5\log(3X)m(R_X^{\rm phys}).
\]

Hence

\[
\boxed{
\langle Y_4,r_X\rangle
<15100\log(3X).
}
\tag{L-92883.1}
\]

This is a response-level bound for the actual unused packet. It does not label a signed mismatch as positive.

## 3. Port and finite base

The direct-sum port of `L-92882` has zero `Y_4` coordinate. Under the optional auxiliary-packet representation, the frozen mass bound `m_port<14/3` gives the conservative additional cost

\[
5\log(3X)m_{\rm port}<\frac{70}{3}\log(3X).
\]

Stop recursion at `X<=134` and use the explicit finite-base constant

\[
C_{\rm base}=2\sqrt{134}\log^2(268).
\]

Thus the fully conservative root bound is

\[
\boxed{
\delta_X^{\rm root}
:=\langle Y_4,r_X\rangle
<15124\log(3X)+C_{\rm base}.
}
\tag{L-92883.2}
\]

In the preferred direct-sum port model, replace `15124` by `15100`.

## 4. No reversed score inequality

No step infers a thinning loss upper bound from score superordination. The cost is bounded directly by the native `Y_4` pairing of a positive reserve. This repairs the reversed inequality identified in the PR #481 review lineage.

## 5. Comparison with PR #488

PR #488 obtains the stronger one-shot uniform estimate

\[
\delta_X<61000
\]

from explicit named slack classes. The present logarithmic estimate is weaker asymptotically but logically independent: it uses positive reserve mass and the exact zero-row logarithmic debt theorem.

## 6. Boundary

```text
unused source reserve                         positive / source-disjoint
reserve target mass                           <3020
reserve Y4 cost                               <15100 log(3X)
aggregate direct-sum port cost                zero
auxiliary port fallback                       <(70/3) log(3X)
finite base                                   explicit constant
score-superordination reversal                not used
PR #488 one-shot cost                         stronger / independent
Riemann Hypothesis                            unproved
```
