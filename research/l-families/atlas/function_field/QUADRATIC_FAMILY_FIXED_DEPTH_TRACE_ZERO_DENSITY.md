# Odd-notch fixed-depth trace-zero density through `M^-3`

Status: **exact for every fixed depth, conditional only on the standard
fixed-modulus prime-polynomial progression theorem; raw detector zeros, not
zeros of an individual `L`-function**.

Exact replay:
[`quadratic_family_fixed_depth_trace_zero_density.py`](quadratic_family_fixed_depth_trace_zero_density.py).

## 0. Outcome

Fix an odd prime power `q` and an integer `j>=1`.  Put

\[
 n=2h+1,\qquad M=4h+1,\qquad d=h-j,
\]

and assume `h>=5j+2`.  Let `Z^(j)_(q,h)` count monic squarefree degree-`M`
conductors whose least factor degree is exactly `d` and whose raw
closed-place notch detector vanishes.  Write

\[
 \delta_{j,0,q}=\Pr(D_{2j+1}=0)
\tag{0.1}
\]

and, for `1<=s<=j`,

\[
 \delta_{j,s,q}
 =\Pr(D_{2j+1}+D_{2j+1-2s}=0).
\tag{0.2}
\]

The probabilities are taken in the exact finite independent-sign model of
Section 5.  Parity gives the unconditional identity

\[
 \boxed{\delta_{j,j,q}=0.}
\tag{0.3}
\]

No positivity is asserted for any of the other local probabilities.

For every fixed `q,j`,

\[
\boxed{
\begin{aligned}
 {Z^{(j)}_{q,h}\over q^M}
={}&{\delta_{j,0,q}(1+\log2)\over3h^2}\\
 &+{1\over h^3}\left[
 {\delta_{j,0,q}\bigl((2j-1)(7+4\log2)+9\bigr)\over36}
 +{1\over2}\sum_{s=1}^{j}\delta_{j,s,q}\right]
 +O_{q,j}(h^{-4}).
\end{aligned}}
\tag{0.4}
\]

After division by the exact squarefree count `q^M-q^(M-1)`, this becomes

\[
\boxed{
\begin{aligned}
 {Z^{(j)}_{q,h}\over q^M-q^{M-1}}
={1\over1-q^{-1}}\Bigg[
 &{16\delta_{j,0,q}(1+\log2)\over3M^2}\\
 &+{32\over M^3}\left(
 {\delta_{j,0,q}\bigl((7j+4)+(4j+1)\log2\bigr)\over9}
 +\sum_{s=1}^{j}\delta_{j,s,q}\right)
 +O_{q,j}(M^{-4})\Bigg].
\end{aligned}}
\tag{0.5}
\]

Thus every fixed depth is `O_(q,j)(M^-2)`.  This is an upper bound: if
`delta_(j,0,q)=0`, the displayed `M^-2` coefficient vanishes.

## 1. Frozen inputs and claim boundary

The packet checks the following historical blobs exactly.

| input | commit | blob |
|---|---|---|
| closed-place notch | `9716d2261e9e7843a6c1ffffd67ee8d6756060aa` | `a1b8476ddd3cad6f63ff205392426ae9c2d0829c` |
| depth phase diagram | `4fc8930e14eaa3863d3f3edc151c056d7d5aedce` | `01cefa8a55c9b1ae1a0b5bed9c11fe323fb6764e` |
| parity sieve | `0b9f407f10ab8b12f22526af8a08b870baaef0e9` | `38f1b6e95f9a7eb6756450673ff067308886a0ff` |
| `j=1` theorem | `f5aabadd65dd53cd9a69e3e3b38b9bc7693b3359` | `12aa4be45fd970f843be6b2024547f7ab7594b21` |
| `j=1` replay | `f5aabadd65dd53cd9a69e3e3b38b9bc7693b3359` | `60dc980a4e8bccb2cdd607829d167909b3f4729c` |
| `j=2` theorem | `d13dfcfcbb32733fc9b7925b82c4cf3dc9a9107a` | `ba853379190d9f4de1172f576095ed29a068c0dd` |
| `j=2` replay | `d13dfcfcbb32733fc9b7925b82c4cf3dc9a9107a` | `8ca76f0286cf95537ba8f00081ba973e2940ed69` |

The only analytic input beyond the frozen exact identities is the standard
prime-polynomial theorem in fixed residue classes.  The result is not
uniform as `j` grows and makes no claim about an individual `L`-function
zero, RH, GRH, or external priority.

The convenient stable range `h>=5j+2` is sufficient, not claimed sharp.  It
simultaneously gives

\[
 2(h-j)>h,\qquad h-j>2j+1,\qquad 5(h-j)>4h+1.
\tag{1.1}
\]

These inequalities respectively collapse the low reciprocal coefficients,
make every polynomial seen by the local channels coprime to `Q`, and rule
out five-factor profiles.  For `j=1,2` the bound is exactly `h>=7,12`, the
stable ranges used in the two predecessor packets.

## 2. Exact residual and parity

Write `m_r` for the number of irreducible factors of `Q` of degree `r`.  The
locked notch identity is

\[
 S_{n,Q}=\sum_{k=1}^{h}a_kD_{n-2k},\qquad
 \sum_{k\ge0}a_kx^k=\prod_{P\mid Q}(1-x^{\deg P})^{-1}.
\tag{2.1}
\]

Since the least factor degree is `d=h-j`, the first possible terms have
`k=d,...,h`.  The first inequality in (1.1) prevents a sum of two factor
degrees from entering any such coefficient, so

\[
 a_{h-j+s}=m_{h-j+s}\qquad(0\le s\le j).
\]

Substitution in (2.1) proves the all-depth residual

\[
\boxed{
 S_{n,Q}=\sum_{s=0}^{j}m_{h-j+s}D_{2j+1-2s}.}
\tag{2.2}
\]

For every odd `r<=2j+1`, put

\[
 p_r=\sum_{\deg F=r}\psi_Q(F).
\]

The second inequality in (1.1) makes every summand a sign.  There are `q^r`
summands, so every `p_r` is odd.  Since

\[
 D_1=p_1,\qquad D_r=p_r-qp_{r-2}\quad(r\ge3),
\]

we obtain

\[
\boxed{D_1\equiv1\pmod2,\qquad D_r\equiv0\pmod2
       \quad(r\ge3\text{ odd}).}
\tag{2.3}
\]

Consequently `S_(n,Q)=0` requires `m_h` even.  In particular the
three-factor profile containing one degree-`h` factor can never vanish;
this is exactly (0.3).

## 3. The complete profile list through `h^-3`

The two-factor profile is

\[
 (d,3h+j+1).
\tag{3.1}
\]

Every three-factor profile is `(d,e,3h+j+1-e)`.  Splitting at `e=h` gives
the following exhaustive table.

| type | profile | exact zero condition | principal weight |
|---|---|---|---:|
| generic | `(d,3h+j+1)` | `D_(2j+1)=0` | `1/(d(3h+j+1))` |
| generic | `(d,e,3h+j+1-e)`, `h+1<=e<=(3h+j+1)/2` | `D_(2j+1)=0` | `1/(de(3h+j+1-e))` |
| repeated minimum | `(d,d,2h+2j+1)` | `D_(2j+1)=0` | `1/(2d^2(2h+2j+1))` |
| near `h` | `(d,d+s,2h+2j+1-s)`, `1<=s<=j` | `D_(2j+1)+D_(2j+1-2s)=0` | `1/(d(d+s)(2h+2j+1-s))` |

At a repeated generic midpoint the second-row weight receives the usual
factor `1/2`.  The final near-`h` row with `s=j` has zero raw population by
parity, although retaining `delta_(j,j,q)=0` makes the formulas uniform.

All remaining profiles have four factors.  Relative to four copies of `d`,
their nonnegative nondecreasing excesses sum to

\[
 M-4d=4j+1.
\tag{3.2}
\]

There are therefore only `O_j(1)` such degree profiles, each with principal
weight `O_j(h^-4)`.  Their entire raw zero population is absorbed by the
remainder in (0.4), without needing to solve their multichannel zero
conditions.

The locked rough-layer bound also gives the coarser estimate

\[
 Z^{(j)}_{q,h}=O_{q,j}(q^Mh^{-2}),
\]

which independently excludes an `M^-1` term at any one fixed depth.

## 4. Exact weights and the generic coefficient

Let `W_j(h)` be the sum of the two generic rows.  Partial fractions, with
half weight at a repeated midpoint, give the exact identity proposed by the
first two depths:

\[
\boxed{
 W_j(h)={1+H_{2h+j}-H_h\over(h-j)(3h+j+1)}.}
\tag{4.1}
\]

Indeed, reflection `e -> 3h+j+1-e` fills the complete harmonic interval
`h+1,...,2h+j`.  Euler--Maclaurin gives

\[
 H_{2h+j}-H_h
 =\log2+{2j-1\over4h}+O_j(h^{-2}),
\tag{4.2}
\]

while

\[
 {1\over(h-j)(3h+j+1)}
 ={1\over3h^2}\left(1+{2j-1\over3h}+O_j(h^{-2})\right).
\tag{4.3}
\]

Therefore

\[
\boxed{
 W_j(h)
 ={1+\log2\over3h^2}
 +{(2j-1)(7+4\log2)\over36h^3}
 +O_j(h^{-4}).}
\tag{4.4}
\]

This proves the requested generic coefficient.  The remaining third-order
weights are

\[
 {1\over2(h-j)^2(2h+2j+1)}
 ={1\over4h^3}+O_j(h^{-4})
\tag{4.5}
\]

for the repeated minimum, and, for each fixed `1<=s<=j`,

\[
 {1\over(h-j)(h-j+s)(2h+2j+1-s)}
 ={1\over2h^3}+O_j(h^{-4}).
\tag{4.6}
\]

Equations (4.4)--(4.6) prove (0.4).

## 5. The finite local delta tower

Let

\[
 \mathcal R_{\le2j+1}=\prod_{\deg R\le2j+1}R
\]

and attach an independent uniform sign `epsilon_R` to every irreducible
factor of this fixed modulus.  Define

\[
 P_\epsilon(u)
 =\prod_{\deg R\le2j+1}(1-\epsilon_Ru^{\deg R})^{-1}
 =\sum_{r\ge0}p_r(\epsilon)u^r,
\tag{5.1}
\]

and

\[
 D_r(\epsilon)=p_r(\epsilon)-qp_{r-2}(\epsilon),
 \qquad p_{-1}=0.
\tag{5.2}
\]

Equations (0.1)--(0.2) are probabilities on this finite sign space.  Formula
(2.3) proves `delta_(j,j,q)=0`, but parity gives no obstruction for
`s<j`: both exterior channels are then even.  This packet deliberately does
not claim that `delta_(j,0,q)` or any `delta_(j,s,q)` with `s<j` is positive.

For each fixed profile, character orthogonality and the prime-polynomial
theorem modulo `R_(<=2j+1)` make the conductor residue uniform, up to an
error exponentially small in `h`.  Repeated-degree distinctness corrections
are exponentially small as well.  There are `O(h)` generic profiles and
only `O_j(1)` exceptional profiles, so the total analytic error is
`O_(q,j)(q^M h^-4)`.  Thus the same finite local probabilities apply to all
profiles carrying their labels in Section 3.

## 6. Conversion to `M` and exact recovery of `j=1,2`

Since `h=(M-1)/4`,

\[
 h^{-2}=16M^{-2}+32M^{-3}+O(M^{-4}),\qquad
 h^{-3}=64M^{-3}+O(M^{-4}).
\tag{6.1}
\]

Substituting (6.1) into (0.4) gives (0.5).

For `j=1`, parity kills `delta_(1,1,q)`.  The `h^-3` coefficient of
`delta_(1,0,q)` is

\[
 {(7+4\log2)+9\over36}={4+\log2\over9},
\]

and its `M^-3` coefficient is `32(11+5log(2))/9`.  These are exactly the
second-boundary formulas.

For `j=2`, parity kills `delta_(2,2,q)`, while

\[
 \delta_{2,0,q}=\Pr(D_5=0),\qquad
 \delta_{2,1,q}=\Pr(D_5+D_3=0).
\]

The `h^-3` coefficient of `delta_(2,0,q)` is

\[
 {3(7+4\log2)+9\over36}={5+2\log2\over6},
\]

and (0.5) becomes exactly the third-boundary formula

\[
 {1\over1-q^{-1}}\left[
 {16\delta_{2,0,q}(1+\log2)\over3M^2}
 +{32\bigl(\delta_{2,0,q}(2+\log2)+\delta_{2,1,q}\bigr)\over M^3}
 +O_q(M^{-4})\right].
\]

## 7. Aggregation boundary

For any fixed finite set of depths, summing (0.5) remains `O(M^-2)`.
Consequently an aggregate `M^-1` contribution can only come from a number
of depths that grows with `M`.  This is only a necessary condition, not a
sufficiency theorem: the fixed-depth error is not uniform in `j`, and the
decay or nondecay of

\[
 \delta_{j,0,q},\ \delta_{j,1,q},\ldots,\delta_{j,j-1,q}
\]

is the decisive open local question.

## 8. Proof ledger and bounded replay

Proved:

- the exact all-depth residual (2.2) for fixed `j` in the stable range;
- the parity-zero terminal channel (0.3);
- the exhaustive two/three-factor profile list and the `O_j(h^-4)`
  four-factor remainder;
- the exact harmonic identity (4.1) and generic coefficient (4.4);
- the full fixed-`q,j` raw zero density (0.4)--(0.5);
- literal recovery of the `j=1` and `j=2` predecessor formulas;
- the necessary aggregation condition in Section 7.

Open:

- positivity or decay of the general local delta tower;
- any asymptotic uniform in growing `j`;
- the aggregate over all depths;
- any individual `L`-function zero, RH, or GRH consequence.

Run:

```text
python -B research/l-families/atlas/function_field/quadratic_family_fixed_depth_trace_zero_density.py --check
python -B -O research/l-families/atlas/function_field/quadratic_family_fixed_depth_trace_zero_density.py --check
python -B -m unittest tests.test_quadratic_family_fixed_depth_trace_zero_density
python -B -O -m unittest tests.test_quadratic_family_fixed_depth_trace_zero_density
```

The replay checks depths `1<=j<=8` and 7,421 degree profiles.  It enumerates
no polynomial, irreducible, residue class, field element, curve, point, or
zero.
