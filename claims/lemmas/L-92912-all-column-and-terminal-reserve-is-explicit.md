# L-92912 — Retained-cell quadrature has explicit all-column and terminal reserve

Claim ID: `L-92912`  
Status: **PROPOSED COMPLETE ANALYTIC/DIRECTED ESTIMATE — REVIEW REQUIRED**  
RH status: **unproved**

Retain the notation of `L-92911` and put \(\mathcal I_X=\{K+2,\ldots,X-W-3\}\).

## 1. Adjacent retained-cell error

For the finite equality density \(d_X^\star\), define
\[
\varepsilon_X(n)=d_X^\star(n)-\int_n^{n+1}d_X^\star(t)\,dt.
\]
On every retained factor-67 cell, differentiating the explicit finite sum leaves only \(k\le67\). The complete derivative constant is
\[
C_{67}=\sum_{k\le67}\frac{|\mu(k)|}{\sqrt k}
\left(1+\frac12\log\frac{67}{k}\right)<19,
\]
so
\[
|\varepsilon_X(n)|<\frac{19}{2}n^{-3/2}.
\]
Define the cumulative retained-cell seed
\[
E_X^I(n)=\sum_{\substack{m\in\mathcal I_X\\m\ge n}}\varepsilon_X(m).
\]
Then \(E_X^I(n)-E_X^I(n+1)=\mathbf1_{\mathcal I_X}(n)\varepsilon_X(n)\); there is no artificial cutoff atom.

## 2. Every ordinary and detail column

For every physical \(q\ge2\), the exact carry identity gives
\[
v_q(E_X^I)=\sum_{jq\in\mathcal I_X}\varepsilon_X(jq).
\]
With \(M_q=\lceil K/q\rceil\) and \(\sum_{j\ge M}j^{-3/2}<3M^{-1/2}\),
\[
|v_q(E_X^I)|<\frac{57}{2q\sqrt K},
\qquad
|\mathcal D_4v_q(E_X^I)|<\frac{171}{4q\sqrt K}.
\]
The explicit two-point martingale quantizer contributes less than \(200/(q\sqrt K)\) in detail. Therefore
\[
\boxed{|e_X^{\rm nonterm}(q)|<\frac{971}{4q\sqrt K}}
\]
for every \(q\ge2\), including \(q<K\).

For \(2\le q\le X/4\), \(\Omega_X(q)=\log4/\sqrt q>4/(3\sqrt q)\), and hence
\[
\frac{|e_X^{\rm nonterm}(q)|}{\Omega_X(q)}<\frac{129}{\sqrt K}.
\]
Use one common thinning
\[
\tau_K=\frac{\sqrt K}{\sqrt K+130}.
\]
Then the complete one-shot row satisfies
\[
\Xi(d_X)(q)<\frac{\sqrt K+129}{\sqrt K+130}\Omega_X(q)<\Omega_X(q)
\]
on every nonterminal column.

## 3. Terminal annulus

The collar and mismatch can overfill a terminal coordinate by at most
\[
4452X^{-3/2}.
\]
The fixed top omission removes more than
\[
5033X^{-3/2}.
\]
Thus every terminal coordinate retains at least \(581X^{-3/2}\) reserve. Above the retained support the response is zero.

## 4. Ordinary capacity

For finite support, radix-four inversion is the positive identity
\[
C(q)=\sum_{a\ge0}2^a\Xi(4^aq).
\]
Therefore \(\Xi(d_X)\le\Omega_X=\mathcal D_4w_X\) implies \(C_{d_X}\le w_X\) on every ordinary column. The final row is a directly constructed feasible row; its numerical slack is never asserted to be a source packet.
