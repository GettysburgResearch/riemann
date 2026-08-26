# L-105654 — One matched vertical factor has quadratic phase debt and linear current reserve

Claim ID: `L-105654`  
Status: **PROVED EXACT ONE-FACTOR MODEL-SPACE THEOREM**  
Created: 2026-08-27  
Depends on: `L-105640--L-105649`; corrected `L-106512/L-106514`  
RH status: **not assumed**

## 1. Matched vertical pair

Let

\[
\lambda=\delta+i\alpha,
\qquad
\delta>0,
\qquad
H>0.
\]

In the Paley--Wiener coordinate, the shallow normalized model vector is

\[
e_0(\xi)=\sqrt{2\delta}\,e^{-(\delta+i\alpha)\xi},
\]

and the same factor shifted deeper by `2H` is

\[
e_2(\xi)=\sqrt{2(\delta+2H)}
 e^{-(\delta+2H+i\alpha)\xi}.
\]

Their squared canonical correlation is

\[
\boxed{
\mathcal O_H(\lambda)
=
|\langle e_0,e_2\rangle|^2
=
\frac{4\delta(\delta+2H)}{(2\delta+2H)^2}
=
1-\frac{H^2}{(\delta+H)^2}.
}
\tag{L-105654.1}

Hence the degree-zero reverse-oriented phase defect is

\[
\boxed{
\mathfrak P_{0,H}(\lambda)
=
1-\mathcal O_H(\lambda)
=
\frac{H^2}{(\delta+H)^2}.
}
\tag{L-105654.2}

## 2. Current/source reserve

The exponential source compression at scale `H` is

\[
\boxed{
\mathcal T_H(\lambda)
=
\langle e_0,M_{e^{-H\xi}}e_0\rangle
=
\frac{2\delta}{2\delta+H}.
}
\tag{L-105654.3}

Its unused reserve is

\[
\boxed{
\mathfrak R_H(\lambda)
=
1-\mathcal T_H(\lambda)
=
\frac{H}{2\delta+H}.
}
\tag{L-105654.4}

The exact difference is

\[
\boxed{
\mathfrak R_H(\lambda)-\mathfrak P_{0,H}(\lambda)
=
\frac{H\delta^2}
{(2\delta+H)(\delta+H)^2}
\ge0.
}
\tag{L-105654.5}

Therefore

\[
\boxed{
\mathfrak P_{0,H}(\lambda)
\le
\mathfrak R_H(\lambda).
}
\tag{L-105654.6}

Equivalently,

\[
\boxed{
\mathcal O_H(\lambda)
\ge
\mathcal T_H(\lambda).
}
\tag{L-105654.7}

## 3. Xi height form

If the unshifted zero has height

\[
\gamma=\delta+H,
\]

then

\[
\mathfrak P_{0,H}=\frac{H^2}{\gamma^2},
\qquad
\mathfrak R_H=\frac{H}{2\gamma-H},
\]

and

\[
\boxed{
\frac{H}{2\gamma-H}-\frac{H^2}{\gamma^2}
=
\frac{H(\gamma-H)^2}
{\gamma^2(2\gamma-H)}
\ge0.
}
\tag{L-105654.8}

The reference current-height owner survival from `L-105646` is

\[
S_\gamma(H)=\frac{2(\gamma-H)}{2\gamma-H}.
\]

Thus its accumulated owner mass below height `H` is exactly

\[
1-S_\gamma(H)=\frac{H}{2\gamma-H},
\]

which pays the complete one-factor phase defect.

## 4. First-contact scaling

As `H downarrow 0` with `gamma` fixed,

\[
\mathfrak P_{0,H}=O(H^2),
\qquad
\mathfrak R_H=\frac{H}{2\gamma}+O(H^2).
\]

A newly created degree-zero phase defect is therefore quadratic at contact,
while the source-owned current reserve is linear.

## 5. Scope

For several factors, the canonical overlap is not the sum of the one-factor
overlaps because the model vectors are nonorthogonal.  The exact packet
problem is the Cauchy-translation trace inequality `CTI105655`.  This lemma
proves the complete rank-one case and identifies the correct normalization; it
does not prove the multipacket inequality, the cofinal Xi passage, or RH.
