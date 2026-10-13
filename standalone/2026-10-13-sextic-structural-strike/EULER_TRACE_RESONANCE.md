# A first-order positive resonance refutes the original unfiltered Euler trace

**Status:** proposed proved refutation of the original critical-line contract
P13 in PR #911, using its actual finite Euler polynomial and source row
majorant. The full norm-filtered inverse moments and RH remain open.

**Scope:** every fixed integer order \(k\ge1\), the admissible trivial
finite-order datum, one fixed legal cross-pair incidence allocation, and a
deterministic common conjugate frequency tending to zero. A slightly more
general theorem is proved for every fixed real part \(0<\sigma_0<1\);
the original P13 is its \(\sigma_0=1/2\) case.

**Exact source:** PR #911 at commit
`2f8b6a3898a722d0602a91dea73bac344a3bb7dd`,
`research/exploratory/2026-10-10-two-hour-continuation/literature/PRIME_SLOT_CANCELLATION.md`,
P1–P2 and P8. Its SHA-256 is
`d37ad696b46c7dda15a7faf314c46cda2d7d67e25ac8d3288c7f138aac373c13`.
The row majorant is the exact source specified in its P1 and P8: PR #914,
`standalone/2026-10-10-sextic-moment-conductor-core/CONDUCTOR_SECTORS.md`,
Section 2, at `0cc0428fedbbfc340044c7451b3d392c1da9a103`, SHA-256
`c160bbb1b1d7c6bcc5514d496ad41f15fd17ea3d36206b0d05cfa0d7d6503983`.
It chooses a fixed nonnegative radial smooth majorant which is at least
one on the unit disk. A compactly supported majorant is a permitted
Schwartz majorant.

The only imported analytic theorem is the classical prime ideal theorem
\(\pi_K(x)\sim x/\log x\) for the fixed Eisenstein field. A primary
account is Alex Burgin, *A New Elementary Proof of Landau's Prime Ideal
Theorem, and Associated Results*, [arXiv:2406.08565v2](https://arxiv.org/html/2406.08565v2),
Theorem 1, Lemma 1, and the explanation immediately after Lemma 1. No
quantitative effective error term is needed here. This note does not
reprove that theorem or assume RH or a subcritical zero-free line.

## 1. The contract and the literal finite polynomial

Let \(K=\mathbb Q(\sqrt{-3})\), let \(S\) be the fixed source set of
excluded primes, and take the allowed datum \(\nu=1\). Write
\(q_p=Np\). For a nonzero row \(u\), the left-slot character is
\(\theta_{i,u}(p)=\chi_p(u)\) and the right-slot character is its
conjugate. The nonunit value is exactly zero. For a squarefree incidence
mask \(Q\), the finite polynomial in P2 is

\[
 \mathcal C_{2k,Y,Q,u}(\mathbf s)
 =\prod_{\substack{q_p\le Y\\p\nmid SQ}}
       \left(1-\sum_{i=1}^{2k}\theta_{i,u}(p)q_p^{-s_i}\right).
 \tag{1.1}
\]

The original P13 asks for

\[
 \left|\sum_{u\ne0}\Phi(u/\sqrt H)\omega_{\mathbf q}(u)
       \mathcal C_{2k,Y,Q,u}(1/2+i\mathbf t)\right|
 \ll_\epsilon HD^\epsilon\prod_i(1+|t_i|)^B,
 \qquad Y=bD,\quad H=D^h,
 \tag{1.2}
\]

uniformly over every independent frequency and every eligible incidence
allocation. The source range is \(1<h\le11/10\). There are no physical
column norm tests inside the trace (1.2). They are applied only in its
subsequent complete Mellin integral.

## 2. The general positive-resonance theorem

### Theorem 2.1. Failure of every polynomial bound below real part one

Fix \(k\ge1\), \(0<\sigma_0<1\), \(h>0\), and \(b>0\). There is a
fixed eligible incidence allocation, and constants \(c>0,Y_0\), such
that for every \(Y\ge Y_0\), with \(D=Y/b\), \(H=D^h\), and

\[
 t_Y=\frac{\pi}{\log Y},\qquad
 \mathbf t_Y=(\underbrace{t_Y,\ldots,t_Y}_{k},
              \underbrace{-t_Y,\ldots,-t_Y}_{k}),
 \tag{2.1}
\]

the complete source trace satisfies

\[
 \boxed{\quad
 \sum_{u\ne0}\Phi(u/\sqrt H)\omega_{\mathbf q}(u)
      \mathcal C_{2k,Y,Q,u}(\sigma_0+i\mathbf t_Y)
 \ge \exp\!\left(c\frac{Y^{1-\sigma_0}}{\log Y}\right).
 \quad}
 \tag{2.2}
\]

Every summand on the left is nonnegative and real. Consequently, at
\(\sigma_0=1/2\), the original P13 is false for every fixed \(k\ge1\).
Enlarging its right side by any fixed power of \(D\) does not repair it.
The frequency in (2.1) is explicitly prescribed; no search or interpolation
is needed for this theorem.

**Proof.** Choose a fixed \(P_0\) so large that

\[
 2kq^{-\sigma_0}\le\frac12\qquad(q>P_0).
 \tag{2.3}
\]

For example, \(P_0=(4k)^{1/\sigma_0}\) suffices. Let \(Q\) be the
product of all prime ideals outside \(S\) with norm at most \(P_0\).
This is a fixed squarefree ideal, not a parameter changing with \(Y\).
Use the actual cross-pair allocation

\[
 q_{\{1,k+1\}}=Q,\qquad q_I=1\quad(I\ne\{1,k+1\}).
 \tag{2.4}
\]

All allocation ideals are pairwise coprime. The source column masks are
\(c_1=c_{k+1}=Q\) and \(c_i=1\) otherwise, so the allocation is
eligible once \(Y\ge NQ\). The exterior row multiplier and source signs
are exactly

\[
 \omega_{\mathbf q}(u)=\chi_Q(u)\overline{\chi_Q(u)}
 =\mathbf1_{(u,Q)=1},\qquad \mu_K(Q)^2=1.
 \tag{2.5}
\]

For arbitrary paired frequencies \(t_{k+j}=-t_j\), every eligible prime
outside the row has local numerator

\[
 1-2q_p^{-\sigma_0}\Re\sum_{j=1}^k
           \chi_p(u)e^{-it_j\log q_p}
 \ge1-2kq_p^{-\sigma_0}\ge\frac12.
 \tag{2.6}
\]

A prime dividing \(u\) contributes one, since all of its slot values are
zero. Thus the actual finite polynomial is positive on every row, on
the whole paired plane. Combined with (2.5) and \(\Phi\ge0\), this
proves positivity of every summand. The trace is well defined: for fixed
\(Y\), the finite product is uniformly bounded in \(u\) by
\(\prod_{q_p\le Y}(1+2kq_p^{-\sigma_0})\), and the fixed Schwartz
majorant has an absolutely convergent lattice sum.

It remains to lower-bound only the retained row \(u=1\), whose spatial
weight is at least one once \(H\ge1\). At (2.1), this row has

\[
 \mathcal C_{2k,Y,Q,1}
 =\prod_{\substack{q_p\le Y\\p\nmid SQ}}
       \left[1-2kq_p^{-\sigma_0}
          \cos\left(\frac{\pi\log q_p}{\log Y}\right)\right].
 \tag{2.7}
\]

Put \(a=3/4\). For \(Y^a<q_p\le Y\), the cosine argument lies in
\((3\pi/4,\pi]\), where the cosine is at most \(-1/2\). Therefore,
writing \(x=q_p^{-\sigma_0}\),

\[
 \log\left[1-2kx\cos\left(\frac{\pi\log q_p}{\log Y}\right)\right]
 \ge\log(1+kx)\ge\frac{k}{2}x.
 \tag{2.8}
\]

Here \(0\le kx\le1/4\), by (2.3), and
\(\log(1+z)\ge z/2\) for \(0\le z\le1\). For every smaller eligible
prime, irrespective of the cosine's sign,

\[
 \log\left[1-2kx\cos\left(\frac{\pi\log q_p}{\log Y}\right)\right]
 \ge\log(1-2kx)\ge-4kx,
 \tag{2.9}
\]

using \(\log(1-z)\ge-2z\) for \(0\le z\le1/2\). These are exact
inequalities; no expansion remainder or implicit summability at an
endpoint is needed. For large \(Y\), fixed excluded primes lie below
\(Y^a\). Equations (2.8)–(2.9) yield

\[
 \log\mathcal C_{2k,Y,Q,1}
 \ge\frac{k}{2}\sum_{Y^a<q_p\le Y}q_p^{-\sigma_0}
       -4k\sum_{q_p\le Y^a}q_p^{-\sigma_0}.
 \tag{2.10}
\]

The prime ideal theorem gives \(\gg_KY/\log Y\) prime ideals in
\([Y/2,Y]\). For large \(Y\), that interval is contained in
\((Y^a,Y]\), and every weight there is at least \(Y^{-\sigma_0}\).
Hence the first sum in (2.10) is at least

\[
 c_K\frac{Y^{1-\sigma_0}}{\log Y}.
 \tag{2.11}
\]

The elementary ideal count \(J(x)\ll_K x\), followed by partial
summation, bounds the second sum by

\[
 \sum_{Nn\le Y^a}(Nn)^{-\sigma_0}
 \ll_{K,\sigma_0}Y^{a(1-\sigma_0)}
 =o\!\left(\frac{Y^{1-\sigma_0}}{\log Y}\right).
 \tag{2.12}
\]

The strict inequalities \(a<1\) and \(\sigma_0<1\) are used exactly
here. Absorb the smaller negative term into (2.11), and exponentiate.
The complete nonnegative trace is at least this unit-row contribution,
proving (2.2). \(\square\)

## 3. Exact consequence for P13

Set \(\sigma_0=1/2\). The left side of the original P13 at (2.1) is at
least

\[
 \exp\!\left(c\frac{\sqrt Y}{\log Y}\right).
 \tag{3.1}
\]

For any fixed finite exponents \(A,B\), \(H=D^h\) and \(Y=bD\),

\[
 HD^A\prod_{i=1}^{2k}(1+|t_{i,Y}|)^B=O_{k,A,B,b,h}(Y^{h+A}).
 \tag{3.2}
\]

The exponential lower bound exceeds (3.2) eventually, independently of
how large the fixed polynomial loss is. This refutes P13 with its full
source uniformity. The fixed cross-pair mask is legal even at \(k=1\).
No exceptional set of rows is removed: positivity was proved for every
row, and the lower bound uses one row of the complete trace.

All the left frequencies in (2.1) are the same and all the right
frequencies are their negatives. The resonance therefore lies on the
exact common conjugate slice, not merely near it. This does not contradict
P5's inverse-logarithmic estimate: P5 bounds the collision ratio

\[
 Q_{\rm coll}=\mathcal C/\prod_i B_i,
\]

whereas P13 concerns \(\mathcal C\) itself. The individual finite Euler
factors \(B_i\) are not controlled by that ratio estimate. A small ratio
can coexist with an exponentially large numerator.

## 4. Separation from the second-order short-trace refutation

The proposed subcritical CT1 of `COMPLEMENTARY_SHORT_TRACE_CONTRACT.md`
is a different object, \(Q_{\rm coll}\prod_iT_{i,Y}\), with each
individual Euler factor replaced by its literal short Möbius polynomial.
The first-order argument above does not by itself prove that CT1 is false.
For the short trace, one needs the separate opposite-cluster collision
growth and simultaneous non-smallness of the short factors. Those are
the components in `RESONANT_SHORT_TRACE.md` and
`SHORT_FACTOR_NONSMALLNESS.md`.

The two proofs expose two different failures of pointwise unfiltered
targets. For the original Euler numerator the leading prime degree
already produces the exponential growth. For the short representation
that degree has been removed, but the second prime degree produces a
new positive resonance in its complementary frequencies.

Neither theorem refutes the full source norm-filtered moment or the exact
Mellin representations. The original finite Euler polynomial contains
products of prime ideals with norms far beyond each physical column
horizon. The smooth column tests remove those coefficients only after
the complete multivariate Mellin operation. The source distinguishes
this full filtering from a pointwise estimate for its integrand; the
counterexample relies on precisely that distinction.

## 5. Verification and independence boundary

The proof was derived by the extraction agent while reviewing the root's
second-order CT1 proof. That agent previously authored the short-factor
non-smallness lemma and contributed early collision calculations. These
are collaborative contributions, not fully independent discoveries.

The source specialization, exact local signs, logarithm inequalities,
prime-weight comparison, and final quantifiers were reconstructed
symbolically. No finite numerical experiment is used to infer (2.2), and
no useful effective value of \(Y_0\) is claimed. The imported prime ideal
theorem has been checked at the stated primary source but not reproved.
The threshold can depend on fixed \(k,\sigma_0,S,Q,b,h\); no uniformity
as \(k\to\infty\) or \(\sigma_0\uparrow1\) is asserted.
