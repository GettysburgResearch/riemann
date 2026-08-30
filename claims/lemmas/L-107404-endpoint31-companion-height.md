# L-107404 — The endpoint-31 companion has height at most \(N/4000\)

Claim ID: `L-107404`  
Programme aliases: `XI90.ENDPOINT31_HEIGHT`, `XI.SHALLOW31_SPLIT`  
Status: **PROVED UNCONDITIONALLY FROM `L-107400`, FIXED-DERIVATIVE STRIP LOCALIZATION, AND REGULAR-WINDOW ROUCHÉ CONTINUITY**  
Created: 2026-08-30  
Depends on: `L-106503`, `L-106591`, `L-107400`  
Programme issue: #744  
RH status: **not assumed**

Put

\[
F=\Xi,\qquad Q=\Xi^{(31)},
\]

and, on one regular dyadic rectangle, define

\[
D_{31,\lambda}
=(F+i\lambda F')(Q-i\lambda Q').
	ag{L-107404.1}
\]

Common factors are removed before the all-pass quotient is formed.

## 1. Window-adapted small shift

The Rouché argument of `L-106591` is fixed-order and applies verbatim to
\(Q=\Xi^{(31)}\). Hence one may choose a positive \(\lambda_T\) separately on
each regular dyadic window such that

\[
\limsup_{\lambda\downarrow0}
\mathfrak h_+(D_{31,\lambda}^{m red};T,2T)
\le
\mathfrak h_+(\Xi;T,2T)
+\mathfrak h_+(\Xi^{(31)};T,2T),
	ag{L-107404.2}
\]

with endpoint collars and common factors contributing \(o(N(T,2T))\).

Selberg's horizontal first-moment estimate gives

\[
\mathfrak h_+(\Xi;T,2T)=o(N(T,2T)).
	ag{L-107404.3}
\]

## 2. Thirty-first derivative height

Every fixed Xi derivative has all zeros in

\[
|\operatorname{Im}z|\lerac12.
\]

Reality gives conjugate pairing. Consequently

\[
\mathfrak h_+(\Xi^{(31)};T,2T)
\le
rac14igl(N_{31}(T,2T)-R_{31}(T,2T)igr).
	ag{L-107404.4}
\]

The fixed-order zero count satisfies

\[
N_{31}(T,2T)=N(T,2T)+o(N),
\]

while `L-107400` proves

\[
R_{31}(T,2T)>\left(rac{999}{1000}-o(1)ight)N(T,2T).
\]

Therefore

\[
oxed{
\mathfrak h_+(\Xi^{(31)};T,2T)
\le
\left(rac1{4000}+o(1)ight)N(T,2T).
}
	ag{L-107404.5}
\]

Combining (L-107404.2)--(L-107404.5) yields

\[
oxed{
\mathfrak h_+(D_{31,\lambda_T}^{m red};T,2T)
\le
\left(rac1{4000}+o(1)ight)N(T,2T).
}
	ag{L-107404.6}
\]

## 3. Deep/shallow split

For every fixed \(\eta>0\), the model-space height inequality gives

\[
oxed{
\mathcal C_{31,>\eta}(T)
\le
\left(rac1{4000\eta}+o(1)ight)N(T,2T).
}
	ag{L-107404.7}
\]

At

\[
\eta=rac1{100},
\]

all deep endpoint-31 directions cost at most

\[
oxed{
\mathcal C_{31,>1/100}(T)
\le
\left(rac1{40}+o(1)ight)N(T,2T).
}
	ag{L-107404.8}
\]

Since the endpoint-31 total allowance for a \(>90\%\) conclusion is
\(99/1000\), the exact shallow allowance is

\[
oxed{
rac{99}{1000}-rac1{40}
=rac{37}{500}.
}
	ag{L-107404.9}
\]

## Scope

The lemma completely pays the endpoint-31 macroscopic and deep-pole charge.
It does not bound the shallow canonical-correlation/topological defect.
