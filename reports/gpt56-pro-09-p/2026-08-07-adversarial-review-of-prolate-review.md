# Adversarial review of the independent prolate review

Agent: `gpt56-pro-09-p`  
Date: 2026-08-07  
PR: #202  
Frozen launch head: `01798daa9fb766f80658a85421d700e7b1e521aa`  
Classification: **REVIEW VERIFIED WITH MATERIAL FRONTIER CORRECTIONS; RH NOT PROVED**

## 1. Scope

This report does not merely accept the supplied independent review. It
reconstructs every decisive objection against the exact repository formulas,
then attacks the review itself for unnecessary assumptions, hidden norm choices,
and claims of logical independence among the remaining gates.

The reviewed proposal consists of:

```text
T-19807 blob  863bd147659dc0fd46ac2f90945b5ff8ea37bc0b
L-19821 blob  1953fcd0e8ca83456b9a878aefaf43adbce825d6
report blob   d5804976635f8ddb1b95d45083b16e7b9bd0e7f7
```

The previous response accepted the review and published `R-19805`, `L-19822`,
`L-19823`, `L-19824`, and `T-19808`. The present pass adversarially checks both
the review and those repairs.

## 2. Findings that survive adversarial review

### 2.1 The support translation cancels exactly

For

\[
 \widehat T_{j,R}(s)
 =\sqrt{d_j(R)/R}\,e^{-isx_R}\Phi_{j,R}(s/R),
\]

the polarized zero-side entry is

\[
 \overline{\widehat T_{j,R}(\bar s)}\widehat T_{k,R}(s).
\]

Since

\[
 \overline{e^{-i\bar s x_R}}e^{-isx_R}
 =e^{isx_R}e^{-isx_R}=1,
\]

the proposed `R^(1/4)` translation cost is absent from the exact quadratic
kernel. This is not a matter of convention or a harmless overestimate. The
mechanism asserted by `L-19821` is not present in the object being estimated.

**Verdict on the reviewer:** correct.

### 2.2 The factor `T` in the large-sieve derivative hypothesis is essential

`L-16226` assumes

\[
 \|A_\gamma(R)\|+T\|\partial_RA_\gamma(R)\|\le B_T.
\]

For the phase `R S(gamma/R)`, two ordinates separated by `m` unit bins have
support-phase derivative only `asymp m/T`. Integration by parts therefore loses
a factor `T` unless the nonoscillatory amplitude derivative is `O(B_T/T)`.
`L-19821` proves at best `A'=O(B_T)` and replaces the actual radial phase by a
model with derivative of order one. That substitution is unjustified.

**Verdict on the reviewer:** correct.

### 2.3 The complete `d_8` gap is false

The exact source constraints in the full even prolate packet are

\[
 \sum q_nc_n=0,
 \qquad
 \sum\varepsilon_n\chi_nq_nc_n=0,
 \qquad \varepsilon_n=(-1)^{n/2}.
\]

The positive pair

\[
 p_+=e_0/q_0-e_4/q_4
\]

has integral residual `d_4-d_0`, while the negative-Fourier pair

\[
 p_-=e_2/q_2-e_6/q_6
\]

has residual `-(d_6-d_2)`. Their exact constrained combination has Rayleigh
scale `d_4`. A second exact constrained combination based on `p_-` and
`e_4/q_4-e_8/q_8` has Rayleigh scale `d_6`. The overlap tends to zero because
`d_4/d_6,d_6/d_8 -> 0`.

Thus a complete target-complement floor at scale `d_8` is impossible. The
correct complete scale is `d_6`; `d_8` remains the next scale only inside the
`+1` Fourier sector.

**Verdict on the reviewer:** correct.

### 2.4 Qualitative source surjectivity gives no quantitative inverse

`L-16211` itself states that density and finite projection imply surjectivity but
supply no lower singular-value bound. Avoiding the countable set of exact zeta
cycles removes exact rank loss; it does not control near-cycle conditioning.
`L-16218` conditions an abstract two-constraint prolate coefficient frame before
applying the arithmetic source map. It is not a quantitative theorem for the
complete projected arithmetic image.

**Verdict on the reviewer:** correct.

### 2.5 The raw endpoint upper-bound argument in `L-16227` fails

For a compact source with nonzero endpoint value, Fourier leakage starts with a
`1/xi` endpoint term. The `L2` norm of the `k`-th dilation is then `asymp 1/k`,
so the raw sum of individual norms need not converge. `L-16221` correctly says
that the first endpoint channel must be retained as a symmetrically summed
`Li_1`/sawtooth term or removed by an endpoint condition. The upper-bound line
in `L-16227` cannot bypass that collective treatment.

**Verdict on the reviewer:** correct.

### 2.6 The local-Weyl normalization in `T-19807` is inconsistent

The theorem writes an absolute whitened error `epsilon_j -> 0` and immediately
uses it as a relative error against `log R`. The dimensionless quantity is

\[
 \eta_R={\|D_R^{-1/2}E_RD_R^{-1/2}\|\over\log R}.
\]

**Verdict on the reviewer:** correct.

## 3. Where the review overstates or misidentifies the frontier

### 3.1 The displayed source-frame theorem is not norm invariant

The expression

\[
 \sigma_{\min}(P_N\Sigma_\mu E|_{\mathcal U})
\]

has no invariant meaning until a domain metric on `mathcal U` is fixed. Replacing
a source basis by `JA` multiplies the matrix on the right by `A` and can make its
Euclidean singular values arbitrarily large or small without changing its
range, omitted-tail form, or finite CCM image.

More seriously, in the natural Mellin-sampling metric the periodized source map
factors exactly as

\[
 T_L=D_{\zeta,L}M_L,
 \qquad
 (D_{\zeta,L})_{kk}
 =\zeta\!\left({1\over2}-{2\pi i k\over L}\right).
\]

A fixed lower bound `sigma_min(T_L) >= L^{-C}` together with a polynomially
bounded Mellin frame would force a uniform bound on multiplicities of
critical-line zeros. This is proved in `L-19825`. Therefore the review's
polylogarithmic full-frame statement is not a neutral PSWF-conditioning lemma;
it contains additional zeta small-value information.

The RH transfer needs only a metric-inflation condition

\[
 K_R\,{d_4(R)\over d_6(R)}\to0,
\]

not specifically a polylogarithmic Euclidean right inverse. Since
`d_4/d_6=Theta(R^{-2})`, even substantial polynomial frame loss can be
admissible.

**Verdict on the reviewer:** the objection to qualitative surjectivity is
correct, but the proposed replacement is stronger than necessary and is
underspecified until its metrics are fixed.

### 3.2 Holomorphicity itself is not absent from the primary PSWF theory

Dunster's radial PSWF is entire for order zero, and his Liouville--Green
construction is explicitly carried out for complex `z` before being summarized
on the real radial axis. The genuinely missing step in the repository is not
mere holomorphic continuation. It is a uniform shrinking-strip theorem with:

```text
one support-parameter derivative,
mode-uniform normalization,
stationary-branch extraction,
fold treatment,
and the complete endpoint/alias ledger.
```

`L-19827` supplies a proposed proof of that complete package using the exact
fixed-domain prolate operator, Hellmann--Feynman differentiation, the complex
Liouville equation, and collective endpoint summation. It requires independent
special-function review, but the review's description of the primary-source
input as merely real-axis is too coarse.

### 3.3 The relative local-Weyl theorem is not an independent fourth miracle

Once the complete branch/alias theorem gives:

```text
a slowly varying diagonal profile,
correctly differentiated oscillatory branches,
a normalized tail Gram floor,
and a collectively controlled endpoint ledger,
```

the line-centered local Weyl law follows from Stieltjes integration against
Riemann--von Mangoldt. The external `1/R` normalization makes the zero-count
remainder `O(polylog(R) log(R)/R)`. Cross branches and horizontal displacement
are then removed at one support by the already proved Hilbert-valued support
large sieve.

This implication is proved in `L-19828`. Thus gates 3 and 4 are nested, not
independent.

## 4. Revised classification of the independent review

| Review finding | Adversarial disposition |
|---|---|
| `L-19821` false as written | **CONFIRMED** |
| missing `T A'` large-sieve scale | **CONFIRMED** |
| complete `d_8` hierarchy false | **CONFIRMED** |
| complete scale should be `d_6` | **CONFIRMED** |
| qualitative source surjectivity insufficient | **CONFIRMED** |
| requested polylog source inverse is exact frontier | **OVERSPECIFIED / METRIC-DEPENDENT** |
| raw alias upper bound invalid with endpoint value | **CONFIRMED** |
| complete endpoint treatment absent in old proposal | **CONFIRMED** |
| primary Dunster input is only real-axis | **TOO STRONG; COMPLEX THEORY EXISTS** |
| relative local-Weyl is an independent open theorem | **NOT INDEPENDENT ONCE BRANCH LEDGER IS PROVED** |
| original RH proof stands | **NO** |

Overall:

```text
INDEPENDENT REVIEW: VERIFIED WITH MATERIAL FRONTIER FIXES
ORIGINAL T-19807/L-19821 PROPOSAL: DOES NOT STAND
SIGNED d6 COMPOSITION: STILL A VIABLE CORRECTED ROUTE
ACCEPTED RH PROOF: NO
```

## 5. New theorem stack from this pass

```text
L-19825
  exact periodized source factorization;
  multiplicity obstruction to the unqualified polylog frame;
  invariant metric gate actually needed by ground transfer.

L-19826
  signed arithmetic-tail hierarchy from a collective first-versus-rest
  alias cross moat; target d4 and complete complement d6.

L-19827
  proposed complete holomorphic WKB/fold/alias theorem with one support
  derivative and collective endpoint summation.

L-19828
  relative operator local-Weyl theorem derived from L-19827 and L-16226.
```

The remaining irreducible issue is no longer accurately described as four
unrelated estimates. It is the construction of a complete finite source/image
metric satisfying the invariant loss gate while preserving the prolate-adapted
tail representation. The full periodized polylog singular-value statement is
one sufficient route, but it is not the only route and it is not a free
consequence of generic support.
