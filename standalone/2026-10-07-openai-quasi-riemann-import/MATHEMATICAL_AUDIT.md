# Selective mathematical audit of OpenAI math family 003

**Upstream revision:** `adc7f1241b42e322a6451854ab7e4b4c146bf78a`, initial public commit, 6 October 2026 at 21:58:50 UTC.
**Audit date:** 7 October 2026.
**Status:** source inspection and exact checks of selected algebraic checkpoints. This document does **not** certify the complete analytic proofs or report an executed Lean build.

## 1. The claims and their precise scope

The principal manuscript is [The Quasi-Riemann Hypothesis: A Zero-Free Half-Plane Re(s)>7/8](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex), dated 30 September 2026. Its Theorem 1.1 (`thm:main`) asserts, unconditionally, that every finite-order Hecke L-function over `Q(sqrt(-3))`, and hence every Dirichlet L-function including the Riemann zeta function, is nonzero in `Re(s)>7/8`. Principal poles at 1 are allowed. The bound is common to the whole family, independently of conductor and height; implied constants in intermediate fixed-character estimates need not be conductor-uniform.

The later [The Quasi-Riemann Hypothesis](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/The-Quasi-Riemann-Hypothesis-October-5-2026/build/paper2.tex), dated 5 October, isolates a simpler proof of `Re(s)>11/12`. Its introduction explicitly presents this as an intermediate result toward the earlier manuscript's stronger 7/8 theorem. The repository README says the 11/12 writeup was human edited for readability. The later date does not indicate a replacement of 7/8 by 11/12.

The companion [Uniform exclusion of Landau–Siegel zeros](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Uniform-exclusion-of-Landau-Siegel-zeros-October-1-2026/build/paper.tex), dated 1 October, gives an independent argument that some absolute `c>0` satisfies `(1-beta) log q >= c` for every real zero in `(0,1)` of every primitive nonprincipal real Dirichlet character of conductor `q>=3`. It does not give an explicit c and does not exclude all real zeros in `(0,1)`.

These are major claimed advances, but none proves RH. For primitive Dirichlet L-functions the 7/8 theorem and functional equation confine nontrivial zeros to `1/8 <= Re(s) <= 7/8`. They leave the entire middle strip, possible boundary zeros, multiplicities, and the critical-line assertion unresolved. They do not assert the same theorem for arbitrary automorphic or arbitrary-number-field L-functions.

## 2. The simpler 11/12 proof: an explicit chain

Write `K=Q(sqrt(-3))`, `O=Z[omega]`, and `N` for ideal norm. Fix a finite-order Hecke character nu and finitely many excluded primes S, containing its conductor and primes above 2 and 3. Original ideal sums use the unique primary generator outside 3; all character zeros on nonunits remain present.

### 2.1 A mean square and sixth-power amplification

For a smooth compactly supported W, set

\[
A_u(D)=\sum_{(n,S)=1}\mu(n)\nu(n)(u/n)_6W(Nn/D).
\]

Proposition 3.1 (`thm:ms`) claims, for every fixed `0<theta<=1/10` and epsilon,

\[
\sum_{0<Nu\le D^{1+\theta}}|A_u(D)|^2
\ll_{\nu,S,W,\theta,\varepsilon}D^{2+\theta+\varepsilon}.
\]

This is an average square-root-cancellation estimate for these specific arithmetic coefficients, not an arbitrary-coefficient sextic large sieve.

For primary prime generators p with `Np~Y`, the row `u=p^6` has `(p^6/n)_6=1_{p not dividing n}`. Hence

\[
A_{p^6}(D)=A_1(D)+O_W(D/Y).
\]

There are asymptotically `Y/log Y` such rows. Taking `Y=H^(1/6)`, `H=D^(1+theta)`, gives

\[
|A_1(D)|^2\ll D^{11/6+5\theta/6+\varepsilon}
                    +D^{5/3-\theta/3},
\qquad
A_1(D)\ll D^{11/12+\varepsilon}.
\]

Theta is selected sufficiently small for each requested epsilon. There is no claim of uniform constants as theta tends to zero.

Mellin integration then produces `W_hat(s)/L_K^S(s,nu)` holomorphically in `Re(s)>11/12`. At a hypothetical zero rho, choosing `W(y)=y^(-rho) phi(y)` with phi nonnegative and nonzero makes `W_hat(rho)>0`, a contradiction. This reduction is explicit in Section 3 and checks out at the level of ordinary Mellin continuation.

### 2.2 Why the field and sextic characters are useful

Poisson summation in u introduces a sextic Gauss sum. The arithmetic identity in Lemma 4.1 (`lem:arithmetic`, `eq:convert2`) is

\[
\mu(n)\gamma_{-1}(n)
=\chi_n(-1)G(n)^{-1}\overline{\alpha(n)}\gamma_2(n),
\qquad \alpha(n)=n/\sqrt{Nn}.
\]

Thus the Möbius coefficient is absorbed into a cubic Gauss-sum coefficient. Patterson's coefficient formula realizes those coefficients in Kubota's cubic theta function. The associated theta sum has indices `nb^3`, with n squarefree and b unrestricted; n and b may share primes.

The angular factor has a specific analytic role. Appendix A.2 obtains it by applying a horizontal derivative to the theta expansion. The derivative kills the constant Fourier modes at the original and transformed cusps. Consequently the associated Mellin transform decays at both ends and is entire, allowing reflection without an unaccounted pole term. It is not enough to cite theta automorphy while omitting this normalization and the constant modes.

In Proposition 6.2 (`lem:reflection`) the theta transformation sends the generic sextic local row exponent `j=1` to `-j-2=3 mod 6`, namely a quadratic character. This allows the quadratic large sieve, whose principal norm is `H+L`, rather than paying the higher-order sieve term `(HL)^(2/3)`.

The difficult analytic conclusion is Proposition 5.2 (`prop:R`): the completed sum T obeys

\[
\sum_{0<Nk\ll\mathcal H}|T(X;k,f)|^2
\ll D^\varepsilon\left(\mathcal H+\frac{\mathcal H^2Nf}{X}\right).
\]

Its proof relies on the explicit cusp coefficients, the transformation for a fixed target ray character, Lemma 6.3's uniformity as the moving row changes, treatment of repeated prime powers, and the quadratic large sieve. A transformation for just one fixed row would not be sufficient for the average.

### 2.3 Removing the artificial cubes without losing cancellation

The completed theta sum is not the original squarefree sum; its other cube terms cannot be discarded from an absolute square. The exact multiplicative completion has the schematic form

\[
T_h(X)=\sum_b\frac{w_h(b)}{Nb}P_h(X/(Nb)^3),
\quad
P_h(X)=\sum_d\frac{\mu(d)w_h(d)}{Nd}T_h(X/(Nd)^3).
\]

Lemma 5.3 (`lem:cube-reduction`) applies the completed bound only to short inverse-cube divisors, up to

\[
H_c^3=\min(X,X^2/\mathcal H^2).
\]

The long divisors produce the same kind of energy at smaller column lengths `L_b=X/(Nb)^3`. Proposition 5.4 (`prop:transfer`) uses two finite Poisson transformations to move these energies into a family with

\[
\mathcal H'\le\frac{\mathcal H L_b}{\Sigma F},\qquad
\frac{\mathcal H'}{\Sigma'}\le\frac{\mathcal H}{\Sigma},\qquad
\Sigma'=X'F'\le L_b,\qquad \Sigma=XF.
\]

The crucial exact cancellation occurs in Lemma 7.3 (`lem:second-transfer`). Before taking absolute values, all preimages producing a fixed transformed row and common factor are grouped. At each prime dividing the transformed auxiliary factor f', the three allocation possibilities contribute

\[
(1+\mathbf1_{p\mid k'})-\mathbf1_{p\mid k'}
                       -\mathbf1_{p\nmid k'}
=\mathbf1_{p\mid k'}.
\]

The aggregate coefficient therefore forces `f'|k'`. The smooth kernels and phases have to agree on the preimages for this cancellation to be valid. The text explicitly verifies that the kernel depends only on the regrouped labels; this is the part to preserve in any adaptation.

For each remaining long divisor, the cutoff and transfer scales imply

\[
\mathcal H'<\mathcal H(\mathcal H/\Sigma)^2.
\]

With initial gap `H/Sigma <= D^(-kappa)`, row sizes contract by `D^(-2kappa)` while the ratio condition is preserved. Proposition 5.1 (`prop:canonical`) closes a finite induction; the derivative-order recursion and epsilon allocation are stated explicitly. The initial Poisson reduction supplies the gap because the original mean square has row length `D^(1+theta)`.

### 2.4 Transfer back to rational Dirichlet functions

For a Dirichlet character chi, quadratic base change factors

\[
L_K(s,\chi\circ N)=L(s,\chi)L(s,\chi\chi_{-3})
\]

up to finitely many Euler factors nonzero in `Re(s)>0`. The principal pole case at 1 is handled separately using classical nonvanishing there. No RH or GRH is used in this deduction.

## 3. What the stronger 7/8 manuscript adds

The September paper is not merely the October proof with optimized constants. It has a two-stage, family-wide continuation architecture. Its first stage establishes 11/12; its second uses that ceiling to establish 7/8.

### 3.1 The continuation criterion

Let beta-star be the supremum of real parts of zeros over all primitive finite-order Hecke characters of K, including 1/2 in the supremum. Proposition 2.1 (`lem:continuation-criterion`) is an ordinary Mellin/Fourier continuation argument. It uses a physical sum J and a signal

\[
f_\eta(Z)=\frac1{2\pi i}\int_{(2)}
 Z^{C(s)}e^{(s-5/6)^2}\frac{H_\eta(s)}{L_K^S(s,\eta)}\,ds,
\quad |H_\eta-1|\le\tfrac12.
\]

If `beta-star > sigma0`, low and high estimates with a *common positive exponent margin* continue every target reciprocal to the left of beta-star. This contradicts the definition of the supremum. The supremum need not be attained. Constants and thresholds may depend on the character, but the continuation distance may not.

The physical sum and signal must be independent of the auxiliary height cutoff. The manuscript explicitly enforces this in the final order of choices. The high estimate is measured relative to `C(beta-star)`, not `C(sigma0)`.

### 3.2 Compensation, two witnesses, and two distinct moment engines

The stronger physical sum uses prime compensation and asymmetric scales

\[
l_x=17/48,\quad l_y=23/48,\quad \ell=1/6,\quad h=13/16,
\quad C_{II}(s)=s-11/16.
\]

Proposition 15.2 (`prop:probe-gram`) proves a structured additive Gram bound. Its exceptional frequencies have sixth-power shape; it retains collision zeros before using the full common-factor Möbius identity. Proposition 15.3 (`prop:probe-low`) combines that estimate with reflected row energy to give the low exponent `3/16=C_II(7/8)`.

The zero detector supplies both an inverse polynomial M (Möbius coefficients) and a plain polynomial S (no Möbius coefficients) for the *same row character and the same witness height*. Their large values constrain the number of bad rows.

Lemma 17.1 (`lem:marked`) bounds an inverse polynomial multiplied by independently weighted prime sums. With row exponent m, inverse length r and total prime length z, its conditions include strict margins

\[
r+2z\le m-c_1,\qquad 2r+8z\le3m-c_2.
\]

Lemma 17.2 (`lem:canonical-moment`) is its two-Poisson recursive engine. It explicitly forbids arbitrary residual column weights or row-dependent masks. Moving conductor radicals are charged to the size budget rather than silently frozen into constants.

Lemma 18.1 (`lem:plain`) controls the squared product of two plain polynomials and short prime factors. Without prime slots it has no length restriction after ordinary Hecke reflection. With positive total prime length z, it needs

\[
n_1+n_2+6\kappa z\le M.
\]

For `kappa<1` it assumes `beta-star <= (1+kappa)/2`. The main proof sets `kappa=2 beta-star-1`, so that hypothesis holds by definition and the 11/12 first stage gives `kappa<=5/6`. This is a legitimate bootstrap hypothesis within the argument, not RH and not an independently unconditional improved moment at a freely selected kappa.

The plain induction treats finite-family inducing characters separately. Its main-term cancellation is valid for centered differences with the same common character, masks, profiles and product of scales. It is not cancellation for every uncentered row in the finite exceptional family.

Proposition 19.2 (`prop:detector-counts`) balances the two witness counts. Available prime length at the decisive endpoint is `ell/h=8/39`, while the largest needed inverse capacity is `7/37`, with positive gap `23/1443`. Equality or vanishing-capacity cases use unmarked amplification, avoiding application of a strict-margin theorem with a shrinking margin.

### 3.3 The endpoint certificate and what it does certify

Put `Delta=beta-star-7/8`, so `0<Delta<=1/24`, `delta=2a-1`, `0<=delta<=5/6`, and `x=q/delta` in `[0,1/2]`. Set

\[
D_x=3-17x/9,\qquad P_x=(2-8x/9)(1-x),
\quad \mathcal J=(5/6-\delta)D_x+\delta P_x,
\]

\[
t=1+\frac{\delta P_x}{2\mathcal J},\qquad
R_*=1-\delta+(5/6-\delta)(t-1).
\]

The ideal high exponent at d=h is

\[
E_*=-1/48+2\delta/3+x\delta/6-(13/16)(1-R_*).
\]

Lemma 20.2 (`lem:balanced-endpoint`) gives an explicit positive polynomial certificate proving

\[
-E_*\ge49/440640>1/10000.
\]

Restoring the dynamic plain capacity raises the row exponent by at most `Delta/4` plus arbitrary small losses. Thus the required comparison is

\[
E_{\rm actual}(h)-\Delta
\le-49/440640-(51/64)\Delta+\varepsilon_{\rm total}.
\]

The subtraction of Delta is essential. The proof does not need to show that every actual high exponent is negative relative to the 7/8 low scale. Proposition 20.3 (`prop:parameter-order`) assigns all real losses and prime slots before choosing the target-dependent height and tail orders, retaining positive common margins.

The endpoint algebra is exactly checked by the accompanying script. That verification establishes the arithmetic implication from the supplied row-count formulas and scales. It does not establish those row counts or the analytic estimates that supply them.

## 4. The independent Landau–Siegel determinant proof

This manuscript was read through its full logical argument. Its strategy is quite different from theta reflection.

1. Lemma 2 shows that a real zero with `(1-beta) log q` small forces primes with chi(p)=1 to have small weighted mass. Consequently primes with chi(p)=-1 carry almost all of `sum(log p)/p` up to a suitable scale U.
2. Lemma 3 proves a coefficient-uniform anisotropic interpolation theorem for the projection of an integer box in four dimensions to three dimensions, assuming rational independence of the four coordinates of the kernel vector. Its proof uses a nearest lattice point to a convex polytope and interpolation on a supporting face.
3. Apply it to the three coordinates `(theta_n, sigma(theta_n), sigma tau(theta_n))` in the biquadratic field `Q(sqrt(d),sqrt(2))`. A greedy weighted order selects `N^4` independent monomial rows at degree scale `U=N^(4/3)`. Lemma 6 concentrates almost all total degree in the first coordinate.
4. At a prime with chi(p)=-1, Frobenius sends `theta^p` to one of the other two conjugates modulo p. Replacing powers by `(theta^p-g_p(theta))^k` gives a lower-triangular row operation, preserves the determinant, and extracts `p^floor(alpha_1/p)` from each row (Lemma 7).
5. Divisibility yields a leading lower bound `S_1 log U`; the Archimedean estimate has `(S_1+S_2) log N`, with `log N=(3/4)log U`. A large fixed weight makes `S_2/S_1` small. Taking N as a large fixed power of q and then passing along a hypothetical sequence of exceptional zeros yields `1<=7/8`, a contradiction.

No defect was identified in this inspection. That statement is weaker than an independent formal verification. The selected rows are independent over the field; the row-operation matrix need not be integral, since integrality of the *replacement entries* supplies the divisibility. The argument explicitly addresses this potential confusion.

## 5. Formalization evidence and boundaries

[lean/docs/003.md](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/docs/003.md) describes formalized 7/8 statements for zeta, all positive-modulus Dirichlet characters, and finite-order Hecke characters over K, plus the uniform real-zero gap. It says the later arithmetic applications are outside the formalization's scope.

The actual zeta entry is `lean/OAI/NumberTheory/DirichletL/Nonvanishing.lean`, with theorem `OAI.riemannZeta_ne_zero_of_seven_eighths_lt_re`, calling `SevenEighths.ProbeFinalAssemblyUnconditional.zeta_nonzero`. The analogous Dirichlet statement uses Mathlib's `DirichletCharacter.LFunction` and explicitly excludes the principal pole. The comparator JSON selects this solution module and permits only `propext`, `Quot.sound`, and `Classical.choice`.

The `sorry` in `ComparatorChallenges/QuasiRiemannHypothesis.lean` is a challenge stub by design, not itself evidence of a gap in the solution. Conversely, a correctly named solution theorem and restrictive comparator configuration do not substitute for actually building its complete dependency closure and executing the comparator. No such execution is claimed in this audit.

## 6. What was checked and what remains to check

The script `verify_upstream_checkpoints.py` uses only the Python standard library and exact integer/rational arithmetic. Its accompanying result file records **27 selected checks passing**, including:

- the sixth-power extraction exponents;
- the primewise common-support allocation identity and the contraction-scale algebra;
- the asymmetric low and Mellin exponents;
- the balanced witness crossing and the full positive polynomial endpoint certificate;
- the fixed endpoint, capacity and prime-supply margins;
- exact Gauss-conversion checks at both primary primes above each of 7, 13, 19, 31, 37, 43 and 61. These 14 cases use polynomial reduction in the appropriate cyclotomic field, with no floating-point tolerance.

The last checks verify finite examples of the phase convention and normalization, not the universal Gauss identity. The symbolic endpoint checks verify an identity and its explicit domain argument, not the analytic hypotheses feeding it.

The load-bearing points deserving a full independent review are:

| Component | Evidence from this pass | Remaining obligation |
| --- | --- | --- |
| Mellin contradiction and family supremum | Logical reductions read; no defect identified | Check all growth/uniformity interfaces in full application |
| Cubic Gauss normalization | Exact checks for 14 split-prime instances | Universal prime-power/composite proof and fixed ray phases |
| Completed theta reflection | Statement, support and transformation mechanism inspected | Full cusp calculation, local `j=0,4` cases, repeated powers, row-uniform coefficient families |
| Two-Poisson transfer | Exact preimage cancellation and scale algebra inspected | All masks, phases, multiplicities and common kernels in the full transformations |
| Marked inverse moment | Hypotheses and induction interfaces inspected | Entire recursive proof including moving punctures and seminorm propagation |
| Plain fourth moment | Hypotheses, bootstrap usage and centered-family role inspected | Entire finite induction; preservation of common character/mask/scale through each transform |
| 7/8 exponent closure | Complete displayed endpoint identity checked exactly | Analytic estimates and allowed coefficient classes underlying the closure |
| Lean result | Entry theorem and comparator configuration inspected | Execute full build/comparator and inspect any reported axioms or definition mismatches |

No concrete contradiction or counterexample was found in the portions audited. The source is unusually explicit about precisely the failure modes that matter here: lost character zeros, arbitrary coefficient extension, moving data treated as fixed, cancellation between unmatched kernels, and exponent margins chosen in the wrong order. Those protections should be carried intact into downstream use.

## 7. Consequences for further research, with the inference separated

**A strong reusable mechanism:** the signed preimage sum in Lemma 7.3 creates an actual divisibility restriction after regrouping, which then contracts the parameter range. This is much more informative for a covariance program than a generic absolute-value bound. A concrete next project is to determine whether the existing covariance coefficients can be represented by this arithmetic family, or by a finite controlled enlargement of it. Such a representation needs proof; similarities of notation or of quadratic-form shape are insufficient.

**A second mechanism:** preserve full squarefree-times-cube support until theta reflection is available, then undo completion with an exact inverse and a contracting recursion. Replacing the completed sum by its squarefree sub-sum before the transformation would invalidate the argument.

**A route to a sharper boundary:** expose the marked inverse moment capacity, the plain fourth-moment capacity, and the low Gram exponent as explicit inputs of a parameterized endpoint theorem. Search for improvements only after the admissible coefficient classes and all size inequalities have been retained. An optimized endpoint certificate can improve constants or a boundary if the input inequalities have slack, but it cannot supply a missing analytic bound.

**An independent structural direction:** the Landau–Siegel manuscript's anisotropic interpolation theorem and weighted determinant are relevant to determinant-based arithmetic obstruction programs. Its exploitation of a Frobenius action at many primes is essential. Applying it to zeta's general complex zeros would require a new bridge from those zeros to similarly strong local algebraic data; the present paper does not provide that bridge.

**What cannot be inferred:** a 7/8 zero-free half-plane cannot simply be combined with a fixed-detector positivity statement, a finite numerical experiment, or an unclosed covariance estimate to obtain RH. The remaining estimate must exclude every off-line zero in the middle strip. A defensible combined program should state that missing implication precisely and verify whether the imported moment machinery actually meets its quantifiers and coefficient restrictions.
