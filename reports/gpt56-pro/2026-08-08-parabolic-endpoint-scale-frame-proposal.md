# Research report — parabolic endpoint-scale frame and blocker theorem

**Agent:** `gpt56-pro`  
**Date:** 2026-08-08  
**Repository:** `gfreund123/riemann`  
**Branch:** `research/gpt56-pro-262-parabolic-scale-frame`  
**Frozen research base:** PR #248 at `5f2b25f89afbb90a3bc4ca6d40148f530303eb54`  
**Status:** **FULL PROPOSAL WITH NEW EXACT THEOREMS; ONE EXPLICIT BLOCKER ESTIMATE OPEN**  
**RH:** **UNPROVEN**

## 1. Objective

The prior review identified the canonical signed Green correction

\[
T_*=G_X^{-1}r_X
\]

and recommended a positivity-preserving deformation.  Re-entering the live
repository showed that PR #248 had already closed most finite signed transport
geometry but still ended at the scalar prime-ramp obstruction.

The present pass asked a more specific question:

> Can the sharp parabolic seed be repaired while remaining inside the genuine
> nonnegative average-binomial carry cone, rather than solving the constraints
> in signed coordinates and attempting to restore positivity afterward?

The answer is structurally yes.  The seed itself, and every increment in its
endpoint, are nonnegative carry-row objects.  This produces a new positive scale
frame and a deterministic finite greedy packing.  The remaining asymptotic
hinge is one explicit endpoint-blocker estimate with a favorable
`T^(-3/2)` charge.

## 2. Main exact advances

### 2.1 The parabolic seed is already a nonnegative carry packing

For

\[
 b_X(m)=2\sqrt m
 \left[\log(X/m)-2(1-\sqrt{m/X})\right],
\]

put

\[
 A_X(m)=\frac{b_X(m)}{m-1},
 \qquad
 d_X(n)=(n+1)\Delta^2A_X(n).
\]

`L-26201` proves

\[
\boxed{d_X(n)\ge0.}
\]

The proof is continuous convexity, not finite experimentation.  Writing
`A_X=f_Xg` gives

```text
f_X >= 0,
f_X' <= 0,
f_X'' > 0,
g > 0,
g' < 0,
g'' > 0,
```

so every term in

\[
A_X''=f_X''g+2f_X'g'+f_Xg''
\]

is nonnegative and the interior curvature is strict.

The exact carry identities of PR #248 then give

\[
\sum_nd_X(n)\beta_{nq}=v_q(b_X),
\]

and

\[
\sum_nd_X(n)G_n=J_X(b_X)
\ge4\sqrt X-O(\log X).
\]

Thus the parabolic seed never failed the positive row cone.  It failed only
column feasibility.

### 2.2 Endpoint differences are positive atoms

For integer endpoints, embed `d_T` in one common row space and define

\[
a_T=d_T-d_{T-1}.
\]

`L-26201` proves

\[
\boxed{a_T(n)>0\quad(2\le n<T).}
\]

The load-bearing derivative is

\[
C_Y(x)=\partial_{\log Y}A_Y(x)
=\frac{2(\sqrt x-x/\sqrt Y)}{x-1}.
\]

Its second derivative is positive whenever `Y>=x`.  The two entering endpoint
rows are treated separately and remain positive.  Therefore

\[
\boxed{d_X=\sum_{T=3}^Xa_T}
\]

is a positive one-dimensional scale decomposition.

Each atom has a positive lower-triangular carry response

\[
\Gamma_T(q)=\sum_na_T(n)\beta_{nq},
\]

with

\[
\Gamma_T(q)>0\quad(q<T),
\qquad
\Gamma_T(q)=0\quad(q\ge T).
\]

The atom entropies telescope to the sharp seed score.

### 2.3 The continuum defect has an ordered tail, not merely balanced mass

Let

\[
E(\theta)=\sum_{k\le1/\theta}g(k\theta)
-\theta^{-1/2}\log(1/\theta)
\]

be the continuum seed defect.  PR #254 had established macroscopic positive and
negative masses and a lower-order signed difference.  `L-26202` proves the
stronger statement

\[
\boxed{
\int_\theta^1E(u)du\le0
\qquad(0<\theta\le1).}
\]

On the reciprocal cell

\[
1/(N+1)\le\theta\le1/N,
\]

the cumulative defect is exactly

\[
\begin{aligned}
H_N(\theta)
={}&4N\theta-4\\
&+\sqrt\theta
[4-4S_N-2A_N-2(S_N+1)\log\theta].
\end{aligned}
\]

At `theta=1/N`,

\[
H(1/N)=2K_N/\sqrt N,
\]

and

\[
K_N-K_{N-1}
=(S_{N-1}+1)\log(N/(N-1))-2/\sqrt N<0.
\]

Thus every reciprocal endpoint is negative.  For `N>=15`, the cell is convex;
the exact gate is `K_16<-1/2`.  The first fourteen cells are increasing, with
an exact rational-interval lower bound for the derivative.

Consequently the positive defect measure is stochastically below the negative
slack measure.  There is a monotone coupling supported on

\[
0<u\le v\le1.
\]

The continuum incidence transport therefore has nonpositive logarithmic cost.
The finite problem is to retain that order through floors and arithmetic
endpoints.

## 3. New finite positive producer

`L-26203` runs backward minimum-ratio elimination on the endpoint atoms rather
than on the individual carry rows.

Initialize

\[
\rho(q)=q^{-1/2}\log(X/q).
\]

For `T=X,...,3`, set

\[
\lambda_T=\min_{q<T}\frac{\rho(q)}{\Gamma_T(q)}
\]

and subtract `lambda_T Gamma_T`.

The output

\[
d_X^{\rm sc}=\sum_T\lambda_Ta_T
\]

is unconditionally

\[
\boxed{d_X^{\rm sc}\ge0}
\]

and

\[
\boxed{B_X^Td_X^{\rm sc}\le w_X.}
\]

This is already a genuine nonnegative finite object at every endpoint.

## 4. Exact blocker ledger

Define

\[
\widehat\lambda_T
=\frac{\rho(T-1)}{\Gamma_T(T-1)},
\qquad
\ell_T=\widehat\lambda_T-\lambda_T.
\]

The final slack in column `T-1` is exactly

\[
\boxed{s_X^{\rm sc}(T-1)=\Gamma_T(T-1)\ell_T.}
\]

Therefore

\[
\boxed{
\Sigma_X^{\rm sc}
=\sum_{T=3}^X\Gamma_T(T-1)\ell_T.}
\]

If stage `T` is blocked by `q<T-1`, then every scale

\[
q<U<T
\]

receives weight zero.  One blocker therefore freezes one contiguous endpoint
interval.  This is much simpler than the residue-class freeze of the original
row greedy.

The diagonal atom is explicit:

\[
\Gamma_{q+1}(q)
=2\sqrt q
\left[
\log(1+1/q)-2(1-(1+1/q)^{-1/2})
\right],
\]

and satisfies

\[
\boxed{
\frac1{5q^{3/2}}
\le\Gamma_{q+1}(q)
\le\frac1{2q^{3/2}}.}
\]

This diagonal decay is the main quantitative gain.

## 5. New closing theorem

The proposal asks for the endpoint-scale blocker bound

\[
\boxed{
\ell_T\le C\sqrt T\log^A(2X).
}
\]

Because the diagonal charge is `O(T^(-3/2))`, this gives

\[
\Sigma_X^{\rm sc}=O(\log^{A+1}X).
\]

PR #244's universal mass--slack theorem then yields

\[
\sum_nd_X^{\rm sc}(n)G_n
\ge4\sqrt X-O(\log^{A+1}X).
\]

Legendre/Kummer and positivity of `Lambda` give the sharp prime-power ramp, and
the repository square-screw/Landau consumer gives RH.

This theorem is substantially weaker than bounded blocker weights:
`ell_T` may grow like `sqrt(T)` times any fixed polylogarithm.

## 6. Connection to the canonical Green correction

The signed Green solution remains valuable:

\[
T_*=G_X^{-1}r_X
\]

solves every constraint exactly and identifies the scalar mode.  But it is no
longer necessary to deform that vector directly into the positive row cone.
The endpoint atoms provide an alternative:

```text
signed Green equality coordinates
    -> exact but positivity unprotected;

positive endpoint scale coordinates
    -> positivity automatic, small slack permitted.
```

The two routes share the same residual.  The continuum tail theorem explains
how signed defect should be moved; the scale frame provides the positive finite
container in which to move it.

## 7. Connection to Greedy Slack and DCRS

The endpoint-scale output is a feasible nonnegative vector, so PR #244's exact
conservation law applies:

\[
M_X^{\rm sc}=8\sqrt X-2\Sigma_X^{\rm sc}+O(\log^2X).
\]

Thus `ESGS` proves the same sharp positive-minorant conclusion as Greedy Slack
or DCRS, without proving either existing producer succeeds.  The reusable
canonical statement should be:

> construct one explicit feasible nonnegative carry vector with total slack
> `X^o(1)`.

Row greedy, scale greedy, phase frame, and FGCM are alternative producers.

## 8. Exact verification

`X-26201` contains two assurance layers.

### Exact rational interval

It proves:

```text
K_16 upper endpoint  -0.528310671770645834 < -1/2;
H_N' > 7/25 on every complete cell N=2,...,14.
```

All logarithms use a rational `atanh` series with explicit remainder; square
roots use integer-square outward enclosures.

### High-precision reconnaissance

At `X=64,128,256`, the actual Decimal scale-greedy produced:

```text
X=64
  total slack                  approximately 0
  off-diagonal blockers        0

X=128
  total slack                  0.0100924917778986...
  prime-power weighted gap     0.0094922692097943...
  off-diagonal blockers        2
  max ell_T/sqrt(T)            0.0631996248240969...

X=256
  total slack                  0.0099898410323845...
  prime-power weighted gap     0.0083008159604794...
  off-diagonal blockers        2
  max ell_T/sqrt(T)            0.0656043314756684...
```

These figures are discovery and mutation evidence only.  They are not used to
claim `ESBT`.

Retained proof-object digest:

```text
3bb2311307155cb36a96017bf0b60d446dd0d54cf0622f3d7ffbd40196f51fe9
```

## 9. Proposed next proof step

The next proof should not estimate each endpoint atom independently.  It should:

1. emit maximal frozen scale intervals from the endpoint greedy;
2. group each interval by reciprocal quotient cells;
3. assign the exact continuum tail flux of `L-26202` to the interval;
4. prove a directed finite-floor comparison retaining incoming slack;
5. charge only interval boundaries and a polylogarithmic terminal scale;
6. conclude the square-root blocker estimate.

This is a finite transport theorem, not a generic prime asymptotic and not a
positive-part cover.

## 10. Exact status

```text
parabolic seed positive in row coordinates       PROPOSED COMPLETE
endpoint increments positive                     PROPOSED COMPLETE
continuum upper-tail majorization                 PROPOSED COMPLETE
endpoint-scale greedy finite packing              PROPOSED COMPLETE
exact scale blocker/slack identity                PROPOSED COMPLETE
q^(-3/2) diagonal charge                         PROPOSED COMPLETE
ESBT / ESGS                                       OPEN / RH-BEARING
ESBT -> nonnegative 4 sqrt(X) object              COMPLETE CONDITIONAL
sharp object -> prime ramp -> RH                  IMPORTED/PROPOSED COMPLETE
Riemann Hypothesis                                UNPROVEN
```
