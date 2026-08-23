# T-105220 — Moving-centre Poisson–Bézout Xi residue frontier

Claim ID: `T-105220`  
Status: **PROPOSED EXACT FINITE LOCALIZATION + UNCONDITIONAL SAFE-LINE INPUTS; correction theorem open**  
Created: 2026-08-23  
Depends on: `L-105220--L-105223`; `R-105220`; PRs #720, #723, #724, #726  
RH status: **unproved**

## 1. What is closed in this checkpoint

The positive localizer

\[
\Omega_a(x)
=
\frac{36}{
((x-a)^2+1)((x-a)^2+4)((x-a)^2+9)
}
\]

has three exact advantages:

1. it uses one positive real-axis weight for count, first residue moment, and
   second residue moment;
2. its boundary functional uses values only at `a+ih`, `h=1,2,3`;
3. all safe points transfer by the functional equation to the absolutely
   convergent half-plane `Re(s)>1`.

At every fixed Xi derivative order the complete safe-line carriers satisfy

\[
\mathcal N_k\asymp\ell,
\qquad
\mathcal A_k\asymp\ell^{-1},
\qquad
\mathcal B_k\asymp\ell^{-3},
\]

and

\[
\boxed{
\mathcal N_k\mathcal B_k-\mathcal A_k^2
=
O_k(\ell^{-4}).
}
\tag{T-105220.1}
\]

Therefore their formal normalized coherence is

\[
1+O_k(\ell^{-2}).
\]

The common Xi anchor `-i` and the fixed-order disk-growth estimate

\[
\log\frac{\max_{|z+i|\le R}|\Xi^{(m)}(z)|}{|\Xi^{(m)}(-i)|}
=
O_m(R\log(R+2))
\]

are also unconditional.

## 2. Exact moving-centre extinction criterion

Let `N_k(a),A_k(a),B_k(a)` denote the actual real-critical moments after the
entire-function passage and all corrections. If

\[
A_k(a)>0
\]

and

\[
\boxed{
\frac{N_k(a)B_k(a)-A_k(a)^2}{B_k(a)}
<
\frac9{25},
}
\tag{T-105220.2}
\]

then there is no wrong extremum of `Xi^(k-1)` in `[a-1,a+1]`.

The formal safe-line defect contributes only `O(ell^-4)`. Thus it is enough
to prove that the exact signed correction combination of `L-105222.7` is

\[
o(\ell^{-3})
\tag{T-105220.3}
\]

uniformly in every sufficiently large real centre. Such a theorem eliminates
all high-ordinate wrong extrema at level `k`; the remaining reverse–Rolle
ledger is compact in height.

Call the uniform correction statement

\[
\boxed{\mathrm{MCRC105220}}
\]

for **moving-centre residue-correction cancellation**.

## 3. Relation to the neighboring programs

- PR #723 supplies exact confluent selectors, shell averaging, Cartan
  allocation, and the sharp finite-event ledger. `L-105223` closes its common
  anchor and generic fixed-order growth input, but not selector-cost
  absorption.
- PR #724 supplies the unconditional exterior-square Xi Gram and a positive
  near-collision expression for residue incoherence. It is a natural candidate
  for controlling the signed correction in `MCRC105220`.
- PR #726 proves summability of the high-derivative coherence tail. Hence a
  proof of `MCRC105220` for the finite low-order prefix would compose with an
  already controlled derivative tail.
- PR #729 supplies a debt-free quotient-algebra spectrum for finite residue
  moments, compatible with the finite Bézout coordinate used here.

The new route therefore does not introduce another detector. It gives a
moving-height local integrality criterion designed to combine the best parts
of the selector, exterior-square, and high-tail programs.

## 4. Exact remaining chain

A complete closure would require

\[
\boxed{
\begin{aligned}
&\text{entire/confluent passage for the multipole identities}\\
&+\ \mathrm{MCRC105220}
+\ \text{finite-height endpoint/winding disposition}\\
&\Longrightarrow
\text{no wrong extrema at every derivative level}\\
&\Longrightarrow
\mathrm{RH}.
\end{aligned}
}
\tag{T-105220.4}
\]

The first line is not yet proved. In particular, the exact rational firewall
`R-105220` forbids dropping the correction terms.

## 5. Scientific boundary

```text
positive three-height localizer            PROVED EXACT FINITE
value-only moment boundary formulas        PROVED EXACT FINITE
safe-line carrier main terms               PROPOSED UNCONDITIONAL
formal coherence defect O(log^-4)          PROVED ALGEBRAICALLY
weighted unit-interval extinction          PROVED EXACT
common Xi derivative anchor                PROPOSED UNCONDITIONAL
fixed-order Xi disk growth                 PROPOSED UNCONDITIONAL
MCRC105220 correction cancellation         OPEN / RH-BEARING
finite-height last-defect disposition      OPEN / RH-BEARING
Riemann Hypothesis                         UNPROVED
```
