# M-26903 — Review protocol for the boundary-commutator factor-five theorem

Claim ID: `M-26903`  
Title: Fail-closed production and adversarial-review contract after the carry-window pole-cancellation refutation  
Status: **METHODOLOGY / REQUIRED `BCF5TC` CERTIFICATE CONTRACT**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-08  
Depends on: `R-26902`, `T-26903`, `M-26902` Parts A--C  
Scope: final theorem review only; no estimate or RH conclusion

## 1. Corrected review boundary

`M-26902` Parts A--C remain the frozen review protocol for the physical normalization, source/carry algebra, parity frame, and scalar consumers.

`R-26902` changes Part D:

```text
old target:
  direct bulk physical-to-carry Gram equivalence;

correct target:
  physical boundary/transverse decomposition,
  carry control only on the transverse sector,
  independent boundary Schur reserve before zeta cancellation,
  explicit lower-scale boundary recurrence.
```

A production object which maps the entire RH-sensitive source into pure carry windows fails by exact transform algebra.

## 2. Required exact decomposition

For each block and transition type, emit matrices or maps

```text
P     direct carry-window projection
B     physical boundary/commutator projection
S     transverse physical-to-carry map
L     lower-scale destination map
```

and prove on the complete source manifest

\[
I=P+B.
\tag{M-26903.1}
\]

The decomposition must be exact before interval enlargement, norm bounds, positive parts, or Schur elimination.

The `B` manifest must contain every source atom whose pole information is lost by `P`, including:

```text
m=1 source
bottom charges 2,3
parity and Bezout endpoints
window support endpoints
quotient-cell boundary commutators
cutoff and noncoprime corrections
fixed-ratio Mertens projection
```

## 3. Pole-audit table

For every analysis window or output channel, record its transform as

```text
zeta factor
Euler numerator
rational/differential factor
compact-window factor
boundary factor
```

and classify its behavior at a hypothetical zeta zero:

```text
POLE_RETAINED
POLE_CANCELED
BOUNDARY_REINJECTED
LOWER_SCALE_ROUTED
```

No source coordinate may disappear without one of these declarations.

In particular:

```text
atomized carry H_theta                  POLE_CANCELED
compact omega carry Z_theta             POLE_CANCELED
pure carry Gram                         POLE_CANCELED
parity-paired physical source           POLE_RETAINED
m=1/bottom boundary                     POLE_RETAINED
```

## 4. Transverse carry certificate

Only the `P` sector may be mapped to carry space. The producer must prove

\[
S^*G_{\rm car}S\preceq C P^*G_{\rm phys}P
\tag{M-26903.2}
\]

and a reserve-return inequality

\[
P^*G_{\rm phys,res}P
\preceq C'S^*G_{\rm car,res}S+G_{\rm lower}.
\tag{M-26903.3}
\]

The carry reserve imported from `L-26902/L-26903` must be applied to the complete positive synthesis. Dropping off-diagonal wavelet cross terms is not allowed.

The direct carry channels may not be used to claim pole exclusion.

## 5. Boundary physical matrix

Construct the independent-frequency boundary matrix from PR #241 before passing to any carry coordinate. Include:

1. both frequency legs;
2. all dyadic translate channels;
3. both parity channels;
4. all finite Bezout delays;
5. the `omega_2` synthesis;
6. all endpoint/cutoff commutators;
7. the `m=1` source.

The final matrix must be displayed as

\[
\begin{pmatrix}
G_B&C^*\\
C&D
\end{pmatrix},
\qquad D\succ0,
\tag{M-26903.4}
\]

and its Schur complement must satisfy

\[
G_B-C^*D^{-1}C\succeq\kappa G_{B,\rm source}.
\tag{M-26903.5}
\]

A reserve computed after multiplying by an atomized carry window is invalid because the pole has already canceled.

## 6. Boundary recurrence

The certificate must finish with an exact recurrence for one declared RH-bearing scalar or energy.

Accepted forms:

### Physical boundary energy

\[
E_B(J)
\le C(1+J)^A
+\sum_\beta\vartheta_\beta E_B(J_\beta),
\quad
J_\beta\le J-\delta,
\quad
\sum_\beta\vartheta_\beta\le1.
\tag{M-26903.6}
\]

### Bottom charge

\[
|\mathcal R_\omega(X)|
\le C\log^A(2X)
+\sum_\beta\vartheta_\beta
|\mathcal R_\omega(Y_\beta)|,
\quad
Y_\beta\le X^{1-\delta}.
\tag{M-26903.7}
\]

### Dyadic signed slack

The analogous recurrence for `Pi_2`, with the exact stable filter back to `omega_2` and the first-cell mutation displayed.

Every coefficient, child scale, and boundary forcing term must be written. “Finite boundary” is not a recurrence.

## 7. Required finite tables

The proof object must contain exact source/matrix rows for:

```text
n<210
quotient cells 2,3,4
all theta/carry-window jump coincidences
all parity/Bezout endpoint coincidences
all noncoprime chains
all support truncations
all bottom-charge injections
```

A finite row list may still have cofinal arithmetic scale. Coefficients and destinations must be symbolic or certified uniformly in the block parameter.

## 8. Mandatory rejection mutations

The production verifier must reject:

```text
B01 map the complete source into pure carry windows
B02 remove the zeta factor from H_theta
B03 treat Z_theta as an RH-sensitive window
B04 omit the m=1 source
B05 omit either bottom charge
B06 omit a parity channel
B07 omit a Bezout delay
B08 omit an independent-frequency cross term
B09 compute the Schur reserve after carry pole cancellation
B10 return the complete boundary energy to the forcing side
B11 use a same-scale carry reserve as the final pole exclusion
B12 omit the finite n<210 table
B13 omit a quotient-cell endpoint or cutoff commutator
B14 use a fixed power condition-number loss
B15 route a child above the declared lower scale
B16 fail the dyadic-shell inversion
B17 fail the 2/3 Mertens mutation
B18 replace the cofinal recurrence by finite computation
```

## 9. Verdict table

Review the final theorem with separate rows:

```text
exact P+B decomposition                 VERIFIED / FALSE / UNPROVEN
pole-audit table                        VERIFIED / FALSE / UNPROVEN
transverse source manifest              VERIFIED / FALSE / UNPROVEN
transverse physical/carry map S         VERIFIED / FALSE / UNPROVEN
carry reserve on complete synthesis     VERIFIED / FALSE / UNPROVEN
boundary physical matrix                VERIFIED / FALSE / UNPROVEN
boundary Schur complement               VERIFIED / FALSE / UNPROVEN
finite boundary tables                  VERIFIED / FALSE / UNPROVEN
lower-scale recurrence                  VERIFIED / FALSE / UNPROVEN
first-cell mutation                     VERIFIED / FALSE / UNPROVEN
RH conclusion                           only if every prior row verifies
```

A failed direct bulk map is already classified by `R-26902` and may not be revived by changing notation.

## 10. Current status

```text
source/carry/parity package              PROPOSED COMPLETE PENDING REVIEW
carry-window pole-cancellation no-go     PROPOSED COMPLETE EXACT
boundary/transverse decomposition        NOT EMITTED
boundary physical matrix                 NOT EMITTED
boundary Schur reserve                   OPEN
boundary recurrence                      OPEN
Riemann Hypothesis                       UNPROVED
```
