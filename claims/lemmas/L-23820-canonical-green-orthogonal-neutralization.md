# L-23820 — Canonical Green orthogonal neutralization

Claim ID: `L-23820`  
Title: Every complete carry residual splits into one logarithmic scalar mode and an exact zero-objective Green correction  
Status: **PROPOSED EXACT FINITE THEOREM — independent review requested**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-08  
Issue: #238  
Dependencies: PR #248 `L-24508/L-24509/L-24510`; exact finite linear algebra  
Scope: the signed divisor-gradient carry system; no asymptotic estimate or RH conclusion

## 1. Setting

Fix one finite carry endpoint and let `Q` be the complete active ordinary-prime
or prime-power constraint set. Let

\[
G=G_X\succ0
\tag{L-23820.1}
\]

be the endpoint-projected divisor Dirichlet Gram of `L-24509`, let

\[
\lambda_q=\Lambda(q),
\tag{L-23820.2}
\]

and let

\[
r=v(b_0)-w
\tag{L-23820.3}
\]

be the complete signed residual of any starting carry profile `b_0`.

A Green correction with coefficient vector `T` changes the residual and the
prime-ramp objective exactly by

\[
 r\longmapsto r-GT,
\tag{L-23820.4}
\]

and

\[
 J(b_T)-J(b_0)=-\lambda^TGT.
\tag{L-23820.5}
\]

No sign restriction on `b_T` or `T` is needed for the signed divisor-gradient
consumer of `L-24508`.

Put

\[
E=\lambda^TG\lambda>0,
\qquad
\delta=\lambda^Tr.
\tag{L-23820.6}
\]

The number `delta` is the exact logarithmic/prime-ramp discrepancy of the
starting profile.

## 2. Orthogonal residual and canonical correction

Define

\[
\boxed{
 r^\perp
 =r-\frac{\delta}{E}G\lambda.}
\tag{L-23820.7}
\]

Then

\[
\lambda^Tr^\perp=0.
\tag{L-23820.8}
\]

Let

\[
\boxed{T^\perp=G^{-1}r^\perp.}
\tag{L-23820.9}
\]

The corrected residual is exactly

\[
\begin{aligned}
 r-GT^\perp
 &=r-r^\perp\\
 &=\boxed{\frac{\delta}{E}G\lambda.}
\end{aligned}
\tag{L-23820.10}
\]

Thus every residual direction except the single logarithmic Riesz direction is
removed in one exact correction.

## 3. The correction has zero objective cost

Equation (L-23820.5) and (L-23820.8) give

\[
\boxed{
 J(b_{T^\perp})-J(b_0)
 =-\lambda^TGT^\perp
 =-\lambda^Tr^\perp
 =0.}
\tag{L-23820.11}
\]

More generally, every residual vector `h` satisfying

\[
\lambda^Th=0
\tag{L-23820.12}
\]

has the exact zero-objective correcting flow

\[
T_h=G^{-1}h.
\tag{L-23820.13}
\]

This is a signed equality, not an inequality or a positive-cover argument.

## 4. Exact Green-energy decomposition

The orthogonality in the `G^-1` metric gives

\[
\boxed{
 r^TG^{-1}r
 =\frac{\delta^2}{E}
 +(r^\perp)^TG^{-1}r^\perp.}
\tag{L-23820.14}
\]

The second summand is the complete high-rank nonlogarithmic carry defect. It is
not required to be small: it can be neutralized exactly at zero objective cost.
Only the first summand contains the RH-bearing scalar.

## 5. Consequences for the later mutations

### 5.1 Same-sign high-rank Möbius cubes

The rank-`K` same-sign cube of PR #239 can contribute arbitrarily many source
coordinates to `r`. Equation (L-23820.10) does not count those coordinates. It
projects their complete signed aggregate into:

```text
one logarithmic scalar;
plus one exact Green-orthogonal vector.
```

The orthogonal vector is removed by (L-23820.9). Hence source rank alone is not
a blocker for this reduction.

### 5.2 Zero reflected reserve

No reflected Schur reserve is used. The neutralization is an exact equality and
survives the mutation in which a proposed positive reserve collapses to zero or
to the tautology `2E=2E`.

### 5.3 Nonnegative-cover obstruction

The correction is signed. It therefore does not incur the `Omega(sqrt X)` cost
proved for nonnegative monotone covers on PR #254.

## 6. What the theorem does not prove

Equation (L-23820.10) leaves the scalar residual

\[
\frac{\delta}{E}G\lambda.
\]

Proving that its positive part has subpolynomial size is exactly the remaining
prime-ramp problem. This theorem removes all orthogonal carry geometry; it does
not hide or solve the scalar Mertens/prime mode.

The next theorem must therefore act on `delta` by a source-specific signed
quotient-layer barrier, not by a generic Green norm, contact count, or unsigned
operator estimate.

## 7. Proof boundary

Closed exactly:

- the logarithmic Riesz projection;
- exact zero-objective removal of the full orthogonal residual;
- the Green-energy Pythagorean identity;
- robustness to arbitrary source rank and zero reflected reserve.

Open:

- a strict lower-scale recurrence for the scalar residual `delta`;
- the prime-ramp estimate;
- RH.
