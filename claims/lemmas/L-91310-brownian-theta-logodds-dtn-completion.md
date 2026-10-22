# L-91310 — The Brownian log-odds cell is a positive two-copy difference channel

Claim ID: `L-91310`  
Status: **CORRECTED EXACT LOCAL CELL; ONE-COPY DtN CLAIM WITHDRAWN**  
Created: 2026-08-12  
Corrected: 2026-08-12  
RH status: **unproved**

## 1. The exact local cell

For `v in (-1,1)` and `a>0`, put

\[
u_{a,\pm}(v)
=\left(\frac{1+v}{1-v}\right)^{\pm a/2}.
\]

Then

\[
\boxed{
-\frac d{dv}
\left((1-v^2)\frac d{dv}u_{a,\pm}\right)
+
\frac{a^2}{1-v^2}u_{a,\pm}
=0.
}
\]

The operator

\[
\mathcal S_a
=-\partial_v(1-v^2)\partial_v+rac{a^2}{1-v^2}
\]

has the nonnegative quadratic form

\[
\int_{-1}^{1}
\left[(1-v^2)|f'(v)|^2+rac{a^2}{1-v^2}|f(v)|^2\right]dv.
\]

Thus the cell is an exact positive Sturm--Liouville component.

## 2. Correct two-copy coordinate

Pair the two BPY Gamma sums as

\[
\Sigma^+=A+D,
\qquad
\Sigma^-=A-D.
\]

With

\[
Z_+=\frac12\log(A+D)+C,
\qquad
Z_-=\frac12\log(A-D)+C,
\]

define

\[
\boxed{
\Delta=Z_+-Z_-=\operatorname{artanh}(D/A),
}
\]

and

\[
\boxed{
S=Z_++Z_-=\frac12\log(A^2-D^2)+2C.
}
\]

The exact half-size tilt is

\[
(\Sigma^+\Sigma^-)^{1/4}=e^{S/2-C}.
\]

Setting `v=D/A`, the local functions are

\[
u_{a,\pm}(v)=e^{\pm a\Delta},
\]

and their odd/even transfer is

\[
\frac{u_{a,+}-u_{a,-}}{u_{a,+}+u_{a,-}}
=\tanh(a\Delta).
\]

The first version of this lemma incorrectly identified
`artanh(D/A)` with the one-copy BPY logarithm. `R-91304` records the exact
correction.

## 3. Complete reflection form

The Xi Pick quadratic in the two-copy Brownian representation is

\[
\boxed{
\mathcal R_a(F)
=\mathbb E\left[
 \sinh(aS)
 \int_{-S/2}^{S/2}
 \overline{F(x+\Delta/2)}F(x-\Delta/2)\,dx
\right].
}
\]

Both coordinates are load-bearing:

```text
Delta  relative displacement of the two copies;
S      oriented interval and the factor sinh(aS);
tilt   exp(S/2-C).
```

The local `Delta` cell alone does not determine the sign.

## 4. Positive reservoirs retained

The following unconditional positive pieces remain valid candidates for a
coupled bulk:

1. the supersymmetric theta Hamiltonian `H_theta=4Q_theta^*Q_theta`;
2. the Gamma(4)--Beta(2,2) Jacobi Dirichlet form;
3. the local log-odds Sturm--Liouville cell in `Delta`;
4. the prime Poisson/Fock difference form;
5. the radial `p=2` Riesz port.

They must be combined before the boundary trace is taken.

## 5. Correct route-III theorem

> **Sum--Difference DtN Identity (`SDDI_a`).**  
> Construct a closed positive form on the exact coupled `(S,Delta)` reservoir,
> with the theta, Poisson, and `p=2` channels retained, such that
> \[
> \mathcal R_a(F)=\|\mathcal J_aF\|^2
> \]
> for every exponential polynomial `F`, or equivalently such that its Weyl
> kernel is the Xi positive-real kernel.

`SDDI_a` is sufficient for the corrected one-vector theorem `T-91303` and the
minimal one-node exhaustion `L-91313`. It remains open and RH-bearing.

## 6. Exact status

```text
log-odds Sturm--Liouville cell             EXACT
cell transfer = tanh(a Delta)              EXACT
Delta = artanh(D/A)                        EXACT
S and the exact half-size tilt             EXACT
one-copy Z = artanh(D/A)                   FALSE
one-variable DtN realization of Xi         WITHDRAWN
coupled S--Delta boundary identity          OPEN / RH-BEARING
Riemann Hypothesis                          UNPROVED
```
