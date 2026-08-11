# T-91001 — RH is equivalent to a unit-disc Stieltjes/Pick property on one safe Euler line

Claim ID: `T-91001`  
Status: **PROPOSED COMPLETE RH-EQUIVALENT ANALYTIC CRITERION — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-11  
Depends on: `T-90903`, `L-91001`, and the standard zero count  
RH status: **unproved**

## 1. The generating function

For

\[
 a_k(x)=\frac{\mathfrak S_k(x)}{(k+2)!},
\]

define

\[
\boxed{
 \mathcal A_x(w)=\sum_{k\ge0}a_k(x)w^k.
}
\tag{T-91001.1}
\]

The zero count and the rational kernel imply local uniform convergence wherever the denominators below do not vanish. Summing the geometric series in `k` gives

\[
\boxed{
\begin{aligned}
\mathcal A_x(w)
={}&\sum_{\rho=1/2+i\gamma}
 m_\rho\frac{2u^2}
 {(1+u^2)^2(1+u^2-w)}\\
&-2\sum_{\Re\rho>1/2}m_\rho
\left[
 \frac{z^2}{(1-z^2)^2(1-z^2-w)}
 +\frac{\bar z^2}{(1-\bar z^2)^2(1-\bar z^2-w)}
\right],
\end{aligned}}
\tag{T-91001.2}
\]

where `u=gamma-x` and `z=rho-(1/2+ix)`.

## 2. RH gives a Stieltjes and Pick function

Under RH, `L-91001` gives the positive measure `nu_x` on `[0,1]` and

\[
\boxed{
 \mathcal A_x(w)
 =\int_{[0,1]}\frac{d\nu_x(\lambda)}{1-w\lambda}.
}
\tag{T-91001.3}
\]

Consequently:

1. `A_x` is holomorphic on `C\[1,infinity)`;
2. `A_x(w)>0` for real `w<1`;
3. `Im A_x(w)>=0` whenever `Im w>0`;
4. every Pick matrix
   \[
   \left(
   \frac{\mathcal A_x(w_i)-\overline{\mathcal A_x(w_j)}}
        {w_i-\overline{w_j}}
   \right)_{i,j}
   \]
   is PSD;
5. every real Loewner matrix below the cut is PSD.

The Pick matrix has the exact Gram representation

\[
\boxed{
 \frac{\mathcal A_x(w_i)-\overline{\mathcal A_x(w_j)}}
 {w_i-\overline{w_j}}
 =\int_{[0,1]}
 \frac{\lambda\,d\nu_x(\lambda)}
 {(1-w_i\lambda)(1-\overline{w_j}\lambda)}.
}
\tag{T-91001.4}
\]

## 3. A false-RH pair creates an interior pole

Suppose

\[
 \rho=\frac12+y+ix,
 \qquad 0<y<\frac12,
\]

is a right-side zero of multiplicity `m`. At the matching centre `x`, its reflected pair contributes

\[
 -\frac{4my^2}
 {(1-y^2)^2(1-y^2-w)}.
\tag{T-91001.5}
\]

Therefore `A_x` has a pole at

\[
\boxed{
 w_\rho=1-y^2\in(3/4,1),
}
\tag{T-91001.6}
\]

with residue

\[
\boxed{
 \operatorname*{Res}_{w=w_\rho}\mathcal A_x(w)
 =\frac{4my^2}{(1-y^2)^2}>0.
}
\tag{T-91001.7}
\]

No other zero can cancel this pole. A second term has the same pole only if its centered coordinate squares to `y^2`; in the chosen right half-strip that is the same reflected pair, whose multiplicity adds.

Hence

\[
\boxed{
\mathrm{RH}
\Longleftrightarrow
\mathcal A_x\text{ is holomorphic in }|w|<1
\text{ for every }x\in\mathbb R.
}
\tag{T-91001.8}
\]

The Stieltjes/Pick property in the unit disk is an equivalent strengthening of the holomorphy condition. Unlike the large-order proof of `T-90903`, the reverse implication here requires no terminal-pair selection: every individual off-line pair exposes its own pole at its matching ordinate.

## 4. Coefficient-growth criterion

By Cauchy-Hadamard, (T-91001.8) is equivalent to

\[
\boxed{
 \mathrm{RH}
 \Longleftrightarrow
 \limsup_{k\to\infty}|a_k(x)|^{1/k}\le1
 \quad\text{for every real }x.
}
\tag{T-91001.9}
\]

A matching off-line pair at depth `y` forces the radius at its ordinate to be at most `1-y^2`, and therefore

\[
 \limsup_{k\to\infty}|a_k(x)|^{1/k}
 \ge\frac1{1-y^2}>1.
\tag{T-91001.10}
\]

This is the analytic-radius form of large-order isolation.

## 5. Depth-resolved version

Fix `0<eta<1/2` and put `R_eta=1-eta^2`. From

\[
 \Re(1-z^2)=1-(\Re z)^2+(\Im z)^2,
\]

one obtains

\[
\boxed{
\begin{aligned}
&\zeta(s)\ne0
 \quad\text{for }\Re s>\frac12+\eta\\
&\quad\Longleftrightarrow\quad
 \mathcal A_x(w)\text{ is holomorphic for }|w|<R_\eta
 \quad\text{for every real }x.
\end{aligned}}
\tag{T-91001.11}
\]

Thus the radial variable encodes zero depth exactly:

\[
 y\longleftrightarrow w=1-y^2.
\]

## 6. Countable and finite certificates

The coefficient formulation uses integer `k` and, by continuity, rational centres `x`. Each coefficient is one absolutely convergent prime-power series on `Re(s)=3/2` plus explicit rational/polygamma terms. Therefore false RH implies finite strict certificates of each of the following types:

```text
one negative normalized coefficient a_k(r);
one negative Hausdorff difference D_(k,m)(r);
one negative shifted beta-Hankel principal minor;
one failed finite Pick matrix at points near the interior pole.
```

The pole itself is an exact structural witness. Indeed, immediately above a real pole with positive residue, `Im A_x(w)<0`, so even a `1 x 1` Pick matrix fails once the point is chosen sufficiently close. Each coefficient or finite-difference witness remains one absolutely convergent prime-power series on `Re(s)=3/2` plus explicit rational/polygamma terms, and hence admits a finite outward-rounded prime cutoff. No such Riemann-data certificate is claimed here.

## 7. Exact frontier

```text
RH -> Hausdorff/Stieltjes/Pick structure       PROPOSED COMPLETE
matching off-line pair -> pole in (3/4,1)      EXACT
unit-disc holomorphy <=> RH                    PROPOSED COMPLETE
coefficient spectral radius <=> RH             PROPOSED COMPLETE
depth eta <-> analytic radius 1-eta^2          PROPOSED COMPLETE
prime-side unit-disc Stieltjes/Pick theorem     OPEN / RH-EQUIVALENT
Riemann Hypothesis                              UNPROVED
```