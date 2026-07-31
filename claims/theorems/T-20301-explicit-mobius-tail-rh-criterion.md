# T-20301 — An explicit Möbius-tail criterion for the final positive RH route

Claim ID: `T-20301`  
Title: Complete finite line framing plus a vanishing explicit Möbius lower-tail operator implies the Riemann hypothesis  
Status: `PROPOSED — COMPLETE CONDITIONAL COMPOSITION; FINAL ARITHMETIC TAIL ESTIMATE OPEN`  
Authoring agent: `gpt56-03-p`  
Created: 2026-08-01  
Dependencies: `L-20301`; `L-20302`; `T-18901`; `L-18501`; `L-15306`; `T-14302`  
Scope: the constructive endpoint after `T-19701`  
Related counterexample candidates: none

## 1. Cofinal data

Let \(\lambda_j\to\infty\) be an unbounded support sequence. At level \(j\),
assume the existing positive stack supplies:

1. an exact finite complete packet \(U_j\);
2. a positive ambient complement \(C_j\succ0\);
3. an old radical-like packet \(R_j\subset U_j\);
4. a finite set of proof-grade simple critical-line zeros framing
   \(W_j=R_j^{\perp}\cap U_j\);
5. the exact graph kernel
   \[
   K_j=U_j\cap\ker V_j;
   \]
6. a basis map
   \[
   J_j:\mathbb C^{d_j}\to K_j;
   \]
7. a common compact support interval
   \[
   [a_j,b_j]\subset(0,\infty).
   \]

By `L-20302`, \(\dim K_j=\dim R_j\).

Choose any integer

\[
N_j a_j>b_j.
\tag{T-20301.1}
\]

Apply the explicit source construction of `L-20301` to obtain

\[
\mathcal R_jc=J_jc+T_jc,
\tag{T-20301.2}
\]

where \(\mathcal R_jc\) is a global Weil-radical vector and \(T_jc\) is the
explicit lower-tail divisor residual.

## 2. Exact tail formula

Writing

\[
g_{j,c}(u)=u^{-1/2}J_jc(u),
\]

the physical residual is

\[
\begin{aligned}
T_jc(u)
={}&u^{1/2}\sum_{k>N_j}
\left(
\sum_{\substack{d\mid k\\d\le N_j}}\mu(d)
\right)
g_{j,c}(ku)\\
&-
u^{1/2}m_{N_j}
\left(\int g_{j,c}\right)
\sum_{m\ge1}\psi_j(mu).
\end{aligned}
\tag{T-20301.3}
\]

In the second line the factor denoted `nu` is the same variable \(u\), so it is
\(u^{1/2}\). Its Mellin transform is

\[
\begin{aligned}
\widehat{T_jc}(z)
={}&
\left[
\zeta\!\left(\frac12-iz\right)
P_{N_j}\!\left(\frac12-iz\right)-1
\right]\widehat{J_jc}(z)\\
&-
m_{N_j}\widehat{J_jc}(i/2)
\zeta\!\left(\frac12-iz\right)M_{\psi_j}(z).
\end{aligned}
\tag{T-20301.4}
\]

Both formulas are exact and provide independent producer paths.

## 3. Final quantitative hypothesis

Assume there are rational or directed numbers \(\eta_j\ge0\) such that, for
every coefficient vector \(c\),

\[
\boxed{
|Q_W(T_jc,T_jc)|
+
\|C_j^{-1/2}Z_{{\rm ker},j}J_jc\|^2
\le
\eta_j\|J_jc\|_{G_j}^2,
}
\tag{T-20301.5}
\]

and

\[
\boxed{\eta_j\longrightarrow0.}
\tag{T-20301.6}
\]

Then global radicality and Schur elimination give

\[
B_{{\rm ker},j}
-
Z_{{\rm ker},j}^*C_j^{-1}Z_{{\rm ker},j}
\succeq
-\eta_jG_{{\rm ker},j}.
\tag{T-20301.7}
\]

The visible quotient and infinite complement are already positive by the
parent stack. The finite triangular Schur theorem therefore gives a complete
localized lower floor

\[
\inf\sigma(A_{\lambda_j})
\ge
-\varepsilon_j,
\qquad
\varepsilon_j\to0.
\tag{T-20301.8}
\]

The cofinal lower-envelope theorem `T-14302` yields

\[
\boxed{\mathrm{RH}.}
\tag{T-20301.9}
\]

## 4. Stronger finite alternative

At any individual level, a strict directed negative upper endpoint for the
corrected kernel quadratic along one rational vector is a finite negative Weil
witness. A positive proof instead requires the uniform matrix inequality
(T-20301.5), not selected midpoint eigenvalues.

## 5. Exact false-RH incompatibility

If RH is false and the complete hierarchy captures an off-line cardinal
difference, `L-20301` gives at its zero parameter

\[
\widehat T_j(z_\rho)
=
-\widehat J_j(z_\rho).
\tag{T-20301.10}
\]

`L-19701` then forces a fixed negative corrected Rayleigh gap. Consequently
(T-20301.5)–(T-20301.6) cannot hold.

Thus the criterion is sharp in logical strength, but its proof object is much
more explicit than the abstract synthesis statement:

\[
\boxed{
\text{the final RH-bearing quantity is a concrete truncated-Möbius
divisor-tail operator.}
}
\tag{T-20301.11}
\]

## 6. Proof-producing routes

Any one of the following can establish (T-20301.5).

1. **Physical dilation route:** directed evaluation of (T-20301.3), followed by
   the complete Weil form.
2. **Mellin route:** a directed operator bound for the multiplier
   \[
   \zeta(s)P_{N_j}(s)-1
   \]
   against the packet transform.
3. **Hybrid zero-deflated route:** exact selected-zero vanishing, finite
   zero-cardinal deflation, and an absolute high-zero/prime remainder.
4. **Schatten route:** a trace or Hilbert–Schmidt bound for the packet tail and
   Schur cross in one metric.
5. **Exact finite-cell route:** exploit the compact support and piecewise
   structure of a finite source packet to assemble a rational tail matrix.

The physical and Mellin producers must agree after all pole and source
corrections.

## 7. Proof boundary

- The theorem constructs the complete radical extension; no source-density
  assumption remains.
- The final quantitative bound is not proved.
- Natural Möbius approximants are known to have RH-sensitive norm convergence;
  no unproved cancellation of Möbius sums is imported.
- No proof of RH is claimed.
