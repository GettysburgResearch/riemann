# L-32706 — The Q=4 unweighted inverse source has only a fifteen-contact negative collar

Claim ID: `L-32706`  
Title: The Euler–Blaschke Q=4 inverse source has an explicit base-four staircase carry potential; every split whose smaller child is at least sixteen has strictly positive source charge, and every negative charge is either `-1` or `-4`  
Status: **PROPOSED COMPLETE EXACT FINITE THEOREM — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-09  
Dependencies: PR #325 `L-32404`; elementary divisor-prefix/carry algebra  
Scope: exact geometry of the unweighted source omitted by logarithmic moments; no global reflected recurrence or RH conclusion

## 1. Q=4 inverse source

Retain the Euler–Blaschke source of PR #325,

\[
 b_4=\mu*e_4,
\tag{L-32706.1}
\]

where

\[
 e_4(1)=1,
 \qquad
 e_4(4^r)=-3\quad(r\ge1),
\tag{L-32706.2}
\]

and all other coefficients vanish. Equivalently,

\[
 \mathbf1*b_4=e_4.
\tag{L-32706.3}
\]

This is the unweighted inverse-source coordinate which is absent from the first and second logarithmic moments of the generalized Selberg system.

## 2. Exact base-four staircase potential

Define the divisor prefix

\[
 D_4(x)
 =\sum_{q\le x}b_4(q)\left\lfloor\frac{x}{q}\right\rfloor,
 \qquad x\in\mathbb Z_{\ge0}.
\tag{L-32706.4}
\]

Finite divisor switching and (L-32706.3) give

\[
 D_4(x)=\sum_{m\le x}e_4(m).
\tag{L-32706.5}
\]

Hence

\[
 \boxed{D_4(0)=0,}
\tag{L-32706.6}
\]

and, for every integer `x>=1`,

\[
 \boxed{
 D_4(x)=1-3\lfloor\log_4x\rfloor.
 }
\tag{L-32706.7}
\]

No Möbius coefficient remains in this coordinate.

## 3. Complete split-charge formula

For a nontrivial integer split

\[
 n=j+k,
 \qquad j,k\ge1,
\]

put

\[
 r=\lfloor\log_4n\rfloor,
 \qquad
 a=\lfloor\log_4j\rfloor,
 \qquad
 c=\lfloor\log_4k\rfloor.
\tag{L-32706.8}
\]

The source carry charge is

\[
 Y_4(n,j)
 =D_4(n)-D_4(j)-D_4(k).
\tag{L-32706.9}
\]

Substitution of (L-32706.7) gives the exact closed form

\[
 \boxed{
 Y_4(n,j)=3(a+c-r)-1.
 }
\tag{L-32706.10}
\]

Thus every nontrivial source charge is congruent to `-1 mod 3`.

The trivial endpoint splits `j=0,n` have charge zero, as they should, by (L-32706.6).

## 4. The larger child loses at most one base-four level

By symmetry assume

\[
 1\le j\le k.
\]

Then

\[
 k\ge\frac n2.
\]

Since `n>=4^r`,

\[
 k\ge2\,4^{r-1}.
\]

Therefore, whenever `r>=1`,

\[
 \boxed{c\in\{r-1,r\}.}
\tag{L-32706.11}
\]

This one-level fact completely localizes the negative sector.

## 5. Every negative split has smaller child at most fifteen

Suppose

\[
Y_4(n,j)<0.
\]

By (L-32706.10), since the parenthetical quantity is integral,

\[
a+c-r\le0.
\tag{L-32706.12}
\]

Using `c>=r-1` from (L-32706.11),

\[
a\le1.
\]

Hence

\[
 \boxed{j<4^2=16.}
\tag{L-32706.13}
\]

By symmetry,

\[
 \boxed{
 Y_4(n,j)<0
 \quad\Longrightarrow\quad
 \min(j,n-j)\le15.
 }
\tag{L-32706.14}
\]

Thus the complete negative unweighted source is a fixed fifteen-contact collar, independent of parent scale.

## 6. Exact negative values

The same argument gives the complete table.

### Large child remains in the parent level

If

\[
c=r,
\]

then negativity requires `a=0`, so `1<=j<=3`, and

\[
 \boxed{Y_4(n,j)=-1.}
\tag{L-32706.15}
\]

### Large child drops one level

If

\[
c=r-1,
\]

then:

- `a=0`, i.e. `1<=j<=3`, gives
  \[
  \boxed{Y_4(n,j)=-4;}
  \tag{L-32706.16}
  \]
- `a=1`, i.e. `4<=j<=15`, gives
  \[
  \boxed{Y_4(n,j)=-1.}
  \tag{L-32706.17}
  \]
- `a>=2` gives a positive charge.

Therefore

\[
 \boxed{
 Y_4(n,j)<0
 \Longrightarrow
 Y_4(n,j)\in\{-4,-1\}.
 }
\tag{L-32706.18}
\]

In particular,

\[
 \boxed{|Y_4(n,j)|\le4\quad\text{on the complete negative sector}.}
\tag{L-32706.19}
\]

## 7. Uniform positive interior

If both children are at least sixteen, then

\[
a\ge2,
\]

and (L-32706.11) gives

\[
a+c-r\ge1.
\]

Consequently

\[
 \boxed{
 \min(j,n-j)\ge16
 \quad\Longrightarrow\quad
 Y_4(n,j)\ge2.
 }
\tag{L-32706.20}
\]

This is stronger than a fixed balanced-cone theorem: the source is favorable on every nontrivial split outside a scale-independent endpoint collar.

As an immediate corollary, if

\[
n\ge64,
\qquad
\frac n4\le j\le\frac{3n}{4},
\]

then both children are at least sixteen and therefore

\[
 \boxed{Y_4(n,j)\ge2.}
\tag{L-32706.21}
\]

More precisely, if `r=floor(log_4 n)>=3`, quarter balance gives `a,c>=r-1`, hence

\[
Y_4(n,j)\ge3r-7.
\tag{L-32706.22}
\]

The unweighted Q=4 source therefore supplies a growing positive current-scale reserve throughout the cofinal balanced interior.

## 8. Consequence for the live reflected proof graph

PR #302 `L-28013` isolates the unweighted inverse source as the unique boundary coordinate omitted by logarithmic Selberg moments. PR #325 closes, for the Q=4 Euler–Blaschke system:

```text
balanced generalized-prime Selberg reserve;
physical-current to balanced-reserve transference;
real-X one-coefficient collar;
unitary coefficient-one scattering return.
```

The present theorem shows that the unweighted source itself is not a diffuse same-scale obstruction. Its carry image has the exact geometry

```text
cofinal balanced/interior sector     strictly positive;
all negative source charge           min child <= 15;
negative magnitude                   only 1 or 4.
```

Thus any remaining source-convolved reflected boundary theorem may localize every adverse unweighted row to a finite child-size collar. No source-blind large-scale estimate is required for this coordinate.

This does **not** by itself prove that the complete independent-frequency boundary quadratic is a direct sum of these scalar source charges. That source-to-quadratic placement remains a separate algebraic obligation.

## 9. Proof boundary

Closed exactly:

- the base-four staircase divisor potential;
- the complete split-charge formula;
- the one-level theorem for the larger child;
- the fixed fifteen-contact localization of every negative source row;
- the exact negative values `-1,-4`;
- strict positivity on every split with both children at least sixteen;
- cofinal quarter-balanced positivity.

Open:

- the exact placement of this finite collar inside the complete independent-frequency reflected quadratic;
- its homogeneous absorption/routing in the global recurrence;
- RH.
