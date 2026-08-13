# L-91104 — Finite-rank endpoint principle and generalized Chebyshev packets

Claim ID: `L-91104` (provisional research range)  
Title: Whenever consecutive endpoint increments lie in a finite-dimensional scale-mode space, every deep endpoint matrix has finite rank; moment-neutral packets on \(d+1\) adjacent endpoints cancel the complete inherited bulk and become compact generalized B-splines  
Status: **PROPOSED COMPLETE ABSTRACT FINITE-RANK THEOREM — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Date: 2026-08-11  
Depends on: elementary linear algebra and finite differences; `L-91101` is the parabolic \(d=2\) instance  
Scope: abstract endpoint/filter architecture; no arithmetic feasibility or RH conclusion

## 1. Abstract endpoint family

Let \(b_T(m)\) be a nested finite-support family:
\[
 b_T(m)=0\qquad(m>T).
\]

Put
\[
 e_T(m)=b_T(m)-b_{T-1}(m).
\]

Assume that there are functions
\[
 u_1(T),\ldots,u_d(T)
\]
and node modes
\[
 \phi_1(m),\ldots,\phi_d(m)
\]
such that every old-node increment has the exact representation
\[
\boxed{
 e_T(m)=\sum_{j=1}^{d}u_j(T)\phi_j(m)
 \qquad(m\le T-1).
}
\tag{L-91104.1}
\]

Let \(\mathcal L_n\) be a fixed local linear row operator using only
\[
 m=n,n+1,\ldots,n+k.
\]
Define
\[
 a_T(n)=\mathcal L_ne_T.
\tag{L-91104.2}
\]

For every deep row
\[
 n\le T-k-1,
\]
all nodes used by \(\mathcal L_n\) are old, and hence
\[
\boxed{
 a_T(n)=\sum_{j=1}^{d}u_j(T)v_j(n),
 \qquad
 v_j(n)=\mathcal L_n\phi_j.
}
\tag{L-91104.3}
\]

Therefore the complete deep endpoint-row matrix has rank at most \(d\).

## 2. Exact moment-neutral cancellation

Let \(c_T\) be a finite endpoint perturbation whose smallest active endpoint is \(T_0\). Then for every
\[
 n\le T_0-k-1,
\]
equation (L-91104.3) gives
\[
 \sum_Tc_Ta_T(n)
 =
 \sum_{j=1}^{d}
 \left(\sum_Tc_Tu_j(T)\right)v_j(n).
\tag{L-91104.4}
\]

Thus the \(d\) moment equations
\[
\boxed{
 \sum_Tc_Tu_j(T)=0,
 \qquad 1\le j\le d,
}
\tag{L-91104.5}
\]
annihilate the complete inherited bulk:
\[
\boxed{
 \sum_Tc_Ta_T(n)=0
 \qquad(n\le T_0-k-1).
}
\tag{L-91104.6}
\]

No norm estimate or asymptotic approximation enters.

## 3. Minimal adjacent packets

Choose \(d+1\) consecutive endpoints
\[
 T_0,T_0+1,\ldots,T_0+d.
\]

If the \(d\times(d+1)\) moment matrix
\[
 [u_j(T_0+i)]_{1\le j\le d,\ 0\le i\le d}
\]
has rank \(d\), its nullspace is one-dimensional. Hence there is a unique nonzero packet, up to scalar,
\[
 (c_0,\ldots,c_d)
\]
satisfying (L-91104.5).

By (L-91104.6), its row image is supported inside
\[
\boxed{
 T_0-k\le n\le T_0+d-1.
}
\tag{L-91104.7}
\]

The packet therefore occupies at most
\[
\boxed{d+k}
\tag{L-91104.8}
\]
moving boundary rows.

For the parabolic endpoint family,
\[
 d=2,\qquad k=2,
\]
so the minimal packet uses three adjacent endpoints and exactly four possible boundary rows: the butterfly of `L-91101`.

## 4. Chebyshev sign alternation

Assume \(u_1,\ldots,u_d\) form a strict discrete Chebyshev system on the ordered endpoint set: every ordered \(d\times d\) evaluation determinant has the same nonzero sign.

The null vector of the \(d\times(d+1)\) adjacent moment matrix is given by its signed maximal cofactors. The Chebyshev determinant signs therefore imply
\[
\boxed{
 (-1)^ic_i
 \quad\text{has one fixed strict sign}.
}
\tag{L-91104.9}
\]

Thus every minimal moment-neutral endpoint packet has alternating coefficients. It is the endpoint analogue of a compact generalized B-spline or divided-difference atom.

For \(d=2\), the signs are \(+,-,+\), exactly the martingale butterfly.

## 5. Scale-filter / endpoint-packet duality

A multiplicative annular filter
\[
 \mathcal F b_X
 =
 \sum_{i=0}^{D}c_i b_{X/R^i}
\]
is compact because its coefficients annihilate the finite set of scale modes carried by \(b_X(m)\) below the innermost endpoint.

An endpoint packet
\[
 \sum_Tc_Ta_T
\]
is compact because its coefficients annihilate the finite set of endpoint increment modes \(u_j(T)\).

These are two manifestations of the same principle:
\[
\boxed{
 \text{finite scale-mode rank}
 +
 \text{moment annihilation}
 \Longrightarrow
 \text{compact arithmetic boundary packet}.
}
\tag{L-91104.10}
\]

The factor-64 polynomial filter performs moment cancellation on a fixed geometric scale grid. The moment-neutral shadow packet performs the same cancellation adaptively on the endpoint-state grid.

This duality suggests a general design rule:

```text
global annular filter:
    choose roots to annihilate scale modes;

local endpoint transport:
    choose martingale moments to annihilate endpoint modes.
```

The former yields a compact criterion; the latter yields a compact positive producer.

## 6. Higher-order generalization

If a higher Riesz or fractional endpoint seed has old-node increments in a \(d\)-dimensional mode space, then:

1. its deep endpoint matrix has rank at most \(d\);
2. \(d\) endpoint moments are the exact inherited-bulk invariants;
3. \(d+1\) adjacent endpoints generate the minimal compact packet;
4. a Chebyshev mode system forces alternating packet signs;
5. the packet touches only \(d+k\) boundary rows.

Thus the parabolic butterfly is the first member of a hierarchy of generalized endpoint B-splines.

This gives a systematic route for designing new producers rather than guessing scale filters or high-dimensional LP coordinates.

## 7. Proof boundary

Closed exactly:

1. the finite-rank deep-interior theorem;
2. moment-neutral cancellation;
3. compact support of minimal adjacent packets;
4. Chebyshev cofactor sign alternation;
5. scale-filter/endpoint-packet duality.

Still open:

1. verification of favorable score curvature for higher-order seeds;
2. positive capacity lifts for generalized packets;
3. the killed-shadow feasibility theorem in the parabolic \(d=2\) case;
4. RH.
