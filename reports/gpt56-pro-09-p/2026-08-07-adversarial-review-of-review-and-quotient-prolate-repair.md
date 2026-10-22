# Adversarial review of the independent prolate review and quotient-energy repair

Agent: `gpt56-pro-09-p`  
Date: 2026-08-07  
PR: #202  
Status: **the independent rejection of the reviewed proposal is upheld; a distinct corrected composition is proposed, not accepted; RH is not claimed proved**

## 1. Frozen object and verdict

The unavailable supplied commit remains unresolved. The reviewed artifacts are
frozen by the exact blob identities already recovered at PR #202 head
`585cda919808429a759cf0bf7ab054af40f9a6d2`:

```text
T-19807  863bd147659dc0fd46ac2f90945b5ff8ea37bc0b
L-19821  1953fcd0e8ca83456b9a878aefaf43adbce825d6
report    d5804976635f8ddb1b95d45083b16e7b9bd0e7f7
```

After reconstructing the algebra independently and attacking the reviewer's
own proposed repairs, the verdict on those blobs remains

```text
GAPS/BLOCKED.
```

More strongly:

- `L-19821` is false as written;
- the complete `d_8` claim is false as written;
- the original source-frame congruence is not proved;
- the complete alias and relative local-Weyl theorems are not present in the
  reviewed proposal.

No new repair retroactively verifies those claims.

## 2. Findings on the reviewer, component by component

### 2.1 Translation cancellation — reviewer correct

For

\[
 \widehat T_{j,R}(s)
 =c_{j,R}e^{-isx_R}\Phi_{j,R}(s/R),
\]

the polarized zero-side product is

\[
 \overline{\widehat T_{j,R}(\overline s)}
 \widehat T_{k,R}(s)
 =\overline{c_{j,R}}c_{k,R}
 \overline{\Phi_{j,R}(\overline s/R)}
 \Phi_{k,R}(s/R).
\]

The support translations cancel exactly. The factor `R^(1/4)` in `L-19821`
never enters the quadratic kernel. The rejection is decisive.

### 2.2 Large-sieve derivative — reviewer correct

For phase differences of ordinates separated by `m` unit bins, the support
phase derivative is `asymp m/R`. One integration by parts requires

\[
 \|A(R)\|+R\|A'(R)\|\le B_R,
\]

not `||A||+||A'||<=B_R`. Omitting the factor `R` loses the full oscillatory
reserve. This is independent of the translation cancellation.

### 2.3 Complete `d_8` gap — reviewer correct

The exact two-constraint low vectors in the `+1` and `-1` Fourier sectors give

\[
 \theta_1=O(d_4),
 \qquad
 \theta_2=O(d_6).
\]

Since `d_6/d_8->0`, a complete `d_8` lower gap is impossible. The new pure
prolate theorem `L-19823/L-19824` supplies the matching lower bound

\[
 \theta_2=\Theta(d_6)
\]

under its declared point-value and fixed-mode hypotheses. Thus the reviewer's
suggested `d_6` repair is mathematically the correct low-packet scale.

### 2.4 Qualitative source surjectivity — reviewer correct

Density followed by finite projection proves only finite surjectivity. It does
not produce a controlled right inverse and exact determinant avoidance does not
bound the determinant away from zero.

### 2.5 Claimed need for a complete polylogarithmic `sigma_min` — reviewer overstrong

The review proposed as the exact missing theorem

\[
 \sigma_{\min}(S_R)\ge(\log R)^{-C}.
\]

That is sufficient for the original congruence argument but is not logically
necessary. The induced finite-space tail form is the quotient energy

\[
 \mathfrak D_R(v)=\min_{S_Ru=v}D_R(u).
\]

A small singular value of `S_R` makes the corresponding normalized output
**more expensive** in quotient energy. The exact min--max theorem `L-19846`
shows that the target/gap transfer needs only:

1. qualitative surjectivity;
2. an upper bound `S_R^*H_RS_R<=K_RG_R`;
3. a lower bound on the image of the single target line;
4. at most one source-tail eigenvalue below the `d_6` scale.

No complete inverse enters the bound.

The natural low-prolate sampling map is in fact expected to be
superalgebraically ill-conditioned: its Hermite Mellin limit is a
gamma-weighted polynomial space of degree `Theta((log R)^2)` sampled only on an
ordinate window of width `Theta(log R)`. `R-19843` constructs the corresponding
small sampling direction, subject to the stated all-orders prolate-to-Hermite
Mellin transfer. This is compatible with exact generic rank and with the
quotient-energy theorem.

The explicit logarithmic interpolation frame `L-19840` gives a separate
quasipolynomial inverse bound

\[
 \|S_R^{-1}\|\le\exp\{C(\log\log R)^2\}=R^{o(1)}
\]

on a positive-measure set. It also shows why a fixed polylogarithmic multiplier
floor would conceal a uniform zero-multiplicity theorem.

### 2.6 Branchwise horizontal-displacement repair — direction correct, not a proof

The reviewer correctly replaced translation growth by analytic continuation of
the radial action. The formula

\[
 RS(x+i\delta/R)=RS(x)+i\delta S'(x)+O(R^{-1})
\]

turns horizontal displacement into a bounded branch amplitude.

An adversarial check found an additional trap: for
`n=O((log R)^2)` the radial action cannot be replaced by one
mode-independent action. Although the mode parameter is `O(n/R)`, multiplying
by `R` creates an `O(n)` phase shift. The first repair draft `L-19842` made this
mistake and is retracted by `R-19842`. Its successor `L-19844` retains the exact
mode-dependent action through WKB, the moving Airy fold, support derivatives,
and all aliases.

### 2.7 Endpoint and alias criticism — reviewer correct

For a nonzero endpoint value, the leading alias is `1/k`; the raw norm sum need
not converge. The correct order is:

1. extract endpoint jets;
2. sum the `1/k` channel exactly as
   `-log(1-exp(i theta))`;
3. retain positive rest/rest self-energy;
4. prove only the first/rest Hermitian cross is small;
5. sum the post-jet remainder absolutely.

`L-19841`, `L-19844`, `L-19845`, and `L-19850` implement this ledger at theorem
level. Their profile-specific estimates remain proposed pending independent
review.

### 2.8 Relative local-Weyl normalization — reviewer correct

The correct error is

\[
 \eta_R=
 \frac{
 \|D_R^{-1/2}(A_R-(\log R)D_R)D_R^{-1/2}\|
 }{\log R}\to0.
\]

The unscaled norm need not tend to zero. `L-19843` uses the complete profile in
the smooth density term, so `(log R)D_R` cancels for neutral and oscillatory
components alike, and treats only the bounded density correction and Stieltjes
fluctuation as error.

### 2.9 Checkers — reviewer correct

The finite checkers replay algebra and imported constants. They do not prove
complex-strip WKB, Airy uniformity, endpoint operator bounds, or an all-scale
local-Weyl theorem. The new `X-19840` checker is likewise labelled synthetic:
it tests quotient-energy and exact algebra only.

### 2.10 Rayleigh/CCM/Hurwitz endpoint — reviewer correct

Once a genuine complete finite target/gap theorem and moving-Hardy target
convergence are available, the finite real-zero theorem and Hurwitz supply the
last logical step. The obstruction is before that endpoint.

## 3. Corrected four-interface programme

The user's four requested interfaces have the following corrected status.

### Interface 1 — source frame

The exact requested complete bound

\[
 \sigma_{\min}\ge(\log R)^{-C}
\]

is neither established nor required, and for the natural low-prolate packet it
is incompatible with the expected growing sampling geometry. It is replaced
by:

- `L-19847`: generic exact rank, a polylogarithmic analysis bound, and fixed
  target nondegeneracy;
- `L-19846`: quotient-energy min--max, eliminating the complete inverse;
- `L-19840`: an independent explicit quasipolynomial interpolation frame.

### Interface 2 — signed arithmetic-tail hierarchy

`L-19841` proves the exact transfer once the first/rest cross and complete
synthesis bounds hold:

\[
 D_{full}=D_1^{1/2}(I+C+P)D_1^{1/2},
 \qquad P\succeq0,
 \qquad \|C\|=o(1).
\]

Together with `L-19823/L-19824`,

\[
 \theta_1\le(\log R)^CO(d_4),
 \qquad
 \theta_2\ge(1-o(1))c_6d_6.
\]

### Interface 3 — holomorphic WKB/Airy/alias

`L-19844` states and derives the corrected mode-dependent action expansion,
including:

- the shrinking strip `|Im z|<=1/(2R)`;
- one scaled support derivative after phase extraction;
- the moving `R^(-2/3)` Airy fold;
- first-versus-later phase separation;
- collective endpoint summation;
- all `k>=2` aliases;
- a polylogarithmic complete synthesis bound on the support set of `L-19845`.

The exact equation-level substitutions remain the principal independent review
target.

### Interface 4 — relative operator local Weyl

`L-19843/L-19850` combine:

- the exact full smooth-density identity;
- phase-neutral Stieltjes integration by parts;
- the corrected Hilbert-valued support large sieve for branch crosses;
- exact same-branch cancellation for hypothetical horizontal displacement;
- collective endpoint density bounds;
- infinite aliases.

They conclude, on a positive-measure set in each large block,

\[
 \frac{
 \|D_R^{-1/2}(A_R-(\log R)D_R)D_R^{-1/2}\|
 }{\log R}\to0.
\]

## 4. New full composition

`T-19810` is the corrected composition:

```text
complete signed low-prolate source packet
-> generic rank, upper map bound, target nondegeneracy
-> complete d4/d6 source-tail hierarchy
-> quotient-energy target/gap transfer
-> relative local-Weyl congruence
-> exact Hermite target maps to xi (`L-19849`)
-> moving-Hardy ground-state convergence
-> CCM real-zero theorem + Hurwitz
-> RH.
```

The crucial congruence estimate is invariant under simultaneous change of
coordinates. Therefore the arbitrarily bad complete condition number does not
amplify the relative Loewner error.

This is a new proposed proof architecture. It is not an accepted RH proof.

## 5. Exact independent review frontier

The next reviewer should attack these points first:

1. **Pure signed low kernel:** the lower `d_6` bound in
   `L-19823/L-19824`, especially the tail-susceptibility estimate.
2. **Mode-dependent normal form:** the coefficient and scaled-variation bounds
   used in `L-19844`, including the exact moving turning point.
3. **First/rest cross:** whether every endpoint/reflected channel really enters
   the collective ledger and whether any constant or stationary endpoint cross
   survives.
4. **Generic source rank:** the degree-echelon generalized alternant in
   `L-19847` after the exact two constraints and signed coordinate split.
5. **Growing analysis bound:** the Meixner--Pollaczek/gamma cancellation of
   `L-19848` and its growing prolate transfer.
6. **Target identity:** convention matching in the exact formula
   `M(Ep_+)=constant*xi` in `L-19849`.
7. **Whitened local Weyl:** the phase-difference lower bound, amplitude
   variation, and endpoint relative-density estimate in `L-19843/L-19850`.
8. **CCM identification:** that the bijective map in `L-19847` is the exact
   finite projection entering the finite real-zero theorem, not merely an
   abstract isomorphic copy.

A failure at any one of these points leaves RH open.

## 6. Durable status

```text
reviewed T-19807 proposal             GAPS/BLOCKED
L-19821                               REJECTED
complete d8 hierarchy                 REJECTED
reviewer's d6 diagnosis               UPHELD
reviewer's complete sigma_min demand  OVERSTRONG / REPLACED
T-19810 quotient composition          PROPOSED PENDING REVIEW
accepted proof of RH                  NO
```
