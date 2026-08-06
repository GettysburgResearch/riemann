# R-19805 — The quarter-power support argument and complete `d_8` gap fail

Claim ID: `R-19805`  
Status: **PROPOSED REVIEW RESPONSE — ORIGINAL `L-19821` AND COMPLETE-SPACE `d_8` CLAIM REJECTED AS WRITTEN**  
Authoring agent: `gpt56-pro-09-o`  
Created: 2026-08-07  
Reviewed objects: `L-19821` blob `1953fcd0e8ca83456b9a878aefaf43adbce825d6`; `T-19807` blob `863bd147659dc0fd46ac2f90945b5ff8ea37bc0b`  
Scope: exact algebraic refutation and corrected proof boundary; no RH claim

## 1. Frozen review boundary

The commit originally reported for the global prolate attack,

```text
83dac9b1ff95f64b4b48f788c017511d3d7f2aee
```

is not resolvable in the repository. The matching artifacts are present at PR
#202 head

```text
585cda919808429a759cf0bf7ab054af40f9a6d2
```

with the blob identities listed above. This refutation applies to those exact
blobs. It does not retroactively change the status of independently passing
finite or conditional claims elsewhere in the stack.

## 2. Exact cancellation of the support translation

The rejected lemma starts with the normalized omitted-tail transform

\[
 \widehat T_{j,R}(s)
 =\sqrt{\frac{d_j(R)}R}\,
   e^{-isx_R}\Phi_{j,R}(s/R),
 \qquad x_R=\log\lambda.
 \tag{R-19805.1}
\]

The polarized zero-side Weil matrix does not use an isolated transform. It uses

\[
 \overline{\widehat T_{j,R}(\overline s)}
 \widehat T_{k,R}(s).
\]

Substitution gives the exact identity

\[
\begin{aligned}
 \overline{\widehat T_{j,R}(\overline s)}
 \widehat T_{k,R}(s)
 &={\sqrt{d_j(R)d_k(R)}\over R}
   e^{isx_R}e^{-isx_R}
   \overline{\Phi_{j,R}(\overline s/R)}
   \Phi_{k,R}(s/R)\\
 &={\sqrt{d_j(R)d_k(R)}\over R}
   \overline{\Phi_{j,R}(\overline s/R)}
   \Phi_{k,R}(s/R).
\end{aligned}
\tag{R-19805.2}
\]

Thus the factor

\[
 |e^{-isx_R}|\le R^{1/4}
\]

cancels identically before the quadratic zero sum is formed. It is neither a
cost nor a reserve in the actual support-average problem. The horizontal issue
lies in the incoming/outgoing radial branch interference inside `Phi`, as was
already recognized by `R-16204`.

Consequently the principal mechanism asserted in Sections 3, 4, and 6 of
`L-19821` is inapplicable to the zero-side quadratic form.

## 3. The large-sieve derivative hypothesis was not met

The abstract support large sieve `L-16226` assumes, on `T<=R<=2T`,

\[
 \|A_\gamma(R)\|+T\|\partial_RA_\gamma(R)\|\le B_T.
 \tag{R-19805.3}
\]

The factor `T` is load-bearing. For the actual support phase

\[
 R S(\gamma/R),
\]

the derivative difference for ordinates separated by `m` unit bins is only of
size `m/T`. One integration by parts therefore requires the amplitude derivative
to be smaller than its amplitude scale by a factor `T^{-1}`.

`L-19821` established only a bound of the form

\[
 \|A_\gamma(R)\|+\|\partial_RA_\gamma(R)\|
 \ll T^{1/4}(\log T)^C.
 \tag{R-19805.4}
\]

This does not imply (R-19805.3) with
`B_T=T^{1/4}(log T)^C`. Interpreted literally, it only gives
`B_T` of order `T^{5/4}(log T)^C`, which destroys the claimed vanishing mean
square. The proof also replaces the radial action by an unproved phase
`exp(i gamma phi(R))` with `|phi'|` bounded below independently of `T`; no such
representation is derived from the Dunster action.

Therefore the displayed bounds `L-19821.13` and `L-19821.14` do not follow from
the stated hypotheses.

## 4. Correct branchwise support-average interface

The viable repair is not a polynomial growth estimate for the cancelled
translation. It is a branchwise holomorphic WKB theorem. One needs an expansion

\[
 \Phi_R(z)=\sum_{\nu=1}^{B}
 a_{\nu,R}(z)e^{iRS_\nu(z)}+e_R(z),
 \tag{R-19805.5}
\]

with `B` fixed, real-analytic actions on the real branch windows, and bounds

\[
 \|a_{\nu,R}\|+\|\partial_z a_{\nu,R}\|
 +R\|\partial_Ra_{\nu,R}\|
 \le(\log R)^C
 \tag{R-19805.6}
\]

through the shrinking strip `|Im z|<=1/(2R)`, together with compatible bounds
for the remainder and the Airy transition.

For

\[
 z=x+i\delta/R,
 \qquad |\delta|<1/2,
\]

Taylor expansion then gives

\[
 RS_\nu(x+i\delta/R)
 =RS_\nu(x)+i\delta S_\nu'(x)+O(R^{-1}),
 \tag{R-19805.7}
\]

and hence

\[
 e^{iRS_\nu(x+i\delta/R)}
 =e^{iRS_\nu(x)}
  e^{-\delta S_\nu'(x)}
  (1+O(R^{-1})).
 \tag{R-19805.8}
\]

On a compact nonfold branch window, horizontal displacement changes only the
amplitude by a bounded factor. After the real support phase is extracted, the
correct amplitude can satisfy

\[
 \|A_\rho(R)\|+R\|A_\rho'(R)\|
 \le(\log R)^C.
 \tag{R-19805.9}
\]

The genuine `L-16226` theorem would then give a mean square of order
`(log R)^C/R`. This remains conditional on a holomorphic Dunster expansion, a
uniform Airy version, and collective endpoint and infinite-alias estimates.
`L-19822` records the exact conditional implication without claiming those
inputs.

## 5. The complete finite space contains both Fourier-sign sectors

Let `e_n` be the even prolate eigenfunctions in the finite Fourier convention,
with

\[
 \widehat e_n=\varepsilon_n\chi_ne_n,
 \qquad
 \varepsilon_n=(-1)^{n/2},
 \qquad
 0<\chi_n<1,
 \tag{R-19805.10}
\]

and put

\[
 d_n=1-\chi_n,
 \qquad
 q_n=e_n(0)\ne0
 \tag{R-19805.11}
\]

for the fixed modes used below. Evaluation of the Fourier transform at zero
gives

\[
 \int e_n=\varepsilon_n\chi_nq_n.
 \tag{R-19805.12}
\]

The `+1` Fourier sector contains modes `0,4,8,...`; the `-1` sector contains
modes `2,6,10,...`. The finite CCM real-zero criterion does not discard the
second sector. Any complete complement theorem must control both.

Define the point-cancelled vectors

\[
 p_+={e_0\over q_0}-{e_4\over q_4},
 \qquad
 p_-={e_2\over q_2}-{e_6\over q_6}.
 \tag{R-19805.13}
\]

They satisfy `p_+(0)=p_-(0)=0`, while their integral residuals are

\[
 r_+=\chi_0-\chi_4=d_4-d_0,
 \tag{R-19805.14}
\]

and

\[
 r_-=-\chi_2+\chi_6=-(d_6-d_2).
 \tag{R-19805.15}
\]

Therefore

\[
 v_1=r_-p_+-r_+p_-
 \tag{R-19805.16}
\]

satisfies both exact source constraints

\[
 v_1(0)=0,
 \qquad
 \int v_1=0.
 \tag{R-19805.17}
\]

After division by `r_-`,

\[
 \widetilde v_1=p_+-{r_+\over r_-}p_-.
 \tag{R-19805.18}
\]

For the exact first-alias defect form

\[
 \mathcal D e_n=s_n^2e_n,
 \qquad
 s_n^2={1-\chi_n^2\over2}\asymp d_n,
 \tag{R-19805.19}
\]

the two Fourier-sign sectors are orthogonal. The fixed-mode Fuchs hierarchy
therefore gives

\[
 \mathcal D(\widetilde v_1,\widetilde v_1)
 =O(d_4)+O(d_4^2/d_6)
 =O(d_4).
 \tag{R-19805.20}
\]

Thus the target can still live at the advertised `d_4` scale after exact signed
repair.

## 6. A target-complement direction exists at the lower `d_6` scale

Introduce the next positive-sector point-cancelled pair

\[
 p_{+,2}={e_4\over q_4}-{e_8\over q_8},
 \qquad
 r_{+,2}=\chi_4-\chi_8=d_8-d_4.
 \tag{R-19805.21}
\]

Then

\[
 v_2=r_{+,2}p_- - r_-p_{+,2}
 \tag{R-19805.22}
\]

also satisfies both exact source constraints. After division by `r_(+,2)`,

\[
 \widetilde v_2=p_--{r_-\over r_{+,2}}p_{+,2},
 \tag{R-19805.23}
\]

and hence

\[
 \mathcal D(\widetilde v_2,\widetilde v_2)
 =O(d_6)+O(d_6^2/d_8)
 =O(d_6).
 \tag{R-19805.24}
\]

The leading terms of `widetilde v_1` and `widetilde v_2` lie in opposite
Fourier-sign sectors. Therefore

\[
 {\langle\widetilde v_2,\widetilde v_1\rangle
  \over
  \|\widetilde v_1\|\,\|\widetilde v_2\|}
 =O(d_4/d_6+d_6/d_8)\longrightarrow0.
 \tag{R-19805.25}
\]

Let `w_2` be the ordinary orthogonal projection of `widetilde v_2` onto
`widetilde v_1^perp`. Then `||w_2||` stays bounded below, and the quadratic
triangle inequality gives

\[
 \mathcal D(w_2,w_2)=O(d_6).
 \tag{R-19805.26}
\]

Consequently the complete target-complement generalized eigenvalue is at most
`C d_6`. Since

\[
 d_6/d_8\longrightarrow0,
 \tag{R-19805.27}
\]

no lower bound of the form

\[
 \mathcal D-\mu_DG\succeq c_8d_8G
 \tag{R-19805.28}
\]

can hold on the complete signed finite space with fixed `c_8>0`.

This refutes `T-19807.10` as a complete-space statement. It does not refute the
`+1`-sector `d_4/d_8` calculation.

## 7. Corrected scale and exact status

The viable full-space hierarchy is

```text
repaired target scale       O(d_4)
positive-sector next scale  Omega(d_8)
negative-sector low scale   Omega(d_6)  [still to be proved]
complete candidate gap      d_6
```

Since `d_4/d_6 -> 0`, the Rayleigh-floor strategy can survive with a weaker
rate. What has been proved here is the obstruction to a `d_8` complete gap and
the exact `d_6` upper-scale witness. A matching complete lower bound at scale
`d_6` is a new signed-sector theorem, not a consequence of this refutation.

Accordingly:

```text
L-19821:                         REJECTED AS WRITTEN
T-19807 complete d_8 hypothesis: REJECTED AS WRITTEN
branchwise support repair:       PROPOSED, conditional
signed d_6 lower hierarchy:      OPEN
RH:                              NOT PROVED
```
