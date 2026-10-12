# Independent completed Taylor8 weighted native acceptance audit

2026-10-10 UTC. Read-only proof/source/receipt audit and independent normal/optimized replay; all new artifacts under `/tmp`. No checkout or Git mutation and no second full continuum integration.

**Scoped PASS.** The completed Taylor8 continuum residual supports the separately checked weighted lower matrix with exact reserve `1e-11`. Both Python modes pass the full fresh source/moment/matrix replay and the quantitative primitive extractor. This proves the same complex native L2 bounded-window positivity consequence under the inherited operator/source hypotheses. The original scalar `27/2` lower-matrix attempt remains explicitly inconclusive and is not used for acceptance.

## Frozen source and receipt

Operator directory: `/workspace/riemann/research/exploratory/2026-10-10-four-hour-wave/operators`.

- Completed `directed_residual_codim8_trial100_taylor.json`: `cba3fb5f17e71678b115c03813b97dda37ec45c19c24604bd302fd8baaf2ed19`.
- Native continuum producer `enclose_residual_phase8_taylor.py`: `f10b2dad34ab16aa6f66f4693093be60657b5d395432bf29f1af33ede8bf3256`.
- Complete local gamma helper `taylor_convolution_source.py`: `118e828d8bf4cb706fd94c9d179fb8d8de88319df8b20273c4e19284175af0da`.
- Separate weighted Taylor wrapper `enclose_weighted_lower_taylor.py`: `0ba57657eef0ea728134e846c2861f778793715c5d091c3c47090cc87f003f25`.
- `LOCAL_GAMMA_TAYLOR_ENCLOSURE.md`: `e28980ff704350db547dc2843bcf5551ffdad5d49a21a0f6483f0b0cf0765e52`.
- Original source-U producer: `b3832a0cddc8bc1e2603c40240b608d1f06a868bda9436d8e88a146393fe007b`.
- Original convolution helper: `d53aa6c4e9c0e33d26c2327305bc1aa0ae9adef035ea4437ccd2a19b23bbf014`.
- Phase-aware supporting-line checker `check_codimension8_phase.py`: `11f1662311aaa5cbd0f274790069c1cb88b49ff591c4d500c6a63cdbdac6e60f`.
- Quantitative extractor `enclose_primitive_norm.py`: `a84255c51d8409fa33ab00ddbab42199e0e19a86a44bb066dcaf7740d657a5f0`.

The complete Taylor helper and wrapper had already been independently source/math/control reviewed in `/tmp/review-local-gamma-taylor.md` (SHA256 `4740c7f8f06402cd406acef3394780ac1931f37bc26428fd10ad00165954f764`). This audit checks their completed output and unchanged provenance. The reviewed continuum derivation and weighted primitive residual argument are retained.

## Complete continuum receipt

The retained receipt has precision 256 bits, Gaussian order 76, endpoint epsilon `2^-50`, all three physical cusp slabs and **636** panels. An independent exact rational reconstruction gives **212** prescribed normalized dyadic panels per slab: each reflected dyadic interval from epsilon to 1/2 is subdivided into the exact required power-of-two number of equal panels to meet width at most 1/100. Comparing this full list to each source slab proves complete adjacency, no duplicate or omitted panel, and exact endpoint coverage `[epsilon,1-epsilon]` in every slab.

The uniform analytic F bound is about `5.08308232155053e14`; the complete FF quadrature-error sum is about `1.8103182804e-16`, and the complete F-times-projection error sum about `1.0684373177e-30`. They satisfy the full analytic budgets `4*M_F^2*2^-152` and `12*M_F*2^-152`, respectively. The omitted-endpoint/cusp modulus is below one (about `0.0001540067231`); the reviewed producer explicitly pays all six omitted pieces with FF radius `24*epsilon` and mixed radius `36*epsilon` before projecting. None of these errors is discarded because the final scalar LDL failed.

The producer computes the complete residual Gram as `R=FF-FP^T*G_P^-1*FP`, symmetrizes it, and stores the entire 8 by 8 R even when its scalar-cost experiment does not pass. That scalar matrix is `U-(27/2)*R`. Its retained failure is the fifth pivot check near `-4e-5`; status is `DIRECTED_LOWER_INCONCLUSIVE`. This is not a claim of a negative native form or a failure of the subsequently weighted estimate.

The new weighted replay legitimately consumes this completed R despite the scalar status. Completion follows from the reviewed producer, complete exact coverage, source/parameter/helper bindings and error budgets; scalar positivity is unnecessary for R to enclose the exact continuum residual. The wrapper does not accept a partial integration status by relying on it: its coverage and frozen parameter guards must all pass independently.

## Full weighted matrix and native basis

The wrapper first requires exactly five removed sine modes, one hundred trial modes, the frozen Taylor producer, epsilon/order/256-bit precision, and current complete source/convolution/Taylor helper hashes. It freshly reproduces the supporting-line certificate and all native analytic source moments. Every coefficient-ball string must match the completed residual's exact Galerkin inventory, so the fresh moment matrix and continuum residual refer to the same tests.

The complete raw-basis inventory is 108 by 8: unnormalized sines 1–5, `exp(+-t/2)`, `cosh(3t/2)`, then sines 6–105. The source's ordinary Gram/orthonormalization and exact projected-trial construction preserve an orthonormal complement basis and its full Galerkin corrections. No sampled coefficients, omitted projections or frequency-tail assumptions enter.

For this supporting line, `alpha=4/5`, `C=244`, and `lambda_n=alpha-C/(n*pi)^2`. Its first admitted weight at n=6 is positive and the primitive lower constant `kappa=1/6` is valid. The wrapper recomputes the complete finite projected cosine moments for n=6,...,128, plus the whole decreasing inverse-weight tail at n=129. It forms

`B_128=(3/2)*[lambda_129^-1*R+2*sum(n=6..128)(lambda_n^-1-lambda_129^-1)*a_n^T*a_n]`.

All 123 finite corrections are positive. The remaining infinite tail is bounded by the full R through Parseval and monotonicity; it is not truncated. The whole tail inverse is enclosed near `1.25232561562843176926327888105288986630119485`. Symmetrization preserves the exact symmetric matrix; shifted directed LDL proves `U-B_128 >= 1e-11*I`.

## Independent replay and exact matrix oracle

I ran the complete weighted Taylor wrapper in normal and optimized Python to

`/tmp/review-native-taylor8-weighted-normal.json`

`/tmp/review-native-taylor8-weighted-optimized.json`.

Both exited zero, with byte-identical SHA256 `cd2178a404167b9cf47aef2e64141d37f9fa01e35fce2a4b66df1c7f6fc9efc9`. The receipt retains the original scalar status but independently reports `DIRECTED_WEIGHTED_SINGLE_WINDOW_LOWER_ACCEPT` and all eight positive shifted LDL pivots.

The independent oracle `/tmp/review_native_taylor8_receipt_oracle.py` verifies the prescribed panel list, both full Cauchy-Gauss budgets, omitted-neighborhood modulus, source/helper freezes, complete coefficient inventory, all 64 old/current U entries, all 64 scalar matrix constructions and all 64 complete weighted matrix constructions. It then takes exact dyadic interval endpoints for the weighted matrix, constructs the exact rational symmetric midpoint, subtracts the **full maximum row-sum radius** as a matrix-norm perturbation and subtracts exact `1/10^11`. A Fraction-only LDL of that robust midpoint matrix has all eight pivots positive. Thus every exact symmetric matrix admitted by those serialized entry balls has the claimed reserve, independently of the original directed LDL implementation.

The oracle script SHA256 is `d51523a5c275aca550c2d056b8f8e8c984447443c6108e784ef64c71cda9536b`. It runs in both normal and optimized Python with the same byte-identical results, recorded in `/tmp/review-native-taylor8-receipt-oracle-normal.json` and `/tmp/review-native-taylor8-receipt-oracle-optimized.json`, SHA256 `cce4477d8cc2ddf25b60b7b11169967156dcf6628cc572d250f9209bcd4814fb`. Its full maximum row-sum ball-error upper endpoint is the exact rational `7997032517/147573952589676412928`. It uses Arb only to recover native exact interval endpoints and reconstruct the outward source/moment expression; its final positive-definiteness proof is exact Fraction arithmetic.

## Quantitative consequence

I independently ran the frozen primitive extractor against each fresh weighted replay and the unchanged completed R, again in normal and optimized Python:

`/tmp/review-native-taylor8-primitive-normal.json`

`/tmp/review-native-taylor8-primitive-optimized.json`.

Both passed with byte-identical SHA256 `a92c35588db8b3b1af9ea32143397f7dc5b98dda7c12a2c1163827a1434091c4`. The extractor itself repeats the complete fresh weighted acceptance and checks exact semantic equality. It obtains `M=1`, coarse synthesis integer `K=47923878`, `kappa=1/6`, `theta=1/200000000001` and

`delta=1/19169551400000000000 > 0`.

The previously reviewed quantitative Young/synthesis argument gives `q_1(h,h)>=delta*(||Pi_E h||^2+||G_1 h||^2)` for every complex native L2 test. Literal-kernel zero extension gives `q_L(h,h)>=delta*||G_L h||^2` for all `0<L<=1`. Since the initial-value primitive is injective, every nonzero such test has strict positive form.

Trust scope: the exact completed source integration is the owner's reviewed 4727-second native run, not an independently repeated quadrature. This review independently reconstructs full coverage/receipt/matrix acceptance and uses a separate exact rational matrix oracle. All native modes share the declared outward arithmetic backend. The inherited O1–O4 source/operator facts remain named mathematical inputs; the separately reviewed exact Xi kernel identification is not reproved by this receipt. There is no native L2 spectral gap, no positivity for cofinal lengths and no RH conclusion.
