# L-91544 — The survival/hazard target-normalized row corridor is uniform in the rough prime

Claim ID: `L-91544`  
Status: **PROVED UNIFORM ROW-DENSITY THEOREM**  
Created: 2026-08-13  
Depends on: `L-91454`; positive component-row support; `L-91329`  
RH status: **unproved**

## 1. Apparent large-prime degeneration

A target-exact branch type has target and row atoms of the form

\[
 T_{c,\alpha}(x,n)
 =c\,n^{-1/2}\big(\alpha\sqrt{x/n}-1\big),
 \tag{L-91544.1}
\]

\[
 R_{c}(x,n;j)
 =c\,n^{-1/2}Q_{x/n}(j),
 \tag{L-91544.2}
\]

where \(c>0\), \(\alpha\ge1\), and \(j\ge2\).

For the hazard type,

\[
 c=r(r+2)\to0,
 \qquad
 \alpha=\frac{2(r+1)}{r+2}\to1
 \qquad(r=p^{-1/2}\to0).
\]

It is therefore necessary to check that target normalization does not create an
unbounded row density.

## 2. Exact cancellation of the branch prefactor

Put

\[
 Y=x/n.
\]

Whenever the target atom is positive,

\[
 \boxed{
 \frac{R_c(x,n;j)}{T_{c,\alpha}(x,n)}
 =
 \frac{Q_Y(j)}{\alpha\sqrt Y-1}.
 }
 \tag{L-91544.3}
\]

The branch prefactor \(c\) and the source factor \(n^{-1/2}\) cancel exactly.

## 3. Causal support removes the singular endpoint

The positive component row has causal support

\[
 Q_Y(j)=0
 \qquad(Y<j).
 \tag{L-91544.4}
\]

Since \(j\ge2\), every nonzero row atom satisfies

\[
 Y\ge j\ge2.
 \tag{L-91544.5}
\]

Therefore, for every \(\alpha\ge1\),

\[
 \boxed{
 \alpha\sqrt Y-1
 \ge\sqrt2-1>0
 }
 \tag{L-91544.6}
\]

on the entire nonzero row support.  The apparent singularity at
\((\alpha,Y)=(1,1)\) occurs only where every finite row is zero.

## 4. Uniform compact-corridor bound

Let \(Y_{\max}\) be the fixed terminal reset bound (`67`, `83`, or the slightly
smaller native factor-54 bound, according to the chosen front end), and define

\[
 M_Q
 =\max_{\substack{2\le j\le Y\le Y_{\max}\\j\in\mathbb Z}}
 Q_Y(j).
 \tag{L-91544.7}
\]

The component rows are continuous and piecewise affine in \(\log Y\) on this
finite corridor, so \(M_Q<\infty\).  Equations (L-91544.3)--(L-91544.6) give

\[
 \boxed{
 0\le
 \frac{R_c(x,n;j)}{T_{c,\alpha}(x,n)}
 \le
 \frac{M_Q}{\sqrt2-1}
 =:C_{\rm row},
 }
 \tag{L-91544.8}
\]

uniformly in

```text
the rough prime p;
the branch prefactor c;
the branch parameter alpha>=1;
the source node n;
the finite row j;
the reset endpoint.
```

## 5. Application to the two binary types

The frozen branch parameters satisfy

\[
 \alpha_s\in(4/3,3/2),
 \qquad
 \alpha_h\in(1,1+67^{-1/2}).
\]

Thus both target-exact Hall outputs obey the same bound (L-91544.8).  Together
with the physical corridor of `L-91540`,

\[
 \frac12T\le S\le2T,
\]

target normalization controls target, score and every exact finite row by
prime-independent constants.

Consequently the large-\(p\) hazard limit does not violate the bounded positive
density corridor required by the one-use quantization theorem `L-91329`.

## 6. Boundary

This theorem assumes the target and row atoms have the common branch prefactor
shown in (L-91544.1)--(L-91544.2), which is the exact normalization asserted by
the target-Hall row lift of `L-91454`.  Confirming that normalization against the
live merged one-prime packet remains part of the producer audit.

```text
branch prefactor cancellation                       EXACT
nonzero rows lie at Y>=2                            EXACT
uniform target-normalized row bound                 EXACT
uniformity as p->infinity                           EXACT
bounded-density corridor after positive entry       CLOSED
live one-prime row-prefactor match                   AUDIT REQUIRED
Riemann Hypothesis                                  UNPROVEN
```
