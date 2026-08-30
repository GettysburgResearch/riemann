# R-32701 — Real zeros of the semilocal characteristic function do not imply positivity of the original Weil form

Claim ID: `R-32701`  
Title: The Connes–van Suijlekom/CCM real-zero mechanism uses the shifted form `Q-epsilon_min I`; the sign of the omitted ground scalar is exactly the positivity question  
Status: **PROPOSED COMPLETE SCOPE REFUTATION / EXTERNAL-PROOF FIREWALL — independent review requested**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-08  
Primary sources: Connes–van Suijlekom, *Quadratic Forms, Real Zeros and Echoes of the Spectral Action*, arXiv:2511.23257; Connes–Consani–Moscovici, *Zeta Spectral Triples*, arXiv:2511.22755  
External claim audited at advertised-chain scope: C. F. Viceré, *A Proof of the Riemann Hypothesis for the Riemann Zeta Function: Weil Positivity via Semilocal Spectral Descent*, Zenodo 19546495 (2026)  
Scope: refutes the inference `semilocal real-zero spectrum => unshifted Weil positivity` unless a separate nonnegative-ground theorem is supplied; it does not adjudicate uninspected arguments in the external PDF

## 1. What the cited real-zero theorem actually says

Connes–van Suijlekom prove a real-zero theorem for a real quadratic form whose lowest spectral value `epsilon` is a simple isolated eigenvalue with even eigenfunction `xi`. The positivity used in the proof is the positivity of the **shifted** form

\[
\boxed{Q-\epsilon\langle\cdot,\cdot\rangle\ge0,}
\tag{R-32701.1}
\]

which is automatic from the definition of the lowest eigenvalue. Their theorem does not assume, and therefore cannot by itself conclude,

\[
\epsilon\ge0.
\tag{R-32701.2}
\]

In the zeta specialization, CCM make this shift completely explicit. If `epsilon_N` is the smallest eigenvalue of the finite restriction `QW_lambda^N`, their self-adjoint rank-one operator is constructed on the quotient using the inner product induced by

\[
\boxed{
QW_\lambda^N-\epsilon_N\langle\cdot,\cdot\rangle.
}
\tag{R-32701.3}
\]

Under the stated simple-even hypothesis, the Fourier transform of the minimizing eigenvector has only real zeros. No sign assumption on `epsilon_N` appears in this real-zero conclusion.

## 2. Elementary finite-dimensional countermodel to the inference

Let

\[
Q=\begin{pmatrix}-1&0\\0&2\end{pmatrix}.
\tag{R-32701.4}
\]

Its lowest eigenvalue is the simple value

\[
\epsilon=-1,
\]

and

\[
Q-\epsilon I
=\begin{pmatrix}0&0\\0&3\end{pmatrix}\ge0.
\tag{R-32701.5}
\]

Any Carathéodory–Fejér or self-adjoint-extension argument applied to the shifted positive form can have the advertised real-zero spectral conclusion while the original form remains strictly negative on the ground vector.

Thus the logical implication

```text
shifted characteristic function has only real zeros
=> original quadratic form is nonnegative
```

is false even before arithmetic enters.

## 3. Exact zeta/Weil consequence

For the localized Weil form,

\[
QW_\lambda^N\ge0
\quad\Longleftrightarrow\quad
\epsilon_N\ge0
\tag{R-32701.6}
\]

at finite matrix level. In the continuum localized form, the analogous scalar is the lowest spectral value `lambda_a`; global nonnegativity for all supports is Weil's RH criterion.

Therefore any proof chain of the form

```text
finite/semilocal spectral reality
-> sum-of-squares representation
-> Weil positivity
```

must retain the ground scalar explicitly. The most it obtains automatically is

\[
QW_\lambda^N(f)
=\epsilon_N\|P_{\rm ground}f\|^2
 +\underbrace{(QW_\lambda^N-\epsilon_N I)(f)}_{\ge0}.
\tag{R-32701.7}
\]

The first term has unknown sign until `epsilon_N>=0` is independently proved.

## 4. Application to the advertised semilocal proof chain

The public description of the Viceré preprint states the chain

```text
(T1) semilocal spectral reality;
(T2) arithmetic-spectral identity converts to a sum of squares >=0;
(T3) compact-support form stability;
(T4) Weil convergence;
(T5) Weil criterion.
```

It attributes T1 to the Connes–van Suijlekom real-zero theorem / CCM semilocal spectral operators.

The cited theorems do **not** license the inference that the unshifted semilocal Weil form is nonnegative: they allow a negative lowest eigenvalue and shift it away before forming the positive quotient metric.

Consequently the advertised T1→T2 inference is incomplete **unless the preprint contains an additional independent proof that the relevant lowest eigenvalue is nonnegative at every semilocal cutoff** and carries that scalar through its arithmetic-spectral identity.

This file does not claim that no such additional argument occurs somewhere in the PDF; the PDF itself was not source-line audited here. It establishes the exact burden that any such argument must meet and rejects any use of the cited real-zero theorem alone as a positivity theorem.

## 5. Relation to repo firewalls

This is the same scalar obstruction already encountered internally:

- `R-19846`: an off-line Xi-cardinal direction obstructs a cofinal affine ground gate;
- `L-32703`: a Suzuki admissible shift tending to zero is equivalent to global Weil positivity;
- current lemma: CvS/CCM real-zero localization shifts by the unknown lowest eigenvalue and therefore cannot certify its sign.

The repeated structural message is

\[
\boxed{
\text{real-zero finite spectral geometry}
\neq
\text{positivity of the unshifted Weil ground scalar}.}
\tag{R-32701.8}
\]

## 6. Proof boundary

Established:

- the exact shift in the cited CvS/CCM constructions;
- the logical independence of real-zero localization from the sign of the lowest eigenvalue;
- the finite-dimensional countermodel;
- the precise missing scalar in any semilocal-to-Weil positivity chain.

Not established:

- a complete line-by-line review of the Viceré PDF;
- that no independent `epsilon_N>=0` theorem is supplied there;
- RH or its negation.
