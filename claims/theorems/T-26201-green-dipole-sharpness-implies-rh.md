# T-26201 — Green–dipole carry sharpness implies RH

Claim ID: `T-26201`  
Title: A subpower obstacle debt for the canonical parabolic Green state gives the critical prime-ramp lower bound and excludes every off-line zero  
Status: **PROPOSED — COMPLETE COMPOSITION THEOREM PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-08  
Issue: #260  
Dependencies: `L-24502`, `T-24504`, `L-26201`, `L-26202`, `L-26203`  
Scope: finite-to-global deduction; the Green–dipole sharpness estimate is the load-bearing proposed theorem

## 1. Green–dipole sharpness

For each integer `X>=2`, construct:

1. the parabolic seed `b_X^(0)` of `L-26203`;
2. the canonical exact Green equality state `b_X^star`;
3. its clipped nonnegative state
   \[
   b_X^\circ=(b_X^\star)_+;
   \]
4. the complete signed residual
   \[
   \varepsilon_X(q)=v_q(b_X^\circ)-w_X(q);
   \]
5. the weighted positive residual
   \[
   D_X^+=\sum_{q=p^a\le X}\Lambda(q)(\varepsilon_X(q))_+;
   \]
6. the explicit lower certificate
   \[
   \mathcal L_X^{\rm GS}=J_X(b_X^\circ)-D_X^+.
   \]

The **Green–Dipole Sharpness theorem**, abbreviated `GDS`, is

\[
\boxed{
\mathcal L_X^{\rm GS}
\ge
J_X(b_X^{(0)})-X^{o(1)}.
}
\tag{T-26201.1}
\]

Equivalently, for every `epsilon>0` there is `C_epsilon` such that

\[
J_X(b_X^{(0)})-\mathcal L_X^{\rm GS}
\le C_\varepsilon X^\varepsilon
\tag{T-26201.2}
\]

for every sufficiently large `X`.

A stronger review target is the finite inequality

\[
\mathcal L_X^{\rm GS}\ge J_X(b_X^{(0)})
\tag{T-26201.3}
\]

at every endpoint. It is supported by reconnaissance but is not assumed in the
composition.

The prefix-contact certificate of `L-26202` may replace the clipped certificate
provided it satisfies the same lower bound.

## 2. Prime-ramp lower bound

The exact clipped dipole identity gives

\[
\mathcal L_X^{\rm GS}
\le
\mathcal P(X)
=
\sum_{q=p^a\le X}
 \frac{\Lambda(q)}{\sqrt q}\log\frac Xq.
\tag{T-26201.4}
\]

The seed estimate is

\[
J_X(b_X^{(0)})
\ge4\sqrt X-C_0\log(2X).
\tag{T-26201.5}
\]

Combining (T-26201.1), (T-26201.4), and (T-26201.5) yields

\[
\boxed{
\mathcal P(X)
\ge4\sqrt X-X^{o(1)}.
}
\tag{T-26201.6}
\]

No prime asymptotic is used in this finite implication. All arithmetic input is
inside the prime-power incidence manifest defining the Green state.

## 3. Transfer to RH

`T-24504` records the reviewed square-screw/Landau transfer

\[
\boxed{
\mathrm{RH}
\iff
\mathcal P(X)\ge4\sqrt X-O_\varepsilon(X^\varepsilon)
\quad\text{for every }\varepsilon>0.
}
\tag{T-26201.7}
\]

For completeness, at square scale `X=N^2` the exact screw formula writes

\[
\Psi(2\log N)
=
4(N+N^{-1}-2)
-\mathcal P(N^2)
+O(\log N).
\tag{T-26201.8}
\]

Equation (T-26201.6) gives a subpolynomial upper envelope for this screw
function on the critical square mesh. The unconditional derivative budget
propagates the envelope between adjacent samples. The sign-oriented Landau
continuation theorem then excludes every pole of the completed logarithmic
derivative in `Re(s)>1/2`. Functional-equation symmetry gives

\[
\boxed{\mathrm{RH}.}
\tag{T-26201.9}
\]

A reviewer may instead use the equivalent Lagarias harmonic-divisor conclusion
in `T-24504`.

## 4. Exact finite certificate variant

A cofinal family of proof objects may establish (T-26201.2) directly. At level
`X`, the consumer verifies:

\[
\mathcal L_X^{\rm GS}
\ge
J_X(b_X^{(0)})-R_X
\]

with a directed rational `R_X`. If the producer also supplies an explicit
envelope

\[
R_X\le C_\varepsilon X^\varepsilon
\]

for every fixed `epsilon>0`, then (T-26201.1) follows.

Finite success at any bounded list of endpoints is not a proof of the cofinal
envelope.

## 5. Why this is not another generic sandwich hypothesis

The theorem does not postulate an arbitrary pair of nonnegative carry vectors.
Both sides are generated canonically from one signed exact state:

```text
parabolic seed
-> endpoint-projected Green equality
-> one physical positive-cone clipping
-> one fully recombined signed dipole residual
-> exact lower certificate.
```

The unproved inequality is a source-specific obstacle comparison for this
single construction. It is weaker than pointwise Carry Saturation, weaker than
positivity of the exact inverse, and does not bound the macroscopic positive and
negative seed residuals separately.

## 6. Proof boundary

Complete, subject to review of imported normalizations:

\[
\mathrm{GDS}
\Longrightarrow
\text{critical prime-ramp lower bound}
\Longrightarrow
\mathrm{RH}.
\]

Not proved here:

\[
\boxed{\mathrm{GDS}.}
\]

Accordingly RH is not claimed proved by this file.
