# Native Newton compression with arbitrary logarithmic rank savings

Status: **proposed component theorem; independent mathematical review required.**

Scope: unconditional asymptotic compression of the complete, finite native
reciprocal-Mobius energy on one strict square step. The theorem below does
not establish a subquadratic coarse-energy recurrence or prove RH.

Exact repository dependency: PR #905 at
`0f82df3bf1d0bc669a1bbca09f8404b77c6fecde`,
`standalone/2026-09-21-native-covariance-compression/PROOF.md` (NRC32).
The finite Newton identity and the block-variance identity are reproduced
below. The only imported analytic theorem is specified in Section 2.

What was actually run: `python3 check_newton.py --output audit.json` checks
finite coefficient reconstruction, both square endpoints, exact rational
block means, and complete energy decompositions. These checks do not certify
the imported analytic theorem or the asymptotic constants.

Smallest remaining gap toward the NRC32 route: an upper bound on the
remaining signed native coarse forms in terms of the *previous* native
energy, with a cumulative saving from the quadratic exponent. Compression
alone supplies no such amplitude bound.

## 1. Statement and normalization

For an integer $Y\geq1$, set

$$
b=Y+1,\qquad N=b^2-1,\qquad
m(k)=\sum_{n\leq k}\frac{\mu(n)}n,\qquad
F_K=\sum_{k=1}^{K}m(k)^2.
$$

All cells $k=b,\ldots,b^2-1$ are retained. There is no assertion about the
coefficient at $b^2$, no infinite continuation, and no Mellin tail in the
energy considered here.

Fix an integer $r\geq0$. The mesh multiplier is the explicitly computable
integer

$$
L_b=1+\lfloor\log_2 b\rfloor,\qquad q_b=L_b^r.
$$

Take the dyadic annuli

$$
J_j=[X_j,\min(2X_j,b^2))\cap\mathbb Z,
\qquad X_j=2^jb<b^2.
$$

On $J_j$, set

$$
H_j=\max\left(1,\left\lfloor
q_b\left(\frac{X_j^2}{b}\right)^{1/3}
\right\rfloor\right).
\tag{1.1}
$$

Starting at the left endpoint, partition $J_j$ into consecutive blocks
of length $H_j$, with a final block of the remaining length if necessary.
No choice in this partition depends on the values of $\mu$.

For a block $I=[a,a+h)\cap\mathbb Z$, let

$$
\bar m_I=\frac1h\sum_{k\in I}m(k),\qquad
S_{Y,r}=\sum_I h\bar m_I^2,\qquad
D_{Y,r}=\sum_I\sum_{k\in I}(m(k)-\bar m_I)^2.
$$

### Theorem 1: logarithmic rank reduction with complete vanishing error

For every fixed integer $r\geq0$ and every fixed real $B>0$, as
$Y\longrightarrow\infty$, the deterministic partition above satisfies

$$
\#\{I\}\ll_r\frac{Y}{(\log(2Y))^r},
\tag{1.2}
$$

$$
F_{b^2-1}-F_Y=S_{Y,r}+D_{Y,r},\qquad
0\leq D_{Y,r}\ll_{r,B}(\log(2Y))^{-B}.
\tag{1.3}
$$

Every mean $\bar m_I$ is an exact signed quadratic form in the finite
prefix $\mu(1),\ldots,\mu(Y)$, with the explicit coefficients in
Section 6. In particular, it is not necessary to know any future Mobius
values to generate the coarse coordinates.

For any prescribed real $A>0$, choosing a fixed integer $r\geq A$
gives $O_A(Y/(\log(2Y))^A)$ coordinates and the same assertion for every
fixed $B>0$. For a fixed $r$, the mesh is independent of $B$.

The assertion is asymptotic. We do not supply numerical values for the
constants or a numerical threshold in the imported short-interval theorem.
The parameter $r$ is fixed before taking $Y\to\infty$; it cannot grow
with $Y$ under this statement.

Compared with NRC32, the new analytic input permits a larger mesh and a
complete error tending to zero faster than any prescribed inverse power
of the logarithm. This is a statement about the resolution required for
the **actual signed source**, not a bound for the unresolved coarse energy.

## 2. Exact imported analytic input

We use the $T=0$ case of Theorem 3.1(i) of K. Matomaki, M. Radziwill,
X. Shao, T. Tao and J. Teravainen, *Higher uniformity of arithmetic functions
in short intervals II. Almost all intervals*,
[arXiv:2411.05770v2](https://arxiv.org/html/2411.05770v2),
version dated 23 January 2026. The paper also appeared in
*Inventiones Mathematicae* **244** (2026), 967--1091,
[DOI 10.1007/s00222-026-01408-6](https://doi.org/10.1007/s00222-026-01408-6).

Here is the precise consequence used. For every fixed $\varepsilon>0$
and $K>0$, and integers $X,Q$ with

$$
X^{1/3+\varepsilon}\leq Q\leq X,
$$

put

$$
U_{X,Q}(k)=\max_{0\leq \ell\leq Q}
\left|\sum_{k<n\leq k+\ell}\mu(n)\right|
\quad (X\leq k<2X,\quad k,\ell\in\mathbb Z).
$$

Then

$$
\sum_{k=X}^{2X-1}U_{X,Q}(k)^2
\ll_{K,\varepsilon}XQ^2(\log X)^{-K}.
\tag{2.1}
$$

To obtain (2.1), the imported theorem bounds maximal sums over **all
arithmetic progressions** in $(x,x+Q]$ by $Q(\log X)^{-K}$, outside
an exceptional set of real $x\in[X,2X]$ of measure
$O_{K,\varepsilon}(X(\log X)^{-K})$. Contiguous initial intervals are
among these progressions. For integer $Q$, both the integer window and
its collection of progressions are constant for $x\in[k,k+1)$, apart
from endpoints of measure zero. Thus the sum over integer $k$ is exactly
the corresponding integral of this piecewise constant quantity.

On the exceptional set use the trivial bound $U\leq Q$. On its
complement use the stated maximal bound. This gives

$$
\sum_k U_{X,Q}(k)^2
\ll XQ^2\big((\log X)^{-2K}+(\log X)^{-K}\big),
$$

which proves (2.1), after absorbing the harmless small values of $X$.
There is no claim that deterministic block endpoints avoid the exceptional
set. The proof below sums over **every interior starting point**, and pays
the exceptional set through (2.1).

No growing-shift exponent from another repository packet, no generalized
Dedekind coefficient estimate, and no conjectured square-root cancellation
is used in (2.1).

## 3. A variance lemma that retains the exceptional set correctly

### Lemma 2: maximal increments control complete block variance

Let $X,Q$ be positive integers. Let a collection of disjoint integer
blocks $I=[a,a+h)$ lie in $[X,2X)$, with $h\leq Q$. Define

$$
U(k)=\max_{0\leq \ell\leq Q}
\left|\sum_{k<n\leq k+\ell}\mu(n)\right|
\qquad (X\leq k<2X).
$$

Then

$$
\sum_I\sum_{k\in I}(m(k)-\bar m_I)^2
\leq\frac1{X^2}\sum_{k=X}^{2X-1}U(k)^2.
\tag{3.1}
$$

**Proof.** Fix $k\geq X$ and $0\leq\ell\leq Q$, and write

$$
A_k(v)=\sum_{k<n\leq k+v}\mu(n).
$$

Partial summation with the positive decreasing weight $1/n$ gives

$$
\sum_{k<n\leq k+\ell}\frac{\mu(n)}n
=\frac{A_k(\ell)}{k+\ell}
 +\int_0^{\ell}\frac{A_k(v)}{(k+v)^2}\,dv.
$$

All the partial sums on the right have modulus at most $U(k)$. Since

$$
\frac1{k+\ell}+\int_0^{\ell}\frac{dv}{(k+v)^2}=\frac1k,
$$

we obtain the useful bound without an extra logarithm,

$$
|m(k+\ell)-m(k)|\leq\frac{U(k)}k\leq\frac{U(k)}X.
\tag{3.2}
$$

For a real sequence on a block of length $h$, the exact pair identity is

$$
\sum_{k\in I}(m(k)-\bar m_I)^2
=\frac1h\sum_{\substack{k,j\in I\\k<j}}(m(j)-m(k))^2.
\tag{3.3}
$$

For each fixed $k\in I$, there are fewer than $h$ choices of $j>k$.
Every difference $j-k$ is at most $Q$, so (3.2) and (3.3) imply

$$
\sum_{k\in I}(m(k)-\bar m_I)^2
\leq\frac1{X^2}\sum_{k\in I}U(k)^2.
$$

The blocks are disjoint, which proves (3.1). $\square$

Combining (3.1) with (2.1), whenever $X^{1/3+\varepsilon}\leq Q\leq X$,

$$
\sum_I\sum_{k\in I}(m(k)-\bar m_I)^2
\ll_{K,\varepsilon}\frac{Q^2}{X}(\log X)^{-K}.
\tag{3.4}
$$

This lemma is the point where the native signs enter the new compression.
Replacing a signed short sum by its termwise absolute value loses (2.1).

## 4. Deterministic bounds and the number of coordinates

For later use we record the elementary NRC32 variance bound. On
$I=[a,a+h)$, the increment estimate

$$
|m(j)-m(k)|\leq\frac{j-k}{a}\quad(a\leq k<j<a+h)
$$

and (3.3) yield

$$
D_I\leq\frac{h(h^2-1)}{12a^2}.
\tag{4.1}
$$

Indeed $\sum_{0\leq i<j<h}(j-i)^2=h^2(h^2-1)/12$.

For fixed $r$ and sufficiently large $b$, the unfloored expression in
(1.1) is at least two, and consequently

$$
\frac12q_b b^{-1/3}X_j^{2/3}
\leq H_j\leq q_b b^{-1/3}X_j^{2/3}.
\tag{4.2}
$$

The number of blocks in $J_j$ is at most $X_j/H_j+1$. The geometric
sum satisfies

$$
\sum_{X_j<b^2}X_j^{1/3}\ll b^{2/3}.
\tag{4.3}
$$

It follows that

$$
\#\{I\}\leq
\frac{2b^{1/3}}{q_b}\sum_jX_j^{1/3}+O(\log b)
\ll \frac{b}{q_b}+\log b.
$$

For fixed $r$, the first term eventually dominates the second, proving
(1.2). Floors and the final short block of each annulus are included.

For any one annulus, (4.1), $h\leq H_j$, $a\geq X_j$, and
$\sum_{I\subset J_j}h\leq X_j$ imply

$$
\sum_{I\subset J_j}D_I
\leq\frac{H_j^2}{12X_j}
\leq\frac{q_b^2}{12b^{2/3}}X_j^{1/3}.
\tag{4.4}
$$

This deterministic bound will pay the initial part of the square step,
where the imported short-interval theorem is not invoked.

## 5. Proof of the complete error estimate

Split the annuli into the two explicit classes

$$
X_j<b^{3/2}\quad\hbox{and}\quad X_j\geq b^{3/2}.
$$

For the first class, summing (4.4) as a geometric series gives

$$
\sum_{X_j<b^{3/2}}\sum_{I\subset J_j}D_I
\ll q_b^2 b^{-2/3}b^{1/2}
=q_b^2 b^{-1/6}.
\tag{5.1}
$$

This includes the complete annulus crossing $b^{3/2}$, if its left
endpoint is smaller than that threshold. No transition cells are omitted.

For the second class use the analytic bound (3.4) with $Q=H_j$ and
fixed $\varepsilon=1/12$. The hypotheses hold for sufficiently large
$b$, depending on $r$. Indeed, $b\leq X_j^{2/3}$ gives

$$
H_j\geq\frac12q_b X_j^{4/9}
\geq X_j^{5/12}=X_j^{1/3+1/12}
$$

eventually. Also

$$
\frac{H_j}{X_j}\leq
\frac{q_b}{(bX_j)^{1/3}}
\leq q_b b^{-5/6}\longrightarrow0.
$$

Every block in this annulus has length at most $H_j$. The last annulus
may be truncated at $b^2$, but its starts form a subset of the full
integer interval $[X_j,2X_j)$, so Lemma 2 still applies. We get

$$
\sum_{I\subset J_j}D_I
\ll_K q_b^2 b^{-2/3}X_j^{1/3}(\log X_j)^{-K}.
$$

The maximal sums used as an upper bound may reach past $b^2$. They contain
the actual, globally defined Mobius function, to which the imported theorem
applies. We do not substitute the truncated Newton coefficient formula
beyond its strict endpoint. Only the energy on the declared finite square
step is being estimated or reconstructed.

Since $X_j\geq b$, (4.3) now gives

$$
\sum_{X_j\geq b^{3/2}}\sum_{I\subset J_j}D_I
\ll_K q_b^2(\log b)^{-K}.
\tag{5.2}
$$

Combining (5.1) and (5.2), we have proved the more informative estimate

$$
D_{Y,r}\ll_K q_b^2\left(b^{-1/6}+(\log b)^{-K}\right)
\tag{5.3}
$$

for every fixed $K>0$, with the validity threshold allowed to depend on
$r,K$. Since $q_b\ll_r(\log b)^r$, choosing $K>B+2r$ proves
the upper bound in (1.3). The exact equality in (1.3) is the orthogonal
identity on each block, summed over the complete partition. Positivity
of $D_{Y,r}$ follows from its definition. $\square$

The $b^{-1/6}$ term is a deliberately inexpensive payment for the early
annuli; its exponent is not optimized. No cancellation assertion below
the imported theorem's range is needed.

## 6. Exact quadratic coordinates from the old prefix

For completeness, define the finite source

$$
g(n)=\mu(n)\mathbf1_{n\leq Y},\qquad z=g*g,
$$

where $*$ is Dirichlet convolution, $\mathbf1(n)=1$, and
$\delta(1)=1,\delta(n)=0$ for $n>1$. Set

$$
v=2g-\mathbf1*g*g.
$$

The exact identity

$$
\mu-v=\mu*(\delta-\mathbf1*g)*(\delta-\mathbf1*g)
\tag{6.1}
$$

follows from $\mu*\mathbf1=\delta$. The factor
$\delta-\mathbf1*g$ vanishes for every integer less than $b$.
Thus the right side of (6.1) vanishes for every $n<b^2$, and

$$
v(n)=\mu(n)\qquad(1\leq n<b^2).
\tag{6.2}
$$

For $b\leq k<b^2$, this gives

$$
m(k)=2m(Y)-\sum_{d\leq Y^2}\frac{z(d)}d H_{\lfloor k/d\rfloor},
\tag{6.3}
$$

with $H_0=0$. In particular, a product with $d>k$ contributes zero.

For integer $t\geq1$, define

$$
A_d(t)=tH_{\lfloor(t-1)/d\rfloor}
-d\lfloor(t-1)/d\rfloor.
$$

Counting $k$ with $dj\leq k<t$ gives exactly

$$
\sum_{k=0}^{t-1}H_{\lfloor k/d\rfloor}=A_d(t).
$$

Therefore each mesh block has the explicit mean

$$
\boxed{\displaystyle
\bar m_{[a,a+h)}
=2m(Y)-\frac1h\sum_{d\leq Y^2}\frac{z(d)}d
\big(A_d(a+h)-A_d(a)\big).}
\tag{6.4}
$$

All products and signs are retained. The term $2m(Y)$ is linear in the
prefix; since $\mu(1)=1$, it can also be written as a quadratic term
in that same prefix. Squaring (6.4) produces the actual coarse covariance,
without replacing signed source terms by their absolute values.

The source $g$ is uncompleted and (6.3) is only a finite coefficient
identity. Nothing here identifies its infinite continuation with the
specified full native continuation in NRC32 or with a balanced Newton
source from another packet.

## 7. What this changes, and the remaining theorem

The previous elementary resolution bound paid a nonzero constant for
omitting the within-block variation. The new theorem both makes that
complete payment arbitrarily small asymptotically and reduces the number
of retained coordinates by any fixed logarithmic factor. It proves that
the actual native output is asymptotically concentrated on a deterministic
space whose dimension is smaller than the old-prefix length by such a
factor.

It does **not** prove that the norm in that space is small. The coarse
coordinates are still the signed quadratic forms (6.4). For example, the
following sufficient gate remains unproved for any fixed $\delta>0$:

$$
S_{Y,r}\leq C(\log(2Y))^A(1+F_Y)^{2-\delta}
\tag{7.1}
$$

on every sufficiently late step of a native square ladder, with fixed
constants $C,A,\delta$. The standard NRC32/BNR26 bootstrap applies to
(7.1), since $D_{Y,r}=o(1)$. We do not present that previously known
conditional bootstrap as the new theorem.

A proof that uses only the number of coordinates, or Cauchy--Schwarz
inside each coordinate, does not establish (7.1). A smaller number of
coordinates is not a bound on their magnitudes. Similarly, one cannot
choose a growing $r=r(Y)$ to manufacture a power reduction from the
fixed-$r$ statement above.

The concrete next object is consequently the same exact native coarse
quadratic form, now with an asymptotically negligible *complete* remainder
and fewer coordinates. Any further argument must use the literal divisor
inverse in (6.1) in a way that bounds those coarse amplitudes.

## 8. Two controls against overclaiming

### 8.1 The improvement uses native signs

Replace $\mu(n)$ by $1$, so that $m(k)$ is replaced by $H_k$.
This sequence satisfies the same pointwise increment bound used in (4.1).
For $b$ restricted to powers of two, the last complete dyadic annulus is
$[b^2/2,b^2)$, with

$$
H=\left\lfloor 2^{-2/3}q_b b\right\rfloor.
$$

For all sufficiently large $b$, $2\leq H\leq b^2/4$. The complete
blocks of length $H$ cover at least $b^2/4$ cells. Every increment of
$H_k$ in these blocks is at least $1/b^2$, so (3.3) gives

$$
D_I^{(+)}\geq\frac{H(H^2-1)}{12b^4}.
$$

Since $H\geq2^{-5/3}q_b b$ for large $b$, summing these complete
blocks yields, with a deliberately loose absolute constant,

$$
D_{Y,r}^{(+)}\geq\frac{q_b^2}{2048}.
\tag{8.1}
$$

Thus the new native error estimate is false for a sequence with the same
increment bound and no signed cancellation. In particular, the enlargement
of the mesh is not paid by deterministic regularity alone.

### 8.2 Even zero detail does not imply a coarse-energy saving

For the coefficient sequence $a(n)=\delta(n)$, its reciprocal partial
sum is identically one for $k\geq1$. Every short sum of $a$ starting
at a sufficiently large positive integer is zero. Nevertheless every
block mean is one, hence

$$
D^{(\delta)}=0,\qquad S^{(\delta)}=b^2-b,
\qquad F_Y^{(\delta)}=Y.
$$

This fake source has perfect short-interval cancellation and perfect
compression, while its coarse energy has the quadratic scale of the
previous energy. It does not satisfy the literal Mobius inverse identity,
which is precisely why that remaining arithmetic condition cannot be
discarded in the next step.

These controls delimit the theorem. They are not models of the actual
Mobius prefix and are not evidence for or against RH.
