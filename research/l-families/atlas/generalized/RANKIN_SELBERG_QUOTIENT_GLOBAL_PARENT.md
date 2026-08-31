# Rankin--Selberg quotient global parent

Status: PROPOSED NATIVE QUOTIENT THEOREM WITH CLASSICAL ANALYTIC INPUTS.
Independent frozen-SHA proof/code review is required before import.

Scope: a canonical one-dimensional quotient of the full weight-24
Rankin--Selberg period matrix; inherited meromorphy and reflection,
real-half-line positivity, genuine fixed-basis coupling, and an exact
noninteger-frequency obstruction. No new automorphic representation,
ordinary Euler product, generalized-prime exclusion, RH/GRH or novelty claim.

Exact sources: primary references below; the manifest binds the published
programme checkpoint at 246434f343029cc821aa236081c4d12080f571f2 as context,
not as a proof of the analytic imports. Remote bytes are not machine
authenticated. Classical modularity and Eisenstein continuation are imported.

What was run: bounded integer q-products, an independent logarithmic-derivative
recurrence, Hecke coefficient identities, rational-frequency convolutions,
finite weighted-Gram/flag controls, and strict source/fixture tests.
No numerical period, gamma/zeta value, zero or infinite-tail sampling.

Smallest remaining gap: the completed quotient can acquire poles at zeros
of its denominator period. Their cancellation/distribution is not controlled.
This construction belongs to the rational closure of classical period entries;
it does not establish a new automorphic L-function or unexplored priority.

## 1. The independent source and its canonical flag

Let Gamma=SL(2,Z), q=exp(2*pi*i*z), and use the classical forms
\[
 E_4=1+240\sum_{n\ge1}\sigma_3(n)q^n,\qquad
 \Delta=q\prod_{m\ge1}(1-q^m)^{24},
 \quad f_0=\Delta E_4^3,\quad f_1=\Delta^2.                 \tag{RQ1}
\]
The imported modular-form facts are: E4 has weight four; Delta is a weight
twelve cusp form, has no zeros in the upper half-plane, and has a simple
zero at infinity; dim M12=2. Consequently multiplication by Delta identifies
M12 with S24: division by Delta is holomorphic both in the half-plane and at
the cusp. E4^3 and Delta are independent by their constant terms, so f0,f1
form a basis of V=S24. This proves dim V=2 without inferring dimension from
a finite coefficient sample.

Write a_n=[q^n]f0 and b_n=[q^n]f1. Then a1=1, b1=0, b2=1.
The normalized cusp and q-coordinate determine the functional ell(f)=[q]f
and its intrinsic line W=ker ell=span(f1). The affine quotient ell(f)=1,
not an arbitrary basis vector, is the intended scalar source.

The exact calibration is
\[
\begin{array}{c|rrrrr}
n&1&2&3&4&6\\ \hline
a_n&1&696&162252&12831808&-882400608\\
b_n&0&1&-48&1080&143820 .
\end{array}                                                    \tag{RQ2}
\]
For f_t=f0+t f1 the coprime multiplicativity defect is
\[
 [q^6]f_t-[q^2]f_t[q^3]f_t
 =48(t^2+312t-20736000).                                    \tag{RQ3}
\]
In this basis the standard Hecke operator is
\[
 T_2=\begin{pmatrix}696&1\\20736000&384\end{pmatrix}.
\]
Its coefficient formula is [q^n]T2f=[q^(2n)]f+2^23[q^(n/2)]f,
with the second term zero for odd n. The first two coefficients determine
the matrix because f0,f1 are a basis. Its normalized eigenvectors f_t have
t=-156 +/- 12 sqrt(144169). The classical commuting Hecke algebra preserves
these distinct one-dimensional eigenspaces. Thus these are precisely the
normalized simultaneous eigenforms in V; outside this two-point locus RQ3
already prevents the usual multiplicative-coefficient Euler product.
This is classical weight-24 calibration, not the new quotient's novelty.

## 2. Global period matrix and the completion that is actually inherited

Use dmu=dx dy/y^2 and the completed Eisenstein series
\[
 E^*(z,s)=\pi^{-s}\Gamma(s)\zeta(2s)
       \sum_{\gamma\in\Gamma_\infty\backslash\Gamma}
            \operatorname{Im}(\gamma z)^s.                    \tag{RQ4}
\]
The quotient identifies the signs +/-I. Its classical continuation has
simple poles at BOTH s=0 and s=1, residues -1/2 and +1/2,
and E*(z,s)=E*(z,1-s). It is positive for real s>1.

Define the sesquilinear period, conjugate-linear in the first input,
\[
 {\cal I}_{ij}(s)=\int_{\Gamma\backslash{\mathbb H}}
       y^{24}\overline{f_i(z)}f_j(z)E^*(z,s)\,d\mu(z).
\]
Cusp decay dominates the Eisenstein family's locally uniform polynomial
growth at the cusp, so integration gives a meromorphic matrix with no
poles away from 0,1. The residue matrix is +/-G/2, where
G_ij is the Petersson Gram of f0,f1. G is positive definite.

Unfolding and Fourier orthogonality give, for Re(s)>1,
\[
 {\cal I}(s)=A(s)R(s),\quad R(s)=\zeta(2s)D(s),\quad
 D_{ij}(s)=\sum_{n\ge1}\overline{a_i(n)}a_j(n)n^{-s-23},
\]
\[
 A(s)=\pi^{-s}\Gamma(s)(4\pi)^{-s-23}\Gamma(s+23)
     =2^{-23}(2\pi)^{-23-2s}\Gamma(s)\Gamma(s+23).             \tag{RQ5}
\]
Here a0(n)=a_n and a1(n)=b_n; the subscript 0 is a basis index, not a constant
Fourier coefficient. Absolute convergence of the diagonal series follows
from the finite positive unfolded integral by Tonelli; the cross series is
absolutely convergent by Cauchy--Schwarz. In particular this assertion does
not require a coefficient Ramanujan bound. Polarization gives the full
sesquilinear identity. The real coefficient basis makes I01=I10, but complex
changes of basis must use Hermitian congruence, not a transpose.

The common archimedean multiplier and Eisenstein equation give
I(s)=I(1-s). They do NOT give D(s)=D(1-s).

## 3. Canonical Schur quotient and its exact poles

Set
\[
 {\cal Q}(s)=\frac{\det{\cal I}(s)}{{\cal I}_{11}(s)},\qquad
 F(s)=D_{00}(s)-\frac{D_{01}(s)D_{10}(s)}{D_{11}(s)},\qquad
 L_Q(s)=\zeta(2s)F(s).
\]
Then, initially on a sufficiently right half-plane and subsequently
meromorphically,
\[
 \boxed{{\cal Q}(s)=A(s)L_Q(s)=A(s)\zeta(2s)F(s),\qquad
        {\cal Q}(s)={\cal Q}(1-s).}                           \tag{RQ6}
\]
D11 and I11 are not identically zero, since they are positive for real s>1.
The scalar meromorphic quotient is therefore well defined, including by
removable continuation where numerator and denominator vanish.

For real sigma>1 the period is a strictly positive Hermitian form: a nonzero
cusp form cannot vanish almost everywhere, and E*(z,sigma)>0. Completion of
squares gives
\[
 {\cal Q}(\sigma)
 =\min_{\ell(f)=1}{\cal I}_\sigma(f,f)>0.                     \tag{RQ7}
\]
The minimum is attained at f0-(I10/I11)f1. The formula is a quotient
metric, not a pointwise minimum definition at nonreal s.

Replace the lifts by f0+t f1 and c f1, with t in C and c nonzero.
The change-of-basis matrix has first row (1,0), and determinant c.
Its Hermitian congruence multiplies det I and I11 by the same |c|^2.
Therefore Q is invariant. It is canonical relative to the specified
modular source, cusp coordinate, and normalized functional ell; no
basis-free canonicity without that data is claimed.

Put q_G=G00-|G01|^2/G11=det G/G11>0. The pole limits are
\[
 \lim_{s\to1}(s-1){\cal Q}(s)=q_G/2,\qquad
 \lim_{s\to0}s{\cal Q}(s)=-q_G/2.                            \tag{RQ8}
\]
Indeed det I has a second-order pole with nonzero leading determinant,
whereas I11 has a first-order pole. Thus neither endpoint pole disappears.
Away from 0,1, Q can have poles only at zeros of I11. In the real basis, if
I11 has zero order m and I01 has zero order r at such a point, the pole
order of Q is max(m-2r,0); take r=infinity if the cross entry vanishes
identically. This is a local divisor statement, not a proof that additional
poles exist or cancel. Reflection and Schwarz conjugation preserve the divisor.

Because 1/A is entire, L_Q has no additional poles from removing A; F=L_Q/
zeta(2s) can also have poles at zeros of zeta(2s), subject to cancellation.
Do not claim that F alone has only the completed quotient's pole set.
No complex-half-plane zero-free theorem, critical-line zero theorem, or
RH consequence follows from the real positivity in RQ7.

## 4. Coupling is not removed by one constant change of basis

A precise sense of genuine coupling can be proved. There is NO fixed
invertible complex change of cusp-form basis that diagonalizes the entire
period family I(s) by congruence.

Suppose a basis h,k made its cross entry identically zero. By RQ5 and
uniqueness of absolutely convergent ordinary Dirichlet series,
overline([q^n]h)[q^n]k=0 for every n. Equivalently the two independent
linear functionals determined by h,k must, between their two kernels,
annihilate every coefficient direction (a_n,b_n).

But the first three directions
\[
 (1,0),\quad(696,1),\quad(162252,-48)
\]
are pairwise nonproportional; the last pair has determinant -195660.
Two lines in C^2 cannot contain all three directions. This is a contradiction.

An s-dependent diagonalization still exists at individual positive real
parameters. The theorem does not prohibit it, nor does it say the entries
are unknown L-functions: in a Hecke eigenbasis they are classical
Rankin--Selberg pairings, and Q is a rational expression in these entries.
The result excludes a fixed direct-sum relabeling of this Gram family,
not every conceivable representation of the scalar quotient.
Section 6 also excludes expressing Q as a constant linear combination of
the period entries: division by their common A(s)*zeta(2s) would express
F as an ordinary Dirichlet series, contrary to its fractional frequency.

## 5. Absolute generalized-Dirichlet expansion, including the missing a1

Let w=s+23, and shear canonically to
\[
 g=f0-696f1,\qquad c_n=[q^n]g.
\]
Then c1=1, c2=0, c3=195660 and c4=12080128. Write
\[
 U(w)=\sum_{n\ge3}b_n^2(n/2)^{-w},\quad
 C(w)=\sum_{n\ge3}c_nb_n n^{-w},\quad
 B(w)=\sum_{n\ge1}c_n^2 n^{-w}.
\]
The exact quotient is
\[
 D_{11}=2^{-w}(1+U(w)),\qquad
 F(s)=B(w)-2^w C(w)^2\sum_{k\ge0}(-U(w))^k.                \tag{RQ9}
\]
The factor 2^w is essential: b1=0, and D11 does not start with one.

Here is the analytic justification, not merely a formal division. The cusp
bound |f(z)|y^12=O(1) on H follows from modularity and cusp decay. Integrating
one horizontal Fourier coefficient at y=1/n gives a_n,b_n,c_n=O(n^12).
Thus every series above converges absolutely sufficiently far right. Fix
a right real w0 with absolute convergence. Dominated convergence gives
sum_{n>=3}b_n^2(n/2)^(-w) ->0 as real w->infinity, since n/2>1.
Choose W0 with this sum below one. For Re(w)>=W0 the geometric series
converges normally and absolutely, uniformly on smaller closed right
half-planes. Cauchy products and regrouping are legitimate there.
This argument proves existence of a right half-plane, not a numerical W0.

Every correction frequency has the form
\[
 \rho=\frac{nm}{2}\prod_{j=1}^k\frac{\ell_j}{2},
 \quad n,m,\ell_j\ge3.                                    \tag{RQ10}
\]
In particular rho>=9/2*(3/2)^k. Below any fixed cutoff this bounds k, and
then bounds each integer n,m,ell_j. The support is locally finite, including
after equal rational frequencies are grouped. Together with absolute
convergence this is an honest generalized Dirichlet series, not a formal
product with unproved convergence.

For frequencies below 9/2, only B contributes: coefficients at 1,2,3,4 are
1,0,195660^2,12080128^2. At frequency 9/2 the only correction word is
k=0,n=m=3. Its coefficient is
\[
 \boxed{[ (9/2)^{-w}]F=-(-48\cdot195660)^2
       =-88203653222400\ne0.}                              \tag{RQ11}
\]
This is the first noninteger frequency. Equivalently,
\[
 F(s)=1+38282835600\,3^{-w}
       +145929492496384\,4^{-w}
       -88203653222400\,(9/2)^{-w}+o((9/2)^{-\operatorname{Re}w})
\]
along the real right-hand limit. The remainder assertion follows from
absolute convergence at W0 and local finiteness, after removing this finite
prefix.

The zeta multiplier is
\[
 \zeta(2s)=\sum_{d\ge1}d^{46}(d^2)^{-w}.
\]
It creates an extra integer-frequency term 2^46 at frequency four, but
cannot cancel the coefficient at 9/2: for d>=2, the required F frequency
would be (9/2)/d^2<=9/8, where only frequency one exists, and d^2 is never
9/2. Thus L_Q has the same first noninteger coefficient in w coordinates.

## 6. The Euler-product obstruction and its precise boundary

An absolutely convergent generalized Dirichlet series with locally finite
positive frequencies has unique coefficients. For completeness: if the
difference of two such series vanishes, choose its least nonzero frequency
rho0, multiply by rho0^w, and let real w tend to infinity. The remaining
terms tend to zero by domination from any fixed absolute-convergence
abscissa, leaving the nonzero coefficient, a contradiction. The union with
the ordinary integer frequencies is still locally finite.

Consequently neither F nor L_Q admits an absolutely convergent ordinary
Dirichlet expansion sum d_n n^(-s) on any right half-plane: rewriting in w
only rescales its coefficients by n^23 and cannot generate frequency 9/2.
By the same reasoning neither has a standard ordinary-prime Euler product
whose local factors are normalized power series in p^(-s) and whose
expansion is absolutely convergent on a right half-plane. Such a product
expands over integer prime-power products, contradicting RQ11.

This excludes neither generalized prime/norm systems nor merely formal,
conditionally convergent, or specially engineered products. It is not a
classification of all possible Euler analogues. The functional equation
belongs to Q=A*zeta(2s)*F; multiplying or dividing by arbitrary factors
changes the object and is not covered by the exclusion.

## 7. Classical boundary and sources

- Miller--Schmid, *The Rankin--Selberg method for automorphic distributions*,
  introduction (1.7)--(1.14): the coefficient pairing, completed Eisenstein
  period, unfolding and common gamma factor:
  https://arxiv.org/pdf/math/0605783 .
  Its introductory wording "only ... s=1" for the COMPLETED E_s and I(s)
  must not be imported literally: reflection retains the pole at zero.
- Zagier, *Eisenstein series and the Riemann zeta-function*, section 1(a)--(c),
  equations (3)--(17), supplies the explicit completed poles 0,1, reflection,
  growth and period contract:
  https://people.mpim-bonn.mpg.de/zagier/files/scanned/EisensteinRiemannZeta/eisenstein-zeta-978-3-662-00734-1_10.pdf .
- Zagier, *Elliptic Modular Forms and Their Applications*, sections 2.1,
  2.2, 2.4 and 4.1, in *The 1-2-3 of Modular Forms*: modularity, the ring
  and dimension facts, product/Fourier definitions, and Hecke algebra:
  https://people.mpim-bonn.mpg.de/zagier/files-restricted/doi/10.1007/978-3-540-74119-0/fulltext.pdf .
- Schur elimination and positive quotient/shorted forms are classical;
  Anderson, *Shorted Operators*, SIAM J. Appl. Math. 20 (1971), 520--525,
  https://doi.org/10.1137/0120053 ; Anderson--Trapp, *Shorted Operators II*,
  28 (1975), 60--71, https://doi.org/10.1137/0128007 .
  RQ7 and flag invariance are proved directly above, not attributed as a
  new matrix inequality.

The new programme object is this source-specified canonical quotient and
its exact loss of integer frequencies, not the discovery of periods,
Schur complements, modular forms, or their scalar linear combinations.
No external priority search is claimed exhaustive.

## 8. Bounded replay contract

The standard-library producer constructs q-coefficients through 24 from
RQ1 and separately reconstructs Delta by its logarithmic-derivative
recurrence. It checks all T2 coefficients accessible through 12, the
calibration polynomial, and complete rational-frequency words below
cutoffs 9/2, 6, 10 and 12. Geometric depth is bounded before expansion
using (9/2)(3/2)^k; q-tail coverage is justified by the same lower bounds.

Finite positive coefficient-weight Grams check real rational shear,
quotient and residue algebra. They are not numerical Eisenstein-period
evaluations and do not verify complex positivity. The complex flag theorem
has the direct Hermitian-congruence proof above.

Public caps: q order<=24, frequency cutoff<=12, polynomial/list size<=25,
and series support<=256. Primitive cutoff, weight, shear and scale components
have 32-bit caps; polynomial/frequency containers are explicitly checked
internal integer/rational representations with 4096-bit caps. There are
<=200000 accounted work units per report: q-product pairs, recurrence
summands, Hecke comparisons, frequency-product pairs, and three Gram sums
per retained weight. This is a deterministic bounded-loop accounting, not
a count of every interpreter operation. Type/count/cutoff guards precede expansion;
booleans, floats, nonfinite JSON, duplicate keys and incompatible schemas
are rejected. Fixed report acceptance is complete typed canonical-JSON
equality to a source-authenticated rebuild. The fixture binds this note,
producer, tests and manifest by LF-normalized hashes.

These computations prove only their exact finite algebra. The global
continuation, geometric-series convergence, uniqueness theorem and Euler
obstruction use the written/imported analysis, not finite extrapolation.

    python -B research/l-families/atlas/generalized/rankin_selberg_quotient_global_parent.py --check
    python -B -O research/l-families/atlas/generalized/rankin_selberg_quotient_global_parent.py --check
    python -B -m unittest discover -s tests -p test_rankin_selberg_quotient_global_parent.py
    python -B -O -m unittest discover -s tests -p test_rankin_selberg_quotient_global_parent.py

Author replay: 30 tests and both producer checks pass normally and under
Python -O; Ruff lint/format and whitespace checks pass. These are author
replays, not the independent exact-SHA review, which remains required.
RH and GRH remain unsolved.
