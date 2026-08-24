# L-105412 — Under the sharp residue sign, one scalar endpoint mass collapses the complete high-Xi tail moments

Claim ID: `L-105412`  
Status: **PROVED CONDITIONAL COMPACTNESS THEOREM — SHARP SIGN AND SCALAR PIVOT OPEN**  
Created: 2026-08-24  
Depends on: `L-105387`, `L-105410`, `L-105411`, `T-105371`  
RH status: **unproved**

## 1. Setup

Let `F_r=Xi^(r)` tend to high derivative order through one parity, and use the normalization of `L-105410`. Assume the complete simple critical set is real and has nonpositive residues. This is the high-level form of the sharp critical gate `CRVH105330`.

Let

\[
\widehat\nu_r
=\sum_{c>0}
\left(-{2\rho_c\over c^2}\right)
\delta_{1/(\omega_r^2c^2)}
\tag{L-105412.1}
\]

be the complete normalized positive critical measure, with the central even residue regularized as in `L-105381`. Let `nu_p` be the complete tangent or cotangent measure of `L-105382`.

Assume only the ordinary zeroth source-capacity pivot

\[
\boxed{
\widehat\nu_r([0,\infty))
\le
\widehat a_{0,r}.
}
\tag{L-105412.2}
\]

Call this scalar gate `ZCAP105412`. It is one scalar part of the boundary gate, not the full Stieltjes hierarchy.

## 2. Local convergence away from zero

For every fixed `delta>0`, only finitely many model atoms lie in `[delta,infinity)`. The fixed-cell theorem gives all corresponding actual critical atoms and excludes additional critical points in that compact rescaled region. Hence

\[
\boxed{
\widehat\nu_r|_{[\delta,\infty)}
\Longrightarrow
\nu_p|_{[\delta,\infty)}.
}
\tag{L-105412.3}
\]

The source theorem gives

\[
\widehat a_{0,r}
\longrightarrow
\nu_p([0,\infty)).
\tag{L-105412.4}
\]

By (L-105412.2),

\[
\limsup_r\widehat\nu_r([0,\infty))
\le\nu_p([0,\infty)).
\]

On the other hand, (L-105412.3), followed by `delta downarrow 0`, gives the opposite lower bound. Therefore

\[
\boxed{
\widehat\nu_r([0,\infty))
\longrightarrow
\nu_p([0,\infty)).
}
\tag{L-105412.5}
\]

No positive mass can escape to the reciprocal-square endpoint `s=0`.

## 3. Complete weak and moment convergence

The first critical cell stays a fixed positive rescaled distance from the origin, so the supports are uniformly bounded above. Equations (L-105412.3)--(L-105412.5) imply

\[
\boxed{\widehat\nu_r\Longrightarrow\nu_p.}
\tag{L-105412.6}
\]

Consequently, for every fixed `n>=0`,

\[
\boxed{
\int s^n\,d\widehat\nu_r(s)
\longrightarrow
\int s^n\,d\nu_p(s).
}
\tag{L-105412.7}
\]

Together with the source convergence of `L-105410`,

\[
\boxed{
\widehat{\mathsf A}_{k,r}^{(a)}
-\widehat{\mathsf C}_{k,r}^{(a)}
\longrightarrow0
}
\tag{L-105412.8}
\]

entrywise and in operator norm for every fixed `k` and `a=0,1`.

Thus, once the sharp residue sign is known, the complete fixed-order remote moment family does not need `2k` independent hypotheses: local cell convergence plus the single scalar mass upper bound prevents the only possible endpoint escape.

## 4. Quantitative version

Let

\[
L_r={\sqrt{\mathcal R_r}\over\log\mathcal R_r}.
\]

The second-order cell estimate gives, for the first `L_r` cells,

\[
\sum_{j\le L_r}|W_{r,j}-W_j^p|
=O(L_r/\mathcal R_r).
\tag{L-105412.9}
\]

The model mass beyond `L_r` is `O(L_r^-1)`. Using (L-105412.2),

\[
\boxed{
0\le
\widehat a_{0,r}
-\widehat\nu_r([0,\infty))
\ll
{\log\mathcal R_r\over\sqrt{\mathcal R_r}}.
}
\tag{L-105412.10}
\]

For every fixed `n>=1`, the tail support is `O(L_r^-2)`, so

\[
\boxed{
\left|
\widehat a_{n,r}
-\int s^n\,d\widehat\nu_r(s)
\right|
=O_n(\mathcal R_r^{-1}).
}
\tag{L-105412.11}
\]

Hence the complete ordinary boundary matrix is a nonnegative zeroth pivot plus an `O_k(mathcal R_r^-1)` remainder, and the complete shifted boundary matrix is `O_k(mathcal R_r^-1)`. In particular their negative parts tend to zero.

## 5. Meaning for the previous remote-tail gate

`RTMH105400(k)` required all first `2k` signed remote moments at one common shrinking rate. Under `CRVH105330`, `ZCAP105412` and the Xi real-saddle localization, those moments are generated automatically. The genuinely new unproved item is the scalar endpoint mass inequality, not an independent moment-matching theorem at every order.

This does not establish exact positivity of the complete terminal matrices at each finite `r`; it proves vanishing negative part. Exact inner-window positivity is supplied separately by the positive model tail in `T-105410`.

## 6. Scope

The theorem assumes the complete critical tail is real, simple and nonpositive-residue, and assumes the scalar pivot (L-105412.2). Neither is proved. It does not perform low-order reverse-Rolle descent and does not prove RH.
