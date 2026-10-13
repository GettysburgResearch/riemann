# Short Möbius products cannot cancel an exponential collision at every nearby frequency

**Status:** a proved elementary analytic component for the audit of the open
complementary short-trace contract in PR #911. No native moment bound or new
zero-free half-plane is asserted here. The collision lower bound and the
composition with the actual row trace are separate obligations, owned by the
root researcher.

**Scope:** every literal norm-truncated Eisenstein Möbius polynomial in SC2,
uniformly in its nonzero arithmetic row, its finite or moving exclusions,
and all permitted finite-order coefficient phases. The proof uses only the
constant coefficient, the coefficient modulus bound, ideal counting, and
complex polynomial interpolation. It requires no Möbius cancellation,
zero-free region, prime ideal theorem, or nonvanishing of a short polynomial
on the subcritical line.

**Exact sources inspected:**

- PR #911, commit `2f8b6a3898a722d0602a91dea73bac344a3bb7dd`,
  `research/exploratory/2026-10-10-two-hour-continuation/literature/SHORT_POLYNOMIAL_COLLISION_TRANSPORT.md`,
  SC1–SC6, Git blob `8c4e6ebd47380578f82ac1720ac4f83a3f1a053d`.
- The same commit and directory,
  `COMPLEMENTARY_SHORT_TRACE_CONTRACT.md`, CT1–CT5, Git blob
  `34a04d5ac549264b6b620d0d52fe000e069da164`.
- The same commit and directory, `PRIME_SLOT_ROUTE_STATUS.md`, Git blob
  `17126bb5664d4c335a89409d45323462783ebc1f`.
- PR #929, commit `97bf40329489992e9384c34d7595af6d01a40774`,
  `standalone/2026-10-10-conductor-averages/GAUSSIAN_SAMPLED_MOMENTS.md`,
  Git blob `31c446ef6dce84a38cdf5d7024b75da56d1e9af2`.
- PR #926, commit `086bf0560c0c2679a1fe41418f583d2c5ca743c3`,
  `standalone/2026-10-10-mobius-overlaps-and-sampled-moments/SAMPLED_MOMENT_CRITERION.md`,
  Git blob `ccb083b8bfd2e3c015c9a8aad5b27ba2754243a4`.

The last two sources motivated the use of explicit high-order interpolation.
Their sampling theorems do not supply an arithmetic moment estimate. The
present result is a lower bound for the actual short factor in a proposed
upper-bound contract, so its use is logically different.

## 1. Literal polynomials and a uniform absolute-chamber anchor

Let \(K=\mathbb Q(\sqrt{-3})\). All indices below are nonzero integral
ideals, with norm \(Nn\). For \(Y\ge3\), let

\[
 T_{j,Y}(s)=\sum_{Nn\le Y} a_j(n)(Nn)^{-s},\qquad
 a_j(1)=1,\quad |a_j(n)|\le1.
 \tag{1.1}
\]

Coefficients are attached to individual ideals; equal norm ideals remain
separate. They may depend on the row, the exclusions, and \(Y\). No
multiplicativity is needed for this lemma. The actual SC2 coefficients
\(\mu_K(n)\theta_j(n)\mathbf1_{(n,SQ)=1}\) satisfy (1.1), including the
literal zero at a nonunit row. Thus the stronger coefficient quantifier of
the analytic lemma causes no change of source in its application.

### Lemma 1.1. A common, row-uniform anchor

For every real \(\tau\), every \(Y\), and every polynomial (1.1),

\[
 |T_{j,Y}(4+i\tau)-1|\le\frac{505}{2304}<\frac14,
 \qquad |T_{j,Y}(4+i\tau)|\ge\frac34.
 \tag{1.2}
\]

**Proof.** The number of ideals of integer norm \(n\) is at most the ordinary
divisor function \(d(n)\). This follows prime by prime: a split rational
prime contributes \(a+1\) ideals of norm \(p^a\); an inert prime contributes
one for even \(a\) and none for odd \(a\); a ramified prime contributes one.
Consequently

\[
 \sum_{n\ne1}(Nn)^{-4}=\zeta_K(4)-1\le\zeta(4)^2-1.
\]

The decreasing-integral estimate gives

\[
 \zeta(4)\le1+2^{-4}+\int_2^\infty x^{-4}\,dx
 =\frac{53}{48}.
\]

Therefore \(\zeta_K(4)-1\le(53/48)^2-1=505/2304<1/4\).
Take absolute values of all nonconstant terms in (1.1). This estimate is
uniform in the phases, all deletions, the row, the cutoff, and \(\tau\).
The reverse triangle inequality proves the second assertion. \(\square\)

Choosing the anchor at real part four avoids any need to identify a
limiting Euler product, control a moving conductor, or assume that the
anchor polynomial is nonzero because of its eventual limit.

## 2. A uniform lower bound on a shrinking interval

Fix an integer \(m\ge1\), \(0<\sigma<1\), and \(\epsilon>0\). Let
\(\tau_1,\ldots,\tau_m\) be any real numbers, possibly depending on \(Y\),
the row, and the coefficients. Define the entire function

\[
 F_Y(s)=\prod_{j=1}^{m}T_{j,Y}(s+i\tau_j).
 \tag{2.1}
\]

### Theorem 2.1. Small-interval non-smallness, uniform in all source rows

There are constants \(C>0\) and \(Y_0\), depending only on
\(K,m,\sigma,\epsilon\), such that for \(Y\ge Y_0\),

\[
 \boxed{\quad
 \sup_{|t|\le\epsilon/\log Y}
       |F_Y(\sigma+it)|
 \ge \exp[-C\log Y\log\log Y].
 \quad}
 \tag{2.2}
\]

One may choose a point from a predetermined grid of
\(N=\lceil100m\log Y\rceil\) nodes inside
\([ -\epsilon/(2\log Y),\epsilon/(2\log Y)]\). The grid is independent
of all arithmetic coefficients and all shifts \(\tau_j\); the successful
node may depend on them.

**Proof.** Ideal counting gives \(J(x)\le C_Kx\), so partial summation
gives, for the fixed \(0<\sigma<1\),

\[
 \sum_{Nn\le Y}(Nn)^{-\sigma}\le C_{K,\sigma}Y^{1-\sigma}.
 \tag{2.3}
\]

Expand the finite product (2.1) into ordered \(m\)-tuples of ideals. All
of its frequencies are \(\log\prod_j Nn_j\), between zero and
\(m\log Y\). For every integer \(N\ge1\) and every \(s\) with
\(\Re s\ge\sigma\),

\[
 |F_Y^{(N)}(s)|
 \le C_{K,\sigma}^{m}Y^{m(1-\sigma)}(m\log Y)^N.
 \tag{2.4}
\]

The imaginary shifts are unimodular in this expansion and do not affect
the bound. This is a bound for every derivative order with an explicit
dependence on \(N\), not an unspecified smoothness constant.

Put \(N=\lceil100m\log Y\rceil\), and define

\[
 t_j=-\frac{\epsilon}{2\log Y}
       +\frac{j\epsilon}{(N-1)\log Y},\quad
 z_j=\sigma+it_j,\qquad 0\le j<N.
 \tag{2.5}
\]

For sufficiently large \(Y\), all \(|t_j|\le1\), and
\(|4-z_j|\le5\). Interpolate \(F_Y\) at these \(N\) complex nodes by
a polynomial \(P\) of degree at most \(N-1\), and evaluate at the real
point four. The convex hull of the nodes and four lies in
\(\Re s\ge\sigma\). The complex divided-difference integral formula
therefore gives

\[
 |F_Y(4)-P(4)|
 \le \frac{1}{N!}\sup_{\operatorname{conv}\{4,z_0,\ldots,z_{N-1}\}}
                 |F_Y^{(N)}|
       \prod_{j=0}^{N-1}|4-z_j|
 \le C_{K,\sigma}^mY^{m(1-\sigma)}
          \left(\frac{5em\log Y}{N}\right)^N.
 \tag{2.6}
\]

For completeness, the divided-difference formula is valid for complex
nodes in a convex domain: repeated use of the fundamental theorem of
calculus along straight segments writes an \(N\)-th divided difference
as the integral of \(F_Y^{(N)}\) over the barycentric simplex. Its volume
is \(1/N!\). No real mean-value point for a complex function is assumed.
The interpolation remainder is that divided difference times
\(\prod_j(4-z_j)\). The last inequality also uses
\(N!\ge(N/e)^N\).

Since \(N\ge100m\log Y\), the ratio inside (2.6) is at most
\(e/20<3/20\). Thus (2.6) is \(o(1)\), uniformly in all coefficients,
shifts, and rows. Lemma 1.1 gives
\(|F_Y(4)|\ge(3/4)^m\). After increasing \(Y_0\),

\[
 |P(4)|\ge\tfrac12(3/4)^m=:c_m>0.
 \tag{2.7}
\]

Let \(\Delta=\epsilon/((N-1)\log Y)\). The Lagrange basis satisfies

\[
 \sum_{j=0}^{N-1}|L_j(4)|
 \le(5/\Delta)^{N-1}
       \sum_{j=0}^{N-1}\frac1{j!(N-1-j)!}
 =\frac{[10(N-1)\log Y/\epsilon]^{N-1}}{(N-1)!}
 \le\left(\frac{10e\log Y}{\epsilon}\right)^{N-1}.
 \tag{2.8}
\]

The factorial identity in the middle is the binomial theorem. Hence

\[
 \max_{0\le j<N}|F_Y(z_j)|
 \ge c_m\left(\frac{\epsilon}{10e\log Y}\right)^{N-1}.
 \tag{2.9}
\]

As \(N=O_m(\log Y)\), the right side is at least
\(\exp[-C\log Y\log\log Y]\) for all sufficiently large \(Y\).
The nodes are inside the required interval. \(\square\)

The fact that an individual factor might have a zero on the interval is
irrelevant: the proof controls the product and supplies a node where all
its factors are simultaneously non-small in the product sense.

### Corollary 2.2. The specific fourth-moment pair

Let \(T_Y\) be the actual SC2 polynomial for any chosen row and any
exclusion set, and let \(\delta_Y=\pi/\log Y\). Then

\[
 \boxed{\quad
 \sup_{|t|\le\epsilon/\log Y}
 |T_Y(\sigma+it)T_Y(\sigma+i(t+\delta_Y))|
 \ge\exp[-C\log Y\log\log Y].
 \quad}
 \tag{2.10}
\]

Its squared modulus has the same form of lower bound, after doubling
\(C\). This is the factor occurring on the paired four-frequency plane
\((t,t+\delta_Y,-t,-t-\delta_Y)\) for trivial source datum.

The result holds even if the chosen row grows with \(Y\). In particular,
one need not use the fixed row one or require that a spatial test be
positive at the origin. Selecting a sixth-power row in a fixed positive
radial annulus is compatible with this lemma. The source collision and
exterior-mask conditions for that selection still have to be checked.

## 3. The lower value occupies positive measure

This section is optional for a pointwise counterexample to CT1. It is
included to distinguish an isolated sample from a genuine frequency
neighborhood.

### Corollary 3.1. A lower integral over the central-frequency interval

For every fixed \(p>0\), after changing \(C\),

\[
 \boxed{\quad
 \int_{-\epsilon/\log Y}^{\epsilon/\log Y}
       |F_Y(\sigma+it)|^p\,dt
 \ge \exp[-C\log Y\log\log Y].
 \quad}
 \tag{3.1}
\]

**Proof.** The first derivative version of (2.4) gives

\[
 \left|\frac{d}{dt}F_Y(\sigma+it)\right|
 \le C_{K,\sigma}^mY^{m(1-\sigma)}m\log Y=:M_Y
 \tag{3.2}
\]

on the entire real axis. The successful point \(t_0\) in (2.5) belongs
to the middle half of the desired interval. Let
\(L_Y=\exp[-C_0\log Y\log\log Y]\) be the lower bound in (2.2), with
\(C_0\) fixed as proved there. For sufficiently large \(Y\),
\(r_Y=L_Y/(2M_Y)\le\epsilon/(2\log Y)\). On
\([t_0-r_Y,t_0+r_Y]\), the mean-value integral and (3.2) give
\(|F_Y(\sigma+it)|\ge L_Y/2\). Thus the integral is at least
\(2r_Y(L_Y/2)^p\). Its logarithm is bounded below by
\(-C\log Y\log\log Y\), since \(\log M_Y=O(\log Y)\). \(\square\)

This proves positive measure only on the one-dimensional paired central
frequency parameter. It is not a lower bound for an independently
integrated four-frequency signed trace. A codimension argument cannot
silently replace that missing step. CT1 as written is pointwise in every
independent frequency, so (2.10) is sufficient for its proposed audit.

## 4. Consequence conditional on the separate collision estimate

Suppose the actual selected row and allocation obey, on the full central
interval in (2.10),

\[
 Q_{\mathrm{coll}}(\sigma+it,\sigma+i(t+\delta_Y),
                  \sigma-it,\sigma-i(t+\delta_Y))
 \ge \exp[cY^\eta/\log Y],\quad c,\eta>0,
 \tag{4.1}
\]

and the full paired row trace is a sum of nonnegative terms which contains
this row with a weight bounded below by a positive constant. Then (2.10)
gives, at an allowed nearby frequency,

\[
 \text{paired row trace}
 \ge \exp\left[\frac{cY^\eta}{\log Y}
                       -C\log Y\log\log Y\right].
 \tag{4.2}
\]

For every fixed \(A>0\), (4.2) exceeds \(Y^A\) eventually. In particular,
it contradicts any CT1 bound \(CHD^{a+\epsilon}\prod_i(1+|t_i|)^B\)
with fixed \(a,B,C\), \(H=D^h\), and \(Y=bD\). The displayed frequencies
are \(O(1/\log Y)\), so their polynomial frequency weight is bounded.
One must also verify that the frequency tuple lies outside the specified
common conjugate tube. The separation \(\delta_Y\) is available for that
check, but the tube width must be read from its exact source.

The hypotheses (4.1), nonnegativity of every retained row, the positive
spatial weight, the permitted incidence allocation, and exclusion from
the tube are not proved by this analytic note. They are explicit
composition gates, not extra assumptions hidden inside Theorem 2.1.

## 5. Audit of earlier extraction ideas and actual work performed

The initial proposed direction was to replace full moments by a tail
count or by moments after discarding the largest \(o(H^{1/6})\) rows.
Source inspection found those results already in
`standalone/2026-10-10-sextic-moment-conductor-core/REPLICA_AVERAGES.md`:
Theorem 2.1 proves rough-base contraction, Theorem 3.1 positive-density
record replication, Corollary 3.2 the tail criterion, and Corollary 3.3
deletion-tolerant moment extraction. Its Section 4 already supplies an
exact-removal countermodel. None of these is claimed as new here.

The Gaussian and compact sampling papers likewise keep an unproved
arithmetic estimate at every sufficiently large scale. Merely reducing
the count of sampled scales does not yield a better moment exponent or
the required cofinal cancellation.

What was performed in this lane was source reading and the analytic
derivation in Sections 1–3. No numerical zeta-zero computation, actual
infinite moment computation, prime ideal asymptotic replay, proof-assistant
check, or external acceptance is claimed. The main proof is symbolic and
uniform, rather than an inference from a finite experiment.

**Smallest remaining local gap for the proposed CT1 refutation:** the root's
exact collision-growth and paired-trace positivity proof, composed with
(2.10) at the same row, fixed datum, permitted allocation, and frequency
tuple. The full norm-filtered identity SC4 is unaffected by a failure of a
pointwise estimate for its unfiltered integrand.
