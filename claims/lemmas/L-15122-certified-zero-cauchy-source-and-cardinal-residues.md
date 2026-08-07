# L-15122 — Certified-zero Cauchy source and exact cardinal residue quadrature

Claim ID: `L-15122`  
Status: **PROVED FINITE/SELECTED-ZERO IDENTITY; ALL-ZERO POSITIVE MEASURE FORM CONDITIONAL ON RH**  
Authoring agent: `gpt56-04-f`  
Created: 2026-07-31  
Dependencies: the Guinand--Weil explicit formula; CCM equations (2.6), (3.2), (3.5), (3.17), and (5.2); `L-15114`; `L-15119`  
Scope: exact zero-side reconstruction of the arithmetic source and of every target-pinned residue weight  
Related counterexample candidates: none

## 1. Purpose

The prime-side formula of `L-15119` gives the exact arithmetic special source
`beta_n`.  The final scalar-line gate, however, is most transparent on the zero
side.

This lemma proves three facts.

1. Every proof-grade real centered zeta zero contributes one explicit positive
   Cauchy ray to the finite Weil matrix and one explicit Cauchy term to its
   special source.
2. Such certified line-zero contributions can be subtracted from the complete
   prime-side source without assuming RH; the remainder is an exact arithmetic
   residual source.
3. Interpolating the source through the finite target polynomial gives every
   target-pinned residue weight by one exact cardinal quadrature formula.

Under RH, taking all zeros turns the complete arithmetic source into a positive
discrete Cauchy transform.  This is a structural interpretation, not a permitted
assumption in a positive proof.

## 2. Fourier transform of the CCM basis

Let

\[
 L=2\log\lambda,
 \qquad
 x_n=\frac{2\pi n}{L},
 \qquad
 U_n(x)=L^{-1/2}e^{2\pi i n x/L},
\]

and let

\[
 V_n(u)=U_n(\log(\lambda u))
 \qquad (\lambda^{-1}\le u\le\lambda).
\]

For the multiplicative Fourier transform

\[
 \widehat V_n(t)=
 \int_{\lambda^{-1}}^\lambda V_n(u)u^{-it}\,\frac{du}{u},
\]

direct integration gives

\[
 \boxed{
 \widehat V_n(t)=
 \frac{2\sin(Lt/2)}{\sqrt L\,(t-x_n)}.}
 \tag{L-15122.1}
\]

The value at `t=x_n` is interpreted by removal of the singularity:

\[
 \widehat V_n(x_n)=(-1)^n\sqrt L.
\]

Put

\[
 r_{\gamma,L}=\frac{L\gamma}{2\pi}.
\]

Then for a real ordinate `gamma`,

\[
 \boxed{
 \widehat V_n(\gamma)=
 \frac{\sqrt L}{\pi}
 \frac{\sin(\pi r_{\gamma,L})}{r_{\gamma,L}-n}.}
 \tag{L-15122.2}
\]

## 3. One certified critical-line zero

Let `rho=1/2+i gamma` be a proof-grade critical-line zero of multiplicity
`m_gamma`.  Its contribution to the polarized Guinand--Weil zero sum on the
finite basis is

\[
 m_\gamma\,
 \widehat V_n(\gamma)\widehat V_m(\gamma).
\]

For a nonresonant ordinate

\[
 r_{\gamma,L}\notin\mathbb Z,
\]

define

\[
 \boxed{
 A_{\gamma,L}
 =m_\gamma\frac{L}{\pi^2}
  \sin^2(\pi r_{\gamma,L})>0.}
 \tag{L-15122.3}
\]

The zero contributes the positive rank-one matrix

\[
 \boxed{
 Q^{(\gamma)}_{nm}
 =\frac{A_{\gamma,L}}
 {(r_{\gamma,L}-n)(r_{\gamma,L}-m)}.}
 \tag{L-15122.4}
\]

A compatible special source, in the gauge `beta_0=0`, is

\[
 \boxed{
 \beta_n^{(\gamma)}
 =A_{\gamma,L}
  \left(
   \frac1{r_{\gamma,L}-n}
   -\frac1{r_{\gamma,L}}
  \right).}
 \tag{L-15122.5}
\]

Indeed,

\[
 \frac{\beta_n^{(\gamma)}-\beta_m^{(\gamma)}}{n-m}
 =Q^{(\gamma)}_{nm}.
\]

If `r_(gamma,L)` is an integer, the evaluation vector is supported on one
coordinate.  Its matrix contribution is diagonal only, so its special-source
contribution may be taken to be zero.  Such resonances must still be retained
in the raw diagonal if that diagonal is used, but they do not enter the
source line or the target-pinned diagonal.

## 4. A finite certified-zero source

For a finite proof-grade multiset `Z` of real centered zeros, put

\[
 Q_Z=\sum_{\gamma\in Z}Q^{(\gamma)},
 \qquad
 \beta_n^Z=\sum_{\gamma\in Z}\beta_n^{(\gamma)}.
 \tag{L-15122.6}
\]

Then

\[
 Q_Z\succeq0,
\]

and its off-diagonal entries satisfy

\[
 (Q_Z)_{nm}=\frac{\beta_n^Z-\beta_m^Z}{n-m}.
\]

Let `beta_n^W` be the complete arithmetic source produced independently from
the polar, archimedean, and all-prime-power formula of `L-15119`.  Define the
exact residual source

\[
 \boxed{
 \beta_n^{\rm rem}=\beta_n^W-\beta_n^Z.}
 \tag{L-15122.7}
\]

This subtraction is unconditional.  No sign is assigned to the residual and no
claim is made that the unlisted zeros lie on the critical line.  A directed
producer may enclose `beta^rem` by subtracting directed certified-zero source
balls from the directed prime-side source balls.

## 5. General Cauchy interpolation identity

The following finite algebra is independent of zeta.

Let the distinct real nodes be

\[
 \lambda_1,\ldots,\lambda_n,
\]

let every target coordinate `p_i` be nonzero, and normalize

\[
 \sum_i p_i=1.
\]

Put

\[
 \Omega(s)=\prod_i(\lambda_i-s),
 \qquad
 \phi_i(s)=\frac{\Omega(s)}{\lambda_i-s},
 \qquad
 P(s)=\sum_i p_i\phi_i(s).
 \tag{L-15122.8}
\]

Let a finite Cauchy source be

\[
 H(s)=d+\sum_\nu A_\nu
 \left(\frac1{r_\nu-s}-\frac1{r_\nu}\right),
 \tag{L-15122.9}
\]

where no `r_nu` is a node, and define

\[
 \beta_i=H(\lambda_i),
 \qquad
 R_0(s)=\sum_i p_i\beta_i\phi_i(s).
\]

Then

\[
 \boxed{
 R_0(s)-H(s)P(s)
 =-\Omega(s)
  \sum_\nu A_\nu
  \frac{P(r_\nu)}
       {\Omega(r_\nu)(r_\nu-s)}.}
 \tag{L-15122.10}
\]

### Proof

The common source gauge `d` cancels.  For one atom,

\[
 \frac1{r-\lambda_i}-\frac1{r-s}
 =\frac{\lambda_i-s}{(r-\lambda_i)(r-s)}.
\]

Since

\[
 (\lambda_i-s)\phi_i(s)=\Omega(s)
\]

and

\[
 \sum_i\frac{p_i}{r-\lambda_i}
 =-\frac{P(r)}{\Omega(r)},
\]

summing over `i` and then over the atoms proves (L-15122.10). QED.

The same identity holds for an infinite discrete source whenever the displayed
Cauchy differences converge absolutely and locally uniformly.  It follows by
applying the finite identity to partial sums and passing to the limit.

## 6. Exact cardinal quadrature for the target-pinned residues

Assume now that `P` has simple real roots

\[
 u_1<\cdots<u_{n-1}.
\]

Define

\[
 v_k=\frac{\Omega(u_k)}{P'(u_k)}
 \tag{L-15122.11}
\]

and the cardinal kernel

\[
 \boxed{
 \mathcal K_k(r)
 =\frac{\Omega(u_k)}{P'(u_k)}
   \frac{P(r)}{\Omega(r)(r-u_k)}.}
 \tag{L-15122.12}
\]

At `r=u_k` this is interpreted by continuity and equals `1`; at another root
`u_l`, it equals `0`.

For the source shifted by the target-pinning scalar,

\[
 \beta_i-c\lambda_i,
\]

the residue weight from `L-15114` is

\[
 w_k(c)=-\frac{R_c(u_k)}{P'(u_k)}.
\]

Equation (L-15122.10) gives the exact quadrature identity

\[
 \boxed{
 w_k(c)
 =c\,v_k+
  \sum_\nu A_\nu\mathcal K_k(r_\nu).}
 \tag{L-15122.13}
\]

Thus a positive Cauchy atom located exactly at one target root contributes its
full positive mass to that residue and zero to every other residue.

## 7. Selected-zero plus arithmetic-residual decomposition

Apply Part 6 first to the certified-zero source `beta^Z` and then by linearity
to the residual source (L-15122.7).  Put

\[
 R_{\rm rem}(s)
 =\sum_i p_i\beta_i^{\rm rem}\phi_i(s)
\]

and

\[
 \boxed{
 e_k^{\rm rem}
 =-\frac{R_{\rm rem}(u_k)}{P'(u_k)}.}
 \tag{L-15122.14}
\]

Then the **complete actual arithmetic residue weight** is

\[
 \boxed{
 w_k(c)
 =c\,v_k
  +\sum_{\gamma\in Z}
    A_{\gamma,L}\mathcal K_k(r_{\gamma,L})
  +e_k^{\rm rem}.}
 \tag{L-15122.15}
\]

Every term in (L-15122.15) has a proof-producing finite interface:

- certified zero balls, multiplicities, and directed phases for the selected
  sum;
- directed smooth target coefficients and directed simple-root isolators for
  `P`, `P'`, `Omega`, and `K_k`;
- the complete directed prime-side source minus the selected source for
  `beta^rem`;
- one rational scalar `c`.

No hypothesis about the unselected zeros is needed.

## 8. Complete all-zero form under RH

Assume RH.  Every centered nontrivial zero is real, and for fixed finite basis
indices the zero-side Gram series is absolutely convergent because

\[
 \widehat V_n(\gamma)=O_L(1/|\gamma|)
\]

and `N(T)=O(T log T)`.  Therefore

\[
 \boxed{
 QW_\lambda^N
 =\sum_\gamma m_\gamma
   \widehat V(\gamma)\widehat V(\gamma)^{\mathsf T}}
 \tag{L-15122.16}
\]

and, in the gauge `beta_0=0`,

\[
 \boxed{
 \beta_n^W
 =\sum_\gamma
  m_\gamma\frac{L}{\pi^2}\sin^2(\pi r_{\gamma,L})
  \left(
   \frac1{r_{\gamma,L}-n}
   -\frac1{r_{\gamma,L}}
  \right).}
 \tag{L-15122.17}
\]

The series in (L-15122.17) converges absolutely because its summand is
`O_L(n/gamma^2)`.

Consequently every arithmetic residue is the positive-measure quadrature

\[
 \boxed{
 w_k(c)=c\,v_k+
 \sum_\gamma
 m_\gamma\frac{L}{\pi^2}\sin^2(\pi r_{\gamma,L})
 \mathcal K_k(r_{\gamma,L}).}
 \tag{L-15122.18}
\]

The kernel `K_k` is signed in general.  Positivity of the measure therefore does
**not** make the residue automatically positive.  The exact remaining issue is
whether the cardinal quadrature, after one common scalar correction `c v_k`, is
positive for every target root.

## 9. Independent normalization audit

Equations (L-15122.5) and (L-15122.17) determine all source differences from the
zero side.  They provide an independent audit of the prime-side source
`L-15119`:

\[
 \frac{\beta_n^W-\beta_m^W}{n-m}
\]

must agree with the off-diagonal matrix obtained from the polar,
archimedean, and complete prime-power terms.  A production certificate should
perform this comparison on a finite selected-zero block plus the directed
residual, rather than infer one normalization from the other.

## 10. Gap audit

1. The selected-zero decomposition (L-15122.15) is unconditional; the complete
   positive-measure formulas (L-15122.16)--(L-15122.18) assume RH and may not be
   used as a premise in a positive proof.
2. Resonant line zeros contribute a diagonal basis atom but no source
   difference.  They must not be divided by `r-n` naively.
3. The cardinal kernels are not nonnegative in general.  A positive zero
   measure does not by itself settle the scalar line.
4. Root intervals must exclude nodes and prove simplicity before (L-15122.12)
   is evaluated.
5. The prime-side residual `beta^rem`, including every unselected zero orbit
   implicitly through the explicit formula, is load bearing.
6. This lemma proves an exact identity and a new finite certificate interface;
   it does not prove the required cofinal positivity.