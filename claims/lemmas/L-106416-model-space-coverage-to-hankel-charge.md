# L-106416 — Model-space coverage converts source energy to topological Hankel charge

Claim ID: `L-106416`  
Status: **PROVED EXACT FINITE OPERATOR INEQUALITY**  
Created: 2026-08-24  
Depends on: `L-106415`; trace monotonicity  
RH status: **not assumed**

Let \(H:\mathcal H\to\mathcal K\) be a finite-rank contraction and put

\[
\mathcal I=(\ker H)^\perp,
\qquad
A=H^*H.
\]

Then \(0\preceq A\preceq P_{\mathcal I}\).  Let \(P=P_{\mathcal S}\) be the
orthogonal projection onto a finite source subspace, and define the coverage
operator on \(\mathcal I\)

\[
C=P_{\mathcal I}PP_{\mathcal I}.
\]

Fix \(0<a<1\), and let \(Q_a\) be the spectral projection of \(C\) onto
\([a,1]\).  Put

\[
r_a=\operatorname{rank}(P_{\mathcal I}-Q_a).
\]

## 1. Exact charge inequality

On \(Q_a\mathcal I\),

\[
Q_a\preceq a^{-1}Q_aCQ_a.
\]

Trace monotonicity with \(A\succeq0\) gives

\[
\operatorname{tr}(AQ_a)
\le a^{-1}\operatorname{tr}(AC)
=a^{-1}\operatorname{tr}(AP).
\]

The discarded space contributes at most its dimension because \(A\preceq I\).
Therefore

\[
\boxed{
\|H\|_{\mathcal S_2}^2
=\operatorname{tr}A
\le r_a+a^{-1}\|HP\|_{\mathcal S_2}^2.
}
\tag{L-106416.1}

This is the exact finite-dimensional source-to-topology inequality.  No
singular-value lower bound for \(H\) is assumed.

## 2. One-sided trace form

If

\[
\operatorname{tr}(I_{\mathcal I}-C)_+\le\varepsilon\dim\mathcal I,
\]

then every eigenvalue below \(a\) pays at least \(1-a\), and hence

\[
\boxed{
r_a\le\frac{\varepsilon}{1-a}\dim\mathcal I.}
\tag{L-106416.2

At \(a=1/2\),

\[
\boxed{
\|H\|_{\mathcal S_2}^2
\le2\varepsilon\dim\mathcal I
 +2\|HP\|_{\mathcal S_2}^2.
}
\tag{L-106416.3

Thus an \(o(1)\) one-sided sampling deficit and a fixed source-energy estimate
control the complete topological Hankel charge.

## 3. Endpoint application

For a rational endpoint all-pass symbol \(U_T\), take

\[
H=H_{U_T},
\qquad
\mathcal I=K_{B_{-,T}},
\qquad
P=P_{\mathcal S_T}.
\]

The coverage operator \(C\) is exactly the explicit sampling matrix
\(\mathcal C_T\) of `L-106415`.  The restricted source energy
\(\|H_{U_T}P_{\mathcal S_T}\|_{\mathcal S_2}^2\) is paid by the four-channel
Xi source estimate of `L-106413` after the endpoint bank is normalized.

Consequently the remaining source-coverage theorem is a lower spectral bound
for one explicit finite matrix; it is not an additional contour identity.
