# A resonant positive trace refutes the proposed subcritical unfiltered contract

**Status:** proposed proved refutation of the particular open contract CT1 in
PR #911. The native, norm-filtered generalized moment and RH remain open.
The result applies at every fixed moment order \(k\ge2\), with the actual
Möbius coefficients, the original nonunit zeros, a permitted fixed incidence
allocation, and the source's nonnegative row majorant. It is an asymptotic
counterexample to an auxiliary analytic target, not to the moment conjecture.

**Sources:** PR #911 at `2f8b6a3898a722d0602a91dea73bac344a3bb7dd`,
especially the preserved [CT1 contract](sources/pr911/COMPLEMENTARY_SHORT_TRACE_CONTRACT.md),
[SC2 short polynomials](sources/pr911/SHORT_POLYNOMIAL_COLLISION_TRANSPORT.md),
and [WT1 frequency tube](sources/pr911/WIDE_SUBCRITICAL_TUBE.md).
The source majorant is PR #914, `CONDUCTOR_SECTORS.md`, Section 2,
at `0cc0428fedbbfc340044c7451b3d392c1da9a103`: it is nonnegative and
at least one on the unit disk. Exact local copies and hashes are recorded
in the packet manifest. The only prime-distribution input is the classical
prime ideal theorem for the fixed Eisenstein field. The proof does not use
the imported theta foundation, a native moment estimate, or a zero-free
half-plane beyond the classical theorem at real part one.

## 1. The exact object being tested

Fix \(K=\mathbb Q(\sqrt{-3})\), the admissible trivial source datum
\(\nu=1\), a fixed bad-prime set \(S\), and a real number
\(1/3<\sigma<1/2\). Let \(k\ge2\) be fixed and put \(r=2k\).
For a squarefree incidence mask \(Q\), the actual finite factors are

\[
\begin{aligned}
B_{i,Y,u}(s_i)&=\prod_{\substack{Np\le Y\\p\nmid SQ}}
       (1-\theta_{i,u}(p)(Np)^{-s_i}),\\
\mathcal C_{Y,u}(\mathbf s)&=\prod_{\substack{Np\le Y\\p\nmid SQ}}
       \left(1-\sum_{i=1}^{2k}\theta_{i,u}(p)(Np)^{-s_i}\right),\\
Q_{\rm coll,Y,u}(\mathbf s)&=
        \mathcal C_{Y,u}(\mathbf s)/\prod_i B_{i,Y,u}(s_i),\\
T_{i,Y,u}(s_i)&=\sum_{\substack{Nn\le Y\\(n,SQ)=1}}
       \mu_K(n)\theta_{i,u}(n)(Nn)^{-s_i}.
\end{aligned}
\tag{1.1}
\]

Here \(\theta_{i,u}=\chi_{(\cdot)}(u)\) on the left and its conjugate
on the right. Their value is literally zero at a prime dividing \(u\).
Every denominator in (1.1) is nonzero when the real parts are positive.
The collision factor (Q_{\rm coll}\) is different from the ideal \(Q\).

For an actual incidence allocation \(\mathbf q\), CT1 asks for a
polynomial bound, uniformly in every independent frequency, for

\[
\mathcal T_Y(\mathbf t)=
 \sum_{u\ne0}\Phi(u/\sqrt H)\omega_{\mathbf q}(u)
 Q_{\rm coll,Y,u}(\sigma+i\mathbf t)
 \prod_{i=1}^{2k}T_{i,Y,u}(\sigma+it_i),
\qquad Y=bD,
\quad H=D^h.
\tag{1.2}
\]

The displayed sum has **no column norm tests inside it**. They enter only
in the later complete multivariate Mellin integral. This distinction is
the source of the counterexample.

### Theorem 1.1. Superpolynomial positive resonances

For every fixed \(k\ge2\), \(1/3<\sigma<1/2\), and fixed \(h>0\),
there is a fixed permitted incidence allocation \(\mathbf q\), constants
\(c>0,Y_0\), and, for every \(Y\ge Y_0\), an explicitly prescribed finite
grid containing a frequency vector \(\mathbf t_Y\), such that

\[
\boxed{
\mathcal T_Y(\mathbf t_Y)
 \ge \exp\!\left(c\frac{Y^{1-2\sigma}}{\log Y}\right).
}
\tag{1.3}
\]

Every component of \(\mathbf t_Y\) is \(O_k(1/\log Y)\). The vector
lies outside every WT1 common conjugate tube with its stated admissible
width. The trace at this vector is a sum of nonnegative real terms.
Consequently CT1 is false, even if its right side is enlarged to

\[
CHD^a\prod_i(1+|t_i|)^B
\tag{1.4}
\]

for any fixed finite \(a,B,C\). In particular, allowing a fixed power
loss does not repair that contract. The original CT range
\(1<h\le11/10\) is contained in the theorem's range.

## 2. A legal mask makes the entire paired trace positive

Choose a fixed number \(P_0\) so large that

\[
2k\,q^{-\sigma}\le\tfrac12\qquad(q>P_0).
\tag{2.1}
\]

Let \(Q\) be the product of every prime ideal outside \(S\) of norm
at most \(P_0\). This is one fixed squarefree ideal, independent of \(Y\).
Use the exact allocation

\[
q_{\{1,k+1\}}=Q,\qquad q_I=1\quad(I\ne\{1,k+1\}).
\tag{2.2}
\]

It obeys the pairwise-coprime allocation rule. Its column masks are
\(c_1=c_{k+1}=Q\) and every other \(c_i=1\), so it is eligible once
\(Y\ge NQ\). Its exterior row multiplier is exactly

\[
\omega_{\mathbf q}(u)=\chi_Q(u)\overline{\chi_Q(u)}
=\mathbf1_{(u,Q)=1}.
\tag{2.3}
\]

The exterior Möbius sign has even multiplicity and is also one. Thus this
is an actual cross-pair allocation, rather than an arbitrarily introduced
row selector or moving source datum.

Take any paired frequencies, with \(t_{k+j}=-t_j\). At each eligible
prime with \(p\nmid u\), write \(x=(Np)^{-\sigma}\) and
\(v_j=\chi_p(u)e^{-it_j\log Np}\). The (2k\) normalized local variables
are \(v_1,\ldots,v_k,\overline v_1,\ldots,\overline v_k\). Hence

\[
1-x\sum_{i=1}^{2k}v_i
=1-2x\Re\sum_{j=1}^k v_j\ge1-2kx\ge\tfrac12,
\qquad
\prod_i(1-xv_i)=\prod_{j=1}^k|1-xv_j|^2>0.
\tag{2.4}
\]

At \(p\mid u\), the local factor equals one exactly. Therefore
\(Q_{\rm coll,Y,u}>0\) for every row on the entire paired plane.
The short factors satisfy

\[
\prod_{i=1}^{2k}T_{i,Y,u}(\sigma+it_i)
=\prod_{j=1}^k|T_{Y,u}(\sigma+it_j)|^2\ge0.
\tag{2.5}
\]

Together with (2.3) and \(\Phi\ge0\), this proves that **every summand**
of (1.2) is nonnegative. The unit row \(u=1\) is retained with weight
at least one whenever \(H\ge1\). No assumption about cancellation among
other rows is needed for a lower bound from that one row.

## 3. The opposite phase clusters produce exponential collision growth

Put

\[
n_+=\lceil k/2\rceil,\qquad n_-=\lfloor k/2\rfloor,
\qquad d=n_+-n_-\in\{0,1\},
\qquad\gamma=k-2d^2>0.
\tag{3.1}
\]

Take \(n_+\) left frequencies equal to \(t\), and \(n_-\) equal to
\(t+\delta_Y\), where

\[
\delta_Y=\frac{\pi}{\log Y},\qquad
|t|\le\frac{\varepsilon_k}{\log Y},\qquad
\varepsilon_k=\frac1{100k^2},\qquad
a_k=1-\frac1{100k^2}.
\tag{3.2}
\]

The right frequencies are their negatives. On row one every character
value is one. At primes in \([Y^{a_k},Y]\), the corresponding normalized
variables are uniformly close to the vector with \(2n_+\) entries (+1\)
and \(2n_-\) entries \(-1\). For that exact vector, the pair sum is

\[
\sum_{i<j}v_iv_j
=\frac{(2d)^2-2k}{2}=-\gamma.
\tag{3.3}
\]

For the actual variables, each distance to its designated sign is at most
\((1+\pi)/(100k^2)\): use \(|e^{ix}-e^{iy}|\le|x-y|\),
\(|t\log Np|\le\varepsilon_k\), and
\(\pi a_k\le\delta_Y\log Np\le\pi\). Each pair changes by at most
twice that distance. Thus

\[
\left|\sum_{i<j}v_iv_j+\gamma\right|
\le\frac{2\binom{2k}{2}(1+\pi)}{100k^2}
<\frac15<\frac\gamma2.
\tag{3.4}
\]

Here \(\pi<4\) suffices for the strict (1/5\) bound. The pair sum is
real on the paired plane. It follows that it is at most \(-\gamma/2\)
throughout the specified interval of \(t\) and range of prime norms.

The real logarithm of the positive local collision factor has the expansion

\[
\log\frac{1-x\sum_i v_i}{\prod_i(1-xv_i)}
=-x^2\sum_{i<j}v_iv_j+O_k(x^3).
\tag{3.5}
\]

This follows by expanding the logarithms under (2.1); the degree-one terms
cancel, and the degree-two identity is
\(((\sum_i v_i)^2-\sum_i v_i^2)/2=\sum_{i<j}v_iv_j\).
The denominator logarithms may first be paired as
\(2\Re\log(1-xv_j)\), so there is no branch ambiguity. The remainder
is uniform in the phases and is summable over prime ideals because
\(3\sigma>1\).

Let \(\rho=1-2\sigma>0\). Summing (3.5), bounding the pair sum in
absolute value below \(Y^{a_k}\), and using (3.4) above that point gives

\[
\log Q_{\rm coll,Y,1}
\ge \frac\gamma2\sum_{Y^{a_k}<Np\le Y}(Np)^{-2\sigma}
-C_k\sum_{Np\le Y^{a_k}}(Np)^{-2\sigma}-O_{k,\sigma,Q}(1).
\tag{3.6}
\]

The classical fixed-field prime ideal theorem
\(\pi_K(x)\sim x/\log x\) implies

\[
\sum_{Y^{a_k}<Np\le Y}(Np)^{-2\sigma}
\ge c_{K,\sigma}\frac{Y^{\rho}}{\log Y}.
\tag{3.7}
\]

Indeed, for large \(Y\), the interval \([Y/2,Y]\) is contained in the
displayed range and has \(\gg_K Y/\log Y\) prime ideals; each has weight
at least \(Y^{-2\sigma}\). Fixed deleted primes have disappeared below
the lower endpoint. Elementary ideal counting bounds the second sum in
(3.6) by \(O(Y^{a_k\rho})\). Since \(a_k<1\) is fixed, this is
\(o(Y^\rho/\log Y)\). Consequently, uniformly for the full interval
in (3.2),

\[
\boxed{
Q_{\rm coll,Y,1}\ge
\exp\!\left(c_{k,\sigma}\frac{Y^{1-2\sigma}}{\log Y}\right)
}
\tag{3.8}
\]

for all sufficiently large \(Y\). A primary account of the classical
prime input is A. Burgin, *A New Elementary Proof of Landau's Prime Ideal
Theorem, and Associated Results*, [arXiv:2406.08565v2](https://arxiv.org/html/2406.08565v2),
Theorem 1 and Lemma 1. This packet imports the prime ideal theorem; it
does not claim to reconstruct that theorem's proof.

## 4. The actual Möbius factors cannot neutralize every resonance

At row one define the literal short polynomial

\[
T_Y(s)=\sum_{\substack{Nn\le Y\\(n,SQ)=1}}\mu_K(n)(Nn)^{-s},
\qquad
F_Y(s)=T_Y(s)^{n_+}T_Y(s+i\delta_Y)^{n_-}.
\tag{4.1}
\]

[SHORT_FACTOR_NONSMALLNESS.md](SHORT_FACTOR_NONSMALLNESS.md), Theorem 2.1,
proves the following elementary and uniform fact. For any fixed product
of \(k\) such factors, there is a predetermined \(O_k(\log Y)\) grid in
\(|t|\le\varepsilon_k/(2\log Y)\) containing a point \(t_Y\) at which

\[
|F_Y(\sigma+it_Y)|\ge
\exp[-C_{k,\sigma}\log Y\log\log Y].
\tag{4.2}
\]

For clarity, the mechanism is not an assumed Möbius lower bound. Each
short factor is within (1/4\) of one at real part four, uniformly in
all rows and all exclusions. The product therefore has modulus at least
\((3/4)^k\) there. Its (N\)-th derivative in \(\Re s\ge\sigma\) is
bounded by \(C_{k,\sigma}Y^{k(1-\sigma)}(k\log Y)^N\).
Lagrange interpolation from (N=\lceil100k\log Y\rceil\) nearby nodes
to real part four has remainder (o(1)\) and amplification
\(\exp[O_k(\log Y\log\log Y)]\). Thus all those actual polynomial
values cannot be smaller than (4.2). The proof handles the product at
once, so zeros of one factor at other points cause no gap.

At the vector obtained from this \(t_Y\), (2.4)–(2.5), the retained unit
row, (3.8), and (4.2) imply

\[
\mathcal T_Y(\mathbf t_Y)
\ge Q_{\rm coll,Y,1}|F_Y(\sigma+it_Y)|^2
\ge \exp\!\left(c\frac{Y^{\rho}}{\log Y}
                   -C\log Y\log\log Y\right).
\tag{4.3}
\]

The second exponent is negligible compared with the first. Decrease the
positive constant to obtain (1.3).

Both frequency groups are nonempty. Their separation is
\(\pi/\log Y\). Membership of a WT1 common conjugate tube would require
every left frequency to be within \(\kappa/\log Y\) of one center and
therefore require \(\pi\le2\kappa\). The source allows only
\(0<\kappa<\arcsin(1/\sqrt{2k})<\pi/2\), so this is impossible.
All chosen frequencies themselves tend to zero. Hence the fixed polynomial
frequency factor in (1.4) is bounded, whereas (1.3) exceeds every power
of \(Y\). This completes the proof. \(\square\)

## 5. What is refuted, and what survives

The refutation is of the actual **unfiltered short trace CT1** with its
full stated uniformity. It is not merely a large local factor, a formal
arbitrary-vector model, a bound on selected rows after taking an absolute
value, or a finite numerical witness. Every row in the complete trace is
nonnegative at the chosen paired vectors, which is why the native unit
row provides a valid lower bound.

The earlier SC4 identity remains correct: applying **all** the physical
column norm tests to the complete multivariate integral recovers the finite
source coefficients. The short factors and the original Euler factors
agree only after this filtering. The enormous values in (4.3) can come
from coefficients outside the physical column horizons and must cancel
in the complete filtered representation. They imply no lower bound for
that norm-filtered integral. The paired locus has smaller dimension than
the full independent-frequency space, and no passage from this locus to a
signed full-dimensional integral is made.

The rapid suppression on the earlier common conjugate tube also survives:
our two opposite phase clusters are outside that tube. The mistake would
be to treat a negligible partial integral as evidence that its pointwise
complement has a polynomial bound. The exact factorization has introduced
a much more unstable integrand than the physical moment.

The critical-line contract P13 in `PRIME_SLOT_CANCELLATION.md` is a
different statement. At \(\sigma=1/2\), the present exponential mechanism
becomes logarithmic and does not refute P13. Nor is a scalar reciprocal
bound, a filtered trace estimate, or the full generalized moment refuted.

For further attacks, the norm horizons must be retained inside the object
being estimated, or the complete frequency cancellation must be proved
before absolute values. Merely enlarging the fixed power allowed by CT1,
or discarding a small number of resonant sample points, does not repair the
uniform contract that this proof contradicts.

## 6. Quantifiers and verification boundary

The ideal \(Q\), the order \(k\), \(\sigma\), and all source data are
fixed before \(Y\to\infty\). The threshold (Y_0\) may be very large
and depends on those data; no effective useful threshold is claimed.
The successful frequency is chosen from a predetermined grid for each
\(Y\). This is sufficient to contradict a bound asserted for every
frequency and every large scale. No uniformity as \(\sigma\uparrow1/2\)
or \(k\to\infty\) is asserted.

The mathematical proof consists of legal source specialization, exact
positivity, a uniform Taylor expansion, the named classical prime ideal
theorem, and elementary analytic interpolation. Finite diagnostics only
check the local algebra and the finite constants; they do not establish
the asymptotic prime input or the moment conjecture. Separate reviewers
must reconstruct the full composition at its frozen file hash.
