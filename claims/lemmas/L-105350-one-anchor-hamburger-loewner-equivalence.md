# L-105350 — One analytic anchor determines the complete Loewner kernel

Claim ID: `L-105350`  
Status: **PROVED EXACT ANALYTIC EQUIVALENCE — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-23  
Depends on: `L-105329`; the classical Hamburger moment theorem  
RH status: **not assumed**

## 1. Setup

Let `I` be a real interval, and let `U` be a conjugation-symmetric complex
neighbourhood of `I` such that

\[
U_+=U\cap\{\operatorname{Im}z>0\}
\]

is connected. Let `H` be holomorphic on `U` and real on `I`. Fix one point
`x_*\in I`, and define

\[
\boxed{
m_n(x_*)={H^{(n+1)}(x_*)\over(n+1)!},
\qquad n\ge0.
}
\tag{L-105350.1}
\]

For `k\ge1`, define the confluent Hankel matrix

\[
\boxed{
\mathsf L_k(x_*)=
\bigl[m_{r+s}(x_*)\bigr]_{r,s=0}^{k-1}.
}
\tag{L-105350.2}
\]

The real divided-difference kernel is

\[
\mathscr L_H(x,y)={H(x)-H(y)\over x-y},
\qquad
\mathscr L_H(x,x)=H'(x).
\tag{L-105350.3}
\]

## 2. Equivalence theorem

The following are equivalent.

1. `\mathscr L_H` is positive semidefinite on every finite real packet in `I`.
2. At the one fixed anchor `x_*`,

   \[
   \boxed{
   \mathsf L_k(x_*)\succeq0
   \quad\text{for every }k\ge1.
   }
   \tag{L-105350.4}
   \]

3. There is a finite positive compactly supported Borel measure `\mu` on
   `\mathbb R` such that, in a neighbourhood of `x_*`,

   \[
   \boxed{
   H(z)=H(x_*)+(z-x_*)
   \int_{\mathbb R}{d\mu(t)\over1-t(z-x_*)}.
   }
   \tag{L-105350.5}
   \]

   The right side is a Pick function on the upper half-plane and agrees with
   `H` throughout `U_+`.

Thus complete all-packet Loewner positivity is an all-order condition at one
source-owned analytic anchor. No search over separated packets is intrinsic.

## 3. All-packet positivity implies the anchor hierarchy

The kernel has the convergent expansion

\[
\mathscr L_H(x_*+u,x_*+v)
=
\sum_{r,s\ge0}m_{r+s}(x_*)u^rv^s.
\tag{L-105350.6}
\]

If the kernel is positive on every real packet, every finite-difference Gram
matrix is positive. Taking confluent limits gives (L-105350.4). Equivalently,
for every real polynomial `q(t)=\sum_{r=0}^{k-1}q_rt^r`, one has

\[
\sum_{r,s=0}^{k-1}q_rq_s m_{r+s}(x_*)\ge0.
\tag{L-105350.7}
\]

## 4. Hamburger measure and compact support

Assume (L-105350.4). The linear functional

\[
\Lambda(t^n)=m_n(x_*)
\]

is nonnegative on every polynomial square. The Hamburger moment theorem gives
a positive Borel measure `\mu` on `\mathbb R` with

\[
m_n(x_*)=\int_{\mathbb R}t^n\,d\mu(t).
\tag{L-105350.8}
\]

The measure is finite because

\[
\mu(\mathbb R)=m_0(x_*)=H'(x_*)<\infty.
\]

It is automatically compactly supported. Choose `r>0` such that `H` is
holomorphic on the closed disk `|z-x_*|\le r`. Cauchy's estimate gives

\[
0\le m_{2n}(x_*)\le C_r r^{-2n}
\tag{L-105350.9}
\]

for one constant `C_r`. If `\mu` charged a set on which
`|t|>r^{-1}+\varepsilon`, its even moments would eventually exceed the right
side. Hence the support is contained in a compact interval. Compact support
also makes the moment measure unique.

## 5. Reconstruction and Pick extension

For `|z-x_*|` sufficiently small, geometric expansion gives

\[
\begin{aligned}
H(x_*)+(z-x_*)
\int {d\mu(t)\over1-t(z-x_*)}
&=H(x_*)+
\sum_{n\ge0}m_n(x_*)(z-x_*)^{n+1}\\
&=H(z).
\end{aligned}
\tag{L-105350.10}
\]

For `\operatorname{Im}z>0` and real `t`,

\[
\operatorname{Im}{z-x_*\over1-t(z-x_*)}
={\operatorname{Im}z\over|1-t(z-x_*)|^2}>0.
\tag{L-105350.11}
\]

Therefore the right side of (L-105350.5) defines a Pick function
`\widetilde H`. Its Hermitian kernel is

\[
\boxed{
{\widetilde H(z)-\overline{\widetilde H(w)}
 \over z-\overline w}
=
\int_{\mathbb R}
{d\mu(t)
 \over
 (1-t(z-x_*))(1-t(\overline w-x_*))}.
}
\tag{L-105350.12}
\]

It is positive semidefinite on every finite upper-half-plane packet. The local
identity (L-105350.10) holds on an upper half-disk. Since `U_+` is connected,
the identity theorem gives `\widetilde H=H` on `U_+`. Boundary limits then give
complete real-packet Loewner positivity on `I`. Any apparent real pole of the
integral representation inside `I` is removable because it agrees there with
the holomorphic function `H`.

## 6. One-anchor contour-square cone

Condition (L-105350.4) is equivalently

\[
\boxed{
\sum_{r,s\ge0}^{\mathrm{finite}}
q_rq_s
{H^{(r+s+1)}(x_*)\over(r+s+1)!}
\ge0
}
\tag{L-105350.13}
\]

for every finite real sequence `(q_r)`. Thus the all-packet gate is one
positive moment functional in powers of a single local coordinate.

## 7. Scope

Analyticity and the complete infinite hierarchy are load bearing. No bounded
initial segment of confluent matrices implies the theorem; `R-105350` gives an
exact rational separator. This lemma is an equivalence, not a favourable Xi
estimate. It proves neither `BRP105220` nor RH.
