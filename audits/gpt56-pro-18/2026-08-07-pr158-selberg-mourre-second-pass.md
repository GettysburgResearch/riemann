# Deep second-pass review — PR #158 Selberg–Mourre proposal

Reviewer: `gpt56-pro-18`  
Date: 2026-08-07  
Frozen PR #158 head: `62989402e20ec4f2fe88937c26d1c6c5c21f9832`  
Frozen PR #216 dependency: `b76eef1b769584aa9d66d082bfc6634126f986a2`  
Review artifact commit: created after the frozen review; it does not retroactively alter the verdicts below  
Scope: load-bearing algebra, Mellin/Hardy transfer, finite/global quantifiers, annular operator structure, proposed square completion, source/checker boundary, and exact RH conditionality

Verdict meanings:

```text
VERIFIED
    The claim survives reconstruction in its stated scope.

VERIFIED WITH FIXES
    The load-bearing result survives, but a precise hypothesis,
    normalization, terminology, or proof-interface repair is needed.

GAPS/BLOCKED
    The claim is a plausible or useful conditional target, but a
    load-bearing theorem has not been supplied.

REJECTED
    The stated claim or proposed implication is false under its written
    quantifiers or uses an incompatible operator identity.
```

## Executive verdict

```text
Exact Chebyshev/Selberg/commutator front half:  SURVIVES
Current Selberg–Mourre finite completion:       REJECTED AS WRITTEN
Repaired source-specific recursion programme:  GAPS/BLOCKED
Accepted proof of RH:                           NO
```

The proposal contains a genuinely strong exact reduction. The Hardy/Mellin energy criteria, scale-subtracted Selberg equation, dilation commutator, second-order elimination, finite positive scale-four energy, and annular square-function model survive review.

The current completion fails for two independent structural reasons:

1. `SM(J)` is false under its literal universal finite graph-domain quantifier. A vector localized in the terminal half of the last annulus sees no prime term at either operator application, so its output is only `O(J^2)` times its norm. The `4^{-j}` output normalization then contradicts homogeneous scaling.
2. The Selberg term in `mathcal L(mathcal L-log4)` is a product-dilation channel coming from `mathcal P^2`; PR #216's balanced semiprime Gram is a factor-ratio channel coming from `mathcal P^*mathcal P`. The latter cannot be inserted directly as the positive factor map claimed in `M-15110`.

The exact counterexample and corrected operator algebra are recorded separately in `R-15112`.

## Component verdict matrix

| Component | Verdict | Finding |
|---|---|---|
| Frozen provenance and PR linkage | **VERIFIED** | The reviewed heads match the PR descriptions exactly. |
| `L-15145` causal safe wavelet and transform | **VERIFIED** | The filter, zero set, Chebyshev identity, weighted energy, and Gram kernel are exact. |
| `T-15119` rightmost-zero energy criterion | **VERIFIED WITH FIXES** | The Hardy-abscissa argument is sound; the upper-half-plane `H^2` bound and removable pole should be written as a standalone analytic lemma. |
| `L-15146` discrete integer energy | **VERIFIED WITH FIXES** | The finite sum is exact. It is an exact quadratic expression in prime logarithms, not literally a rational number unless logarithms are retained as symbolic/source-bound atoms. |
| `L-15146` multiplicative cocycle | **VERIFIED** | The cocycle and fixed-power transfer are exact. |
| `L-15147` Selberg summatory identity | **VERIFIED** | Coefficients, partial summation, endpoint convention, and convolution term pass. |
| `L-15147` scale subtraction | **VERIFIED** | The integral and quadratic convolution both close on the same increment exactly. |
| `L-15147` normalized Volterra equation | **VERIFIED** | Division by `x` gives the displayed operator and forcing with correct factors. |
| Bounded forcing `H_a=O_a(1)` | **VERIFIED** | Follows from Selberg's elementary summatory estimate and Chebyshev. |
| `L-15148` dilation isometry | **VERIFIED** | Correct in `L2(dx)` with zero extension below one. |
| `L-15148` commutator | **VERIFIED** | Both causal averaging pieces commute exactly; only `log x` contributes `log a`. |
| `L-15148` second-order elimination | **VERIFIED** | Direct operator algebra gives the displayed equation exactly. |
| `L-15148` Mellin multiplier | **VERIFIED** | Both dilation factors and the logarithmic derivative normalization are correct. |
| `L-15148` rightmost-zero exponent | **VERIFIED WITH FIXES** | Correct under the same half-plane Hardy lemma as `T-15119`; the shifted Mellin line should be made explicit. |
| Scale-four coefficients `1,-6,8` | **VERIFIED** | Recomputed directly from `(I-U_4)(P-P(./4))`. |
| Exact finite `R_4(N)` formula | **VERIFIED** | Unit-cell integration gives `1/[m(m+1)]` exactly. |
| Annular isometry and shift model | **VERIFIED** | The `2^j` normalization and backward-shift relation are exact. |
| Annular square-function identity | **VERIFIED** | Holds with the zero-extension boundary convention. |
| PR #216 prime-only Hardy criterion | **VERIFIED WITH FIXES** | Möbius inversion isolates the zeta poles correctly; the standard `H^2` continuation should remain an explicit imported interface. |
| PR #216 squarefree-semiprime rewrite | **VERIFIED** | The unordered prime-pair Gram is exactly the stated balanced semiprime sum. |
| `A_J=(log4)N_J+T_J` structural decomposition | **VERIFIED WITH FIXES** | Correct at the block-operator level; the actual finite source coordinate/domain is not defined. |
| Finite commutator with `S` | **VERIFIED WITH FIXES** | The causal compression preserves the relation modulo terminal compression, but “rank independent of J” is false as literal source-coordinate rank unless block rank is meant. |
| Claim that `Ran(I-S)` cancels the `z=0` prime pole | **REJECTED** | `I-U_4` has multiplier `1-4^{-z-1/2}`, nonzero at `z=0`; the cancellation comes from the separate factor `1-4^{-z}` already present in `f_4`. |
| `SM(J)` universal finite-section estimate | **REJECTED** | Terminal-annulus counterexample `R-15112`. |
| Deduction `SM(J) => R_4(4^J)<<J^A` | **VERIFIED** | Logically correct if `SM(J)` were true. |
| Deduction `SM(J) => RH` | **VERIFIED** | Correct conditional composition through `L-15148/T-15119`. |
| Selberg coefficient identity inside the operator square | **VERIFIED** | `[M,P]+P^2=P_(Lambda_2)` is exact in normalized dilation coordinates. |
| Positivity of scalar `Lambda_2(n)` | **VERIFIED WITH FIXES** | `Lambda_2>=0`, supported on integers with at most two distinct prime factors; coefficient positivity alone does not imply operator-form positivity. |
| Direct insertion of PR #216 into `V_(J,n)` | **REJECTED** | PR #216 is `P^*P`/factor-ratio geometry; the second-order operator contains `P^2`/product-dilation geometry. |
| Positive square identity `M-15110.17` | **GAPS/BLOCKED** | Factor maps are undefined, mixed terms are unaccounted for, and the cited semiprime channel has the wrong orientation. |
| Endpoint/continuous ledger `B_J` | **GAPS/BLOCKED** | No derivation shows that all residual bulk terms reduce to boundary traces. |
| Lower bound `B_J >= -poly(J)P_bdry` | **GAPS/BLOCKED** | Unproved; even if true, the terminal boundary norm is not controlled by the displayed `SM(J)` right side. |
| Claim `(17)+(18) imply SM(J)` | **REJECTED** | Contradicted by the terminal-annulus test; a terminal trace or a source-specific recursion is indispensable. |
| `X-15121` finite checker | **VERIFIED WITH FIXES** | It correctly replays the supplied Gram contraction, but leading principal minors alone are not a general PSD test. The analytic Gram representation supplies PSD independently. |
| Full current RH proof proposal | **REJECTED AS WRITTEN** | Its load-bearing finite coercivity statement is false. |
| Corrected Selberg/renewal route | **GAPS/BLOCKED** | The exact front half remains a serious route, but it needs a source-specific contraction with a controlled terminal term. |

## 1. Exact analytic front half

### 1.1 Chebyshev safe filter

For

\[
 W_a(u)=e^{-u/2}1_{u\ge0}-\sqrt a\,e^{-(u-\log a)/2}1_{u\ge\log a},
\]

one obtains

\[
 \widehat W_a(z)={1-\sqrt a\,a^{-z}\over z+1/2}.
\]

All zeros of the numerator lie on `Re z=1/2`; the zeta pole at the same point is removable, and no off-line zero in `0<Re z<1/2` is canceled.

The signal identity

\[
 Q_a(\log t)=\sqrt t\left[{\psi(t)\over t}-{\psi(t/a)\over t/a}\right]
\]

and the weighted energy change of variables are exact.

### 1.2 Hardy abscissa

For every `sigma>Theta_zeta`, the filtered logarithmic derivative is analytic on `Re z>=sigma`, has a fixed positive horizontal distance from every zero pole, and decays like one inverse vertical power times a polylogarithm. Its square is vertically integrable. Half-plane Paley–Wiener therefore gives the upper weighted-energy bound.

Conversely, weighted `L2` analyticity forbids every uncancelled zero pole to the right of the weight line. Thus

\[
 \Theta_\zeta
 =\inf\left\{\sigma>0:
 \int_2^\infty t^{-2\sigma}|P(t)-P(t/a)|^2dt<\infty
 \right\}.
\]

The cumulative-mass lemma then gives the exact limsup exponent.

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

On the Mellin-Plancherel line `z=-1/2+sigma+it`, a zeta zero `rho` appears at

\[
 z=\rho-1=-1/2+(\rho-1/2).
\]

Therefore the critical weight is exactly `Re(rho-1/2)`. The second factor has zeros only on the boundary `Re z=-1/2`, so it does not remove an off-line obstruction.

## 2. Exact Selberg and commutator algebra

The scale-subtracted summatory identity and normalized Volterra equation have the correct coefficients. In particular,

\[
 \mathcal Lf_a=H_a,
 \qquad H_a=O_a(1).
\]

The exact commutator is

\[
 \mathcal LU_a=U_a\mathcal L+(\log a)U_a.
\]

Consequently

\[
 \mathcal L(\mathcal L-\log a)r_a
 =(I-U_a)\mathcal LH_a-(\log a)(I+U_a)H_a,
\]

and the forcing is `O_a(1+log x)`.

These are durable results independent of the failed completion.

## 3. Why `SM(J)` is false

The exact proof is `R-15112`. The key point is that a test vector supported in

\[
 3\cdot4^{J-1}<x<(4-\varepsilon)4^{J-1}
\]

has no prime preimage inside `[1,4^J)`, even after one application of the archimedean part. Therefore

\[
 \mathcal A_J(\mathcal A_J-\log4)d
 =(M-\mathcal H)(M-\mathcal H-\log4)d
\]

and has norm only `O(J^2)||d||` in the terminal annulus. The normalized output in `SM(J)` is `O(J^4 4^{-J})||d||^2`, whereas the left side is `||d||^2`. Homogeneous scaling contradicts the estimate for large `J`.

This failure is not a small endpoint constant. It says an unweighted global inverse cannot be controlled by the proposed block-normalized forcing norm on an unrestricted finite graph domain.

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

This is a product-dilation channel `U_(pq)`. The balanced semiprime Gram of PR #216 is a factor-ratio channel from inner products of `U_p` and `U_q`, hence from an adjoint composition. It is valuable in its own prime-energy problem but is not the channel in the displayed second-order operator.

The full corrected identity is

\[
 \begin{aligned}
 \mathcal L(\mathcal L-\ell)
 ={}&(M-\mathcal H)(M-\mathcal H-\ell)\\
 &+2\mathcal P(M-\mathcal H)-\ell\mathcal P
 +\sum_n{\Lambda_2(n)\over\sqrt n}U_n.
 \end{aligned}
\]

A future square completion must start from this formula and retain the mixed term.

## 5. Corrected proof frontier

The exact front half supports two viable next targets.

### A. Source-specific causal recursion

Prove a literal block contraction

\[
 \mathcal B_4(J)
 \le C(1+J)^A
 +\varepsilon_J\max_{J_0\le k<J}\mathcal B_4(k),
 \qquad \varepsilon_J<1\text{ eventually}.
\]

This is already recorded in `L-15146/M-15108`. It naturally retains the terminal trace as a previous-scale quantity rather than discarding it.

### B. A finite Carleman estimate with terminal data

A valid finite operator inequality would need the form

\[
 \|P_Jd\|^2
 \le \operatorname{poly}(J)
 \left[
  \text{normalized forcing}
  +\|P_{\mathrm{top}}d\|^2
  +\|P_{\mathrm{bottom}}d\|^2
 \right].
\]

To prove RH one must then establish a strict contraction or decay theorem for the terminal term. Omitting it gives the counterexample above; retaining it exposes the actual RH-bearing step.

## 6. Integration recommendation

Promote separately, after ordinary review:

```text
T-15119                    VERIFIED WITH FIXES
L-15147                    VERIFIED
L-15148 exact algebra      VERIFIED
L-15148 Hardy transfer     VERIFIED WITH FIXES
PR #216 T-21502            VERIFIED WITH FIXES
PR #216 L-21504            VERIFIED
R-15112                    PROPOSED REFUTATION
```

Do not promote:

```text
M-15110.12 SM(J)
M-15110.17 as a PR #216 factor-ratio square
M-15110.18 => SM(J)
the full RH conclusion
```

The repaired research programme remains serious, but it no longer has only one finite identity between the present repository and RH.
