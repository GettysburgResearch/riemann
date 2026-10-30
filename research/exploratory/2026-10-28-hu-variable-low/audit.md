# Source audit of the variable-scale low-side calculation

**Status:** Independent source-matching and scalar review of [the variable-low note](README.md). Hu's [v1 manuscript](https://hexagonmath.org/2610.00216v1), §§3.3–3.5, 4.3–4.4 and 6.1–6.5, is treated as a source of claimed inputs, not independently proved here. No new zero-free theorem follows. I found no specific contradiction in the source matching, but the source's finite Gauss tables, field/sector calibration and reflected-energy theorem remain imported.

## One rescaled subset

Fix the subset `J` of rescaled slots, its prime tuple, and `d=sum_(i in J) ell_i`. Hu (6.9) uses `X'=X/N(p_J)`, `Y'=Y/N(p_J)`, and `Z'=Z N(p_(J^c))`; the remaining slots in `J^c` mark the whole completed index. Since the same prime norm divides `X` and `Y`, `Y'/X'=Z^b` exactly up to fixed window conventions. The row ball has exponent

```text
M'=lx+ly-2d=1-ell-2d,
ell'=ell-d,
N*=1+ell'+theta_N,
M'+ell'-1=-3d.
```

The completed coefficient match to Hu (4.18) is exact under his displayed calibrations. Set the squarefree label `f=1` and puncture `rho=1`, and choose `nu=conjugate(G) psi` in `Theta union psi Theta`. Hu §4.2 gives `a0=conjugate(Lambda) gamma_2`; therefore `a0(c)nu(c)=gamma_2(c) vartheta(c)` and `conjugate(Lambda)^3 nu(n)^3=vartheta(n)^3`, with `vartheta=conjugate(Lambda) conjugate(G) psi` from (6.1). The actual completed coefficient is consequently `gamma_2(c)vartheta(c n^3)/(Nc)^(1/2)Nn`, with its character and whole-index mark, as required. The surviving slot coefficient is its original `Wi(Np/Pi) conjugate(psi)(p)` times a separated norm phase; it remains independent of the additive row and of the dual index. The `J` primes are frozen rescaling parameters and do not create an additional puncture or an unrequested coprimality condition.

The stated orientation of `psi` matters: Hu Proposition 3.2 chooses conjugation so the theta-period angular type is nonzero. This is assumed in the variable-low statement. It is not a proof that the identical displayed probe applies directly to an unoriented target or to a norm twist that has not first been removed.

## Mark masks and the conductor ledger

Hu Theorem 3.5 and Lemma 4.8 explicitly remove a primal tuple meeting its row, and retain the active/inactive mark split, `1_(P,d)=1` and `1_(P,n')=1` masks, finite classes, and the unrestricted cube variable. Thus the `J^c` marks need to be applied **before** reflection and summed within the completed row, exactly as proposed; they may not be replaced with independent rowwise prime choices. The source's recorded coefficient independence after its local tables is the needed input, not a conclusion of the Gaussian Fourier manipulation.

Under that source identification, with no label and no non-slot puncture, every prime in the active nonresidual ordinary radical `A0` lies in the frozen powerful row part `k_pow`. Every prime of that ideal has valuation at least two, including primes with valuation `0 mod 6`; active mark primes are accounted for separately by `za`. The local contributions assigned to `N0` are a subproduct of the same `A0`. Hence, up to fixed dyadic support constants,

```text
2 A0 <= O+O(1/log Z),     N0<=A0,     za<=ell'.
```

This follows from ideal divisibility, not from an assumed relation between arbitrary variables. Its limitation is that it relies on Hu's identification of the active ordinary radical and on the primal zero masks in the marked local expansion. Fixed exceptional primes may be absorbed only after S is fixed; a changing prime cannot be called an S-prime.

## Retained blocks and tails

On Gaussian annulus `N*=1+ell'+theta_N`, Hu (4.19) gives

```text
Td=2H+2A0+2za-N*-N0-3B0 <= H-3d+O(|theta_N|+1/log Z).
```

Hu's Lemma 4.8 permits a dual block only after the independent retained/tail split `v+3 lb<=Td+tau_ref`; blocks outside it have arbitrary power decay at the cost of fixed higher kernel order and its associated seminorms. On retained blocks, the [elementary scalar lemma](../2026-10-28-variable-energy-lemma.md) uses the preceding ledger and yields squared completed-row exponent at most

```text
M' + (5ell+d-1)_+/4 + O(epsilon+|theta_N|).
```

The identity `1+3ell'-2M'=5ell+d-1` was checked symbolically. This is **not** the fixed numerical simplification `Z^M'` from Hu (6.22), and must be retained when varying `ell`. If `Td` is too small for any nonnegative dual block, the retained set is empty; the source tail assertion covers the complement. Its constants, profile orders and total lengths must remain uniform in the fixed finite slot system and target type as stated by Hu.

The companion [Gaussian separation](../2026-10-28-gaussian-slot-profile.md) is a valid way to supply fixed annular tests: on the `j`th logarithmic annulus the Fourier density and all fixed polynomial frequency moments are `O(exp(-c j^2))`; the completed-index phase and each slot phase separate, while the same original zero masks remain. Keeping `|j|<=eta log Z` gives `|theta_N|<=eta+O(1/log Z)`. The absolute tail uses fixed ideal counts, compact unit-sector representatives and the genuine completed series, not the reflected bound. Applying Hu Lemma 4.8 to each Fourier component and integrating its fixed polynomial height/seminorm factors requires exactly the source's common-profile uniformity and finite-sector calibration; these are imported, not independently derived.

## Additive Gram and normalization

Hu Proposition 3.8 applies at fixed `p_J` to `Q0~X'Y'`, `Y'`, with `Pa=Y'^2/Q0~Z^b`. It requires `Q0,Y'>=1` in fixed polynomial ranges, a row-independent coefficient and one common annular profile. The hypotheses `lx>ell` and `ly-ell>11b/6` imply those scale requirements and `Pa^2/Y'<<Pa^(1/6)`. Hu explicitly says the additive coefficient in the physical probe is independent of the fixed unitary target; its phase belongs in the completed theta row. The additive Gram then contributes `(X')^(1/2) Pa^(1/12)` after Cauchy–Schwarz with the completed-row bound and the source prefactor.

The frozen `J`-tuple count costs `Z^(d+epsilon)`, its coefficient costs `Z^(-3d/2)`, and `(X')^(1/2)` contributes `Z^(-d/2)` relative to `X^(1/2)`. Their combined factor is `Z^(-d)`. For `ell<=1/5`, `5ell-1<=0`, so the extra exponent from the square root of the energy is at most `d/8`, leaving `-7d/8`. The fixed number of subsets and the logarithmic number of retained annuli cost an arbitrarily small power. Hu's normalization `Z^(-ell/6) product_i S_i(Z)` is `Z^o(1)` and has reciprocal `Z^o(1)` because each fixed, nonnegative, nonzero window has `S_i~constant*P_i^(1/6)/log P_i` by the fixed-field prime ideal theorem. This uses the same fixed S, windows and physical probe on both sides.

## Remaining assumptions

The derivation does not independently prove Hu's Proposition 3.1 arithmetic calibration, Theorem 3.5 finite marked tables and sector recombination, Proposition 3.8, or Lemma 4.8's actual-row kernel tail and profile uniformity. In particular, if the source permits a hidden non-slot puncture or a row-dependent mark coefficient in this physical specialization, the `2A0<=O` or common-profile step would need revision; none is displayed in (6.1) or (6.9). The use of a fixed theta orientation, a fixed finite slot system and target-dependent analytic constants must remain explicit. This audit confirms the algebra and the displayed source mapping, not the underlying theta or analytic results.

## Moving profiles and family closure

There is no displayed requirement in Lemma 4.8 that the marks or their scales be fixed numerically as `Z` moves: its product-form mark (4.17) uses disjoint prime lists and row-independent bounded coefficients, with the active total length `za` explicit in (4.19)–(4.20). Its constants and finite seminorm/height orders are stated for bounded real length ranges. The specialization here freezes the `J` tuple before applying the lemma, while the surviving `J^c` marks are still summed inside the row norm. The frozen tuple changes the scale and produces bounded individual slot phases; it does not create a fresh coefficient depending on the row. This is the source-level reason the moving marks are admissible, conditional on the completeness of the claimed local table.

For the Gaussian, the separated factor `(N(c n^3)/(Z P))^(it)` is a **global norm twist in the test**, not a new arithmetic background depending on the row. Hu §4 explicitly puts such norm twists into the smooth profiles and allows fixed polynomial costs in their frequencies. The compact annular profile has uniformly controlled seminorms after integration against the rapidly decreasing Fourier density. This matches the stated parameter order; it does not license an independently chosen smooth weight for every physical row.

For the [common-family closure](../2026-10-29-unitary-family-closure.md), Hu (2.2) fixes the three types `0,omega_infinity,conjugate(omega_infinity)`, all finite-order twists, and norm translations. The theta orientation can be fixed for each type orbit before those twists: finite-order twists leave its continuous angular weight unchanged. Hu Proposition 4.14 explicitly claims the real losses and moment mesh can be fixed before the later finite-order target and its conductor; after that target and the finite slot system are fixed, seminorm and height degrees may depend on them. Its §8 then chooses the target-dependent height exponent only after the common real saving, and the external tail order last. The low-side exponent in the calculation above depends on `b,ell` and the fixed field-level source exponents, not the target or the specific subset, while its constant and threshold may depend on the target.

This verifies the **quantifier route**, conditional on Hu's uniformity claims and on every high-side real margin having a positive lower bound independent of the later target. It does not show that the high-side bounds actually meet those hypotheses. If a positive saving were obtained only after a target-dependent real choice, the supremum argument in the family-closure note could fail: arbitrarily small target-dependent savings need not reduce the family supremum. Norm twists must be restored by vertical translation and conjugation of the target, as in Hu, rather than silently treated as the same oriented physical expression.
