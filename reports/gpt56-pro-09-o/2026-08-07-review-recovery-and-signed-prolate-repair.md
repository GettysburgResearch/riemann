# Recovery of the independent prolate review and signed-sector repair

Agent: `gpt56-pro-09-o`  
Date: 2026-08-07  
PR: #202  
Classification: review recovery, exact refutation, and proposed repair; **RH is not proved**

## 1. Provenance recovered

The global prolate proposal was reported at a commit

```text
83dac9b1ff95f64b4b48f788c017511d3d7f2aee
```

that is not resolvable in the repository. PR #202 was frozen for this response at

```text
585cda919808429a759cf0bf7ab054af40f9a6d2.
```

The three artifacts described by the user and reviewer are present there with
exactly the reviewer-supplied blob identities:

```text
claims/theorems/T-19807-non-effective-cofinal-prolate-resolution.md
  863bd147659dc0fd46ac2f90945b5ff8ea37bc0b

claims/lemmas/L-19821-critical-strip-growth-closes-support-average.md
  1953fcd0e8ca83456b9a878aefaf43adbce825d6

reports/gpt56-pro-09-n/2026-08-07-global-prolate-resolution-attack.md
  d5804976635f8ddb1b95d45083b16e7b9bd0e7f7
```

I searched the accessible repository branches, commits, pull requests, formal PR
reviews, PR comments, and recent issues for a separately pushed review artifact.
No separate accessible GitHub ref containing that review was found. The detailed
review supplied in the conversation is therefore treated as the independent
review record, and this report preserves its mathematical conclusions durably.

## 2. Review verdict accepted

Overall classification:

```text
GAPS/BLOCKED
```

The review correctly identifies two rejected load-bearing claims and four global
analytic gaps.

| Component | Disposition after review |
|---|---|
| `L-19821` quarter-power support argument | **REJECTED AS WRITTEN** |
| complete finite-space `d_8` gap | **REJECTED AS WRITTEN** |
| `T-19807` conditional finite-to-RH composition | **VERIFIED WITH FIXES** |
| Mellin factorization and weak radical | **VERIFIED WITH FIXES** |
| exact radical-tail zero-side identity | **VERIFIED WITH FIXES** |
| qualitative generic-support surjectivity | **VERIFIED WITH FIXES** |
| quantitative complete source frame | **GAP/BLOCKED** |
| exact leakage normalization | **VERIFIED** |
| real-axis growing PSWF/Hermite window | **VERIFIED WITH FIXES** |
| shrinking-complex-strip branch theorem | **GAP/BLOCKED** |
| exact first-alias Gram | **VERIFIED** |
| complete growing alias Gram | **GAP/BLOCKED** |
| abstract Selberg/Stieltjes estimate | **VERIFIED WITH FIXES** |
| actual growing-packet local Weyl theorem | **GAP/BLOCKED** |
| abstract support large sieve `L-16226` | **VERIFIED WITH FIXES** |
| `+1`-sector `d_4/d_8` hierarchy | **VERIFIED WITH FIXES** |
| complete signed-sector hierarchy | original `d_8` claim rejected; repaired `d_6` theorem proposed |
| Rayleigh-floor and CCM/Hurwitz endpoint | **VERIFIED WITH FIXES / VERIFIED** |
| RH proof | **GAPS/BLOCKED** |

No passing earlier theorem is demoted merely because the proposed full
composition failed. Every repair in this response is separately marked
`PROPOSED` pending independent review.

## 3. First decisive correction: the translation factor cancels

For

\[
 \widehat T_{j,R}(s)
 =\sqrt{d_j/R}\,e^{-isx_R}\Phi_{j,R}(s/R),
\]

the polarized zero-side kernel is

\[
 \overline{\widehat T_{j,R}(\overline s)}
 \widehat T_{k,R}(s)
 ={\sqrt{d_jd_k}\over R}
 \overline{\Phi_{j,R}(\overline s/R)}
 \Phi_{k,R}(s/R).
\]

The factors `exp(+isx_R)` and `exp(-isx_R)` cancel exactly. The `R^(1/4)`
modulus estimate used by `L-19821` therefore measures a factor absent from the
actual quadratic form.

The second defect is independent. The support large sieve requires

\[
 \|A(R)\|+T\|A'(R)\|\le B_T,
\]

whereas `L-19821` controlled only `||A||+||A'||`. The omitted factor `T` is
required because the derivative separation of phases `R S(gamma/R)` is of size
`|gamma-gamma'|/T`.

These defects are now recorded as `R-19805`; the original file is not rewritten
or retrospectively verified.

## 4. Correct support-average theorem

`L-19822` supplies the exact viable interface. One must first construct a
branchwise holomorphic expansion

\[
 \Phi_R(z)
 =\sum_{\nu=1}^{B}a_{\nu,R}(z)e^{iRS_\nu(z)}+e_R(z)
\]

in the strip `|Im z|<=1/(2R)` with

\[
 \|a\|+\|\partial_za\|+R\|\partial_Ra\|
 \le(\log R)^C.
\]

For `z=x+i delta/R`,

\[
 e^{iRS_\nu(z)}
 =e^{iRS_\nu(x)}e^{-\delta S_\nu'(x)}(1+O(R^{-1})).
\]

Thus horizontal displacement modifies branch amplitudes by a bounded factor.
After the real support phase is extracted, the true large-sieve condition

\[
 \|A_\rho(R)\|+R\|A_\rho'(R)\|
 \le(\log R)^C
\]

holds. The abstract large sieve then gives mean square `polylog(R)/R`, stronger
than the rejected quarter-power conclusion.

This repair remains conditional on:

1. a shrinking-strip holomorphic Dunster expansion;
2. a uniform Airy fold theorem;
3. collective endpoint-channel summation;
4. a uniformly absolutely summable post-endpoint alias remainder;
5. both Fourier-sign sectors.

## 5. Second decisive correction: the `-1` sector lowers the complete scale

The original hierarchy used only modes

```text
0,4,8,12,...
```

from the `+1` Fourier sector. The finite CCM space also contains

```text
2,6,10,...
```

from the `-1` sector.

The exact point-cancelled pairs

\[
 p_+=e_0/q_0-e_4/q_4,
 \qquad
 p_-=e_2/q_2-e_6/q_6
\]

have integral residuals of scales `d_4` and `-d_6`. Their exact signed repair has
Rayleigh scale `d_4`. A second exact constrained vector, dominated by `p_-`, has
Rayleigh scale `d_6`. Hence a complete complement lower bound at scale `d_8` is
impossible because

\[
 d_6/d_8\to0.
\]

`R-19805` records the explicit obstruction.

The stronger new result `L-19823`, with the exact low-kernel calculation isolated
in `L-19824`, proves in the pure prolate model that the first two constrained
eigenvalues satisfy

\[
 \theta_1=O(d_4),
 \qquad
 \theta_2=\Theta(d_6).
\]

The proof uses:

- an explicit exact basis of the low four-mode signed kernel;
- fixed-mode Fuchs ratios;
- the uniform point-value window;
- a graph representation of the complete source constraints;
- a tail susceptibility

  \[
  d_6\sum_{n\ge8}|q_n|^2/\delta_n\to0.
  \]

This is a genuine repair of the **pure prolate** hierarchy. It does not prove the
same lower bound for the arithmetic Poisson tail or localized Weil form.

## 6. Corrected conditional composition

`T-19808` replaces `T-19807` as the current proposed composition theorem.

Its load-bearing hypotheses are:

1. a quantitative exact source frame containing both Fourier-sign sectors, with
   polylogarithmic right-inverse and Hardy-metric constants on a positive-measure
   support set;
2. an arithmetic omitted-tail hierarchy

   \[
   \mu_D\le C_4d_4,
   \qquad
   D_R-\mu_DH_R\succeq c_6d_6H_R
   \]

   on the complete target complement;
3. the correctly normalized local-Weyl estimate

   \[
   \eta_R
   ={\|D_R^{-1/2}[A_R-(\log R)D_R]D_R^{-1/2}\|
     \over\log R}
   \to0;
   \]
4. the moving-Hardy target projection limit.

Then

\[
 A_R\succeq0,
\]

\[
 \mu_A
 \le(1+\eta_R)(\log R)C_4d_4,
\]

and the complete target-complement floor is

\[
 g_R\ge(\log R)
 \left[(1-\eta_R)c_6d_6-2\eta_RC_4d_4\right].
\]

Therefore

\[
 {\mu_A-L_R\over g_R}
 =O(d_4/d_6)+o(1)\to0.
\]

Polylogarithmic frame/Hardy conditioning is absorbed by the fixed-mode power
saving. The reviewed Rayleigh-floor theorem and CCM/Hurwitz endpoint then imply
RH.

This is a correct conditional theorem, not a proof that its hypotheses hold.

## 7. Exact remaining frontier

The corrected route now requires exactly four global results.

### A. Quantitative signed source frame

Construct exact-radical packets in both Fourier-sign sectors and prove, on a
positive-measure subset of every large support block,

\[
 \sigma_{\min}
 \left(P_{N_\lambda}\Sigma_\mu E
       \bigm|_{\mathcal U_{\lambda,+}\oplus
                    \mathcal U_{\lambda,-}}
 \right)
 \ge(\log\lambda)^{-C}.
\]

Qualitative finite surjectivity and avoidance of exact zeta-cycle lengths do not
imply this.

### B. Signed arithmetic-tail hierarchy

In one common exact metric prove

\[
 D_{R,+}-\mu_DH_{R,+}\succeq c_8d_8H_{R,+},
\]

\[
 D_{R,-}\succeq c_6d_6H_{R,-},
\]

and the constrained finite Schur adapter giving the complete `d_6` floor.
`L-19823` proves only the corresponding diagonal prolate model.

### C. Complete holomorphic branch and alias theorem

Prove the WKB/Airy expansion with

\[
 \|a\|+\|\partial_za\|+R\|\partial_Ra\|
 \le(\log R)^C
\]

through the shrinking strip, and treat all endpoint and infinitely many alias
channels collectively before using absolute summation.

### D. Full relative local-Weyl theorem

At one support in every sufficiently large dyadic block prove

\[
 {\|D_R^{-1/2}[A_R-(\log R)D_R]D_R^{-1/2}\|
  \over\log R}
 \longrightarrow0.
\]

This must combine the line-centered Selberg estimate, corrected support
averaging, quantitative source conditioning, and the complete alias ledger.

## 8. Current status

```text
original L-19821:              REJECTED AS WRITTEN
original complete d8 gap:      REJECTED AS WRITTEN
pure prolate signed repair:     PROPOSED, d4/d6 proved
corrected composition T-19808:  PROPOSED CONDITIONAL THEOREM
quantitative global inputs:     GAPS/BLOCKED
accepted proof of RH:           NO
serious resolution path:        YES, conditional on A-D
```

The review improved the route substantially: it removed a false mechanism,
identified the missing Fourier sector, and reduced the corrected full-space
ratio to `d_4/d_6`. The remaining obstacles are now stated without hiding them
inside qualitative surjectivity, imported checker constants, or an incorrect
support derivative estimate.
