# L-108311 — Endpoint 31 has a strict source-aligned minority-phase moat

Claim ID: `L-108311`  
Status: **PROVED EXACT DESCENT ARITHMETIC AND CONDITIONAL TRANSFER INTERFACE**  
Created: 2026-08-31  
Depends on: `L-108310`; PR #772 `L-107400`, `L-107401` at head `93726d7f4a4c17ee530d064c19aa3a4519fd5465`  
RH status: **not assumed**

Let `K` be odd. On a regular window let

\[
c_1<\cdots<c_M
\]

be consecutive simple real zeros of `f^(K)` and put

\[
\rho_j={f(c_j)\over f^{(K+1)}(c_j)}.
\]

Let `U_+` and `U_-` count the two signs and let `V_K` count adjacent sign
transitions.

## 1. Direct endpoint descent

The signs of `f^(K+1)(c_j)` alternate. Therefore

\[
\rho_j\rho_{j+1}>0
\quad\Longrightarrow\quad
f(c_j)f(c_{j+1})<0.
\]

Every same-sign residue edge contains a real zero of `f`. Moreover every
transition edge touches a minority-sign vertex, and every vertex has degree
at most two. Hence

\[
\boxed{
V_K\le2\min(U_+,U_-)
}
\tag{L-108311.1}
\]

and, with the complete endpoint/common-zero/multiplicity ledger retained,

\[
\boxed{
N_{\mathbb R}(f;I)
\ge
M-1-2\min(U_+,U_-)-\mathcal E_{\rm reg}.
}
\tag{L-108311.2}
\]

By `L-108310`, the two `U_sigma` are the limiting negative phase variations
of the two direct entire companions.

If

\[
{M\over N}\ge\alpha_K-o(1),
\]

then more than `90%` follows from

\[
\boxed{
{\min(U_+,U_-)+\tfrac12\mathcal E_{\rm reg}\over N}
<
{\alpha_K-9/10\over2}.
}
\tag{L-108311.3}
\]

## 2. Exact endpoint-31 allowance

PR #772 proves unconditionally

\[
\alpha_{31}>{999\over1000}.
\]

Therefore the exact minority allowance is

\[
\boxed{
{\alpha_{31}-9/10\over2}
>{99\over2000}.
}
\tag{L-108311.4}
\]

The same PR proves the carrier-adapted source constant

\[
{1\over2K}={1\over62}
\]

at `K=31`. Consequently

\[
\boxed{
{99\over2000}-{1\over62}
={2069\over62000}
>0.
}
\tag{L-108311.5}
\]

Thus the following physical transfer statement is sufficient:

\[
\boxed{
\limsup_{T\to\infty}
{\min_\sigma U_{31,\sigma}(T)
 +\tfrac12\mathcal E_{\rm reg}(T)
 \over N(T,2T)}
\le
{1\over62}+\delta,
\qquad
\delta<{2069\over62000}.
}
\tag{L-108311.6}
\]

This is named `XI31MINPHASE108310`.

The statement is deliberately physical. `L-107401` proves a Fourier-source
ratio `1/62`; it does not prove (L-108311.6).

## 3. Why the endpoint order matters

If the only proposed main term is `1/(2K)`, even the idealized bound
`alpha_K<=1` can beat `90%` only when

\[
{1\over2K}<{1-9/10\over2},
\]

that is, only when

\[
K>10.
\]

Among odd orders the first possible endpoint is `K=11`. Endpoint `31` has a
proved high-derivative proportion and a generous exact moat.

More generally, if a sequence of odd endpoints satisfies

\[
\alpha_K\to1
\]

and the physical minority phase obeys

\[
{\min_\sigma U_{K,\sigma}\over N}
\le{1\over2K}+o_K(1),
\]

then the direct descent gives

\[
\liminf{N_0\over N}
\ge
\alpha_K-{1\over K}-o_K(1),
\]

which tends to one as `K` tends to infinity. This is a conditional density-one
hierarchy, not RH.

## Scope

All descent constants and the endpoint-31 moat are exact. The Xi physical
minority-phase transfer remains open.
