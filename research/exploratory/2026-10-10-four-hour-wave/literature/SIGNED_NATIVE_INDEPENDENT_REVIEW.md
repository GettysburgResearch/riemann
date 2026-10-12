# Independent signed balanced native witness audit

Date: 2026-10-10 UTC. Read-only audit of the frozen wave packet; no checkout or Git mutation.

**Scoped PASS.** I find no mathematical or arithmetic gap in N1–N5 of `literature/SIGNED_BALANCED_NATIVE_WITNESS.md`. Its exact witness demonstrates a nonzero positive finite signed remainder, including the coprime leading face. It does not estimate that remainder asymptotically, disprove a moment estimate, or prove RH. The spatially compact smooth witness and the source's Fourier-compact Poisson test are explicitly distinct.

## Frozen artifacts

Wave: `/workspace/riemann/research/exploratory/2026-10-10-four-hour-wave`.

- Proof SHA256: `23e1f1075d49fa6d91e123b944cf5305cb7bbca8d2fc00660de567f92895b351`.
- Checker SHA256: `e5f577319fca28b115452781224fcd396c27c3255d1a040e5dfa32dd6eb6c154`.
- Owner certificate SHA256: `5bc6036c9139dad239d3214881354f7d40379fd55ee6dd1d31c9ef45394e91f6`.
- PR914 source commit: `0cc0428fedbbfc340044c7451b3d392c1da9a103`.
- Literal `CONDUCTOR_SECTORS.md` SHA256: `c160bbb1b1d7c6bcc5514d496ad41f15fd17ea3d36206b0d05cfa0d7d6503983`.
- Literal `A2_COMPLETION.md` SHA256: `d99eade56807077b07e5ec1325001f1592115db216e1e10e6a3906a3e01f0aad`.

The two literal source files under `/workspace/.riemann-research/moment-sources/914/standalone/2026-10-10-sextic-moment-conductor-core/` were read and their current hashes independently checked. Their controlled-sector estimates and Poisson theorem remain imported analytic inputs, not independently reproved here.

## Source and normalization audit

1. N1, proof lines 20–29, is the exact residual set in `CONDUCTOR_SECTORS.md` lines 475–525. That source takes the literal union of the no-singleton and low-complexity controlled sets, counts its overlap once, and retains the full smooth character sums with principal masks. The remaining condition is `g1 != 1` and `Ng1*sqrt(Ng2)>H`, equivalent to the squared comparison used by the checker. The error is `O(H D^(k+epsilon))`, and the unpaid assertion is an upper bound on the signed real remainder. No positivity of a sector was substituted for positivity of the full moment.

2. N2, proof lines 33–53, correctly uses ideal factorization, rather than merely equality of rational norms. Equality of left and right products forces equal prime multiplicities; every occurring prime then has even total multiplicity and no singleton. This also handles residual exponents divisible by six at higher order. The correction-triple product `s_t=c^3 d^3 e^4` and reconstructed product covariance agree with `A2_COMPLETION.md` lines 657–678. The diagonal is `s_t*x1*x2=s_t'*y1*y2`; it is not equality of the individual factor pairs.

3. N3, proof lines 57–74, correctly preserves the exact common-factor collapse already derived in `BELOW_DIAGONAL_SOURCE_ADAPTER.md` lines 79–101: for squarefree g, each prime dividing g contributes zero unless it divides k, and contributes -1 if it does, giving `mu(g)*1[g|k]`. The balanced residual coefficient is independent of the selected divisor f after the change `c_j=f*m_j`. Substituting `k=g*h` gives the displayed profile `Psi(H*Nh/(Ng*Nd1*Nd2))`. On the pairwise-distinct face the product columns are coprime, so `b=g=f=1`; neither this auxiliary collapse nor the four original Mobius signs cancels the leading fourth-moment tuples.

4. The actual coefficient family is the source's `mu_K(n)*nu(n)*W(Nn/D)` (`CONDUCTOR_SECTORS.md` lines 55–79). The witness chooses the allowed principal finite character and eight good prime ideals, all excluding primes above 2 and 3. Its fixed smooth norm profile has supremum one. The bumps of radius strictly below 1/60, scaled by D=30, have norm radius below 1/2, hence only integer norms 7, 13, 19 and 31 occur. Each splits into precisely two distinct prime ideals, and all eight coefficients equal -1. No arbitrary coefficient class is being substituted.

5. The compact spatial row majorant is allowed by `CONDUCTOR_SECTORS.md` lines 79–108. A fixed radial C-infinity profile can be one on `|z|^2<=1` and zero on `|z|^2>=41/40`, so at H=40 its lattice values are exactly the sharp row indicator. The zero row contributes zero since every prime character has its zero extension there. This is different from the source test in `A2_COMPLETION.md` lines 470–493, whose Fourier profile Psi is compact. The witness is not claimed to evaluate the centered expression for that other test.

6. N5, proof lines 131–157, correctly retains the source normalization in `A2_COMPLETION.md` equation (6.3), lines 478–493. Its b=f=1 coprime component has prefactor H/L^2. The displayed E_cen has prefactor 1/L, so its contribution is `(H/L)*E_cen`; the proposed bound `|E_cen| << L*D^epsilon` would pay this component at `H*D^epsilon`. At L=D^2 and H=D^(1+theta), the frequency length is `L^2/H=D^(3-theta)` and its ratio to L is `D^(1-theta)>1`. Other common factors, moving masks, finite ray components and the correction covariance still require estimates. This remains an explicit conditional contract, not a bound inferred from the finite witness or from positive completed energy.

## Native arithmetic and completeness

Checker lines 58–78 verify the primary generators and their conjugates, exact prime norms, residue-field roots and eight distinct ideals. Its primary convention is `a=1 mod 3`, `b=0 mod 3`; the seeds and conjugates satisfy it. The field image of omega is `-a/b mod q`. The symbol is the sixth-power residue symbol `v^((q-1)/6)` identified with the six exact Eisenstein units, and is zero for a nonunit. Integer-pair multiplication, conjugation and norm are correct.

Checker lines 80–88 enumerate the complete 150 nonzero rows. The identities `4N-3a^2=(a-2b)^2` and `4N-3b^2=(2a-b)^2` imply `|a|,|b|<=7` for N<=40, so the larger [-8,8]^2 box misses nothing. Lines 109–156 enumerate all 8^4=4096 ordered Hermitian tuples, preserve all nonunit masks even when a residual exponent is zero, partition the exact critical set, and use Counter equality for the actual ideal-product diagonal. All pairwise-distinct tuples satisfy the strict critical comparison. Negative controls in lines 158–167 correctly expose the errors from dropping a principal zero mask or reducing an odd sextic residual to a cubic phase.

## Independent oracle

`/tmp/review_signed_balanced_native_oracle.py` has SHA256 `2db8cee0ddbe1e53ffa82346c075427f4425cc792e66e817678279c524256063`. It changes the arithmetic implementation and summation organization:

- It uses basis `1,zeta6`, with `zeta6^2-zeta6+1=0`, instead of the checker's basis `1,omega`.
- It constructs both finite fields for each norm from all roots of `r^2+r+1=0 mod q`, independently of the primary-generator seeds.
- It constructs the sextic characters from a primitive-generator discrete-log table and the discrete log of `1+r`, rather than the checker's Euler-power value lookup.
- It enumerates lattice rows from the exact quadratic discriminant inequalities, rather than the rectangular row box.
- It evaluates 1296 left/right unordered-pair blocks with explicit permutation multiplicities, rather than the 4096 ordered-tuple loop. It also independently groups the leading contribution by the 70 four-ideal sets and six left/right assignments, with multiplicity four.
- It computes the original product diagonal directly row by row as `2*n_active^2-n_active`.

Normal and optimized oracle receipts are byte-identical:

`/tmp/review-signed-balanced-native-oracle-normal.json`

`/tmp/review-signed-balanced-native-oracle-optimized.json`

SHA256 for either: `dcff13b980725019daeabe178923551a3c9b71bbd4e03c78a686da46d95c089a`.

Both independently reproduce:

| Quantity | Exact value |
| --- | ---: |
| Complete nonzero lattice rows | 150 |
| Good prime-ideal columns | 8 |
| Full fourth moment | 16752 |
| Critical signed remainder | 1176 |
| Controlled complementary contribution | 15576 |
| Original product diagonal | 15564 |
| Leading pairwise-distinct contribution | 456 |
| Critical ordered tuples | 3696 |
| Critical tuples removed by product diagonal | 0 |
| Leading ordered tuples | 1680 |

## Original-checker replay

I also independently ran the frozen original checker with Python normal and optimized modes, to `/tmp/review-signed-balanced-native-normal.json` and `/tmp/review-signed-balanced-native-optimized.json`. Both exited zero and reproduced the retained certificate byte for byte, with SHA256 `5bc6036c9139dad239d3214881354f7d40379fd55ee6dd1d31c9ef45394e91f6`. This also reproduces the original checker's 120 product-diagonal tuples, 560 nonzero critical tuple row kernels, all tuple-wise literal/residual mask comparisons and both negative controls. Hash guards remain active under `-O` because they use `require`, not Python assertions.

Trust scope: this exact finite-field arithmetic is independently reproduced, including support and row completeness. The general controlled-sector and Poisson estimates are the explicitly frozen source imports. No new asymptotic cancellation, coefficient supply, row-moment theorem, zero-free region or RH assertion follows.
