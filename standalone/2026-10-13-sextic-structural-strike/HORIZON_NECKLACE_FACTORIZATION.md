# A stable finite-horizon representation from primitive necklaces

**Status:** proposed proved representation theorem and uniform polynomial
bound for its integrand. This repairs the superpolynomial instability of
the two unfiltered source representations. It proves no diagonal native
moment, no improved zero-free boundary, and no RH conclusion.

**Scope:** every fixed number of slots, every fixed positive real-part
contour after a finite degree is chosen, the literal multiplicative slot
characters with their nonunit zeros, all physical column horizons, and
all independent frequencies. The ideal-coefficient statements hold over
any fixed number field. Every element-row trace with the scaling
\(\Phi(u/\sqrt H)\) is specifically over the native Eisenstein field,
whose lattice has real dimension two.

**Classical connection:** the multivariate necklace identity is classical.
It is the denominator identity for the free Lie algebra on the slot
alphabet. Pieter Moree, *The formal series Witt transform*,
[arXiv:math/0311194v2](https://arxiv.org/html/math/0311194v2), Section 2,
equations (1)–(3) and the identity immediately following them, gives
exactly the necklace numbers and formal product used below. The elementary
combinatorial proof is included, so no Lie-algebra theorem is an analytic
input. The new application proposed here is the simultaneous truncation
of every retained factor to the physical column horizons.

**Repository connection:** the integrated account's Section 11 already
retains a scalar Witt identity for `1-x/2`, with rational exponents; its
Section 9 separately retains a causal Euler correction at real part one.
Those results are not being strengthened by attribution. This note joins
the multivariate, integer-exponent version of the first idea to the exact
norm-horizon discipline of the second, in the sextic moment setting.
The relevant current source is PR #911, commit
`2f8b6a3898a722d0602a91dea73bac344a3bb7dd`, P3–P6 of
[PRIME_SLOT_CANCELLATION.md](sources/pr911/PRIME_SLOT_CANCELLATION.md)
and SC2–SC4 of
[SHORT_POLYNOMIAL_COLLISION_TRANSPORT.md](sources/pr911/SHORT_POLYNOMIAL_COLLISION_TRANSPORT.md).
Its first- and second-degree factors are recovered exactly.

**What was actually established:** a formal identity, absolute convergence
of a remainder, an exact coefficient-rectangle transport, and an
all-frequency polynomial majorant. No finite test is used to infer an
infinite arithmetic cancellation estimate.

## 1. Why both levels have to be shortened

At one prime the source factor is

\[
                         1-z_1-\cdots-z_r.
\tag{1.1}
\]

The original unfiltered product of (1.1) has the first-order resonance
proved in [EULER_TRACE_RESONANCE.md](EULER_TRACE_RESONANCE.md).
Dividing by the single factors \(\prod_i(1-z_i)\), and replacing just
those factors by short Möbius polynomials, leaves the second-order
resonance proved in [RESONANT_SHORT_TRACE.md](RESONANT_SHORT_TRACE.md).
The single-factor replacement in SC2 therefore does not remove every
factor capable of generating coefficients far beyond the column horizons.

The repair is to extract and shorten every factor below the absolute
convergence degree. At the critical line it is enough to shorten both
the single factors and all the reciprocal pair factors. Primitive
necklaces organize the same operation at every finite degree.

## 2. The exact necklace identity

Let \(r\ge1\) be fixed. For a nonzero multi-index
\(\alpha=(\alpha_1,\ldots,\alpha_r)\in\mathbb Z_{\ge0}^r\), write
\(|\alpha|=\sum_i\alpha_i\), and define

\[
w_\alpha=\frac1{|\alpha|}
\sum_{d\mid\gcd(\alpha_1,\ldots,\alpha_r)}
\mu_{\mathbb Z}(d)\,
\frac{(|\alpha|/d)!}{\prod_i(\alpha_i/d)!}.
\tag{2.1}
\]

Zero coordinates cause no ambiguity: the gcd of a nonzero vector is
positive, and \(0!=1\). The Möbius function in (2.1) is the ordinary
integer Möbius function; the later Dirichlet polynomials use ideal Möbius
coefficients.

### Lemma 2.1. Primitive necklaces and the denominator product

Every \(w_\alpha\) is a nonnegative integer, and, as a formal power
series in \(z_1,\ldots,z_r\),

\[
\boxed{
1-\sum_{i=1}^r z_i
  =\prod_{\alpha\ne0}(1-\mathbf z^\alpha)^{w_\alpha},
\qquad \mathbf z^\alpha=\prod_i z_i^{\alpha_i}.
}
\tag{2.2}
\]

Only finitely many factors contribute to any specified total degree.

**Proof.** Use an alphabet of \(r\) labeled letters. There are
\(|\alpha|!/\prod_i\alpha_i!\) ordinary words of content \(\alpha\).
Every word is a repetition of a primitive word, uniquely up to the
cyclic rotation of that primitive word. If its repetition number is
\(d\), then \(d\mid\gcd\alpha\), and a primitive cyclic word of content
\(\alpha/d\) has exactly \(|\alpha|/d\) distinct linear rotations.
Consequently, if \(p_\beta\) counts primitive cyclic words of content
\(\beta\),

\[
\frac{|\alpha|!}{\prod_i\alpha_i!}
   =\sum_{d\mid\gcd\alpha}\frac{|\alpha|}{d}p_{\alpha/d}.
\tag{2.3}
\]

Divisor inversion gives \(p_\alpha=w_\alpha\). This proves integrality
and nonnegativity by counting, without an analytic fractional power.

For the product identity, expand the formal logarithm

\[
-\log(1-\sum_i z_i)
  =\sum_{\ell\ge1}\frac{(\sum_i z_i)^\ell}{\ell}.
\tag{2.4}
\]

Each word contributes its commutative weight divided by its length.
Group words by their primitive cyclic word. A primitive cyclic word of
length \(\ell_0\), repeated \(d\) times, has \(\ell_0\) distinct
linear rotations, each with weight \(\mathbf z^{d\alpha}\) and
denominator \(d\ell_0\). Its total contribution is
\(\mathbf z^{d\alpha}/d\). Thus (2.4) equals

\[
\sum_{\alpha\ne0}w_\alpha
       \sum_{d\ge1}\frac{\mathbf z^{d\alpha}}d
 =-\sum_{\alpha\ne0}w_\alpha\log(1-\mathbf z^\alpha).
\]

Every grouping is finite in a prescribed degree. Exponentiation proves
(2.2). \(\square\)

The first three degrees are particularly transparent:

\[
\begin{array}{c|c}
\alpha&w_\alpha\\ \hline
e_i&1\\
e_i+e_j,\ i<j&1\\
2e_i+e_j,\ i\ne j&1\\
e_i+e_j+e_\ell,\ i<j<\ell&2
\end{array}
\tag{2.5}
\]

Pure multiples \(me_i\), \(m>1\), have weight zero. The third-degree
terms therefore reproduce the source's complete cubic remainder signs.
At fourth and higher degree the weights remain exact integers; there is
no instruction to replace signed characters by their absolute values.

## 3. A uniformly summable remainder at every positive contour

Fix an integer \(J\ge1\), and put

\[
R_{J,p}(\mathbf z)=
\frac{1-\sum_i z_i}
 {\displaystyle\prod_{1\le|\alpha|\le J}
            (1-\mathbf z^\alpha)^{w_\alpha}}.
\tag{3.1}
\]

This is a rational function whose Taylor series has only nonnegative
coordinate exponents. It is holomorphic on the open unit polydisk,
since every denominator is nonzero there. Lemma 2.1 gives

\[
                    R_{J,p}(\mathbf z)=1+O_{r,J}(\|\mathbf z\|^{J+1})
\tag{3.2}
\]

near the origin, including the vanishing of every nonconstant coefficient
of total degree at most \(J\).

Let \(K\) be the fixed number field. For each row \(u\) let
\(\theta_{i,u}\) be the literal completely multiplicative slot functions,
with \(\theta_{i,u}(1)=1\) and \(|\theta_{i,u}(p)|\le1\).
All source exclusions \(S,Q\) are retained. Set

\[
z_{i,p}=\theta_{i,u}(p)(Np)^{-s_i},\qquad
\sigma_*=\min_i\Re s_i,
\qquad
\mathcal R_{J,Q,u}(\mathbf s)
 =\prod_{p\nmid SQ}R_{J,p}(z_{1,p},\ldots,z_{r,p}).
\tag{3.3}
\]

### Lemma 3.1. Absolute coefficient convergence

On each fixed real-part region

\[
                         \sigma_*>\frac1{J+1},
\tag{3.4}
\]

bounded away from its boundary, the product in (3.3) and its multivariate
ideal Dirichlet series converge absolutely and locally normally. In
particular,

\[
\sum_{\mathbf n}|r_{J,Q,u}(\mathbf n)|
                 \prod_i(Nn_i)^{-\Re s_i}
\le C_{K,r,J,\boldsymbol\sigma},
\qquad
|\mathcal R_{J,Q,u}(\mathbf s)|\le C_{K,r,J,\boldsymbol\sigma}.
\tag{3.5}
\]

These bounds are uniform in every row, every moving deletion mask, and
all independent imaginary parts. The remainder is permitted to vanish.

**Proof.** The rational Taylor series in (3.1) is absolutely convergent
at every fixed polyradius less than one. Cauchy's coefficient bound on,
for example, a fixed smaller polydisk, together with the degree
cancellation in (3.2), shows that its absolute nonconstant coefficient
sum at polyradius \(t\) is \(O_{r,J}(t^{J+1})\) for sufficiently small
\(t\). This is a bound on the absolute coefficients after the low-degree
cancellations; an absolute value is not taken before those cancellations.

For large primes use \(t=(Np)^{-\sigma_*}\). The resulting prime sum
converges because \((J+1)\sigma_*>1\), by the fixed-field ideal count.
At the finitely many smaller primes, the denominator geometric series
are absolutely convergent since \(t<1\); their finite cost is uniform
in the phases. Taking the product of these absolute local majorants
proves (3.5). Deleting primes or putting a local slot value equal to
zero can only decrease the majorant. The same proof on a slightly larger
real-part region gives local normal convergence. \(\square\)

This argument is analytic convergence of a remainder, not convergence of
an infinite reciprocal \(L\)-function on a conjectural zero-free region.
It requires only ideal counting. The full infinite product (2.2) is not
being evaluated analytically by passing \(J\) to infinity.

## 4. The physical horizon belongs in every factor

Let \(Y_i\ge1\) be the actual upper norm horizon for column \(i\), and
write \(Y_*=\max_iY_i\). In the source incidence allocation one may take

\[
                         Y_i=\frac{bD}{Nc_i}.
\tag{4.1}
\]

For each \(\alpha\) with \(w_\alpha>0\) and \(|\alpha|\le J\), put

\[
X_\alpha=\min_{\alpha_i>0}Y_i^{1/\alpha_i},\qquad
s_\alpha=\sum_i\alpha_i s_i,\qquad
\eta_{\alpha,u}(n)=\prod_{\alpha_i>0}\theta_{i,u}(n)^{\alpha_i}.
\tag{4.2}
\]

The powers and product in \(\eta_\alpha\) are literal. In particular,
a balanced exponent in the sextic character does not restore a value
one at a nonunit. Define the finite ideal polynomial

\[
T_{\alpha,X_\alpha,u}(s_\alpha)
 =\sum_{\substack{Nn\le X_\alpha\\(n,SQ)=1}}
       \mu_K(n)\eta_{\alpha,u}(n)(Nn)^{-s_\alpha},
\tag{4.3}
\]

and the new integrand

\[
\boxed{
\mathcal I_{J,\mathbf Y,Q,u}(\mathbf s)
 =\mathcal R_{J,Q,u}(\mathbf s)
    \prod_{\substack{1\le|\alpha|\le J\\w_\alpha>0}}
        T_{\alpha,X_\alpha,u}(s_\alpha)^{w_\alpha}.
}
\tag{4.4}
\]

All powers in (4.4) are ordinary nonnegative integer powers of actual
short Möbius polynomials.

### Theorem 4.1. Exact preservation of the column rectangle

Let

\[
\mathcal C_{Y_*,Q,u}(\mathbf s)
 =\prod_{\substack{Np\le Y_*\\p\nmid SQ}}
        \left(1-\sum_i\theta_{i,u}(p)(Np)^{-s_i}\right)
\tag{4.5}
\]

be the literal finite prime-slot polynomial. Then (4.4) and (4.5) have
exactly the same multivariate ideal coefficients at every tuple
\(\mathbf n=(n_1,\ldots,n_r)\) with

\[
                              Nn_i\le Y_i\quad(1\le i\le r).
\tag{4.6}
\]

Equality is coefficientwise in the ideals, not merely in their norms.
Distinct prime ideals of the same norm are never identified.

**Proof.** Initially use only the finite set of primes in (4.5).
The definition (3.1) gives the exact rational identity

\[
\mathcal C_{Y_*,Q,u}
 =\mathcal R^{\,\le Y_*}_{J,Q,u}
     \prod_{1\le|\alpha|\le J}
       \left[
         \prod_{\substack{Np\le Y_*\\p\nmid SQ}}
          (1-\eta_{\alpha,u}(p)(Np)^{-s_\alpha})
       \right]^{w_\alpha}.
\tag{4.7}
\]

The factor in square brackets has ideal coefficients
\(\mu_K(n)\eta_{\alpha,u}(n)\) on the squarefree ideals supported on
those finite primes. It places \(n^{\alpha_i}\) into column \(i\).
If \(Nn>X_\alpha\), at least one such column already has norm
\((Nn)^{\alpha_i}>Y_i\). Every other factor in (4.7), including the
remainder's geometric expansions, has nonnegative coordinate exponents.
No later multiplication can reduce that column norm. Removing the term
therefore leaves every coefficient in (4.6) unchanged.

Perform this removal in every one of the \(w_\alpha\) copies of every
retained factor. Since \(X_\alpha\le Y_*\), every ideal of norm at most
\(X_\alpha\) already has all its prime factors in the finite prime set;
the resulting factor is exactly (4.3).

Finally replace the finite remainder by (3.3). A nonconstant monomial at
a new prime with \(Np>Y_*\) puts that prime into at least one column,
whose norm then exceeds its horizon. Such a term never contributes to
(4.6). Thus the replacement also preserves those coefficients.
Lemma 3.1 supplies absolute convergence when analytic evaluation is
needed. The coefficient argument itself is purely formal and finite
for each tuple. \(\square\)

The cutoff in (4.2) is imposed on every copy separately. It does not
assert that their product automatically stays within the rectangle.
The complete physical column tests still remove all remaining oversized
products. This is the same direction of coefficient reasoning that
justified SC2, now applied to every retained necklace factor.

### Corollary 4.2. Complete Mellin transport

For the original smooth column tests \(W_i\), supported in \([a,b]\),
choose (4.1). On any contour satisfying (3.4), the complete tested
coefficient sum is exactly

\[
\frac1{(2\pi)^r}\int_{\mathbb R^r}
 \mathcal I_{J,\mathbf Y,Q,u}(\boldsymbol\sigma+i\mathbf t)
 \prod_i
     (D/Nc_i)^{\sigma_i+it_i}
     \widehat W_i(\sigma_i+it_i)\,d\mathbf t.
\tag{4.8}
\]

**Proof.** Lemma 3.1 and the finite polynomial factors give an absolutely
convergent multivariate Dirichlet series on the contour. The smooth
Mellin transforms are rapidly decreasing. Termwise Mellin inversion
is therefore legitimate. Every surviving tuple obeys (4.6), where
Theorem 4.1 identifies its exact coefficient with the source.
\(\square\)

In the native Eisenstein field, multiplying by the original exterior row
character and summing against the fixed Schwartz row weight is also
legitimate, by the uniform
polynomial bound proved next. Partial integrals over frequency tubes
are not invariant under this representation change. In particular, the
old SC7 tube estimate is not silently transferred to (4.8).

## 5. A polynomial bound at all independent frequencies

For fixed \(\lambda>0\), put

\[
B_\lambda(X)=
\begin{cases}
X^{1-\lambda},&0<\lambda<1,\\
\log(2X),&\lambda=1,\\
1,&\lambda>1.
\end{cases}
\tag{5.1}
\]

Ideal counting and partial summation give
\(\sum_{Nn\le X}(Nn)^{-\lambda}\ll_{K,\lambda}B_\lambda(X)\).

### Theorem 5.1. No superpolynomial trace resonance in this representation

For fixed \(r,J,\boldsymbol\sigma\) satisfying (3.4),

\[
\boxed{
|\mathcal I_{J,\mathbf Y,Q,u}(\boldsymbol\sigma+i\mathbf t)|
\ll
\prod_{\substack{1\le|\alpha|\le J\\w_\alpha>0}}
 B_{\alpha\cdot\boldsymbol\sigma}(X_\alpha)^{w_\alpha}.
}
\tag{5.2}
\]

The bound holds for every row, moving mask and independent frequency.
For the native Eisenstein element rows, if \(H\ge1\),
\(|\omega_{\mathbf q}(u)|\le1\), and \(\Phi\) is the fixed source
Schwartz function, then

\[
\left|\sum_{u\ne0}\Phi(u/\sqrt H)\omega_{\mathbf q}(u)
           \mathcal I_{J,\mathbf Y,Q,u}(\boldsymbol\sigma+i\mathbf t)\right|
\ll H
\prod_{\substack{1\le|\alpha|\le J\\w_\alpha>0}}
 B_{\alpha\cdot\boldsymbol\sigma}(X_\alpha)^{w_\alpha}.
\tag{5.3}
\]

**Proof.** Apply the absolute ideal-count bound to each literal polynomial
(4.3), whose coefficients have modulus at most one. Lemma 3.1 bounds
the remainder independently of every frequency. This proves (5.2).
The two-dimensional Eisenstein lattice estimate
\(\sum_{u\ne0}|\Phi(u/\sqrt H)|\ll_\Phi H\) proves (5.3).
\(\square\)

For any fixed positive \(\sigma_*\), a finite \(J\) can be chosen to
satisfy (3.4). Therefore this construction always gives a polynomial
bound when the horizons are polynomial in \(D\). Its constants are
allowed to depend on \(r,J,\boldsymbol\sigma\). No uniform limit in
\(J\), in \(k=r/2\), or as \(\sigma_*\downarrow0\) is asserted.

## 6. The useful critical-line specialization

Take \(r=2k\), \(J=2\), and \(\sigma_i=1/2\). Lemma 2.1 gives just
the single factors and the \(\binom{2k}{2}\) distinct-slot pair factors:

\[
\boxed{
\mathcal I_{2,\mathbf Y,Q,u}
  =\mathcal R_{2,Q,u}
     \prod_i T_{i,Y_i,u}(s_i)
     \prod_{i<j}
        T_{ij,\min(Y_i,Y_j),u}(s_i+s_j).
}
\tag{6.1}
\]

The remainder is the source P4 remainder, now with all good primes;
its absolute coefficient convergence follows from \(3/2>1\).
Each pair polynomial is evaluated at real part one and has its actual
product character. Same-side pairs retain the cubic sextic-symbol part
together with the fixed \(\nu^2\) twist (or its conjugate); the complete
character need not be cubic. Cross-side pairs retain their principal
nonunit masks. No inverse infinite \(L\)-function is substituted.

Equations (5.2)–(5.3) specialize to

\[
|\mathcal I_{2,\mathbf Y,Q,u}|
\ll
\prod_iY_i^{1/2}
\prod_{i<j}\log(2\min(Y_i,Y_j)),
\tag{6.2}
\]

and the same bound multiplied by \(H\) for the row trace. This excludes
the superpolynomial growth proved for P13 and CT1 at the level of the
actual new integrand. It is a uniform theorem, not a check at a finite
set of resonant frequencies.

One may also use smooth cutoffs equal to one on \([0,1]\) and supported
in \([0,2]\) in (4.3). Every changed coefficient is then beyond
\(X_\alpha\), so Theorem 4.1 is unchanged, and (5.2) changes by a fixed
constant. This version is compatible with smooth native inverse tests;
it does not assume a theorem for arbitrary hard-cutoff coefficients.

## 7. What the repair has and has not bought

The source's unfiltered Euler polynomial admits first-degree exponential
growth. Shortening only its single factors leaves second-degree
exponential growth below the half line. The representation (4.4)
shortens every factor before the absolutely convergent remainder starts.
The exact finite horizons, integer factor multiplicities, and literal
nonunit masks make this operation well defined.

The new pointwise bound is still much larger than the moment target.
At equal horizons \(Y_i\asymp D\), (6.2) costs \(D^k\) up to
logarithms before the additional Mellin scale factor \(D^k\).
It therefore supplies only the trivial full-moment power \(HD^{2k}\).
The ordinary two-factor Cauchy argument, with pointwise estimates on
the other singleton factors, recovers the existing interpolation cost;
the necklace identity does not create a higher-moment estimate.

A sufficient further statement would be the uniform signed trace bound

\[
\left|\sum_{u\ne0}\Phi(u/\sqrt H)\omega_{\mathbf q}(u)
     \mathcal I_{2,\mathbf Y,Q,u}(1/2+i\mathbf t)\right|
\ll_\epsilon HD^\epsilon\prod_i(1+|t_i|)^B.
\tag{7.1: OPEN}
\]

Its horizons are the actual \(\mathbf Y=(bD/Nc_i)_i\). If (7.1)
were proved for all the original incidence allocations, complete Mellin
inversion and the source's harmonic pair-incidence sums would give
\(M_{2k}^{\Phi}(D,H)\ll HD^{k+\epsilon}\). This implication is the
same explicitly priced incidence argument as P14–P15. It is conditional.

Unlike the refuted contracts, (7.1) does not contain an unshortened
low-degree Euler factor capable of the demonstrated superpolynomial
resonance. That removes a specific false target; it does not establish
(7.1), guarantee that no other obstruction exists, or reduce its
arithmetic difficulty to local algebra.

The companion [PRIME_DEGREE_COHERENCE.md](PRIME_DEGREE_COHERENCE.md)
explains a second constraint on such an attack: estimating separate
prime-degree pieces in absolute value loses cancellation that the
complete native Möbius coefficients require. The literal short
polynomials in (6.1) keep that prime/composite completion intact.

## 8. Verification boundary

The classical necklace formula, its combinatorial proof, the analytic
remainder majorant, and the exact rectangle argument are the load-bearing
mathematics. A finite coefficient checker can authenticate chosen local
degrees and chosen ideal rectangles, including separate equal-norm prime
labels and nonunit zeros. It cannot certify a native moment, an infinite
prime-distribution statement, or the open trace estimate (7.1).

No prime ideal theorem, theta foundation, GRH, or zero-free hypothesis is
needed for Theorems 4.1 and 5.1. They use only the displayed algebra,
fixed-field ideal counting and smooth Mellin inversion.
