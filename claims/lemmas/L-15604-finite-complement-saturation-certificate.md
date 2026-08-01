# L-15604 — Finite complement saturation certificate

Claim ID: `L-15604`  
Title: A symbol outer floor plus one finite visible Schur block proves exact low-index saturation  
Status: `PROPOSED`  
Authoring agent: `gpt56-pro-09-d`  
Created: 2026-07-31  
Dependencies: completion of squares; `L-14308`; `L-14310/L-14311`; `L-15603`  
Scope: finite proof interface for `D<=C`

## Setup

Let `A` be a lower-bounded self-adjoint operator or closed quadratic form on a
Hilbert space `H`.  Let `L` be a finite-dimensional exact repaired radical
packet and let `U` be any finite symbol-selected packet whose orthogonal
complement already has a rigorous floor.

Put

\[
 W=L+U,
 \qquad
 V=W\cap L^\perp,
 \qquad
 E=W^\perp.
 \tag{L-15604.1}
\]

Then

\[
 \boxed{L^\perp=V\oplus E.}
 \tag{L-15604.2}
\]

The space `V` is finite-dimensional, with

\[
 \dim V\le\dim U.
 \tag{L-15604.3}
\]

Relative to (L-15604.2), write the restriction of the exact form to `L^perp` as

\[
 A|_{L^\perp}
 =\begin{pmatrix}Y&R^*\\R&C\end{pmatrix}.
 \tag{L-15604.4}
\]

Let `M` be strictly positive on `E`.

## Saturation theorem

Suppose there are real `Gamma`, `h>0` such that

\[
 C-\Gamma I_E\succeq hM
 \tag{L-15604.5}
\]

and

\[
 \boxed{
 Y-\Gamma I_V-h^{-1}R^*M^{-1}R\succeq0.}
 \tag{L-15604.6}
\]

Then

\[
 \boxed{A|_{L^\perp}\succeq\Gamma I.}
 \tag{L-15604.7}
\]

Consequently, if `dim L=d` and for some `t<Gamma`

\[
 A|_L\prec tI,
 \tag{L-15604.8}
\]

then

\[
 \boxed{
 N_A(t)=N_A(\Gamma)=d.}
 \tag{L-15604.9}
\]

In particular the scalar capacity inequality is certified exactly with

\[
 D_{\rm sat}=C=d.
 \tag{L-15604.10}
\]

### Proof

For `v in V`, `e in E`, (L-15604.5) gives

\[
 \begin{aligned}
 \langle(A-\Gamma)(v+e),v+e\rangle
 &\ge \langle(Y-\Gamma)v,v\rangle
 +2\Re\langle Rv,e\rangle+h\langle Me,e\rangle.
 \end{aligned}
\]

Completing the square in the `M` metric yields

\[
 \begin{aligned}
 h\langle Me,e\rangle+2\Re\langle Rv,e\rangle
 ={}&h\|M^{1/2}e+h^{-1}M^{-1/2}Rv\|^2\\
 &-h^{-1}\langle R^*M^{-1}Rv,v\rangle.
 \end{aligned}
\]

The remaining finite quadratic form is nonnegative by (L-15604.6), proving
(L-15604.7).  Equation (L-15604.8) and min--max give at least `d` eigenvalues
below `t`; (L-15604.7) gives at most `d` below `Gamma`.  Since `t<Gamma`, all
counts equal `d`.  QED.

## Why the certificate is finite

The symbol theorem is used only for the complete outer space `E=W^perp`.
Everything not covered by that theorem is retained in the finite space `V`.
Thus the proof object consists of:

1. a finite basis for `L`;
2. a finite basis for the symbol packet `U`;
3. exact or directed Gram data constructing `V=(L+U) intersect L^perp`;
4. a directed outer floor (L-15604.5);
5. finite matrices `Y`, `R`, and the metric compression needed for
   `R^*M^-1R`;
6. an exact rational LDL certificate for (L-15604.6).

No principal angle or eigenvector matching is required.

## Directed enclosure adapter

Suppose the assembled form differs from the represented form by an operator or
absolute form radius `delta>=0`.  It is sufficient to prove the stronger
represented inequalities

\[
 C_0-(\Gamma+\delta)I\succeq hM
 \tag{L-15604.11}
\]

and

\[
 Y_0-(\Gamma+\delta)I
 -h^{-1}R_0^*M^{-1}R_0
 -\mathcal E_R\succeq0,
 \tag{L-15604.12}
\]

where `mathcal E_R` is a rigorously derived Loewner charge for the interval
uncertainty in the cross map.  Alternatively, form one complete directed block
and use a robust Schur complement with lower `M` and upper cross Gram.

The analytic radius and every Loewner direction must be declared explicitly; a
midpoint Schur complement is not a certificate.

## Evaluation-visible refinement

Let `Z` be a finite set of certified zeta zeros and apply the evaluation split of
`L-15304` to the finite packet `V`:

\[
 V=V_{\rm near}\oplus V_{\rm vis}.
\]

The radical-like near-kernel `V_near` may be enlarged into `L`.  Only the
visible residual `V_vis` remains in the finite saturation matrix `Y`.  This can
substantially reduce the size of the load-bearing Schur block without changing
any logical quantifier.

## Relationship to the multiband symbol packet

`L-14311` provides precisely the outer-floor input:

\[
 A|_{U^\perp}\succeq\gamma_{\rm symbol}I.
\]

Since `E=(L+U)^perp subset U^perp`, the same floor holds on `E`.  The symbol
packet need not be close to `L`; any mismatch is represented exactly by `V` and
must pass (L-15604.6).

This is the correct finite composition of the symbol and radical routes.

## Proof boundary

- L-15604 proves a finite sufficient condition for exact saturation.
- It does not show that the finite visible Schur matrices pass cofinally.
- It does not estimate the size of `U` or `V`.
- It does not turn a sampled symbol into a directed outer floor.
- The cofinal asymptotic theorem remains a separate obligation.
