# R-106040 — Composite-conductor Kummer leverage is tensor-local

Claim ID: `R-106040`  
Status: **PROVED EXACT NORMALIZATION FIREWALL**  
Created: 2026-08-24  
Depends on: `L-106020`, `L-106024`, `L-106027`  
Programme issues: #743, #736, #737  
RH status: **unproved**

An earlier unpublished continuation proposed the scalar composite-conductor
leverage

\[
\left(1-\frac{\varphi(q)}q\right)4^{\omega(q)}.
\tag{R-106040.1}
\]

That formula is withdrawn. It conflates two different additive frames:

```text
all nonzero frequencies modulo q;

the tensor of nonzero local square phases at every p|q.
```

The CV/XD owner packet uses the second frame.

Let

\[
q=\prod_{p\mid q}p
\]

be odd and squarefree. On one fixed local quadratic-class sector, the exact
one-prime physical-observation norm is

\[
\frac{p-1}{p+1}.
\]

Therefore the squarefree tensor frame has sector norm

\[
\boxed{
 c(q)=\prod_{p\mid q}\frac{p-1}{p+1}.
}
\tag{R-106040.2}
\]

The reciprocal principal-root-fibre weight is

\[
\boxed{
 c(q)^{-1}=\prod_{p\mid q}\frac{p+1}{p-1}.
}
\tag{R-106040.3}
\]

These are not equal to `1-phi(q)/q`. Already for `q=15`,

\[
 c(15)=\frac13,
\qquad
1-\frac{\varphi(15)}{15}=\frac7{15}.
\]

Moreover there are

\[
2^{\omega(q)}
\]

local quadratic-class sectors. If they are recombined by source-blind Cauchy,
the exact cost is that number of sectors. It is not a new amplifier gain.

## Binding rule

A valid composite-conductor argument must retain:

```text
one nonzero local additive phase at every selected prime;
the local quadratic-class vector sigma;
the tensor product of the one-prime Kummer frames;
the complete 2^omega(q) principal/quadratic root fibre;
the fixed full-source Euler completion before residual selection.
```

It may not replace this tensor geometry by a scalar `1-phi(q)/q` eigenvalue.

The corrected theorem is `L-106040`; the corrected conditional frontier is
`T-106040`. This refutation changes no theorem already published in
`L-106020--L-106027` and establishes no RH result.
