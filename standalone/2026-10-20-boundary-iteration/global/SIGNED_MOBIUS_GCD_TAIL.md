# A signed long-gcd tail from uniform Mobius cancellation

20 October 2026. **Conditional consequence of a common Hecke zero-free
half-plane; new signed-tail estimate, not a complete inverse improvement.**
The short common-divisor sector remains uncontrolled by this argument.

It suffices to assume a common zero-free half-plane `Re s>beta`, with
`1/2<beta<1`, for the finite-order cubic Hecke characters arising below,
their fixed finite-ray twists, and their norm translates. A common
boundary for every finite-order Hecke character is a convenient stronger
premise. Norm translation does not change any real part of a zero.
The uniform reciprocal and Mobius proof in
`../uniform/UNIFORM_INVERSE_AND_STRIPPING.md` then applies to this family:
its growth estimates are uniform in conductor, while norm twists are
vertical translations. No growing angular infinity type occurs.

In particular the inherited finite-order theorem of Liu already allows
`beta=B_flat`, retaining its source dependencies. The new all-unitary
extension in this packet is sufficient but unnecessary for this tail.
The premise cannot be replaced by a pointwise bound with uncontrolled
conductor constants.

## 1. Exact unselected component

Use the pinned Ope26a source at commit
`1581d4cbdd69a0faf34b2089614fe2a814316a6a`, SHA256
`42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3`.
The relevant labels are `initial-formal-component`,
`initial-common-extraction`, and `initial-outer-arithmetic`.
The zero extensions and full common profile are as audited in
`../mixed/CENTERED_INVERSE_INTERFACE.md`.

Let `H,D` be the original row and column lengths. Fix dyads
`NC~C` and `Ns~S`, with `C,S>=1` and `CS` at most a fixed multiple
of `D`. Fix the earlier mode and finite ray summand, and take no prime
slots. Sum the complete component over the overlap ideals in the first
dyad, their divisors `d'`, nonzero frequencies `h'`, and the common
divisors in the second dyad. The two residual squarefree columns have
length

\[
                     N=D/(CS).                             \tag{1}
\]

Allow bounded nonempty endpoint dyads in the usual way. The whole
signed component, denoted `T(C,S)`, satisfies

\[
 \boxed{\quad
 |T(C,S)|\ll_{\beta,\epsilon}
  (DHq_j)^\epsilon\,\mathcal S\,
                   D^2 C^{-2}S^{\beta-2}.
 \quad}                                                    \tag{2}
\]

Here `j` is the inherited fixed puncture, and `mathcal S` is a fixed
finite smooth seminorm, with the usual polynomial cost for the earlier
norm-twist mode. Formula (2) concerns the signed, principal-restored
nonzero component before triangle in `s`; it is not an estimate for one
positive canonical child. Its original diagonal, principal restoration,
and raw frequency tail retain their separate source bounds.

## 2. The character in the Mobius sum

Freeze the two residual columns `n1,n2` and `C,d',h'`. The source's
common-extraction identity makes the product of the two extracted
`A_*(s)` factors equal to one on its support. All remaining arithmetic
dependence on `s` is exactly

\[
 \mu(s)\,\chi_{n_1}(s)^4\overline{\chi_{n_2}(s)^4}
                 \mathbf 1_{(s,Cjh')=1}.                    \tag{3}
\]

The character zeros already exclude primes of `n1 n2`. In particular
one does not discard the zero when a local exponent cancels to zero.
After replacing the product in (3) by its primitive inducing Hecke
character, all removed zeros are retained in a puncture of radical
dividing `Cj h'n1 n2`. Its moving conductor divides the radical of
`n1 n2`, up to the fixed bad-place modulus. Reciprocity, if needed
for a different symbol convention, costs only a fixed ray partition.

The uniform zero-free premise implies, for this primitive character
`psi` and any such puncture `Q`,

\[
 \sum_{Ns\le x}\mu(s)\psi(s)\mathbf 1_{(s,Q)=1}
 \ll_\epsilon (\mathcal C(\psi,0)NQ)^\epsilon
                            x^{\beta+\epsilon}.             \tag{4}
\]

Indeed its Dirichlet series is `1/L(s,psi)` times the inverse local
Euler factors at the extra excluded primes. On each fixed half-plane
strictly to the right of beta their product and fixed derivatives cost
`(NQ)^epsilon`, after decreasing the preliminary epsilon. Perron gives
(4) by the same uniform argument as for the unpunctured series. A norm
twist is either included in `psi` or in the smooth profile.

## 3. Preserve the common kernel before applying (4)

Keep both original windows and the full Fourier kernel in the `s`
weight. Its relevant factors are

\[
 \frac1{q_s}
 W_0(q_Cq_sq_{n_1}/D)\overline{W_0(q_Cq_sq_{n_2}/D)}
 \mathcal K_{\rm init}
 \left(\frac{Hq_{h'}}{q_{d'}q_s^2q_{n_1}q_{n_2}}\right).
                                                               \tag{5}
\]

Insert only the original smooth dyad cutoffs. No triangle over the
individual `s` ideals, or alteration of their phases, has occurred.
The inherited outer frequency ball is independent of `s,n1,n2`.
For fixed residual columns in the enclosing `N` annulus, define

\[
                 L=\frac{D^2q_{d'}}{Hq_C^2}.             \tag{6}
\]

Every fixed number of Euler derivatives in `q_s/S` of (5) is bounded by

\[
       \mathcal S_A S^{-1}(1+q_{h'}/L)^{-A}.
\]

This follows directly from the six independent normalized coordinates:
the two windows have bounded ratios, while the kernel argument is
`q_h'/L` times a product of ratios in fixed compact sets. Schwartz
decay absorbs all derivatives. Thus partial summation using (4) gives

\[
 \left|\sum_{s\asymp S}\frac{\mu(s)\psi(s)}{q_s}
                       (\text{full smooth profile})\right|
 \ll (DHq_jq_{h'})^\epsilon\mathcal S_A
                   S^{\beta-1}(1+q_{h'}/L)^{-A}.         \tag{7}
\]

One may first make a common smooth Fourier separation, provided its
weighted seminorm is retained and the `s` sum remains signed. Direct
use of (5) already supplies the required uniformity.

## 4. Count the remaining variables and locate the gain

After (7), absolute values in the remaining variables are legitimate.
The outside factor is `H/(D q_d')`; the two normalized column sums cost

\[
 \left(\sum_{n\asymp N}q_n^{-1/2}\right)^2\ll N.
\]

The frequencies `h'` lie in the fixed Eisenstein lattice used in the
source's masked Poisson formula. Its number of elements of norm at most
`x` is `O(1+x)`, and its nonzero norms have a fixed positive lower bound;
the finite unit multiplicity is included. Consequently the full nonzero
frequency sum of the decay in (7) is `O(L)`. For `L<1`, use decay order
greater than one to obtain `O(L^A)`, which is at most `O(L)`. The extra
small power in `q_h'` is absorbed in the final small power and decay.
For a fixed overlap ideal, the product of these factors is

\[
 \frac{H}{Dq_{d'}}\,
 \frac{D^2q_{d'}}{Hq_C^2}\,
 \frac{D}{q_CS}\, S^{\beta-1}
       =D^2q_C^{-3}S^{\beta-2}.                         \tag{8}
\]

Summing `d'|C` costs only a divisor power. Summing the `O(C)` overlap
ideals gives (2). All coprimality restrictions retained so far can only
reduce these final positive counts.

For example, the signed dyad is at most the original row scale `H`
when, with fixed positive buffers for the small powers,

\[
 S\ \ge\ \left(\frac{D^2}{HC^2}\right)^{1/(2-\beta)}.    \tag{9}
\]

At `C=1` this is a nonempty part of `S<=D` if `H>=D^beta`.
Against the existing amplified scale `H^(1/6)D^(5/6)`, the weaker
threshold is

\[
 S\ \ge\ \left(D^{7/6}H^{-1/6}C^{-2}\right)^{1/(2-\beta)}.
                                                               \tag{10}
\]

For `C=1` it is feasible already when `H>=D^(6 beta-5)`; any strict
inequality in (9) or (10) gives the corresponding fixed power saving.
These are nontrivial long-common-divisor ranges. They do not imply a
saving in the full inverse norm: the sector `s=1`, and more generally
short common divisors, is still present and can dominate. At the
inherited critical scale `D` approximately `H^1.16377`, (9) with
`beta=B_flat,C=1` is empty, while (10) remains nonempty. No numerical
zero-free boundary decrease follows from the tail estimate alone.
