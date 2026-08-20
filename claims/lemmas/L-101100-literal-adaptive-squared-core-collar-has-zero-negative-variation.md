# L-101100 — The literal adaptive squared-core collar has zero one-sided negative variation

Claim ID: `L-101100`  
Status: **PROVED EXACTLY ON THE FROZEN COMPLETED SOURCE**  
Created: 2026-08-21  
Frozen inputs: PR #684 at `bbf4e2f8633700e4c8cd6cc11874eae3dacccaa8`  
RH status: **not assumed**

Fix a physical endpoint `X` and put

\[
Z=X^{9/10}.
\]

Apply the finite Euler completion only to source labels `q<=Z`. On the final
critical centered-Bernstein source this replaces each small-prime pair by

\[
\boxed{
(I-q^{-1/2}S_q)(I+q^{-1/2}S_q)
=I-q^{-1}S_{q^2}.
}
\tag{L-101100.1}
\]

Thus the small-prime core is one literal squared source. Every unsquared label
satisfies `p>Z`.

## Depth one

If `p,q>Z`, then

\[
pq>Z^2=X^{9/5}>X.
\]

Consequently no active source integer `n<=X` contains two unsquared
large-prime labels. The complete unsquared collar is exactly one parent minus
a depth-one sum of children.

Let `P_Z(X)>=0` denote the completed small-prime parent packet and let
`C_(Z,p)(X)>=0` be the child with the unique unsquared owner `p`. The critical
one-label Harnack estimate of the frozen completion gives

\[
C_{Z,p}(X)\le {1\over p}P_Z(X).
\]

Therefore

\[
\begin{aligned}
\mathcal C_Z(X)
&:=P_Z(X)-\sum_{Z<p\le X}C_{Z,p}(X)\\
&\ge
\left(1-\sum_{Z<p\le X}{1\over p}\right)P_Z(X).
\end{aligned}
\tag{L-101100.2}
\]

For `Z=X^(9/10)`, the elementary prime-reciprocal estimate used in
`L-100180--L-100182` gives

\[
\sum_{Z<p\le X}{1\over p}<1
\]

throughout the stated large-`X` range; the finite base is separately covered
by the frozen finite-completion theorem. Hence

\[
\boxed{\mathcal C_Z(X)\ge0.}
\tag{L-101100.3}
\]

It follows immediately that

\[
\boxed{
\int_2^Y(\mathcal C_{X^{9/10}}(X))_-{dX\over X}=0.
}
\tag{L-101100.4}
\]

This proves the literal one-sided-variation statement for the completed
squared-core collar in its strongest possible form.

## Scope

The observable in (L-101100.4) depends on `X` through its completion cutoff.
It is not the fixed activation-free critical scalar consumed by Mellin--Landau.
No desmoothing conclusion is included in this lemma.
