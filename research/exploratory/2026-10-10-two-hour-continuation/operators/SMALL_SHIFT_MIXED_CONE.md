# A small shift expands the complete mixed-moment cone

Status: complete actual-source analytic theorem with exact rational guards.
For the same complete actual Xi source, at the fixed shift t=1,

\[
                       D_{n,j}(1)>0
       \quad\text{for EVERY integer }n,j\ge0\text{ with }
                       j\le3100(n-1)+1500.                     \tag{SS1}
\]

Here c=3/4, b_n=c^n*C_(n+1)(1), and
D_(n,j)=sum_(h=0)^j(-1)^h*binom(j,h)*b_(n+h). Every unknown complex
occurrence and all multiplicities remain in these sums. This proves an
infinite family with arbitrarily large mixed degree. It does not prove
every mixed pair, all-order actual Hankel positivity or RH.

The exact source, complete-tail and real-head argument is MM1–MM3 in
`FINITE_CENSUS_MIXED_MOMENT_CONE.md`, SHA256
b904361d5af54885d6cd9bb1cfd730f11fdd05e6a0f2c1557328a92b5a40f166.
Its count-free actual real head through5419, known actual occurrence,
strip half-width1/2 and complete theta/Jensen upper count are unchanged.
Here the same frozen first-root interval is explicitly checked inside
(14.1347,14.1348), instead of losing that information in the coarser14..15
bounds. This companion changes the shift and finite rational constants;
it performs no additional root, moment or quadrature computation.

## SS2. Exact small-shift comparison

The hypothesis t^2>=3*A^2 still holds, since1>=3/4. Therefore MM2–MM3
bound the whole tail by2Q^(-n) for n>=1 with

\[
 l=141347/10000,\quad b=141348/10000,\quad
 a=l^2+1/4=20003974409/100000000,\quad
 B=b^2+1=1254953569/6250000,\quad Q=117462247/4,\\
 r=B/Q=1254953569/183534760937500,\quad
 s=B/a=692388176/689792221>1.
\]

The exact known real atom contributes more than a^j/B^(n+j+1). The
complete tail/head ratio is consequently less than or equal to

\[
                         2B r^n s^j.                            \tag{SS2}
\]

The checker verifies exact positive rational inequalities

\[
 0<r<1,\qquad 2Brs^{1500}<4/5,\qquad r s^{3100}<4/5.           \tag{SS3}
\]

For j<=3100(n-1)+1500, n>=1 automatically, and s>1 gives

\[
 2Br^n s^j\le(2Brs^{1500})(r s^{3100})^{n-1}<(4/5)^n<1.       \tag{SS4}
\]

Thus the retained actual real head strictly dominates the entire unknown
tail for EVERY pair in SS1. No finite enumeration of those pairs is used.
For scale only,2Brs^1500 is approximately.7686215 and r*s^3100 is
approximately.7800016; all acceptance comparisons use exact fractions.

## SS3. Scope and the remaining source mechanism

At n=1 the theorem already covers all0<=j<=1500; at n=2 it covers
all0<=j<=4600, and every increase of n adds3100 allowed mixed degrees.
This is a different shifted normalization
from the t=512 cone; combining their results does not equate their mixed
coefficients or remove the uncovered pairs at either shift.

The universal Hausdorff criterion holds at one fixed admissible shift only
when EVERY n,j>=0 is controlled. SS1 leaves n=0 and arbitrarily large j
at each fixed n uncovered. If an off-real node exists, the constructive
negative-witness theorem forces a complete negative mixed coefficient in
that complementary region. The source obstruction survives these positive
cones; this note supplies no unproved monotonic transport in j or shift.

The contrast in the two proved cones has a concrete mechanism: reducing
the shift reduces B/a, the penalty for the mixed index j, while using the
actual first-root interval avoids artificial loss in that ratio. The known
first real atom still remains much larger than every unknown-tail node.
All zero-location information stays bounded by the inherited complete
head. An ever-growing real head or an independent whole-source mixed-sign
mechanism is required for a universal conclusion.
