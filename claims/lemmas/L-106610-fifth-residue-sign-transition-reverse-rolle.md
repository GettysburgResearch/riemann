# L-106610 — Fifth-residue sign transitions are the exact reverse–Rolle defect

Claim ID: `L-106610`  
Status: **PROVED EXACT ON REGULAR FINITE WINDOWS**  
Created: 2026-08-26  
Depends on: the exact fifth-endpoint notation of `L-106500/L-106514`  
RH status: **not assumed**

Let \(F\) be a real \(C^6\) function on an interval and put

\[
Q=F^{(5)},\qquad
\mathcal L_5=F'F^{(5)}-FF^{(6)}.
\]

Let

\[
c_1<c_2<\cdots<c_M
\]

be consecutive simple real zeros of \(Q\), with no common \(F,Q\) zero.
Define the fifth critical residues

\[
\rho_j=\frac{F(c_j)}{Q'(c_j)}
       =\frac{F(c_j)}{F^{(6)}(c_j)}.
\tag{L-106610.1}
\]

At a \(Q\)-zero,

\[
\boxed{
\mathcal L_5(c_j)=-F(c_j)Q'(c_j)
                 =-\rho_j Q'(c_j)^2.
}
\tag{L-106610.2}
\]

Hence \(\rho_j\) and \(-\mathcal L_5(c_j)\) have the same sign.

## 1. Exact interval criterion

The derivative signs at consecutive simple zeros alternate:

\[
Q'(c_j)Q'(c_{j+1})<0.
\tag{L-106610.3}
\]

Therefore

\[
\operatorname{sgn}\!\bigl(F(c_j)F(c_{j+1})\bigr)
=
-\operatorname{sgn}(\rho_j\rho_{j+1}).
\tag{L-106610.4}
\]

Consequently,

\[
\boxed{
\rho_j\rho_{j+1}>0
\quad\Longrightarrow\quad
F \text{ has a real zero in }(c_j,c_{j+1}).
}
\tag{L-106610.5}
\]

Equivalently, equal signs of the sampled Wronskian
\(\mathcal L_5(c_j),\mathcal L_5(c_{j+1})\) force a parent zero.

Let

\[
V_5
=
\#\{1\le j<M:\rho_j\rho_{j+1}<0\}
\tag{L-106610.6}
\]

be the number of residue-sign transitions. The open intervals are disjoint, so

\[
\boxed{
N_{\mathbb R}(F;(c_1,c_M))
\ge M-1-V_5.
}
\tag{L-106610.7}
\]

This is the literal fifth-step converse–Rolle ledger. No residue magnitude,
separation constant, all-pass scale, or model-space condition number occurs.

## 2. Common and confluent events

If \(F(c_j)=0\), that point is already a parent real zero and should be
removed from the transition list after being credited once. Multiple
\(Q\)-zeros are handled by a generic real perturbation or by the confluent
Hermite–Bézout block; the multiplicity excess is retained explicitly in the
entire-window ledger. Equation (L-106610.7) is unchanged on every regularized
simple stratum.

## 3. Xi consumption

For \(F=\Xi\), the fifth-endpoint theorem supplies a cofinal regular-window
count \(R_5(T,2T)\). After subtracting the literal multiple/common/endpoint
ledger \(\mathcal E_{\rm reg}(T)\), (L-106610.7) gives

\[
\boxed{
R_0(T,2T)
\ge
R_5(T,2T)-V_5(T)-\mathcal E_{\rm reg}(T)-O(1).
}
\tag{L-106610.8}
\]

Thus the microscopic endpoint obstruction can be expressed either as the
canonical-correlation/Hankel charge of `T-106530--T-106540`, or as the
projective sign variation of the fifth critical residues. The latter is
denominator-free and discrete.

## Scope

The lemma does not bound \(V_5(T)\). Positive Fourier density of
\(\mathcal L_5\) does not control its sampled signs; the binding counterexample
is recorded in `R-106610`.
