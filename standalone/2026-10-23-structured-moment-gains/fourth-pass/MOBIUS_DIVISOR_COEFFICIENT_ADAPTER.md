# Fixed divisor weights in the Möbius cubic Gauss moment

24 October 2026. Status: proposed source-dependent coefficient extension,
submitted for independent review. No numerical full-moment saving or new
zero-free boundary is asserted. This is separate from the frozen
`SIXTH_MOMENT_ROOT_NUMBER_REDUCTION.md`: at divisor order six it addresses
only that note's squarefree coefficient weight, not the entire signed
sextic frequency sum or its nonsquarefree sectors.

## 1. Inputs and statement

Use the Eisenstein ideal and zero-extension conventions of the frozen
third-pass packet at
`GettysburgResearch/riemann@f11e86684905c6417683a9f45ac75c223da6a162`.
The exact source argument is `openai/math` at
`1581d4cbdd69a0faf34b2089614fe2a814316a6a`, in
`preprints/An-unconditional-first-moment-for-cubic-Gauss-sums-September-25-2026/build/`:

* `sections/dual.tex`, especially the proof of `prop:dual` after its
  short convolution identity. Local SHA256
  `1209fd17cee79f4a21b71d66d3d8b60b210216fa783ec555959d2ebff2fba483`.
* `sections/background-type1.tex`, `lem:cubic-extensions` and its
  unrestricted-inner bound `eq:inner-extension`. Local SHA256
  `1c7be908c862dc440772964cfdd59e095e7b0f079cec11d99f5c7a9644198dd1`.
* The full dispersion assembly and angular extension, with the source
  bindings in the frozen packet's `SOURCES.json`.

The byte-exact local source copies for these two hashes are
`root_lane/pass3/cubic_first_moment_dual_EXACT.tex` and
`root_lane/pass3/cubic_first_moment_background-type1_EXACT.tex`.

The moving finite character below has the scope proved in the
companion `MOVING_SEXTIC_TWIST_EXTENSION.md`: its good primitive
conductor is a squarefree ideal \(t\), and its local sextic exponent
is odd at every good prime of \(t\). Its fixed-prime part is in a
fixed finite family. Thus a cubic twist cannot cancel its nontrivial
quadratic local component. Large additional redundant punctures are
not silently included in this statement. The special case \(t=1\)
is permitted.

Fix a positive integer \(K\), independently of the lengths. Put

\[
 a_K(n)=\mu(n)d_K(n)=\mu(n)K^{\omega(n)},
 \qquad \theta_t=\Theta_\ell\nu\xi_t.
\]

Here \(d_K\) is the \(K\)-fold ideal divisor function, so the first
equality holds on every ideal: both sides vanish off squarefree
support. The angular order \(\ell\) and ray character \(\nu\)
are fixed, and every character retains its zeros. Define

\[
 J_K(A,B;t)=\sum_a W(a/\sqrt A)
 \left|\sum_n\frac{a_K(n)\theta_t(n)G(n)}{\sqrt{Nn}}
       \overline{\chi_n(a)}V(Nn/B)\right|^2.             \tag{1}
\]

The character \(\chi\) is cubic and \(G\) is the normalized cubic
Gauss coefficient. The weights have the same fixed smooth class as the
frozen full moment. Under its all-finite-character hypothesis
\(\mathrm{ZF}_\beta\), the claimed implication is: for some
\(\eta_K>0\), uniform in the moving character,

\[
 \boxed{J_K(A,B;t)\ll(AB)^\epsilon
      \{A+(AB)^{2/3-\eta_K}\},\qquad
        A\ge B\ge2,\quad Nt\le B^{2/3}.}               \tag{2}
\]

Constants and \(\eta_K\) may depend on fixed \(K\). The saving
is existential; it is not the explicit saving from the three-factor
quantitative appendix. Only the indicated moving character family is
quantified.

## 2. An exact Euler-product decomposition

Let \(\mu^{*K}\) denote \(K\)-fold Dirichlet convolution. Define
the multiplicative function \(h_K\) by

\[
 \sum_{j\ge0}h_K(p^j)x^j=\frac{1-Kx}{(1-x)^K}.
\]

For \(K\ge2\) its local coefficients are

\[
 h_K(p^j)=(1-j)\binom{j+K-2}{K-2}\quad(j\ge0).       \tag{3}
\]

For \(K=1\), \(h_1\) is the convolution identity. In every case
\(h_K(p)=0\), so every nonunit in its support is powerful. Its
coefficients have a fixed divisor bound depending on \(K\), and

\[
 \sum_d\frac{|h_K(d)|}{(Nd)^\sigma}<\infty
 \quad\text{for every fixed }\sigma>1/2,
 \qquad
 \sum_{Nd\asymp D}|h_K(d)|\ll_{K,\epsilon}D^{1/2+\epsilon}.
                                                               \tag{4}
\]

Multiplying the local series proves the exact identity

\[
 \boxed{a_K=\mu^{*K}*h_K.}                            \tag{5}
\]

There is no squarefree projection left to insert on the right side:
(5) gives zero at every nonsquarefree ideal by cancellation. Every
complete multiplicative twist, including its zero extension,
distributes through (5).

## 3. Exceptional moments for a fixed convolution power of Möbius

First replace \(a_K\) by \(\mu^{*K}\) in an ordinary exceptional
character sum at length \(Y\). There are \(\delta_0,\eta_0>0\)
such that the source bound \(Y^{7/3-\eta_0}\) holds in its two
\(\delta_0\)-neighborhoods, with moving twist

\[
 Nt\le Y^{7/10},\qquad 1+|u|\le Y^{1/100}.            \tag{6}
\]

The neighborhoods concern the row length exponents
\((\log_Y P,\log_Y Q)=(1,0)\) or \((1/3,1/3)\). The extra
numerator and original puncture satisfy the source's sufficiently
small positive-power bounds.

To prove this within the structured coefficient class, choose \(Y_0\)
larger than the fixed upper support endpoint times \(Y\), and set
\(m=\mu\,1_{N\le\sqrt{Y_0}}\). The exact identity

\[
 \mu=2m-m*m*1\qquad(Nn\le Y_0)
\]

applies separately to all \(K\) factors of \(\mu^{*K}\). Its
expansion has at most \(2^K\) terms, each a product of at most
\(3K\) character polynomials after dyadic division and common Mellin
separation. Every truncated Möbius factor has length at most
\(Y^{1/2+o(1)}\). A factor of limiting full length must therefore
be a full smooth constant-one sum; all other factors then have
subpower trivial size.

These are precisely the structural facts used in the source proof
after its short convolution identity. Its remaining limiting argument
does not require three factors:

* If a factor has limiting exponent one, apply its full-sum functional
  equation. With (6), the moving conductor and total height have
  budget at most \(Y^{7/10+2/50}=Y^{.74}\), after truncating the
  common shifts as in the moving-twist companion. This is the same
  budget as the source's dominant-full-factor calculation. It gives
  exponents at most \(2.16\) at the first endpoint and
  \(2/3+2(1/3+.37)\) at the second, both below \(7/3\).
* Otherwise \(a_i\ge0\), \(\sum_i a_i=1\), and every
  \(a_i<1\). At the second endpoint the ordinary sieve applied
  to the square of the product forces total value exponent \(5/6\)
  on row exponent \(2/3\). Repeating a positive factor with
  value at least \(5a_i/6\) gives the source's strict contradiction.
* At the first endpoint, set \(d_i=v_i-5a_i/6\). The same
  multiplicity inequality, compared with the unsaved-moment lower
  bound, gives \(d_i\le0\) on adding any one factor. Hence the
  row exponent satisfies \(r\ge2/3\). A positive short factor
  exists with \(0<a_i\le1/2\), since no factor has exponent
  one. Omitting this particular factor keeps the total length in
  \([1/2,2]\) and gives \(d_i\ge0\), so its value is exactly
  \(5a_i/6\). A fixed number of its copies has total length
  strictly between \(4/3\) and 2. The source's off-diagonal
  Gram contradiction is valid for \(r\ge2/3\): a larger row
  exponent only decreases its diagonal and averaged off-diagonal
  upper exponents. No conclusion about the \(d_i\) of a possible
  factor longer than one half is needed.

All copies have fixed divisor bounds. The entire moving twist and its
zeros belong to the common coefficient vector in the unpunctured row
Gram Hilbert space, as in the moving-twist companion. The primitive
full factor is nonprincipal: the odd local component at \(t\) cannot
cancel with the cubic row, and remaining large cubic conductor outside
\(t\) is also primitive. Small deleted factors are handled before
reflection as in the source.

The source compactness argument now supplies uniform positive
\(\delta_0,\eta_0\). The factor count \(3K\) is fixed. Every
copied-factor multiplicity is chosen after passing to a limiting
subsequence and is fixed independently of \(Y\). This proves the
exceptional bound for \(\mu^{*K}\), without claiming numerical
margins.

## 4. Transfer the exceptional estimate through the powerful series

For \(a_K\), we claim

\[
 \sum_{p,q}\left|\sum_{(n,e)=1}a_K(n)\theta_t(n)
       (Nn)^{iu}W(Nn/Y)\chi_n(vpq^2)\right|^2
       \ll Y^{7/3-\eta_*}                               \tag{7}
\]

for some positive \(\delta,\eta_*\), in the two
\(\delta\)-neighborhoods, whenever

\[
 Nt\le Y^{17/25},\qquad 1+|u|\le Y^{1/200},
 \qquad Nv,Ne\le Y^\delta.                              \tag{8}
\]

Choose a fixed \(\rho>0\), sufficiently small relative to
\(\delta_0\), and split (5) into \(Nd\le Y^\rho\) and its
complement. For small \(d\), the residual column length is
\(Z=Y/Nd\). After decreasing \(\rho,\delta\), the original row
lengths are in the \(\delta_0\)-neighborhoods relative to \(Z\),
and

\[
 Y^{17/25}\le Z^{7/10},\qquad
 Y^{1/200}\le Z^{1/100}.
\]

The scalar depending on \(d\) retains its character and puncture
zeros and has modulus at most \(|h_K(d)|\). Minkowski and Section 3
bound the square-root moment of this part by

\[
 \sum_{Nd\le Y^\rho}|h_K(d)|
           (Y/Nd)^{7/6-\eta_0/2}
 \ll Y^{7/6-\eta_0/2}.                                  \tag{9}
\]

We may decrease \(\eta_0\) below \(1/10\) first, so the
coefficient mass converges by (4). No unweighted count of small
\(d\)'s is paid in (9).

### The large-divisor tail with the unrestricted-inner cubic sieve

Group \(Nd\asymp D\ge Y^\rho\), and put \(L=Y/D\). Freeze
\(d\) within each character mean. Its outer phase
\(\chi_d(vpq^2)\), including zeros, has modulus at most one. The
remaining polynomial has coefficients \(\mu^{*K}\) times the
common twist and mask, all divisor-bounded. Its profile is a dilation
by \(Nd/D\) in a fixed compact interval, so its smooth seminorms
are uniform.

The source's unrestricted-inner cubic sieve is exactly

\[
 \sum_{Np\asymp P}\mu^2(p)
       \left|\sum_{Nn\asymp L}b_n\chi_p(n)\right|^2
 \ll (PL)^\epsilon L\{P+L+(PL)^{2/3}\}                \tag{10}
\]

for divisor-bounded \(b_n\), with no squarefree requirement on
\(n\). All moving twists, exclusions, and a frozen \(q\) are
in \(b_n\). A fixed ray reciprocity partition and the sign of the
cubic character do not change the estimate.

At the first endpoint, fix \(q\), at cost \(Y^{O(\delta)}\),
and use \(P=Y^{1+O(\delta)}\). Minkowski in \(d\), followed by
\((\sum_{Nd\asymp D}|h_K(d)|)^2\ll D^{1+\epsilon}\), gives

\[
 \ll Y^{O(\delta)+\epsilon}
       \{Y^2+Y^2/D+Y^{7/3}D^{-2/3}\}.                  \tag{11}
\]

At the second endpoint, fix \(q\) and sum its
\(Q=Y^{1/3+O(\delta)}\) possibilities; use
\(P=Y^{1/3+O(\delta)}\) in (10). The identical Minkowski step
gives

\[
 \ll Y^{O(\delta)+\epsilon}
       \{Y^{5/3}+Y^{7/3}/D+Y^{20/9}D^{-2/3}\}.         \tag{12}
\]

For example, the last term in (12) is
\(D\,Q\,L(PL)^{2/3}\) at \(L=Y/D\).
Both (11) and (12) save a fixed power against \(Y^{7/3}\) when
\(D\ge Y^\rho\), after taking \(\delta\) and the internal
losses small compared with \(\rho\). Sum their logarithmically many
\(D\)-dyads. Nonempty bounded residual column scales are harmless;
the original support forces \(Nd\ll Y\). Equations (9)--(12)
prove (7) for some \(\eta_*>0\).

This tail proof uses neither squarefree support for
\(\mu^{*K}\) nor a fictitious equality between a powerful divisor
and the entire powerful part of its multiple. Masks stay in the
coefficient vector throughout (10).

## 5. Uniform cancellation, with punctures handled before bounding

For a finite twist \(\psi\) of the fixed angular type, (5) gives

\[
 \sum_n\frac{a_K(n)\psi(n)}{(Nn)^s}
 =L(s,\psi)^{-K}H_{K,\psi}(s),
 \qquad
 H_{K,\psi}(s)=\prod_p
       \frac{1-K\psi(p)(Np)^{-s}}
            {(1-\psi(p)(Np)^{-s})^K}.                  \tag{13}
\]

The product \(H\) is holomorphic and absolutely bounded on any
fixed closed half-plane \(\Re s\ge1/2+\epsilon\), uniformly
over the finite twist. Primes where \(\psi(p)=0\) contribute one.
It may have zeros; its nonvanishing is neither asserted nor needed.

For an additional puncture \(Q\), the safe exact presentation is

\[
 \boxed{\quad
 \sum_{(n,Q)=1}\frac{a_K(n)\psi(n)}{(Nn)^s}
 = L(s,\psi)^{-K}
   \prod_{p\mid Q}(1-\psi(p)(Np)^{-s})^{-K}
   H_{K,\psi}^{(Q)}(s),
 \quad}                                                     \tag{14}
\]

where \(H^{(Q)}\) omits the primes of \(Q\). Its bound is uniform
in \(Q\), since the absolute Euler product is convergent. The
displayed deleted **Hecke** factors have subpower mass on every fixed
positive half-plane. In contrast, bounding
\((1-K\psi(p)(Np)^{-s})^{-1}\) separately would introduce
artificial poles at small primes; their zeros have already canceled
in (14).

Under \(\mathrm{ZF}_\beta\), the frozen reciprocal-Hecke bound
and Mellin inversion applied to (14) give

\[
 \sum_{(n,Q)=1}a_K(n)\psi(n)(Nn)^{iu}W(Nn/Y)
 \ll [Y\,NQ\,q_\psi(2+|u|)]^\epsilon Y^\beta.        \tag{15}
\]

The possible principal pole creates a zero of \(L^{-K}\), not a
pole of (14). All small powers can be chosen after fixed \(K\).

## 6. Full-moment assembly

Follow the literal full-moment proof in the frozen packet. The
coefficient \(a_K\) is multiplicative on coprime ideals and vanishes
off squarefree support. Its exact \(f,m,l\) decomposition has column

\[
 a_K(fln)=a_K(fl)a_K(n)1_{(n,fl)=1}.                    \tag{16}
\]

The extra outer factor \(a_K(fl)\) is divisor-bounded. The same
large-common-divisor estimates and convergent factor sums therefore
apply with an arbitrarily small power loss. Short-frequency and cubic
principal-frequency estimates use (15). Generic large-conductor
estimates use the same fixed divisor bounds. The two exceptional
neighborhoods use (7).

Their surviving column length is \(Y=B/(FL)=B^{1-o(1)}\).
The strict gap \(2/3<17/25\) permits
\(Nt\le B^{2/3}\le Y^{17/25}\) after choosing the outer \(F,L\)
cutoffs sufficiently small. Common Mellin heights may be truncated at
\(Y^{1/200}\), since the fixed smooth kernels have arbitrary decay.
The remaining small-label budgets are chosen in the same order as in
the moving-twist companion. The source compactness argument supplies
a uniform positive full-moment saving \(\eta_K\), proving the
implication (2). The original pair diagonal remains the \(A\) term;
no natural zero or frequency is discarded.

## 7. Rectangular amplification and scope of the sixth-moment use

The exact cubic-power amplifier identity continues to hold with outer
coefficient \(a_K(d)\theta_t(d)G(d)/\sqrt{Nd}\). Its divisor
Cauchy step has only an additional fixed divisor power, absorbed in
\((AB)^\epsilon\). Thus, if \(A\le B\),
\(C\asymp(B/A)^{1/3}\), and
\(Nt\le(B/C)^{2/3}\), the rectangular companion's proof gives

\[
 J_K(A,B;t)\ll(AB)^\epsilon
   \{A^{1/3}B^{2/3}+A^{1/3}B^{1-2\eta_K}\}.           \tag{17}
\]

For \(K=6\), this fills the squarefree \(\mu d_6\) coefficient
requirement in the signed sixth-moment reduction, for the stated
Gauss/character orientation. The orientation is another actual
restriction in its application. That reduction contains
\(\overline{\gamma_2(n)}\,\overline{\chi_{6,n}(h)}\).
Writing \(h=t b^2\) leaves
\(\overline{\gamma_2(n)}\,\overline{\chi_{3,n}(b)}\),
apart from the moving twist. This is not the orientation of (1),
which has \(\gamma_2\overline{\chi_3}\), nor its whole
conjugate \(\overline{\gamma_2}\chi_3\). Writing a fourth
power \(h=t b^4\) matches the conjugate orientation but creates
a sparse parametrization and a larger residual core; it is not a
free replacement of an ordinary row average.

Thus the result does not convert the full sextic frequency into an
admissible cubic row, quantify \(\eta_6\), or estimate the remaining
nonsquarefree Gauss sectors, squarefree-row sieve tail, and coupled
signed first moment. Neither (2) nor (17) alone proves a sixth-moment
loss below \(0.18010287536465091825\).

## 8. Corollary for a complete natural presentation

The following corollary uses the separately reviewed
`NATURAL_PRESENTATION_TWIST_EXTENSION.md`, local source
`new_work_lane/pass4/NATURAL_PRESENTATION_TWIST_EXTENSION.md`, SHA256
`fda494d598fa01a5f6c652b9bf503bad2fc95f4fe1a3af7e594b41b43ce6775f`.
Its exact natural functional equation, including the fixed-angular
version, is an additional input to this corollary. It does not change
the narrower odd-local statement above.

Let \(R\) be squarefree and let \(\vartheta_R\) be a common
natural finite presentation: every good prime of \(R\) has a
sextic unit character of any exponent, including exponent zero, and
the presentation vanishes on its nonunits. Thus \(R\) includes
the entire good primitive conductor and every good redundant zero.
Its fixed-prime data belong to a fixed finite family. Put
\(\theta_R=\Theta_\ell\nu\vartheta_R\), with fixed
\(\ell,\nu\). The presentation is common to a row mean, not
chosen separately for each live row.

Under the same \(\mathrm{ZF}_\beta\) hypothesis, there is
\(\eta_{K,\mathrm{nat}}>0\), uniform over these presentations,
such that

\[
 \boxed{\quad
 J_{K,R}(A,B)\ll(AB)^\epsilon
       \{A+(AB)^{2/3-\eta_{K,\mathrm{nat}}}\},\qquad
 A\ge B\ge2,\quad NR\le B^{2/3}.
 \quad}                                                     \tag{18}
\]

Here \(J_{K,R}\) is (1) with \(\theta_t\) replaced by
\(\theta_R\). For \(A\le B\) and
\(C\asymp(B/A)^{1/3}\), the sufficient restriction
\(NR\le(B/C)^{2/3}\) also gives

\[
 J_{K,R}(A,B)\ll(AB)^\epsilon
   \{A^{1/3}B^{2/3}+A^{1/3}B^{1-2\eta_{K,\mathrm{nat}}}\}.
                                                               \tag{19}
\]

Here is the complete modification of the preceding proof.

First, in an exceptional row family, remove primitive-principal
inducing rows before any short convolution identity or full-factor
reflection. If the fixed angular type is nonzero there are none.
Otherwise every prime of the coprime squarefree product \(pq\)
must divide \(R\operatorname{rad}v\), outside the fixed omitted
set. Their number is at most
\(3^{\omega(R\operatorname{rad}v)}\ll Y^\epsilon\).
Both an original \(a_K\) polynomial and a
\(\mu^{*K}\) polynomial have absolute value
\(Y^{1+\epsilon}\), so these rows contribute at most
\(Y^{2+\epsilon}\). No principal polar term is omitted.

For every remaining dominant full factor, use the natural reflection
from the companion. If \(Q_\psi\) is its primitive conductor norm
and \(R_0\) its redundant radical, the budget is

\[
 Q_\psi\,NR_0\ll N(Rvpqe).
\]

The exact reflection keeps the common conjugate natural coefficient
\(\overline{\theta_R}\), including its zeros. The redundant Euler
quotient on the symmetry line has subpower norm, and the largest
dual length is bounded by the displayed conductor-radical product
times the height factor, divided by the original length. Therefore
\(NR\le Y^{7/10}\) and total height at most \(Y^{1/50}\)
give exactly the \(.74\) budget used in Section 3. The same
limiting argument with at most \(3K\) factors applies.

For the passage through \(h_K\), replace \(Nt\) in (8) by the
**whole** \(NR\). In addition to \(\rho\ll\delta_0\),
choose \(\rho<1/35\); then

\[
 NR\le Y^{17/25}\le(Y/Nd)^{7/10}
       \qquad(Nd\le Y^\rho).
\]

The principal inducing character in a residual convolution sum is
the same as in its original row: freezing \(d\) introduces only
the scalar \(\theta_R(d)\chi_d(vpq^2)\), and introduces no
additional \((n,d)=1\) restriction. Its principal rows have already
been removed. Thus (9) applies unchanged. The tail estimates
(10)--(12) keep all natural zeros in their coefficient vectors and
are uniform in \(R\).

For the reciprocal estimate, write the finite unit character in its
primitive presentation and combine the good redundant zeros of
\(R\) with the explicitly declared puncture. Apply the exact
co-deletion identity (14) to this combined puncture. Only the usual
deleted Hecke factors are inverted, so the same conductor and
radical small powers yield (15).

Finally the strict handoff \(2/3<17/25<7/10\) applies to
\(NR\) just as it applied to \(Nt\). The full \(f,m,l\)
assembly and the cubic-power amplifier commute with the complete
multiplicative presentation and its zeros, giving (18)--(19).
All other moving punctures must be charged to \(R\) or to the
explicit small-label budget. The corollary does not permit an
unrecorded mask or a different twist on each live row.
