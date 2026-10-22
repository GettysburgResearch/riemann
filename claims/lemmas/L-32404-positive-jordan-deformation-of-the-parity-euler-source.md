# L-32404 — Positive Jordan deformation of the parity Euler source

Claim ID: `L-32404`  
Title: The complete multiplicative deformation `A(s-t)/A(s)` of the Euler-filtered inverse-zeta source has nonnegative coefficients for every `t>=0`, and the parity sum retains only even two-adic fibers  
Status: **PROPOSED COMPLETE EXACT DIRICHLET-ALGEBRA LEMMA**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-08  
Dependencies: PR #263 `L-26202/L-26205`  
Scope: source-complete coefficient deformation; no physical block estimate or RH conclusion

## 1. Source and inverse

Let

\[
A_{\mathcal E}(s)
=\frac{\zeta(s)}{(1-2^{1-s})(1-2^{1/2-s})^2}
=\sum_{n\ge1}\frac{a_{\mathcal E}(n)}{n^s}
\]

be the positive inverse from PR #263 and let `b_E` be its Dirichlet inverse.
For real `t>=0` define

\[
\boxed{
\mathcal J_t(s)
:=\frac{A_{\mathcal E}(s-t)}{A_{\mathcal E}(s)}
=\sum_{n\ge1}\frac{J_t(n)}{n^s}.
}
\tag{L-32404.1}
\]

Equivalently,

\[
\boxed{J_t=b_{\mathcal E}*(a_{\mathcal E}n^t).}
\tag{L-32404.2}
\]

At `t=0`, `J_0=epsilon`.

## 2. Odd-prime local coefficients are positive

For an odd prime `p`, put `z=p^{-s}` and `a=p^t>=1`. The local factor of (L-32404.1) is

\[
\frac{1-z}{1-az}
=1+\frac{(a-1)z}{1-az}.
\]

Hence

\[
\boxed{
J_t(p^k)=(p^t-1)p^{t(k-1)}\ge0
\qquad(k\ge1).
}
\tag{L-32404.3}
\]

## 3. The prime-two factor is also coefficientwise positive

The local factor of `A_E` at two is

\[
\frac1{(1-z)(1-2z)(1-\sqrt2 z)^2}.
\]

For each local species `c in {1,2,sqrt(2),sqrt(2)}`, its contribution to the ratio is

\[
\frac{1-cz}{1-c2^t z}
=1+\frac{(2^t-1)cz}{1-c2^tz}.
\tag{L-32404.4}
\]

Every coefficient is nonnegative for `t>=0`. The product of the four series therefore has nonnegative coefficients. Thus

\[
\boxed{J_t(2^k)\ge0\qquad(k\ge0).}
\tag{L-32404.5}
\]

Multiplicativity now gives

\[
\boxed{J_t(n)\ge0\qquad(n\ge1,t\ge0).}
\tag{L-32404.6}
\]

For `t>0`, every coefficient permitted by the Euler factors is strictly positive.

## 4. Complete derivative tower

Because (L-32404.2) is finite coefficientwise at each `n`, differentiation at `t=0` gives

\[
\boxed{
\partial_t^rJ_t\big|_{t=0}
=b_{\mathcal E}*(a_{\mathcal E}\log^r)
\qquad(r\ge0).
}
\tag{L-32404.7}

In particular

\[
\partial_tJ_t|_0=\Lambda_{\mathcal E}^{\#},
\]

and

\[
\partial_t^2J_t|_0
=\Lambda_{\mathcal E}^{\#}\log
 +\Lambda_{\mathcal E}^{\#}*\Lambda_{\mathcal E}^{\#}.
\tag{L-32404.8}

Thus the positive generalized-prime and Selberg channels of PR #263 are the first two derivatives of one coefficientwise-positive multiplicative deformation, not unrelated identities.

More strongly, every derivative coefficient at every `t>=0` is nonnegative. For an odd prime-power local coefficient,

\[
J_t(p^k)=e^{(k-1)(\log p)t}(e^{(\log p)t}-1),
\]

whose derivatives are nonnegative. The same representation applies to each factor in (L-32404.4), and products preserve absolute monotonicity. Therefore

\[
\boxed{\partial_t^rJ_t(n)\ge0
\qquad(t\ge0,r\ge0,n\ge1).}
\tag{L-32404.9}

## 5. Parity-paired deformation

Let `chi_2(n)=(-1)^{v_2(n)}` and let the second Euler channel be the complete multiplicative twist. Its Jordan coefficients are

\[
J_t^-(n)=\chi_2(n)J_t(n).
\tag{L-32404.10}

Hence the paired coefficient sequence is

\[
\boxed{
J_t^+(n)+J_t^-(n)
=(1+\chi_2(n))J_t(n)
\ge0.
}
\tag{L-32404.11}

It vanishes exactly on odd two-adic valuation and equals `2J_t(n)` on even valuation. The same statement holds after every `t` derivative.

For every carry row `chi_(N,q)(j)>=0`, define

\[
H_t^{\rm pair}(N,j)
=\sum_{q\le N}[J_t^+(q)+J_t^-(q)]\chi_{N,q}(j).
\]

Then

\[
\boxed{H_t^{\rm pair}(N,j)\ge0
\quad(t\ge0),}
\tag{L-32404.12}

and every derivative in `t` is nonnegative.

## 6. Significance and limit

This gives a source-complete positive deformation joining the identity source to the full generalized-prime/Selberg moment tower while preserving the exact parity orthogonalization. It is stronger than checking only the first two coefficient identities.

It does **not** imply a Kummer-square inequality. The exact generalized-prime counterexample of `R-29002` shows that positivity of the deformation and of all its derivatives is insufficient to conclude

```text
(first derivative)^2 >= second derivative.
```

Any completion must use additional coupled source geometry—e.g. the two-frequency reflected normal matrix, the parity perfect-reconstruction frame, or an exact convexity/Schur identity for the full paired deformation.

## 7. Proof boundary

Closed exactly:

- coefficientwise positivity of the complete Jordan deformation;
- absolute monotonicity in the deformation parameter;
- exact recovery of every logarithmic moment;
- parity-paired even-valuation positivity.

Open:

- a source-coupled reflected inequality strong enough to close the physical block;
- the final lower-scale recurrence;
- RH.