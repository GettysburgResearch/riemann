# L-105350 — One analytic anchor determines the complete Loewner kernel

Claim ID: `L-105350`  
Status: **PROVED EXACT ANALYTIC EQUIVALENCE — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-23  
Depends on: `L-105329`; the classical Hamburger moment theorem  
RH status: **not assumed**

## 1. Setup

Let `I` be a real interval and let `U` be a conjugation-symmetric complex
neighbourhood of `I` whose upper part

\[
U_+=U\cap\{\operatorname{Im}z>0\}
\]

is connected. Let `H` be holomorphic on `U` and real on `I`. Fix one point

\[
x_*\in I.
\]

Put

\[
\boxed{
m_n(x_*)={H^{(n+1)}(x_*)\over(n+1)!},
\qquad n\ge0,
}
\tag{L-105350.1}
\]

and for `k>=1` define the confluent Hankel matrix

\[
\boxed{
\mathsf L_k(x_*)=
[m_{r+s}(x_*)t_{r,s=0}^{k-1}.
}
\tag{L-105350.2}

The divided-difference kernel is

\[
\mathscr L_H(x,y)
={H(x)-H(y)\over x-y},
\qquad
\mathscr L_H(x,x)=H'(x).
\tag{L-105350.3}

## 2. Equivalence theorem

The following are equivalent.

1. `mathscr L_H` is positive semidefinite on every finite real packet in `I`.
2. For this one fixed anchor `x_*`,

   \[
   \boxed{\mathsf L_k(x_*)\succeq0\quad\text{for every }k\ge1.}
   \tag{L-105350.4}
   \]

3. There is a finite positive Borel measure `mu` on `R`, with compact support,
   such that the germ of `H` at `x_*` has the representation

   \[
   \boxed{
   H(z)=H(x_*)+(z-x_*)
   \int_{\mathbb R}{d\mu(t)\over1-t(z-x_*)}.
   }
   \tag{L-105350.5}
   \]

   The right side defines a Pick function on the complete upper half-plane and
   agrees with `H` throughout `U_+`.

Thus complete all-packet Loewner positivity is an all-order condition at one
source-owned analytic anchor; no separated-node search is intrinsically
required.

## 3. All-packet positivity implies the anchor hierarchy

Expand the kernel at `(x_*,x_*)`:

\[
\mathscr L_H(x_*+u,x_*+v)
=\sum_{r,s\ge0}m_{r+s}(x_*)u^rv^s.
\tag{L-105350.6}
\]

If the kernel is positive on all real packets, every finite-difference Gram
matrix is positive. Taking confluent limits gives

\[
\mathsf L_k(x_*)\succeq0
\]

for every `k`. Equivalently, for every real polynomial

\[
q(t)=\sum_{r=0}^{k-1}q_rt^r,
\]

one has

\[
\sum_{r,s}q_rq_sm_{r+s}(x_*)\ge0.
\tag{L-105350.7}
\]

## 4. The Hamburger measure and compact support

Assume (L-105350.4). The linear functional

\[
\Lambda(t^n)=m_n(x_*)
\]

is nonnegative on every polynomial square. By the Hamburger moment theorem,
there is a positive measure `mu` on `R` with

\[
m_n(x_*)=\int t^n\,d\mu(t).
\tag{L-105350.8}
\]

The measure is finite because

\[
\mu(\mathbb R)=m_0(x_*)=H'(x_*)<\infty.
\]

It is automatically compactly supported. Indeed, choose a closed disk of
radius `r>0` about `x_*` on which `H` is holomorphic. Cauchy's estimate gives

\[
0\le m_{2n}(x_*)
\le C_r r^{-2n}
\tag{L-105350.9}
\]

for one constant `C_r`. If `mu` charged a set on which
`|t|>r^{-1}+epsilon`, its even moments would eventually exceed the right side.
Hence

\[
\operatorname{supp}\mu\subset[-r^{-1},r^{-1}]
\]

after reducing `r` if necessary.

Compact support also makes the Hamburger measure unique.

## 5. Reconstruction and Pick extension

For `|z-x_*|` sufficiently small, geometric expansion and (L-105350.8) give

\[
\begin{aligned}
H(x_*)+(z-x_*)
\int{d\mu(t)\over1-t(z-x_*)}
&=H(x_*)+
\sum_{n\ge0}m_n(x_*)(z-x_*)^{n+1}\\
&=H(z).
\end{aligned}
\tag{L-105350.10}

Define the right side for all `Im z>0` by `widetilde H(z)`. For real `t`,

\[
\operatorname{Im}{z-x_*\over1-t(z-x_*)}
={\operatorname{Im}z\over|1-t(z-x_*)|^2}>0.
\tag{L-105350.11}
\]

Therefore `widetilde H` is a Pick function. Its complete Hermitian kernel is

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

This is positive semidefinite on every finite upper-half-plane packet.

The local equality (L-105350.10) holds on an upper half-disk. Since `U_+` is
connected, the identity theorem gives

\[
\widetilde H=H\qquad\text{on }U_+.
\]

Taking nontangential limits to real packets in `I` proves complete Loewner
positivity there.

## 6. A single-anchor contour-square cone

Condition (L-105350.4) can be written without matrices. It is equivalent to

\[
\boxed{
\sum_{r,s\ge0}^{\rm finite}
q_rq_s{H^{(r++s+1)}(x_*)\over(r+s+1)!}\ge0
\qquad\text{for every real finite sequence }(q_r).
}
\tag{L-105350.13}
\]

Thus the all-packet gate is one positive moment functional on the powers of a
single local coordinate. The requirement remains all-order: no fixed finite
truncation is promoted to the complete theorem.

## 7. Scope

Analyticity and the complete infinite hierarchy are load bearing. A bounded
initial segment of confluent matrices does not imply the result; `R-105350`
gives an exact rational separator. This theorem supplies an equivalence, not a
favourable estimate for the Xi boundary function. It proves neither
`BRP105220` nor RH.
