# T98300 — Tao–Stieltjes cross-scale completion port

Status: **unconditional hardening; one cross-scale theorem open; RH unproved**  
Base: PR #582 at `699f9f119a66823702e96fba95cc8b14b8251c60`  
Compared: PR #607 at `a28f8e5b8c90e3aef30e97053ed42e9ddde9c665`; PR #608 at `f362acf56bbbbd183976b6377fbe883193886e1a`

## 1. Exact unit Schur port on every multiplicative semigroup

For a prime set `P`, let `S_P` be its multiplicative semigroup and put

\[
A_P(x)=\sum_{\substack{n\le x\\n\in S_P}}\frac{\mu(n)}n,
\quad N_P(x)=\#(S_P\cap[1,x]),
\quad H_P(x)=\sum_{\substack{n\le x\\n\in S_P}}\frac1n.
\]

Let `N_(P^c)(x)` count the complementary-prime semigroup. Restricted Möbius
inversion gives

\[
xA_P(x)=N_{P^c}(x)+E_P(x),
\qquad |E_P(x)|\le N_P(x)-H_P(x).
\]

Consequently

\[
C_P(x)=\frac{N_P(x)+N_{P^c}(x)-H_P(x)}x
\]

satisfies

\[
\boxed{
K_P(x)=\begin{pmatrix}C_P(x)&A_P(x)\\A_P(x)&C_P(x)\end{pmatrix}\succeq0,
\qquad 0\le C_P(x)\le1.}
\]

This is a genuinely unit-normalized passive completion port at reciprocal
exponent one, with a self-contained elementary proof.

## 2. The unique 5:3 scalar has a positive monotone Stieltjes source

The positive unsieved dictionary is

\[
q_\diamond(1)=0,
\quad q_\diamond(2)=15,
\quad q_\diamond(4)=3,
\quad q_\diamond(n)=6\text{ otherwise}.
\]

For

\[
H_X(n)=\min(\log4,\log(X/n))_+,
\quad b_0(X)=\sum_n\frac{q_\diamond(n)}{\sqrt n}H_X(n),
\quad h_0(X)=\frac{b_0(X)}{\sqrt X},
\]

directed finite-cell arithmetic and an analytic tail prove

\[
\boxed{dh_0\ge0,\qquad 0\le h_0(X)<12,\qquad h_0(X)\uparrow12.}
\]

Since `a_diamond=q_diamond*mu`, the actual factor-four scalar obeys

\[
\boxed{
\frac{\mathcal A_X}{\sqrt X}
=\sum_{d\le X}\frac{\mu(d)}d h_0(X/d)
=\int_{[1,X]}A_{\mathbb P}(X/x)\,dh_0(x).}
\]

Thus the whole unsieved source is positive; no unsigned rough reservoir is
introduced.

## 3. Exact integrated completion matrix

Integrating the unit Schur ports against `dh_0` gives

\[
\boxed{
\mathfrak J_X=
\int_{[1,X]}K_{\mathbb P}(X/x)\,dh_0(x)
=\begin{pmatrix}\Gamma_X&\mathcal A_X/\sqrt X\\
\mathcal A_X/\sqrt X&\Gamma_X\end{pmatrix}\succeq0.}
\]

Moreover

\[
0\le\Gamma_X<h_0(X)<12,
\qquad \Gamma_X\to12,
\qquad \mathcal A_X/\sqrt X\to0.
\]

This identifies the exact completion diagonal and the exact trace-free scalar.

## 4. Exact Markov state

For a new prime `p` the four quotient profiles satisfy

\[
A_{P\cup\{p\}}(x)=A_P(x)-p^{-1}A_P(\lfloor x/p\rfloor),
\]

\[
N_{P\cup\{p\}}(x)=\sum_{k\ge0}N_P(\lfloor x/p^k\rfloor),
\]

\[
H_{P\cup\{p\}}(x)=\sum_{k\ge0}p^{-k}H_P(\lfloor x/p^k\rfloor),
\]

\[
N_{(P\cup\{p\})^c}(x)=N_{P^c}(x)-N_{P^c}(\lfloor x/p\rfloor).
\]

Hence `(A,N,H,N_comp)` on the `O(sqrt N)` quotient DAG is the smallest exact
state exposed by the semigroup proof.

## 5. Binding no-go theorems

1. The finite Euler system `P={3,5,7,11,13}`, `N=26` has every local unit
   semigroup port PSD, but its half-order reciprocal-Julia boundary is
   `>1.1306169339746402`. Independent pointwise ports therefore do not survive
   the Abel/dyadic lift.
2. Since `Gamma_X -> 12`, retaining any nonzero completion trace in the
   Mellin--Landau observable produces a `sqrt X` background that masks the
   off-line poles. The final extraction must be trace-free.
3. For every fixed prime `p`, the homogeneous Dickman margin
   `rho(u)-p^(-1)rho(u-1)` is eventually negative because
   `rho(u-1)/rho(u)->infinity`. PR #608's one-prime mechanism is necessarily
   mesoscopic and cannot be extrapolated to the root by a better error constant.

## 6. Exact remaining theorem

The surviving closure target is **CSCBI**, a source-faithful cross-scale
completion Bellman inequality: construct one common completion Gram on the
quotient DAG whose diagonal blocks are the exact `K_P(x)`, whose prime updates
obey the four recurrences above, and whose trace-free Schur short controls the
Abel/dyadic scalar by the unit boundary.

PRs #607--#608 provide this in the hereditary mesoscopic tail. The critical
finite block remains open. A proof would give the factor-four scalar
nonnegative, then the zero-safe Mellin--Landau consumer would imply RH.

```text
Tao unit Schur port                     PROVED EXACT
positive unsieved Stieltjes source      PROVED DIRECTED/ANALYTIC
integrated completion matrix            PROVED EXACT
four-profile Markov recurrence          PROVED EXACT
pointwise lift to RJTE                   REFUTED
trace-bearing Landau shortcut            REFUTED
fixed-prime all-depth Dickman extension REFUTED
CSCBI                                    OPEN / RH-BEARING
Riemann Hypothesis                       UNPROVEN
```

## Replay

```text
PASS_T98300_TAO_STIELTJES_COMPLETION_PORT
824fba0aed136007a26bb553aa1e0d18d22a9810417cad6c23ad0b9038bba0d1
13 hostile tests: PASS
```
