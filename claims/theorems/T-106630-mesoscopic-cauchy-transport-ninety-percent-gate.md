# T-106630 — Mesoscopic Cauchy-transport certificate for more than ninety percent

Claim ID: `T-106630`  
Status: **UNCONDITIONAL EXACT PRIMAL REDUCTION + ONE CONSTRUCTIVE ARITHMETIC TRANSPORT OPEN**  
Created: 2026-08-26  
Depends on: `T-106620`, `L-106630--L-106631`; pinned
\(R_5/N>997/1000-o(1)\) input  
RH status: **unproved**

Retain the mesoscopic frozen Riemann--Siegel cross-ratios \(U_{5,j}\) of
`T-106620`. Their complete denominator height is at most

\[
\left(\frac3{4000}+o(1)\right)N(T,2T),
\]

so every denominator direction above height \(1/100\) has already been paid
at cost at most \(3N/40+o(N)\).

## 1. Explicit shallow Cauchy data

For each subwindow, let \(E_{-,j}\) synthesize the normalized confluent
Cauchy kernels at the shallow denominator companion zeros. Choose any
source-owned numerator inner subfactor \(A_{+,j}\mid B_{+,j}\), and let
\(E_{+,j}\) synthesize its normalized confluent kernels.

Put

\[
G_{-,j}=E_{-,j}^*E_{-,j},
\quad
G_{+,j}=E_{+,j}^*E_{+,j},
\quad
C_j=E_{-,j}^*E_{+,j}.
\]

For any finite matrix \(X_j\), define the exact generalized transport cost

\[
\boxed{
\mathcal R_j(X_j)
=
\operatorname{tr}\!\left[
G_{-,j}^{-1}
\left(
G_{-,j}
-C_jX_j-X_j^*C_j^*
+X_j^*G_{+,j}X_j
\right)
\right].
}
\tag{T-106630.1}
\]

Every entry is an explicit Cauchy or confluent-Cauchy value determined by the
finite zeta-derivative packets of `T-106620`.

## 2. Exact domination

`L-106630--L-106631` give

\[
\boxed{
\mathfrak C_{\rm meso,sh}(T)
\le
\sum_j\mathcal R_j(X_j).
}
\tag{T-106630.2}
\]

If the complete numerator factor is used and

\[
X_j=G_{+,j}^{-1}C_j^*,
\]

then equality holds. Thus the transport formulation loses nothing, while an
explicit nonoptimal \(X_j\) is already a valid proof certificate.

## 3. Constructive ninety-percent gate

Define `MESOTRANS106630` to be the construction, from the explicit
mesoscopic zeta-derivative packets, of numerator subfactors and matrices
\(X_j\) for which

\[
\boxed{
\limsup_{T\to\infty}
\frac{
\sum_j\mathcal R_j(X_j)
+\mathcal E_{\rm meso,reg}(T)
}{
N(T,2T)
}
<
\frac{11}{500}.
}
\tag{T-106630.3}
\]

Then `T-106620` gives

\[
\boxed{
\mathrm{MESOTRANS}_{106630}
\Longrightarrow
\liminf_{T\to\infty}
\frac{N_0(T,2T)}{N(T,2T)}
>0.9.
}
\tag{T-106630.4}
\]

## 4. Why this is a useful new interface

The open statement is no longer phrased only as a spectral deficit or phase
mean. A proof may exhibit an actual matrix transport and verify one positive
quadratic residual. The normal-equation error is itself exactly positive:

\[
\mathcal R_j(X_j)-\mathfrak C_j
=
\operatorname{tr}\left(
G_{-,j}^{-1}Y_j^*G_{+,j}^{-1}Y_j
\right),
\qquad
Y_j=G_{+,j}X_j-C_j^*.
\]

This is suitable for:

```text
Cauchy interpolation at shallow companion zeros;
approximate-functional-equation construction of X_j;
interval certification on finite windows;
blockwise source ownership and sparse transport;
mollified normal-equation estimates.
```

No denominator-multiplied Hankel source, raw pairwise sum, hidden Gram
condition number, or favorable numerator-degree payment is introduced.

## 5. Boundary

```text
canonical defect = minimum generalized residual    PROVED EXACT
numerator-subfactor monotonicity                    PROVED EXACT
one-pole pseudohyperbolic calibration               PROVED EXACT
raw unwhitened matching shortcut                    REFUTED EXACT
MESOTRANS106630 <11/500                             OPEN / 90%-BEARING
ninety percent / density one / RH                   UNPROVED
```
