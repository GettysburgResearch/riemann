# R-26201 — High-index signed carry transport is invisible to the dyadic Möbius source

Claim ID: `R-26201`  
Title: The fixed-`q_0=2` source sees only the bottom divisor-gradient charges, so half-scale adjacent transport alone cannot prove the dyadic contraction  
Status: **EXACT STRUCTURAL REFUTATION / PIVOT**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-08  
Dependencies: `L-26201`, `L-26202`; PR #254 adjacent-flow calculus  
Scope: refutes one direct bridge only; signed transport may still contribute after an explicit bottom-charge telescope

## 1. Divisor-gradient coordinate

For a finite coefficient vector `b=(b(m))_(2<=m<=X)`, put

\[
v_q(b)
=
\sum_{m=2}^X
b(m)
\left(
\mathbf1_{q\mid m}
-
\mathbf1_{q\mid m-1}
\right).
\tag{R-26201.1}
\]

Let

\[
b_2(q)
=
\mu(q)-\mathbf1_{2\mid q}\mu(q/2).
\]

The divisor sum of `b_2` over divisors at least two is

\[
D_2(1)=0,
\qquad
D_2(2)=-2,
\qquad
D_2(m)=-1\quad(m\ge3).
\tag{R-26201.2}
\]

Therefore

\[
\boxed{
\sum_{q=2}^Xb_2(q)v_q(b)
=-2b(2)+b(3).
}
\tag{R-26201.3}
\]

The complete signed inverse-zeta source has become a dipole at the two lowest
physical coordinates.

## 2. Adjacent transport

For a flow `F_1=F_X=0`, define

\[
b_F(m)=b(m)+F_{m-1}-F_m.
\tag{R-26201.4}
\]

The exact adjacent-flow constraint change is

\[
v_q(b_F)-v_q(b)
=
\sum_{j=2}^{X-1}F_j
\left(
\mathbf1_{q\mid j+1}
-2\mathbf1_{q\mid j}
+\mathbf1_{q\mid j-1}
\right).
\tag{R-26201.5}
\]

Pairing with `b_2` and using (R-26201.2),

\[
\boxed{
\sum_q b_2(q)
[v_q(b_F)-v_q(b)]
=3F_2-F_3.
}
\tag{R-26201.6}
\]

Every flow supported at indices `j>=4` is exactly invisible.

## 3. Refuted shortcut

The following proof pattern is invalid:

```text
move signed positive defect to negative slack at indices comparable with X
-> descend every generated child below half scale
-> infer contraction of the fixed-q0=2 Möbius scalar.
```

The first two arrows may repair the full constraint vector cheaply, but the
third does not follow. The dyadic source does not see those high-index moves.
Its charge changes only when the accumulated transport reaches coordinates `2`
and `3`.

Thus neither:

- small adjacent-flow objective cost at large indices, nor
- factor-two descent of prime-power children

is by itself a contraction theorem for the RH-bearing dyadic scalar.

## 4. What survives

This refutation does not reject signed carry transport as a component. A valid
transport proof may:

1. route high-scale defect through half-scale children;
2. retain the exact signed accumulated charge along the whole descent;
3. solve every same-scale cluster;
4. emit the final coefficients at `2` and `3`;
5. prove that the resulting bottom dipole is subpower.

That production theorem is the Parity Blocker Descent target in `T-26201`.

## 5. Mutation test

A fail-closed checker must compare two flows:

- one with arbitrary rational values at `F_2,F_3`, whose projected change must
  be `3F_2-F_3`;
- one with arbitrary rational values only at `F_j`, `j>=4`, whose projected
  change must be exactly zero.

`X-26201/verify_bottom_charge.py` performs both tests.

## 6. Status boundary

Established exactly:

- bottom-dipole projection;
- high-index invisibility;
- failure of the direct high-scale transport-to-dyadic contraction.

Still open:

- a bottom-charge telescope;
- DSS/PBD;
- RH.
