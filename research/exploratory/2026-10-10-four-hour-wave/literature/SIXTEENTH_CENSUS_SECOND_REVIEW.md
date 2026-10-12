# Independent native sixteenth-moment census audit

2026-10-10 UTC, read-only independent analytic/source/code review and final frozen-file/equivalence audit. No checkout/Git mutation. **Scoped PASS** at the source-qualified finite census and companion-column scope below.

## Analytic scope and prior-source bootstrap

I read the complete `xi/outer-ray/SIXTEENTH_MOMENT_CENSUS_RECOVERY.md` S16-1 through S16-4 and `check_sixteenth_moment_census.py`. The intended conclusion is a complete simple actual-Xi census through5419, with4968 positive roots, and the separately proved finite companion columns up to derivative order10835. It is a finite-height theorem with unrestricted vertical column depth and positive lambda, not a cofinal-height or RH assertion.

S16-1 explicitly imports the independently established **count-free complete simple census through2240**, receipt SHA256 `ce21c175914c1e1d3ad049a8b67e6528ae2f72baed309b4719c1ca8de48a7832`. This source is essential. It already proves every root through2240 is the unique simple real root in one of1739 original intervals. The new1561 refined brackets are strictly inside old brackets below2048 and have fresh strict Hardy-Z crossings, so their roots are those same unique already established lower roots. The remaining brackets below2240 are unchanged. Therefore selecting and removing exactly one real occurrence per new/original bracket removes every source occurrence through2240. The **complete remaining source**, not the original whole Xi zero set, has `|Re rho|>2240`.

This preserves the exact source's selection semantics. Above2240 no initial uniqueness or completeness is assumed. Every extra selected multiplicity and unknown nonreal conjugate pair remains in the residual. The older native receipt's historical count and earlier uniqueness assertions are unused. The separate global real-part14 bootstrap is also unnecessary. The prerequisite complete census is itself proved from complete moment/positive-theta/strip facts and strict endpoint signs, so the argument does not reintroduce a historical finite-count contract.

## Complete source moment and corner bound

The actual completed formula is correctly normalized as `Xi(z)=s(s-1)/2*exp(-s*log(pi)/2)*Gamma(s/2)*zeta(s)`, `s=1/2+i*z`. The complete paired genus-zero product in z^2 has no nonconstant exponential factor. Hence `-8*[z^16]log(Xi/Xi(0))` is the complete inverse16 sum over the positive-half-plane source, retaining each analytic multiplicity. Removing one selected real occurrence and its negative reflection subtracts exactly one `gamma^-16` term. The remaining full conjugate grouping makes T8 real; absolute convergence follows already from the inverse-square product sum.

For `f(x,y)=Re((x+i*y)^-16)`, differentiation gives `partial_x f=-16*|z|^-17*cos(17*theta)` and `partial_y f=-16*|z|^-17*sin(17*theta)`. On `x>=2240`, `0<=y<=1/2`, the exact sufficient angle bound `17*atan(1/4480)<17/4480<1<pi/2` makes f strictly decreasing in x and nonincreasing in y. Evenness handles negative y. All remaining roots also have positive real inverse16 projection. Thus any remaining occurrence through H contributes at least

`d8(H)=Re((H+i/2)^-16)=sum(j=0..8)(-1)^j*binom(16,2j)*H^(16-2j)*(1/2)^(2j)/(H^2+1/4)^16`.

The denominator power16 is correct for the real part of the reciprocal complex power; replacing it by8 would be an error. A valid complete residual upper endpoint below this exact corner value excludes every unselected occurrence and extra multiplicity, including an occurrence at the boundary. All other real projections remain nonnegative. The absence of boundary-intersecting selected intervals makes the exact finite list unambiguous.

This proves complete **simplicity** as well as reality/completeness through the accepted height. It does not assume that all unknown roots begin beyond8192 or that candidate indices form a complete list. The strict decrease of d8(H) validates the largest-integer interpretation:5419 passes and5420 fails this particular upper-endpoint predicate. Failure at5420 asserts no zero, no negativity, no mathematical barrier and no RH evidence.

The finite-census column theorem then applies with the correct maximum integer order `2*5419-3=10835`, all lambda>0, every y>=0, and strict finite horizontal range `|T|<5419-(r+2)/2`. The stated nonvanishing and positive `Re(iE/E')` conclusions retain precisely that imported theorem's scope.

## Complete native checker and producer

The checker explicitly sets320-bit precision and truncation capacity17, constructs the degree16 actual Gamma/zeta source jet, checks the strict positive Xi(0) seed/nonzero divisor and every parity/reality enclosure, and forms the normalized logarithmic jet. Every one of8049 selected inverse16 terms is evaluated on its full interval ball. Strict nesting does not replace sign existence; all3122 refined Hardy-Z endpoint signs are freshly computed. Their actual-Xi implication uses the nonzero real gamma factor, so branch choices in logGamma after exponentiation do not change the zero/sign-crossing argument.

The complete old8049 interval inventory is checked for strict positive disjoint geometry. Every new bracket has exact integer numerators and width2^-160 inside its original2^-24 bracket. The lower census geometry is checked at2240 and the final selected list is checked against5419. The native original6488 later strict-sign facts remain explicit imports with their direct source hash map. The count-free2240receipt hash and all its direct sources are checked independently. These import maps authenticate file identity, not infinite theta/product theorems by finite computation.

The corrected candidate producer uses bulk indexed native zeros only for suggestions. The separate checker contains no complete count or root-enumeration call. Producer indexing correctness is therefore unnecessary for existence or completeness: strict source signs and the complete remaining moment supply those facts. The early accidental `sha320` producer typo was corrected before freezing; no failed pre-freeze producer run supplies an accepted candidate source.

All acceptance branches are explicit and survive optimized Python. Current native binaries are hashed in the produced receipt. Normal/optimized modes share the same outward arithmetic backend; distinct source formulations and exact integer controls do not claim another backend.

## Independent coefficient and complete endpoint oracle

My scratch experiment authenticated all3122new signs, strict prefix nesting and full8049-term native moment before packaging. Its complete candidate list and receipt remain frozen under `/tmp`; they are exploratory precursors rather than independent validation of the eventual owned packet.

I then independently evaluated `xi(1/2+t)` at400bits through degree16 and computed its even normalized logarithmic coefficients by **eight explicit coefficient recurrences**, without calling series `.log` and without substituting the complex `i*z` source. The exact relation `i^16=1` identifies the complete C8 coefficient. Each of16098 reciprocal16 endpoint bounds was evaluated by Python integer powers and division onto a fixed320-bit dyadic grid, using exact monotonic endpoints rather than Arb reciprocal powers. This retains the full interval uncertainty for all8049 selections and bounds the exact selected sum independently.

The frozen native scratch residual contains the entire independently tighter interval

`[1.2269305781515028e-60,1.8067724995217247e-60]`.

Both the frozen and independent upper endpoints admit5419 and reject5420. The independent ratios are approximately0.9991032936547856 and1.0020573061835052; only their recorded exact rational predicates are acceptance data.

The original oracle/script/receipt is preserved. A deterministic replay version omits elapsed time from its canonical acceptance payload and sends runtime only to stdout. It was independently run in normal and optimized Python to distinct output files:

`/tmp/review-k8-real-s-endpoint-oracle-normal.json`

`/tmp/review-k8-real-s-endpoint-oracle-optimized.json`

Both passed and are byte-identical, SHA256 `eada12fdf80879c8eca28d7c79cb5d22171893d37b1a2270c7282c2fab4fcf8b`. Script `/tmp/review_k8_real_s_endpoint_oracle_replay.py` SHA256 `2b8a89af87c90ca17fb144f59d5ea2c9751adc75d9d0a8f71402a520226292cc`. Original oracle script `10ce167acc86f6963eab53d5f8362b1409f4ac62cb6cd700f8e7808c062f2548` and receipt `efd9ad6058ef3dd7e92268e5d239092b81acf9a966aee2909f61de18d700b28d` remain unchanged.

The oracle imports new strict signs from the scratch execution and old primitive sign facts from their reviewed source; it does not repeat their full endpoint runtime. Its real-s400-bit native arithmetic shares the declared outward backend but its recurrence and exact integer endpoint summation are independently organized.

## Final frozen binding and review boundary

The corrected owner's packet was frozen and all five current hashes independently verified:

- Proof: `f897ae7c02eb1c912557c22bdd5fa3d2d89c61cdfecaf894d43f7c8943e070d4`.
- Native checker: `88717519250cfd68f6c74398b5f7d16672250966c70d79cebbe016637586eae6`.
- Corrected candidate producer: `4ba9295d839163f2f57e8e4499fb690edeed41f6b5381521b1482cd570139001`.
- Complete candidate file: `2cb7d16f7ad8bd6e7a99cff1f7c94597f39dee01d6da86f078beed4d7657272d`.
- Official native receipt: `964f49cc79a61b354cd77fe1f077637e54bb46f39a5643e1455e87f60fabc4d6`.

Independent exact package control `/tmp/review-sixteenth-package-equivalence.json`, SHA256 `f1b44925cd1e28b41ddd08077cc3e2480f03864c0fa5dfd4caac1eb109ac51af`, verifies all1561 prefix numerator pairs are **exactly identical** to the scratch prefix, along with denomination, cutoff, source input, backend version and producer binding. The entire packaged residual rational interval is **exactly identical** to the scratch interval. Both5419accepted and5420failed rational ratios are exactly identical to the scratch and deterministic independent oracle. All displayed current direct source hashes and six current native binary hashes match. AST controls confirm no complete-count/root-enumeration call in the checker and no Python assert acceptance branch.

The official frozen receipt records successful complete new primitive runtime. Parent `/root/review_setup` independently runs the full packaged native checker in normal and optimized Python; this equivalence audit does not duplicate that packaged runtime. My prior scratch execution did freshly replay all3122signs and complete native degree16/8049interval calculation, with exact candidate/quantity equivalence to this independently reviewed packaged code and receipt. Its normal/optimized independent coefficient-and-endpoint oracle is separately recorded above.

The complete theta identity, classical strip, genus-zero product, previously proved count-free2240census, older primitive sign facts and finite-census column theorem remain named inputs. This audit does not rerun the historical Gram/Rosser contract or prove global real zeros. No checkout/Git integration is authorized by this research review.
