# L-102868 — The balanced core form is exact through phases, owners and gauges

Claim ID: `L-102868`  
Status: **PROVED EXACT SOURCE-TYPING THEOREM**  
Created: 2026-08-24  
Depends on: `L-102830--L-102867`  
RH status: **not assumed**

Retain one clean largest-two squareclass

\[
N=pq\,a^2,
\qquad p>q>P^+(a),
\]

and write

\[
Y=X/(pq).
\]

Apply `L-102867` to the literal core Möbius coefficient before introducing any
additive phase. The surviving balanced packet is

\[
\mathcal B_{p,q}(X)
=\frac1{\sqrt{pq}}
\sum_{\substack{u,v>Y^{1/6}\\m\le Y^{1/6}}}
\frac{a_U(u)a_U(v)\mu(m)}{uvm}
R_L\!\left(\frac{X}{pq\,u^2v^2m^2}\right),
\tag{L-102868.1}

with `U=floor(Y^(1/6))` and the support restriction

\[
uvm\asymp\sqrt Y.
\]

## 1. Phase functoriality

Every owner phase in `L-102860--L-102865` is a multiplicative character of the
physical product modulo a prime which is coprime to `uvm`. Thus, for any
selected phase modulus `ell`,

\[
e_\ell(hN)
=e_\ell(hpq\,u^2v^2m^2).
\]

The exact Vaughan identity is coefficientwise, so it commutes with:

```text
all nonzero additive owner phases;
all 15 adaptive phase choices;
all owner and squareclass projections;
Euler/half-divisor/Wick gauge transfer;
the fixed outer-ray observation;
one-octave physical localization.
```

No zero phase or extra source copy is introduced.

## 2. Dyadic Type-II blocks

Split `u`, `v`, and `m` into dyadic ranges

\[
U_1\le u<2U_1,
\qquad
V_1\le v<2V_1,
\qquad
M\le m<2M.
\]

Every nonempty block satisfies

\[
\boxed{
U_1,V_1>Y^{1/6},
\qquad
M\le Y^{1/6},
\qquad
U_1V_1M\asymp\sqrt Y.
}
\tag{L-102868.2}

Hence both large variables are genuine Type-II variables and the residual
Möbius variable is short.

The truncated-divisor coefficient obeys

\[
|a_U(n)|\le\tau(n),
\]

so all representation multiplicities created by the decomposition are
`Y^o(1)` and remain inside the already-established factor-pair ledger.

## 3. Global owner range

Since every prime divisor of `uvm` is smaller than the second owner `q`,

\[
q>Y^{1/6}.
\]

As `p>q`,

\[
pq>Y^{1/3}.
\]

Because `Y=X/(pq)`,

\[
\boxed{pq>X^{1/4}.}
\tag{L-102868.3}

Thus every squareclass remaining after the Type-I removal lies above the
quarter-power owner threshold. Equivalently, its square core has length at
most `X^(3/8)`.

## 4. Exact surviving coherent form

For two clean squareclasses `P=pq` and `Q=rs`, the remaining cross packet is a
sum of dyadic blocks of the form

\[
\boxed{
\begin{aligned}
\mathscr B_{P,Q}
={}&\sum_{\substack{u,v,m\\u',v',m'}}
\frac{a_{U_P}(u)a_{U_P}(v)\mu(m)}{uvm\sqrt P}
\frac{a_{U_Q}(u')a_{U_Q}(v')\mu(m')}{u'v'm'\sqrt Q}\\
&\times
\mathcal K\!\left(
\log\frac{P(uvm)^2}{Q(u'v'm')^2}
\right),
\end{aligned}}
\tag{L-102868.4}

with the chosen nonzero owner phases inserted exactly as in `L-102865` and
with `mathcal K` supported in the fixed ratio-eight window.

All Type-I, complete-lattice and small-squareclass terms have finite
logarithmic cost. The coherent sum of (L-102868.4) is the only arithmetic
quantity retained in `T-102880`.
