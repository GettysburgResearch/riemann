# L-91328 — The finite `P_61` forcing retains a uniform positive margin after one new rough least prime

Claim ID: `L-91328`  
Status: **PROPOSED COMPLETE DIRECTED FINITE-BLOCK THEOREM — MULTIPRIME SCALAR TENSORIZATION NOT CLAIMED**  
Created: 2026-08-12  
Depends on: `L-91113`, `L-91317`, `L-91320`, `R-91303`  
RH status: **unproved**

## 1. Finite forcing through `61`

Let

\[
 \mathcal P_{61}
 =\{2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61\},
\]

\[
 P_{61}=\prod_{p\in\mathcal P_{61}}p,
\]

and, for `a in {1,2}`, define

\[
 \boxed{
 F_a(x)=
 \sum_{\substack{d\mid P_{61}\\d\le x}}
 \mu(d)
 \left(\frac{a\sqrt x}{d}-\frac1{\sqrt d}\right).
 }
\tag{L-91328.1}

`L-91320` proves `F_a(x)>0` globally.  The present theorem supplies a fixed
normalized margin on the range where a new rough prime can activate.

## 2. Directed normalized corridor

### Theorem 2.1

For every real `x>=67`,

\[
 \boxed{
 F_1(x)>\frac3{40}\sqrt x,
 \qquad
 F_2(x)>\frac9{100}\sqrt x.
 }
\tag{L-91328.2}

### Finite reduction

Order the `2^18=262144` divisors of `P_61`:

\[
 1=d_1<d_2<\cdots<d_{262144}.
\]

On one activation cell

\[
 d_j\le x<d_{j+1},
\]

put

\[
 A_j=\sum_{i\le j}\frac{\mu(d_i)}{d_i},
 \qquad
 B_j=\sum_{i\le j}\frac{\mu(d_i)}{\sqrt{d_i}}.
\]

Then

\[
 \boxed{
 \frac{F_a(x)}{\sqrt x}
 =aA_j-\frac{B_j}{\sqrt x}.
 }
\tag{L-91328.3
}

This is monotone on the cell.  Hence its minimum occurs at one cell endpoint.
The companion checker evaluates both endpoints, which avoids even having to
decide the sign of the directed enclosure of `B_j`.

It uses:

```text
one exact common denominator P_61 for A_j;
directed inverse-square-root enclosures of denominator 10^50 for B_j;
exact Fraction comparisons at both endpoints of every cell meeting x>=67.
```

It proves all

\[
 1,048,414
\]

endpoint/channel inequalities in (L-91328.2).

The smallest directed excess above `3/40` in the reserve channel occurs at
`x=91` and exceeds

\[
 0.0027554.
\]

The smallest directed excess above `9/100` in the equality channel occurs at
`x=74` and exceeds

\[
 0.0075222.
\]

These decimals are readable summaries; the retained rational lower endpoints
are the proof objects.

## 3. A simple global upper corridor

For one positive atom

\[
 w_a(x,n)=\frac{a\sqrt x}{n}-\frac1{\sqrt n},
\]

adding one finite Euler factor has the form

\[
 G(x)\longmapsto G(x)-p^{-1/2}G(x/p).
\]

`L-91317` proves that every intermediate finite forcing is nonnegative.
Therefore each new factor can only decrease the preceding forcing pointwise.
Starting from

\[
 w_a(x,1)=a\sqrt x-1<a\sqrt x,
\]

one gets

\[
 \boxed{
 0<F_a(x)<a\sqrt x
 \qquad(x>1).
 }
\tag{L-91328.4}

No numerical certificate is needed for this upper bound.

## 4. One new least rough prime

Let `p>=67` be prime.  Adding this one Euler factor to the complete finite block
gives

\[
 \boxed{
 F_{a;p}(x)
 =F_a(x)-p^{-1/2}F_a(x/p),
 \qquad x\ge p.
 }
\tag{L-91328.5}

Using (L-91328.2)--(L-91328.4),

\[
 F_{1;p}(x)
 >\left(\frac3{40}-\frac1p\right)\sqrt x,
\]

and

\[
 F_{2;p}(x)
 >\left(\frac9{100}-\frac2p\right)\sqrt x.
\]

At the worst prime `p=67`, the exact comparisons are

\[
 \frac3{40}-\frac1{67}
 =\frac{161}{2680}
 >\frac3{50},
\tag{L-91328.6}
\]

\[
 \frac9{100}-\frac2{67}
 =\frac{403}{6700}
 >\frac3{50}.
\tag{L-91328.7}

Hence

\[
 \boxed{
 F_{a;p}(x)>\frac3{50}\sqrt x
 \qquad
 (a=1,2;\ p\ge67;\ x\ge p).
 }
\tag{L-91328.8}

The finite small-prime forcing therefore retains a fixed positive reserve after
one new rough least-prime transition.

## 5. Reset interpretation

In the factor-54 architecture, a nontrivial rough least prime satisfies

\[
 x/p<c_0x.
\]

Thus one rough prime is processed before its branch enters the next reset
generation.  Equation (L-91328.8) is exactly aligned with that one-prime-per-reset
structure:

```text
finite block through 61;
one new least rough prime;
strict positive forcing margin;
then scale contraction into the next generation.
```

The margin is large enough to absorb any fixed finite-window perturbation which
is smaller than `3 sqrt(x)/50` in the same normalized channel.  The finite
mismatch and terminal collars are already much smaller at their declared scale.

## 6. Distinct-prime scope firewall

This theorem does not assert positivity of an independent scalar product over
two or more distinct new rough primes inside one generation.

`R-91303` proves that the native endpoint port itself has a negative mixed
`(67,71)` detail.  Distinct-prime composition is governed instead by:

```text
the positive four-state semigroup of L-91327;
the common Hilbert colligation of L-91326;
and one local parity projection at each reset boundary.
```

Equation (L-91328.8) supplies the robust scalar forcing at one transition; it is
not a tensorization theorem.

## 7. Verification

Retained verdict:

```text
PASS_P61_ONE_ROUGH_PRIME_MARGIN
```

The standard-library checker certifies:

```text
262,144 activation cells;
1,048,414 directed endpoint/channel gates;
reserve normalized lower bound 3/40;
equality normalized lower bound 9/100;
the two exact 3/50 one-prime margins.
```

## 8. Proof boundary

```text
P_61 normalized reserve corridor                DIRECTED EXACT
P_61 normalized equality corridor               DIRECTED EXACT
global upper corridor F_a<a sqrt(x)             EXACT
one new p>=67 forcing margin >3sqrt(x)/50        EXACT
one-prime-per-reset compatibility                EXACT SUPPORT LOGIC
distinct-prime scalar tensorization              NOT CLAIMED / REFUTED ELSEWHERE
positive four-state multiprime state             AVAILABLE
all-generation parity/endpoint ledger            OPEN / RH-BEARING
Riemann Hypothesis                               UNPROVEN
```
