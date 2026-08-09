# L-33804 — The Q=4 all-pass bireflected defect is one block-state telescope

Claim ID: `L-33804`  
Title: In the exact independent-frequency normal orientation, the off-diagonal defect of the critical Euler–Blaschke factor factors through one positive state Gram and is the difference of two adjacent logarithmic-block kernels  
Status: **PROPOSED COMPLETE EXACT TWO-FREQUENCY / SCATTERING THEOREM — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-09  
Dependencies: PR #325 `L-32406`; PR #241 `L-9518`; elementary Blaschke algebra  
Scope: exact neutral-source placement; no arithmetic current bound, recurrence, or RH conclusion

## 1. Scalar all-pass factor

Fix `Q>1` and put

\[
 L=\log Q,
 \qquad
 a=Q^{-1/2},
 \qquad
 b=\sqrt{1-a^2}.
\]

In the centered variable `z=s-1/2`, retain the normalized Euler–Blaschke factor

\[
 \boxed{
 \phi(z)={a-e^{-Lz}\over1-ae^{-Lz}}.
 }
 \tag{L-33804.1}
\]

Define also the scalar state transfer

\[
 \boxed{
 R(z)={b\over1-ae^{-Lz}}.
 }
 \tag{L-33804.2}
\]

On `Re z=0`, `phi` is all-pass.

## 2. Exact two-frequency polarization identity

Let `z,w` be arbitrary complex numbers for which the denominators below are nonzero. Direct subtraction gives

\[
\begin{aligned}
1-\phi(z)\phi(w)
&={
 (1-ae^{-Lz})(1-ae^{-Lw})
 -(a-e^{-Lz})(a-e^{-Lw})
 \over
 (1-ae^{-Lz})(1-ae^{-Lw})}\\
&={(1-a^2)(1-e^{-L(z+w)})
 \over(1-ae^{-Lz})(1-ae^{-Lw})}.
\end{aligned}
\]

Therefore

\[
 \boxed{
 1-\phi(z)\phi(w)
 =R(z)R(w)\,[1-e^{-L(z+w)}].
 }
 \tag{L-33804.3}
\]

This is a polarized identity.  It is strictly stronger for local-block work than the diagonal boundary statement `|phi(it)|=1`.

For independent real frequencies `t,u`, set

\[
 z=it,
 \qquad
 w=-iu.
\]

Then

\[
 \boxed{
 1-\phi(it)\phi(-iu)
 =R(it)R(-iu)\,[1-e^{-iL(t-u)}].
 }
 \tag{L-33804.4}
\]

Thus every off-diagonal departure from the diagonal all-pass identity carries one exact difference factor in the physical frequency `t-u`.

## 3. Exact action on a block kernel

For any bounded interval `I` define the independent-frequency block kernel

\[
 \Phi_I(\omega)=\int_I e^{i\omega x}\,dx.
 \tag{L-33804.5}
\]

Translation gives

\[
 e^{-iL\omega}\Phi_I(\omega)
 =\Phi_{I-L}(\omega).
 \tag{L-33804.6}
\]

Multiplying (L-33804.4) by the block kernel therefore yields

\[
 \boxed{
 [1-\phi(it)\phi(-iu)]\Phi_I(t-u)
 =R(it)R(-iu)
 [\Phi_I(t-u)-\Phi_{I-L}(t-u)].
 }
 \tag{L-33804.7}

\]

This is exactly the independent-frequency orientation of PR #241 `L-9518`: no diagonal-frequency replacement has been made.

## 4. Bilinear physical identity

Let `F(t)` be the Fourier transform of any real or complex physical input for which the displayed finite/regularized integrals are legitimate.  Define

\[
 y=\phi(D)f,
 \qquad
 x=R(D)f.
\]

Use the normal block form

\[
 \mathcal B_I(f)
 ={1\over(2\pi)^2}
 \iint F(t)\overline{F(u)}\Phi_I(t-u)\,dt\,du.
 \tag{L-33804.8}
\]

Insert (L-33804.7).  Fourier inversion gives the exact localized energy identity

\[
 \boxed{
 \mathcal B_I(f)-\mathcal B_I(y)
 =\mathcal B_I(x)-\mathcal B_{I-L}(x).
 }
 \tag{L-33804.9}
\]

Equivalently,

\[
 \boxed{
 \mathcal B_I(f)+\mathcal B_{I-L}(x)
 =\mathcal B_I(y)+\mathcal B_I(x).
 }
 \tag{L-33804.10}
\]

The right-side state energy is nonnegative.  Summing (L-33804.9) over consecutive `L`-blocks telescopes exactly to the finite-prefix scattering law of PR #325 `L-32406`.

Thus the neutral principal return has an exact two-frequency local-block realization; it is not merely a diagonal `|phi|=1` statement.

## 5. Q=4 normalization

For `Q=4`,

\[
 a={1\over2},
 \qquad
 b={\sqrt3\over2},
 \qquad
 L=\log4,
\]

and the unnormalized Euler factor is

\[
 E_4(1/2+z)=2\phi(z).
\]

Hence for any input `f`,

\[
 \boxed{
 4\mathcal B_I(f)-\mathcal B_I(E_4f)
 =4[\mathcal B_I(x)-\mathcal B_{I-L}(x)].
 }
 \tag{L-33804.11}
\]

This identity explains the distinguished constant `4` in Q=4 physical-current reconnaissance: at the complete two-frequency level, the failure of the source factor to have squared modulus exactly four inside one local block is **only** the signed difference of one explicit positive scattering-state energy across adjacent blocks.

Equation (L-33804.11) does not imply the discovery inequality `|Q_4|^2<=4S_4`; the arithmetic logarithmic current still has to be controlled.  It does prove that no additional same-scale off-diagonal source defect is hidden in the Euler–Blaschke factor.

## 6. Interaction with the reflected Selberg block

PR #241 `L-9518` requires the block kernel `Phi_I(t-u)` precisely because a localized physical energy uses independent frequencies.  Equation (L-33804.7) shows that the Q=4 neutral filter is compatible with that orientation without approximation:

```text
independent-frequency Q=4 source product
= identity source product
  - one state transfer on the current block
  + the same state transfer on the preceding log4 block.
```

Therefore any future source-bound reflected estimate may move the Q=4 all-pass factors through the complete bireflected block at the exact cost of one telescoping nonnegative state, rather than estimating their off-diagonal product by absolute values.

## 7. What this closes

Closed exactly:

1. the polarized Euler–Blaschke defect;
2. its factorization through the causal state transfer;
3. compatibility with the independent-frequency block kernel;
4. exact current-block / preceding-block state telescope;
5. the Q=4 factor-four normalization;
6. equivalence with the time-domain scattering conservation law.

## 8. What remains open

This theorem does **not** prove:

1. an RH-scale estimate for the Q=4 logarithmic current;
2. the discovery inequality `|Q_4^phys|^2<=4S_4`;
3. a source-bound sign for the Jordan product curvature;
4. the final coefficient-one Hermitian recurrence;
5. RH.

Its role is to remove the neutral source factor itself from the list of unidentified two-frequency cross terms.  The surviving obstruction is arithmetic and source-coupled, not an all-pass localization artifact.
