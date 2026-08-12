# L-91330 — One rough Euler factor is a canonical contracted child plus positive square-root slack

Claim ID: `L-91330`  
Status: **PROVED EXACT ONE-PRIME RESET IDENTITY — MULTIPRIME TENSORIZATION NOT USED**  
Created: 2026-08-12  
Depends on: `L-91317`, `R-91303`  
RH status: **unproved**

## 1. The positive parity atom

For `a>0`, real `x>=1`, and integer `n<=x`, put

\[
 w_a(x,n)=\frac{a\sqrt x}{n}-\frac1{\sqrt n}.
\tag{L-91330.1}
\]

Let `p` be prime and write

\[
 r=p^{-1/2},
 \qquad
 B_p=1-r.
\]

## 2. Canonical-child decomposition

If `pn<=x`, then

\[
\boxed{
\begin{aligned}
 w_a(x,n)-w_a(x,pn)
 ={}&B_p\,w_a(x/p,n)\\
 &+aB_p\frac{\sqrt x}{n}.
\end{aligned}}
\tag{L-91330.2}
\]

Indeed, the right side is

\[
 B_p\left(\frac{ar\sqrt x}{n}-\frac1{\sqrt n}\right)
 +aB_p\frac{\sqrt x}{n}
 =\frac{a(1-r^2)\sqrt x}{n}
  -\frac{1-r}{\sqrt n},
\]

which is exactly the left side.

Both terms in (L-91330.2) are nonnegative. The first is the **same parity atom
at the canonical child endpoint `x/p`**. The second is a pure positive
square-root-mode slack.

This refines `L-91317.2`, whose equivalent positive dilation used the parameter
`x(1+r)^2`. The new form is adapted to recursive reset because its child is
located at the actual contracted endpoint.

## 3. Truncated positive source identity

Let `nu(n)>=0` be finitely supported and define

\[
 \mathcal E_{p,a}[\nu](x)
 =\sum_{n\le x}\nu(n)w_a(x,n)
  -\sum_{n\le x/p}\nu(n)w_a(x,pn).
\tag{L-91330.3}
\]

Splitting at `x/p` and applying (L-91330.2) gives

\[
\boxed{
\begin{aligned}
 \mathcal E_{p,a}[\nu](x)
 ={}&B_p
   \sum_{n\le x/p}\nu(n)w_a(x/p,n)\\
 &+aB_p\sqrt x
   \sum_{n\le x/p}\frac{\nu(n)}n\\
 &+\sum_{x/p<n\le x}\nu(n)w_a(x,n).
\end{aligned}}
\tag{L-91330.4}

Every term is positive.

Thus one rough factor has exactly three destinations:

```text
canonical contracted child at endpoint x/p;
positive square-root slack;
positive activation frontier.
```

No projective sign conversion and no colored finite column is present in this
identity.

## 4. Factor-54 routing

For every rough prime `p>=67`,

\[
 \frac xp<c_0x.
\]

Hence the first term of (L-91330.4) enters the next factor-54 generation. Split
the frontier as

\[
 x/p<n\le c_0x
 \qquad\text{and}\qquad
 c_0x<n\le x.
\]

The first slice is contracted and the second lies in the already constructed
outer packing. The harmonic slack is positive and belongs to the square-root
mode whose finite Boolean and endpoint Schur reservoirs are already explicit in
`L-91316/L-91320`.

Therefore one rough prime can be processed completely before the next rough
prime is introduced.

## 5. Why this avoids the tensorization firewall

`R-91303` proves that independent scalar one-prime endpoint ports do not
multiply to a positive multiprime scalar detail. Equation (L-91330.4) does not
multiply such ports.

Instead, after each prime:

1. the canonical child is passed to the next contracted generation;
2. the local parity projection is applied there;
3. the positive harmonic slack and frontier are paid immediately;
4. only then is the next least rough prime processed.

Thus every root-to-leaf path contains at most one unprojected rough factor at a
time. Distinct-prime products are represented by sequential reset generations,
not by a tensor product of scalar endpoint ports.

## 6. Iterated finite-tree form

For a finite ordered rough-prime path

\[
 p_1<p_2<\cdots<p_k,
\]

repeated use of (L-91330.4), with a parity projection after every step, leaves
one canonical terminal child at endpoint

\[
 \frac{x}{p_1\cdots p_k}
\]

with coefficient

\[
 \prod_{j=1}^k(1-p_j^{-1/2})\le1,
\]

plus a finite sum of positive square-root slacks and positive frontiers.

This statement is pathwise. Parallel least-prime branches still require the
source-partition/one-use target ledger of `L-91329`; no scalar sum of the path
coefficients is asserted.

## 7. Score orientation

The canonical child coefficient `B_p` is less than one. Embedding the child
packing at its native contracted endpoint therefore cannot multiply inherited
score loss by a factor larger than one. The positive harmonic slack and frontier
have nonnegative score, while the local parity and butterfly corrections are
score-favorable.

The stronger affine score amplification of `L-91318` remains available but is
not needed for this one-prime reset identity.

## 8. Proof boundary

```text
one active rough factor -> canonical child + slack      EXACT
truncated positive-source identity                       EXACT
child endpoint x/p and factor-54 contraction             EXACT
positive harmonic/frontier channels                      EXACT
one-prime-per-generation pathwise reset                   EXACT
avoidance of scalar port tensorization                    EXACT
parallel least-prime source/target partition              OPEN
all-generation endpoint-measure ledger                    OPEN / RH-BEARING
Riemann Hypothesis                                        UNPROVEN
```
