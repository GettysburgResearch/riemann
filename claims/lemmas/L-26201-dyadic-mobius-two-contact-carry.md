# L-26201 — The dyadic Möbius source is an exact two-contact carry vector

Claim ID: `L-26201`  
Title: The Euler-aligned dyadic Möbius coefficient collapses pointwise under every finite carry row to the two endpoint-neighbor contacts  
Status: **PROPOSED EXACT LEMMA — COMPLETE FINITE ALGEBRA**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-08  
Dependencies: PR #236 `L-23010`--`L-23012`; PR #244 `L-23701`; elementary Möbius inversion and Kummer's theorem  
Scope: exact source trace from the corrected fixed-`q_0=2` / dyadic shell into carry-incidence and carry-Hermitian coordinates; no asymptotic estimate or RH conclusion

## 1. The Euler-aligned dyadic source

Put

\[
\boxed{
 b_2(q)
 =
 \mu(q)-\mathbf 1_{2\mid q}\mu(q/2).
}
\tag{L-26201.1}
\]

Equivalently,

\[
b_2=(\varepsilon-\delta_2)*\mu
\]

in the Dirichlet-convolution algebra. Hence

\[
\boxed{
\mathbf 1*b_2=\varepsilon-\delta_2.
}
\tag{L-26201.2}
\]

For integer `x>=0`, define

\[
A_2(x)
=
\sum_{q\le x} b_2(q)\left\lfloor {x\over q}\right\rfloor.
\tag{L-26201.3}
\]

Summing the convolution in (L-26201.2) gives

\[
\boxed{
A_2(x)=\mathbf 1_{\{x=1\}}.
}
\tag{L-26201.4}
\]

Thus a coefficient carrying the complete inverse-zeta difficulty has an
exceptionally short divisor-prefix image.

## 2. Carry indicators

For integers

\[
n\ge2,\qquad 0\le j\le n,\qquad 1\le q\le n,
\]

put

\[
\boxed{
\chi_{n,q}(j)
=
\mathbf 1_{\{j\bmod q>n\bmod q\}}.
}
\tag{L-26201.5}
\]

This is the carry across the base-`q` digit boundary in the addition

\[
j+(n-j)=n.
\]

The equivalent floor formula is

\[
\boxed{
\chi_{n,q}(j)
=
\left\lfloor{n\over q}\right\rfloor
-
\left\lfloor{j\over q}\right\rfloor
-
\left\lfloor{n-j\over q}\right\rfloor .
}
\tag{L-26201.6}
\]

Its average is the carry matrix of PR #244:

\[
\beta_{nq}
=
{1\over n+1}\sum_{j=0}^n\chi_{n,q}(j)
=
{\lfloor n/q\rfloor\,[q-1-(n\bmod q)]\over n+1}.
\tag{L-26201.7}
\]

The `q=1` carry indicator is identically zero, so it may be inserted or
removed from every sum below.

## 3. Exact pointwise two-contact collapse

Define the dyadic carry profile

\[
Y_n(j)
=
\sum_{q=2}^n b_2(q)\chi_{n,q}(j).
\tag{L-26201.8}
\]

Using (L-26201.6) and (L-26201.3),

\[
Y_n(j)=A_2(n)-A_2(j)-A_2(n-j).
\]

Since `n>=2`, (L-26201.4) gives the exact identity

\[
\boxed{
Y_n(j)
=
-\mathbf 1_{\{j=1\}}
-\mathbf 1_{\{j=n-1\}}.
}
\tag{L-26201.9}
\]

For `n=2`, the two contacts coincide and the value at `j=1` is `-2`.
For every `n>=3`, the complete signed Möbius carry row vanishes at every
interior point except the two endpoint neighbors.

This is stronger than an averaged rank statement and stronger than the
proposed generic two-contact face assertions in earlier branches: it is a
literal source-specific coefficient identity before any estimate.

## 4. Rank-one averaged image

Averaging (L-26201.9) over `j` gives

\[
\boxed{
\sum_{q=2}^n b_2(q)\beta_{nq}
=
-{2\over n+1}.
}
\tag{L-26201.10}
\]

More generally, for `1<=m<=n`,

\[
\boxed{
\sum_{k\le n/m} b_2(k)\beta_{n,mk}
=
\begin{cases}
-\dfrac{2m}{n+1},&2m\le n,\\[2mm]
\dfrac{2m-n-1}{n+1},&2m>n.
\end{cases}}
\tag{L-26201.11}
\]

Indeed the Möbius carry collapse of `L-23704` gives

\[
\sum_{k\le n/m}\mu(k)\beta_{n,mk}
={2m-n-1\over n+1};
\]

subtracting the same expression at `2m`, when `2m<=n`, proves
(L-26201.11).

Thus the dyadic source is a one-kink affine row under the full carry matrix and
a pure harmonic ray at `m=1`.

## 5. Exact carry-Hermitian energy

The pointwise identity immediately gives

\[
\boxed{
{1\over n+1}\sum_{j=0}^n |Y_n(j)|^2
=
\begin{cases}
\dfrac43,&n=2,\\[2mm]
\dfrac2{n+1},&n\ge3.
\end{cases}}
\tag{L-26201.12}
\]

Let `L:N->R` be any completely additive function and define its generalized
von Mangoldt weights by

\[
\Lambda_L(p^a)=L(p),\qquad
\Lambda_L(q)=0
\quad\text{if `q` is not a prime power.}
\]

Kummer's theorem gives

\[
\sum_{q=p^a\le n}\Lambda_L(q)\chi_{n,q}(j)
=
L\binom nj.
\tag{L-26201.13}
\]

Pairing this profile with (L-26201.9) yields

\[
\boxed{
{1\over n+1}
\sum_{j=0}^n
Y_n(j)L\binom nj
=
-{2L(n)\over n+1}.
}
\tag{L-26201.14}
\]

For `L=log`, the reflected cross term is exactly `-2 log(n)/(n+1)`.

For `n>=3`, the orthogonal projection of

\[
j\longmapsto \log\binom nj
\]

onto the dyadic two-contact vector `Y_n` is

\[
-\log n\,Y_n.
\]

Consequently the exact Schur decomposition is

\[
\boxed{
{1\over n+1}\sum_{j=0}^n
\log^2\binom nj
=
{2\log^2n\over n+1}
+
{1\over n+1}
\sum_{j=2}^{n-2}\log^2\binom nj .
}
\tag{L-26201.15}
\]

The second term is a strict positive reserve for every `n>=4`. This is a
genuine source-specific Hermitian reserve in carry feature space. It is not yet
an intertwiner to the physical two-frequency normal Gram of `L-9518`.

## 6. Reflected divisor-gradient form

The carry profile also has the exact discrete derivative

\[
\boxed{
\chi_{n,q}(j)-\chi_{n,q}(j-1)
=
\mathbf 1_{q\mid n-j+1}
-
\mathbf 1_{q\mid j}.
}
\tag{L-26201.16}
\]

Thus carry incidence is an integrated reflected divisor gradient.

For the dyadic source, put

\[
D_2(r)=
\sum_{\substack{q\mid r\\q\ge2}}b_2(q).
\]

Equation (L-26201.2) gives

\[
D_2(1)=0,\qquad
D_2(2)=-2,\qquad
D_2(r)=-1\quad(r\ge3).
\tag{L-26201.17}
\]

Substitution in (L-26201.16) shows directly that every interior reflected
divisor gradient cancels and only the two boundary jumps survive. This is the
exact algebraic interface to signed carry transport.

## 7. What the two-contact theorem does and does not prove

Closed exactly:

- the dyadic divisor-prefix collapse;
- the pointwise two-contact carry identity;
- the rank-one averaged carry image;
- the complete carry-Hermitian norm and reflected cross term;
- a strict carry-space Schur reserve;
- the reflected divisor-gradient representation.

Not supplied:

- a bounded map from the carry Hermitian form to the physical `L-9518` normal
  Gram;
- a critical estimate for the dyadic shell;
- a lower-scale contraction;
- RH.

The exact identities identify a much smaller honest target: only the
two-contact/two-charge dyadic source needs to be transported through a coupled
normal-Gram theorem. Generic packet-face counting is unnecessary and
insufficient.
