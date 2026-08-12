# L-91423 — A unique root-locked safe scale collapses the three-scale quasi-Lévy source to one positive prime channel and one fixed-sign continuous channel

Claim ID: `L-91423`  
Status: **PROVED EXACT SIGN-GEOMETRY THEOREM; TWO-CHANNEL HARDY DOMINATION REMAINS OPEN**  
Created: 2026-08-12  
Depends on: `L-91404`, `L-91410`, `T-91005`  
RH status: **unproved**

## 1. The normalized Cauchy residual

Write

\[
\mathfrak r_a(u)=aR(a|u|),
\tag{L-91423.1}
\]

where

\[
\boxed{
R(x)=
-\frac14(1+x)e^{-x}
+\frac{17}{32}(1+2x)e^{-2x}
-\frac1{16}(1+4x)e^{-4x}.
}
\tag{L-91423.2}
\]

The exact three-scale source coefficient of `L-91404` is

\[
\boxed{
c_a(u)
=
-2a^{-4}\mathfrak r_a(u)
=
-2a^{-3}R(au)
\qquad(u>0).
}
\tag{L-91423.3}
\]

## 2. One zero of the residual profile

One has

\[
R(0)=\frac7{32},
\qquad
\int_0^\infty R(x)\,dx=0,
\tag{L-91423.4}
\]

and

\[
\boxed{
R'(x)
=
\frac{x e^{-4x}}8
\left(2e^{3x}-17e^{2x}+8\right).
}
\tag{L-91423.5}
\]

Put

\[
P(y)=2y^3-17y^2+8.
\]

For \(y\ge1\),

\[
P'(y)=2y(3y-17).
\]

Thus \(P\) decreases on \([1,17/3]\), increases afterward, satisfies \(P(1)<0\), and tends to \(+\infty\). It has exactly one zero \(y_c>1\).

Consequently \(R\) decreases until \(x_c=\log y_c\) and increases afterward. Moreover \(R(1)>0\), \(R(2)<0\), and

\[
R(x)=-\frac14(1+x)e^{-x}(1+o(1))<0
\]

for large \(x\). Therefore there is a unique

\[
\boxed{
\tau_*\in(1,2)
}
\tag{L-91423.6}
\]

such that

\[
R(x)>0\quad(0\le x<\tau_*),
\qquad
R(x)<0\quad(x>\tau_*).
\tag{L-91423.7}
\]

Numerically,

\[
\tau_*=1.164606978873629\ldots.
\tag{L-91423.8}
\]

The numerical value is diagnostic; uniqueness and the sign law are analytic.

## 3. One zero of Nakamura's continuous base density

The scale-independent completed base measure of `L-91410` has continuous density

\[
e^{-u/2}B(u),
\qquad
B(u)=\frac1{1-e^{-2u}}-(1+e^u)
=\frac{1+e^u-e^{3u}}{e^{2u}-1}.
\tag{L-91423.9}
\]

Let \(\varpi>1\) be the plastic constant,

\[
\varpi^3-\varpi-1=0,
\]

and put

\[
\kappa=\log\varpi.
\tag{L-91423.10}
\]

Since \(1+y-y^3\) is strictly decreasing for \(y\ge1\),

\[
\boxed{
B(u)>0\ (0<u<\kappa),
\qquad
B(u)<0\ (u>\kappa).
}
\tag{L-91423.11}
\]

Numerically,

\[
\kappa=0.2811995743229618\ldots.
\]

## 4. Root-locked scale

Define

\[
\boxed{
a_*=\frac{\tau_*}{\kappa}.}
\tag{L-91423.12}
\]

Then \(a_*>1\), so all evaluations \(1/2+r a_*\), \(r\in\{1,2,4\}\), lie safely in \(\Re s>1\). Numerically,

\[
a_*=4.141567360753047\ldots.
\tag{L-91423.13}
\]

By construction, \(R(a_*u)\) and \(B(u)\) change sign at the same point. Hence

\[
\boxed{
R(a_*u)B(u)\ge0
\qquad(u>0),
}
\tag{L-91423.14}
\]

with equality only at \(u=\kappa\).

Substituting the source coefficient (L-91423.3),

\[
\boxed{
c_{a_*}(u)\,e^{-u/2}B(u)\le0
\qquad(u>0).
}
\tag{L-91423.15}
\]

Thus the entire continuous archimedean part of the three-scale recurrence has one fixed sign at \(a_*\). Its internal short/long Jordan split disappears.

## 5. Prime atoms have the opposite sign

Every prime-power atom satisfies

\[
u=\log n\ge\log2>\kappa,
\]

because the plastic constant is below \(2\). Therefore

\[
R(a_*\log n)<0
\]

and

\[
\boxed{
c_{a_*}(\log n)>0
\qquad(n=p^k\ge2).
}
\tag{L-91423.16}
\]

At the root-locked scale the complete source ledger is therefore exactly

```text
positive prime atomic channel;
negative continuous archimedean channel;
deterministic connection / bridge.
```

The six signed scale/Jordan sectors of `L-91404` have collapsed to two measure channels plus one scalar connection.

## 6. Correct operator target at the anchor

Let \(\mathscr Q_{a_*,\mathrm p}\) and \(\mathscr Q_{a_*,\infty}\) be the delayed, two-sided, bridge-complete Hardy feature maps obtained by factoring respectively:

\[
c_{a_*}(u)\,d\Pi(u)
\]

and

\[
-c_{a_*}(u)e^{-u/2}B(u)\,du,
\]

both now positive measures. Let \(\mathscr C_{a_*}\) denote the deterministic connection block.

The root-locked completion theorem is the explicit two-channel domination

\[
\boxed{
\mathscr Q_{a_*,\mathrm p}^*
\mathscr Q_{a_*,\mathrm p}
+
\mathscr C_{a_*}
\succeq
\mathscr Q_{a_*,\infty}^*
\mathscr Q_{a_*,\infty},
}
\tag{L-91423.17}
\]

in the exact normalization of `L-91407/L-91410`, with compressed delays, both Hardy orientations, and the bridge retained.

This is strictly smaller than the previous six-sector domination problem. It remains unproved.

## 7. Role in a cofinal recurrence

The root-locked scale is a canonical safe anchor. A complete RH proof still needs either:

1. a positive source cocycle transporting (L-91423.17) from \(a_*\) to the dyadic sequence \(a_*2^{-j}\); or
2. a direct proof of the two/three-channel domination at every scale in that sequence.

`T-91005` then turns the coefficient-one recurrence into RH.

```text
unique residual zero                           EXACT
unique Nakamura sign boundary                  EXACT
root-locked sign alignment                     EXACT
prime/continuous two-channel collapse          EXACT
two-channel delayed Hardy domination           OPEN
cofinal scale propagation                      OPEN / RH-BEARING
Riemann Hypothesis                             UNPROVED
```
