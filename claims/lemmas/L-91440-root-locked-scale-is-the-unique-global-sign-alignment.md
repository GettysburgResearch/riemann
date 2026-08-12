# L-91440 — The root-locked scale is the unique global sign alignment of the Cauchy residual and completed continuous source

Claim ID: `L-91440`  
Status: **PROVED EXACT UNIQUENESS / MISMATCH-INTERVAL THEOREM**  
Created: 2026-08-12  
Depends on: `L-91423`  
RH status: **unproved**

## 1. The two sign boundaries

Retain the residual profile `R` and Nakamura continuous sign factor `B` of
`L-91423`. There are unique constants

\[
 \tau_*>0,
 \qquad
 \kappa=\log\varpi>0
\]

such that

\[
 R(x)>0\ (0<x<\tau_*),
 \qquad
 R(x)<0\ (x>\tau_*),
\tag{L-91440.1}
\]

and

\[
 B(u)>0\ (0<u<\kappa),
 \qquad
 B(u)<0\ (u>\kappa).
\tag{L-91440.2}
\]

For a safe scale `a>0`, the residual factor `R(au)` changes sign at

\[
 \frac{\tau_*}{a}.
\tag{L-91440.3}
\]

## 2. Exact uniqueness

Define

\[
 a_*:=\frac{\tau_*}{\kappa}.
\]

Then

\[
\boxed{
 R(au)B(u)\ge0\quad\text{for every }u>0
 \iff a=a_*.
}
\tag{L-91440.4}
\]

### Proof

At `a=a_*`, the two sign boundaries coincide, which is `L-91423.14`.

If `0<a<a_*`, then

\[
 \kappa<\frac{\tau_*}{a}.
\]

On the nonempty interval

\[
 \boxed{
 \kappa<u<\frac{\tau_*}{a},
 }
\tag{L-91440.5}
\]

one has `B(u)<0` but `R(au)>0`, so their product is negative.

If `a>a_*`, then

\[
 \frac{\tau_*}{a}<\kappa.
\]

On the nonempty interval

\[
 \boxed{
 \frac{\tau_*}{a}<u<\kappa,
 }
\tag{L-91440.6}
\]

one has `R(au)<0` but `B(u)>0`, again giving a negative product. ∎

Thus the root lock is not merely one convenient alignment. It is the unique
scale at which the entire continuous Jordan source collapses to one sign
pointwise.

## 3. Prime-atom sign threshold

The prime coefficient is

\[
 c_a(\log n)=-2a^{-3}R(a\log n).
\]

Since every prime power satisfies `n>=2`, all prime coefficients are
nonnegative exactly when the first atom is beyond the residual zero:

\[
\boxed{
 c_a(\log n)\ge0\quad\text{for every }n=p^k\ge2
 \iff
 a\ge a_{\rm p}:=\frac{\tau_*}{\log2}.
}
\tag{L-91440.7}
\]

They are all strictly positive for `a>a_p`; at equality only the atom `n=2`
has zero coefficient.

Numerically,

\[
 a_{\rm p}=1.6801727130056628\ldots,
 \qquad
 a_*=4.1415673607530469\ldots.
\]

## 4. Exact comparison with the first dyadic scales

The inequalities

\[
 \boxed{
 \frac{a_*}{2}>a_{\rm p},
 \qquad
 \frac{a_*}{4}<a_{\rm p}
 }
\tag{L-91440.8}
\]

are equivalent to

\[
 \log2>2\kappa,
 \qquad
 \log2<4\kappa.
\]

They admit elementary algebraic proofs. Since the plastic constant is the
unique root `varpi>1` of `y^3-y-1`, the polynomial is increasing for `y>=1` and

\[
 \varpi<\sqrt2
\]

because `(sqrt2)^3-sqrt2-1=sqrt2-1>0`. Hence
`2>varpi^2`, which gives `log2>2 log varpi`.

Also `varpi>5/4`, since

\[
 (5/4)^3-(5/4)-1=-19/64<0.
\]

Therefore

\[
 \varpi^4=\varpi^2+\varpi
 >25/16+20/16>2,
\]

which gives `4 log varpi>log2`.

## 5. Consequence

The root-locked source is the unique pointwise two-channel collapse. Any
continuation in the radial scale must use a genuinely nonlocal operator or
source cocycle; pointwise preservation of the Jordan signs is impossible away
from `a_*`.

```text
unique continuous sign alignment                    EXACT
mismatch interval for every a != a_*                 EXPLICIT
all-prime positive coefficient threshold             EXACT
first dyadic half retains prime sign                  EXACT
second dyadic half loses the n=2 prime sign           EXACT
root-lock pointwise propagation                       IMPOSSIBLE
nonlocal/operator scale cocycle                       OPEN
Riemann Hypothesis                                    UNPROVEN
```
