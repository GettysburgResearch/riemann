# Genus-two repeated-factor tomography

**Status:** exact local-polynomial theorem plus a bounded, source-locked
finite census.

**Scope:** the algebraic theorem applies to every positive integer `q` and
every integral reciprocal coefficient pair `(a,b)`. The arithmetic census is
only for the complete monic squarefree quintic histograms at `q=3,5,7`. The
selector analysis covers the full real repeated-factor compact line. No
finite field, polynomial, curve, orbit, or member is enumerated here.

This is a theorem about a local polynomial and its factorization. It does
**not** identify a split Jacobian, an isogeny, an endomorphism algebra, extra
automorphisms, a monodromy subgroup, a geometric substack, or a compatible
global system.

## 1. The repeated-cosine certificate is exactly a square criterion

Use the repository's low-degree coefficient convention

\[
 P(T)=1+aT+bT^2+qaT^3+q^2T^4
\]

and set

\[
 \Delta=a^2-4b+8q,\qquad G=\Delta/q.
\]

Then

\[
 \boxed{
 G=0
 \quad\Longleftrightarrow\quad
 P(T)=(1-rT+qT^2)^2\text{ for a unique }r\in\mathbb Z.
 }
\]

The parity step is part of the theorem, not an empirical side condition. If
`Delta=0`, then

\[
 a^2=4(b-2q),
\]

so `4` divides `a^2`, hence `a` is even. Put `r=-a/2`. The same identity
gives `b=r^2+2q`, and direct multiplication yields

\[
 (1-rT+qT^2)^2
 =1-2rT+(r^2+2q)T^2-2qrT^3+q^2T^4=P(T).
\]

Conversely, comparing the first two coefficients of this square gives
`a=-2r`, `b=r^2+2q`, and therefore `Delta=0`.

This also closes the relation to the pre-existing integral `+q`
elliptic-form factorization predicate. That packet writes

\[
 P(T)=(1-rT+qT^2)(1-sT+qT^2),\qquad
 \Delta=(r-s)^2.
\]

Thus `G=0` is exactly its diagonal `r=s` sublocus. Here and below,
“elliptic-form” means only the displayed reciprocal quadratic shape. A Hasse
inequality is checked when asserted, but no curve-realization theorem is
being imported.

The normalized monic convention is

\[
 Q(Z)=Z^4-e_1Z^3+e_2Z^2-e_1Z+1.
\]

On the square locus, write

\[
 Q(Z)=(Z^2-2xZ+1)^2,\qquad -1\leq x\leq1,\qquad z=x^2.
\]

Then

\[
 e_1^2=16z,\qquad e_2=2+4z,qquad
 z={r^2\over4q}\in[0,1].
\]

This identifies the earlier repeated-cosine certificate with the exact
integral repeated-factor predicate in the present arithmetic setting.

## 2. Exact selector tomography on the full compact line

Substitution of `e1^2=16z`, `e2=2+4z` into the locked root-free selector
adapter gives

\[
\begin{aligned}
 P(z)&=-32z(z-1)(4z-1)(4z-3),\\
 D(z)&=8(4z-1)h(z),
 &h(z)&=16z^3-20z^2+7z-2,\\
 S(z)&=-8(2z-1)k(z),
 &k(z)&=256z^4-512z^3+336z^2-80z+3.
\end{aligned}
\]

These are identities in `Z[z]`; the producer multiplies the factors and
compares every coefficient with the direct adapter substitution.

### The `P` chambers

The zeros are `0,1/4,3/4,1`. Therefore

- `P>0` on `(0,1/4)` and `(3/4,1)`;
- `P<0` on `(1/4,3/4)`; and
- `P=0` at the four displayed points.

### The `D` chambers

The cubic discriminant of `h` is exactly `-13360`, so `h` has one real root,
call it `rho_D`. Exact endpoint evaluation gives

\[
 h(11/12)=-7/108,
 \qquad h(12/13)=10/2197,
\]

hence

\[
 11/12<\rho_D<12/13.
\]

It follows that

- `D>0` on `[0,1/4)` and `(rho_D,1]`;
- `D<0` on `(1/4,rho_D)`; and
- `D=0` at `1/4` and `rho_D`.

### The `S` chambers

The symmetry is exposed exactly by

\[
 k((1+y)/2)=16y^4-12y^2-1.
\]

Define

\[
 \alpha={1-\sqrt{(3+\sqrt{13})/8}\over2},
 \qquad
 \beta={1+\sqrt{(3+\sqrt{13})/8}\over2}=1-\alpha.
\]

These are the two real zeros of `k`; the other two roots are nonreal. Exact
isolation gives

\[
 1/25<\alpha<1/20,
 \qquad 19/20<\beta<24/25,
\]

with

\[
 k(1/25)=119331/390625,
 \qquad k(1/20)=-139/625.
\]

Consequently

- `S>0` on `[0,alpha)` and `(1/2,beta)`;
- `S<0` on `(alpha,1/2)` and `(beta,1]`; and
- `S=0` at `alpha,1/2,beta`.

Thus none of the three selectors has a fixed sign on the full repeated-factor
compact line.

## 3. The locked `q=3,5,7` census

An atom here is one signed `(a_D,b_D)` coefficient state. Member weights are
the uniform monic-squarefree-quintic weights inherited unchanged from the
locked histogram.

| `q` | repeated signed atoms | repeated members | fraction of full family | compact `z` member law |
|---:|---:|---:|---:|---|
| 3 | 0 | 0 | `0` | empty |
| 5 | 3 | 15 | `3/500` | `z=0: 5`, `z=1/5: 10` |
| 7 | 3 | 84 | `2/343` | `z=0: 42`, `z=1/7: 42` |

The complete repeated signed atoms are

| `q` | `(a_D,b_D)` | members | repeated trace `r` | factor |
|---:|---:|---:|---:|---|
| 5 | `(-4,14)` | 5 | 2 | `(1-2T+5T^2)^2` |
| 5 | `(0,10)` | 5 | 0 | `(1+5T^2)^2` |
| 5 | `(4,14)` | 5 | -2 | `(1+2T+5T^2)^2` |
| 7 | `(-4,18)` | 21 | 2 | `(1-2T+7T^2)^2` |
| 7 | `(0,14)` | 42 | 0 | `(1+7T^2)^2` |
| 7 | `(4,18)` | 21 | -2 | `(1+2T+7T^2)^2` |

All have `r^2<=4q`. The source supports contain only

\[
 z\in\{0,1/5,1/7\}\subset[0,1/4),
\]

which is the first exact `D`-positive chamber. This explains the earlier
finite observation that every `G=0` member at `q=5,7` has `D>0`: it is a
support fact, not a universal implication.

At the nonzero support values,

\[
\begin{array}{c|ccc}
z&P&D&S\\ \hline
1/5&1408/625&1272/625&-48696/3125\\
1/7&9792/2401&11208/2401&-284040/16807.
\end{array}
\]

At `z=0`, the values are `(P,D,S)=(0,16,24)`.

## 4. Sharp no-go for universal `D>0`

The integral Hasse-admissible square

\[
 (1-4T+5T^2)^2
 =1-8T+26T^2-40T^3+25T^4
\]

has `q=5`, `r=4`, `G=0`, and `z=4/5`. Nevertheless,

\[
 D(4/5)=-11088/625<0.
\]

It is absent from the locked genus-two family support, but it lies inside the
same integral Hasse-admissible local-polynomial locus. This is the promised
counterexample: repeated factorization alone does not force positive `D`.
No geometric realization is asserted for this control polynomial.

## 5. Provenance and replay

The producer authenticates, before parsing or dynamic execution:

- the frozen histogram, its producer, coefficient arithmetic, and affine
  action;
- the prior zero-geometry fixture, producer, and note;
- the root-free selector producer and note; and
- the integral `+q` split-locus fixture, producer, and note.

It then checks all three canonical payload hashes, the complete member-ledger
hashes, exact coverage markers, atom counts, member masses, and agreement of
the repeated census across the three packets. Exactly `251` source atoms are
visited under an inclusive cap of `4096`. There is no root finding, random
sampling, or floating-point arithmetic.

Replay from the repository root:

```text
python research/l-families/atlas/function_field/genus2_repeated_factor_tomography.py --check
python -m unittest tests.test_genus2_repeated_factor_tomography -v
python -O -m unittest tests.test_genus2_repeated_factor_tomography -v
```
