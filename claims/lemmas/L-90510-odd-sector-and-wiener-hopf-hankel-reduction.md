# L-90510 — RH is equivalent to the odd sector, which is an explicit Wiener–Hopf–Hankel prime form

Claim ID: `L-90510`  
Status: **PROPOSED COMPLETE EXACT PARITY / FORM LEMMA — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-11  
Depends on: corrected pole form `R-90501/L-90506`; Xi-cardinal capture on PR #365; Lévy representation `L-90507`  
Scope: exact parity index splitting and half-line normal form; no positivity theorem

## 1. Reflection decomposition

Let

\[
 (\mathcal Rf)(u)=f(-u).
\]

The zero form `W`, pole-free form `Q=W-P`, gamma term and every prime shift commute with `R`. Hence the test space splits orthogonally into even and odd sectors.

There are no nontrivial real zeros of zeta in `0<s<1`, so every off-line centered zero belongs to a distinct quartet

\[
 \{\omega,\bar\omega,-\omega,-\bar\omega\}.
 \tag{L-90510.1}
\]

Let `p` be the number of such quartets, allowing infinity. Equivalently, the number of reflected off-line pairs in the complete two-sided zero set is `2p`.

## 2. Exact parity index split

For one positive-ordinate reflected pair, let

\[
 H_\omega=L_\omega-L_{\bar\omega}
\]

be its Xi-cardinal negative vector. Evenness of `Xi` gives

\[
 H_\omega(-z)=H_{-\omega}(z).
\]

Therefore

\[
 H_\omega^{\rm ev}=H_\omega+H_{-\omega},
 \qquad
 H_\omega^{\rm odd}=H_\omega-H_{-\omega}
 \tag{L-90510.2}
\]

are respectively even and odd, and each has Weil value `-4m_omega` before pole correction.

The odd pole cardinal

\[
 E_{\rm odd}=E_+-E_-
\]

has pole values `(1,-1)` and vanishes at all nontrivial zeros. Subtracting the unique multiple of `E_odd` makes `H_omega^odd` pole-null without changing its zero values. Thus it remains `Q`-negative. The analogous even correction uses `E_even=E_++E_-`.

On the pole plane, `-P` is positive on the odd line `(a,-a)` and negative on the even line `(a,a)`. The zero-coordinate pullback gives the matching upper bounds. Consequently

\[
 \boxed{
 n_-(Q|_{\rm odd})=p,
 \qquad
 n_-(Q|_{\rm even})=p+1.
 }
 \tag{L-90510.3}
\]

In particular

\[
 \boxed{
 \mathrm{RH}
 \iff Q(f,f)\ge0\quad\text{for every odd admissible }f.
 }
 \tag{L-90510.4}
\]

No pole constraint remains: under RH, for odd `f` one has `P(f,f)=-2|fhat(i/2)|^2`, so `Q=W-P>=0`; under false RH the corrected odd cardinal gives a negative witness.

## 3. Exact half-line correlation

Let `f` be the odd extension of `h in L^2(0,infinity)`, and use

\[
 (T_yf)(u)=f(u-y),\qquad y>0.
\]

Its autocorrelation is real and equals

\[
 \boxed{
 \langle f,T_yf\rangle
 =2\Re\int_0^\infty h(x+y)\overline{h(x)}\,dx
 -\int_0^y h(x)\overline{h(y-x)}\,dx.
 }
 \tag{L-90510.5}
\]

The second integral is real by `x -> y-x`. Moreover

\[
 \boxed{
 \begin{aligned}
 \|f-T_yf\|_2^2={}&
 2\int_0^\infty|h(x+y)-h(x)|^2\,dx\\
 &+\int_0^y|h(x)+h(y-x)|^2\,dx.
 \end{aligned}}
 \tag{L-90510.6}
\]

Thus every gamma jump is a sum of a positive Wiener–Hopf difference square and a positive reflected boundary square.

## 4. Odd prime side

Put

\[
 A_y(h)=\int_0^\infty h(x+y)\overline{h(x)}\,dx,
 \qquad
 B_y(h)=\int_0^y h(x)\overline{h(y-x)}\,dx.
\]

The complete prime term on the odd sector is

\[
 \boxed{
 -2\sum_{n\ge2}{\Lambda(n)\over\sqrt n}
 \langle f,T_{\log n}f\rangle
 =-4\sum_{n\ge2}{\Lambda(n)\over\sqrt n}\Re A_{\log n}(h)
 +2\sum_{n\ge2}{\Lambda(n)\over\sqrt n}B_{\log n}(h).
 }
 \tag{L-90510.7}
\]

The first sum is a Wiener–Hopf translation term; the second is a positive-coefficient Hankel reflection term supported on `x+x'=log n`.

Combining with `L-90507`, the RH-equivalent odd form is

```text
positive continuum Wiener–Hopf difference squares
+ positive continuum reflected boundary squares
+ negative constant mass
- prime Wiener–Hopf translations
+ prime Hankel reflections.
```

This is a genuine half-line operator, not a generic indefinite matrix.

## 5. Trace-class odd operator

Because the Cauchy–Sobolev weight and resolvent kernels are even, `J_(a,c)` commutes with reflection. Restricting its coefficient space to odd functions gives a self-adjoint trace-class operator `A_(a,c)^odd` representing `Q|odd`, and

\[
 \boxed{n_-(A_{a,c}^{\rm odd})=p.}
 \tag{L-90510.8}
\]

Hence RH is equivalent to positivity, Fredholm zero-freeness, or heat-trace nonpositivity of this one half-line Wiener–Hopf–Hankel operator.

## 6. Proof boundary

Proved here:

- exact even/odd negative-index splitting;
- reduction of RH to odd tests alone;
- the half-line correlation and jump-square identities;
- the exact Wiener–Hopf minus Hankel prime decomposition;
- a trace-class odd-sector Fredholm operator.

Not proved:

- positivity of the odd half-line form;
- a total-positivity or reflection-positivity theorem for its Hankel term;
- RH.
