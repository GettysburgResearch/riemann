# Independent review: first-window majorant, close pairs and Bessel bound

Reviewer: semantic_skeptic. Date: 17 November 2026. Inspected pinned K839 commit `0e961ea199b425010843bc8044676d4ad29fe031`, `Distinct839/Defs.lean:45–89`, `Majorant/Pointwise.lean`, and the separated/Fourier source statements. Reviewed and replayed `experiments/code/839_majorant_check.py`; recorded code SHA256 `da45687bd8c0d21a58cfa43e92757044a54c243dbff17f9fe3adeb4ced40f3c8`.

**Conclusion:** the inspected analytic enclosures and exact replay validate this component. No whole-cell, endpoint, sign or Fourier-normalization issue was found. Scope is the first-window pointwise majorant, its separated-set Gram bound and the close-pair scalar premises, using the previously independently validated table at its identical binary hash. This is not a full K839 theorem proof or a Lean build.

## Exact source parameters

The density is

f(u)=[1+sum_(j=1..6)a_j cos(2pi j u)]1_[-1/2,1/2](u),

a=(193305,-23105,29166,13952,-21009,41052)/10^6.

The source constants are theta=17/20, gamma=607/1000, clip c=67/20, beta=8824337/134217728, x=54350/10^6 and y=69433/10^6. The coefficient absolute sum is321589/10^6<1, so f is nonnegative and has integral1. The majorant is

S(u)=sinc(theta(u-1/2))+sinc(theta(u+1/2)),

g(u)=gamma S(u)^2,

where sinc(t)=sin(pi t)/(pi t), extended continuously to1 at0. The code/input constants and source definitions agree.

## Pi and trigonometric enclosures

The arctangent helper returns the interval between two consecutive partial sums of atan(1/q), for q=5 and239. These are valid alternating-series enclosures. Machin's identity pi=16atan(1/5)-4atan(1/239) combines them with the correct direction for the negative coefficient. It can independently be checked from tan(4atan(1/5))=120/119, followed by subtraction of atan(1/239), giving tangent1 in the correct quadrant. Outward decimal rounding to denominator10^55 preserves enclosure.

The chosen rational piQ=355/113 need not lie inside that tight interval. The code uses the maximum distance from piQ to its two endpoints, which bounds |pi-piQ| regardless. All arithmetic in certificate inequalities is exact Fraction arithmetic; the floating clock is used only for elapsed time.

For cosine, reducing j times the midpoint by an integer gives red in[-1/2,1/2). The rational Taylor argument is2piQ*red. Exact periodicity removes that integer with the **true** pi before the approximation is applied. Thus the code's perturbation bound

2piUpper*j*halfwidth+2*piError*|red|

is valid on the entire closed cell. The global cosine Lipschitz constant is1. The18-term Taylor sum is a lower bound and the19-term sum an upper bound: the omitted alternating tail has the required sign and decreasing magnitudes at these orders for |argument|<=piQ. The first cosine terms need not decrease; the proof only uses tail monotonicity. Multiplying a negative coefficient by the lower cosine bound, as the code does, gives the needed upper bound on that signed density term.

For sinc_rad(t)=sin(t)/t, use the entire extension

sinc_rad(t)=integral_0^1 cos(st)ds.

Differentiation gives the global Lipschitz constant1/2, including through0. The code's argument perturbation and division by2 are therefore correct. Its rational sinc arguments have absolute value below3, and the18/19-term alternating power-series bounds have the stated directions at that range. No derivative of sin(t)/t is evaluated by division at0.

## Whole closed cells and squaring

The42 source subintervals form an increasing partition from0 to1/2. The code compares every breakpoint with the actual source list when the pinned source is available; it was available in this review, and its SHA256 agrees with the recorded source hash.

On each cell, the cosine calculation gives f<=fUp. Each shifted sinc has a whole-cell lower bound; their sum SLow is explicitly checked to be strictly positive. Hence S>=SLow>0 implies g>=gamma*SLow². The exact certificate inequality gamma*SLow²>=fUp therefore proves f<=g on the **entire closed interval**, including both endpoints. Evenness covers the negative half. Outside the compact support, f=0 and g>=0. All42 certificates passed replay.

The positivity check before squaring is material: without it, squaring a lower bound on S would not justify a lower bound on S². The implementation includes that check.

## Fourier support, normalization and boundary separation

With transform exp(-2pi i u xi), the inverse transform of

Psi(xi)=(2/theta)cos(pi xi)1_[-theta/2,theta/2](xi)

is exactly S. This follows by writing the cosine as two exponentials and integrating the two boxes. Since Psi is compactly supported and in L2, S is in L2 and g=gamma S² is integrable. The product/convolution theorem gives

ghat=gamma(Psi*Psi).

The convolution is continuous, supported in[-theta,theta], and vanishes at both endpoints: at an endpoint its overlap is a set of measure0, or equivalently continuity matches the zero exterior. In particular differences **equal** to theta have zero off-diagonal Fourier coefficient; strict separation is unnecessary.

The zero-frequency value is

Lambda=integral g
 =gamma integral Psi²
 =(2gamma/theta)[1+sinc(theta)].

This checks the normalization and all factors of2 and pi independently. The rational upper enclosure in the replay is below67/40. I additionally compared it exactly with the stronger source premise in `Spec.lean:48`, obtaining

Lambda<=16711/10000<67/40.

Its decimal display is approximately1.671051566, but the comparison used the exact rational enclosure, not that decimal.

For any finite theta-separated real set y_i and finite complex vector v,

integral g(u)|sum_i v_i exp(2pi i y_i u)|²du
 =Lambda sum_i|v_i|²,

because every off-diagonal transform value vanishes. Replacing g by the nonnegative density f can only decrease the integral. Consequently the f-Gram matrix satisfies0<=G_f<=Lambda I. The finite sum is bounded and both weights are integrable, so all expansions are justified. This establishes the stated Bessel component, not a conclusion about the full zero-operator argument.

## Close-pair table coverage and exact scalar margins

The current table SHA256 is

`b80e5a8c70e4beb3b872dada426016bc97b0954c1a8a5eabaeb40fba49cded36`.

It matches the separately reviewed all209010-cell result `independent_kernel_cells.json`. The grid H=16384, scale V=2^28, last index209009 and binary length all match the pinned inputs/source. This identity check is essential to connecting the new component with the prior whole-cell proof; this review did not rerun that larger proof.

Exactly floor(theta H)+1=13927 cells, indices0,...,13926, cover[0,theta]. The last cell includes the partial endpoint theta; no monotonicity of K is assumed. Their minimum table integer is17657024, giving

min/V-beta=4175/134217728>0.

The prior whole-cell certificates therefore supply K(t)^2>=beta for every |t|<=theta, using evenness on negative t and including endpoints.

All scalar conditions passed exact comparison:

c>2, (c-2)^2-4beta=1308215383/838860800>0,

2beta-2x=956002177/41943040000>0,

4beta-x-y=72982324121/524288000000>0,

8beta-2y=101477376921/262144000000>0.

Since beta>0 and c>2, the first condition is equivalent to2+2sqrt(beta)<c. These are checks of the stated scalar premises; the separate clipped-matrix/transfer proof is outside this review.

## Replay evidence and limits

The guarded script replay exited0. Independent hash, coverage and scalar checks are exported in `experiments/results/839_majorant_skeptic_replay.json`. Source checking found that the initial script lacked explicit table-hash/grid/clip identity guards; the author added those guards, without changing the enclosure arithmetic, before the replay reviewed here. The final pinned script additionally asserts the stronger source LMajBound; that final version was replayed again, also with exit0. This is reproducibility hardening, not a detected mathematical counterexample.

Classification: **Independently checked with no issue found in the inspected portion.** The first-window majorant/close-pair/Bessel component is supported by ordinary analysis and exact rational certificates. The earlier branch search, local-to-global inequality, clipped-matrix argument, pair-correlation moment and complete theorem retain separate evidence requirements. No complete Lean verification is asserted.
