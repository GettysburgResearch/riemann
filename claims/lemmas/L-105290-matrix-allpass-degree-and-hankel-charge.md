# L-105290 — Matrix all-pass degree is a Hilbert–Schmidt Hankel charge

Claim ID: `L-105290`  
Status: **PROVED EXACT AT FINITE-RATIONAL / H^(1/2) SCOPE**  
Created: 2026-08-24  
Depends on: `L-105280--L-105281`; elementary Fourier/Parseval theory  
RH status: **not assumed**

## 1. Matrix degree formula

Let

\[
U:\mathbb T\longrightarrow U(r)
\]

be a rational unitary matrix function with no pole on the circle. More
generally, assume that its boundary values belong to the matrix Sobolev class
\(H^{1/2}\). Write

\[
U(e^{it})=\sum_{n\in\mathbb Z}U_ne^{int}.
\]

Then

\[
\boxed{
\operatorname{wind}\det U
 =\frac1{2\pi i}\int_0^{2\pi}
   \operatorname{tr}(U^*U')\,dt
 =\sum_{n\in\mathbb Z}n\,\|U_n\|_{\mathrm F}^2.
}
\tag{L-105290.1}
\]

Indeed, \(U^{-1}=U^*\) on the circle. Substitution of the Fourier series and
Parseval leave only equal frequencies and give the final sum. The rational
case is immediate; the \(H^{1/2}\) statement follows by approximation.

## 2. Negative Hardy energy is a Hankel norm

Let

\[
H_U=P_-M_U|_{H^2(\mathbb T;\mathbb C^r)}
\]

be the block Hankel operator. In the standard bases its \((j,k)\)-block is
\(U_{-(j+k+1)}\). Consequently

\[
\boxed{
\|H_U\|_{\mathcal S_2}^2
 =\sum_{m\ge1}m\,\|U_{-m}\|_{\mathrm F}^2.
}
\tag{L-105290.2}
\]

Put

\[
\mathcal E_-(U)=\sum_{m\ge1}m\|U_{-m}\|_{\mathrm F}^2,
\qquad
\mathcal E_+(U)=\sum_{m\ge1}m\|U_m\|_{\mathrm F}^2.
\]

Equation (L-105290.1) is

\[
\operatorname{wind}\det U=\mathcal E_+(U)-\mathcal E_-(U),
\]

and therefore

\[
\boxed{
\bigl(-\operatorname{wind}\det U\bigr)_+
 \le \mathcal E_-(U)
 =\|H_U\|_{\mathcal S_2}^2.
}
\tag{L-105290.3}
\]

The estimate is sharp. For an anti-analytic finite Blaschke product of degree
\(d\), the Hankel operator is a rank-\(d\) partial isometry and both sides of
(L-105290.3) equal \(d\).

## 3. The five-rung Xi block

For a real derivative chain \(F_j'=F_{j+1}\), let \(U_j\) be the normalized
adjacent companion all-pass quotient of `L-105281`; the one-unit Rolle carrier
has already been removed. If \(E_j\) is the wrong-extremum count at the
\(j\)-th downward step, then

\[
\operatorname{wind}U_j=-2E_j.
\]

For

\[
\mathbb U_K=\operatorname{diag}(U_1,\ldots,U_K)
\]

one has

\[
\boxed{
2\sum_{j=1}^K E_j
 =-\operatorname{wind}\det\mathbb U_K
 \le \|H_{\mathbb U_K}\|_{\mathcal S_2}^2.
}
\tag{L-105290.4}
\]

Thus all derivative losses are one block Hankel charge; they need not be
priced independently rung by rung.

Combining with exact reverse Rolle gives, up to the explicit endpoint ledger,

\[
\boxed{
R_0\ge R_K-\|H_{\mathbb U_K}\|_{\mathcal S_2}^2-O(K).
}
\tag{L-105290.5}
\]

## 4. Safe feature changes

Constant unitary matrices on either side preserve the Frobenius Fourier
energies, the Hankel Hilbert–Schmidt norm and the determinant winding. Hence a
finite Gauss transform or character transform may be performed directly on
the Hankel coefficient Hilbert space without weakening (L-105290.4).

A variable determinant-one bank preserves winding but need not preserve the
Hankel norm. This distinction is load-bearing: the exact determinant-one bank
of PR #726 removes bank-induced partial index, while its nonconstant boundary
energy must still be retained in the analytic ledger.

## Scope

The theorem is exact Fourier/operator algebra. It converts the topological
Levinson defect into a positive Hilbert-space norm on which source-owned
orthogonality identities can act. It does not estimate the actual Xi Hankel
operator and does not prove ninety percent, density one or RH.
