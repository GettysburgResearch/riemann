# Independent review: averaged-shift transport

Reviewer: `/root/repo_connections`, 25 October 2026.

**Verdict: PASS at the stated conditional scope**, after the hypothesis clarifications below. No new zero-free region or RH proof is established. The complete averaged-correlation estimate remains OPEN.

## Frozen source and exact-commit publication verification

Repository: `GettysburgResearch/riemann`.

Reviewed mathematical commit: `14aba2d9af60f2c2849dfe31bab10f5c6996c8aa`.

Publication branch: `research/hlc-zero-free-transfer-20261025`.

Both published paths below are relative to
`standalone/2026-10-25-hlc-zero-free-transfer/` at that exact commit.

| Published file | Bytes | SHA-256 | Git blob |
| --- | ---: | --- | --- |
| `SHIFT_BRIDGE.md` | 20896 | `4e35da2c609278b4f95ca581da234ef4b0019ac761bec3dedfe570632e32d64b` | `1d38d095b7d0cfa8cf47b11c53ed6c91d9f5ae3e` |
| `verify_shift_bridge.py` | 3352 | `191872e83469b98603cd0cdce71791dbf1f4745e8a23e69ccc70e6f084240625` | `d1b1afb8cefb82a8be21532dd0b08df047fe4ac4` |

I independently fetched both files through the GitHub connector using the
full commit SHA above, encoded the returned contents as UTF-8, and recomputed
both SHA-256 and Git blob SHA-1 (including the Git blob header). Every value
matches the table and the bytes previously reviewed. The published
`SHIFT_BRIDGE.md` is byte-identical to the originally reviewed local
`zero_free_bridge.md`; its renamed path does not alter the mathematics.
The earlier local checker replay therefore applies to these exact published
checker bytes; no additional optional test replay was performed for this
publication verification. Later mathematical edits require a new review
identity.

[Exact published bridge](https://github.com/GettysburgResearch/riemann/blob/14aba2d9af60f2c2849dfe31bab10f5c6996c8aa/standalone/2026-10-25-hlc-zero-free-transfer/SHIFT_BRIDGE.md)
and [checker](https://github.com/GettysburgResearch/riemann/blob/14aba2d9af60f2c2849dfe31bab10f5c6996c8aa/standalone/2026-10-25-hlc-zero-free-transfer/verify_shift_bridge.py).

Authorship: I authored the separate native affine-correlation note, not the initial averaged-shift theorem. I requested two review corrections: nonnegative summatory exponents for the noncompact extension, and `1/2<=alpha<b_0<2 theta-1` for the decreasing recurrence. Both appear in these frozen bytes. This is an independent agent check, not external peer review or formal verification.

## 1. Exact remainder and powers of H

Independently reordering the integer shifts gives

`S_H=sum_n mu(n)W(n/X) integral_0^infinity K((n-t)/H) dpsi(t)`.

For compact W supported in `(1,2)` and `H<=X/4`, every relevant n exceeds 2H. The continuous `dt` term is exactly `kappa H M_W`; no approximation of a lattice shift sum by an integral is being made. All lattice effects remain in `E=psi-t`.

Integration by parts in t gives the plus sign in

`R_H=(1/H) integral E(t) sum_n mu(n)W(n/X)K'((n-t)/H) dt`.

A second integration by parts against `dM(u)` gives the negative sign and both terms in (2.4): `W'(u/X)K'((u-t)/H)/(XH)` and `W(u/X)K''((u-t)/H)/H^2`.

The u-support has length O(X); for each u, the t-support has length O(H), with both variables comparable to X. The unnormalized errors are therefore `O(X^(beta_M+beta_P))` and `O(X^(beta_M+beta_P+1)/H)`. Division by `kappa H` proves precisely

`O(X^(beta_M+beta_P)/H + X^(beta_M+beta_P+1)/H^2)`.

No boundary term of size X is omitted. At `H=X^theta`, fixed theta<1, the support restriction holds beyond a theta-dependent threshold, which is legitimate asymptotically.

## 2. Mellin noncancellation and endpoints

For compact nonnegative nonzero W, `W_tau(v)=W(v)v^(-i tau)` has initial Mellin quotient `W_hat(s-i tau)/zeta(s)`. At a hypothetical zero `rho=beta+i tau`, its numerator equals `W_hat(beta)>0`. Hence the reciprocal-zeta pole, of any multiplicity, cannot be hidden by smoothing. Constants may depend on each fixed tau; no height-uniform assertion is required to exclude a given zero.

The compact sum vanishes for sufficiently small X. Its Mellin integral on `(0,1)` is therefore entire, or one may integrate directly on `(0,infinity)` as in the note.

For the log-Gaussian, direct integration gives `W_hat(s)=sqrt(pi)exp(s^2/4)`, entire and nonzero. If `X<exp(-1)`, then

`|M_W(X)|<=exp(-log(1/X)^2) sum_n n^(-2 log(1/X))`

by discarding the additional factor `exp(-(log n)^2)<=1`. The sum is bounded by zeta(2). This proves faster-than-any-power decay at zero and the required entire lower-end correction.

## 3. Gaussian boundary near n=H

The actual continuous term is `H integral_1^(min(2,n/H))K(v)dv`. It differs from `kappa H` only for `n<=2H`. Since the Gaussian increases on `(0,1)`, its normalized correction is bounded by

`O(H exp(-log(X/(2H))^2))`.

For fixed theta<1 this is smaller than every fixed negative power of X. All fixed weighted moments of W and W' are finite. With the clarified nonnegative beta inputs, the two remainder estimates remain valid when t approaches zero: on the kernel support `1+t<=1+u` and `u>=H>=1`. One does not need `t` comparable to `u` in this small region.

This Gaussian argument does NOT license `H=cX`: its boundary correction then need not decay. The table correctly restricts that row to the compact test family.

## 4. Exponents and conditional bootstrap

At theta<=1, the second remainder exponent dominates, giving `gamma=max(alpha,beta_M+beta_P+1-2 theta)`. The printed decimals agree with this expression. With theta=49/50 and initial 7/8, the exact unclipped sequence is `79/100,31/50,7/25`; alpha=1/2 clips the last value at 1/2. This is conditional on the OPEN full square-root correlation input.

The recurrence decreases under the corrected assumptions `1/2<=alpha<b_0<2 theta-1`. Epsilon losses create no gap in the finite examples: fix the strict margins first and then choose each available epsilon sufficiently small.

I checked the analytic equivalence renewing the summatory premises after each zero-free conclusion. At sufficiently large height, disks centered at `2+it` inside `Re s>b` have an analytic log zeta. Choose radii `r_0<r<r_1<2-b`, the inner disk wholly in `Re s>1`, and the target in the radius-r disk. Polynomial growth and Borel–Carathéodory give `O(log t)` on the outer disk, while the inner bound is O(1). Three-circles gives `O((log t)^a)` for some fixed a<1 at the target. Thus `1/zeta` has subpower growth there; Cauchy controls the logarithmic derivative. Truncated Perron, at noninteger endpoints and a sufficiently large fixed polynomial height, yields the stated `x^(b+epsilon)` bounds. The pole at 1 contributes x to psi. This is for ordinary zeta, not a silently uniform Hecke conductor family.

## 5. Full principal contribution and the added one-sign audit

The note correctly requires the FULL signed average S_H. Bounding only `S_H-kappa H M_W` removes the main term containing the Möbius mean and cannot prove the asserted zero exclusion.

For Section 5.4, I compared the normalized energy to the supplied paper's pp. 43–45, (5.14)–(5.16), and its first Cauchy inequality (4.4), p. 15. Granting the stated idealized Möbius supremum and exceptional-set premises gives energy `M^(2 beta-2)X^epsilon`. The physical source scale is XY, so `Q_Y^maj<<XY M^(2 beta-2)X^epsilon`. Combining `|T_Y|^2<<(X/Y)Q_Y` gives only `|T_Y|<<X M^(beta-1)X^epsilon`. At M=X^m, its exponent `1-m(1-beta)>=beta` is correct.

This is a valid limitation of that particular chain of inequalities. The note explicitly grants the required uniformity and power upgrades hypothetically, rather than deriving them from ordinary zeta zero-freeness or claiming every refinement is impossible.

## 6. Independent finite reproduction

I inspected the checker, then independently ran:

`python -I -B /workspace/scratch/f294926d877d/verify_shift_bridge.py`

| X | H | Absolute error |
| ---: | ---: | ---: |
| 40 | 5 | `7.405742685762107e-13` |
| 80 | 10 | `2.008171406941983e-12` |
| 120 | 12 | `3.715916463420399e-12` |

The exact rational output was `7/8,79/100,31/50,7/25`. The sieve includes actual Möbius values and all von Mangoldt prime powers. The quadrature splits at integer jumps. On each resulting piece the polynomial degree is at most 10, so eight-node Gaussian quadrature is exact algebraically before floating-point evaluation.

This uses ordinary double precision. It checks signs, scale factors and finite algebra; it is not directed interval certification or evidence for the asymptotic correlation bound. The analytic derivation is the basis of the conditional theorem.

## 7. Review limits

I did not prove the full averaged-correlation input, independently certify B_flat or the full OpenAI/Liu arguments, or validate all 52 pages of arXiv:2610.20242v1. The paper-mechanism checks above do not replace its separate audit. The remote verification covers precisely the two published files bound above, not every file in the repository or an integration approval.

The reviewed contribution gives a rigorous bridge and an explicit quantitative target for a stronger HLC mechanism. It does not establish a new unconditional zero-free region.

