# R-103000 — TP2 does not orient order-inverting source minors

Claim ID: `R-103000`  
Status: **PROVED EXACT SOURCE-ORDER FIREWALL**  
Created: 2026-08-25  
Depends on: `L-103000--L-103003`  
RH status: **not assumed**

The common positive half-kernel is `TP_2`, and its derivative companion has a strict order-Wronskian sign. These kernel facts do not orient an arbitrary signed arithmetic source.

Choose two physical locations `n<m` in a range where

\[
\mathcal W_{n,m}(X)<0
\]

for some `X`.

Let `nu_n=nu_m=1`.

### Increasing source ratio

Take

\[
\mu_n=0,
\qquad
\mu_m=1.
\]

Then

\[
\Delta_{n,m}(\mu,\nu)=-1,
\]

so

\[
\mathcal P_{\mu,\nu}(X)
=-\mathcal W_{n,m}(X)>0.
\]

### Decreasing source ratio

Interchange the two values:

\[
\mu_n=1,
\qquad
\mu_m=0.
\]

Now

\[
\Delta_{n,m}(\mu,\nu)=+1,
\]

and

\[
\mathcal P_{\mu,\nu}(X)
=\mathcal W_{n,m}(X)<0.
\]

Thus the same `TP_2` kernel produces either physical sign under two source-exact coefficient arrays.

Consequently none of the following implications is valid without an arithmetic source-order theorem:

```text
TP2 common mother -> Boolean core orientation;
Wronskian sign -> Pluecker current orientation;
positive endpoint kernels -> signed middle Euler source;
order-concordant sector control -> order-inversion sector control.
```

The actual arithmetic inversion current remains open. This counterfixture does not refute that current; it prevents the kernel theorem from being promoted beyond its exact scope.