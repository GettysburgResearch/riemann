# L-105322 — The Wick prime-side model has record-sized rank reserve

Claim ID: `L-105322`  
Status: **PROVED FOR THE FROZEN STATIONARY MODEL**  
Created: 2026-08-23  
Depends on: `L-105321`; Montgomery--Vaughan mean value  
RH status: **not assumed**

## 1. Two-sided model symbol

Let `a_L(n)` be as in `L-105321` and put

\[
f_L(t)=1+2\Re\sum_{n\le e^L}{a_L(n)\over n^{it}}.
\tag{L-105322.1}
\]

For a long interval `I=[T,2T]` with `e^L=T^theta`, fixed `theta<1`, the
Montgomery--Vaughan mean-value theorem gives

\[
{1\over T}\int_I f_L(t)\,dt=1+o(1),
\tag{L-105322.2}
\]

and

\[
{1\over T}\int_I|f_L(t)|^2dt
=1+2\sum_{n\le e^L}{a_L(n)^2\over n}+o(1).
\tag{L-105322.3}
\]

The factor two is the Hermitian forward/backward symmetrization. By
`L-105321`, the limiting mean square is strictly below

\[
1+{7\over160}={167\over160}.
\tag{L-105322.4}
\]

## 2. Compression inequality

Let `V_J` be any `J`-dimensional subspace of `L^2(I,dt/T)` with constant
reproducing diagonal, for example the first `J` Fourier modes, and let

\[
K_{L,J}=P_{V_J}M_{f_L}P_{V_J}.
\]

Then

\[
\operatorname{tr}K_{L,J}=J\,{1\over T}\int_If_L,
\]

while compression and Parseval give

\[
\|K_{L,J}\|_{HS}^2
\le J\,{1\over T}\int_I|f_L|^2.
\]

Therefore the normalized effective rank satisfies

\[
\boxed{
\liminf
{(\operatorname{tr}K_{L,J})_+^2
\over J\|K_{L,J}\|_{HS}^2}
\ge {160\over167}.}
\tag{L-105322.5}
\]

The statement is independent of the growth of `J`, provided the constant
reproducing-diagonal model and the mean-value asymptotics remain valid.

## 3. One-percent perturbation

If an arithmetic matrix `H_T` of the same dimension satisfies

\[
\operatorname{tr}H_T\ge {99\over100}\operatorname{tr}K_{L,J},
\qquad
\|H_T\|_{HS}\le {101\over100}\|K_{L,J}\|_{HS},
\]

then

\[
\boxed{
{(\operatorname{tr}H_T)_+^2
\over J\|H_T\|_{HS}^2}
\ge
{160\over167}\left({99\over101}\right)^2
={1568160\over1703567}
=0.920515\ldots .}
\tag{L-105322.6}

Combining this with the multiplicity nuisance density `821/10000` from
`L-105311` gives the conditional line proportion

\[
\boxed{
2{1568160\over1703567}-1-{821\over5000}
={5765136493\over8517835000}
=0.676831\ldots .}
\tag{L-105322.7}

This exceeds the conservative upper decimal `0.672501` for the published
Montgomery--Taylor constant.

## 4. Scope

`K_(L,J)` is the frozen stationary prime-side model. The theorem does not say
that the actual Xi contour compression is a one-percent perturbation. That
entry-dependent, boundary and canonical-product comparison is exactly
`WXFER105320`.
