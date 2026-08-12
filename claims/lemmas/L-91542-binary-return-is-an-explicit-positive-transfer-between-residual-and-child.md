# L-91542 — The binary return is an explicit positive transfer between the exact arithmetic residual and child

Claim ID: `L-91542`  
Status: **PROVED EXACT ONE-PRIME SCALAR NORMAL FORM — ROW NORMALIZATION STILL OPEN**  
Created: 2026-08-13  
Frozen inputs: PR `#399` at `22d7f2f3f3668f664c09708838f6a738e4398eef`; PR `#416` at `23aa9adc48a6c3176b799944dfbac11e665407ef`  
Depends on: `L-91540`  
RH status: **unproved**

## 1. Active one-prime sector

Put

\[
 r=p^{-1/2},
 \qquad
 A=1-r^2,
 \qquad
 B=1-r,
 \qquad
 d=r(1-r),
\]

and let

\[
 z=\sqrt{x/n}.
\]

This lemma concerns the active child sector \(n\le x/p\), so

\[
 rz\ge1.
 \tag{L-91542.1}
\]

The native target and score atoms, with the common factor \(n^{-1/2}\)
suppressed, are

\[
 T_0=4z-3,
 \qquad
 S_0=5z-3.
 \tag{L-91542.2}
\]

The canonically scaled child atoms at endpoint \(x/p\) are

\[
 T_c=r(4rz-3),
 \qquad
 S_c=r(5rz-3).
 \tag{L-91542.3}
\]

Hence the exact arithmetic residual is

\[
 \boxed{
 T_a=T_0-T_c=(1-r)\,[4(1+r)z-3],
 }
 \tag{L-91542.4}
\]

\[
 \boxed{
 S_a=S_0-S_c=(1-r)\,[5(1+r)z-3].
 }
 \tag{L-91542.5}
\]

## 2. Binary survival and hazard atoms

The frozen binary-return branch has

\[
 T_s=(1-r)(r+3)
 \left[\frac{2(r+2)}{r+3}z-1\right],
 \tag{L-91542.6}
\]

\[
 T_h=r(r+2)
 \left[\frac{2(r+1)}{r+2}z-1\right],
 \tag{L-91542.7}
\]

\[
 S_s=(1-r^2)(5z-3),
 \tag{L-91542.8}
\]

\[
 S_h=r\big[(4r+1)z-(2r+1)\big].
 \tag{L-91542.9}
\]

They satisfy the parent telescope

\[
 T_s+T_h=T_0,
 \qquad
 S_s+S_h=S_0+d(z-1).
 \tag{L-91542.10}
\]

## 3. Exact transfer normal form

Direct subtraction gives

\[
 \boxed{
 T_a-T_s=T_h-T_c=d(2z+1).
 }
 \tag{L-91542.11}
\]

Thus the binary return moves the positive target packet

\[
 \mathcal C_T=d(2z+1)
 \tag{L-91542.12}
\]

from the exact current-generation residual to the contracted child.

On the score side,

\[
 \boxed{
 S_a-S_s=3d,
 }
 \tag{L-91542.13}
\]

while

\[
 \boxed{
 S_h-S_c=d(z+2).
 }
 \tag{L-91542.14}
\]

The difference between the score received by the hazard child and the score
removed from survival is exactly

\[
 \boxed{
 d(z+2)-3d=d(z-1)\ge0,
 }
 \tag{L-91542.15}
\]

the target-null favorable score surplus of the binary telescope.

Equivalently,

\[
 \boxed{
 \begin{aligned}
 (T_s,S_s)&=(T_a,S_a)-\big(d(2z+1),3d\big),\\
 (T_h,S_h)&=(T_c,S_c)+\big(d(2z+1),d(z+2)\big).
 \end{aligned}
 }
 \tag{L-91542.16}
\]

## 4. The child correction is one positive physical packet

Restore the common factor \(n^{-1/2}\).  The correction added to the child is

\[
 \boxed{
 \begin{aligned}
 \mathcal C_T
 &=d\left(2\frac{\sqrt x}{n}+\frac1{\sqrt n}\right),\\
 \mathcal C_S
 &=d\left(\frac{\sqrt x}{n}+\frac2{\sqrt n}\right).
 \end{aligned}
 }
 \tag{L-91542.17}
\]

Its target-per-score ratio is

\[
 q_C(z)=\frac{2z+1}{z+2}.
 \tag{L-91542.18}
\]

For \(z\ge1\),

\[
 q_C(1)=1,
 \qquad
 q_C'(z)=\frac3{(z+2)^2}>0,
 \qquad
 q_C(z)<2.
 \tag{L-91542.19}
\]

Therefore the correction lies strictly inside the positive physical two-ledger
cone.  Its inverse physical coordinates are especially simple:

\[
 \boxed{
 L_C=\frac{2\mathcal C_S-\mathcal C_T}{3}
     =\frac d{\sqrt n},
 \qquad
 R_C=\frac{2\mathcal C_T-\mathcal C_S}{3}
     =d\frac{\sqrt x}{n}.
 }
 \tag{L-91542.20}
\]

It is one positive constant endpoint channel plus one positive harmonic
channel.  No signed state is hidden in the scalar transfer.

## 5. What this closes

The scalar normalization match between the exact arithmetic split and the
binary-return split is now explicit:

```text
exact arithmetic residual + exact contracted child
        =
binary survival + binary hazard
```

in target, while the binary score is larger by the positive target-null amount
\(d(z-1)\).

The remaining one-step audit is not scalar.  It is to prove that the same
transfer is implemented by the exact component-row/affine-pushforward diagram,
with the constant and harmonic correction charged once through the resident
positive row and endpoint-port packets.

## 6. Scope firewall

This theorem does not infer a row identity from equality of target and score
kernels.  The component row \(Q_Y(j)\) depends on the endpoint \(Y\), so replacing

\[
 K_x-rK_{x/p}
\]

by a single reparameterized scalar channel is not a valid row argument.

```text
exact arithmetic target/score split                  EXACT
binary target transfer normal form                    EXACT
target-null favorable score surplus                   EXACT
child correction in positive physical cone            EXACT
constant-plus-harmonic correction coordinates         EXACT
component-row transfer identity                       OPEN
affine child/collar normalization                      OPEN
Riemann Hypothesis                                    UNPROVEN
```
