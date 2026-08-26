# Frobenius interferometry: exact compact-subgroup selectors

**Status:** exact compact-group theorem and complete bounded classification.

**Scope:** the standard four-dimensional representation of `USp(4)`, raw
trace interferometers of total frequency at most ten, one full-rank and two
rank-one proper subgroup images, and their uniform tori.  This packet
constructs no finite field,
curve, zero, Euler product, or random sample.

**What was actually run:** sparse integer Laurent algebra, normalized Weyl
constant terms for `C2`, `A1 x A1`, and `A1`, and an exact rational-rank
search over 25 raw observables.  The whole replay is protected by an
exclusive 100,000-accounted-operation cap.

**Smallest next gap:** evaluate the three selectors on a source-faithful
arithmetic family with independently justified monodromy candidates, then
separate finite-field boundary corrections from an actual subgroup signal.

## 1. The observable and the correction to the moonshot

Let a normalized `USp(4)` torus element have eigenvalues

\[
 x,x^{-1},y,y^{-1},
\]

and put

\[
 p_r(U)=\operatorname{Tr}(U^r)
       =x^r+x^{-r}+y^r+y^{-r},
 \qquad
 I_{r,s}=p_rp_s-p_{r+s}.                                  \tag{1}
\]

The phrase “vanishes on generic monodromy but survives on a subgroup” must
not mean pointwise vanishing.  A class function that vanishes on every point
of `USp(4)` also vanishes on each subgroup.  The viable statement is instead

\[
 \langle F\rangle_{USp(4)}=0,
 \qquad
 \langle F|_H\rangle_H\ne0,                               \tag{2}
\]

where the brackets are normalized Haar means.  Thus “ambient projection” in
this packet always means the projection onto the **constant**, or trivial
isotypic, component.  It does not mean that every ambient irreducible
projection vanishes.

There is a useful degree-two precursor.  Since

\[
 p_1^2-p_2-2=2\chi_{\omega_2},
 \qquad
 p_1^2+p_2=2\chi_{2\omega_1},                              \tag{3}
\]

the first expression detects the extra invariant in the block-product
restriction, while the second detects the doubled-standard diagonal.  But
both retain nonzero uniform-torus means.  The theorem below cancels those
zero-weight backgrounds as well.

## 2. The three compact images

Besides the ambient group `G=USp(4)`, consider:

1. `H_x = SU(2) x SU(2)`, acting block diagonally as `V_1 direct_sum V_1`;
2. `H_Delta = SU(2)`, embedded by `A -> diag(A,A)`, with torus weights
   `+/-1,+/-1`;
3. `H_3 = Sym^3(SU(2))`, with torus weights `+/-3,+/-1`.

The first is the standard compact endoscopic/product image.  The second is
the diagonal rank drop inside it.  The third is the irreducible
symmetric-cube image.  We also retain the uniform measures on the ambient
maximal torus `T^2` and on the one-dimensional tori of `H_Delta` and `H_3`.
These torus columns distinguish a root-action resonance from a mere
zero-weight count.

The signature order used below is

\[
 (G,H_\times,H_\Delta,H_3,T^2,T_\Delta,T_3).               \tag{4}
\]

## 3. Exact selector theorem

Define three integer virtual trace packets:

\[
\begin{aligned}
 P&=I_{2,2}-I_{4,4},\\
 D&=-I_{1,1}+2I_{1,5}+I_{4,4},\\
 S&=-2I_{2,8}.
\end{aligned}                                               \tag{5}
\]

Then their exact normalized Haar signatures are

\[
\begin{array}{c|rrrrrrr}
 &G&H_\times&H_\Delta&H_3&T^2&T_\Delta&T_3\\ \hline
 P&0&2&0&0&0&0&0\\
 D&0&0&2&0&0&0&0\\
 S&0&0&0&2&0&0&0.
\end{array}                                                 \tag{6}
\]

Thus `(P,D,S)` is an exact subgroup-selector basis for these three images at
the level of Haar means.  All three are invisible not only to the ambient
constant channel but also to the three listed uniform tori.  Their signals
therefore come from how the corresponding roots act, not from torus
zero-weight multiplicity alone.

The ambient `L^2` Gram matrix is

\[
 \left\langle
 \begin{pmatrix}P\\D\\S\end{pmatrix}
 \begin{pmatrix}P&D&S\end{pmatrix}
 \right\rangle_G
 =
 \begin{pmatrix}
 24&-20&4\\
 -20&48&0\\
 4&0&40
 \end{pmatrix}.                                             \tag{7}
\]

Its leading principal minors are `24`, `752`, and `29312`, so the packets
are nonzero and linearly independent in ambient `L^2`.  Equation (7) is also
an honest noise warning: a subgroup mean of two is not a large memberwise
effect, and arithmetic use should retain covariance rather than compare
three isolated sample means.

## 4. Why the resonances occur

Put `q_n(z)=z^n+z^-n`.  Normalized `SU(2)` Haar integration gives the exact
frequency kernel

\[
 \langle q_n\rangle=-\mathbf1_{n=2},
 \qquad
 \langle q_mq_n\rangle
 =2\mathbf1_{m=n}
  -\mathbf1_{m+n=2}
  -\mathbf1_{|m-n|=2}.                                     \tag{8}
\]

For the formal rank-one pullback with weights `+/-a,+/-b`, restriction gives
`p_r=q_(ar)+q_(br)`.  Therefore

\[
\begin{aligned}
 \langle I_{r,s}\rangle_{H_{a,b}}
 ={}&c_{ar,as}+c_{ar,bs}+c_{br,as}+c_{br,bs}\\
    &-m_{a(r+s)}-m_{b(r+s)},                               \tag{9}
\end{aligned}
\]

where `m` and `c` denote the two quantities in (8).  Formula (9), not a
sampled moment table, explains the symmetric-cube selector:

\[
 \langle I_{2,8}\rangle_{H_3}=-1                          \tag{10}
\]

because `3*2=6` and `1*8=8` differ by the `A1` root frequency two.  The
uniform `T_3` mean is zero, so this is a pure Weyl-density/root resonance.
Arbitrary positive `(a,b)` in (9) define a class-function pullback, not
automatically a four-dimensional symplectic representation or an `SU(2)`
subgroup of `USp(4)`.  The two actual embeddings used in the theorem are
precisely `(a,b)=(1,1)` and `(3,1)`.

For the independent block product, (8) similarly reduces to

\[
 \boxed{
 \langle I_{r,s}\rangle_{H_\times}
 =4\mathbf1_{r=s}
  -2\mathbf1_{|r-s|=2}
  +2\mathbf1_{r=s=2}.}                                    \tag{11}
\]

This makes the product selector transparent:
`<I_(2,2)>=6` while `<I_(4,4)>=4`.

For the ambient group the exact Weyl formula is

\[
 \langle f\rangle_G
 ={1\over8}\operatorname{CT}\!\left[
 f\prod_{\alpha\in\{(2,0),(0,2),(1,1),(1,-1)\}}
 (2-X^\alpha-X^{-\alpha})\right].                         \tag{12}
\]

The normalized density has finite nonzero support, up to sign and coordinate
exchange, only at

\[
 (0,0),\ (2,0),\ (4,0),\ (1,1),\ (3,3),\ (3,1),\ (4,2),  \tag{13}
\]

with respective coefficients

\[
 1,-\tfrac14,-\tfrac14,-\tfrac14,-\tfrac14,
 +\tfrac14,+\tfrac18.                                     \tag{14}
\]

Equations (8)--(14) give a short human replay of every entry in (6).

## 5. Complete raw no-go table through total frequency ten

Every odd-total row has zero signature because all seven measures have the
relevant central inversion symmetry.  The nonzero even-total rows are:

| `(r,s)` | `G` | `H_x` | `H_Delta` | `H_3` | `T^2` | `T_Delta` | `T_3` |
|---:|---:|---:|---:|---:|---:|---:|---:|
| `(1,1)` | 2 | 4 | 6 | 2 | 4 | 8 | 4 |
| `(1,3)` | 1 | -2 | -4 | 1 | 0 | 0 | 2 |
| `(2,2)` | 4 | 6 | 8 | 4 | 4 | 8 | 4 |
| `(1,5)` | -1 | 0 | 0 | -1 | 0 | 0 | 0 |
| `(2,4)` | 0 | -2 | -4 | -2 | 0 | 0 | 0 |
| `(3,3)` | 2 | 4 | 8 | 4 | 4 | 8 | 4 |
| `(2,6)` | -1 | 0 | 0 | 2 | 0 | 0 | 2 |
| `(3,5)` | -1 | -2 | -4 | -1 | 0 | 0 | 0 |
| `(4,4)` | 4 | 4 | 8 | 4 | 4 | 8 | 4 |
| `(2,8)` | 0 | 0 | 0 | -1 | 0 | 0 | 0 |
| `(3,7)` | -1 | 0 | 0 | -1 | 0 | 0 | 0 |
| `(4,6)` | -1 | -2 | -4 | -1 | 0 | 0 | 0 |
| `(5,5)` | 4 | 4 | 8 | 4 | 4 | 8 | 4 |

All omitted even rows are identically zero in these seven mean coordinates.
Consequently the only raw `I_(r,s)` with ambient mean zero and a nonzero
named-subgroup mean in this complete cap are

\[
 I_{2,4}\mapsto(0,-2,-4,-2,0,0,0),
 \qquad
 I_{2,8}\mapsto(0,0,0,-1,0,0,0).                         \tag{15}
\]

The first nontrivial raw contrast is therefore `I_(2,4)` at total frequency
six.  The first pure symmetric-cube raw selector is `I_(2,8)` at total
frequency ten.

An exact rational-rank search over all 25 capped raw observables also proves
that the target signatures in (6) require respectively at least two, three,
and one raw supports, even if rational coefficients are allowed.  The
displayed `P` and `D` use the smallest maximum frequency among the recorded
support-minimal witnesses; `S` is the unique one-support witness.

This is a bounded classification, not an all-frequency theorem.  Formula
(9) makes an all-frequency classification for any fixed `H_(a,b)` a finite
Diophantine resonance problem, which is the natural next symbolic extension.

### 5.1 An infinite pure symmetric-cube selector ladder

One all-frequency part of that Diophantine problem is especially clean.  For
every integer in the stated ranges, define

\[
 S_r^+=-2I_{r,3r+2}\quad(r\ge2),
 \qquad
 S_r^-=-2I_{r,3r-2}\quad(r\ge4).                       \tag{15a}
\]

Then both branches have the exact signature

\[
 \boxed{
 \operatorname{sig}(S_r^\pm)=(0,0,0,2,0,0,0).}          \tag{15b}
\]

Thus `I_(2,8)` is the first member of an infinite root-resonance ladder, not
an isolated low-frequency accident.

Here is a complete proof.  In the symmetric-cube pullback, the cross term
`c_(3r,s)` in (9) equals `-1` when `|3r-s|=2`.  At the thresholds in
(15a), every other term in (9) vanishes, so the raw `H_3` mean is `-1`.
Equations (8) and (11) show directly that the block-product and doubled
means vanish: the frequencies are unequal and their difference is neither
zero nor two.

For the ambient group, every exponent in the `C2` Weyl density (12) has
absolute coordinate at most four.  The nonzero exponent types in
`I_(r,s)` are axis frequencies `r+s` and `|r-s|`, and cross frequencies
with absolute coordinates `(r,s)` up to exchange.  On the plus branch these
are already outside the density support for `r>=2`; on the minus branch
they are outside it for `r>=4`.  Hence the ambient constant term is zero.
Finally, the uniform tori see a constant term only at `r=s`, `s=3r`, or
`r=3s`; none occurs in (15a).  This proves (15b).

The executable replays both ladders exactly through base `r=12`; the proof
above supplies the unbounded quantifier.  The earlier uniqueness statement
for `I_(2,8)` remains only the declared `r+s<=10` classification.

## 6. Root-free coefficient adapter

The selectors require no eigenvalue recovery.  Write the normalized local
quartic as

\[
 Z^4-e_1Z^3+e_2Z^2-e_1Z+1.                              \tag{16}
\]

Starting with

\[
 p_0=4,\quad p_1=e_1,\quad p_2=e_1^2-2e_2,\quad
 p_3=e_1^3-3e_1e_2+3e_1,                                 \tag{17}
\]

the exact recurrence

\[
 p_n=e_1p_{n-1}-e_2p_{n-2}+e_1p_{n-3}-p_{n-4}             \tag{18}
\]

computes everything through `p_10`.  The producer exports
`selector_values_from_coefficients(e1,e2)` and tests it on exact rational
reciprocal spectra.  This is the intended adapter for a locked arithmetic
local-factor table; it performs no numerical root finding.

All three selectors are even in `e_1`.  The producer additionally exports
`selector_values_from_squared_first_elementary(A,e2)`, where `A=e_1^2`.
For a normalized genus-two factor coming from
`T^4+aT^3+bT^2+qaT+q^2`, one may therefore substitute

\[
 A={a^2\over q},\qquad e_2={b\over q},                     \tag{19}
\]

entirely in rational arithmetic.  This removes the otherwise artificial
`sqrt(q)` from the adapter while retaining the sign-blindness forced by the
central `USp(4)` symmetry.

## 7. Interpretation and firewalls

If an arithmetic family is independently proved to equidistribute in one of
the three compact images, (6) predicts its limiting selector means.  The
selectors can then help distinguish a product/endoscopic image, a diagonal
rank drop, and a symmetric-cube image even though all sit inside the same
ambient `USp(4)` coefficient space.

What is **not** proved here:

- that any named curve or variety family has one of these monodromy groups;
- that a finite-family mean is close to a compact Haar mean;
- that a large individual selector value identifies an endomorphism or
  correspondence;
- that local agreement across one or several primes supplies a compatible
  system, functorial transfer, or motive; or
- any zero-free region, RH, or GRH statement.

The tori in (6) are controls, not candidate arithmetic monodromy groups.  A
zero torus mean plus a nonzero subgroup mean records sensitivity to the Weyl
density—the root operators missing from uniform torus averaging.  It does
not make the selector positive, deterministic, or memberwise diagnostic.

Replay with:

```text
python research/l-families/atlas/function_field/frobenius_interferometry_subgroup_selectors.py --check
python -m unittest tests.test_frobenius_interferometry_subgroup_selectors -v
python -O -m unittest tests.test_frobenius_interferometry_subgroup_selectors -v
```
