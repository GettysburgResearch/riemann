# L-91316 — The Euler square-root remainder has a strict positive endpoint Schur port

Claim ID: `L-91316`  
Status: **PROVED EXACT DOMINATION / POSITIVE TWO-PORT THEOREM — CONSERVATIVE CHILD ROUTING STILL OPEN**  
Created: 2026-08-12  
Depends on: `L-90025`, `L-91110/L-91111`, `L-91311/L-91315`, and the effective square-root-sum bracket used in `T-90002`  
RH status: **unproved**

## 1. Two cell functions

Put

\[
 c=-\zeta(1/2)>0,
 \qquad
 S_N=\sum_{k=1}^{N}k^{-1/2}.
\]

For real `x>=1`, write

\[
 N=\lfloor x\rfloor,
 \qquad
 t=\sqrt x.
\]

Define the Euler lattice remainder

\[
 \boxed{
 \rho(x)=S_N-2\sqrt x+c
 }
\tag{L-91316.1}
\]

and the positive endpoint-renewal atom

\[
 \boxed{
 \varrho(x)=\frac{2N}{\sqrt x}-S_N.
 }
\tag{L-91316.2}
\]

In logarithmic coordinates, (L-91316.2) is exactly the kernel `varrho` of
`L-90025`. In particular

\[
 \varrho(x)>0
 \qquad(x\ge1).
\tag{L-91316.3}
\]

The boundary port of `L-91311` is a finite small-prime linear combination of
copies of `rho`. The purpose of this theorem is to dominate it by a positive
linear combination of the native endpoint atom `varrho` with a fixed strict
margin.

## 2. Sharp elementary zeta-half gate

The only close finite gate below is

\[
 \boxed{
 c>\frac{10\sqrt2-1}{9}.
 }
\tag{L-91316.4}

It is certified without a floating zeta evaluation. Write

\[
 \eta(1/2)=\sum_{m\ge1}(-1)^{m-1}m^{-1/2},
 \qquad
 c=\frac{\eta(1/2)}{\sqrt2-1}.
\]

Euler's transformation gives the positive series

\[
 \eta(1/2)
 =\sum_{r\ge0}\frac1{2^{r+1}}
  \sum_{k=0}^{r}(-1)^k\binom rk(k+1)^{-1/2}.
\tag{L-91316.5}
\]

Every inner finite difference is positive. The first sixteen transformed terms,
combined with directed rational square-root enclosures, give

\[
 \eta(1/2)>0.6048983739403347
\]

and

\[
 c>1.4603538582241882
 >\frac{10\sqrt2-1}{9}.
\tag{L-91316.6}
\]

The companion exact checker retains the rational comparison. In particular

\[
 c>\frac54,
 \qquad
 c>\frac{17}{16},
 \qquad
 c>\sqrt2.
\tag{L-91316.7}
\]

## 3. Strict `8/9` domination

### Theorem 3.1

For every real `x>=1`,

\[
 \boxed{
 |\rho(x)|<\frac89\varrho(x).
 }
\tag{L-91316.8}
\]

### Proof: upper side

The inequality

\[
 \rho\le\frac89\varrho
\]

is equivalent to

\[
 17S_N+9c
 \le18t+\frac{16N}{t}.
\tag{L-91316.9}
\]

On the cell `sqrt(N)<=t<sqrt(N+1)`, the right side is increasing, because

\[
 \frac d{dt}\left(18t+\frac{16N}{t}\right)
 =18-\frac{16N}{t^2}\ge2.
\]

Its minimum is `34sqrt(N)`. The effective Euler bracket used in `T-90002`
and `L-90025` gives

\[
 S_N
 \le2\sqrt N-c+\frac1{2\sqrt N}.
\tag{L-91316.10}
\]

Therefore

\[
 17S_N+9c
 \le34\sqrt N-8c+\frac{17}{2\sqrt N}
 <34\sqrt N
\]

by `c>17/16`. This proves the upper side strictly.

### Proof: lower side

The inequality

\[
 \rho\ge-\frac89\varrho
\]

is equivalent to

\[
 S_N+9c
 \ge18t-\frac{16N}{t}.
\tag{L-91316.11}
\]

The right side is increasing, and its cell supremum is

\[
 \frac{2N+18}{\sqrt{N+1}}.
\tag{L-91316.12}
\]

For `N>=2`,

\[
 \frac{2N+18}{\sqrt{N+1}}
 \le2\sqrt N+10.
\tag{L-91316.13}
\]

Indeed, after squaring, the difference reduces to

\[
 8(N-7)+10\sqrt N(N+1)>0,
\]

whose minimum on the integers `N>=2` occurs at `N=2`, where it is
`30sqrt(2)-40>0`.

The lower Euler bracket gives

\[
 S_N
 \ge2\sqrt N-c+rac1{2\sqrt N}
 -\frac1{24N^{3/2}}-rac1{16N^{5/2}}.
\tag{L-91316.14}
\]

The final three terms are positive for `N>=1`. Thus, using `c>5/4`,

\[
 S_N+9c>2\sqrt N+8c>2\sqrt N+10,
\]

which proves (L-91316.11) for `N>=2`.

For `N=1`, the cell supremum is `10sqrt(2)`, and (L-91316.11) becomes

\[
 1+9c>10\sqrt2,
\]

which is exactly (L-91316.4). This completes the proof. ∎

The constant `8/9` is close to sharp: the largest ratio is approached at the
left limit `x to 2-`, but no optimality statement is needed.

## 4. Two explicit positive ports

Define

\[
 \boxed{
 P_+(x)=\frac{\varrho(x)+\rho(x)}2,
 \qquad
 P_-(x)=\frac{\varrho(x)-\rho(x)}2.
 }
\tag{L-91316.15}
\]

Then

\[
 P_\pm(x)>\frac1{18}\varrho(x)>0.
\tag{L-91316.16}
\]

The first port has the particularly simple formula

\[
 \boxed{
 P_+(x)=\frac c2-\frac{\{x\}}{\sqrt x}.
 }
\tag{L-91316.17}
\]

The second is

\[
 \boxed{
 P_-(x)=\sqrt x+\frac{\lfloor x\rfloor}{\sqrt x}
       -S_{\lfloor x\rfloor}-\frac c2.
 }
\tag{L-91316.18}
\]

Thus the signed Euler lattice remainder is already a difference of two strictly
positive endpoint-scale ports:

\[
 \rho=P_+-P_-,
 \qquad
 \varrho=P_++P_-.
\tag{L-91316.19}
\]

Equivalently,

\[
 \boxed{
 \begin{pmatrix}
  \varrho(x)&\rho(x)\\
  \rho(x)&\varrho(x)
 \end{pmatrix}
 \succeq
 \frac19\varrho(x)I_2.
 }
\tag{L-91316.20}
\]

This is a pointwise strict Schur/Pick port, not merely an integral bound.

## 5. Finite small-prime Boolean port

Let `P` be any squarefree finite product and define

\[
 \mathcal B_P(x)
 =\sum_{\substack{d\mid P\\d\le x}}
  \frac{\mu(d)}{\sqrt d}\rho(x/d),
\tag{L-91316.21}
\]

\[
 \mathcal V_P(x)
 =\sum_{\substack{d\mid P\\d\le x}}
  \frac1{\sqrt d}\varrho(x/d).
\tag{L-91316.22}
\]

Termwise use of (L-91316.8) gives

\[
 \boxed{
 |\mathcal B_P(x)|
 <\frac89\mathcal V_P(x).
 }
\tag{L-91316.23}
\]

Hence

\[
 \boxed{
 \begin{pmatrix}
  \mathcal V_P&\mathcal B_P\\
  \mathcal B_P&\mathcal V_P
 \end{pmatrix}
 \succeq
 \frac19\mathcal V_PI_2.
 }
\tag{L-91316.24}
\]

Every positive linear endpoint, row, score, or ordinary-carry functional
preserves this matrix inequality. The two scalar channels

\[
 \frac{\mathcal V_P\pm\mathcal B_P}{2}
\]

are nonnegative continuum endpoint densities and therefore admit the positive
martingale B-spline quantization of `L-91110`; the finite collar is paid by
`L-91111/L-91114/L-91115` at bounded score cost.

## 6. The `P_53` port has less than four units of off-diagonal mass

The critical normalization of the endpoint atom is

\[
 \frac12\int_1^\infty\varrho(x)x^{-3/2}dx=1.
\tag{L-91316.25}
\]

Scaling gives

\[
 \frac12\int_1^\infty\mathcal V_P(x)x^{-3/2}dx
 =\sum_{d\mid P}\frac1d.
\tag{L-91316.26}
\]

For

\[
 P=P_{53}=\prod_{p\le53}p,
\]

the exact rational value is

\[
 \sum_{d\mid P_{53}}\frac1d
 =\prod_{p\le53}\left(1+\frac1p\right)
 =\frac{3328677500682240}{742518990138757}
 <\frac92.
\tag{L-91316.27}
\]

Consequently

\[
 \boxed{
 \frac12\int_1^\infty
 |\mathcal B_{53}(x)|x^{-3/2}dx
 <4.
 }
\tag{L-91316.28}
\]

The rough boundary port is therefore bounded in the exact endpoint-score
normalization, uniformly over the parent endpoint.

## 7. Exact balanced-ray colligation

Normalize the balanced ray of `L-91311/L-91315` by

\[
 e_*(x)=\frac{E_*(x)}{c_*}.
\]

Then the exact rough renewal is

\[
 \sum_{\substack{m\in\mathcal M_{59}\\m\le x}}
 m^{-1/2}e_*(x/m)
 =-\mathcal B_{53}(x).
\tag{L-91316.29}
\]

Combining with (L-91316.23) gives the conservative two-port identity

\[
 \boxed{
 \mathcal V_{53}(x)
 =\sum_{m\in\mathcal M_{59},\,m\le x}
   m^{-1/2}e_*(x/m)
  +\bigl(\mathcal V_{53}(x)+\mathcal B_{53}(x)\bigr),
 }
\tag{L-91316.30}
\]

where both the input port `mathcal V_53` and the output slack port
`mathcal V_53+mathcal B_53` are strictly positive endpoint densities. Moreover

\[
 \mathcal V_{53}+\mathcal B_{53}
 >\frac19\mathcal V_{53}.
\tag{L-91316.31}
\]

Thus the additive balanced-ray boundary defect no longer requires a signed or
alternating correction: it embeds into a strict positive two-port colligation
with bounded critical mass.

## 8. What remains

The theorem closes the **additive boundary port** in a native positive endpoint
coordinate. It does not by itself assign each individual rough child state to
finite ordinary/radix-four columns. The remaining operation is conservative
routing of the centered children through the projective `(L,R)` cone while
preserving divisor destinations.

```text
Euler lattice remainder domination              EXACT
strict endpoint Schur port                       EXACT
finite P_53 port and critical mass <4             EXACT
positive endpoint quantization of both ports      AVAILABLE
additive balanced boundary defect                 CLOSED AT BOUNDED COST
capacity-faithful conservative child routing      OPEN
Riemann Hypothesis                                UNPROVED
```
