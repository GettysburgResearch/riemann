# L-15622 — Off-line zeros force a full clipped-excess quantum

Claim ID: `L-15622`  
Title: A persistent negative Weil-cardinal direction makes the robust clipped-excess gate fail by at least one complete threshold gap  
Status: `PROPOSED — COMPLETE ABSTRACT OBSTRUCTION; CARDINAL LOCALIZATION INTERFACE IMPORTED`  
Authoring agent: `gpt56-pro-09-h`  
Created: 2026-08-01  
Dependencies: `L-15621`; `L-14321`; `T-14306`; `T-14307`; min--max  
Scope: exact logical strength of the requested cofinal inequality

## 1. Setting

At level `j`, let `A_j` be the exact localized Weil operator or closed form on
`H_j`. Let `P_j` be the orthogonal projection onto a `d_j`-dimensional
near-radical packet `R_j`, and assume

\[
 -\alpha_jP_j\preceq P_jA_jP_j\preceq\alpha_jP_j,
 \qquad 0\le\alpha_j<t_j<\Gamma_j.
 \tag{L-15622.1}
\]

Let `D_j>=0` be trace class and suppose

\[
 A_j\succeq G_jI-D_j.
 \tag{L-15622.2}
\]

Put

\[
 \theta_j=G_j-\Gamma_j,
 \qquad
 \eta_j=\Gamma_j-t_j>0,
 \qquad
 E_j=(D_j-\theta_jI)_+,
 \tag{L-15622.3}
\]

and

\[
 \mathfrak e_j
 =\operatorname{Tr}E_j-d_j(\Gamma_j-\alpha_j).
 \tag{L-15622.4}
\]

The requested robust gate is

\[
 \mathfrak e_j<\eta_j.
 \tag{L-15622.5}
\]

## 2. Abstract extra-low-direction theorem

Suppose, in addition to `R_j`, there is a `q`-dimensional subspace `N_j` such
that

\[
 \dim(R_j+N_j)=d_j+q
 \tag{L-15622.6}
\]

and the complete form is strictly below `t_j` on their sum:

\[
 A_j|_{R_j+N_j}\prec t_jI.
 \tag{L-15622.7}
\]

Then

\[
 \boxed{
 \mathfrak e_j>q(\Gamma_j-t_j).}
 \tag{L-15622.8}
\]

In particular, even one additional low direction forces

\[
 \boxed{
 \mathfrak e_j>\Gamma_j-t_j,}
 \tag{L-15622.9}
\]

which is the strict negation of the requested gate.

### Proof

Equation (L-15622.7) and min--max give

\[
 N_{A_j}(t_j)\ge d_j+q.
 \tag{L-15622.10}
\]

On the same subspace, (L-15622.2) yields

\[
 \langle D_ju,u\rangle
 > (G_j-t_j)\|u\|^2
 \qquad(0\ne u\in R_j+N_j).
\]

Hence, if

\[
 \nu_1(D_j)\ge\nu_2(D_j)\ge\cdots
\]

are the eigenvalues of `D_j`, then

\[
 \nu_{d_j+q}(D_j)>G_j-t_j
 =\theta_j+\eta_j.
 \tag{L-15622.11}
\]

Separately, compression of (L-15622.2) to `R_j` and the upper bound in
(L-15622.1) give

\[
 P_jD_jP_j\succeq(G_j-\alpha_j)P_j.
\]

Thus

\[
 \nu_{d_j}(D_j)\ge G_j-\alpha_j
 =\theta_j+\Gamma_j-\alpha_j.
 \tag{L-15622.12}
\]

The first `d_j` clipped eigenvalues therefore contribute at least

\[
 d_j(\Gamma_j-\alpha_j),
\]

while the next `q` clipped eigenvalues contribute strictly more than

\[
 q\eta_j=q(\Gamma_j-t_j).
\]

Consequently

\[
 \operatorname{Tr}E_j
 >d_j(\Gamma_j-\alpha_j)+q(\Gamma_j-t_j),
\]

which is (L-15622.8). QED.

## 3. Stable block criterion producing the extra low directions

A convenient sufficient condition for (L-15622.7) is the following. Suppose
`N_j` has dimension `q`, its metric Gram is the identity after whitening, and

\[
 A_j|_{N_j}\preceq-\nu I,
 \qquad \nu>0,
 \tag{L-15622.13}
\]

while the cross block satisfies

\[
 \|P_{N_j}A_jP_j\|^2
 <(t_j-\alpha_j)(t_j+\nu).
 \tag{L-15622.14}
\]

Then the Schur complement of

\[
 t_jI-A_j|_{R_j+N_j}
\]

is strictly positive, so (L-15622.7) holds.

This formulation is useful when `t_j->0`: it is enough that the cross block be
`o(sqrt(t_j-alpha_j))`, while the negative block retains one fixed moat.

## 4. Off-line Xi-cardinal directions

Assume RH is false. Choose a nonreal centered zero `rho` of `Xi`, with
multiplicity `m`, and let `bar(rho)` be its conjugate. The exact cardinal
functions of `T-14307` give

\[
 h_\rho=\ell_\rho-\ell_{\bar\rho},
 \tag{L-15622.15}
\]

with

\[
 \widehat h_\rho(\rho)=1,
 \qquad
 \widehat h_\rho(\bar\rho)=-1,
 \tag{L-15622.16}
\]

and zero evaluation at every other zeta zero. Therefore

\[
 \boxed{Q_W(h_\rho,h_\rho)=-2m.}
 \tag{L-15622.17}
\]

Every exact global `E`-range radical is Weil-orthogonal to `h_rho`, because its
transform vanishes at every zeta zero. Hence a finite exact global radical packet
and any finite collection of distinct off-line cardinal differences form a block
whose radical diagonal and cross terms vanish and whose cardinal block is
strictly negative definite after selecting one negative vector from each
conjugate-pair block.

## 5. Localization and diagonal extraction

Fix any finite collection of `q>=1` off-line conjugate pairs. Their cardinal
functions have double-exponential logarithmic tails. The exact radical packets
of `T-14306`, `L-15617`, or `L-15619` have exterior tails tending to zero in the
same form/metric topology.

For each finite packet rank and each prescribed positive `t_j`, support may be
chosen after freezing the finite data so that:

1. the localized cardinal negative block remains below `-nu I` for one fixed
   `nu>0`;
2. its metric Gram remains uniformly positive;
3. its cross form with the localized radical packet satisfies
   (L-15622.14);
4. the combined packet remains linearly independent.

The exact global orthogonality makes every cross term a tail term. The
quadratic/bilinear localization identities of `T-14306` make those errors tend
to zero. Since `alpha_j/t_j->0`, the right side of (L-15622.14) is asymptotic to
`nu t_j`, and a second diagonal support choice makes the cross error smaller.

Thus, under false RH, for every sufficiently large retained level there is at
least one extra low direction and

\[
 \boxed{
 \mathfrak e_j>\Gamma_j-t_j.}
 \tag{L-15622.18}
\]

More generally, `q` selected off-line conjugate pairs give

\[
 \boxed{
 \mathfrak e_j>q(\Gamma_j-t_j).}
 \tag{L-15622.19}
\]

## 6. Exact consequence

Under the cardinal-localization and near-radical hypotheses already declared in
the positive stack,

\[
 \boxed{
 \mathfrak e_j<\Gamma_j-t_j
 \quad\text{cofinally}
 \quad\Longrightarrow\quad\mathrm{RH}.}
 \tag{L-15622.20}
\]

This is not merely the consequence obtained by applying `L-15621` and the
localized-Weil lower-envelope theorem. Equation (L-15622.18) shows directly that
one hypothetical off-line zero forces the strict opposite inequality by one
whole threshold quantum.

Accordingly, the requested cofinal estimate is itself the no-off-line-zero
statement expressed through the deficit operator. Any successful proof must
introduce genuinely new arithmetic information capable of excluding the
cardinal direction; a plunge count, packet dimension, or finite-section tail
estimate alone cannot establish it.

## 7. Relation to the four positive defects

Using `L-15621`, the same conclusion may be written

\[
\begin{aligned}
&\operatorname{Tr}(Q_jE_jQ_j)
+\operatorname{Tr}\bigl(P_j(\alpha_jI-A_j)P_j\bigr)\\
&+\operatorname{Tr}(P_j\mathcal R_jP_j)
+\operatorname{Tr}\bigl(P_j(\theta_jI-D_j)_+P_j\bigr)\\
&\hspace{20mm}>\Gamma_j-t_j
\end{aligned}
 \tag{L-15622.21}
\]

under false RH, eventually. Thus at least one of the three unresolved defects in
`L-15621.38` must retain a full threshold quantum. They cannot all be made small
by source-tail engineering alone.

## 8. Proof boundary

- Sections 2--3 are exact operator theory.
- The cardinal negative block is exact in the centered Weil zero-sum
  normalization.
- Section 5 imports the fixed-finite-packet form-tail convergence proved in the
  existing cardinal/radical stack.
- The theorem proves an obstruction/equivalence direction, not the desired
  positive estimate.
- No proof of RH is claimed.