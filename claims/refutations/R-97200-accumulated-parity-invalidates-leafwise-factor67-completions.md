# R-97200 — Accumulated parity invalidates the leafwise factor-67 completions

Claim ID: `R-97200`  
Status: **PROVED EXACT COMPOSITIONAL REFUTATION**  
Created: 2026-08-17  
Frozen inputs: PR #555 at `341697b4694ba7f44f2ba2be73cb3fc982939412`; PR #556 at `a4feca0457d310c72054f274040f93b0503f658b`; PR #559 at `88d97adef8a42c5baf2f52c2c259a4ef536bdfdd`; binding audit PR #561 at `db9bdc63c855c6ddf664b763d748f8155a6a2c67`  
RH status: **unproved**

## 1. The parity action

For a paired source `P=(E,O)`, let

\[
S(E,O)=(O,E),
\qquad
\mathcal O(P)=R(E)-R(O).
\]

Every rough-prime placement swaps the two channels once. Therefore a rough
history \(h=(p_1,\ldots,p_m)\) satisfies the exact identity

\[
\boxed{\mathcal O(S^mP)=(-1)^m\mathcal O(P).}
\tag{R-97200.1}
\]

The placement preserves the physical activation and coefficient magnitude,

\[
\frac{X/p}{k/p}=\frac Xk,
\qquad
p^{-1/2}(k/p)^{-1/2}=k^{-1/2},
\tag{R-97200.2}
\]

but not the signed orientation.

## 2. Why a positive scalar does not repair the swap

Let \(L\) be any fixed linear combination of component-row observations. In
particular this includes the unique scalar used by PR #559,

\[
L(P)=5R_2(P)+3R_3(P).
\]

Linearity commutes with the channel swap, hence

\[
\boxed{L(S^mP)=(-1)^mL(P).}
\tag{R-97200.3}
\]

Thus replacing two rows by one positive scalar does not erase accumulated
parity. A canonical leaf with \(L(P)>0\) becomes negative after an odd history.
The leafwise completion asserted in PR #559 is therefore not a valid successor
to PR #561.

## 3. The exact hostile leaf

PR #561 gives the frozen directed witness

```text
X=67*71*13=61841,
history=(67),
terminal=(p,y)=(71,13),
E_T(71,13)-O_T(71,13)>17.
```

The history is odd, so the incoming leaf requires the reverse Target-Lorenz
orientation. The strict margin rules that out. This refutes the gluing
interface of PR #555, not native-row nonnegativity itself.

## 4. Grouping the finite colours is necessary but not sufficient

PR #556 correctly keeps the complete `d|P_61` annular reserve grouped until its
terminal inequality. That repairs the false promotion of individual finite
colours. It does not repair (R-97200.1): the entire grouped observation is still
multiplied by \((-1)^m\) after a rough history of length \(m\).

Consequently the following dispositions are binding:

```text
PR #555 finite stopping depth                     retained algebraically
PR #555 parity-blind terminal realization         refuted
PR #556 scale-four quadrature                      retained
PR #556 grouped P61 reserve                        retained in grouped scope
PR #556 parity-blind root promotion                refuted
PR #559 5:3 scalar and zero-safe numerator         retained
PR #559 leafwise scalar factor-67 completion       refuted
```

A valid successor must either carry the cumulative parity through one global
source problem, or change the physical source so that the finite colours are
not signed terminal objects. The later claims in T-97200 do both: they flatten
the rough histories exactly and, in the new consumer, leave every prime below
67 inside a positive source rather than treating it as a colour.
