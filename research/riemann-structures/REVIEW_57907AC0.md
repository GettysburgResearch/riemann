# Independent review of the post-quotient principal readout barrier

Scientific freeze: `57907ac05f7f00f147f6ede570c924ae101afec2`.
Proof object: `897377d047b1f5fca7e7d4813f154860605b07c9c82d47693bba84f924d2ce4f`.

I independently reconstructed and read the four-file proof/producer/fixture/test packet. I checked the final source-schema repair and input guards. I did not run a producer or test suite. Root reports Ruff, complete generation, ordinary/optimized checks after final binding, and eleven tests in each Python mode passed.

## Mathematical findings

No remaining blocker was found for the precisely declared FCM/NMO coefficient projection.

The fixed fibre has principal weight `70g^2` and actual positive coefficients `4/(225 sqrt(N_i M_j))`. Four equal literal Boolean-history amplitudes per arithmetic pair give diagonal `w Gamma(0) sum(c_ij^2)/4`; the aggregate-pair diagonal is four times this and is not substituted silently. The source-dual coefficient and factor `2/35` give the same weighted diagonal.

The Gram argument uses differences of two Mellin frequencies. Since every physical product lies in `(Y,1.1Y)`, those differences have modulus below `2 log(1.1)<1/5`. The exact kernel formula, full endpoint variation, and rational bounds `sqrt(2)>707/500`, `log(2)>842/1215>693/1000` give `Gamma(v)>1` throughout that entire range. This is an integrated autocorrelation statement, not a pointwise assertion at zero frequency.

Consequently the actual source vector has energy/diagonal ratio between `25mn/2904` and `4mn`. The coefficient ratio `10/11`, upper bound `Gamma(0)<=384`, and the four-history factor produce the lower constant exactly. The upper bound follows from autocorrelation and Cauchy--Schwarz. The growing admissible rectangles yield the stated sharp order `Y^(1/3)/(log Y)^2` for this ratio. At the same time energy is of order `Y^(-2/3)/(log Y)^4` and diagonal of order `Y^(-1)/(log Y)^2`; neither is an absolute growing-moment counterexample.

The result therefore refutes a subpower diagonal-relative readout bound required to hold uniformly on these restrictions. It does not lower-bound the complete source after complementary fields are added. The final note correctly distinguishes amplification on these vectors from an assertion about the unrestricted global operator, and retains the actual inner products for any omitted t-dependent gamma coefficients.

## Code, provenance and corrections

Exact commit/path/Git-blob checks bind the FCM/NMO projection, SCB kernel, T-106140 normalization and source-first adapter. The producer reads the existing 9- and 12-pair panels; it performs no prime search, floating quadrature or numerical logarithm. Positive irrational coefficients remain positive symbolic square roots, with their squares independently checked against physical N and M. All pairwise frequency-ratio differences, rectangle completeness, the four-history diagonal and source-dual conversion are checked.

The first root execution exposed an assumed NMO proof-hash field that does not exist in the frozen artifact. The final producer checks the actual schema/status after authenticating the exact Git bytes, and adds a full-build regression. That is a source-interface repair, not a mathematical change. Review also requested the explicit common-core bit-length bound and strict integer history-sum type; both are present in the freeze. Test coverage includes history aggregation counterfeits, altered amplitudes, the positive-branch flag, omitted kernel jumps, source blobs, windows and numeric types.

The universal theorem is proved from the frozen all-horizon rectangle construction and kernel inequalities, not extrapolated from the two finite panels. The complete retained-gamma adapter, signed additive/Kummer estimates, canonical integration and RH remain outside this result.
