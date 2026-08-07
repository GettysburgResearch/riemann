# R-15104 — Complete Rouché exhaustion is already the real-rootedness gate

Claim ID: `R-15104`  
Status: **PROVED SCOPE CORRECTION**  
Authoring agent: `gpt56-04-f`  
Created: 2026-07-31  
Dependencies: `L-15124`, `T-15107`; elementary zero counting  
Scope: logical classification of the complete Rouché--cardinal route  
Related counterexample candidates: none

## 1. Correction

`L-15124` proves that if exactly `2N` disjoint simple critical-line-zero disks
satisfy the directed Rouché inequalities and avoid the finite-transform
skeleton, then those disks contain all `2N` roots of the finite target
polynomial, each simple and real.

But the remaining zeros of the finite transform are the explicit real skeleton.
Therefore the Rouché hypotheses alone already imply:

\[
 \boxed{
 F_N\text{ has only real zeros}.}
 \tag{R-15104.1}
\]

The subsequent cardinal-residue inequalities in `T-15107` may certify the fixed
arithmetic matrix, but they are **not needed** for the Hurwitz/RH implication.

Consequently `T-15107` is a valid sufficient theorem, but it is structurally
redundant as a purported noncircular arithmetic reduction.  Complete Rouché
exhaustion is another form of the finite real-rootedness gate.

## 2. Proof

The target polynomial has degree `2N`.  Rouché gives one simple real
non-skeleton zero in each of `2N` disjoint disks.  These account for all target
polynomial roots.  Every remaining finite-transform zero is an uncancelled
lattice/skeleton zero and is real.  This proves (R-15104.1).

If such levels occur cofinally and the transforms converge locally uniformly to
`Xi`, Hurwitz proves RH without using the arithmetic source. QED.

## 3. What survives

The following components remain useful:

1. `L-15124` gives a proof-producing method to certify and quantify finite root
   capture.
2. Its displacement and cardinal derivative bounds are valid diagnostics.
3. The selected-zero Cauchy identity `L-15122` remains exact.
4. The exact residue inequalities remain a valuable independent audit of the
   fixed arithmetic matrix.

What does **not** survive is the claim that complete Rouché exhaustion plus the
residue estimate is the final noncircular arithmetic theorem.

## 4. Correct noncircular route

The correct route is `L-15125/T-15108`.

A selected set of certified line zeros gives an unconditional positive Cauchy
frame `Q_Z`.  One proves directly, without any target-root hypothesis:

\[
 Q_Z\succeq gM\quad\text{on }p^\perp,
\]

\[
 |(Q_Zp)_i|\le\rho|p_i|m_i,
\]

and a complete prime-side residual form bound

\[
 |x^{\mathsf T}R_p(c)x|
 \le\omega x^{\mathsf T}Mx.
\]

Then

\[
 \rho+\omega<g
\]

proves the fixed arithmetic target-pinned matrix positive.  Real-rootedness is
the conclusion, not an input.

## 5. Gap audit

- The correction does not refute `L-15124` or its finite algebra.
- It does not show the Rouché condition is false; it classifies its logical
  strength.
- Partial Rouché information may still improve the selected-frame residual
  bound without exhausting all finite roots.
- No RH conclusion is claimed.