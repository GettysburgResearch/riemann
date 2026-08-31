# Independent audit: cusp quotient positivity versus positive Laplace spectra

Status: PASS WITH FIXED-NORMALIZATION AND QUALITATIVE-ONSET BOUNDARIES.
Review date: 2026-08-31.
Programme: #764.

## Exact accepted source

Original five-file scientific source:
1483ff25e9100276ac7064ba7d7d696b45afb9ea.
Authoring parent: 43ecb4ac3f2487ee944b6bb6bef72e1ad92f2678.
Original programme import: 11a09d8ed0d4150c05d001f4e825107c56650112.
Separate release repair: 282ce03941444d0e02daba5fde260ccb54a3f909.
Repaired programme import: 65e3f808714bbfeaeac30ca389695fa055082ea9.

| Accepted artifact | Frozen repaired Git blob |
|---|---|
| CUSP_FLAG_POSITIVE_SPECTRUM_BOUNDARY.md | d241501272a32771717494dd4c59aa17a6888e98 |
| cusp_flag_positive_spectrum_boundary.py | f229a4e3819759e778a41209576f2c1725cd0d59 |
| cusp_flag_positive_spectrum_boundary.json | e553f9404ab87e7b057fea1e81c81b539242c673 |
| cusp_flag_positive_spectrum_boundary.sources.json | 8138fc876d80a7d87b4f0faee8b5aff2bcfd1a0e |
| tests/test_cusp_flag_positive_spectrum_boundary.py | 8f8879c5f483c73a8f8d7282e9df4fe1324b9916 |

The first four paths are in research/l-families/atlas/generalized/.
Fixture LF SHA-256:
5684f78e970ac3fc9c03f2bab498a0bfc54b4c409d6dd157d07830354a063e8b.
Canonical payload seal:
2d9a02f5eb3a23861c65f9a54dad5ddaceae82912559bf01b8f686ff56eb097d.

Six source bindings retain all five original all-weight family files at
43ecb4 and the weight-24 audit at 8e9f0521. Source bytes, not just derived
JSON, are authenticated. The [separate repair audit](CUSP_FLAG_ARITHMETIC_TAXONOMY_REPAIR_AUDIT.md)
records the metadata-only correction for both family and spectrum reports;
neither written proof nor any mathematical output was changed.

## Accepted source-specific theorem

The [proof](CUSP_FLAG_POSITIVE_SPECTRUM_BOUNDARY.md) fixes every eligible
even level-one weight k, its full Miller basis and first-coefficient flag.
With w=s+k-1 it uses exactly

    F(w)=D11-D1W D_W^-1 DW1,
    L(w)=zeta(2w-2k+2) F(w),
    Q(s)=A_k(s) L(s+k-1).

These are the previously defined uncompleted normalizations. Multiplication
by an arbitrary gamma factor, a changed variable or a parameter-dependent
scalar vector is not part of the theorem.

For real w>k, the positive source matrix gives a unique minimizer f_w over
ell(f)=1. Smooth differentiation is justified by absolute coefficient
convergence at an earlier abscissa and logarithmic moment domination.
Stationarity, not a constant-minimizer assumption, gives

    F'(w)=-sum_(n>=2) log(n) |a_n(f_w)|^2 n^-w <0,
    F(w)>1,  F(w) tends to 1.

Equality would force the modular cusp form to be q, contradicted by its
transformation under z -> -1/z. The same positivity, decrease and limit
hold for L.

Writing a=(1,-D_W^-1 DW1), H=D_W and g=(D'a)_W, the exact curvature is

    F''=a*D''a - 2 g*H^-1g.

The factor is two. In the square-summable coefficient realization it is
also ||(1-P)Xv||^2-||PXv||^2. Thus positive parent Laplace atoms do not
automatically prove scalar convexity after minimization. A declared
non-native Gram calibration has F''(log 2)=-46/125; the packet does not
assert a negative second derivative of the actual cusp quotient.

## Negative atom and the order-of-quantifiers distinction

The parent supplies an absolutely normally convergent generalized
Dirichlet series on a sufficiently right half-plane for each fixed k.
Its first fractional atom has negative coefficient a_*:

    rho_*=(d+1)^2/d,
    a_*=-c_(d+1)^2 b_d(d+1)^2,

except at weights 124 and 248, where the retained zero top pivot is
replaced by the next active pivot, with frequencies 121/9 and 441/19.
Both exceptions and their all-weight nonvanishing proof remain part
of the original source. The same first fractional atom occurs in L.

Put x_*=log rho_*, fix an absolute-convergence abscissa w0, and let
w_m=w0+m/x_*. Termwise differentiation and exact normalization give

    (-1)^m f^(m)(w_m)/(x_*^m exp(-w_m x_*))
      = sum_x a_x exp(-w0(x-x_*))
          [ (x/x_*) exp(1-x/x_*) ]^m.

The bracket is between zero and one and is one only at the target
atom. The summable absolute tilted mass dominates the entire series,
so the displayed value tends to a_*<0 for f=F or L. The derivative
is taken before evaluation at w_m; it is not differentiation of the
sampled sequence.

Local finiteness supplies q_*<1 and the error bound

    exp(w0 x_*) A_rest(w0) q_*^m.

No numerical actual-cusp absolute mass or derivative onset is certified
by this packet. Its optional rational support enclosure leaves rho_*
alone between the adjacent integers. For ordinary weights, the next
endpoint, pivot and depth bounds exceed d+3. For the two exceptions,
both zero top-pivot endpoints and the active next pivot are retained;
the analogous bounds exceed d+4. Square-integer zeta multiplication
cannot insert another frequency in this gap.

In contrast, every fixed derivative order eventually has the correct
alternating sign, by domination by the first positive nonconstant atom.
For F this atom is c_(d+1)^2 at d+1. For L it is at min(4,d+1), including
the exact collision when d+1=4. Taking a maximum of finitely many
thresholds gives one tail for any prescribed finite number of orders.

It does not give one tail for all orders. The moving-order negative
sequence occurs arbitrarily far right. Hence neither F nor L is
completely monotone on any right half-line.

Any positive Borel Laplace measure in this fixed variable, finite on
a right half-line, would imply all alternating derivative inequalities
at every interior point. It is therefore excluded, as is the corresponding
positive fixed-vector semigroup scalar representation. Signed measures,
other transforms, changed variables, renormalizations and parameter-dependent
vectors are not excluded. The original positive variational automorphic
integral is untouched: its minimizer varies with w.

## Independent review and finite replay

The root read the full unchanged proof and manifest, the producer and
complete repaired tests. It verified the positive-half-line argument,
curvature calculation, all-order/fixed-order quantifiers, tilted-mass
domination and support-gap proof, including both exceptional weights.

A separate root reconstruction checked all 138 source atom, positive-leading
atom and rational gap rows against the previously independently rebuilt
family. It derived the three generic gap differences symbolically.
For both complete Gram controls, it formed polynomial matrices in an
independent variable, differentiated their determinant quotients, and
reproduced all moment matrices and F, F', F''. It directly reconstructed
all six signed-exponential controls. All primitive and current hashes,
repair semantics and these mathematical controls also passed -O.

The original independent reviewer reported no mathematical findings,
verified PS1--PS15 and both exceptions, reconstructed all 138 rows,
the direct reciprocal and three-dimensional Gram calibrations, all six
signed controls, and 39 additional optimized-mode type/source/cap controls.
It identified the one arithmetic-taxonomy release defect. Its later
separate exact-SHA repair audit passes without changing mathematics.

The accepted module has 36 tests, all passing normally and under -O;
root times were 3.123s and 2.684s. Both producer modes, Ruff lint/format,
the original parent-to-source whitespace check and the complete repair
diff passed. The 5,264 declared work units are below the 200,000-unit
budget; this is not a wall-clock or arbitrary-JSON denial-of-service bound.

The classical signed-Laplace injectivity argument was checked against
[Salazar, Proposition 2.3 and its proof](https://arxiv.org/html/2607.09868v1#S2).
After shifting to a convergence half-line, finite tilted measures are
determined by their moments under t -> exp(-t). The paper explicitly
credits the abstract implication as elementary/classical. The packet's
moving-order derivative proof is self-contained and does not depend on
a theorem unique to that preprint.

Reproduction:

~~~text
python -B tests/test_cusp_flag_positive_spectrum_boundary.py
python -B -O tests/test_cusp_flag_positive_spectrum_boundary.py
python -B research/l-families/atlas/generalized/cusp_flag_positive_spectrum_boundary.py --check
python -B -O research/l-families/atlas/generalized/cusp_flag_positive_spectrum_boundary.py --check
~~~

No completed-Q positivity classification, numerical cusp onset, actual
cusp second-derivative failure, universal spectral impossibility,
Weil/RH positivity criterion, zero-distribution theorem, RH/GRH result
or external novelty claim follows from this acceptance.
