# L-26203 — The dyadic source is the Green potential of two fixed divisor charges

Claim ID: `L-26203`  
Title: In the full-divisor Dirichlet Gram, the dyadic Möbius coefficient has exactly the charge vector `-3 e_2+e_3` and energy five  
Status: **PROPOSED EXACT LEMMA — COMPLETE FINITE ALGEBRA**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-08  
Dependencies: `L-26201`; the endpoint/divisor-gradient calculus of PR #248  
Scope: source-specific signed Green representation; no Green-to-physical-normal transference is claimed

## 1. The unprojected full-divisor Gram

Fix an integer `X>=3`. Unlike the prime-power-only constraint Gram, retain
every integer divisor coordinate

\[
\mathcal D_X=\{2,3,\ldots,X\}.
\]

For `q in D_X`, define

\[
u_q(j)=
\begin{cases}
\mathbf 1_{q\mid j},&1\le j\le X,\\
0,&j=0.
\end{cases}
\tag{L-26203.1}
\]

Put

\[
\Delta u_q(j)=u_q(j+1)-u_q(j),
\qquad0\le j<X,
\]

and define

\[
\boxed{
\overline G_X(q,d)
=
\sum_{j=0}^{X-1}
\Delta u_q(j)\Delta u_d(j).
}
\tag{L-26203.2}
\]

For a coefficient vector `T=(T_q)`, let

\[
D_T(j)
=
\sum_{\substack{q\mid j\\q\ge2}}T_q.
\tag{L-26203.3}
\]

Then

\[
\boxed{
T^T\overline G_XT
=
\sum_{j=0}^{X-1}
\left[D_T(j+1)-D_T(j)\right]^2.
}
\tag{L-26203.4}
\]

If this energy is zero, `D_T` is constant. Since `D_T(1)=0`, it vanishes
identically. Induction over `j=2,3,...,X` then gives `T_j=0`. Therefore

\[
\boxed{\overline G_X>0.}
\tag{L-26203.5}
\]

No endpoint projection is needed because the full divisor incidence already
has the fixed initial value `D_T(1)=0`.

## 2. Exact two-charge image

For the dyadic vector `b_2`, equation `L-26201.17` gives

\[
D_{b_2}(1)=0,\qquad
D_{b_2}(2)=-2,\qquad
D_{b_2}(j)=-1\quad(j\ge3).
\tag{L-26203.6}
\]

Hence its divisor profile has only two nonzero gradients:

\[
\Delta D_{b_2}(1)=-2,
\qquad
\Delta D_{b_2}(2)=1.
\tag{L-26203.7}
\]

For every `q>=2`,

\[
\begin{aligned}
(\overline G_Xb_2)(q)
&=
-2\,\Delta u_q(1)
+\Delta u_q(2)\\
&=
-2\,\mathbf1_{q=2}
+\mathbf1_{q=3}
-\mathbf1_{q=2}.
\end{aligned}
\]

Therefore

\[
\boxed{
\overline G_Xb_2=-3e_2+e_3.
}
\tag{L-26203.8}
\]

The right side is independent of `X`. Pairing once more with `b_2` gives

\[
\boxed{
b_2^T\overline G_Xb_2
=
-3b_2(2)+b_2(3)
=5.
}
\tag{L-26203.9}
\]

Thus the complete RH-bearing dyadic coefficient is a Green potential of two
fixed bottom charges and has constant Dirichlet energy.

## 3. Explicit inverse

Let `a,b in D_X`. Möbius inversion of the divisor-incidence map and the Green
kernel of the one-sided path give

\[
\boxed{
\overline G_X^{-1}(a,b)
=
\sum_{d\mid a}\sum_{e\mid b}
\mu(a/d)\mu(b/e)\min(d,e).
}
\tag{L-26203.10}
\]

The expression is independent of the ambient endpoint once
`X>=max(a,b)`.

### Proof

The map `T -> D_T` is triangular and its inverse is

\[
T(q)=\sum_{d\mid q}\mu(q/d)D_T(d),
\tag{L-26203.11}
\]

with `D_T(1)=0`. The inverse of the discrete gradient energy on a path
anchored at `1` has kernel

\[
\min(d,e)-1.
\]

Double Möbius transformation removes the constant `1`, because

\[
\sum_{d\mid a}\mu(a/d)=0
\qquad(a>1),
\]

and yields (L-26203.10).

Equivalently,

\[
\overline G_X^{-1}(a,b)
=
\sum_{k\ge1} A_a(k)A_b(k),
\tag{L-26203.12}
\]

where

\[
A_a(k)
=
\sum_{\substack{d\mid a\\d\ge k}}\mu(a/d).
\]

This displays the inverse itself as a finite positive-semidefinite Gram.

The first two rows simplify to

\[
\boxed{
\overline G_X^{-1}(2,q)=-\mu(q),
}
\tag{L-26203.13}
\]

and

\[
\boxed{
\overline G_X^{-1}(3,q)
=
-2\mu(q)
-\mathbf1_{2\mid q}\mu(q/2).
}
\tag{L-26203.14}
\]

Consequently

\[
-3\overline G_X^{-1}(2,q)
+\overline G_X^{-1}(3,q)
=
b_2(q),
\tag{L-26203.15}
\]

which is the inverse form of the two-charge identity.

## 4. Two-coordinate form of dyadic signed slack

Let `s=(s(q))` be any real constraint residual and define its Green potential

\[
T_s=\overline G_X^{-1}s.
\tag{L-26203.16}
\]

Then

\[
\boxed{
\sum_{q=2}^X b_2(q)s(q)
=
-3T_s(2)+T_s(3).
}
\tag{L-26203.17}
\]

In particular, the Dyadic Signed Slack theorem of `L-26202` is exactly a
two-coordinate Green theorem. It does not require a bound for all coordinates
of `T_s`, the full Green energy, or the unsigned residual mass.

Cauchy--Schwarz in the Green metric gives the stronger sufficient condition

\[
\boxed{
\left|
\sum_q b_2(q)s(q)
\right|^2
\le
5\,s^T\overline G_X^{-1}s.
}
\tag{L-26203.18}
\]

A subpower full Green-energy bound therefore proves the signed theorem, but it
is not logically necessary.

## 5. Exact relation to the two-contact carry profile

The divisor-gradient identity

\[
\chi_{n,q}(j)-\chi_{n,q}(j-1)
=
\mathbf1_{q\mid n-j+1}-\mathbf1_{q\mid j}
\]

says that the carry-incidence feature is a reflected primitive of the
full-divisor gradient. The two carry contacts in `L-26201.9` and the two Green
charges in (L-26203.8) are therefore the same source in integrated and
differentiated coordinates.

This is the corrected bridge sought between:

```text
two-frequency / fixed-q0 dyadic normal source
<-> pointwise carry incidence
<-> signed divisor-gradient transport.
```

The bridge is exact at source level. It does not identify the physical
`L-9518` normal Gram with `Gbar_X`.

## 6. Why this is a sharper proof target

Existing Green-energy proposals ask for a bound on

\[
s^T\overline G_X^{-1}s
\]

or on an analogous prime-power Gram. The exact dyadic source needs only

\[
\boxed{
|-3T_s(2)+T_s(3)|=X^{o(1)}.
}
\tag{L-26203.19}
\]

Large Green energy orthogonal to this fixed dipole is harmless for the dyadic
Riesz criterion. This is a substantial weakening of both:

- the unsigned Greedy Slack theorem;
- the full Green Energy theorem.

A production proof should focus directly on the bottom-charge combination in
(L-26203.19).

## 7. Proof boundary

Closed exactly:

- positive definiteness of the full-divisor gradient Gram;
- the two-charge image and energy-five identity;
- the exact inverse kernel;
- the two-coordinate representation of signed slack;
- the source-level carry/divisor-gradient bridge.

Open:

- a subpower bound for the two bottom Green coordinates of the greedy residual;
- a Green-to-physical-normal transference;
- RH.
