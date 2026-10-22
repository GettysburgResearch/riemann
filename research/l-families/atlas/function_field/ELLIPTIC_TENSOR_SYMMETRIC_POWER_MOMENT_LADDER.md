# The tensor/symmetric-power compact moment ladder

## Status and exact scope

This packet proves an exact representation-theoretic theorem for every
integer $r\geq 1$.  It compares the compact trace laws

\[
 X_r=\chi_1(u)\chi_r(v),\qquad
 Y_r=\chi_{2r+1}(w),
 \tag{1}
\]

where $u,v,w$ are Haar elements of $SU(2)$, $u$ and $v$ are independent,
and $\chi_n$ is the character of
$V_n=\operatorname{Sym}^n(\operatorname{Std})$.  Both representations in
(1) have dimension $2r+2$.

The main result is a detector hierarchy:

- the two structured laws have identical moments through degree four;
- they first separate in degree six, for **every** $r\geq1$;
- both already separate in degree four from the standard trace of generic
  $USp(2r+2)$.

The proof is symbolic.  Runtime work is a small exact regression only:
`r <= 16`, tensor degree at most eight, no floats, no random sampling, no
numerical integration, and no runtime CAS.

These are compact Haar laws, not finite-field family moments.  Nothing here
proves equidistribution, monodromy, automorphy, analytic continuation, RH, or
GRH.

## 1. One coefficient formula controls every even moment

Put

\[
 B_k(n)=\dim\left(V_n^{\otimes 2k}\right)^{SU(2)}.
 \tag{2}
\]

The weights of $V_n$ are $n,n-2,\ldots,-n$.  In any even-parity
$SU(2)$-character, the multiplicity of $V_0$ is the multiplicity of
weight zero minus the multiplicity of weight two.  Indeed, every even
irreducible $V_{2j}$ contains each of those weights once when $j>0$,
whereas $V_0$ contains weight zero but not weight two.

Let $P_n(q)=1+q+\cdots+q^n$.  Palindromy exchanges the two adjacent
central coefficients, so the weight difference gives

\[
 \boxed{
 B_k(n)=[q^{kn}](1-q)P_n(q)^{2k}.}
 \tag{3}
\]

Since

\[
 (1-q)P_n(q)^{2k}
 =\frac{(1-q^{n+1})^{2k}}{(1-q)^{2k-1}},
\]

coefficient extraction yields the finite exact formula

\[
 \boxed{
 B_k(n)=
 \sum_{0\leq j\leq\lfloor kn/(n+1)\rfloor}
 (-1)^j {2k\choose j}
 {kn-j(n+1)+2k-2\choose 2k-2}.}
 \tag{4}
\]

Equations (3) and (4) hold for every $n\geq0$ and $k\geq1$.  Thus the
packet contains an all-even-moment law, even though its executable regression
stops at $k=4$.

## 2. Closed formulas through degree eight

Expanding (4) for $k=1,2,3,4$ gives

\[
\begin{aligned}
 B_1(n)&=1,\\
 B_2(n)&=n+1,\\
 B_3(n)&=\frac{(n+1)(n^2+2n+2)}2,\\
 B_4(n)&=\frac{(n+1)(n^2+n+1)(n^2+3n+3)}3.
\end{aligned}
\tag{5}
\]

There is a particularly transparent certificate for the sixth moment.
Clebsch--Gordan gives

\[
 V_n\otimes V_n=\bigoplus_{a=0}^{n}V_{2a}.
 \tag{6}
\]

After grouping six copies into three pairs, an invariant occurs in
$V_{2a}\otimes V_{2b}\otimes V_{2c}$ exactly when $a,b,c$ satisfy the
triangle inequalities, and then with multiplicity one.  Of the
$(n+1)^3$ triples in $[0,n]^3$, exactly
${n+2\choose3}$ violate each one of the three possible triangle
inequalities.  These violations are disjoint.  Hence

\[
 B_3(n)=(n+1)^3-3{n+2\choose3},
 \tag{7}
\]

which is the third line of (5).

For the eighth moment, (4) at $k=4$ is

\[
 {4n+6\choose6}
 -8{3n+5\choose6}
 +28{2n+4\choose6}
 -56{n+3\choose6},
 \tag{8}
\]

with the usual convention that a binomial coefficient vanishes when its
upper entry is smaller than its lower entry.  Writing
${x\choose6}=x(x-1)\cdots(x-5)/720$ in (8), the degree-six terms cancel and
the remainder is

\[
 \frac{n^5+5n^4+11n^3+13n^2+9n+3}{3}
 =\frac{(n+1)(n^2+n+1)(n^2+3n+3)}3.
\]

This is the final line of (5).  The producer separately
checks (5) against both (4) and a Clebsch--Gordan multiplicity recursion; no
displayed factorization is accepted merely because it fits a table.

## 3. Product and principal moments

The standard $SU(2)$ trace has Catalan even moments:

\[
 B_k(1)=C_k=\frac1{k+1}{2k\choose k}.
 \tag{9}
\]

Independence in (1), followed by (2), gives the complete even-moment laws

\[
 \boxed{
 \mathbb E[X_r^{2k}]=C_kB_k(r),\qquad
 \mathbb E[Y_r^{2k}]=B_k(2r+1).}
 \tag{10}
\]

Every odd moment in (10) is zero.  For $X_r$, the factor $\chi_1(u)$
changes sign under $u\mapsto-u$; for $Y_r$, the odd highest weight
$2r+1$ changes sign under $w\mapsto-w$.

Write $s=r+1$.  Substitution in (5) gives the compact table

| degree | independent product $X_r$ | principal slice $Y_r$ |
|---:|---:|---:|
| $0$ | $1$ | $1$ |
| $2$ | $1$ | $1$ |
| $4$ | $2s$ | $2s$ |
| $6$ | $\frac52s(s^2+1)$ | $s(4s^2+1)$ |
| $8$ | $\frac{14}{3}s(s^4+s^2+1)$ | $\frac23s(16s^4+4s^2+1)$ |

The sixth- and eighth-degree gaps factor as

\[
\begin{aligned}
 \mathbb E[Y_r^6]-\mathbb E[X_r^6]
 &=\frac32s(s^2-1)
 =\frac32r(r+1)(r+2),\\
 \mathbb E[Y_r^8]-\mathbb E[X_r^8]
 &=2s(s^2-1)(3s^2+2)\\
 &=2r(r+1)(r+2)(3r^2+6r+5).
\end{aligned}
\tag{11}
\]

Both are positive for every $r\geq1$.  Therefore:

> **Universal first-split theorem.**  The product and principal compact trace
> laws agree in every moment of degree at most four and first differ in
> degree six, for every $r\geq1$.

The matching fourth moment is not a finite coincidence at $r=1,2,3$; it
is the identity $2B_2(r)=B_2(2r+1)=2r+2$.

## 4. The first three locked specializations

The new formulas reproduce three earlier packets without importing their
formulas as premises:

| $r$ | product moments in degrees $0,\ldots,8$ | principal moments |
|---:|---|---|
| 1 | `1,0,1,0,4,0,25,0,196` | `1,0,1,0,4,0,34,0,364` |
| 2 | `1,0,1,0,6,0,75,0,1274` | `1,0,1,0,6,0,111,0,2666` |
| 3 | `1,0,1,0,8,0,170,0,5096` | `1,0,1,0,8,0,260,0,11096` |

The $r=1$ packet had already recorded the split $25$ versus $34$, the
$r=2$ packet the split $75$ versus $111$, and the $r=3$ packet the
split $170$ versus $260$.  Here they become the first three values of
the positive cubic gap in (11).

The all-$r$ subtorus-rigidity predecessor proves that the two monomial
torus parameterizations producing the principal spectrum are exactly

\[
 (|a|,|b|)=(r+1,1)\quad\hbox{or}\quad(1,2).
 \tag{12}
\]

Equation (10) concerns the independent $SU(2)\times SU(2)$ Haar law, not
the correlated one-dimensional subtori in (12).  Thus the moment split is a
measure/monodromy detector; it does not contradict their pointwise spectral
aliases.

## 5. Comparison with generic symplectic trace

Let $Z_g$ be the standard trace of Haar $USp(2g)$, where $g=r+1\geq2$.
The invariant multiplicity in the $2k$-fold standard tensor power is the
number of length-$2k$ oscillating tableaux from the empty partition back to
itself, constrained to partitions of height at most $g$.  Through degree
eight this gives

| rank | $\mathbb E[Z_g^2]$ | $\mathbb E[Z_g^4]$ | $\mathbb E[Z_g^6]$ | $\mathbb E[Z_g^8]$ |
|---:|---:|---:|---:|---:|
| $g=2$ | 1 | 3 | 14 | 84 |
| $g=3$ | 1 | 3 | 15 | 104 |
| $g\geq4$ | 1 | 3 | 15 | 105 |

In the stable range $g\geq k$, every pair contraction is independent and

\[
 \mathbb E[Z_g^{2k}]=(2k-1)!!.
 \tag{13}
\]

Below the stable range, the partition-height constraint—or equivalently the
symplectic Pfaffian relations—accounts for the corrections $14,84,104$.
The executable checker obtains all entries from the oscillating-tableau
recurrence rather than hard-coding the table as its only evidence.

Since both structured fourth moments equal $2g\geq4$, whereas the generic
fourth moment is $3$, the hierarchy is now exact:

1. degree two is blind: all three moments are $1$;
2. degree four detects structured versus generic symplectic behavior;
3. degree six first distinguishes the independent product from the principal
   symmetric-power slice.

There is a polarization caveat.  The invariant form on $V_n$ has sign
$(-1)^n$, so $V_1\otimes V_r$ is symplectic for even $r$ and orthogonal
for odd $r$.  The $USp(2r+2)$ comparison is polarization-matched to the
product representation only for even $r$; it remains a valid numerical
reference for all $r$.  The principal $V_{2r+1}$ is always symplectic.

## 6. What the producer authenticates

The producer locks four predecessors by fixture schema, canonical payload,
declared payload hash, LF-normalized fixture hash, and LF-normalized producer
hash:

- the all-$r$ tensor/symmetric-power subtorus rigidity packet;
- the $r=3$ tensor--symmetric-cube / symmetric-seventh packet;
- the $r=2$ tensor--symmetric-square / symmetric-fifth packet;
- the $r=1$ Rankin--SO(4) compact-moment packet.

It then performs three independent exact regressions:

- the coefficient formula (4) versus (5) for $0\leq n\leq33$;
- Clebsch--Gordan recursion versus (5) for $0\leq n\leq16$;
- oscillating-tableau counts versus the generic $USp$ table for
  $2\leq g\leq17$.

The note, producer, and independent test are themselves LF-hash-locked in
the JSON payload.  Replay with

```bash
python -B research/l-families/atlas/function_field/elliptic_tensor_symmetric_power_moment_ladder.py --check
python -B -O research/l-families/atlas/function_field/elliptic_tensor_symmetric_power_moment_ladder.py --check
python -B -m pytest -q tests/test_elliptic_tensor_symmetric_power_moment_ladder.py
python -B -O -m pytest -q tests/test_elliptic_tensor_symmetric_power_moment_ladder.py
```

## 7. Boundaries and next proof targets

- A compact Haar moment is not a finite-family moment theorem.  Applying this
  detector arithmetically requires a family and an error-controlled
  equidistribution statement.
- Matching through degree four does not imply equality of probability laws,
  spectra, local factors, or arithmetic origins.
- The displayed all-$r$ statements are proved from (3)--(11); the runtime
  table capped at $r=16$ is regression, not induction.
- No literature-priority claim is made for these elementary
  representation-ring formulas.

The clean next problem is to turn the degree-six gap into an arithmetic
statistic for explicit $L$-function families with a proved error term.
For odd $r$, the corresponding generic orthogonal comparison should be
classified separately.  Beyond degree eight, (4) supplies an exact starting
point for studying which factorizations of $B_k(n)$ persist and where new
piecewise behavior begins.
