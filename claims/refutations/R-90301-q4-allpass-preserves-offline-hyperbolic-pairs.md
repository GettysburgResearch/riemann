# R-90301 — Q4 all-pass filtering preserves every off-line hyperbolic pair

Claim ID: `R-90301`  
Title: The critical Euler–Blaschke all-pass factor is exactly J-unitary on functional-equation pairs, so inertia alone cannot turn the existing Q4 neutral state into an RH proof  
Status: **PROPOSED COMPLETE EXACT SCOPE FIREWALL — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-10  
Dependencies: PR #325 `L-32406`; functional equation pairing  
Scope: exact two-point source algebra; no statement against source-convolved reserve mechanisms

## 1. Normalized Q-factor

For `Q>1`, define

\[
\Phi_Q(s)
=Q^{-1/2}\frac{1-Q^{1-s}}{1-Q^{-s}}.
\tag{R-90301.1}
\]

Put `x=Q^s`.  Then

\[
\Phi_Q(s)
=Q^{-1/2}\frac{x-Q}{x-1},
\]

while

\[
\Phi_Q(1-s)
=Q^{1/2}\frac{x-1}{x-Q}.
\]

Therefore, wherever both sides are defined,

\[
\boxed{\Phi_Q(s)\Phi_Q(1-s)=1.}
\tag{R-90301.2}
\]

By continuation this is the exact meromorphic identity.

Since the coefficients are real,

\[
\boxed{
\Phi_Q(1-\bar s)=\frac1{\overline{\Phi_Q(s)}}.
}
\tag{R-90301.3}
\]

On the critical line this specializes to `|Phi_Q|=1`.

## 2. Hyperbolic pair block

An off-line functional-equation pair contributes, in the natural two-coordinate basis, the Hermitian hyperbolic block

\[
J=
\begin{pmatrix}0&1\\1&0\end{pmatrix},
\qquad \operatorname{sig}J=(1,1).
\tag{R-90301.4}
\]

Filter the two paired evaluations by

\[
D(s)=\operatorname{diag}\left(
\Phi_Q(s),\Phi_Q(1-\bar s)
\right).
\]

Using (R-90301.3),

\[
\boxed{D(s)^*J D(s)=J.}
\tag{R-90301.5}
\]

Thus the normalized Euler–Blaschke factor is exactly **J-unitary** on every off-line pair.  It preserves both the hyperbolic signature and the pair form itself.

## 3. Consequence

Claude's 2026 theorem extracts unconditional information precisely because it accepts the off-line `(1,1)` blocks and uses their positive index together with trace/Frobenius information.

A tempting combination with the repository would be:

```text
Q4 all-pass attenuation off the line
+
Claude inertia bookkeeping
-> force the off-line blocks away.
```

Equation (R-90301.5) rejects that shortcut.  On the functional-equation-paired zero side, the all-pass factor by itself does not shrink or rotate the hyperbolic block in the relevant Hermitian geometry at all.

Therefore any genuine Q4 completion must use the **source-convolved Selberg/Jordan reserve, current innovation, or delayed state ledger**.  It cannot obtain RH merely by iterating the critical all-pass factor and recounting inertia.

## 4. What survives

This firewall does not weaken the live Q4 route.  The repository's strongest Q4 work is explicitly not source-blind:

- the true current is placed in the same carry/physical coordinates;
- the radix-four reserve is source-matched and of critical size;
- the compact innovation has a two-tap source;
- reflected product and individual terms are assembled before norms;
- the corrected ledger is two-state.

The appropriate import from Claude is therefore `L-90301`: tolerate a controlled negative spectral mass **after** this source-specific assembly, not before it.

## 5. Proof boundary

Closed exactly:

1. `Phi_Q(s)Phi_Q(1-s)=1`;
2. paired conjugate reciprocal identity;
3. exact preservation of the hyperbolic pair block.

Not claimed:

1. any obstruction to source-convolved Q4 dissipation;
2. any bound on the assembled inertia defect;
3. RH.