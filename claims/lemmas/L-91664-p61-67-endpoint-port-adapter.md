# L-91664 — Endpoint port normalization for the finite prime block through 61

Claim ID: `L-91664`  
Status: **PROVED EXACT NORMALIZATION ADAPTER — ROOT CAPACITY PLACEMENT REMAINS SEPARATE**  
Created: 2026-08-14  
Depends on: the pointwise `8/9` domination in `L-91316`  
RH status: **unproved**

Let

\[
\rho(x)=\sum_{k\le x}k^{-1/2}-2\sqrt x-\zeta(1/2),
\qquad
\varrho(x)=\frac{2\lfloor x\rfloor}{\sqrt x}-\sum_{k\le x}k^{-1/2}.
\]

The exact scalar estimate is

\[
|\rho(x)|<\frac89\varrho(x)\qquad(x\ge1).
\tag{L-91664.1}
\]

For any squarefree finite product `P`, define

\[
\mathcal B_P(x)=\sum_{d\mid P,\ d\le x}\frac{\mu(d)}{\sqrt d}\rho(x/d),
\qquad
\mathcal V_P(x)=\sum_{d\mid P,\ d\le x}\frac1{\sqrt d}\varrho(x/d).
\]

Termwise use of (L-91664.1) gives

\[
|\mathcal B_P(x)|<\frac89\mathcal V_P(x).
\tag{L-91664.2}
\]

Therefore

\[
\mathcal P_{P,+}=\frac{\mathcal V_P+\mathcal B_P}{2},
\qquad
\mathcal P_{P,-}=\frac{\mathcal V_P-\mathcal B_P}{2}
\]

are strictly positive and satisfy

\[
\mathcal P_{P,\pm}(x)>\frac1{18}\mathcal V_P(x)>0.
\tag{L-91664.3}
\]

For

\[
P_{61}=\prod_{p\le61}p,
\]

the exact critical mass is

\[
\frac12\int_1^\infty\mathcal V_{P_{61}}(x)x^{-3/2}\,dx
=\prod_{p\le61}\left(1+\frac1p\right)
=\frac{399441300081868800}{86204059532560853}<5.
\tag{L-91664.4}
\]

The final inequality is the integer comparison

\[
399441300081868800<5\cdot86204059532560853.
\]

Consequently

\[
\frac12\int_1^\infty|\mathcal B_{P_{61}}(x)|x^{-3/2}\,dx
<\frac{40}{9}<5.
\tag{L-91664.5}
\]

Thus the endpoint port in the finite-block-through-61 normalization retains
strict positivity and one absolute critical-mass bound. The old numerical
`P_53` estimate `<4` is not reused; only the constant changes.

Both positive channels admit the linear positive martingale B-spline
quantization. Their collar and score charges remain bounded independently of
`X`. Placement inside the residual native root capacity is a separate NRC
obligation.

```text
pointwise finite-block Schur domination          EXACT
strictly positive two-channel port               EXACT
critical positive mass <5                        EXACT
off-diagonal critical mass <40/9                 EXACT
root residual-capacity placement                 OPEN / NRC
Riemann Hypothesis                               UNPROVEN
```
