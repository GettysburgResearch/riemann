# T-105222 — A single debt-free contour cut for 90% and density one

Claim ID: `T-105222`  
Status: **PROVED CONDITIONAL IMPLICATION; boundary interpolation estimate open**  
Depends on: L-105221; L-105222

For \(1\le k\le K\), choose \(\lambda_k\ge0\) and a source-matched
interpolant \(U_{k,\Omega}\) from L-105222. Define
\[
\mathfrak D_{K,\Omega}
=
\sum_{k=1}^K
\left[
\frac1{2\pi i}\int_{\partial\Omega}
\frac{F_{k+1}}{F_k}
(1+\lambda_kU_{k,\Omega})^2\,dz
-
\sum_{\substack{F_k(c)=0\\c\in\Omega\setminus\mathbb R}}
(1+\lambda_k\rho_{k,c})^2
\right].
\tag{1}
\]
Then \(\mathfrak D_{K,\Omega}\) is exactly the sum of the real square defects
\(\sum_{k,c\in\mathbb R}(1+\lambda_k\rho_{k,c})^2\). Hence
\[
\boxed{
R_0\ge R_K-2\mathfrak D_{K,\Omega}-K.
}
\tag{2}
\]

Let \(N(T)\) be a common zero-count scale and suppose
\(R_K(T)/N(T)\ge p_K-o(1)\), with \(K=o(N(T))\). Then:

### 90% cut
\[
\boxed{
\limsup_{T\to\infty}
\frac{\mathfrak D_{K,\Omega(T)}}{N(T)}
<\frac{p_K-0.9}{2}
\Longrightarrow
\liminf\frac{R_0(T)}{N(T)}>0.9.
}
\tag{3}
\]

### Density-one cut
If \(p_K\to1\), \(K=o(N(T))\), and
\[
\mathfrak D_{K,\Omega(T)}=o(N(T)),
\]
then
\[
\boxed{R_0(T)/N(T)\to1.}
\tag{4}
\]

The theorem replaces K separate residue-coherence ratios and K
adjacent-derivative debts by one additive boundary-flux estimate for
source-matched square completions. Its exact remaining interface is:

```text
IBFC105222:
construct or estimate the symmetric interpolation fields U_(k,Omega)
so that the combined boundary flux and nonreal correction satisfy (3),
or o(N) for density one.
```

`IBFC105222` is open. Density one still does not imply RH.
