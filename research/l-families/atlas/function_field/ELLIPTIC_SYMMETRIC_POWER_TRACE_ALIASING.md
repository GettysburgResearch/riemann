# Elliptic symmetric-power scalar-trace aliasing

## Status and scope

Let an elliptic Frobenius pair satisfy

\[
 \alpha+\beta=t,\qquad \alpha\beta=q,
\]

and put

\[
 \tau_m(t;q)=\operatorname {Tr}(\operatorname {Sym}^m)=
 \sum_{i=0}^m\alpha^{m-i}\beta^i.
\]

This packet proves an exact classification of certain **scalar trace** fibers
over the integers. It does not classify equality of the full degree-`m+1`
local factors. That distinction matters: most scalar aliases below are split
by a higher coefficient, while one special sign pair has the same full
factor.

The finite tables are deterministic transforms of the source-locked
genus-one model/stack trace histograms for `q=3,5,7,11,13`. No curve or field
is enumerated here. All arithmetic is integral, with no floats, randomness,
or interpolation.

## 1. The recurrence and closed form

Write `E_m(t,q)=tau_m(t;q)`. The complete symmetric functions in `alpha,beta`
satisfy

\[
 E_0=1,\qquad E_1=t,\qquad
 E_m=tE_{m-1}-qE_{m-2}.                                    \tag{1}
\]

Equivalently,

\[
 \boxed{E_m(t,q)=\sum_{j=0}^{\lfloor m/2\rfloor}
 (-1)^j{m-j\choose j}q^jt^{m-2j}.}                         \tag{2}
\]

This is the Dickson polynomial of the second kind in the convention fixed by
(1). It is odd in `t` for odd `m` and even in `t` for even `m`.

## 2. Integer collision theorem

### Theorem

For every odd integer `q` and all \(x,y\in\mathbf Z\):

\[
 \boxed{m\equiv1,3\pmod6\quad\Longrightarrow\quad
 E_m(x,q)=E_m(y,q)\iff x=y,}                                \tag{3}
\]

and

\[
 \boxed{m\equiv2\pmod6\quad\Longrightarrow\quad
 E_m(x,q)=E_m(y,q)\iff x=\pm y.}                            \tag{4}
\]

The proof uses only that `q` is odd. In the elliptic application, `q` is a
positive odd prime power. No Hasse bound is needed for (3)--(4).

### 2.1 Collision quotients

Let

\[
 H_n(x,y)=\frac{x^{n+1}-y^{n+1}}{x-y}
          =\sum_{i=0}^n x^{n-i}y^i.                         \tag{5}
\]

For `m=2r+1`, divide the difference by `x-y` and index (2) by the
remaining odd exponent `2s+1`:

\[
 Q_{2r+1}(x,y)=
 \sum_{s=0}^r(-1)^{r-s}{r+s+1\choose2s+1}
 q^{r-s}H_{2s}(x,y).                                        \tag{6}
\]

For `m=2r`, evenness permits division by `x^2-y^2`:

\[
 R_{2r}(x,y)=
 \sum_{s=0}^{r-1}(-1)^{r-s-1}{r+s+1\choose2s+2}q^{r-s-1}
 \sum_{i=0}^s x^{2(s-i)}y^{2i}.                             \tag{7}
\]

These formulas are polynomial identities, including on the diagonals where
the displayed rational notation for the quotient would otherwise be
undefined.

### 2.2 The 12-residue parity table

Reduce modulo `2`, so `q=1`. Put

\[
 A_r(z)=E_{2r+1}(t,1)/t,\qquad F_r(z)=E_{2r}(t,1),\quad z=t^2.
\]

Then

\[
 A_0=1,\ A_1=z,\qquad F_0=1,\ F_1=z+1,
\]

and both sequences obey

\[
 P_r=zP_{r-1}+P_{r-2}\quad\text{over }\mathbf F_2.          \tag{8}
\]

Off the diagonal, quotient values are differences of the values at `z=0,1`.
On the diagonal they are formal derivatives. Tracking value and derivative
in (8) is a finite recurrence; its state returns after 12 steps.

The table is indexed by **`r mod 12`**, with `m=2r+1` in the odd column and
positive `m=2r` in the even column. This qualification is load-bearing: the
even table has period 12 in `r`, hence period 24 in `m`, not period 12 in
`m`. Entries are quotient values at parities `(00,01,10,11)`.

| `r mod 12` | odd quotient | odd target? | even quotient | even target? |
|---:|:---:|:---:|:---:|:---:|
| 0  | 1111 | yes | 0000 | no |
| 1  | 0111 | yes | 1111 | yes |
| 2  | 1000 | no  | 1001 | no |
| 3  | 0111 | yes | 0001 | no |
| 4  | 1111 | yes | 0111 | yes |
| 5  | 0000 | no  | 1000 | no |
| 6  | 1111 | yes | 1000 | no |
| 7  | 0111 | yes | 0111 | yes |
| 8  | 1000 | no  | 0001 | no |
| 9  | 0111 | yes | 1001 | no |
| 10 | 1111 | yes | 1111 | yes |
| 11 | 0000 | no  | 0000 | no |

The odd target condition is `r=0,1 mod 3`, equivalent to
`m=1,3 mod 6`. The even target condition is `r=1 mod 3`, equivalent to
`m=2 mod 6`. Every zero in a target row is therefore `(x,y)=(0,0)` modulo
`2`; some target rows have no parity root at all. Thus a putative nontrivial
integer collision in (3) or (4) forces

\[
 x=2X,\qquad y=2Y.                                          \tag{9}
\]

### 2.3 The unique least 2-adic term: odd case

After (9), the `s`-th term of (6) contains

\[
 {r+s+1\choose2s+1}q^{r-s}2^{2s}H_{2s}(X,Y).                \tag{10}
\]

The `s=0` constant is `(-1)^r(r+1)q^r`. For `s>=1`, write the binomial
numerator as the interval

\[
 [r-s+1,r+s+1],                                             \tag{11}
\]

which contains `r+1`. Removing that factor and using Legendre's formula

\[
 v_2((2s+1)!)=2s+1-\operatorname {popcount}(2s+1)            \tag{12}
\]

shows that the coefficient in (10) exceeds the constant's valuation by

\[
 v_2(\text{other interval factors})+
 \operatorname {popcount}(2s+1)-1.                          \tag{13}
\]

Since the odd integer `2s+1>=3` cannot be a power of two, its popcount is at
least `2`. Every higher term has at least one extra factor of `2`, regardless
of `X,Y`. Hence the constant is the unique term of least 2-adic valuation,
and `Q_{2r+1}(2X,2Y)` cannot vanish.

### 2.4 The unique least 2-adic term: even case

After (9), the `s`-th term of (7) contains

\[
 {r+s+1\choose2s+2}q^{r-s-1}2^{2s}.                         \tag{14}
\]

The `s=0` constant is
`(-1)^(r-1) binom(r+1,2)q^(r-1)`. The numerator interval

\[
 [r-s,r+s+1]                                                \tag{15}
\]

contains the adjacent factors `r(r+1)`. After removing them, the valuation
margin for `s>=1` is

\[
 v_2(\text{remaining interval factors})+
 \operatorname {popcount}(2s+2)-1.                          \tag{16}
\]

This is positive unless `2s+2` is a power of two. In that exceptional case,
the interval has length `2s+2>=4` and therefore contains at least two even
integers. Only one of `r,r+1` is even, so an even factor remains; (16) is
again at least `1`. Thus `R_{2r}(2X,2Y)` cannot vanish.

Equations (6)--(16) prove (3)--(4). The cases `m=1` and `m=2` simply have a
constant quotient and require no higher-term argument.

## 3. Sharp complementary congruence classes

The omitted positive residue classes `m=4,5,0 mod 6` really do admit
collisions. For any `k>=0`, set

\[
 q=3^{2k+1},\qquad t=3^{k+1},\qquad t^2=3q.                 \tag{17}
\]

These integers satisfy Hasse's inequality because `t^2=3q<=4q`. Directly
from (1),

\[
 (E_0,E_1,E_2,E_3,E_4,E_5)(t,q)
 =(1,t,2q,qt,q^2,0),                                        \tag{18}
\]

and

\[
 E_{m+6}(t,q)=-q^3E_m(t,q).                                 \tag{19}
\]

At `t=0`, odd terms vanish and `E_{2j}(0,q)=(-q)^j`. It follows that

\[
 \boxed{E_m(0,q)=E_m(3^{k+1},q)
        \quad(m\equiv4,5,0\pmod6).}                         \tag{20}
\]

Equation (17) provides Hasse-admissible trace integers. This packet does not
infer curve realization from the Hasse inequality alone. The one realization
claim made here is source-backed: at `q=3`, the locked genus-one histogram has
positive mass at `t=0,+3,-3`. Hence (20) is an actual collision inside that
locked family for every complementary `m`.

Through `m=18`, the expected-domain quotient has exactly these extra `q=3`
fibers:

- `m=4`: scalar `9`, classes `0,3`;
- `m=5`: scalar `0`, classes `-3,0,3`;
- `m=6`: scalar `-27`, classes `0,3`, and scalar `13`, classes `1,2`;
- `m=10,12,16,18`: the classes `0,3`;
- `m=11,17`: the classes `-3,0,3`.

There are no extra fibers after the expected quotient in the frozen
`q=5,7,11,13` supports through `m=18`. These last statements are finite
source-locked observations, not all-`q` theorems.

## 4. Scalar equality versus full-factor equality

Let

\[
 P_{m,t,q}(T)=\det(1-\operatorname {Sym}^m(\mathrm{Frob})T).
\]

Its first coefficient is `-tau_m(t;q)`, but equality of that one coefficient
does not imply equality of `P_{m,t,q}`. The producer independently rebuilds
the whole factor from root power sums and Newton identities:

\[
 \sum_{i=0}^m(\alpha^{m-i}\beta^i)^j
 =E_m(\alpha^j+\beta^j,q^j).                                \tag{21}
\]

### 4.1 The constructed zero/nonzero aliases are split

For the pair in (17), compare the second root power sum. Write

\[
 p_2^{(m)}(u;q)=\sum_{i=0}^m(\alpha^{m-i}\beta^i)^2
               =E_m(u^2-2q,q^2),
 \qquad \alpha+\beta=u,\quad\alpha\beta=q.
\]

At `u=0`, the base second power sum is `-2q`, whereas at `u^2=3q`
it is `q`. Hence

\[
 p_2^{(m)}(0;q)=(-1)^m(m+1)q^m,\qquad
 p_2^{(m)}(t;q)=q^mU_m(1/2).                                \tag{22}
\]

For every positive `m=4,5,0 mod 6`, these values differ. Since the scalar
traces agree, the second Newton identity gives different second local-factor
coefficients. Thus the constructed `0` versus nonzero collision is scalar
aliasing, not full-factor aliasing.

The smallest example is `m=4,q=3,t=0,3`. Both scalar traces are `9`, but the
raw second coefficients are respectively `-162` and `81`, or normalized
values `-2` and `1`. The factors are

\[
\begin{aligned}
 P_{4,0,3}(T)&=1-9T-162T^2+1458T^3+6561T^4-59049T^5,\\
 P_{4,3,3}(T)&=1-9T+81T^2-729T^3+6561T^4-59049T^5.
\end{aligned}                                                \tag{23}
\]

### 4.2 The sign nuance

For even `m`, replacing `t` by `-t` negates both base roots but leaves every
Symmetric-`m` eigenvalue unchanged. Therefore the `t` and `-t` full factors
are equal; this is the expected quadratic-twist quotient.

For odd `m=5 mod 6` in (17), there is an additional special symmetry. With
normalized angle `theta=pi/6`, the eigenvalue exponents

\[
 m,m-2,\ldots,-m\pmod {12}
\]

form complete six-cycles, each with equal multiplicity. Adding `6`, which
negates every eigenvalue, preserves the multiset. Thus the `+t` and `-t`
full factors coincide even though odd powers do not normally have the twist
symmetry.

At `q=3,m=5`, all three traces `-3,0,3` have scalar trace zero, but

\[
\begin{aligned}
 P_{5,\pm3,3}(T)&=1+3^{15}T^6,\\
 P_{5,0,3}(T)&=1+3^6T^2+3^{11}T^4+3^{15}T^6.
\end{aligned}                                                \tag{24}
\]

So the full factor separates `0` from the sign pair, while the sign pair
itself remains aliased. The theorem in Section 2 deliberately says nothing
about these full-factor fibers.

### 4.3 An ordinary-looking scalar witness

There is also a less cyclotomic-looking integral example:

\[
 q=31,\qquad x=-7,\qquad y=3,\qquad
 E_5(-7,31)=E_5(3,31)=5544.                                 \tag{25}
\]

Both integers satisfy the Hasse inequality, but this packet imports no trace
realization theorem and therefore does not assert that either is realized by
an elliptic curve. Newton reconstruction gives different full factors; the
stored fixture records both exactly.

## 5. The `m=5` genus-one collision curve

The odd collision quotient at `m=5` is

\[
 3q^2-4q(x^2+xy+y^2)
 +(x^4+x^3y+x^2y^2+xy^3+y^4)=0.                             \tag{26}
\]

Put `H_2=x^2+xy+y^2` and

\[
 z=3q-2H_2.
\]

Using (26) to eliminate `q` gives

\[
 \boxed{z^2=x^4+5x^3y+9x^2y^2+5xy^3+y^4.}                  \tag{27}
\]

The dehomogenized quartic

\[
 X^4+5X^3+9X^2+5X+1
\]

has discriminant `189`, so it is squarefree in characteristic zero and its
smooth projective double-cover model is genus one. The point (25) gives
`H_2=37` and `z=19`, with the right side of (27) equal to `361`.

This curve is recorded as a useful future Diophantine target. The packet does
not determine all of its integral points, infer elliptic-curve realization,
or claim novelty for the model.

## 6. Frozen histogram transforms

The source fixture is locked by all of the following:

- schema;
- canonical payload hash;
- LF-normalized fixture-file hash;
- LF-normalized source-producer hash;
- all five normalization strings, including the sign of the trace and local
  polynomial.

For each `q=3,5,7,11,13` and each `1<=m<=18`, the producer pushes every
locked trace atom through (1), aggregates the scalar-trace histogram, and
then tests injectivity on the expected domain quotient:

- singleton trace classes for odd `m`;
- `t~-t` classes for even `m`.

There are 55 source atoms representing 3,650 models, hence 990 frozen
atom/power transforms. The accounted work, including recurrence rows and
the small Newton diagnostics, stays below an exclusive 2,000-unit cap.

The measure is uniform monic squarefree cubic models, equivalently the
normalized elliptic-moduli-stack measure used by the source packet. It is not
uniform coarse elliptic isomorphism classes.

## 7. Literature and priority boundary

The recurrence (1) is classical Dickson-polynomial/`SU(2)` character
algebra. Relevant prior literature includes:

- Stephen D. Cohen,
  [*Dickson Polynomials of the Second Kind that Are Permutations*](https://doi.org/10.4153/CJM-1994-009-8),
  *Canadian Journal of Mathematics* 46 (1994), 225--238;
- Longjiang Qu and Cunsheng Ding,
  [*Dickson Polynomials of the Second Kind that Permute Z_m*](https://doi.org/10.1137/130942589),
  *SIAM Journal on Discrete Mathematics* 28 (2014), 722--735;
- Phil Martin and Mark Watkins,
  [*Symmetric powers of elliptic curve L-functions*](https://arxiv.org/abs/math/0604095),
  arXiv:math/0604095.

The first two works concern permutation behavior of Dickson polynomials over
finite fields or residue rings, and the third studies elliptic symmetric-power
`L`-functions computationally. This packet makes no originality or priority
claim for the recurrence, its congruence phenomena, the integer theorem, the
genus-one collision model, or the finite transforms. A dedicated literature
search would be required before describing any part as new.

## 8. Exactness and firewall

Exact within this packet:

- the recurrence and binomial form;
- the two collision quotient identities;
- the finite-state parity table and its period certificate;
- the all-`m` 2-adic proof of (3)--(4);
- the sharp Hasse-admissible construction;
- Newton reconstruction for the displayed full-factor diagnostics;
- the `m=5` binary-quartic elimination and discriminant;
- the transforms of all five locked histograms through `m=18`.

Imported:

- the five genus-one trace histograms and their model/stack measure
  interpretation.

Not claimed:

- that scalar-trace equality is the same as full local-factor equality;
- realization of the general Hasse-admissible trace pairs by curves;
- a classification of all complementary collisions or all integral points
  on (27);
- automorphy, a zero-free region, RH, or GRH;
- literature priority.

## 9. Replay contract

From the repository root, run

```text
python research/l-families/atlas/function_field/elliptic_symmetric_power_trace_aliasing.py --check
python -O research/l-families/atlas/function_field/elliptic_symmetric_power_trace_aliasing.py --check
python -m unittest tests.test_elliptic_symmetric_power_trace_aliasing
python -O -m unittest tests.test_elliptic_symmetric_power_trace_aliasing
```

The producer also accepts `--write [PATH]` and `--check [PATH]`; omitting the
path selects the adjacent JSON fixture. Every invariant uses explicit checks,
so optimized mode removes no part of the replay contract.
