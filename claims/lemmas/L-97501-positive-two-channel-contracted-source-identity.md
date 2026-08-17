# L-97501 — The raw rough source has an exact positive two-channel contracted identity

Claim ID: `L-97501`  
Status: **PROVED EXACT SOURCE THEOREM**  
Created: 2026-08-18  
RH status: **not assumed**

## 1. Paired source category

Let a source packet be `P=(P^+,P^-)` in the positive cone. Let

\[
 S(P^+,P^-)=(P^-,P^+)
\]

and let signed observation be `ell(P)=ell_+(P^+)-ell_+(P^-)`, so
`ell(SP)=-ell(P)`.

Suppose the literal raw first-owner identity at node `v` is

\[
 \boxed{
 P_v=B_v\oplus\bigoplus_{w} r_{v,w}S P_w,
 } \tag{L-97501.1}
\]

where the direct sum is source-disjoint and every `r_(v,w)>=0` is the actual
rough coefficient.

## 2. Arbitrary safe contraction

Choose any

\[
 0\le t_{v,w}\le r_{v,w}.
\]

Define the current packet

\[
 \boxed{
 C_v(t)=B_v\oplus
 \bigoplus_w(r_{v,w}-t_{v,w})S P_w.
 } \tag{L-97501.2}
\]

Then

\[
 \boxed{
 P_v=C_v(t)\oplus\bigoplus_w t_{v,w}S P_w.
 } \tag{L-97501.3}
\]

Every packet on the right is positive; first ownership, activation, source
index, and the complete raw coefficient are retained exactly:

\[
 (r_{v,w}-t_{v,w})+t_{v,w}=r_{v,w}. \tag{L-97501.4}
\]

Thus the literal source identity missing from PR #576 exists in the paired
source cone. What cannot in general be positive is its **one-channel signed
current observation**.

## 3. Signed scalar

Let

\[
 b_v=\ell(B_v),\quad f_v=\ell(P_v),\quad c_v=\ell(C_v(t)).
\]

Then

\[
 \boxed{
 f_v=b_v-\sum_w r_{v,w}f_w,
 } \tag{L-97501.5}
\]

\[
 \boxed{
 c_v=b_v-\sum_w(r_{v,w}-t_{v,w})f_w,
 } \tag{L-97501.6}
\]

and

\[
 \boxed{
 f_v=c_v-\sum_wt_{v,w}f_w.
 } \tag{L-97501.7}
\]

Equations (L-97501.6)--(L-97501.7) are exactly the resolvent transfer of
`L-97500`.

## 4. Minimality

There is no nonzero positive scalar functional `phi` on the paired cone with

\[
 \phi(SP)=-\phi(P)
\]

for every positive `P`: both sides would have opposite signs while `phi(P)` and
`phi(SP)` are nonnegative. Hence two positive parity channels are the minimal
source-faithful realization of the sign character.
