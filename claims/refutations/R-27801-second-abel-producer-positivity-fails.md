# R-27801 — Second-Abel producer positivity fails exactly

Claim ID: `R-27801`  
Title: Generic producer positivity and the second cumulative Abel kernel are false, while the third cumulative kernel survives finite exact stress tests  
Status: **EXACT REFUTATION OF TWO STRONGER SURROGATES**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-08  
Parent: PR #277 at `d5be8262c80a1debcf86922b45a4d00a406803f1`  
Scope: source-specific continuation of the binary–ternary producer programme

## 1. Linear producer operator

Fix an endpoint `X`. For a target column vector `w(2),...,w(X)`, define

\[
U(m)=\sum_{k\le X/m}\mu(k)w(mk),\qquad
r(m)=U(m)-U(m+1),
\]

and let `A_w(n)` be the descending binary–ternary producer of `L-23811`:

\[
A_w(n)=r(n)+\frac12\sum_{m>n}A_w(m)
\bigl[1_{a_3(m)=n}+1_{b_3(m)=n}+1_{a_2(m)=n}+1_{b_2(m)=n}\bigr].
\]

The map `w -> A_w` is linear. Write

\[
A_w(n)=\sum_{q=2}^X K_X(n,q)w(q).
\tag{R-27801.1}
\]

The actual critical target is

\[
w_X(q)=q^{-1/2}\log(X/q),
\]

but a generic positivity theorem for `K_X` would be much stronger.

## 2. Generic positive-target preservation is false

At `X=8`, take the nonnegative basis target

\[
w(4)=1,\qquad w(q)=0\;(q\ne4).
\]

Exact rational evaluation of the recurrence gives

\[
\boxed{A_w(3)=-1.}
\tag{R-27801.2}
\]

Equivalently,

\[
K_8(3,4)=-1.
\]

Thus the binary–ternary inverse is not an entrywise nonnegative matrix. Any proof of producer positivity must use the special shape of `w_X`; an ambient positive-operator argument is impossible.

## 3. The natural second-Abel shortcut also fails

A tempting source-specific repair is to ask whether two cumulative sums of the kernel become positive. For `Q<=X`, define the discrete ramp target

\[
w_Q^{(2)}(q)=(Q-q+1)_+.
\tag{R-27801.3}
\]

Its producer is the second prefix of `K_X`:

\[
A_{w_Q^{(2)}}(n)
 =\sum_{q=2}^{Q}(Q-q+1)K_X(n,q).
\tag{R-27801.4}
\]

At the exact finite endpoint

\[
X=60,\qquad Q=59,\qquad n=11,
\]

Fraction arithmetic gives

\[
\boxed{
A_{w_{59}^{(2)}}(11)=-\frac{13}{16}<0.
}
\tag{R-27801.5}
\]

Therefore the statement

```text
all second cumulative producer kernels are nonnegative
```

is false.

This witness is important because the critical target `w_X(q)` is decreasing and convex. Convexity alone cannot prove producer positivity by a twofold Abel transform.

## 4. Why this does not refute the live producer theorem

Neither witness has the critical source shape

\[
q^{-1/2}\log(X/q).
\]

They refute only stronger surrogate statements:

```text
nonnegative target -> nonnegative producer          FALSE
convex decreasing target -> positivity by 2-Abel   FALSE
actual critical producer positivity                OPEN
```

This is exactly the distinction exposed by the verdict-scope audit: the correct continuation must exploit a source property stronger than convexity without replacing the arithmetic target by an arbitrary cone.

## 5. Surviving third-order phenomenon

Define the third cumulative target

\[
w_Q^{(3)}(q)=\binom{Q-q+2}{2}\,1_{q\le Q}.
\tag{R-27801.6}
\]

The exact checker `X-27801` verifies

\[
A_{w_Q^{(3)}}(n)\ge0
\]

for every

\[
2\le Q\le80,\qquad2\le n\le80,
\]

covering 6,241 exact rational rows. This is reconnaissance, not a theorem. It motivates `L-27801/T-27801`, where the third cumulative kernel is coupled to complete monotonicity of the actual target and an explicit endpoint collar.

## 6. Mandatory mutation

Every proposed proof of the third-Abel route must reproduce both exact failures:

```text
K_8(3,4)                         = -1
second prefix at X=60,Q=59,n=11 = -13/16
```

A proof that also implies either quantity is nonnegative has silently reintroduced a false generic positivity theorem.
