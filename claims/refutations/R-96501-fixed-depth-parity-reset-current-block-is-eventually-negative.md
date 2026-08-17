# R-96501 - Every fixed even-depth parity reset has an eventually negative current Euler truncation

Claim ID: `R-96501`
Status: **PROVED UNCONDITIONAL ASYMPTOTIC NO-GO + DIRECTED COUNTEREXAMPLE**
Created: 2026-08-17
Depends on: `L-96502`; the canonical component-row formula; classical Mertens/Landau fixed-order almost-prime estimates
Replay: `X-96500-parity-covariant-gluing`
RH status: **unproved**

Let

\[
D_{P,Y}(q)=\sum_{d\mid P_{61}}\frac{\mu(d)}{\sqrt d}Q_{Y/d}(q).
\]

For fixed row `q>=2`, integral comparison in the component-row formula gives

\[
D_{P,Y}(q)=a_q\sqrt Y+O_q(\log(2Y)),
\qquad
 a_q=\frac{8}{q(q-1)}
 \prod_{\ell\le61,\ \ell\text{ prime}}(1-\ell^{-1})>0.
\tag{R-96501.1}
\]

The signed current block after stopping all rough histories of length at least
`L` is

\[
B_{L,X}(q)=
\sum_{\substack{m\le X/q,\ m\text{ squarefree}\\
 p\mid m\Rightarrow p\ge67,\ \omega(m)<L}}
\frac{\mu(m)}{\sqrt m}D_{P,X/m}(q).
\tag{R-96501.2}
\]

For each fixed `r`, standard reciprocal almost-prime estimates give

\[
\sum_{\substack{m\le X\\\omega(m)=r}}\frac1m
=\frac{(\log\log X)^r}{r!}
+O_r((\log\log X)^{r-1}),
\]

while the accumulated error from (R-96501.1) is lower order. Hence

\[
\boxed{
\frac{B_{L,X}(q)}{\sqrt X}
=a_q\frac{(-1)^{L-1}}{(L-1)!}(\log\log X)^{L-1}
+O_{L,q}((\log\log X)^{L-2}).}
\tag{R-96501.3}
\]

Therefore:

```text
L even: recursive parity is canonical, but current block is eventually negative;
L odd:  current leading sign is positive, but recursive parity stays reversed.
```

No fixed depth can satisfy both requirements.

The first repaired depth fails concretely at `X=200000`. A direct 256-bit MPFR
interval computation, with directed rounding for every square root, logarithm,
and arithmetic operation, certifies

\[
\boxed{B_{2,200000}(2)<-11,\qquad B_{2,200000}(3)<-2.}
\tag{R-96501.4}
\]

The retained enclosures are

```text
row 2: [-11.2745354467343289724470811741,
        -11.2745354467343289715797194361]
row 3: [ -2.11516352829808095838658166254,
         -2.11516352829808095816974122805]
```

This refutes the proposed two-level positive star `PAST23`; it does not refute
full-row or two-row nonnegativity, which may depend on global cancellation
across arbitrarily many rough levels.
