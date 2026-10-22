# Low-conductor removal for the long inverse moment

22 October 2026. **Status: complete conditional analytic deduction from a
common finite-order Hecke zero-free half-plane; the remaining high-conductor
moment is unproved. No new zero-free boundary is established.**

This note strengthens the observation that principal sixth-power rows can
already be controlled using the inherited zero-free theorem. It removes a
whole growing conductor range, with all sixth-power overlaps and natural
zeros retained. The removed range is stable under the actual sixth-power
amplifier. Consequently a specified high-conductor raw estimate would
suffice for a full improved inverse moment; one need not prove that raw
estimate again for the removed rows.

The elementary counting and the amplification reduction below are native
arguments. The analytic input is a conductor-uniform reciprocal estimate
deduced from the stated common zero-free half-plane. No novelty claim is
made for the classical reciprocal consequence itself.

## 1. Arithmetic setting and the exact reciprocal input

Work over the Eisenstein field E=Q(sqrt(-3)), with good primary ideal
representatives outside a fixed set S containing the primes above 6 and
the conductor of a fixed finite-order ray character nu. A finite set of
unit/reciprocity sectors is permitted. Let q_a=N(a). All residue symbols
are zero-extended, including their sixth powers. Write

\[
 M_u(D;Q,W)=\sum_{(n,Q)=1}
    \frac{\mu_E(n)\nu(n)\overline{\chi_n(u)}}{\sqrt{q_n}}
                      W(q_n/D),\qquad D\ge2.                 \tag{1.1}
\]

Here W is smooth with support in a fixed compact subinterval of (0,infinity),
Q is a puncture ideal, and u is a nonzero element row, with the original
finite unit multiplicity. The sum is over good ideals. Constants may
depend on S, nu, the support, and finitely many normalized seminorms of W.

Assume that, for a common beta in (1/2,1), every finite-order Hecke
L-function needed after reciprocity and primitive induction is zero-free
on Re(s)>beta, allowing the simple principal pole. A sufficient premise
is the common finite-order Hecke theorem for E. The only quantitative
consequence used here is

\[
 |L_E(\sigma+it,\psi)^{-1}|
 \ll_{\delta,\epsilon}
       \{N\mathfrak f_\psi(3+|t|)^2\}^{\epsilon},
       \qquad \sigma\ge\beta+\delta,                       \tag{1.2}
\]

uniformly over the primitive characters psi, for every fixed positive
delta and epsilon. At a principal pole, the reciprocal is its continued
holomorphic value. The same estimate after deleting Euler factors has
the additional factor (NQ')^epsilon, where Q' is the radical of the extra
deleted primes.

An explicit proof of (1.2), from common zero-freeness and the classical
Hecke functional equation, is resident at frozen repository head
`64cb43c038d1828a478cb97cbc32e435e111d2d2`, in
`standalone/2026-10-20-boundary-iteration/uniform/UNIFORM_INVERSE_AND_STRIPPING.md`,
Proposition 1. Its finite-order predecessor is
`standalone/2026-10-20-liu-all-field-artin-and-barrier/uniform_mobius_consequence.md`.
Their mechanism is a zero-free logarithm, Borel--Caratheodory,
three-circles, and then Mellin or Perron inversion. Uniform constants in
the proof of the zero-free theorem are not an additional premise.

Liu, [arXiv:2610.26835v1](https://arxiv.org/abs/2610.26835v1), Theorem 17.1,
supplies beta=B_flat as an imported preprint input, with the analytic
dependencies stated in that paper. The weaker beta=7/8 also suffices for
the rational example below. The unreviewed unitary-family extensions in
the repository are not needed: all characters here are finite order,
and any Mellin norm twist is a vertical translate.

Put

\[
 \kappa=2\beta-1,\qquad
 \rho_\beta=1-\frac{6\kappa}{5}
                   =\frac{11-12\beta}{5}.                   \tag{1.3}
\]

The useful case rho_beta>0 is beta<11/12.

### Pointwise smooth inverse bound, including every deleted factor

For every epsilon>0,

\[
 |M_u(D;Q,W)|
 \ll_\epsilon \mathcal S(W)
                (Dq_uq_Q)^\epsilon D^{\beta-1/2}.           \tag{1.4}
\]

Here mathcal S is one fixed finite smooth seminorm, whose order can be
chosen before u,D,Q. This is also uniform for a row-dependent family
W_u with bounded mathcal S(W_u), and for row-dependent punctures with
a common upper bound q_Q<=Q_0. That last assertion is pointwise
uniformity; it is not an extension of a different averaged theorem to
adaptive coefficients.

**Proof.** Reciprocity, after the fixed ray partition, presents the
coefficient as mu_E(n) psi_u(n) with a primitive Hecke character psi_u
and the full original zero mask. Its conductor divides a fixed
S-supported factor times rad(u), and every lost natural zero is retained
by deleting the corresponding Euler factor. Thus for Re(s)>1 its
Dirichlet series is

\[
 L_E(s,\psi_u)^{-1}
 \prod_{\mathfrak p\mid Q'_u}
       (1-\psi_u(\mathfrak p)q_{\mathfrak p}^{-s})^{-1},    \tag{1.5}
\]

where Q'_u has radical dividing a fixed factor times uQ. At primes of
the primitive conductor the displayed correction equals one. If a
local exponent becomes a multiple of six, its unit indicator is still
in Q'_u; it is not replaced by an everywhere-one character.

Mellin inversion writes (1.1) as the integral of (1.5) at s=1/2+z,
times D^z and W_hat(z). Shift from Re(z)>1/2 to
Re(z)=beta-1/2+epsilon_0. The reciprocal is holomorphic throughout
this strip, including its zero at a principal pole. The finite
corrections have no poles on Re(s)>0 and cost a subpower of q_uq_Q
on each fixed narrower half-plane. Equation (1.2) and rapid Mellin
decay, with a fixed sufficiently large derivative order, bound the
new integral by

\[
 \mathcal S(W)(q_uq_Q)^\epsilon
                          D^{\beta-1/2+\epsilon_0}.
\]

Choose epsilon_0 and all preliminary conductor losses smaller than the
prescribed final epsilon. This proves (1.4). The same estimates are
uniform over a family with bounded seminorm. No positivity or averaging
is used in this step. QED.

## 2. Counting rows by the radical of their sixth-power-free part

Write each nonzero row uniquely as

\[
                  u=v a^6,                               \tag{2.1}
\]

where v is sixth-power-free, including the retained unit sector.
There is **no** condition (v,a)=1. Define

\[
                   R(u)=N\operatorname{rad}(v).           \tag{2.2}
\]

The primes in a whose total valuation is divisible by six remain
natural zeros of the row character, even when absent from rad(v).

**Lemma 2.1.** For H,C>=1,

\[
 \#\{0<q_u\le H:R(u)\le C\}
              \ll_\epsilon H^{1/6}C^{5/6+\epsilon}.        \tag{2.3}
\]

The same upper bound holds for any further subset of these rows.

**Proof.** The number of Eisenstein ideals with norm at most X is O(X).
For a fixed v with q_v<=H, the number of a in (2.1) is therefore
O((H/q_v)^(1/6)). Sum first over its squarefree radical r. Exactly,

\[
 \sum_{\operatorname{rad}(v)=r}q_v^{-1/6}
 =\prod_{\mathfrak p\mid r}
       \left(\sum_{j=1}^{5}q_{\mathfrak p}^{-j/6}\right)
 \le 5^{\omega(r)}q_r^{-1/6}.                            \tag{2.4}
\]

Dropping the condition q_v<=H only increases this positive sum.
The standard divisor bound 5^omega(r)<<_epsilon q_r^epsilon and
ideal counting/partial summation give

\[
 \sum_{q_r\le C}^{\rm sf}5^{\omega(r)}q_r^{-1/6}
                        \ll_\epsilon C^{5/6+\epsilon}.
\]

The finitely many unit sectors only change the constant. This proves
(2.3), including C=1 and overlaps between v and a. QED.

### What “conductor” means here

Outside S, a good prime of v has exponent j in {1,...,5}; its local
sextic residue character is therefore nonprincipal and tamely primitive
at that prime. Thus the primitive conductor of the row twist outside
S is exactly rad(v). Since nu has conductor supported on S, multiplying
by nu cannot cancel one of these exterior local characters. Fixed
unit and reciprocity sectors only affect S. In this setting R(u) is
the exterior primitive-conductor norm, up to the fixed supported
factor.

It is **not** rad(u). The latter also includes primes occurring only
in a^6, which contribute a puncture rather than primitive conductor.
Those primes are nevertheless retained in (1.4). If a different
varying base character is used, one must first enlarge S by its
conductor or keep the possible local cancellations explicitly; this
note makes no unqualified identification in that changed setting.

## 3. The low-conductor inverse moment

For a fixed puncture Q define

\[
 I_{\le C}(H,D;Q,W)
   =\sum_{\substack{0<q_u\le H\\R(u)\le C}}
                             |M_u(D;Q,W)|^2.               \tag{3.1}
\]

**Theorem 3.1.** Under (1.2), for every epsilon>0,

\[
 \boxed{\displaystyle
 I_{\le C}(H,D;Q,W)
 \ll_\epsilon \mathcal S(W)^2
 (HD Cq_Q)^\epsilon H^{1/6}C^{5/6}D^\kappa.}
                                                               \tag{3.2}
\]

This remains true with any further row selection, uniformly bounded
row profiles W_u, and row-dependent punctures q_{Q(u)}<=Q_0, replacing
q_Q by Q_0 and mathcal S(W) by the uniform seminorm. Indeed combine
(1.4) with (2.3), distribute epsilon among the two bounds, and sum
positive squares. This completes the proof.

The exact physical removal identity is

\[
 \begin{split}
 I_{\le C}(H,D;Q,W)
  =\sum_{\substack{v\ {\rm sixth\!\!\!-power\!\!\!-free}\\
                    N\operatorname{rad}(v)\le C}}
      \sum_{q_a^6q_v\le H}
                         |M_v(D;Qa,W)|^2 .                 \tag{3.3}
 \end{split}
\]

Finite unit sectors are understood. Equation (3.3) follows from
chi_n(v a^6)=chi_n(v)1_(n,a)=1; it remains valid when a and v share
primes. Extra copies of a prime in Qa do not change the puncture.
A smooth radial row weight can be retained at its exact argument
q_vq_a^6/H. Consequently (3.2) removes actual nonnegative physical
terms, rather than a conjectural part of a transformed diagonal.

### Three exact quantitative forms

1. **At raw row scale:** the power in (3.2) is at most H when

   \[
                C\le H D^{-6\kappa/5}.                   \tag{3.4}
   \]

   A factor D^{-tau} on the right yields a strict D^{-5tau/6}
   saving, before the arbitrary small losses are charged.

2. **At a proposed extended raw scale H=D^(1-eta):** write

   \[
       C=D^{\rho_\beta-\eta-\tau},\qquad
       0<\eta<\rho_\beta,\quad
       0<\tau<\rho_\beta-\eta.                            \tag{3.5}
   \]

   Then

   \[
       I_{\le C}(D^{1-\eta},D)
           \ll D^{1-\eta-5\tau/6+\epsilon}.              \tag{3.6}
   \]

   The same saving relative to H holds for every H>=D^(1-eta),
   since H^(1/6)<=H D^(-5(1-eta)/6).

3. **Against the inherited amplified moment:** for original row
   scale U and long column D, set C=D^(rho_beta-tau). Then

   \[
      I_{\le C}(U,D)
        \ll U^{1/6}D^{5/6-5\tau/6+\epsilon}.              \tag{3.7}
   \]

   Thus low-conductor rows do not saturate the old amplified scale
   U^(1/6)D^(5/6). At D=U^r the threshold is
   R(u)<=U^{r rho_beta-r tau}.

All comparisons require small epsilon relative to the stated positive
buffer; an equality of exponents alone is not a strict power saving.

At beta=B_flat,

\[
 \rho_\beta=0.1002720471040864\ldots.
\]

This decimal is only an orientation value; (1.3) is the exact threshold.
At the inherited detector r approximately 1.163953577, the cutoff in
(3.7) is approximately U^0.11671 before the positive buffer. The
precise numeric r is not used in this theorem.

## 4. A high-conductor raw theorem would suffice

The preceding low-conductor estimate can be combined with the real
sixth-power amplifier without introducing a new stability assumption.
This gives a smaller sufficient analytic target than a raw theorem
over every row.

Fix eta,tau as in (3.5), and put

\[
 c=\rho_\beta-\eta-\tau>0,\qquad C(D)=D^c.
\]

For the uniform source implementation fix a base Z>=max(2,U,D) and
a constant C_Q in advance, with q_Q<=Z^(C_Q). The input below must
be uniform in those punctures, with the displayed q_Q^epsilon loss.
One can take Z=max(2,U,D,q_Q) and C_Q=1; the resulting buffering
factor is then charged to the final small power of UDq_Q.

**Unproved high-conductor premise HC(eta,c).** Suppose, with the same
fixed-seminorm uniformity, complete row support, and polynomially
bounded growing punctures as the source inverse theorem, that

\[
 \sum_{\substack{0<q_u\le H\\ R(u)>D^c}}
             |M_u(D;Q,W)|^2
       \ll_\epsilon (HDq_Q)^\epsilon\mathcal S(W)^2 H,
               \qquad H\ge D^{1-\eta}.                   \tag{4.1}
\]

The convention of strict source length margins can instead be used by
enlarging H by an arbitrarily small fixed power of the common base.
This is the **remaining analytic hypothesis**, not an assertion proved
by (3.2).

**Conditional corollary 4.1.** If HC(eta,c) holds, then

\[
 \boxed{\displaystyle
  \sum_{0<q_u\le U}^{\rm sixth\!\!\!-power\!\!\!-free}
               |M_u(D;Q,W)|^2
   \ll_\epsilon (UDq_Q)^\epsilon\mathcal S(W)^2
             U^{1/6}\max\{U,D^{1-\eta}\}^{5/6}.}          \tag{4.2}
\]

The same bound holds on all nonzero rows, after absorbing a logarithm
and the puncture losses into the small power. No new boundary is
claimed until the unproved premise and the full scalar comparison are
supplied.

**Proof.** First (3.2) and (4.1) imply the full raw bound of size H on
H>=D^(1-eta); indeed (3.6) already bounds the removed part. One may
now apply the source sixth-power amplification argument verbatim.
For completeness, the high-conductor stability can also be seen
directly, so that no part of the removal has to be recreated after
amplification.

Let H_0=max{U,D^(1-eta)} times an arbitrarily small buffering power.
Choose amplifier primes a in one fixed-width norm interval around
A=(H_0/U)^(1/6), outside S and Q. The buffer permits A to grow; only
O(log(2q_Q)) primes divide Q, and a good prime interval contains
gg A/log A primes. The fixed polynomial bound on q_Q, with the
buffer Z^zeta chosen for any fixed zeta>0, makes these exclusions
negligible for sufficiently large Z. Bounded Z is absorbed in the
constant. Primes in the interval give q_(u a^6)<=C_0 H_0 for a
fixed annular constant C_0; apply HC at that actual row bound.
The exact zero-preserving identity is

\[
 M_u(D;Q,W)=M_{u a^6}(D;Q,W)
  -\frac{\nu(a)\overline{\chi_a(u)}}{\sqrt{q_a}}
                     M_{u a^6}(D/q_a;Q,W).                \tag{4.3}
\]

When a divides u, its second coefficient is zero; the identity still
holds. The map (u,a)->u a^6 is injective for sixth-power-free u,
without a coprimality condition. Moreover

\[
                     R(u a^6)=R(u).                       \tag{4.4}
\]

Thus a row with R(u)>D^c remains in the high-conductor set for both
column lengths D and D/q_a. In particular the shorter-length cutoff
is no larger than D^c. Square (4.3), sum over u,a, use the actual
injection and (4.1), and divide by the prime count. The first term
costs H_0/A up to a logarithm. The second has an additional A^-1
and is no larger.

For the shorter length, q_a/A lies in a fixed compact interval.
A common column scale D/A with profile W(theta x),
theta=q_a/A, suffices. Since A>=1 after buffering,
R(u a^6)>D^c implies R(u a^6)>(D/A)^c, so the one fixed
HC row support contains all the shorter terms.
A fixed one-dimensional Sobolev bound for the function obtained by
replacing W(x) by W(theta x), followed by integration in one common
theta interval, bounds its row-dependent profile by fixed profiles
W(theta x) and xW'(theta x). Apply (4.1) to each fixed theta before
integrating. This justifies the same H_0 bound with finitely many
additional seminorms; no maximum of separate averaged norms is used.
If D/q_a<2, the nonempty bounded windows have only O(1) column
ideals, so their squared row sum is O(H_0) directly; sufficiently
small windows are empty. Thus the second amplifier term never
requires (4.1) outside its stated D>=2 range.

The original low-conductor rows have, by (3.2), size at most

\[
 U^{1/6}D^{(5/6)c+\kappa+\epsilon}
   =U^{1/6}D^{(5/6)(1-\eta-\tau)+\epsilon},              \tag{4.5}
\]

strictly below the amplified term. Equations (4.3)--(4.5), with
H_0/A=U^(1/6)H_0^(5/6), prove (4.2).

For all rows, use the exact decomposition (3.3) without its conductor
cutoff and apply (4.2) at row length U/q_a^6 with puncture Qa. The
row-scale terms sum against q_a^-6; the amplified terms sum against
q_a^-1 up to q_a<=U^(1/6). These cost O(1) and O(log(2U)),
respectively, before the preassigned small powers. The puncture cost
q_a^epsilon is absorbed by first choosing its exponent smaller than
the final allowance. Bounded subunit column windows, if present, are
covered directly by their fixed number of ideals. This proves the
all-row assertion. QED.

### A completely rational calibration

Already beta=7/8 gives kappa=3/4 and rho_beta=1/10. Take

\[
             \eta=\frac1{100},\qquad
             c=\frac2{25},\qquad \tau=\frac1{100}.
\]

Then the low-conductor part at H=D^(99/100) is bounded by

\[
 I_{\le D^{2/25}}(H,D)
             \ll H D^{-1/120+\epsilon}.                  \tag{4.6}
\]

Therefore a proof of (4.1) **only on** R(u)>D^(2/25) in this raw
range would imply the improved amplified long exponent

\[
                e_{\rm new}(r)=\frac16+\frac{33}{40}r,
\]

with its row-scale floor, instead of 1/6+5r/6. The saved exponent
is r/120. This is a conditional numerical calibration, not a proved
moment or a certified finite zero-free boundary. In particular a local
scalar sensitivity formula at eta=0 does not certify that the specific
value eta=1/100 lies in its valid neighborhood.

## 5. What remains after the removal

The current canonical transform does not prove (4.1). Its positive
diagonal at dual row length K=D^2/H is introduced after losing the
signed common-divisor projector. That diagonal has not been identified
with the low-conductor physical rows removed in (3.3). It would be
incorrect to erase it merely because (3.2) controls those rows.

If one wants to insert this restriction directly into Poisson rather
than use the sufficient premise (4.1), the exact arithmetic projector
R(u)>D^c must accompany the row kernel. It is not a smooth radial
cutoff and cannot be dropped without justification. The stable identity
(4.4) helps the amplification, but does not supply a new transform or
an off-diagonal bound for that projector.

The distinction is useful: the remaining raw theorem can be restricted
to a definite growing conductor range, and its full complement is now
bounded with a strict margin. The high-conductor signed correlation,
which carries the actual numerical-boundary difficulty, remains open.

## 6. Proper-order rows: what the supplied classical sieves do not remove

The remaining conductor restriction cannot presently be strengthened to
"genuine order six only" by invoking the standard quadratic and cubic
large sieves. This is already visible on two particularly simple
physical subsets, with no sixth-power overlap to resolve.

Let r run over good squarefree ideals with q_r asymptotic to R. On the
subset u=r^3 the row residue character is quadratic, and on u=r^2 it
is cubic. In both cases its exterior conductor is r. At a fixed
puncture Q, set

\[
 b_n=\mu_E(n)\nu(n)q_n^{-1/2}W(q_n/D)\mathbf1_{(n,Q)=1}.
\]

These coefficients are independent of r, are squarefree-supported,
and satisfy sum_n |b_n|^2<<S(W)^2. The quadratic and cubic kernels
keep the literal zero when (r,n)>1. Fixed reciprocity sectors have
only a bounded cost. Goldmakher--Louvel, Theorem 1.1, and Heath-Brown,
Theorem 2, respectively yield

\[
 \begin{array}{ll}
 \displaystyle\sum_{q_r\asymp R}^{\rm sf}|M_{r^3}(D;Q,W)|^2
       \ll (RD)^\epsilon(R+D)\mathcal S(W)^2,
       & R^3\asymp H,\\[4pt]
 \displaystyle\sum_{q_r\asymp R}^{\rm sf}|M_{r^2}(D;Q,W)|^2
       \ll (RD)^\epsilon\{R+D+(RD)^{2/3}\}\mathcal S(W)^2,
       & R^2\asymp H .
 \end{array}                                                   \tag{6.1}
\]

Here fixed punctures are simply zeros in the column coefficients.
For u=r^3 a^6 or r^2 a^6, at each fixed a the exact same argument
has puncture Qa; overlaps between a and r are permitted and all
natural zeros remain. A varying a cannot be silently removed
before applying the sieve or summing its resulting cost. Nor does
a cubic factor sharing the row variable become a fixed coefficient
in the quadratic sieve.

Write H=D^h with 0<h<1. On both displayed primitive subsets the
largest resource in (6.1) is D. In contrast, the inherited long
amplified scale is

\[
                     H^{1/6}D^{5/6}
                         =D^{h/6+5/6}<D.                   \tag{6.2}
\]

At the supplied critical ratio D approximately H^1.163953577,
h approximately 0.859140794 and the target exponent is approximately
0.976523466. The direct reciprocal alternatives from (1.4) on
these two strata are R D^kappa, with exponents approximately
1.036153559 and 1.179343691, so they do not improve the D resource
there. At the proposed raw H=D^(1-eta), (6.1) similarly gives D,
which is larger than the required H by D^eta.

For the cutoff c in Section 4 these strata contain high-conductor
rows: c<rho_beta is well below h/3 and h/2 in the stated critical
rectangle. Restricting to q_r>D^c decreases the positive row sum,
but the two quoted sieve bounds supply no saving in their D term.
This is a limitation of the supplied upper bounds, not a lower bound
for the actual Möbius moment or a counterexample to HC(eta,c).
Consequently both proper-order high-conductor sectors remain within
the stated unproved target.

The exact source conventions for (6.1) are recorded in the frozen
original Eisenstein source, equations labelled
quadratic-large-sieve and cubic-large-sieve, at OpenAI commit
1581d4cbdd69a0faf34b2089614fe2a814316a6a. The additional
quadratic-family audit is
standalone/2026-10-20-boundary-iteration/global/QUADRATIC_LARGE_SIEVE_SOURCE_AUDIT.md
at the repository source head below. The imported primary results are
Goldmakher--Louvel, [arXiv:1112.1642v2](https://arxiv.org/abs/1112.1642v2),
Theorem 1.1, and Heath-Brown, *Kummer's conjecture for cubic Gauss sums*,
[doi:10.1007/s11856-000-1273-y](https://doi.org/10.1007/s11856-000-1273-y),
Theorem 2.

## Source pins and verification scope

- Repository source head:
  `64cb43c038d1828a478cb97cbc32e435e111d2d2`, PR #1012.
- Reciprocal proof: the two files identified in Section 1.
- Inverse/amplifier normalization:
  `standalone/2026-10-20-boundary-iteration/mixed/MARKED_CANONICAL_MEAN.md`,
  equations (1.1), (2.1)--(2.2), Section 3, at the same source head.
- The actual centered gap:
  `standalone/2026-10-20-boundary-iteration/mixed/CENTERED_INVERSE_INTERFACE.md`
  and `WEAKER_CENTERED_TARGET.md`, at the same head.
- Primary zero-free input: Liu arXiv:2610.26835v1, Theorem 17.1.

The proof is analytic and elementary arithmetic after the imported
reciprocal estimate. Any accompanying exact finite check concerns the
valuation identities and exponent algebra only; it does not certify
L-values, a zero census, the upstream preprint, or HC(eta,c).
