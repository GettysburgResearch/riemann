# L-91842 — The complete root correction demand has one source-partitioned port owner

Claim ID: `L-91842`  
Status: **PROVED EXACT PSD AGGREGATION THEOREM; PR #487 SPECIALIZATION IS PORT-FREE**  
Created: 2026-08-15  
Primary inputs: the uncolored matrix inequality of `L-91320`; positive integration `L-91674`; scope firewall `L-91725`  
RH status: **unproved**

## 1. Six correction classes

For the portful recursive realization, partition the current-owned correction
source into the disjoint classes

\[
\mathcal C=
\{\mathrm{mis},\mathrm{collar},\mathrm{ref},
  \mathrm{taper},\mathrm{base},\mathrm{cur}\}.
\tag{L-91842.1}
\]

For class `c` and fibre `s`, let

\[
0\preceq D_{c,s}\preceq P_{c,s}
\tag{L-91842.2}
\]

be respectively its complete `2x2` correction demand and its own available
source-labelled port share. The shares, not merely the demands, are disjoint
parts of the root source ledger.

## 2. One aggregate inequality

With nonnegative current coefficient `b_s`, define

\[
 D=\sum_{c\in\mathcal C}\int b_sD_{c,s}\,d\mu(s),
 \qquad
 P=\sum_{c\in\mathcal C}\int b_sP_{c,s}\,d\mu(s).
\tag{L-91842.3}
\]

The PSD cone is closed under positive summation and integration, so

\[
\boxed{0\preceq D\preceq P.}
\tag{L-91842.4}
\]

The surplus

\[
\boxed{S^{\rm port}=P-D\succeq0}
\tag{L-91842.5}
\]

is retained explicitly as a current-owned matrix coordinate. It is not erased,
assigned to a child, or represented as native radix-four slack.

The invalid inference

```text
D_c <= the same full P for every c  =>  sum_c D_c <= P
```

is never used. Every class must carry its own port share before aggregation.

## 3. Separation from the native dual

The port is a separate matrix coordinate. It has no ordinary or radix-four
column and therefore

\[
\boxed{\langle Y_4,S^{\rm port}\rangle=0.}
\tag{L-91842.6}
\]

Every recursive child has zero root-global port.

## 4. PR #487 specialization

The direct one-shot row of PR #487 invokes no colored state completion, signed
finite correction row, or auxiliary Schur port. In that route

\[
P_{c,s}=D_{c,s}=0
\quad(c\in\mathcal C),
\tag{L-91842.7}
\]

so (L-91842.4) is the exact zero identity. The six-class theorem remains a
complete firewall for any reviewer who reconstructs the older portful
implementation.

## 5. Boundary

```text
six correction classes                       explicit
one port share per class                      required
aggregate demand <= aggregate port            exact
positive port surplus                         explicit current coordinate
child root port                               zero
Y4 cost of matrix port                        exactly zero
PR #487 preferred route                       port-free
Riemann Hypothesis                            unproved
```
