# R-91001 — One-sided amplifier contraction does not close the completed contour

Claim ID: `R-91001`  
Title: Exponential decay of the fractional-part amplifier on a right Euler line cannot by itself bound the completed zero moment, because the functional-equation reflection introduces the uncontrolled factor `A(1-s)^r` or an equivalent critical-line boundary  
Status: **PROPOSED COMPLETE EXACT SCOPE FIREWALL — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-12  
Dependencies: `L-91001/L-91002`; the functional equation of xi  
Scope: rules out a tempting contour shortcut; it does not refute the fractional-part amplifier programme

## 1. The tempting but invalid inference

`L-91002` proves

\[
\sup_{t\in\mathbb R}|A(3+it)|<\frac34.
\tag{R-91001.1}
\]

It is tempting to combine (R-91001.1) with a completed-log-derivative contour and conclude that every weighted power sum of `A(rho)` decays exponentially.

That conclusion would contradict the known critical-line zeros, whose amplifier values have modulus one. The missing term is the functional-equation reflection.

## 2. Symmetric completed multipliers

Write

\[
\mathcal X(s)=\frac{\xi'}{\xi}(s).
\]

The functional equation gives

\[
\boxed{
\mathcal X(1-s)=-\mathcal X(s).
}
\tag{R-91001.2}
\]

A global analytic multiplier suitable for a symmetric completed contour must retain both sides. The natural symmetric power multiplier is

\[
\boxed{
M_r(s)=A(s)^r+A(1-s)^r.
}
\tag{R-91001.3}
\]

On the right safe line `Re s=3`, the first term is exponentially small by (R-91001.1), but the second is

\[
A(-2-it)^r,
\tag{R-91001.4}
\]

which has no such bound and is not represented by the positive right-half-plane fractional-part Laplace kernel.

Therefore the symmetric contour has not been controlled.

## 3. Half-strip formulation has the same obstruction

One may instead shift only the right half-strip, from `Re s=1/2` to `Re s=3`. For a decaying symmetric weight `W`, the residue theorem has the schematic exact form

\[
\sum_{\operatorname{Re}\rho>1/2}
 W(\rho)A(\rho)^r
=
\frac1{2\pi i}
\left[
\int_{(3)}WA^r\mathcal X\,ds
-
\int_{(1/2)}WA^r\mathcal X\,ds
\right].
\tag{R-91001.5}
\]

The first integral decays like `(3/4)^r`. The second is a genuine critical-boundary integral. Away from zero ordinates, `X(1/2+it)` is purely imaginary, but `A(1/2+it)` is not of unit modulus in general. Consequently the boundary integral is not bounded by the unit-modulus zero residues and cannot be discarded by taking a real or imaginary part.

Thus the one-sided and symmetric formulations contain the same unresolved quantity in different coordinates:

```text
symmetric contour:
    reflected power A(1-s)^r on the right safe line;

half-strip contour:
    critical-line boundary integral of A(s)^r xi'/xi(s).
```

## 4. Piecewise reflected multipliers do not evade the boundary

A second tempting construction uses `A(s)^r` on the right half-strip and `A(1-s)^r` on the left half-strip. Both outer safe lines then contain the contracting multiplier `A(3+it)^r` after reflection.

However the two functions are not one global analytic multiplier. Adding the two half-strip residue equations retains the jump

\[
A(1/2-it)^r-A(1/2+it)^r
\tag{R-91001.6}
\]

on the critical boundary. Any linear combination that cancels this jump also cancels the conjugation-symmetric right-zero moment itself. The apparent safe-line-only identity is therefore tautological, not a zero-exclusion theorem.

## 5. Relation to the repository firewalls

This is the nonlinear counterpart of several existing exact no-go results:

- critical-line all-pass behaviour does not give strip contraction;
- a source-blind multiplier norm is bounded below by its value at an off-line coordinate;
- positive or decaying one-sided Euler data do not automatically control the reflected completed form.

A valid fractional-part/Li proof must add one genuinely new ingredient controlling the boundary jump, for example:

1. a phase-locked reflected identity;
2. a positive canonical-system representation of the boundary moment;
3. a finite-compression inequality that prices the jump without absolute values;
4. a moving-order mechanism that makes the jump itself a lower-order state.

## 6. Proof boundary

Established here:

1. the exact reflected multiplier forced by the functional equation;
2. failure of the right-line contraction to control that multiplier;
3. the equivalent half-strip critical-boundary term;
4. the failure of piecewise analytic gluing as a shortcut.

Not refuted:

1. the spectral-radius criterion of `L-91001`;
2. the positive fractional-part convolution powers;
3. a future source-specific reflected closure;
4. RH.