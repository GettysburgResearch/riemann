# L-99960 — Both owner-packing alternatives are equivalent to RH on the canonical packet

Claim ID: `L-99960`  
Status: **PROVED CONDITIONAL-EQUIVALENCE THEOREM**  
Created: 2026-08-20  
Frozen packet: PR #666 at `7ae9e3e15b8bcb0a5f382db49f31ad385b02e24a`  
RH status: **not assumed in the forward implications; used only for the converses**

Let

\[
\beta(n)=\mu(n)-\mathbf1_{67\mid n}\mu(n/67),
\]

and let the canonical block kernel be

\[
\psi_L=\mathcal F_LT,
\qquad
c_{L,y}(n)=\frac{\beta(n)}{\sqrt n}\psi_L(y/n),
\qquad
f_L(y)=\sum_n c_{L,y}(n).
\]

Retain the PR #659 parameters

\[
M_L=\left\lfloor\frac{L}{(\log(L+e))^3}\right\rfloor\vee1,
\qquad
\tau_L=\frac1{\log(L+e)},
\]

the positive inverse coefficients

\[
b_{L,k}=\binom{M_L+k-1}{k},
\]

and the support/complexity bounds

\[
\operatorname{supp}\psi_L\subset[1,R_L],
\quad
R_L=2^{M_L+3}=2^{o(L)},
\quad
\|\psi_L\|_\infty+
\operatorname{Var}_{\log}\psi_L=2^{o(L)},
\]

\[
\sum_{k=0}^{L+1}b_{L,k}=2^{o(L)}.
\tag{L-99960.1}
\]

Define the exact Hardy and divisor packets

\[
Q_L(y)=
\sum_{m,n}c_{L,y}(m)c_{L,y}(n)\min(m,n)^{2\tau_L},
\tag{L-99960.2}
\]

and

\[
\mathcal G_L(y)=
\sum_{d\ge1}J_{2\tau_L}(d)
\left|\sum_{d\mid n}c_{L,y}(n)\right|^2.
\tag{L-99960.3}
\]

Then the following are equivalent:

1. the Riemann Hypothesis;
2. `HTOC99810` for the canonical packet;
3. `DGOC99810` for the canonical packet.

## 1. Either packing theorem implies RH

By the exact Hardy identity of PR #666,

\[
Q_L(y)=|f_L(y)|^2+
2\tau_L\int_1^\infty
 t^{2\tau_L-1}
 \left|\sum_{n\ge t}c_{L,y}(n)\right|^2dt,
\]
so

\[
Q_L(y)\ge|f_L(y)|^2.
\tag{L-99960.4}
\]

Likewise `J_(2 tau)(1)=1`, and the `d=1` term of (L-99960.3) is exactly
`|f_L(y)|^2`; hence

\[
\mathcal G_L(y)\ge|f_L(y)|^2.
\tag{L-99960.5}
\]

Consequently either inverse-weighted packing estimate gives the blockwise
subpower `L^1(dy/y)` bound for `|f_L|`. The positive inverse of PR #659 then
gives subpower logarithmic negative mass for the zero-safe compact packet.
The frozen Mellin--Landau consumer excludes every off-line zero. Thus

\[
\boxed{
HTOC99810\Longrightarrow RH,
\qquad
DGOC99810\Longrightarrow RH.
}
\tag{L-99960.6}
\]

## 2. RH implies every truncated Hardy tail is subpower

Assume RH. The Littlewood criterion gives, for every `eta>0`,

\[
B_\beta(x):=\sum_{n\le x}\beta(n)
=O_\eta(x^{1/2+\eta}).
\tag{L-99960.7}
\]

Fix `y` in a PR #659 inverse block and put

\[
S_{L,y}(t)=\sum_{n\ge t}
\frac{\beta(n)}{\sqrt n}\psi_L(y/n).
\]

The support lies in `[y/R_L,y]`. Abel summation on each smooth cell, followed
by summation over the finitely many activation cells, gives uniformly in `t`

\[
\boxed{
|S_{L,y}(t)|
\ll_\eta
2^{o(L)}y^\eta.
}
\tag{L-99960.8}
\]

Indeed the boundary terms use
`|B_beta(u)|u^(-1/2)<=u^eta`, while the Stieltjes derivative of
`u^(-1/2)psi_L(y/u)` has total weighted size
`2^{o(L)}R_L^eta`.

Since

\[
y^{2\tau_L}=2^{o(L)},
\qquad
\log R_L=o(L),
\]

(L-99960.8) and the Hardy identity imply

\[
\boxed{Q_L(y)^{1/2}\le2^{o(L)}y^\eta.}
\tag{L-99960.9}
\]

Using (L-99960.1), integrating over the inverse blocks and then taking `eta`
arbitrarily small proves `HTOC99810`.

## 3. RH implies every divisor-owner square is subpower

For `d` with `beta(d)!=0`, `L-99961` gives the exact factorization

\[
\sum_{d\mid n}c_{L,y}(n)
=\frac{\beta(d)}{\sqrt d}
\sum_{r\ge1}\frac{g_d(r)}{\sqrt r}
 f_L\!\left(\frac{y}{dr}\right),
\tag{L-99960.10}
\]

where `g_d(r)>=0`. For every fixed `eta>0`, its Euler factors give

\[
\sum_{r\ge1}\frac{g_d(r)}{r^{1/2+\eta}}
\ll_{\eta,\epsilon}d^\epsilon
\qquad(\epsilon>0).
\tag{L-99960.11}
\]

Apply the RH bound from the same Abel argument to `f_L`. Choosing the small
Euler-factor loss below `eta/2`, we obtain

\[
\left|\sum_{d\mid n}c_{L,y}(n)\right|
\ll_\eta
2^{o(L)}y^\eta d^{-1/2-\eta/2}.
\tag{L-99960.12}
\]

Also `J_(2 tau_L)(d)<=d^(2 tau_L)`. For large `L`, `2 tau_L<eta/2`; hence

\[
\begin{aligned}
\mathcal G_L(y)
&\ll_\eta 2^{o(L)}y^{2\eta}
\sum_{d\ge1}d^{-1-\eta+2\tau_L}\\
&\ll_\eta2^{o(L)}y^{2\eta}.
\end{aligned}
\tag{L-99960.13}
\]

The inverse-block sum again has subpower mass, so `DGOC99810` follows.

## 4. Disposition

The two positive squares are valuable normal forms, but they are not weaker
unconditional substitutes for the scalar RH obstruction. Each contains the
unknown canonical packet as its root square, and under RH every additional
Hardy/divisor term is automatically subpower.

```text
RH -> HTOC99810                         PROVED
RH -> DGOC99810                         PROVED
HTOC99810 -> RH                         INHERITED EXACT
DGOC99810 -> RH                         INHERITED EXACT
both alternatives independently weaker  FALSE
Riemann Hypothesis                       UNPROVED
```
