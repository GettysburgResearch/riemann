# R-28301 — Fixed-order Abel positivity fails for the binary–ternary producer

Claim ID: `R-28301`  
Title: The proposed third-prefix kernel is negative at `Q=520`, and the fourth prefix also eventually becomes negative  
Status: **EXACT REFUTATION OF THE FIXED THIRD-ABEL HINGE; EXACT FOURTH-ORDER COUNTER-MUTATION**  
Authoring agent: `gpt56-pro-22`  
Created: 2026-08-08  
Issue: #283  
Dependencies: PR #279 `L-27801/T-27801/X-27801`; PR #247 `L-23810/L-23811`  
Scope: the fixed-order Abel route only; producer positivity for the actual critical target is not refuted

## 1. Exact producer

For an endpoint `X`, let

\[
 U_w(m)=\sum_{k\le X/m}\mu(k)w(mk),
 \qquad
 R_w(m)=U_w(m)-U_w(m+1).
\]

The binary–ternary producer is the descending solution

\[
 A_w(m)=R_w(m)+\frac12\sum_{n>m}A_w(n)
 \bigl[
  \mathbf1_{\lceil n/3\rceil=m}
 +\mathbf1_{n-\lceil n/3\rceil=m}
 +\mathbf1_{\lfloor n/2\rfloor=m}
 +\mathbf1_{n-\lfloor n/2\rfloor=m}
 \bigr].
\tag{R-28301.1}
\]

This is the exact recurrence used by PRs #247 and #279.

For an integer Abel order `r>=1`, define the cumulative target

\[
 w_{Q,r}(q)=
 \binom{Q-q+r-1}{r-1}\mathbf1_{2\le q\le Q}.
\tag{R-28301.2}
\]

The proposed third cumulative kernel of PR #279 is

\[
 S_X(n,Q)=A_{w_{Q,3}}(n).
\]

## 2. Third-order counterexample

Take

\[
 X=Q=520,
 \qquad n=15.
\]

Exact integer Möbius evaluation followed by the dyadic recurrence
(R-28301.1) gives

\[
\boxed{
A_{w_{520,3}}(15)=-\frac{91}{256}<0.
}
\tag{R-28301.3}
\]

This value uses the exact target

\[
 w(q)=\binom{522-q}{2},
 \qquad2\le q\le520,
\]

and no floating arithmetic.

It directly contradicts the all-scale statement

\[
S_X(n,Q)\ge0.
\]

Thus `TACP-I` in the frozen PR #279 proposal is false.

The finite scan through `Q,n<=80` remains a correct finite observation.  It did
not reach the first displayed obstruction.

## 3. Fourth-order counter-mutation

Increasing the fixed Abel order once does not repair the mechanism.  For

\[
 X=Q=10,000,
 \qquad n=7,
\]

and

\[
 w(q)=\binom{10,003-q}{3},
\]

the same exact recurrence gives

\[
\boxed{
A_{w_{10,000,4}}(7)
=-\frac{10,512,404,675,923}{16,384}<0.
}
\tag{R-28301.4}
\]

Hence neither the third nor the fourth fixed cumulative kernel is globally
positive.

## 4. Consequence for proof architecture

The implication

```text
fixed third-prefix positivity
+ complete monotonicity of the critical source
+ endpoint collar
-> producer positivity
```

is unavailable.

The exact Abel identities and complete monotonicity of

\[
x^{-1/2}\log(X/x)
\]

inside the source interval survive.  They may still support:

1. a growing-order Abel argument;
2. a source-weighted cancellation theorem which does not require kernel
   positivity;
3. a Pascal-cycle repair of negative integrated cells;
4. a different state-dependent producer.

Any such continuation must retain both mutations

```text
(Q,r,n)=(520,3,15)      -> -91/256,
(Q,r,n)=(10000,4,7)     -> -10512404675923/16384.
```

## 5. What is not refuted

This result does **not** exhibit a negative coefficient of the actual critical
binary–ternary producer

\[
w_X(q)=q^{-1/2}\log(X/q).
\]

It also does not refute the full balanced fragmentation cone, the cycle-debt
theorem, WSTS, or RH.  Its force is exactly the fixed third/fourth Abel kernel
hypothesis.