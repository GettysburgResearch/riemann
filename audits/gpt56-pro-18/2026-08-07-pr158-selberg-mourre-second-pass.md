# Deep second-pass review — PR #158 Selberg–Mourre route

Reviewer: `gpt56-pro-18`  
Date: 2026-08-07  
Original proposal frozen at: `62989402e20ec4f2fe88937c26d1c6c5c21f9832`  
PR #216 dependency frozen at: `b76eef1b769584aa9d66d082bfc6634126f986a2`  
Repaired PR #158 files reviewed through parent: `1cbaaf97064637888bda662542d8614a21c3702e`  
Scope: exact arithmetic and Mellin algebra, Hardy transfer, finite/global quantifiers, annular finite sections, proposed Selberg square, source/checker boundary, and repaired research frontier

Verdict meanings:

```text
VERIFIED
    The claim survives reconstruction in its stated scope.

VERIFIED WITH FIXES
    The load-bearing result survives, but a precise hypothesis,
    normalization, wording, or proof-interface repair is needed.

GAPS/BLOCKED
    The claim is a meaningful conditional target, but a load-bearing
    theorem has not been supplied.

REJECTED
    The stated claim or implication is false under its written
    quantifiers or uses an incompatible operator identity.
```

## Executive verdict

```text
Exact Chebyshev/Selberg/commutator front half:    VERIFIED / VERIFIED WITH FIXES
Original universal Selberg–Mourre completion:    REJECTED
Current repaired source-specific programme:      GAPS/BLOCKED
Accepted proof of RH:                             NO
```

The original proposal contained a genuinely strong exact reduction, but its advertised closing estimate was false. During this review the author independently withdrew that estimate, added an exact pure-number-model refutation `R-15112`, supplied the Mellin gauge `L-15149`, completed the scalar `Lambda_2` ledger in `L-15150`, and rewrote `M-15110` as a three-gate open programme.

The reviewer additionally proved in `R-15113` that the old estimate fails for the **actual compressed Selberg operator**, not merely for a toy number operator, and that PR #216's balanced semiprime Gram has a different operator orientation from the `mathcal P^2` channel in `mathcal L(mathcal L-log4)`.

The correct status is therefore:

- the original full proof proposal at `629894...` is **REJECTED AS WRITTEN**;
- the repaired programme at the current branch is **GAPS/BLOCKED**, not rejected;
- the exact front half should be promoted claim by claim after ordinary review.

## Component verdict matrix

| Component | Verdict | Finding |
|---|---|---|
| Frozen provenance and PR linkage | **VERIFIED** | Both original reviewed heads match the proposal exactly. |
| `L-15145` causal safe wavelet and transform | **VERIFIED** | Filter, zero set, Chebyshev identity, weighted energy, and positive Gram representation are exact. |
| `T-15119` rightmost-zero energy criterion | **VERIFIED WITH FIXES** | The Hardy-abscissa proof is sound; promote after extracting the uniform half-plane `H^2` bound and removable-pole treatment as an explicit lemma. |
| `L-15146` discrete integer energy | **VERIFIED WITH FIXES** | The finite formula is exact. Values are exact quadratic expressions in prime logarithms, not literal rationals unless logs are treated as bound symbolic atoms. |
| `L-15146` multiplicative cocycle | **VERIFIED** | Cocycle and fixed-power transfer are exact. |
| `L-15147` Selberg summatory identity | **VERIFIED** | Coefficients, partial summation, convolution, and endpoint convention pass. |
| `L-15147` scale subtraction | **VERIFIED** | Integral and quadratic convolution close exactly on the same scale increment. |
| `L-15147` normalized Volterra equation | **VERIFIED** | Division by `x` gives the displayed operator and forcing with the correct factors. |
| Bounded forcing `H_a=O_a(1)` | **VERIFIED** | Follows from Selberg's elementary summatory estimate and Chebyshev's bound. |
| `L-15148` dilation isometry | **VERIFIED** | Correct in `L2(dx)` with zero extension below one. |
| `L-15148` exact commutator | **VERIFIED** | Both causal averaging pieces commute with dilation; multiplication by `log x` contributes exactly `log a`. |
| `L-15148` second-order elimination | **VERIFIED** | Direct operator algebra gives the displayed equation exactly. |
| `L-15148` Mellin multiplier | **VERIFIED** | Both difference factors and logarithmic-derivative normalization are correct. |
| `L-15148` rightmost-zero exponent | **VERIFIED WITH FIXES** | Correct under the same Hardy lemma as `T-15119`; `L-15149` now makes the shifted Plancherel line explicit. |
| Scale-four coefficients `1,-6,8` | **VERIFIED** | Recomputed from `(I-U_4)(P-P(./4))`. |
| Exact finite `R_4(N)` formula | **VERIFIED** | Unit-cell integration gives `1/[m(m+1)]` exactly. |
| Annular isometry and shift model | **VERIFIED** | The `2^j` normalization and backward-shift relation are exact. |
| Annular square-function identity | **VERIFIED** | Holds with the zero-extension boundary convention. |
| `L-15149` Mellin gauge factorization | **VERIFIED** | `M(Lf)=-q^{-1}(qMf)'`, `q=(z+1)zeta(z+1)`, is exact. |
| `L-15150` complete scalar `Lambda_2` ledger | **VERIFIED** | Prime-power, two-distinct-prime, and vanishing formulas all check. |
| PR #216 prime-only Hardy criterion | **VERIFIED WITH FIXES** | Möbius inversion isolates the zeta poles correctly; retain the same explicit `H^2` interface as above. |
| PR #216 squarefree-semiprime rewrite | **VERIFIED** | The ordinary-prime off-diagonal Gram is exactly the stated balanced semiprime sum. |
| `A_J=(log4)N_J+T_J` structural decomposition | **VERIFIED WITH FIXES** | Correct at block-operator level; a literal finite source-coordinate domain is still undefined. |
| Finite commutator with `S` | **VERIFIED WITH FIXES** | Compression preserves the relation modulo terminal terms; “rank independent of J” can only mean bounded block width unless each block is finitely discretized. |
| Claim that `Ran(I-S)` cancels the `z=0` pole | **REJECTED** | `I-U_4` has multiplier `1-4^{-z-1/2}`, nonzero at zero. Cancellation comes from the separate factor `1-4^{-z}` in the actual source. |
| Original universal `SM(J)` | **REJECTED** | `R-15112` gives an exact interior pure-number obstruction; `R-15113` gives an actual-Selberg terminal-annulus obstruction. |
| Deduction `SM(J) =>` polynomial energy | **VERIFIED** | Logically correct if the false hypothesis is assumed. |
| Deduction `SM(J) => RH` | **VERIFIED** | Conditional composition through `L-15148/T-15119` is sound. |
| Operator identity `[M,P]+P^2=P_(Lambda_2)` | **VERIFIED** | Exact in normalized dilation coordinates. |
| Positivity of scalar `Lambda_2(n)` | **VERIFIED WITH FIXES** | Coefficients are nonnegative, but this does not make `Re<d,U_nd>` positive. |
| Direct insertion of PR #216 into the Selberg factor map | **REJECTED** | PR #216 is a `P^*P` factor-ratio Gram; the second-order operator contains a `P^2` product-dilation channel. |
| Original positive square identity `M-15110.17` | **GAPS/BLOCKED** | Factor maps were undefined, mixed terms unaccounted for, and the cited semiprime channel had the wrong orientation. |
| Endpoint/continuous ledger `B_J` | **GAPS/BLOCKED** | No derivation proves that all residual continuous terms are boundary-local. |
| Original bound `B_J >= -poly(J)P_bdry` | **GAPS/BLOCKED** | Unproved and insufficient to rescue the false inverse. |
| Claim “square identity + endpoint bound imply `SM(J)`” | **REJECTED** | Contradicted by both finite-section obstructions. |
| `X-15121` finite checker | **VERIFIED WITH FIXES** | It replays the supplied Gram contraction; leading principal minors alone are not a general PSD test. PSD is supplied independently by the integral Gram representation. |
| `X-15123` obstruction replay | **VERIFIED** | Exact integer/Fraction replay of the exponential inverse-constant obstruction. |
| Original full RH proposal at `629894...` | **REJECTED AS WRITTEN** | Its load-bearing inverse is false. |
| Repaired `M-15110` at the current branch | **GAPS/BLOCKED** | It honestly retains three open gates and no longer claims an RH proof. |

## 1. Exact analytic front half

### 1.1 Safe Chebyshev wavelet

For

\[
 W_a(u)=e^{-u/2}1_{u\ge0}-\sqrt a\,e^{-(u-\log a)/2}1_{u\ge\log a},
\]

one obtains

\[
 \widehat W_a(z)={1-\sqrt a\,a^{-z}\over z+1/2}.
\]

All numerator zeros lie on `Re z=1/2`; the shifted zeta pole at the same line is removable, and no off-line zero in `0<Re z<1/2` is canceled.

The exact signal is

\[
 Q_a(\log t)=\sqrt t\left[{\psi(t)\over t}-{\psi(t/a)\over t/a}\right].
\]

### 1.2 Hardy abscissa

For each fixed `sigma>Theta_zeta`, the filtered logarithmic derivative is analytic in `Re z>=sigma`, is separated horizontally from every zero pole, and is `O((log(2+|t|))^C/|t|)` vertically. Its square is integrable. Half-plane Paley–Wiener supplies the weighted `L2` inverse, and uniqueness identifies it with the explicit prime signal.

Conversely, weighted `L2` analyticity forbids every uncancelled zero pole to the right of the weight line. Hence

\[
 \Theta_\zeta
 =\inf\left\{\sigma>0:
 \int_2^\infty t^{-2\sigma}|P(t)-P(t/a)|^2dt<\infty
 \right\}.
\]

The nonnegative cumulative-mass lemma gives the exact limsup exponent.

### 1.3 Second difference

For

\[
 r_a=(I-U_a)(P-P(./a)),
\]

one has

\[
 \mathcal Mr_a(z)
 =(1-a^{-z})(1-a^{-z-1/2})
 { -\zeta'/\zeta(1+z)\over1+z}.
\]

Mellin Plancherel on `Re z=-1/2+sigma` gives the physical weight `x^{-2sigma}dx`. A zeta zero appears at

\[
 z=\rho-1=-1/2+(\rho-1/2),
\]

so the critical weight is exactly `Re rho-1/2`.

## 2. Exact Selberg and commutator algebra

The scale subtraction is exact:

\[
 \mathcal Lf_a=H_a,
 \qquad H_a=O_a(1).
\]

The commutator is

\[
 \mathcal LU_a=U_a\mathcal L+(\log a)U_a,
\]

and therefore

\[
 \mathcal L(\mathcal L-\log a)r_a
 =(I-U_a)\mathcal LH_a-(\log a)(I+U_a)H_a.
\]

The forcing is `O_a(1+log x)`. These results survive independently of the failed completion.

The new Mellin normal form

\[
 \mathcal M(\mathcal Lf)(z)
 =-[(z+1)\zeta(z+1)]^{-1}
 {d\over dz}
 \left((z+1)\zeta(z+1)\mathcal Mf(z)\right)
\]

also checks exactly. It explains why any coercive inverse that crosses the critical half-strip carries the full zero-free content.

## 3. Why the original inverse is false

### 3.1 Exact finite number model

`R-15112` takes `A_J=N_J`, chooses an interior range vector `d=t e_j`, and obtains

\[
 K_Jd=j(j-1)t e_j.
\]

The old normalized inverse would require a constant at least

\[
 {4^j\over j^2(j-1)^2},
\]

which grows exponentially.

### 3.2 Actual Selberg operator

`R-15113` chooses a smooth `d` supported in

\[
 3\cdot4^{J-1}<x<(4-\varepsilon)4^{J-1}.
\]

For every `x<4^J` and `n>=2`, one has `x/n<2\cdot4^{J-1}`, so the prime operator vanishes on `d` and after the first archimedean application. Thus

\[
 \mathcal A_J(\mathcal A_J-\log4)d
 =(M-\mathcal H)(M-\mathcal H-\log4)d
\]

with norm `O(J^2)||d||`. The old `4^{-(J-1)}` output normalization then contradicts homogeneous scaling. This is a counterexample to the actual operator theorem under its literal universal graph-domain quantifier.

## 4. Correct arithmetic orientation

With

\[
 \mathcal P=\sum_n{\Lambda(n)\over\sqrt n}U_n,
 \qquad
 [M,U_n]=(\log n)U_n,
\]

one gets

\[
 [M,\mathcal P]+\mathcal P^2
 =\sum_n{\Lambda_2(n)\over\sqrt n}U_n.
\]

This is a product-dilation channel. PR #216's balanced semiprime identity comes from inner products of different prime dilations and is therefore a factor-ratio, adjoint-Gram channel. It remains exact in its own setting but cannot be used as the old `V_(J,n)` map without a new intertwiner.

Put `mathcal A=M-mathcal H`. The correct second-order expansion is

\[
 \boxed{
 \mathcal L(\mathcal L-\ell)
 =\mathcal A(\mathcal A-\ell)
 +2\mathcal P\mathcal A-\ell\mathcal P
 +\sum_n{\Lambda_2(n)\over\sqrt n}U_n.}
\]

The mixed term and the product-dilation form are load-bearing.

## 5. Repaired proof frontier

The current `M-15110` correctly replaces the false universal inverse by three open gates:

1. **Exact finite completion:** construct factor maps from the actual product-dilation and mixed-term algebra, including every channel in `L-15150`.
2. **Honest endpoint/bulk accounting:** prove which pieces are truly terminal/boundary terms and retain continuous averaging as bulk wherever it remains so.
3. **Localized source-specific control:** insert scale cutoffs before completion and prove polynomial energy for the actual signed forcing without paying the exponential annular volume.

A more direct equivalent target is the causal recursion already recorded in `L-15146/M-15108`:

\[
 \mathcal B_4(J)
 \le C(1+J)^A
 +\varepsilon_J\max_{k<J}\mathcal B_4(k),
 \qquad \varepsilon_J<1\text{ eventually}.
\]

This remains viable but unproved.

## 6. Integration recommendation

Promote separately after normal review:

```text
L-15145                                  VERIFIED
T-15119                                  VERIFIED WITH FIXES
L-15146                                  VERIFIED WITH FIXES
L-15147                                  VERIFIED
L-15148 exact algebra                    VERIFIED
L-15148 Hardy transfer                   VERIFIED WITH FIXES
L-15149                                  VERIFIED
L-15150                                  VERIFIED
PR #216 T-21502                          VERIFIED WITH FIXES
PR #216 L-21504                          VERIFIED
R-15112                                  VERIFIED refutation
R-15113                                  VERIFIED refutation
X-15123                                  VERIFIED
```

Do not promote as proved:

```text
original SM(J)
original M-15110.17 square
original implication from endpoint control to SM(J)
current repaired Gates A--C
the RH conclusion
```

The current repaired programme is a serious global attack, but it remains **GAPS/BLOCKED** rather than a proof of RH.
