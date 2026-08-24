# L-105560 — Defect-retaining multiplicity bridge

Claim ID: `L-105560`  
Status: **PROVED EXACT LINEAR ALGEBRA + PINNED FORMAL INPUT**  
Created: 2026-08-24  
RH status: **not assumed**

Let `N=N(T,2T)` be the complete zero count with multiplicity and let
`S=N0simple(T,2T)` be the simple critical-line zero count. The pinned no-hypothesis
theorem

```text
Zeta23.ThmD.thmD₀_simple_mult
```

in `m0at/zeta-23-lean@3635e748`, file `Zeta23/ThmD/Mult.lean`, proves

\[
S\ge H_0N-o(N),
\qquad
H_0=\frac32-\frac1{\sqrt2}\cot\frac1{\sqrt2}.
\tag{1}
\]

The similarly valued theorem in `ThmD/Final.lean` concerns `N0star`; it is not
the source used here.

In the multiplicity-aware decomposition behind Theorem D, write the Hermitian
matrix as

\[
H=P+Q,
\qquad P=VV^*\succeq0,
\tag{2}
\]

where the `S` simple on-line atoms give the columns of `V`. Let

\[
M=V^*V,
\qquad
\Delta(M)=\operatorname{tr}\Psi(M),
\tag{3}
\]

with

\[
\Psi(t)=
\begin{cases}
(t-1)^2,&0\le t\le2,\\
2t-3,&t\ge2.
\end{cases}
\]

Every positive direction of the remainder `Q` consumes at least two units of
zero multiplicity. Consequently

\[
\boxed{n_+(Q)\le\frac{N-S}{2}.}
\tag{4}
\]

Apply the stability-enhanced rank--inertia inequality of `L-105210` with
`r=S` and `b=(N-S)/2`:

\[
\|H\|_{\mathrm{HS}}^2
\ge4\operatorname{tr}H-2N-S+\Delta(M).
\tag{5}
\]

The formal Theorem D trace and Hilbert--Schmidt estimates give the baseline
constant `H0`. Keeping the nonnegative term in (5), rather than dropping it,
yields

\[
\boxed{
S\ge H_0N+\Delta(M)-o(N).
}
\tag{6}
\]

Equation (6) is the exact interface consumed by `L-105561/L-105562`.
