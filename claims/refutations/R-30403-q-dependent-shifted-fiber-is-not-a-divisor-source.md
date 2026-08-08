# R-30403 — A carry-column-dependent shifted fiber is not a divisor source

Claim ID: `R-30403`  
Title: The coefficients `A_k(q,s),B_k(q,s)` in `L-30402` depend on the output carry column and cannot be inserted directly as coefficients of the column-independent source atoms `e_(2k),e_(2k+1)`  
Status: **EXACT SOURCE-TYPE REFUTATION**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-08  
Frozen target: PR #304 at `78b75fc17e27334a9950018528c1c6e083d74820`  
Primary target: `L-30402.8--.11`, and its use in `L-30403/T-30401`  
Dependencies: PR #272 adjacent-tree source identity; elementary finite arithmetic  
Scope: the asserted direct map from the analytic cutoff row to a divisor-source flow; the abstract adjacent-tree map for a genuine source remains valid

## 1. What the adjacent-tree map consumes

For a fixed finite source vector

\[
 \sigma=(\sigma_m)_{m\ge2},
\]

the adjacent-tree map satisfies

\[
 \Phi(\sigma)=\sum_m\sigma_mE_{m-1},
\]

and

\[
 \boxed{
 L_r(\Phi(\sigma))
 =\sum_{r\mid m}\sigma_m.
 }
\tag{R-30403.1}
\]

The coefficient `sigma_m` is one number. It cannot depend on the output carry column `r`.

Conversely, for a finite target vector `h(r)`, the unique divisor source is obtained by Möbius inversion over multiples:

\[
 \boxed{
 \sigma_m
 =\sum_{d\le N/m}\mu(d)h(md).
 }
\tag{R-30403.2}
\]

Any proposed source map must perform this inversion or an exactly equivalent recombination.

## 2. The object used in `L-30402`

The frozen proposal defines

\[
 A_k(q,s)=\frac{(2kq-1)^{-s}}{2k},
 \qquad
 B_k(q,s)=\frac{((2k+1)q)^{-s}}{2k+1},
\tag{R-30403.3}
\]

and then treats

\[
 A_k(q,s)e_{2k}-B_k(q,s)e_{2k+1}
\tag{R-30403.4}

as a divisor source.

But the symbol `q` in (R-30403.3) is the output coordinate of the finite boundary operator. Equation (R-30403.4) therefore defines a different source vector for every output column. Applying (R-30403.1) does not recover the original coordinatewise boundary value.

## 3. Minimal exact mismatch

Take

\[
 N=18,
 \qquad q_0=5,
 \qquad k=2,
 \qquad s=1.
\]

The shifted-even and unshifted-odd tails both first omit index `k=2`:

\[
 2q_0-1=9\le18,
 \qquad
 3q_0=15\le18,
\]

while

\[
 4q_0-1=19>18,
 \qquad
 5q_0=25>18.
\tag{R-30403.5}
\]

The actual zeroth common-tail boundary value at output column `q_0` is

\[
 \frac12(A_2(q_0,1)-B_2(q_0,1)).
\tag{R-30403.6}
\]

Here

\[
 A_2(5,1)=\frac1{4(20-1)}=\frac1{76},
 \qquad
 B_2(5,1)=\frac1{5(25)}=\frac1{125}.
\]

Thus

\[
 \boxed{
 \text{actual boundary value}
 =\frac12\left(\frac1{76}-\frac1{125}\right)
 =\frac{49}{19000}>0.
 }
\tag{R-30403.7}
\]

The declared divisor source is

\[
 \frac12A_2(5,1)e_4-rac12B_2(5,1)e_5.
\]

Its carry load at column `5` is instead

\[
 \begin{aligned}
 \frac12A_2(5,1)\mathbf1_{5\mid4}
 -\frac12B_2(5,1)\mathbf1_{5\mid5}
 &=-\frac1{250}.
 \end{aligned}
\tag{R-30403.8}

Therefore

\[
 \boxed{
 \frac{49}{19000}\ne-\frac1{250}.
 }
\tag{R-30403.9}
\]

The proposed flow has the wrong value in the very column from which its coefficients were computed.

## 4. What the exact checker on PR #304 verifies

`X-30401` verifies that the flow attached to the invented source

\[
 A e_{2k}-B e_{2k+1}
\]

has carry vector

\[
 A\mathbf1_{r\mid2k}-B\mathbf1_{r\mid2k+1}.
\]

That statement is correct. It does not verify that this vector equals the finite cutoff boundary function

\[
 h(q)=\sum_k[A_k(q,s)-B_k(q,s)]
\]

or any of its Euler jets. The missing equality is exactly the source-manifest map required before `Phi` may be applied.

## 5. Correct source coordinate

For a declared finite boundary vector `h(q)`, the legitimate source is

\[
 \boxed{
 \sigma_m=\sum_{d\le N/m}\mu(d)h(md).
 }
\tag{R-30403.10}
\]

This source generally mixes all output columns and all parity indices. Its atomic norm must be estimated after this exact Möbius recombination. Neither the pointwise ordering `A_k(q,s)>=B_k(q,s)` nor the fixed-`q` estimate in `L-30402.11` supplies such a bound.

## 6. Consequence

The terminal proof fails before the claimed polylogarithmic estimate:

```text
analytic boundary row h(q)
   -/-> q-dependent coefficients on fixed source nodes
   -> adjacent commutator flow.
```

The map is ill-typed. `R-30402` independently shows that even the literal source interpretation proposed in the files would have square-root atomic mass.

A repaired proof must first emit the complete boundary vector, perform (R-30403.10), replay every carry column, and only then estimate its source norm or construct a coupled flow. That is a new theorem, not a reviewer reconstruction task.

## 7. Corrected status

```text
adjacent-tree map for a genuine sigma         RETAINED
fixed-q shifted coefficient estimates          RETAINED AS SCALAR ESTIMATES
fixed-q source-to-flow replay                  RETAINED FOR THE INVENTED SOURCE
boundary-row to divisor-source identification  FALSE
L-30403/T-30401 composition                    REJECTED
correct Möbius-inverted boundary source         OPEN
RH                                              UNPROVED
```
