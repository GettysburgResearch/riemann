# L-19822 — Two-end zero-orbit phase decomposition

Claim ID: `L-19822`  
Title: After endpoint phase extraction, every large off-line factor is oscillatory and every nonoscillatory horizontal correction is amplitude-local  
Status: `PROPOSED — COMPLETE ORBIT ALGEBRA; SOURCE-SPECIFIC AMPLITUDE BOUNDS SEPARATE`  
Authoring agent: `gpt56-pro-09-n`  
Created: 2026-08-07  
Dependencies: the exact two-end transform decomposition in `L-15631/L-19819`; zeta-zero conjugation symmetry  
Scope: Interface C of `T-19807`

## 1. Evaluation row

Let `H_R` be a finite coefficient Hilbert space.  Suppose the corrected-tail
evaluation row of `L-19820` has the exact finite branch form

\[
 \boxed{
 U_R(z)=
 e^{iLz/2}A_{+,R}(z)
 +e^{-iLz/2}A_{-,R}(z),
 \qquad L=\log R,
 }
 \tag{L-19822.1}
\]

where

\[
 A_{\pm,R}(z):H_R\to K_R
 \tag{L-19822.2}
\]

are holomorphic on the closed centered zeta strip.  A fixed finite number of
radial, parity, endpoint, and Poisson branches is handled by a Hilbert direct
sum and does not change the algebra.

Let

\[
 z=\gamma+i\delta,
 \qquad |\delta|<1/2.
 \tag{L-19822.3}
\]

The Hermitian contribution of the conjugate horizontal pair is

\[
 \boxed{
 \mathcal O_R(z)
 =U_R(\bar z)^*U_R(z)
  +U_R(z)^*U_R(\bar z).
 }
 \tag{L-19822.4}
\]

On the centered line,

\[
 \mathcal O_R(\gamma)=2U_R(\gamma)^*U_R(\gamma)\succeq0.
 \tag{L-19822.5}
\]

Multiplicity simply multiplies the matrix.

## 2. Exact four-channel expansion

Because

\[
 \overline{e^{iL\bar z/2}}=e^{-iLz/2},
\]

one has

\[
\begin{aligned}
 U_R(\bar z)^*U_R(z)
 ={}&A_{+,R}(\bar z)^*A_{+,R}(z)\\
 &+A_{-,R}(\bar z)^*A_{-,R}(z)\\
 &+e^{-iLz}A_{+,R}(\bar z)^*A_{-,R}(z)\\
 &+e^{iLz}A_{-,R}(\bar z)^*A_{+,R}(z).
\end{aligned}
 \tag{L-19822.6}
\]

Thus the orbit splits into:

```text
same-end ++ channel: nonoscillatory;
same-end -- channel: nonoscillatory;
cross-end +- channel: phase exp(-i L gamma) exp(+L delta);
cross-end -+ channel: phase exp(+i L gamma) exp(-L delta).
```

The terms with possible exponential horizontal weight retain the nonconstant
support phases `exp(+-iL gamma)`.  No exponentially large off-line factor becomes
a hidden nonoscillatory diagonal term.

## 3. Line-centered subtraction

Put

\[
 \Delta\mathcal O_R(z)
 =\mathcal O_R(z)-\mathcal O_R(\gamma).
 \tag{L-19822.7}
\]

### Same-end part

For `epsilon in {+,-}`, define

\[
 B_{\epsilon,R}(z)
 =A_{\epsilon,R}(\bar z)^*A_{\epsilon,R}(z).
 \tag{L-19822.8}
\]

Then

\[
 \boxed{
 B_{\epsilon,R}(\gamma+i\delta)
 -B_{\epsilon,R}(\gamma)
 =\int_0^\delta
 \partial_yB_{\epsilon,R}(\gamma+iy)\,dy.
 }
 \tag{L-19822.9}
\]

This term contains no support phase.  Its complete cost is controlled by the
horizontal amplitude-derivative Gram.

### Cross-end part

Every cross-end term in the actual orbit and in the line-centered comparator is
rank one and carries one of the phases

\[
 e^{\pm iL\gamma}.
 \tag{L-19822.10}
\]

The horizontal factors `e^(+-L delta)` belong to the profile amplitude.  Thus
the cross-end difference is a fixed finite sum of rank-one support-phase
families of the form required by `L-19818`.

## 4. Quantitative same-end bound

Assume, in the regularized metric `widehat D_R`, that

\[
 \boxed{
 {1\over R}\sum_{aR\leq\gamma\leq bR}
 \sup_{|y|\leq1/2}
 \left|
 \partial_y
 [A_{\epsilon,R}(\gamma-iy)^*
  A_{\epsilon,R}(\gamma+iy)]
 \right|
 \preceq h_R\widehat D_R
 }
 \tag{L-19822.11}
\]

for both endpoint signs.  Then the complete nonoscillatory horizontal
correction satisfies

\[
 \boxed{
 -h_R\widehat D_R
 \preceq
 \Delta\mathcal O_R^{\rm same}
 \preceq
 h_R\widehat D_R.
 }
 \tag{L-19822.12}
\]

The factor `|delta|<=1/2` is absorbed into `h_R`.

A sufficient profile-level condition follows from Cauchy--Schwarz.  If

\[
 {1\over R}\sum_\gamma
 A_{\epsilon,R}(\gamma+iy)^*
 A_{\epsilon,R}(\gamma+iy)
 \preceq C\log R\,\widehat D_R
 \tag{L-19822.13}
\]

and

\[
 {1\over R}\sum_\gamma
 (\partial_yA_{\epsilon,R})(\gamma+iy)^*
 (\partial_yA_{\epsilon,R})(\gamma+iy)
 \preceq q_R^2\log R\,\widehat D_R,
 \tag{L-19822.14}
\]

then

\[
 \boxed{
 h_R\leq C q_R\log R.
 }
 \tag{L-19822.15}
\]

Thus `q_R=o(1)` gives `h_R=o(log R)`, and

\[
 q_R\tau_R\log R\to0
 \tag{L-19822.16}
\]

places the same-end correction below the final whole-matrix lower-envelope
scale.

For radial corrected tails, the natural horizontal derivative scale is
`q_R=R^(-1+o(1))`.  Endpoint and finite-prefix channels must be retained in
their exact ledgers rather than assigned that scale without proof.

## 5. Cross-end support average

Let `M_R` be the regularized vector-profile envelope of every cross-end branch,
and assume the line-centered Bessel estimate of `L-19821`.  Applying
`L-19818` gives, for a packet of dimension `d_R`,

\[
 \boxed{
 {1\over R}\int_R^{2R}
 \|\Delta\mathcal O_s^{\rm cross}\|_{\rm op}^2ds
 \ll {d_RM_R^2(\log R)^3\over R}.
 }
 \tag{L-19822.17}
\]

For

\[
 d_R=R^{o(1)},
 \qquad M_R=R^{3/8+o(1)},
 \tag{L-19822.18}
\]

this is

\[
 R^{-1/4+o(1)}.
 \tag{L-19822.19}
\]

Hence a cofinal selected support has cross-end error

\[
 R^{-1/8+o(1)}.
 \tag{L-19822.20}
\]

## 6. Central and fold regions

The clean phase theorem applies where the support action has nonzero derivative
separation.  The remaining pieces are finite and explicit:

1. a central region in which the endpoint amplitudes are expanded directly;
2. Airy/fold windows whose total support measure shrinks;
3. endpoint-polylogarithm and Poisson-alias channels from `L-16221`;
4. discarded Fourier-mode terms in the corrected tail of `L-19820`.

They belong to the deterministic regular error `alpha_R` in `T-19807` and must
satisfy

\[
 \alpha_R=o(\log R),
 \qquad
 \alpha_R\tau_R\to0.
 \tag{L-19822.21}
\]

## 7. Consequence for Interface C

The complete actual-minus-line matrix is the sum of:

\[
 \boxed{
 \text{same-end horizontal amplitude correction}
 +\text{rank-one cross-end support phases}
 +\text{finite central/fold/endpoint ledger}.}
 \tag{L-19822.22}
\]

Therefore Interface C of `T-19807` is reduced to proof-grade source estimates
for:

1. the horizontal derivative Gram `q_R`;
2. the regularized cross-end vector envelope;
3. the finite central and endpoint ledgers.

The decomposition itself is exact and contains every member of every symmetric
zero orbit.

## 8. Proof boundary

- The four-channel orbit expansion is exact.
- It uses no RH assumption and no zero-density estimate beyond the later Bessel
  summation.
- Production must verify that the corrected-tail transform really has the
  declared finite two-end branch form after every Poisson and Fourier correction.
- The smallness of the same-end derivative channel is not automatic for an
  arbitrary Paley--Wiener vector; it is a source-specific radial/endpoint gate.
- This lemma closes the phase bookkeeping, not the final source derivative
  estimate.
