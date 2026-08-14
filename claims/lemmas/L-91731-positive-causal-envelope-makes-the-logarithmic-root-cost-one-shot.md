# L-91731 — The positive causal envelope makes the logarithmic root cost one-shot

Claim ID: `L-91731`  
Status: **PROVED CONDITIONAL COMPOSITION FROM EXACT POSITIVE-PACKET INPUTS**  
Created: 2026-08-15  
Inputs: `L-91375`, `L-91650`, `L-91654`, `L-91658`, `L-91726`, `T-91312`; factor-67 endpoint density bound of PR #479  
RH status: **unproved**

## 1. Positive descendants need no new root realization

After the factor-67 Hall entry, every recursive object is already a positive
typed packet.  For such a packet the exact causal identity, complete causal
positivity, same-index placement and target monotonicity give the Hereditary
Typed Reset directly:

\[
 \Delta(P^{\rm cur})\le2m(P),
 \qquad
 \sum_i\alpha_i m(U_{p_i}P_i)<\frac18m(P).
 \tag{L-91731.1}
\]

Thus the normalized positive-packet envelope of `T-91312` is uniformly bounded:

\[
 \boxed{
 \Delta(P)\le C_+m(P)
 }
 \tag{L-91731.2}
\]

for one absolute `C_+` including the finite positive base range.  No finite
root Hall, continuum approximation, collar or port is repeated on descendants.

## 2. Uniform mass of the factor-67 root residual

On one root fiber `1<=x<67`, the positive target residual is at most the total
unsigned positive target mass.  Since

\[
 T_x(k)\le\frac{4\sqrt{67}}k,
\]

and the exact rational inequality `H_66<5` holds,

\[
 M_{\rm fiber}<4\frac{33}{4}\cdot5=165.
 \tag{L-91731.3}
\]

PR #479 gives the positive endpoint measure

\[
 d\nu(x)=2L(x)\frac{dx}{x},
 \qquad 0<L(x)<2.
\]

Moreover `log 67<5`; for example `e>8/3` and `(8/3)^5>67`.  Hence

\[
 \nu([1,67])<4\log67<20.
 \tag{L-91731.4}
\]

Therefore the complete integrated positive root residual has target mass

\[
 \boxed{M_{\rm root}<3300.}
 \tag{L-91731.5}
\]

Positive omissions and common thinning only reduce this mass.

## 3. Descendant contribution is an absolute constant

By `L-91726`, the actual weighted child target satisfies

\[
 \sum_i\alpha_i m(P_i)<\frac18M_{\rm root}.
\]

Using (L-91731.2),

\[
 \boxed{
 \sum_i\alpha_i\Delta(P_i)
 \le C_+\sum_i\alpha_i m(P_i)
 <\frac{825}{2}C_+.
 }
 \tag{L-91731.6}
\]

This includes all grandchildren through the already-closed positive causal
envelope.

## 4. Native root consequence

Let `delta_X=<Y_4,r_X>` be the one-shot native root realization cost.  The exact
packet cocycle gives

\[
 \Delta_X=\delta_X+\sum_i\alpha_i\Delta(P_i).
\]

If `L-91728` supplies

\[
 \delta_X\le A_0+4290\log(2X),
\]

then

\[
 \boxed{
 J_\Lambda(X)-\mathcal H(d_X)
 \le A_0+\frac{825}{2}C_++4290\log(2X)
 =O(\log X).
 }
 \tag{L-91731.7}
\]

Thus the finite root realization is charged exactly once.  The proof does not
assume that arbitrary positive descendants have the native root form.

```text
positive-packet causal envelope             T-91312 ON EXACT POSITIVE INPUTS
factor-67 root target mass <3300             EXACT / FROZEN DENSITY
all recursive child deficit                  O(1)
root native realization                      ONE SHOT
native root deficit                          O(log X)
Riemann Hypothesis                           UNPROVED
```
