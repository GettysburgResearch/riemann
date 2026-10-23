# Retaining the physical local-modulus support in the label vector

23 October 2026. Proposed source-dependent deduction by root; independent
review requested. This is a full Gauss-series vector estimate. It does not
assert its primitive analogue or a smaller zero-free boundary.

Use the exact coefficients, fixed sectors, literal zeros and local table of
`SIXTH_FREE_LABEL_EXTENSION.md`, SHA256
`3e4a3d902aa937d7a498ab1201a269e6891265a9b1c8a34945524c330797b507`,
and the finite decomposition V4--V11 of `SHORT_LABEL_RESIDUE_VECTOR.md`.
Ideal letters inside exponents denote absolute norms. Write the actual
inverse input as `I(X,D) << (XDNQ)^epsilon (X+X^(1/6)D^(5/6))`.
The smooth tests have the same fixed annular support and seminorm convention.

## 1. Improved finite vector

For all good sixth-power-free labels R of norm at most K, and X,D,K>=1,
the proposed strengthening is

\[
 \sum_{NR\le K}|S_R(X)|^2
 \ll (XDKNQ)^\epsilon
       \min\{K,1+K/\sqrt X\}\{X+X^{1/6}D^{5/6}\}.       \tag{L1}
\]

The scalar-sum K bound is unchanged. For the other bound, retain the
predecessor's local factors h,g,l, with H=Nh, L=Nl, and local squared
weight omega. Its full modulus is `c=e^2 l c0`. On the physical annulus
`Nc asymp X`, necessarily `L <= C X` for a fixed support constant C.
This restriction was discarded in the earlier estimates of the four sums.

The four sums in that proof are

\[
 S_0=\sum\omega,\quad S_1=\sum\omega L/H,\quad
 S_2=\sum\omega L^{2/3}H^{-5/6},\quad
 S_3=\sum\omega L^{1/6}H^{-1/3}.                     \tag{L2}
\]

For each prime put a=v_p(h), epsilon=1_(p|n), j=v_p(l), and let w be
the exponent of q=Np in omega. The exact nonprincipal branches have
`j=a+epsilon+1`, `6` not dividing j, and `w=-1-epsilon`. The additional
principal branches are `(a,epsilon,j,w)=(4,1,6,-3),(5,0,6,-2),(5,1,6,-1)`.
The nonprincipal `(5,1,7,-2)` is retained too. In every branch,

\[
 w\le-1,\quad w+j/2-a\le-1,\quad
 w+5j/12-5a/6\le-1,\quad w+j/6-a/3\le-1.            \tag{L3}
\]

These are direct rational inequalities. Applying Rankin to the physical
local modulus L, at exponents respectively `epsilon`, `1/2+epsilon`,
`1/4+epsilon`, and `epsilon`, makes every local Euler sum convergent.
There are a fixed number of branches at each prime; all have j>=2.
Consequently, with every local branch and shared-prime zero retained,

\[
 S_0\ll X^\epsilon,\quad S_1\ll X^{1/2+\epsilon},\quad
 S_2\ll X^{1/4+\epsilon},\quad S_3\ll X^\epsilon.    \tag{L4}
\]

The restrictions H<=K may be discarded in these positive sums. The
predecessor's fixed-divisor Cauchy and dyadic e aggregation are otherwise
unchanged. Expanding the same sixth-order sieve now gives the multiplier

\[
 1+KX^{-1/2}+K^{5/6}X^{-5/12}+K^{1/3}X^{-1/6}.
\]

With x=K/sqrt(X), this is `1+x+x^(5/6)+x^(1/3) << 1+x`.
This proves L1. No assertion of a better arbitrary-coefficient sieve was used.

## 2. Original and reflected completion envelopes

Let B_R(Y) be the original completed finite vector and F_R(Y) its completed
contour vector, as in `COHERENT_FULL_REMAINDER_VECTOR.md`, SHA256
`f6058c80c4bde0f049f7f7a50740cfae4d4a158a88e1bc6c0cb8534be8f215a4`.
Then L1 implies

\[
 \sum_R|B_R(Y)|^2\ll (YDKNQ)^\epsilon
 [Y+K\sqrt Y+D^{5/6}Y^{1/6}+D^{5/6}K],\qquad Y\ge1. \tag{L5}
\]

Indeed expand L1 as `X+K sqrt(X)+D^(5/6)X^(1/6)+D^(5/6)K X^(-1/3)`.
In `sum_b b^(-1) S_R(Y/b^6)`, the first three square-root terms have
summable b weights `b^-4,b^-5/2,b^-3/2`. For the fourth, the b weight
is constant after taking its square root, but the original annular support
forces `b << Y^(1/6)`. Its total amplitude is `O(D^(5/12)sqrt(K))`.
For subunit Y the finite part is zero below a fixed threshold; the bounded
transition range is covered by fixed constants.

For a label dyad NR asymp H<=K put C=DH/Y. The reflected estimate is

\[
 \sum_{NR\asymp H}|F_R(Y)|^2\ll (YDHNQ)^\epsilon
 [C+H\sqrt C+D^{5/6}C^{1/6}+D^{5/6}H].               \tag{L6}
\]

Here and below fixed subpowers can use `(2+Y+1/Y)` when Y is subunit;
the explicit small-scale argument in section3 avoids retaining that loss.
To verify L6, use the unchanged numerator and fixed finite reflection
matrix of the completed FE. Separate the common norm profiles first.
Before the completion b-sum, the reflected kernel obeys
`|K_w(x)| << min(x^(1/6-epsilon),x^-A)` with its required derivatives.
For C>=1, dyadic application of L1 to the physical modulus gives amplitude

    C^(1/2) + sqrt(H) C^(1/4)
      + D^(5/12) [C^(1/12) + sqrt(H) C^(-1/6)],

up to subpowers. The final term has only a logarithmic dyadic loss:
its `X^(-1/6)` cancels the small-x kernel power `X^(1/6)`.
For C<1 use rapid large-x decay directly, obtaining arbitrarily high
positive powers of C times `O((1+sqrt(H))(1+D^(5/12)))`.

Now restore every integral completion ideal b, with weight b^-1 and scale
`C/b^6`. For `b<=C^(1/6)`, the first three amplitude terms sum as in L5.
The fourth is constant in b after its weight, so its sum is
`O(D^(5/12)sqrt(H))`. For `b>C^(1/6)`, the rapid subunit-scale estimate
gives the same bound. If C<1 the entire sum uses that rapid estimate.
Thus no infinite constant-weight b tail was used. This proves L6.

## 3. Full raw remainder

Retain the short residue vector `sum_R |P_R(D)|^2 << D^(2/3+epsilon)`
for `K<=D^(1/7)`, proved in the predecessor. The improved raw vector is

\[
 \boxed{\quad
 \sum_{NR\le K}|\mathcal R_R(U)|^2
 \ll ((2+U)DKNQ)^\epsilon
 [D^{11/12}K^{1/12}+D^{5/6}K],\qquad U>0,
 \quad 1\le K\le D^{1/7}.\quad}                      \tag{L7}
\]

For `U>=sqrt(DK)`, use the exact reciprocal completion, split at
`A=U^(1/6)(DK)^(-1/12)`, and apply L6 to the head and L5 minus its
complete pole to the tail. The base volume, nonvolume and pole costs
are unchanged: their squares are `(DK)^(1/2)`, `D^(11/12)K^(1/12)`,
and `D^(5/6)K^(1/6)`. The new mixed volume term has head amplitude

    D^(1/4) K^(3/4) U^(-1/4) sum_(a<=A) a^(1/2)
       << D^(1/8) K^(5/8),

and the original tail gives the same value. Its square `D^(1/4)K^(5/4)`
is dominated by the first term in L7 for `K<=D^(1/7)`.
The remaining plateau has squared cost `D^(5/6)K`; its a-weight is
harmonic over a finite head or over the finite original support range.
All subunit original terms are exactly negative poles and sum absolutely.

For `1<=U<=sqrt(DK)`, use the exact raw finite-minus-pole identity and L1.
Its coarse finite bound is the bracket in L5 with Y=U. Every term is
at most the bracket in L7, by the same comparisons just made; the pole
cost is `U^(1/3)D^(2/3)<=D^(5/6)K^(1/6)`. Fixed U below 1 are covered
by the finite transition range and the exact negative-pole expression
below the original annular support threshold. This proves the all-scale
statement without an inverse power of U hidden in the epsilon loss.

For `U=D^h`, comparison with the old inverse resource `D^(5/6+h/6)`
now permits `k<min(2h-1,h/6,1/7)` when `K=D^k`. This is a full-series
bound only. Its transfer through the selected-prime primitive inversion
and its relation to the complementary inverse space remain separate.
