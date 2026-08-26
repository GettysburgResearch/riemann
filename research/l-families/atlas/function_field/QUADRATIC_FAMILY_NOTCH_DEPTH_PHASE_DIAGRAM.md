# Odd-notch depth phase diagram

Status: **exact uniform counting theorem and exact exterior-channel
decomposition**.  No polynomial, curve, or zero enumeration is used.

These results count factor-degree layers of squarefree conductors and describe
their raw quadratic-family correlation sums.  They do not count zeros of an
individual `L`-function.

## Start here

Fix a prime power `q`, an integer `n>=2`, and put

\[
 M=2n-1,\qquad h=\left\lfloor {n\over2}\right\rfloor.
\]

For `1<=d<=h`, let `B_q(M,d)` be the number of monic squarefree degree-`M`
polynomials whose minimum irreducible-factor degree is exactly `d`.  Then

\[
 \boxed{B_q(M,d)\le {q^M\over d^2}.}
 \tag{0.1}
\]

The constant is one, the estimate is uniform in `q`, and odd characteristic
is not needed for this counting statement.  Consequently, for every set
`E` of admissible factor degrees,

\[
 \boxed{
 \sum_{d\in E}B_q(M,d)
 \le q^M\sum_{d\in E}{1\over d^2}.}
 \tag{0.2}
\]

In particular, if `d>=alpha*M` on `E` and `W=#E`, then

\[
 \sum_{d\in E}B_q(M,d)
 \le {W\over\alpha^2}{q^M\over M^2}.
 \tag{0.3}
\]

Thus one proportional-depth layer is `O_alpha(q^M/M^2)`, and any
`o(M)`-width collection of proportional-depth layers is `o(q^M/M)`.  An
additional leading `q^M/M` population cannot be supported on only `o(M)`
layers with `d` bounded below by a fixed positive multiple of `M`.  It must
instead use a macroscopic number of such layers, escape to `d=o(M)`, or use
both mechanisms.

There is a sharper scale-sensitive form.  A band of `W` layers with minimum
degree `d_0` contributes at most

\[
 {Wq^M\over d_0^2}.
 \tag{0.4}
\]

It is therefore negligible at the `q^M/M` scale whenever
`W=o(d_0^2/M)`.  In particular, even a single layer is negligible whenever
`d/sqrt(M) -> infinity`.  These are only counting firewalls: a layer allowed
by the bound need not contain any raw zeros.

## 1. The rough-polynomial lemma

Let `R_q(N,d)` count monic squarefree degree-`N` polynomials all of whose
irreducible factors have degree at least `d`.  Write `I_q(e)` for the number
of monic irreducibles of degree `e`.  Since

\[
 I_q(e)\le {q^e\over e},
\]

coefficientwise domination gives

\[
\begin{aligned}
 q^{-N}R_q(N,d)
 &= [u^N]\prod_{e\ge d}
       \left(1+q^{-e}u^e\right)^{I_q(e)}\\
 &\le [u^N]\exp\!\left(\sum_{e\ge d}{u^e\over e}\right)
 =:c_{N,d}.
\end{aligned}
\tag{1.1}
\]

Here `(1+x)^I <= exp(Ix)` is used coefficientwise, so no analytic choice of
`u` is involved.  If

\[
 A_d(u)=\exp\!\left(\sum_{e\ge d}{u^e\over e}\right)
       =\sum_{N\ge0}c_{N,d}u^N,
\]

logarithmic differentiation gives the exact recurrence

\[
 Nc_{N,d}=\sum_{e=d}^{N}c_{N-e,d}.
 \tag{1.2}
\]

Now `c_(0,d)=1` and `c_(N,d)=0` for `1<=N<d`.  Induction in (1.2) proves

\[
 \boxed{c_{N,d}\le {1\over d}\qquad(N\ge d).}
 \tag{1.3}
\]

Indeed, when `N<2d`, (1.2) gives `c_(N,d)=1/N<=1/d`.  When `N>=2d`, the
zero term contributes one and the remaining at most `N-2d+1` terms are at
most `1/d`, so

\[
 Nc_{N,d}
 \le 1+{N-2d+1\over d}
 ={N-d+1\over d}
 \le {N\over d}.
\]

Therefore

\[
 \boxed{R_q(N,d)\le {q^N\over d}\qquad(N\ge d).}
 \tag{1.4}
\]

To prove (0.1), mark one degree-`d` factor of a conductor in the exact
layer.  There are at most `I_q(d)<=q^d/d` choices, and the complementary
degree `M-d` polynomial is `d`-rough.  Since `d<=h` implies `M-d>=d`,

\[
 B_q(M,d)
 \le I_q(d)R_q(M-d,d)
 \le {q^d\over d}{q^{M-d}\over d}.
\]

Marking overcounts conductors with several degree-`d` factors and allowing
the marked factor to reappear in the complement only enlarges the upper
bound.  Hence squarefreeness creates no missing case.

## 2. Exact depth-to-exterior-channel dictionary

Now assume `q` is odd so that the frozen quadratic-family notch adapter
applies.  If the irreducible factor degrees of a squarefree conductor `Q`
have minimum `d` and `m_d` factors attain that minimum, then

\[
 \sum_{k\ge0}a_kx^k
 =\prod_{P\mid Q}(1-x^{\deg P})^{-1}
\]

has `a_k=0` for `1<=k<d` and `a_d=m_d`.  The exact odd-notch identity is

\[
 S_{n,Q}=\sum_{k=1}^{h}a_kD_{n-2k}.
 \tag{2.1}
\]

Write

\[
 n=2h+\varepsilon,\qquad
 \varepsilon\in\{0,1\},\qquad d=h-j.
\]

Then (2.1) becomes the exact depth decomposition

\[
 \boxed{
 S_{n,Q}
 =m_dD_{2j+\varepsilon}
  +\sum_{\ell=1}^{j}a_{d+\ell}
       D_{2(j-\ell)+\varepsilon}.}
 \tag{2.2}
\]

Thus depth `j` exposes the primitive exterior channel

\[
 \boxed{
 D_{2j+\varepsilon}
 =(-1)^nq^{(2j+\varepsilon)/2}
   \chi_{\omega_{2j+\varepsilon}}}
 \tag{2.3}
\]

with positive integer coefficient `m_d`; every other term has exterior
index lower by an even integer.  This is a formal top-weight statement.  At
a particular Frobenius class, the numerical value of the top channel can
vanish or cancel against lower channels.

The first-boundary theorem is the case `j=0`.  The fixed-depth estimate from
that packet follows immediately from (0.1), since `d=h-j` is asymptotic to
`M/4` for fixed `j`.  This independently confirms its earlier factor-profile
proof and removes its harmless "sufficiently large `n`" bookkeeping.

## 3. What the phase diagram says

For a set `J` of depths, put `d_j=h-j`.  Even if every conductor on those
layers were a raw zero, (0.2) gives

\[
 {1\over q^M}\#\{Q:\min\deg P\in\{d_j:j\in J\}\}
 \le \sum_{j\in J}{1\over(h-j)^2}.
 \tag{3.1}
\]

Hence the natural counting coordinate is not depth alone but the
**harmonic-square budget**

\[
 \mathcal H_2(J)=\sum_{j\in J}(h-j)^{-2}.
\]

A leading extra density of order `1/M` requires
`M*mathcal H_2(J)` not to tend to zero.  In the proportional regime this
forces `#J` to be of order `M`.  Near smaller factor degrees the same budget
permits thinner bands; the present theorem deliberately does not claim that
such layers actually have trace zero.

The channel dictionary (2.2) changes at the same time: fixed `j` exposes a
fixed-rank exterior character, while `j` proportional to `M` exposes rank
proportional to `M`.  Any leading-density mechanism built from proportional
depths must therefore confront a growing-rank family of exterior channels,
not a finite list such as `(D_1,D_3)`.

## 4. Audit and claim boundary

The fixed-depth proof in
`QUADRATIC_FAMILY_FIRST_BOUNDARY_TRACE_ZERO_DENSITY.md` is sound.  For fixed
`j`, its complementary degree is `3d+4j-1` when `n` is even and
`3d+4j+1` when `n` is odd.  Once `d>4j+1`, the complement has at most three
irreducible factors; the one- and two-factor estimates are
`O_j(q^(M-d)/M)`, and only `O_j(1)` three-factor degree profiles remain.
After marking a degree-`d` factor this is `O_j(q^M/M^2)`.  The rough lemma
above proves the same result uniformly without separating factor counts.

Proved here:

- the uniform rough-polynomial bound (1.4);
- the exact-layer bound (0.1) and arbitrary-layer-set bound (0.2);
- the proportional-regime and harmonic-square phase criteria;
- the exact residual exterior-channel decomposition (2.2).

Not proved here:

- that any deeper layer contains a raw correlation zero;
- the density or distribution of cancellations among the `D_s`;
- a monodromy or equidistribution theorem in growing exterior rank;
- a zero theorem for an individual `L`-function, RH, or GRH;
- external novelty or priority.

The rough-polynomial majorant is an elementary analogue of the standard
cycle-index bound and should be treated as known or folklore unless a
specialist literature review establishes otherwise.  The contribution of
this packet is the exact uniform layer packaging and its alignment with the
odd-notch exterior-channel depth scan.
