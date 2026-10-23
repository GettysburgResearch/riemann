# Stronger structured estimates for the zero-free program

Date: 23 October 2026.

**Status:** proposed component mathematics for review. These notes improve
specified estimates used in the zero-free program. They do **not** prove a
smaller zero-free half-plane, and they do not change an integrated claim.

The inherited external benchmark remains
`B_flat = 0.874886647039964...`, as stated in Baiying Liu,
[arXiv:2610.26835v1](https://arxiv.org/html/2610.26835v1), Theorem 17.1.
That preprint and its analytic dependencies have not been independently
certified by this packet. Its Theorem 14.12 concerns the optimum of a
specified comparison system, not an obstruction to a new analytic estimate.

## Results

### 1. The complete nonprincipal additive Gram contribution

[SIGNED_COPRIME_GRAM.md](gram/SIGNED_COPRIME_GRAM.md) retains the full
coprime Euler identity, all prime-power overlaps, every deleted local
factor, and the original common smooth profiles.

For the actual additive Gram sum in Liu (13.7), put `Q=X'Y'`, `Y=Y'`
and `P=Y^2/Q`. The source estimate is

\[
 \sum_{[k]\ne0}|\widetilde A_{[k]}|^2
 \ll \frac QY\left(1+P^{1/6}+\frac{P^2}{Y}\right)Z^\epsilon.
\]

Using the source's unmarked ordinary-product moment M2, the new deduction is

\[
 \boxed{\displaystyle
 \sum_{[k]\ne0}|\widetilde A_{[k]}|^2
 \ll \left\{\frac QY(1+P^{1/6})+1\right\}Z^\epsilon.}
\]

The complete nonprincipal contribution drops from `P Z^epsilon` to
`Z^epsilon`. This application uses M2 as an imported analytic theorem;
it does not require an additional zero-free hypothesis. In the physical
range `X'>=1`, its final constant is absorbed into `Q/Y`, removing the old
extra nonprincipal length restriction.

The note also proves a general smooth coprime-pair estimate under a
common finite-order Hecke zero-free half-plane. For nonprincipal primitive
conductor norm `q`, it gives

\[
 \left|\sum_{(a,b)=1}\lambda(a)\overline{\lambda(b)}
 W(Na/N_1,Nb/N_2)\right|
 \ll (qrN_1N_2)^\epsilon
       q^{\beta/2}(N_1N_2)^{\beta/2}\mathcal S(W),
\]

with all conductor and puncture zeros retained; the precise hypotheses,
an asymmetric variant, and the exact local overlap factors are in the proof.
The exceptional principal `P^(1/6)` term remains. It is already the active
Gram term at the inherited boundary optimizer, so this improvement alone
does not lower that boundary.

### 2. A fully reassembled short-core inverse estimate

[SHORT_CORE_CUBIC_TRANSFER.md](arithmetic/SHORT_CORE_CUBIC_TRANSFER.md)
identifies the actual transformed inverse coefficient with an angular cubic
Gauss coefficient, retaining its fixed ray factors. Its short-core theorem
sums all common-support overlaps, signed divisor variables, extracted sixth
powers, and natural zeros in the specified nonzero transformed component.

Here `H` and `D` are the original row and column scales, and `L` bounds
the norm of the sixth-power-free part of the physical dual frequency.
Up to the displayed small powers and one fixed common profile seminorm,

\[
 \boxed{|T_{\rm short}(H,D;L)|\ll H^{2/3}L^{4/3}.}
\]

This deduction uses the cubic functional equation on its Euler half-plane
and requires no new zero-free premise. It controls the entire specified
short-core sector at size `H` when `L<=H^(1/4)`, with strict buffers for
the small losses.

Given a common finite-order Hecke boundary `beta` with `1/2<beta<1`, the
signed divisor estimate further gives

\[
 |T_{\rm short}(H,D;L)|
 \ll H^{(3-\beta)/(5-2\beta)}
       L^{(7-3\beta)/(5-2\beta)}.
\]

The corresponding cutoff is `L<=H^((2-beta)/(7-3beta))`. The proof explains
why its three complete bounds concern the same signed expression before
interpolation. Original-origin terms and separate source restorations retain
their own estimates; this theorem is not an estimate for the whole inverse
moment.

The remaining long-core contribution is the concrete unresolved part.
The available positive norm still returns a term of size `D`, which exceeds
`H` when `D>H`. Subtracting a short-core upper bound from a full upper bound
does not estimate this complement. The long-core signed diagonal must be
cancelled inside its actual two-column expression.

### 3. Exact finite-cover costs and an ordinary Fourier saving

The two ordinary notes work over `K=Q(i)` and keep that scope separate
from the Eisenstein-field inverse above.

[FINITE_COVER_AND_CUSP.md](ordinary/FINITE_COVER_AND_CUSP.md) computes the
exact evaluation norm on the square-divisibility incidence subspace:

\[
 \|\operatorname{ev}_{x_0}\|^2
 =\sum_{Nd\le R,\ d\ {\rm squarefree}}
       \prod_{p\mid d}\{Np(Np+1)-1\}\asymp R^3.
\]

The actual Mobius sieve nevertheless has bounded probability-normalized
norm, with an explicit squared tail at most `96/R`. Its distinguished
evaluation is exactly a summatory Mobius function. The note derives an
ordinary cusp constant-term saving from a stated prior Mobius estimate and
gives an explicit other-coset obstruction to uniform pointwise inference.

[NONCONSTANT_ORDINARY_SECTOR.md](ordinary/NONCONSTANT_ORDINARY_SECTOR.md)
then proves that a nonzero Fourier mode `k` of a square-divisibility old
section vanishes unless `d|k`. For the actual sieve and its induced
pointwise-square section, this yields a complete ordinary nonconstant
horosphere estimate uniform in `R`:

\[
 \int_{\mathbb C/\mathbb Z[i]}
 |E^{{\rm nc}}_\lambda(z,y;u+it)|^2\,dz
 \ll
 \frac{(1+|t|)^{6-4u+\epsilon}
       y^{2u-2-\epsilon}}{|\zeta_K(u+it)|^2},\qquad 0<u\le1.
\]

Its ordinary reciprocal-zeta factor remains explicit. The induced series
`E[V_R^2]` is not the product `|E[V_R]|^2`. Applying this estimate to the
quartic inverse still requires the actual bilinear angular and cusp
unfolding, with row punctures and the arithmetic diagonal retained.

[ORDINARY_SIEVE_TAIL.md](ordinary/ORDINARY_SIEVE_TAIL.md) proves that the
two induced nonconstant series agree at every frequency with `Nk<=R`.
Their difference therefore gains, in squared norm, any fixed power of
`(1+|t|)^2/(R y^2)` relative to the displayed bound. The spectral and
height factors are paid explicitly. Both series have the same nonconstant
Fourier limit; this gives no convergence assertion for their incoming
constant terms `M(R)` and `M(R)^2`.

## Dependencies and review scope

The complete mathematical arguments, exact source versions, normalization
conventions, and smallest remaining gaps reside in the five proof notes.
The new files are additive and based on main commit
`f99d9e3908dde4865377c75d9ca051c1f545bf4f`.

Important imported inputs are:

| Input | Use |
| --- | --- |
| Liu, arXiv:2610.26835v1, Lemma 12.10, Theorem 12.14, Sections 13.2 and 14.2 | Exact full Gauss correlations, ordinary M2, source profiles and approximate functional equation |
| Dunn--Radziwill, arXiv:2109.07463v3, Section 5 and Appendix A | Cubic periodic-twist functional equation and cusp coefficients |
| `openai/math` at `1581d4cbdd69a0faf34b2089614fe2a814316a6a` | Literal inverse-Poisson and cubic/sextic coefficient dictionary |
| PR #1010 at `a1afee36313ff5994dad7b97983948113571965e` | Primitive-twist Type-I proof used directly at its Euler endpoint |
| PR #1012 at `64cb43c038d1828a478cb97cbc32e435e111d2d2` | Signed common-divisor argument and reciprocal uniformity |
| PR #1016 at `7ea66551190f291101b0dd44fb1fc9b3331c560d` | The precise ordinary/quartic spectral interface being improved |

Repository deductions and current preprints remain source-qualified
dependencies. The finite checkers test local identities, normalizations,
selector logic, and exact exponent arithmetic. They do not certify the
analytic continuations, imported moment theorems, or any zero-free result.

This packet is intended for a draft research PR. A frozen mathematical
commit and subsequent independent agent-review record accompany it;
agent review is not external peer review or formal proof verification.

## Reproduce the finite checks

From the repository root, run:

```sh
python3 -I -S -B standalone/2026-10-23-structured-moment-gains/gram/check_signed_coprime_gram.py
python3 -I -S -B standalone/2026-10-23-structured-moment-gains/arithmetic/check_short_core.py
python3 -I -S -B standalone/2026-10-23-structured-moment-gains/ordinary/verify_finite_cover.py
python3 -I -S -B standalone/2026-10-23-structured-moment-gains/ordinary/verify_ordinary_fourier.py
```

Only the Python standard library is needed. The recorded outputs are next
to each checker. Acceptance uses explicit exceptions, and each script was
also run with `-O`; normal and optimized outputs were byte-identical.

| Checker | Actual finite coverage |
| --- | --- |
| Coprime Gram | 2,298 exact finite-field correlations; 42 independent full small-modulus enumerations; six deleted-prime Euler-factor cases; an admissible direct-exponent regime changing from `1/5` to `17/120` |
| Short core | 13,824 divisibility-selector cases; 54 rational-boundary reassemblies; local digit costs, zero masks and all normalization exponents |
| Finite cover | 725 exact rational predicates for primitive representatives, Gram orthogonality, evaluation, sieve and tail norms, and local convolution |
| Ordinary Fourier sector | 78,281 exact rational predicates for the old-section formula, literal Fourier support, complete lcm cross terms, low-frequency agreement and coefficient bounds |

The direct-exponent example in the first row verifies a component gain of
`7/120`; it does not verify the distinct high-side closure inequalities.
The analytic theorems are justified by the written proofs and stated
dependencies, not by extrapolation from these finite checks.
