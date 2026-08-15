# L-93902 — The `P_61` stopped leaf has one explicit live two-channel Target-Lorenz certificate

Claim ID: `L-93902`  
Status: **PROVED EXACT GENERATOR FORMULA; UNIVERSAL SIGNS FROM THE COMPLETE AVLT**  
Created: 2026-08-16  
Inputs: `L-91362`, `L-91682`, `L-91720`, `L-93602`, `L-93783`, `L-93900`  
Replay: `X-93900-live-native-compiler`  
RH status: **unproved**

## 1. Explicit source occurrences

Fix

\[
p\ge67,
\qquad1\le y<67,
\qquad d\mid P_{61},
\qquad d\le py.
\]

The occurrence label is

\[
\omega=(p,y,d,\mu(d),\text{parent},\text{actual child},\text{first owner}).
\]

Its actual parent and child endpoints are `py/d` and `y/d`, and the child
coefficient is exactly `p^{-1/2}` once.

The generator evaluates

\[
K_T(d),\quad K_S(d),\quad
K_R^{(j)}(d)
=\frac1{\sqrt d}
 [Q_{py/d}(j)-p^{-1/2}Q_{y/d}(j)]
\]

for every active component row, together with

\[
K_\Gamma^{(q)}(d)
=\frac1{\sqrt d}
 [C_{py/d}(q)-p^{-1/2}C_{y/d}(q)]
\]

at `q` and `4q`.  Detail is formed only after those two ordinary values are
assembled on the same source coefficients.

## 2. Exact equality/reserve subchannels

Each occurrence is deterministically decomposed as

\[
A_d^{E}
=(E_{p,y}(d),2E_{p,y}(d),K_R(d),K_\Gamma(d),K_\Xi(d)),
\]

\[
A_d^{R}
=(2R_{p,y}(d),R_{p,y}(d),0,0,0),
\]

whose sum is the original target/score/row packet.  Both subchannels retain the
same occurrence and actual-child owner.

## 3. One Target-Lorenz coefficient vector

Let `E` and `O` be the positive even and odd occurrence measures in the **total
SHARP target** `K_T`.  The leftmost Target-Lorenz coefficients satisfy

\[
0\le u_d\le1,
\qquad
\sum_{\mu(d)=1}u_dK_T(d)
=
\sum_{\mu(d)=-1}K_T(d).
\tag{L-93902.1}
\]

The coefficient `u_d` is applied to both `A_d^E` and `A_d^R`.  Define the
literal residual arithmetic source

\[
\nu=E-U.
\]

The complete AVLT gives, simultaneously for every component row,

\[
B_j
=\sum_{\mu(d)=1}u_dK_R^{(j)}(d)
 -\sum_{\mu(d)=-1}K_R^{(j)}(d)
\ge0.
\tag{L-93902.2}
\]

The score-optimality theorem gives

\[
\sigma
=\sum_{\mu(d)=-1}K_S(d)
 -\sum_{\mu(d)=1}u_dK_S(d)
\ge0.
\tag{L-93902.3}
\]

The exact typed output is

```text
positive arithmetic residual source   nu;
current-only nonnegative row bonus     B;
explicit declared-score surplus        sigma.
```

It obeys

\[
T(\nu)=T(E)-T(O),
\]

\[
S(\nu)=S(E)-S(O)+\sigma,
\]

\[
R(\nu)+B=R(E)-R(O).
\tag{L-93902.4}
\]

The row bonus has zero source target by type and is never sent to a child.

## 4. Every physical coordinate

Apply the positive ordinary response map to (L-93902.4) at `q` and `4q`
separately.  The same `u_d` is used in both.  After the common sums, define

\[
\Xi(q)=\Gamma(q)-2\Gamma(4q).
\]

This yields one certificate containing target, declared score, literal score,
every component row, every ordinary column, every radix-four column, actual
child incidences, and one owner per occurrence.

## 5. Live certificate replacing the toy boundary

`X-93900` generates the hostile leaf

\[
(p,y)=(67,13)
\]

from the actual formulas.  It enumerates `229` active `P_61` occurrences,
records each parent/child coefficient and owner, evaluates all `870` component
rows and all `870` ordinary/detail columns through endpoint `871`, and verifies
one common Target-Lorenz coefficient vector.

The retained strict minima are approximately

```text
positive component row  >3.9036e-5;
positive ordinary       >3.8946e-5;
positive detail         >3.8946e-5;
score surplus           >2.6219.
```

A targeted grid also evaluates `p=67`, `y in {1,2,13,33,66}`, rows `2..66`.
The universal sign theorem is `L-93602`; the live file is its arithmetic
compiler and fail-closed reconstruction, not a substitute toy vector.

```text
explicit Möbius occurrences                complete
actual child endpoint/coefficient           complete
target/score channels                       exact
one Target-Lorenz coefficient vector        exact
all component rows                          generated
ordinary q and 4q                           generated before detail
ownership                                   one source/child owner
universal positivity                        complete AVLT input
Riemann Hypothesis                          unproved
```
