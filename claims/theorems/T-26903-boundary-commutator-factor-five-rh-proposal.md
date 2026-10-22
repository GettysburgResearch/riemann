# T-26903 — Boundary-commutator factor-five proposal for RH

Claim ID: `T-26903`  
Title: A boundary-preserving factor-five commutator recurrence for the parity-paired source implies the Riemann Hypothesis  
Status: **CORRECTED CONSOLIDATED FULL CONDITIONAL PROPOSAL — ONE BOUNDARY-COMMUTATOR THEOREM OPEN**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-08  
Supersedes: the direct bulk physical-to-carry formulation in `T-26902.11`  
Depends on: `T-26902` Sections 1--10 and 12--14; `R-26902`; `M-26903`  
Scope: corrected final theorem after the exact carry-window pole-cancellation audit; RH is not claimed proved

## 1. Retained source/carry package

The following parts of `T-26902` are retained without change:

```text
correct independent-frequency physical block
fixed RH-bearing omega_2 source
stable dyadic and fixed-ratio filters
pointwise compact carry wavelet
factor-five localization of every negative Kummer row
positive inverse and generalized-prime coefficients
positive full wavelet synthesis
uniform carry-space Schur reserve
zero/first/second Selberg-carry moment tower
bottom-charge, DSS, shell, and first-cell RH consumers
```

In particular, every potentially negative carry/Kummer transition lies in

\[
2m\le n<5m,
\tag{T-26903.1}
\]

and the generalized-prime carry profile has a uniform strict reserve on every sufficiently large row.

## 2. Exact scope correction

`R-26902` proves that the atomized carry window

\[
H_\theta(u)=e^{-u/2}C(e^u,\theta)
\]

has transform

\[
\widehat H_\theta(z)
=\frac{\zeta(z+1/2)}{z+1/2}
\left[1-\theta^{z+1/2}-(1-\theta)^{z+1/2}\right].
\tag{T-26903.2}
\]

Thus every direct carry-window analysis channel vanishes at every zeta zero. Multiplying the generalized-prime pole by this window cancels it exactly.

Consequently the following former interpretation is withdrawn:

```text
same-scale carry Gram coercivity
-> same-scale RH-sensitive physical coercivity.
```

No direct reverse frame inequality from a zeta-safe physical source to the pure carry-window bank can hold across an off-line zero.

The carry algebra remains useful only for the transverse transition sector. The RH-sensitive boundary/commutator coordinate must be retained separately.

## 3. The surviving RH-bearing boundary

`L-26904` proves

\[
\sum_m a_\omega(m)Z_{n,m}(j)=0,
\tag{T-26903.3}
\]

\[
\sum_m a_\omega(m)\log m\,Z_{n,m}(j)\ge0,
\tag{T-26903.4}
\]

and

\[
\sum_m a_\omega(m)(\log m)^2Z_{n,m}(j)\ge0.
\tag{T-26903.5}
\]

The unit source is absent from (T-26903.4)--(T-26903.5) because \(\log1=0\). It survives instead as the bottom charge

\[
\boxed{
5c_X(2)+3c_X(3)=-6\mathcal R_\omega(X).
}
\tag{T-26903.6}
\]

and as the coherent fixed-ratio Mertens cell.

This is the boundary coordinate that the pure carry bank cancels in transform space.

## 4. Correct final object — `BCF5TC`

A **Boundary-Commutator Factor-Five Transition Certificate** consists of four source-bound objects for every sufficiently large physical block:

```text
P_J       projection onto the direct carry-window span;
B_J       complementary physical boundary/commutator map;
S_J       map from the transverse physical transition sector to the carry Gram;
L_J       declared strict lower-scale destination map.
```

They must form an exact source decomposition

\[
\boxed{
I=P_J+B_J
}
\tag{T-26903.7}
\]

on the complete parity-paired \(\omega_2\) source manifest, with no source atom omitted or duplicated.

The direct carry component \(P_J\) may be used only for the pole-canceling transverse sector. The boundary component \(B_J\) must retain:

1. the \(m=1\) source;
2. every finite parity/Bezout delay;
3. all independent-frequency translate cross terms;
4. every quotient-cell endpoint and cutoff commutator;
5. the bottom charges \(2,3\);
6. the dyadic and \(2/3\) Mertens projections.

## 5. Transverse factor-five estimate

On the transition rows (T-26903.1), the certificate must prove

\[
\boxed{
S_J^*G^{\rm car}_{J}S_J
\preceq C_J P_J^*G^{\rm phys}_{J}P_J
}
\tag{T-26903.8}
\]

and transfer the carry Schur reserve back to the **transverse** physical sector:

\[
\boxed{
P_J^*G^{\rm phys}_{J,\rm res}P_J
\preceq C'_J S_J^*G^{\rm car}_{J,\rm res}S_J
+G^{\rm lower}_{J}.
}
\tag{T-26903.9}
\]

Because the transverse carry windows are RH-blind, these inequalities are not themselves a pole-exclusion theorem. Their role is only to pay every transition component orthogonal to the boundary source.

The allowed condition numbers must be uniform, polylogarithmic, or have explicitly vanishing logarithmic exponent.

## 6. Boundary-commutator recurrence

The load-bearing theorem is the source-specific estimate

\[
\boxed{
E_B(J)
\le C(1+J)^A
+\sum_\beta\vartheta_\beta E_B(J_\beta),
}
\tag{T-26903.10}
\]

where

\[
J_\beta\le J-\delta
\qquad\text{and}\qquad
\sum_\beta\vartheta_\beta\le1,
\tag{T-26903.11}
\]

or the stronger strict-contraction version with total coefficient below one.

Here \(E_B\) is the norm of the exact physical boundary/commutator coordinate, not the carry output.

An equivalent accepted scalar form is

\[
\boxed{
|\mathcal R_\omega(X)|
\le C\log^A(2X)
+\sum_\beta\vartheta_\beta
|\mathcal R_\omega(Y_\beta)|,
}
\tag{T-26903.12}
\]

with

\[
Y_\beta\le X^{1-\delta}.
\]

Every term connecting (T-26903.10) or (T-26903.12) to the transverse factor-five estimate must be written explicitly. A statement that the boundary is “finite” is insufficient: its arithmetic coefficient remains cofinal.

## 7. Required physical Schur complement

After the transverse carry sector and lower-scale destinations are isolated, the remaining independent-frequency matrix must be written in the block form

\[
\begin{pmatrix}
G_B&C^*\\
C&D
\end{pmatrix},
\qquad D\succ0.
\tag{T-26903.13}
\]

The certificate must prove

\[
\boxed{
G_B-C^*D^{-1}C
\succeq\kappa_J G_{B,\rm source}
}
\tag{T-26903.14}
\]

with a recurrence-compatible \(\kappa_J\).

Unlike the refuted direct carry transference, this Schur complement is taken **before** the common zeta factor is introduced. It acts on the parity-paired physical source and its boundary commutator.

A calculation which first passes entirely into the carry-window bank has already canceled the pole and cannot establish (T-26903.14).

## 8. Finite boundary obligations

The production object must include exact tables or symbolic families for:

```text
all n<210 rows
all quotient cells 2,3,4
all carry-window jump coincidences
all noncoprime chains
all compact-window support endpoints
all parity/Bezout delay endpoints
all m=1 contributions
all bottom-charge injections
```

The finite row threshold does not make the arithmetic source finite in scale. Every source coefficient and scale label must remain in the manifest.

## 9. Conditional completion

Assume `BCF5TC` and either recurrence (T-26903.10) or (T-26903.12).

Scale induction gives

\[
E_B(J)=e^{o(J)}
\]

or

\[
\mathcal R_\omega(X)=O_\varepsilon(X^\varepsilon).
\]

The source transform contains

\[
\frac{(1-2^{-s})(1-2^{-s-1})}{\zeta(s)},
\]

and the boundary map is required to retain this numerator without the carry-window zeta cancellation. Therefore a zero \(\rho\) with \(\Re\rho>1/2\) creates a genuine pole in the normally convergent half-plane, a contradiction.

Functional-equation symmetry gives

\[
\boxed{\mathrm{BCF5TC}\Longrightarrow\mathrm{RH}.}
\tag{T-26903.15}
\]

## 10. Exact status

Complete, subject to review:

```text
source and filter algebra
parity-paired reconstruction
factor-five carry localization
positive generalized-prime synthesis
uniform carry-space reserve
Selberg-carry moment tower
carry-window pole-cancellation refutation
bottom-charge and fixed-ratio consumers
conditional boundary recurrence -> RH
```

Open:

```text
exact boundary/transverse decomposition P_J+B_J
independent-frequency boundary commutator matrix
transverse physical/carry map S_J
boundary Schur reserve before zeta cancellation
lower-scale boundary or bottom-charge recurrence
```

This corrected proposal is sharply reviewable but remains gap-blocked at `BCF5TC`. RH is unproved.
