# L-106603 — Uniformly small analytic scales retain the fifth-companion height budget

Claim ID: `L-106603`  
Status: **PROVED FROM REGULAR-WINDOW ROUCHÉ CONTINUITY AND L-106591 INPUTS**  
Created: 2026-08-26  
Depends on: `L-106591`, `L-106600`  
RH status: **not assumed**

Let \(F=\Xi\) and \(Q=\Xi^{(5)}\) on one regular dyadic rectangle. Let
\(a_\nu\) be holomorphic near its closure, real and strictly positive on the
real boundary, and satisfy

\[
\|a_\nu\|_{L^\infty(\Omega)}\longrightarrow0.
\]

Define

\[
D_{a_\nu}=(F+ia_\nu F')(Q-ia_\nu Q').
\]

## 1. Variable-scale Rouché continuity

On the compact rectangle,

\[
F+ia_\nu F'\longrightarrow F,
\qquad
Q-ia_\nu Q'\longrightarrow Q
\]

uniformly. Choose disjoint zero-cluster disks exactly as in `L-106591`.
Rouché's theorem then preserves the complete multiplicity in every disk and
excludes additional zeros in the remaining compact set. Consequently, for
every \(\epsilon>0\),

\[
\boxed{
\limsup_{\nu\to\infty}
\mathfrak h_+(D_{a_\nu}^{\rm red})
\le
\mathfrak h_+(F)+\mathfrak h_+(Q)+\epsilon .
}
\tag{L-106603.1}
\]

No root-separation constant is required.

## 2. Cofinal Xi consequence

Choose one such scale \(a_T\) on each regular dyadic Xi window, small enough
for the declared cluster error to be \(o(N(T,2T))\). The Selberg height bound
for \(F\), the centered half-strip bound for \(Q\), and the pinned
\(R_5/N>997/1000-o(1)\) theorem used in `L-106591` give

\[
\boxed{
\sum_{B_{-,a_T}(x+iy)=0}y
\le
\left(\frac3{4000}+o(1)\right)N(T,2T).
}
\tag{L-106603.2}
\]

The positive-scale homotopy of `L-106600` simultaneously preserves the
endpoint index.

## 3. Deep directions

For every fixed \(\eta>0\), the model-space height split gives

\[
\boxed{
\mathcal C_{>\eta}(U_{5,a_T})
\le
\left(\frac3{4000\eta}+o(1)\right)N(T,2T).
}
\tag{L-106603.3}
\]

At \(\eta=1/100\), all deep directions cost at most \(3N/40+o(N)\), leaving
the same shallow allowance \(11N/500\) as `T-106590`.

The theorem does not estimate the shallow canonical-correlation defect.
