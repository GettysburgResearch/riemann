# Odd-notch second-boundary density through `M^-3`

Status: **exact fixed-`q` third-order asymptotic, conditional only on the
standard fixed-modulus prime-polynomial progression theorem; detector zeros,
not zeros of an individual `L`-function**.

Exact replay:
[`quadratic_family_second_boundary_zero_density_third_order.py`](quadratic_family_second_boundary_zero_density_third_order.py).

## 0. Outcome

Keep the notation of the preceding packet:

\[
 n=2h+1,\qquad M=4h+1,
\]

and let `Z^(2)_(q,h)` count monic squarefree degree-`M` conductors whose least
factor degree is `h-1`, which have no degree-`h` factor, and for which the
exterior-cubic residual `D_3` vanishes.  For every fixed odd prime power `q`,

\[
\boxed{
 {Z^{(2)}_{q,h}\over q^M}
 =\delta_q\left{
 {1+\log2\over3h^2}
 +{4+\log2\over9h^3}
 +O_q(h^{-4})\right}.}
\tag{0.1}
\]

The finite probability `delta_q` is exactly the same one as at leading order:

\[
 \delta_q=\Pr\left(
 S_3+S_1S_2+{S_1^3+(2-3q)S_1\over6}=0\right).
\tag{0.2}
\]

After division by the exact squarefree count `q^M-q^(M-1)` and use of
`h=(M-1)/4`, this becomes

\[
\boxed{
 {Z^{(2)}_{q,h}\over q^M-q^{M-1}}
 ={\delta_q\over1-q^{-1}}\left{
 {16(1+\log2)\over3M^2}
 +{32(11+5\log2)\over9M^3}
 +O_q(M^{-4})\right}.}
\tag{0.3}
\]

The exceptional raw-zero profile `(h-1,h,h,h+2)` is `O_q(M^-4)`, so (0.3)
is also the full second-boundary raw-zero density through order `M^-3`.

## 1. Frozen inputs and claim boundary

The exact residual and parity reduction is frozen at commit
`97cdc4a5ea27bc1052dbad7eef19276da331388c`.  The leading-density and local
probability packet is frozen at commit
`9d4f13a9e1d788f9460a02cad0c21be45b6803f2`, blob
`5aa85cdbc5ddf45327569845843f9815a02726ff`.

This note refines only the factor-profile asymptotic.  It does not infer an
individual `L`-function zero, RH, GRH, or an external novelty claim.

## 2. Exhausting the profiles at the required order

For `h>=7`, the `m_h=0` degree budget leaves the following complete list.
The factorials in the weight column account for repeated factor degrees.

| multiplicity of `h-1` | profile | principal `q^M` weight | scale |
|---:|---|---:|---:|
| 1 | `(h-1,3h+2)` | `1/((h-1)(3h+2))` | `h^-2` |
| 1 | `(h-1,d,3h+2-d)` | `1/((h-1)d(3h+2-d))` | total `h^-2` |
| 2 | `(h-1,h-1,2h+3)` | `1/(2(h-1)^2(2h+3))` | `h^-3` |
| 2 | `(h-1,h-1,h+1,h+2)` | `1/(2(h-1)^2(h+1)(h+2))` | `h^-4` |
| 3 | `(h-1,h-1,h-1,h+4)` | `1/(6(h-1)^3(h+4))` | `h^-4` |

In the second row,

\[
 h+1\le d\le{3h+2\over2},
\]

and the midpoint receives half weight when it is integral.  Four pinned
factors cannot meet the degree budget for `h>=7`.  Thus only the first three
rows can affect the answer through `h^-3`.  The replay independently
enumerates nondecreasing degree multisets through `h=40` and checks this
closed list exactly.

## 3. Euler--Maclaurin for the one-pinned profiles

Let `W_1(h)` be the sum of the first two rows.  Partial fractions and the
half-weight midpoint combine into an exact harmonic-number identity:

\[
\begin{aligned}
 W_1(h)
 &= {1\over(h-1)(3h+2)}
 +{1\over h-1}\sum_{d=h+1}^{(3h+2)/2}{}^{\!*}
 {1\over d(3h+2-d)}\\
 &= {1+H_{2h+1}-H_h\over(h-1)(3h+2)}.
\end{aligned}
\tag{3.1}
\]

Here the star records the half-weight endpoint.  Euler--Maclaurin gives

\[
 H_{2h+1}-H_h
 =\log2+{1\over4h}+O(h^{-2}),
\tag{3.2}
\]

while

\[
 {1\over(h-1)(3h+2)}
 ={1\over3h^2}\left(1+{1\over3h}+O(h^{-2})\right).
\tag{3.3}
\]

Consequently

\[
\boxed{
 W_1(h)
 ={1+\log2\over3h^2}
 +{7+4\log2\over36h^3}
 +O(h^{-4}).}
\tag{3.4}
\]

## 4. The two-pinned correction

The only new third-order profile is `(h-1,h-1,2h+3)`.  Its two equal pinned
degrees produce the essential factor `1/2`:

\[
 {1\over2(h-1)^2(2h+3)}
 ={1\over4h^3}+O(h^{-4}).
\tag{4.1}
\]

Adding (4.1) to (3.4) gives

\[
 {7+4\log2\over36}+{1\over4}
 ={4+\log2\over9},
\]

which proves the profile part of (0.1).

## 5. Why the same `delta_q` survives

Every factor in every listed profile has degree at least `h-1`, so it is
coprime to the fixed modulus

\[
 \mathcal R_{\le3}=\prod_{\deg R\le3}R.
\]

For any fixed profile, character orthogonality and the prime-polynomial
theorem in progressions make the product residue uniform in
`(F_q[T]/R_(<=3))^times`.  This remains true for the repeated-degree pair:
the diagonal removed by `binom(I_q(h-1),2)` is exponentially smaller than
`q^M` at fixed `q`.  The number of profiles is `O(h)`, and every
nonprincipal-character or prime-count error has an exponential saving in
`h`.  Their total is therefore `O_q(q^M h^-4)`.

The local signs are consequently independent uniform Rademacher variables
to the required main orders for every profile.  The fraction satisfying
`D_3=0` is the same exact `delta_q`; no new joint residue law appears at
third order.

## 6. Conversion from `h` to `M`

Since `h=(M-1)/4`,

\[
 {1\over h^2}={16\over M^2}+{32\over M^3}+O(M^{-4}),
 \qquad
 {1\over h^3}={64\over M^3}+O(M^{-4}).
\tag{6.1}
\]

Writing

\[
 C_2={1+\log2\over3},\qquad C_3={4+\log2\over9},
\]

the third coefficient is

\[
 32C_2+64C_3
 ={32(11+5\log2)\over9}.
\tag{6.2}
\]

Together with the exact squarefree denominator, this proves (0.3).

## 7. Proof ledger and bounded replay

Proved:

- the exact closed profile list for all `h>=7`;
- the harmonic compression (3.1) and its third-order expansion;
- the unique two-pinned `h^-3` correction;
- persistence of the same finite local probability `delta_q`;
- the fixed-`q` count and squarefree density through `M^-3`.

Still open:

- the `M^-4` coefficient, where both remaining rough profiles and the
  exceptional mixed trace `D_3+2D_1=0` enter;
- a uniform joint limit in `q` and `h`;
- any individualization to one `L`-function.

Run:

```text
python -B research/l-families/atlas/function_field/quadratic_family_second_boundary_zero_density_third_order.py --check
python -B -O research/l-families/atlas/function_field/quadratic_family_second_boundary_zero_density_third_order.py --check
python -B -m unittest tests.test_quadratic_family_second_boundary_zero_density_third_order
python -B -O -m unittest tests.test_quadratic_family_second_boundary_zero_density_third_order
```

The replay enumerates only degree multisets through `h=40`.  It enumerates no
polynomial, irreducible, residue class, field element, curve, point, or zero.
