# T-90301 — Inertia-tolerant Q4 recurrence as a full RH proposal

Claim ID: `T-90301`  
Title: The corrected two-state Q4 reflected programme can replace full polarized PSD by a scalar negative-eigenvalue defect; a polynomial defect ledger gives the coefficient-one recurrence and RH  
Status: **FULL CONDITIONAL PROPOSAL — NEW REDUCTION COMPLETE, DEFECT ESTIMATE OPEN / RH-BEARING**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-10  
Dependencies: `L-90301`, `L-90302`, `R-90301`; PRs #341, #342, #345, #346, #350; resident vector-valued pole-energy consumer  
Scope: corrected Q4/Jordan route only

## 1. Frozen source-complete state

Use the corrected Q2/Q4 source order and root-Haar state on PR #350 together with the exact two-state reflected ledger on PR #341.

At each physical logarithmic block `J`, let

\[
K_J
\]

be the complete `2 x 2` Hermitian jet-curvature matrix **after**:

1. independent-frequency localization;
2. complete source convolution;
3. corrected second-current source order;
4. root/low-pass state assembly;
5. inclusion of every product-current and individual reflected term;
6. explicit finite collars and gauges.

Put

\[
E(J)=\operatorname{tr}K_J,
\qquad
\delta(J)=\operatorname{tr}(K_J)_-.
\tag{T-90301.1}
\]

The existing Q4 work supplies, at row/finite-block scope subject to its reviews:

```text
state dimension                                      exactly 2;
true RH-sensitive current                            correctly placed;
source-complete scalar augmented curvature           cofinally positive;
critical radix-four/odd-prime reserve increment      Theta(n log n);
complete product/individual reflected ledger         two-state;
current-scale finite parity synthesis                strict reserve;
all unresolved gauges                                strictly delayed / finite collar;
neutral principal all-pass return                    explicit coefficient one.
```

The earlier proof target demanded `K_J >= 0`.  `L-90301` shows that this is stronger than the synthesis argument needs.

## 2. Exact replacement for polarized PSD

For every parameter-independent synthesis operator `W` with

\[
W^*W\le qI,
\]

`L-90301` gives

\[
\operatorname{tr}(W K_J W^*)
\le q[E(J)+\delta(J)].
\tag{T-90301.2}
\]

Because the state dimension is two,

\[
\delta(J)
=\max\left(0,
\frac{\sqrt{2\|K_J\|_F^2-E(J)^2}-E(J)}2
\right),
\tag{T-90301.3}
\]

and, when `E(J)>0`,

\[
\delta(J)
\le\frac{(-\det K_J)_+}{E(J)}.
\tag{T-90301.4}
\]

`L-90302` further gives an exact Wronskian expression for `det K_J`.  Thus the missing matrix theorem has become one scalar arithmetic defect.

## 3. The production theorem — Q4 Inertia-Defect Recurrence (QIDR)

A complete proof should emit the actual finite synthesis and establish the following statement, not merely cite it.

> **QIDR.** There exist fixed `delta0>0`, `A<infinity`, and a complete source-bound Q4 block decomposition such that, for every sufficiently large `J`, the exact reflected ledger satisfies
> \[
> \boxed{
> \mathcal E(J)
> \le \mathcal E(J-\delta_0)
> +C(1+J)^A
> +D(J),
> }
> \tag{T-90301.5}
> \]
> where `mathcal E(J)` is the RH-sensitive physical block energy and the complete inertia forcing obeys
> \[
> \boxed{D(J)\le C(1+J)^A.}
> \tag{T-90301.6}
> \]
> Every current-scale synthesis contribution is estimated using (T-90301.2), and `D(J)` is the explicitly emitted sum of the corresponding negative spectral masses.  The sole coefficient-one return is the declared delayed principal state.

A stronger but still sufficient rowwise form is

\[
(-\det K_J)_+
\ll n\log^B n
\tag{T-90301.7}
\]

on the critical physical rows.  Since the existing scalar moat gives `E(J) >> n log n` there, (T-90301.4) turns (T-90301.7) into only polylogarithmic negative spectral mass.

## 4. QIDR implies RH

Iterating (T-90301.5) through `O(J)` fixed delays gives

\[
\mathcal E(J)=O((1+J)^{A+1}).
\tag{T-90301.8}
\]

Hence

\[
\mathcal E(J)=e^{o(J)}.
\]

The resident vector-valued pole criterion for the Q4 physical current then excludes every zeta zero with real part greater than one half.  Functional-equation symmetry gives

\[
\boxed{\mathrm{QIDR}\Longrightarrow\mathrm{RH}.}
\tag{T-90301.9}
\]

No reviewer is being asked to prove QIDR: it is explicitly the remaining production theorem.

## 5. Why this is a genuine weakening

The previous target was

\[
K_J\ge0
\quad\Longleftrightarrow\quad
\delta(J)=0.
\]

QIDR allows `K_J` to be indefinite at every scale.  It requires only that the **magnitude of the bad spectral direction** be polynomially payable after complete source recombination.

This is exactly the conceptual import from Claude's unconditional two-thirds theorem: the off-line part of a finite compression need not be made positive; one should use its inertia quantitatively and spend only what the final inequality sees.

In the present repo this idea is unusually sharp because the corrected Q4 state is already two-dimensional.  There is only one possible bad eigenvalue once the scalar curvature is positive.

## 6. Mandatory firewall

`R-90301` proves that the normalized Q4 Euler-Blaschke factor is J-unitary on every functional-equation off-line pair.  Therefore QIDR may **not** be justified by a source-blind all-pass iteration or by claiming that the Q4 filter itself shrinks hyperbolic zero blocks.

A valid proof must obtain the defect bound from the complete source-specific Selberg/Jordan/carry ledger.

## 7. Exact status

```text
Claude-style inertia synthesis inequality               PROPOSED COMPLETE EXACT
two-state negative spectral mass formula                PROPOSED COMPLETE EXACT
Wronskian/determinant reduction                         PROPOSED COMPLETE EXACT
all-pass hyperbolic-pair shortcut                       REFUTED EXACTLY
corrected Q4 state dimension                            IMPORTED EXACT / REVIEW
source-complete scalar critical moat                    IMPORTED COFINAL / REVIEW
Q4 inertia-defect estimate                              OPEN / RH-BEARING
QIDR coefficient-one recurrence                         OPEN / RH-BEARING
QIDR -> polynomial energy -> RH                         COMPLETE CONDITIONAL
Riemann Hypothesis                                      UNPROVEN
```

The preferred next calculation is no longer a full matrix PSD certificate.  It is the source-specific scalar

\[
\boxed{(-\det K_J)_+}
\]

or its Wronskian form from `L-90302`, with every Q2/Q4 filter and product-carry collision left intact.