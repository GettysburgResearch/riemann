# Independent finite-census and native slab review

Status: scoped analytic and directed runtime PASS, 2026-10-10.
Scope: actual Xi, derivative order zero, lambda=10, closed rectangle -2<=Re(z)<=2 and -1/2<=Im(z)<=0. No cofinal or RH conclusion.
What ran: complete mathematical/source audit and an independent invocation of the frozen checker, with its output redirected to `/tmp/review-native-slab-normal.json` so the author's artifact remained untouched.
Smallest remaining global gap: effective protected margins and complete coverage on an unbounded domain; the finite result does not supply them.

## Analytic audit

`../xi/outer-ray/FINITE_CENSUS_COMPLEMENT.md` C1–C17 passes. The primitive complete census, including multiplicities and its endpoint convention, splits the full actual paired product exactly. Partial summation retains the optional negative complete-count endpoint. The differentiated paired logarithms converge absolutely, and the k=1 cancellation is preserved. The higher logarithmic derivative bounds and Bell/Leibniz recursion retain the entire tail, allowing all off-line zeros permitted beyond the census.

Every nonconstant derivative of the finite simple real-rooted polynomial has simple real roots. Its companion and derivative have strict lower-half-plane sectors, including the real boundary by the displayed Laguerre expression. Compactness supplies the finite protected margins; these are not assumed to be uniform on growing domains. Full-function Leibniz gives the relative numerator and denominator errors in C13. The inequality alpha+(1+tau)beta<tau protects both actual companions and gives the strict sector. The r=0 disk estimate gives exactly C17, without dropping multiplier derivative terms.

`../xi/outer-ray/NATIVE_SLAB_CERTIFICATE.md` N1–N11 and the checker implementation also pass. The completed functional equation gives the displayed actual Hardy-Z normalization and its nonzero factor. The phase exponential is insensitive to Gamma-argument branch changes by 2pi. Opposite directed signs in 8049 disjoint exact dyadic intervals give at least that many simple-or-higher odd crossings; the imported complete count of 8049 then forces exactly one analytic multiplicity per interval and no omitted root. This reasoning correctly derives simplicity from count saturation rather than assuming it from sign changes.

The full finite logarithmic sums, companion quotient, complete-tail negative endpoint and protected predicate match the formulas. The 32-by-8 directed boxes cover the entire closed target rectangle. Exact lower and upper endpoints supply the sector ratio and all strict guards, with no floating-point acceptance.

## Independent runtime and provenance

The checker was independently invoked under python-flint 0.9.0 / FLINT 3.6.0 at 128 bits. All actual Gamma/zeta endpoint brackets, the nonzero census endpoint, xi(1/2)>1/4 seed, exact complete count, complete finite polynomial sums and all 256 full boxes passed. Its complete JSON matched the owner's `native_slab_certificate.json` exactly. A subsequent display-only correction labels rounded console minima as approximations. The acceptance logic and every mathematical receipt field are unchanged; inspection confirmed that the current receipt differs from our independent output only in that checker's source hash. The minimum protected acceptance exceeds 0.241178; the actual companion-sector lower bound exceeds 1.160128. Exact per-box rationals in the receipt are the acceptance evidence.

The completed count explicitly imports FLINT's verified historical Gram/Rosser rule at this index. Neither this replay nor the author's runtime independently repeats that historical finite verification. The complete Hadamard product, classical strip and coarse all-height counting argument remain named analytic dependencies. The producer proposes intervals only; their actual endpoint values are reevaluated independently by the checker. Both runtimes use the same outward arithmetic implementation.

Reviewed SHA-256:

| File | SHA-256 |
| --- | --- |
| `FINITE_CENSUS_COMPLEMENT.md` | `93e623688c60116375a7dffc68ce46919395a2f2ef7c812cd9dc78dd16304748` |
| `NATIVE_SLAB_CERTIFICATE.md` | `0cb56603222f874f9783404f691c32a5e409c2a8fe96c998d75ef6f39c8ef03e` |
| `check_native_slab.py` | `64349a2a5ac7b8e04ff24faeccdb7132e2f0407963b1d5325e289f799138354e` |
| `native_candidates.json` | `bbb7fe9adce4fa9581cbb23fb558c62abafec4e568cb69c4d9f0324443ad8c20` |
| `produce_native_candidates.py` | `4cd87390db736ee4a745942a988da4566412909b51b7cdca029171f2a67aa3f2` |
| `COARSE_ZERO_COUNT.md` | `67725ad90c5caaad231c4e232b76f5c38c81a84efe5005fc8909342456afa726` |

This review validates the finite source-qualified result. An off-real quartet beyond the protected finite domain remains compatible with it; no RH or unbounded continuation is established.
