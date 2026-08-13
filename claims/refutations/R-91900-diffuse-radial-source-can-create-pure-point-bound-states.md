# R-91900 — A diffuse radial medium can create a pure-point bound state through nonlocal feedback

Claim ID: `R-91900`  
Status: **EXACT FRIEDRICHS-MODEL FIREWALL**  
Created: 2026-08-13  
Corrects the motivation, not the conditional implication, of: `T-91800`  
Depends on: `L-91800`--`L-91803`  
RH status: **unproved**

## 1. The overstrong intuition

The radial-spectral-type programme observes that the declared arithmetic
one-particle source is diffuse in horizontal depth, whereas the crossed-zero
model port is naturally graded by point masses at the exact off-line depths.

The abstract theorem of `L-91802` is correct **provided** the completed
source-to-model map is interval local, equivalently an `L^infinity(dr)`-module
map.  What is false is the stronger intuition

```text
diffuse source coefficients
    =>
no pure-point output in a global conservative realization.
```

A nonlocal feedback loop can create a bound state from a completely diffuse
medium.

## 2. Exact rank-one Friedrichs model

Let

\[
 \mathcal H=L^2([1,2],dr),
 \qquad
 (H_0f)(r)=r f(r),
 \qquad
 v(r)=1.
\]

Then `H_0` has purely absolutely continuous spectrum `[1,2]`, and `v` is a
diffuse source vector.  For `t>0` put

\[
 \boxed{
 H_t=H_0-t|v\rangle\langle v|.
 }
 \tag{R-91900.1}
\]

The family is affine, hence norm-resolvent continuous, in the diffuse
parameter `t`.

A number `-kappa<0` is an eigenvalue of `H_t` precisely when

\[
 \boxed{
 1=t\int_1^2\frac{dr}{r+\kappa}
  =t\log\frac{2+\kappa}{1+\kappa}.
 }
 \tag{R-91900.2}

Indeed, the eigenvector equation gives

\[
 f(r)=\frac{tc}{r+\kappa},
 \qquad
 c=\langle v,f\rangle,
\]

and a nonzero `c` exists exactly under (R-91900.2).

## 3. An atomic spectral-flow birth

The function

\[
 \kappa\longmapsto
 \log\frac{2+\kappa}{1+\kappa}
\]

is strictly decreasing from `log 2` to zero.  Consequently

\[
 t_c=\frac1{\log2}
\]

is the exact threshold:

```text
0<t<t_c      no negative eigenvalue;
t=t_c        one zero eigenvalue, f(r)=1/r;
t>t_c        one simple negative eigenvalue.
```

For `t>t_c` the eigenvalue is explicit.  Writing `E=exp(1/t) in (1,2)`,

\[
 \boxed{
 \kappa(t)=\frac{2-E}{E-1}>0.
 }
 \tag{R-91900.3}

Thus the negative-index counting function is

\[
 \boxed{
 N_-(H_t)=\mathbf1_{(t_c,\infty)}(t),
 }
 \tag{R-91900.4}

and its distributional derivative is the point mass

\[
 \boxed{
 dN_-=\delta_{t_c}.
 }
 \tag{R-91900.5}

A continuously varying diffuse medium has created an atomic spectral-flow
output.

## 4. The missing property is locality

Let `P_I` denote multiplication by the indicator of an interval
`I subset [1,2]`.  For disjoint positive-length intervals `I,J`,

\[
 \boxed{
 P_I|v\rangle\langle v|P_J
 =|\mathbf1_I\rangle\langle\mathbf1_J|\ne0.
 }
 \tag{R-91900.6}

Hence the feedback term does not commute with the radial multiplication
algebra.  It is not an `L^infinity(dr)`-module map and couples separated depth
cells before the spectrum is read.

This is exactly the loophole excluded by RLSL.  The model does not refute the
conditional theorem `T-91800`; it proves that interval locality cannot be
inferred from source diffuseness, continuity, positivity of the source metric,
or existence of a global conservative colligation.

## 5. Corrected interpretation of the crossed-zero atom

A crossed-zero depth atom should not automatically be viewed as an atom
transported from the source.  It may instead be the spectral-flow jump of a
global feedback or Birman--Schwinger loop.

The correct alternatives are therefore:

```text
Route A:
    prove the strong interval-module property RLSL;

Route B:
    identify the global feedback loop and prove strict small gain,
    excluding every Birman--Schwinger eigenvalue 1.
```

The second route is developed in `L-91900`--`T-91900`.

## 6. Exact boundary

```text
diffuse affine source family                         EXACT
global nonlocal rank-one feedback                    EXACT
pure-point bound-state birth                         EXACT
spectral-flow atom at t=1/log 2                      EXACT
source diffuseness alone excludes atomic output      FALSE
RLSL with interval locality                          STILL SUFFICIENT
completed zeta interval locality                     OPEN / RH-EQUIVALENT
completed zeta strict-feedback small gain            OPEN / RH-EQUIVALENT
Riemann Hypothesis                                   UNPROVED
```
