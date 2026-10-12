# All residual scalar signs after any fixed real head still allow later off-real zeros

Status: complete proposed analytic extension of the frozen positive-Fourier
heat countermodel. No actual-Xi counterexample or native experiment.
Scope: for EVERY prescribed finite real-prefix length N and census height H0,
there EXISTS a qualitative strictly positive Fourier source with that Bessel
real head, later off-real zeros, and a complete residual heat trace positive
at every positive time after the first N real occurrences are removed.
Every scalar residual shifted moment is positive at every order and shift.
The source may depend on N; no one fixed source working for all removals is
asserted. No positive Fourier kernel is asserted for the residual quotient.
Exact dependencies: PF1–PF4 in
[HEAT_POSITIVE_FOURIER_COUNTERMODEL.md](HEAT_POSITIVE_FOURIER_COUNTERMODEL.md),
SHA256 `7ca1093e7b239f3908ae5a4332b4b3432e05c50e3169abaf33424548a1307d24`.
What was actually run: complete analytic derivation. No endpoint or moment run.
Smallest remaining gap for actual RH: a source-specific complete mixed sign
or uniform progress theorem; fixed-head scalar positivity cannot supply it.

## FR1. Choose the source after the prescribed finite removal

Use the Bessel source G_a and its complete simple real spectrum gamma_n from
PF1. Fix a>0, a finite ell>0, A>0, integer N>=0 and finite H0>=0. The full
variational bound remains `gamma_n^2<=B^2 n^2`, with
`B^2=(pi/ell)^2+a^2 exp(2ell)`. Choose X so large that

\[
             X>\max\{H_0,\gamma_N\},\qquad
             X^2>(N+2)^2B^2+A^2.
 \tag{FR1}
\]

For N=0 the gamma_N condition is omitted. Form precisely the normalized
source F_X in PF5. Its even strictly positive Fourier kernel, order at most
one, complete strip, absence of imaginary-axis roots and simple real roots
are unchanged from that proof. All added off-real roots have absolute real
coordinate at least X; the first N Bessel roots therefore form an actual
known real prefix before any added complex occurrence. The entire real
census below H0 is unchanged from G_a.

Remove one actual occurrence at each of `gamma_1,...,gamma_N`. Since these
roots are simple, the complete residual paired product is the even entire
quotient

\[
 h_N(z)=F_X(z)\left[\prod_{n=1}^N
                          (1-z^2/\gamma_n^2)\right]^{-1}.
 \tag{FR2}
\]

No Fourier positivity of this quotient is needed or claimed. The ORIGINAL
complete source retains its strictly positive Fourier kernel. The residual
has all remaining real roots and every off-real lattice occurrence with
its original multiplicity, and summability remains valid.

## FR2. The whole residual heat trace is positive for every time

For j>=0, the elementary index inequality is

\[
      N+2j+2\le(N+2)(2j+1).
 \tag{FR3}
\]

Combining FR1, FR3 and the complete variational bound gives

\[
 d_j=(2j+1)^2X^2-A^2
       >B^2(N+2j+2)^2
       \ge\gamma_{N+2j+2}^2
       \ge\gamma_{N+2j+1}^2.
 \tag{FR4}
\]

The real roots remaining after the removal can be partitioned into these
disjoint pairs. At every u>0 each pair of real heat terms is strictly
greater than `2 exp(-d_j u)`, while the absolute heat contribution of the
corresponding off-real pair is at most that value. Thus

\[
 K_{h_N}(u)=\sum_{n>N}e^{-\gamma_n^2u}
       +2\sum_{j\ge0}e^{-d_j u}\cos(2(2j+1)XA u)>0
                         \qquad(u>0).
 \tag{FR5}
\]

Both complete series converge absolutely and normally on positive-time
compact intervals by the same summability/Gaussian proof as PF3. Grouping
them does not omit a tail. The first group already gives strict positivity;
every subsequent group is strictly positive as well.

## FR3. Every complete residual scalar moment has a positive sign

Every remaining squared root has positive real part. For any integer k>=1
and any t>=0 the complete absolute Gamma/Fubini bound of PF12 survives
finite removal. Consequently

\[
 \sum_{\rho\ {m remaining}}m_\rho(\rho^2+t^2)^{-k}
       =\frac1{(k-1)!}\int_0^\infty
                 u^{k-1}e^{-t^2u}K_{h_N}(u)\,du>0.
 \tag{FR6}
\]

These are the exact logarithmic moments of the complete residual source,
not moments of only its real roots. Thus all residual scalar orders and
all nonnegative shifts have a strict positive sign, even though the source
still contains infinitely many off-real occurrences.

The same argument permits any fixed finite collection of removed Bessel
roots: take N at least their largest index, use the post-N pairs above, and
retain any unremoved earlier real roots as extra positive contributions.
If the intended removal is all real roots below a prescribed H0, choose N
to be that finite Bessel count before choosing X. The construction then
applies to an entire known finite simple census, not merely an arbitrary
real subset.

## FR4. Exact cofinal boundary

The quantified statement is `for every finite N, there exists X(N)` with
the residual signs FR5–FR6. It does not state that a single fixed X has
those signs after arbitrarily many real-root removals. The complete
Hausdorff or Hankel criterion must still fail for each constructed source,
because its off-real poles remain. A fixed finite census plus even the
ALL-order/ALL-shift residual scalar signs is therefore insufficient to
force real zero location or cofinal progress within these qualitative
source hypotheses. A sound exclusion guard additionally needs a strict
complete magnitude bound, not just positivity.

The literal actual theta arithmetic, Gamma/prime cancellation, complete
mixed moments or another stronger source condition may distinguish actual
Xi from this model. No assertion about their actual signs is made here.
