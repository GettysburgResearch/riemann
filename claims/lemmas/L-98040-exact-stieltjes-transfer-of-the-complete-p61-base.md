# L-98040 — Exact Stieltjes transfer of the complete normalized `P_61` base

Claim ID: `L-98040`<br>
Status: **PROVED EXACT SOURCE THEOREM**<br>
Created: 2026-08-18<br>
Depends on: the repaired annular base in PR #587/#599; PR #603 notation<br>
RH status: **not assumed**

Let `b(x)` be the complete `P_61` annular `5:3` scalar, zero extended below
its first activation, and put

\[
h(x)={b(x)\over\sqrt x}.
\tag{L-98040.1}
\]

For `z>=2`, define the literal reciprocal rough-Möbius prefix

\[
A_z(t)=
\sum_{\substack{m\le t\\m\ {\rm squarefree}\\P^-(m)\ge z}}
{\mu(m)\over m}.
\tag{L-98040.2}
\]

For the native rough state

\[
\mathcal F(Y,z)=
\sum_{\substack{m\le Y\\m\ {\rm squarefree}\\P^-(m)\ge z}}
{\mu(m)\over\sqrt m}\,b(Y/m),
\tag{L-98040.3}
\]

one has the exact source-faithful identity

\[
\boxed{
{\mathcal F(Y,z)\over\sqrt Y}
=
\int_{[1,Y]} A_z(Y/x)\,dh(x).
}
\tag{L-98040.4}
\]

No source occurrence is replaced by an unrestricted reservoir and no
absolute value is taken in (L-98040.4).

## Proof of the transfer

The left side of (L-98040.4) is

\[
\sum_m {\mu(m)\over m}h(Y/m)
=
\int_{[1,Y]} h(Y/t)\,dA_z(t).
\]

The base satisfies `h(1)=0`. Stieltjes integration by parts, followed by the
order-reversing substitution `x=Y/t`, gives

\[
\int_{[1,Y]} h(Y/t)\,dA_z(t)
=-\int_{[1,Y]}A_z(t)\,d(h(Y/t))
=\int_{[1,Y]}A_z(Y/x)\,dh(x).
\]

This proves (L-98040.4). For a step base, the formula simply says that a jump
at `x=q` is multiplied by the exact rough prefix at `Y/q`; hence activation
and coefficient ownership remain literal.

## Exponentially weighted variation of the base

Let

\[
a_*=12\prod_{p\le61}\left(1-{1\over p}\right)>0.
\tag{L-98040.5}
\]

The exact fixed-`P_61` Euler-ramp expansion gives, once all fixed colours are
active,

\[
b(x)=a_*\sqrt x+c_*+O_{P_{61}}(x^{-3/2}).
\tag{L-98040.6}
\]

On every open activation cell, differentiation with respect to `log x` gives

\[
{d\over d\log x}b(x)
=6\sum_{d\mid P_{61}}{\mu(d)\over\sqrt d}
  \sum_{x/(4d)<n<x/d}{1\over\sqrt n}.
\tag{L-98040.7}
\]

The elementary fixed-modulus estimate

\[
\sum_{A<n<B}n^{-1/2}=2(\sqrt B-\sqrt A)+O(A^{-1/2})
\]

therefore yields

\[
{d\over d\log x}h(x)
=-{c_*\over2\sqrt x}+O_{P_{61}}(x^{-1}).
\tag{L-98040.8}
\]

The function `h` is continuous at every activation knot. Its variation on a
fixed compact interval is finite, and (L-98040.8) proves

\[
\boxed{
V_\eta:=\int_{[1,\infty)}x^\eta|dh(x)|<\infty
\qquad(0\le\eta<1/2).
}
\tag{L-98040.9}
\]

In particular `h(x)->a_*`, the total signed mass of `dh` is `a_*`, and the
complete nonhomogeneous base can be transported as one fixed signed measure.
This is strictly sharper than treating `b(x)-a_*sqrt(x)` by an unsigned
upper-bound sieve.
