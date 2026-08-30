# Rational rotations: exact degree for every positive real absolute power

Status: **proposed exact local theorem; external novelty unreviewed**
Issue: [#764](https://github.com/gfreund123/riemann/issues/764)
Authoring agent: codex-two-programmes / root
Claim labels: GLO764.EXPONENTIAL_DESCARTES_BOUND,
GLO764.RATIONAL_ABSOLUTE_REAL_MODE_ZEROS,
GLO764.RATIONAL_ABSOLUTE_REAL_EXACT_DEGREE,
GLO764.COMPLEX_FULL_DEGREE_COUNTEREXAMPLE
Source commit: 3fd6c34d1cd8109eab3622d3966e05a0ad8fc7a4

## 1. What this strengthens, and what it does not

The earlier uniform-degree gate proved unbounded reduced degrees outside
the even-integer absolute-power chamber. It did not supply a rate.
For **positive real** exponents there is an exact answer at every
rational angle:

\[
\boxed{
d_{\mathrm{abs}}(\lambda;a,b)=
\begin{cases}
\min(b,2m+1),&\lambda=2m,\quad m\in\mathbb Z_{>0},\\
b,&\lambda>0,\quad\lambda\notin2\mathbb Z_{>0}.
\end{cases}}
\tag{1.1}
\]

Here \(b\ge2,\ 1\le a<b,\ \gcd(a,b)=1\), and \(d_{\mathrm{abs}}\)
is the reduced denominator degree of

\[
\sum_{r\ge0}
\left|\frac{\sin((r+1)a\pi/b)}{\sin(a\pi/b)}\right|^\lambda T^r.
\tag{1.2}
\]

Zeros have value zero. Powers of positive real numbers use their real
logarithm. A degree means minimal **eventual** constant-coefficient
recurrence order, not merely a displayed period.

This is one scalar, unramified, determinant-one, tempered rank-two local
model. It does not construct a global family, ramified factors, a
completion, an automorphic or motivic realization, or any RH/GRH result.
It is not a theorem about the signed fixed-branch power. The extension
of (1.1) to all complex exponents with positive real part is false
(Section 6).

## 2. Reduction to real exponential sums

Put

\[
s_\lambda(l)=\sin^\lambda(\pi l/b),\qquad 0\le l<b.
\tag{2.1}
\]

The sine is nonnegative on this block. Taking absolute values makes
the original samples a permutation by \(l\mapsto al\bmod b\), followed
by a cyclic shift and multiplication by a nonzero constant. These
operations preserve discrete Fourier support cardinality.

Use the unnormalized Fourier coefficients

\[
E_j(x)=\sum_{l=1}^{b-1}
       \sin^{2x}(\pi l/b)e^{-2\pi i jl/b},
\qquad x=\lambda/2>0.
\tag{2.2}
\]

The \(l=0\) term is zero and is omitted. Pairing \(l\) and \(b-l\)
shows that \(E_j(x)\) is real, \(E_{b-j}(x)=E_j(x)\), and
\(E_0(x)>0\). For \(1\le j\le\lfloor b/2\rfloor\),

\[
E_j(x)=\sum_{l=1}^{\lfloor b/2\rfloor}c_l a_l^x,\qquad
a_l=\sin^2(\pi l/b),
\tag{2.3}
\]

where \(c_l=2\cos(2\pi jl/b)\), except that when \(b\) is even
the single middle term has \(c_{b/2}=\cos(\pi j)=(-1)^j\).
The bases \(a_l\) are positive and strictly increasing.
After discarding zero coefficients, their sign sequence has at most
\(j\) variations: as \(l\) increases, the cosine argument runs inside
\((0,\pi j]\), where there are exactly \(j\) possible sign crossings.
Omitting samples or reducing the middle coefficient by a positive
factor cannot increase this count.

## 3. An elementary generalized Descartes bound

**Lemma GLO764.EXPONENTIAL_DESCARTES_BOUND.**
Let \(r_1<\cdots<r_N\) be real and let all real coefficients \(c_i\)
be nonzero. If their sign sequence has \(V\) variations, then

\[
F(x)=\sum_{i=1}^N c_i e^{r_i x}
\tag{3.1}
\]

has at most \(V\) real zeros, counted with multiplicity.

### Proof

Induct on \(V\). If \(V=0\), every summand has the same strict sign.
Otherwise choose adjacent coefficients \(c_{q-1},c_q\) with opposite
signs, and choose \(p\) strictly between \(r_{q-1}\) and \(r_q\).
Then

\[
\frac{d}{dx}\big(e^{-px}F(x)\big)
=\sum_i(r_i-p)c_i e^{(r_i-p)x}.
\tag{3.2}
\]

Multiplication by \(r_i-p\) reverses every coefficient before that
cut and preserves every coefficient after it. All internal sign
variations are unchanged; the selected variation disappears.
The derivative has exactly \(V-1\) variations, hence at most \(V-1\)
real zeros by induction. Rolle's theorem, including multiplicities,
implies that any finite collection of zeros of \(e^{-px}F\) has total
multiplicity at most \(V\). The nonvanishing factor \(e^{-px}\) does
not change zeros or their multiplicities. This also excludes an
infinite collection of zeros, proving the assertion. \(\square\)

This is a classical generalized Descartes argument, not a novelty claim.
The proof is included so the result does not depend on access to a
literature theorem or on a numerical zero count.

## 4. All positive zeros of each nonzero Fourier mode

**Theorem GLO764.RATIONAL_ABSOLUTE_REAL_MODE_ZEROS.**
For \(1\le j\le\lfloor b/2\rfloor\), the positive real zeros of the
analytic exponential sum \(E_j(x)\) are exactly

\[
1,2,\ldots,j-1,
\tag{4.1}
\]

each with multiplicity one. For \(j=1\) the set is empty.

### Proof

Section 3 and the sign count in Section 2 give at most \(j\) real
zeros, hence at most \(j\) positive zeros, including multiplicity.

For \(m=1,\ldots,j-1\), \(\sin^{2m}t\) is a trigonometric
polynomial with frequencies \(-m,\ldots,m\) when written in
\(e^{2it}\). None of these frequencies is congruent to \(j\bmod b\):
both \(j\) and \(b-j\) exceed \(m\). Discrete orthogonality therefore
gives \(E_j(m)=0\). There are at least \(j-1\) positive zeros.

At \(x=0\), the analytic continuation of (2.3) satisfies

\[
E_j(0)=\sum_{l=1}^{b-1}e^{-2\pi i jl/b}=-1.
\tag{4.2}
\]

This does **not** assign a value to \(0^0\); the omitted zero sample
remains omitted. The exponential sum is analytic at \(x=0\) because
all its bases are strictly positive.

The largest base has nonzero coefficient with sign \((-1)^j\).
For even \(b\) it is the middle coefficient. For odd \(b\) it is

\[
2\cos\!\left(\pi j-\frac{\pi j}{b}\right)
=2(-1)^j\cos(\pi j/b),
\tag{4.3}
\]

whose last cosine is positive. More precisely,
\(E_j(x)/a_{\lfloor b/2\rfloor}^{\,x}\) tends to this nonzero
last coefficient. Thus \(E_j(x)\) has eventual sign \((-1)^j\)
as \(x\to+\infty\), even though for odd \(b\) its raw value tends
to zero.

Because there are finitely many zeros, the sum \(Z_+\) of their
positive-real multiplicities obeys

\[
(-1)^{Z_+}
=\frac{(-1)^j}{-1}=(-1)^{j-1}.
\tag{4.4}
\]

An even-order zero does not change sign; an odd-order zero does.
Since \(j-1\le Z_+\le j\), the parity in (4.4) forces
\(Z_+=j-1\). The known \(j-1\) distinct zeros exhaust the count and
must each be simple. \(\square\)

In particular, away from these zeros the sign is

\[
\operatorname{sgn}E_j(x)
=(-1)^{1+\#\{m\in\mathbb Z:1\le m\le j-1,\ m<x\}}.
\tag{4.5}
\]

No floating-point evaluation is needed for either the zero set or the
sign rule.

## 5. Exact reduced degree and the regular-polygon interpretation

**Theorem GLO764.RATIONAL_ABSOLUTE_REAL_EXACT_DEGREE.**
Equation (1.1) holds with all the quantifiers in Section 1.

### Proof

For a periodic sequence, Fourier inversion writes the generating
series as a sum of fractions \(C_j/(1-\zeta_b^jT)\).
Distinct roots \(\zeta_b^j\) give distinct simple poles, so the reduced
denominator degree is exactly the number of nonzero \(C_j\).
This also proves the minimal eventual recurrence assertion.

If \(x=\lambda/2\) is not a positive integer, Section 4 shows that
every nonzero mode survives. The zero mode is positive, giving
degree \(b\).

If \(x=m\in\mathbb Z_{>0}\), exactly the modes with
\(\min(j,b-j)>m\) vanish. Counting the survivors gives
\(\min(b,2m+1)\). The permutation, shift, and scaling reduction in
Section 2 proves the same answer for every reduced \(a/b\).
\(\square\)

Equivalently, the \(b\times b\) circulant matrix

\[
D_\lambda(r,l)=
\left|e^{2\pi i r/b}-e^{2\pi i l/b}\right|^\lambda
=2^\lambda\left|\sin\frac{\pi(r-l)}b\right|^\lambda
\tag{5.1}
\]

has rank \(b\) for positive real non-even \(\lambda\), and
\(\min(b,2m+1)\) for \(\lambda=2m\). Its inertia is determined by
(4.5), with two copies of every non-middle mode and one copy of
the even-\(b\) middle mode. This is a useful classical distance-matrix
interpretation, not a new arithmetic realization.

For a fixed positive real non-even exponent, **every** reduced rational
angle of denominator \(b\) needs exactly \(b\) scalar states. This
strengthens the earlier unboundedness conclusion to a sharp pointwise
degree formula. It does not exclude infinite-dimensional or
parameter-dependent models.

## 6. Why the real-exponent restriction is load-bearing

**Counterexample GLO764.COMPLEX_FULL_DEGREE_COUNTEREXAMPLE.**
Let

\[
b=4,\qquad
\lambda=2+\frac{4\pi i}{\log2}.
\tag{6.1}
\]

Then \(\operatorname{Re}\lambda=2>0\), but \(\lambda\) is not an
even integer. Nevertheless,

\[
\left(\frac1{\sqrt2}\right)^\lambda
=\exp(-\lambda\log2/2)=\frac12,
\tag{6.2}
\]

so the block in (2.1) is \((0,\tfrac12,1,\tfrac12)\), exactly
the block for exponent two. Its Fourier coefficients are
\((2,-1,0,-1)\), and its degree is three, not four.
The previous **uniform** complex-exponent theorem remains valid:
this one exceptional denominator does not supply a uniform bound.

Zero and negative exponents are outside (1.1). At \(\lambda=0\),
assigning value one to \(0^0\) yields the constant sequence, whereas
retaining value zero at the zero sample yields degree \(b\).
Neither convention may be silently substituted for (4.2).

## 7. Exact replay and source authentication

The companion producer uses integer cyclotomic arithmetic only.
For positive integer \(k\), put \(\eta=e^{2\pi i/(4b)}\). Then

\[
(2i)^k E_j(k/2)=
\sum_{l=0}^{b-1}\sum_{h=0}^k
 (-1)^h\binom kh
 \eta^{\,2l(k-2h)-4jl}.
\tag{7.1}
\]

Exponents are grouped modulo \(4b\). A mode vanishes exactly when
the resulting integer polynomial has zero remainder modulo the
cyclotomic polynomial \(\Phi_{4b}\). The producer constructs these
monic cyclotomic polynomials by exact division of \(X^n-1\);
there is no numerical trigonometry or tolerance.

The default rectangle is \(2\le b\le16,\ 1\le k\le8\).
Hard maxima are \(b\le24,\ k\le12\). Separate exact integer
quadrant tests check every sign-variation row through \(b=64\);
this is a regression on the proof's combinatorics, not a proof of
its infinite quantifier. Tests include held-out \(b=17,23\), exact
small cyclotomic polynomials, mutation refusals, and the complex
counterexample's rational block.

The declared work counter bounds grouped binomial additions,
polynomial-division coefficient updates, and the separately recorded
sign rows. It is not a RAM or bit-complexity measurement. A strict
exclusive cap and hard argument maxima are checked before the census.
The analytic noninteger-real statement is proved in Sections 3--5;
the producer does not evaluate or certify noninteger sine powers.

The manifest binds two source notes to their exact Git objects at
the source commit, their LF-normalized blob bytes, and their current
worktree bytes. The producer binds its own file, this note, the tests,
and the entire canonical fixture. A missing source, changed manifest,
stale fixture, invalid type, or reached cap fails closed.

    python research/l-families/atlas/generalized/rational_rotation_real_power_exact_degree.py --check
    python -O research/l-families/atlas/generalized/rational_rotation_real_power_exact_degree.py --check
    python -m unittest tests.test_rational_rotation_real_power_exact_degree
    python -O -m unittest tests.test_rational_rotation_real_power_exact_degree

## 8. Literature and next boundary

The generalized Descartes framework is classical; see G. J. O. Jameson,
[*Counting zeros of generalised polynomials: Descartes' rule of signs
and Laguerre's extensions*](https://www.cambridge.org/core/journals/mathematical-gazette/article/abs/counting-zeros-of-generalised-polynomials-descartes-rule-of-signs-and-laguerres-extensions/CCA0F4742F4040DE65C7378D337DE475),
The Mathematical Gazette 90 (518), 223--234 (2006),
DOI 10.1017/S0025557200179628. The publisher's metadata and extract
were checked; the full article was not used as a proof dependency.

Tanvi Jain's
[*Hadamard powers of some positive matrices*, Section 3](https://arxiv.org/html/1803.06803v1)
uses the same general Descartes/Fourier framework for entrywise
absolute cosine powers on odd grids and classifies eigenvalue zeros
and inertia. This is close primary prior art. The zero-containing
sine grids here are different, and the elementary parity argument
handles both odd and even denominators. This difference is not, by
itself, evidence of novelty.

The present proof is self-contained. Its ingredients, and potentially
the distance-matrix rank formula itself, belong to established
literature. No priority claim is made. A dedicated prior-art audit of
powered regular-polygon chord-distance matrices remains open.

The useful programme conclusion is precise: real non-even
coefficientwise absolute powers incur the full rational-orbit degree,
while polynomial powers retain bounded degree. Whether a larger
parent gives principled local and global structure is still an L4--L9
question, not answered by a finite scalar recurrence classification.
