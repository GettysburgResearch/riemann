# L-32718 — The true Q=4 pole-current innovation has vanishing fresh-reserve cost

Claim ID: `L-32718`  
Title: Although the true four-adic innovation is the RH-bearing Möbius-contracted Chebyshev discrepancy rather than the deterministic Kummer innovation, its square consumes a vanishing fraction of the newly available top-scale reserve  
Status: **PROPOSED COMPLETE UNCONDITIONAL COFINAL THEOREM — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-11  
Dependencies: source correction `R-32707`; `L-32713`; `L-32715`; PR #337 `L-32708`  
Scope: exactly dilated integer rows and the true pole current; continuous block collars are treated in the final assembly

## 1. Source-correct current renewal

Retain

\[
 c_4=e_4*\Lambda_4,
 \qquad
 q_4=\mu*c_4=b_4*\Lambda_4.
\]

Let

\[
 h_4=(\varepsilon-4\delta_4)*\Lambda_4.
\]

The coefficient recurrence `c_4=h_4+delta_4*c_4` gives

\[
 \boxed{
 q_4=\mu*h_4+\delta_4*q_4.
 }
 \tag{L-32718.1}
\]

For a row `e=(n,j)` and its exact lift `4e=(4n,4j)`, define the true unnormalized pole current

\[
 Q_e=\mathcal L_e(q_4).
\]

Since

\[
 \chi_{4n,4d}(4j)=\chi_{n,d}(j),
\]

(L-32718.1) gives the exact source-correct renewal

\[
 \boxed{
 Q_{4e}=Q_e+I_e,
 \qquad
 I_e=\mathcal L_{4e}(\mu*h_4).
 }
 \tag{L-32718.2}
\]

Divisor switching identifies

\[
 I_e
 =H_4(4n)-H_4(4j)-H_4(4n-4j),
 \tag{L-32718.3}
\]

where

\[
 H_4(x)=\Psi_4(x)-4\Psi_4(x/4)
 =\psi(x)-4\psi(x/4)
  +3\lfloor\log_4x\rfloor\log4.
 \tag{L-32718.4}
\]

Thus `I_e` is the true prime-sensitive innovation. No deterministic bound for it is assumed.

## 2. The innovation is controlled by the two endpoint currents

Equation (L-32718.2) gives trivially

\[
 \boxed{
 |I_e|^2
 \le2|Q_{4e}|^2+2|Q_e|^2.
 }
 \tag{L-32718.5}
\]

PR #337 `L-32708` proves uniformly on the quarter-balanced cone

\[
 \frac{|Q_e|^2}{R_4(e)}\longrightarrow0.
 \tag{L-32718.6}
\]

The same theorem applies to the lifted row:

\[
 \frac{|Q_{4e}|^2}{R_4(4e)}\longrightarrow0.
 \tag{L-32718.7}
\]

Meanwhile `L-32713` gives, for every fixed `epsilon>0`, cofinally

\[
 R_4(4e)\ge(16-\epsilon)R_4(e).
 \tag{L-32718.8}
\]

Therefore

\[
 \frac{|Q_e|^2}{R_4(4e)}
 \le
 {1\over16-\epsilon}
 { |Q_e|^2\over R_4(e)}
 \longrightarrow0.
 \tag{L-32718.9}
\]

Combining (L-32718.5), (L-32718.7), and (L-32718.9),

\[
 \boxed{
 \frac{|I_e|^2}{R_4(4e)}\longrightarrow0
 }
 \tag{L-32718.10}
\]

uniformly on the full quarter-balanced cone.

This is unconditional: the only analytic input is the classical PNT already used in `L-32708`.

## 3. Exact normalized cross-term inequality

As in the withdrawn shortcut, but now with the correctly typed `I_e`, put

\[
 \alpha_n={4n+1\over n+1}.
\]

The sharp completed-square inequality gives

\[
 \boxed{
 { |Q_e+I_e|^2\over4n+1}
 \le
 { |Q_e|^2\over n+1}
 +{ |I_e|^2\over3n}.
 }
 \tag{L-32718.11}
\]

Using (L-32718.2),

\[
 \boxed{
 { |Q_{4e}|^2\over4n+1}
 \le
 { |Q_e|^2\over n+1}
 +{ |I_e|^2\over3n}.
 }
 \tag{L-32718.12}
\]

## 4. A fixed fresh top-scale reserve fraction pays the true innovation

From (L-32718.10), for every fixed `delta>0` and every sufficiently large balanced row,

\[
 |I_e|^2
 \le\delta R_4(4e).
\]

Choose, for example, `delta=1/20`. Since

\[
 {4n+1\over3n}<\frac32,
\]

cofinally

\[
 \boxed{
 { |I_e|^2\over3n}
 \le
 {1\over8}{R_4(4e)\over4n+1}.
 }
 \tag{L-32718.13}
\]

Combining with (L-32718.12),

\[
 \boxed{
 { |Q_{4e}|^2\over4n+1}
 -{1\over8}{R_4(4e)\over4n+1}
 \le
 { |Q_e|^2\over n+1}.
 }
 \tag{L-32718.14}
\]

The true innovation and its cross term are therefore paid entirely from a fixed fraction of the reserve at the **new** parent `4e`.

## 5. No double spending with the complete reflected row ledger

`L-32715` proves, after paying the full Selberg forcing, product-source term, both individual source-convolved terms, and the current square, that at least

\[
 \frac34R_4(4e)
\]

remains unused on every sufficiently large balanced top row.

Equation (L-32718.13) consumes only `R_4(4e)/8`. Hence at least

\[
 \boxed{
 \left(\frac34-\frac18\right)R_4(4e)
 =\frac58R_4(4e)
 }
 \tag{L-32718.15}
\]

remains after **all current-scale reflected terms and the complete true innovation** have been paid.

The inherited reserve `R_4(e)` is never charged. Therefore successive generations use disjoint top-scale reserve accounts.

## 6. Finite-chain consequence

For a finite chain `e_k=4^ke_0`, apply (L-32718.14) at every sufficiently large generation. The coefficient-one current terms telescope, while generation `k` spends only reserve at `e_k`:

\[
 \boxed{
 { |Q_{e_K}|^2\over4^Kn_0+1}
 \le
 { |Q_{e_0}|^2\over n_0+1}
 +\sum_{k=1}^K
 {1\over8}{R_4(e_k)\over4^kn_0+1}.
 }
 \tag{L-32718.16}
\]

Inside the reflected ledger these reserve terms occur with dissipative sign and are absorbed generation by generation, leaving the coefficient-one delayed current and polynomial collars only.

## 7. Proof boundary

Closed here, subject to review:

1. exact source-correct true-current renewal;
2. identification of the prime-sensitive innovation;
3. vanishing innovation/reserve ratio without estimating the innovation directly;
4. normalized coefficient-one cross-term inequality;
5. payment from a fixed fresh top-scale reserve fraction;
6. compatibility with the complete reflected row budget without double spending.

Still open:

1. exact continuous-block/floor-collar integration;
2. conversion of the finite-chain row ledger into the declared unit-block recurrence;
3. RH.
