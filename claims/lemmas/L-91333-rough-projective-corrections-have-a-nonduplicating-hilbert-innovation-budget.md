# L-91333 — Rough projective corrections have a nonduplicating Hilbert innovation budget

Claim ID: `L-91333`  
Status: **PROVED EXACT HILBERT-TELESCOPE / RANK-ONE DOMINATION THEOREM**  
Created: 2026-08-12  
Depends on: `L-91319`, `L-91326`, `L-91324`  
RH status: **unproved**

## 1. Common diagonal metric

Put

\[
 X=L-R,
 \qquad
 Y=L-2R,
\]

and let

\[
 S=
 \begin{pmatrix}
 1&-1\\
 1&-2
 \end{pmatrix},
 \qquad
 H=S^{\mathsf T}S
 =\begin{pmatrix}2&-3\\-3&5\end{pmatrix}>0.
\tag{L-91333.1}

For one rough prime, write

\[
 r=p^{-1/2},
 \qquad A=1-r^2,
 \qquad B=1-r.
\]

The signed physical state matrix is

\[
 M_p=S^{-1}
 \begin{pmatrix}A&0\\0&B\end{pmatrix}S.
\tag{L-91333.2}

Therefore its Hilbert innovation is

\[
\boxed{
 \Delta_p
 =H-M_p^{\mathsf T}HM_p
 =S^{\mathsf T}
  \begin{pmatrix}
   1-A^2&0\\0&1-B^2
  \end{pmatrix}S
 \succeq0.
}
\tag{L-91333.3
}

The metric is independent of `p`.

## 2. Exact innovation telescope

For an ordered finite sequence `p_1,...,p_k`, put

\[
 P_0=I,
 \qquad
 P_j=M_{p_j}\cdots M_{p_1}.
\]

Then

\[
\boxed{
 H-P_k^{\mathsf T}HP_k
 =\sum_{j=1}^k
  P_{j-1}^{\mathsf T}\Delta_{p_j}P_{j-1}.
}
\tag{L-91333.4
}

Every term is positive semidefinite. Thus the innovation ports of distinct
rough primes are not independent copies of one reservoir: they form one exact
orthogonal-energy telescope whose total never exceeds the initial metric `H`.

For a state `z_0`, writing `z_{j-1}=P_{j-1}z_0`,

\[
\boxed{
 \sum_{j=1}^k z_{j-1}^{\mathsf T}\Delta_{p_j}z_{j-1}
 =z_0^{\mathsf T}Hz_0-z_k^{\mathsf T}Hz_k
 \le z_0^{\mathsf T}Hz_0.
}
\tag{L-91333.5
}

## 3. The projective correction is paid by one innovation

`L-91319` shows that the minimal positive SHARP-preserving completion uses the
scalar correction

\[
 c_p(z)=\tau_pR,
 \qquad
 \tau_p=r(1-r).
\tag{L-91333.6}

In diagonal coordinates `R=X-Y`. Put

\[
 \alpha=1-A^2=r^2(2-r^2),
 \qquad
 \beta=1-B^2=r(2-r).
\]

Then

\[
 z^{\mathsf T}\Delta_pz
 =\alpha X^2+\beta Y^2.
\tag{L-91333.7}

Weighted Cauchy gives

\[
 \alpha X^2+\beta Y^2
 \ge\frac{\alpha\beta}{\alpha+\beta}(X-Y)^2.
\tag{L-91333.8}

Moreover

\[
\begin{aligned}
 &(2-r^2)(2-r)
 -2(2+r-r^3)(1-r)^2\\
 &\qquad
 =r\left(4-2r+r^2-4r^3+2r^4\right)>0
\end{aligned}
\]

for `0<r<=1/2`. Hence

\[
 \frac{\alpha\beta}{\alpha+\beta}
 >2r^2(1-r)^2
 =2\tau_p^2.
\tag{L-91333.9}

Therefore

\[
\boxed{
 |c_p(z)|^2
 <\frac12 z^{\mathsf T}\Delta_pz.
}
\tag{L-91333.10
}

The branch correction consumes less than half of the Hilbert innovation created
by that same Euler factor.

## 4. Global nonduplication

At stage `j`, put

\[
 c_j=\tau_{p_j}R(z_{j-1}).
\]

Combining (L-91333.5) and (L-91333.10),

\[
\boxed{
 \sum_{j=1}^k|c_j|^2
 <\frac12 z_0^{\mathsf T}Hz_0.
}
\tag{L-91333.11
}

Thus no diagonal endpoint port is spent once per prime. All projective
corrections share one finite quadratic budget.

If the ordered product tends strongly to zero in the diagonal coordinates,
the innovation sum exhausts the initial energy exactly; otherwise the unspent
terminal energy is the positive remainder `z_k^T H z_k`.

## 5. Gram/Schur formulation

Let `C_j` be the rank-one correction operator corresponding to `c_j`, normalized
so that

\[
 C_j^*C_j=|c_j|^2.
\]

Equation (L-91333.10) is the branch-local Schur domination

\[
 C_j^*C_j
 \preceq\frac12
 P_{j-1}^{\mathsf T}\Delta_{p_j}P_{j-1}.
\tag{L-91333.12}

Summing and using (L-91333.4),

\[
\boxed{
 \sum_j C_j^*C_j
 \preceq\frac12 H.
}
\tag{L-91333.13
}

This is precisely the form preserved by the positive evaluation, summation,
quantization and physical color-erasure functors of `L-91324`. Consequently the
projective rough corrections may be combined before physical projection without
reusing one branch-local Schur port.

The theorem does not identify `H/2` with the complete native endpoint capacity
matrix; that final source-to-port embedding remains separate.

## 6. Relation to the scalar-port firewall

`R-91303` refutes multiplication of independent scalar endpoint ports. The
present theorem uses neither scalar multiplication nor one fresh port per prime.
It uses a common Hilbert metric and the exact identity

\[
 H-P_k^THP_k=\sum\text{innovations}.
\]

Thus it supplies the correct noncommutative replacement for the failed scalar
Euler product.

## 7. Proof boundary

```text
common Hilbert metric for every rough prime       EXACT
positive innovation per Euler factor              EXACT
ordered innovation telescope                      EXACT
projective correction < half local innovation     EXACT
global nonduplicating correction budget           EXACT
positive-functor/color-erasure preservation        AVAILABLE
embedding H/2 into native endpoint capacity        OPEN
least-prime source partition                       OPEN
Riemann Hypothesis                                UNPROVEN
```
