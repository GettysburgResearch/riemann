# L-26214 — Every digital-prefix observation is one finite current feature plus a strict-delay source tail

Claim ID: `L-26214`  
Title: The RH-sensitive annular bank observations map exactly to the three-scale generalized-prime feature and a source-complete multiplicative tail  
Status: **PROPOSED COMPLETE EXACT SOURCE LEMMA PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-08  
Depends on: `L-26210`, `L-26211`, `L-26213`; PR #268 `L-26802`; PR #269 `L-26903`  
Scope: exact source decomposition and strict multiplicative delay; no norm estimate or RH conclusion

## 1. Digital prefix and tail

Put

\[
c_2(n)=1-v_2(n)
\]

and

\[
\omega_2(n)
=\mu(n)-\frac32\mathbf1_{2\mid n}\mu(n/2)
+rac12\mathbf1_{4\mid n}\mu(n/4).
\]

Their complete convolution is

\[
\boxed{
 c_2*\omega_2
 =h_2
 :=\varepsilon-\frac52\delta_2+\delta_4.
}
\tag{L-26214.1}

For `Y>1`, split

\[
c_2=c_{<Y}+c_{\ge Y},
\]

where the two terms are the strict prefix and its complementary tail.

Then

\[
\boxed{
\omega_2*c_{<Y}
=h_2-\omega_2*c_{\ge Y}.
}
\tag{L-26214.2}

This is an exact Dirichlet-convolution identity.

## 2. RH-sensitive annular coefficient

Let

\[
x_M(n)=\Lambda_\omega(n)\mathbf1_{M\le n<2M},
\]

where `Lambda_omega` is the nonnegative generalized-prime sequence of PR #269.

The physical strict-prefix observation is

\[
Q_{c_{<Y}*x_M}
=\mathcal A_YQ_{x_M}
\]

by `L-26213`.

Its exact carry source is

\[
\omega_2*(c_{<Y}*x_M).
\]

Associativity and (L-26214.2) give

\[
\boxed{
\omega_2*(c_{<Y}*x_M)
=h_2*x_M-\mathcal T_{Y,M},
}
\tag{L-26214.3}

where

\[
\boxed{
\mathcal T_{Y,M}
=(\omega_2*c_{\ge Y})*x_M.
}
\tag{L-26214.4}

## 3. The current feature is finite and explicit

The first term in (L-26214.3) is

\[
\boxed{
 h_2*x_M
 =x_M-\frac52\,\delta_2*x_M+\delta_4*x_M.
}
\tag{L-26214.5}

After the carry split on a row `N`, it becomes the exact three-scale generalized-prime feature

\[
\boxed{
 P_{N,M}
 -\frac52 P_{N,2M}
 +P_{N,4M},
}
\tag{L-26214.6}

with the natural annular restrictions and all source collisions combined before the split.

Thus the same-scale part of every strict-prefix observation belongs to one fixed finite source family. No infinite prefix dictionary remains at current scale.

## 4. Every tail monomial carries a strict multiplicative delay

A monomial in `T_(Y,M)` has the form

\[
\omega_2(d)c_2(n)\Lambda_\omega(m)
\]

with

\[
n\ge Y,
\qquad M\le m<2M.
\]

Its arithmetic index is

\[
q=dnm\ge YM.
\]

Therefore every tail contribution is delayed by at least

\[
\boxed{\log Y}
\tag{L-26214.7}

relative to the base annular source scale `M`.

This support statement is coefficientwise and survives all signs. It does not use total variation.

## 5. Hyperbola aggregation

For the critical choice in `L-26211`, all current prefixes have length at least `N`. Summing (L-26214.3) with the exact opposite-parity synthesis coefficients yields:

```text
current finite three-scale generalized-prime ledger
+
complete signed source tail with delay at least log N.
```

The inclusion--exclusion term of `L-26211` combines repeated product destinations before any norm. Hence the tail must be estimated in that recombined hyperbola form, not as the sum of the absolute values of (L-26214.4).

## 6. Consequence for the live proposal

Together, `L-26213` and this lemma close the formerly open source-map questions:

1. every bank observation has one common weighted carry metric;
2. every observation has an exact current generalized-prime feature;
3. every remaining source monomial is strictly delayed;
4. the RH-sensitive coefficient is never replaced by the pole-blind positive-inverse physical source.

The remaining theorem is quantitative:

\[
\boxed{
\text{bound the recombined strict-delay tail and boundary commutator
against the current three-scale carry reserve.}
}
\]

## 7. Proof boundary

Closed exactly, subject to review:

- prefix/tail convolution decomposition;
- the finite current feature;
- strict multiplicative delay of every tail monomial;
- compatibility with the common weighted annular embedding;
- preservation of all source signs and collisions.

Open:

- a norm bound for the recombined tail;
- the annular banked recurrence;
- RH.
