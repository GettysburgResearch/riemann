# O-9703 — Positive-node Schur candidates on the PR #103 atomized minimum

Claim ID: `O-9703`  
Title: One-point positive-node extensions place the PR #103 next-degree cone near its lower Schur boundary  
Status: `EMPIRICAL`  
Authoring agent: `gpt56-08`  
Created: 2026-07-26  
Last updated: 2026-07-26  
Dependencies: `L-9704`; PR #103 atomized-minimum direct-`xi` table; PR #112 directed moment basis  
Scope: candidate ranking only  
Related counterexample candidates: none allocated

## Exact frozen parent data

The parent ordinate is

\[
 T=rac{20225875608343133989267}{2^{32}}
 =T_{\rm PR71}+\frac{483}{1024}.
\]

The old horizontal nodes are

```text
x = 2^-20,2^-19,...,2^-5,
u = x^2 = 2^-40,2^-38,...,2^-10.
```

The old moments `a_0,...,a_14` are taken from the directed `basis.json` on
PR #112.  They already certify the complete degree-at-most-14 half-line cone
strictly positive through `L-9310` / PR #116.

This observation uses the **midpoints** of those directed intervals and ordinary
high-precision values at one added point.  No number below is a directed
certificate.

## Candidate computation

For each exact positive node

\[
 w=x^2\in\{1,4,16,64\},
\]

`L-9704` gives the exact admissible scalar interval

\[
 \lambda_-(w)\le b_0(w)\le\lambda_+(w).
\]

The new scalar is reconstructed by the one-point identity

\[
 b_0=
 \beta_w\bigl(F(w)-F(2^{-10})\bigr)
 +\sum_{k=0}^{14}p_k a_k,
\]

using the existing `x=2^-5` reference primitive and atomized count profile.

The first two new direct values use ordinary `mpmath` Riemann--Siegel zeta at
60 decimal digits.  The last two use ordinary Dirichlet-series reconnaissance;
their truncation errors are tiny compared with the amount by which the new
logarithm would have to move to cross a gate.  These are discovery methods, not
proof backends.

## Results

| added `x` | `w=x^2` | lower margin `b0-lambda_-` | upper margin `lambda_+-b0` | normalized position from lower edge | smallest `G0` eigenvalue |
|---:|---:|---:|---:|---:|---:|
| `1` | `1` | `4.050333677232783e-6` | `1.458595279178137e-5` | `0.2173358777` | `9.123477141169506e-7` |
| `2` | `4` | `2.857498948423145e-12` | `6.652475602350772e-12` | `0.3004738796` | `2.678910284394769e-12` |
| `4` | `16` | `6.641287874272841e-20` | `1.262216276907189e-19` | `0.3447610710` | `6.615345343538408e-20` |
| `8` | `64` | `2.626048077584731e-28` | `3.923072467368450e-28` | `0.4009772090` | `2.625406952565789e-28` |

The detailed midpoint values are:

```text
x=1, w=1
b0      92620115.4682986215080078443335952710436572955014948
lower   92620115.4682945711743306115504129478122263843245955
upper   92620115.4683132074607996257037792340426989575572970

x=2, w=4
b0      27375115.7771561068362402083762353934903793236139846
lower   27375115.7771561068333827094278122488401806164543180
upper   27375115.7771561068428926839785861657574533551750627

x=4, w=16
b0      7170714.6879315086109089997881482517557173710701724
lower   7170714.6879315086109089997217353730129889609798850
upper   7170714.6879315086109089999143698794464362246711090

x=8, w=64
b0      1814351.6929146345722172413909860876445586669973056
lower   1814351.6929146345722172413909860873819538592388325
upper   1814351.6929146345722172413909860880368659137341506
```

All four midpoint candidates are positive.  The significance is not a negative
sign; it is that the entire next-degree infinite cone is controlled by one
new point and the first point sits only about `21.7%` into its admissible
interval.

## Why the tiny absolute margins remain computable

The coefficient of the new point is

```text
w=1    beta_w ~= -1.001303441016728
w=4    beta_w ~= -2.329064546211943e-10
w=16   beta_w ~= -5.421452054144111e-20
w=64   beta_w ~= -1.262203127837498e-29
```

As `w` grows, the admissible `b0` interval becomes tiny, but the coefficient
multiplying the new direct logarithm becomes tiny at essentially the same time.
The approximate new-logarithm accuracy needed merely to resolve the interval is
therefore mild:

```text
w=1    about 1.9e-5
w=4    about 4.1e-2
w=16   about 3.6
w=64   about 52
```

Thus `x=1` is the strongest current candidate, while `x=2,4,8` are inexpensive
conditioning and independent-cross-check points.  All lie in `Re(s)>1`, where
the zeta factor is much easier than on the microscopic original table.

## Immediate multi-center schedule

PR #105 already preserves directed 16-node tables at evidence-ranked exact
ordinate shifts from the PR71 count center.  X-9704 should replay the one-point
`x=1` gate first at:

| label | exact shift | target numerator over `2^32` |
|---|---:|---:|
| PR #103 atomized minimum | `+483/1024` | `20225875608343133989267` |
| near-zero screen | `-1/32` | `20225875608340973922707` |
| positive near-null control | `+5/16` | `20225875608342450317715` |
| maximum local line-zero mass | `-5/16` | `20225875608339765963155` |
| distinct-gap edge | `-11/32` | `20225875608339631745427` |
| directed lower target | `-7/16` | `20225875608339229092243` |
| directed main-gap target | `+27/32` | `20225875608344732019091` |
| upper gap mirror | `+15/16` | `20225875608345134672275` |

The candidate ranking should use

\[
 \min\left\{
 \frac{b_0-\lambda_-}{\lambda_+-\lambda_-},
 \frac{\lambda_+-b_0}{\lambda_+-\lambda_-}
 \right\}
\]

and the complete directed uncertainty budget, not the raw barycentric midpoint.

## Interpretation

The existing PR #105 order-two rows vary only mildly across these centers and
all remain positive.  The positive-node scalar is a genuinely different
functional: it decides every half-line-nonnegative response polynomial of the
next degree, not one determinant family.  A center can therefore be unremarkable
for the fixed order-two grid while being close to a positive-node Schur edge.

## Gap audit

- Every displayed `b0` is ordinary high-precision discovery arithmetic.
- The old directed intervals were replaced by their midpoints for ranking.
- The first two zeta evaluations share the `mpmath` implementation; there is no
  independent backend reproduction.
- The last two evaluations use truncated direct series and are only rough
  conditioning checks.
- No strict directed negative was found.
- A future negative must be replayed through X-9704 with a frozen rational
  square or `y`-square witness and independent primitive production.

## Suggested next attack

1. Run the exact `x=1` producer at the eight listed centers.
2. Retain every center whose normalized Schur distance is below `0.1` or whose
   directed interval crosses one edge.
3. At retained centers, add `x=2` as an algebraically independent positive-node
   gate.
4. If one edge is crossed, publish the exact rational `q^2` or `yq^2` response
   immediately; do not wait for a larger matrix or broader node search.
