# L-105210 — Stability-enhanced rank–inertia inequality

Claim ID: `L-105210`  
Status: **EXACT FINITE LINEAR ALGEBRA**  
RH status: not assumed

Let \(V\) be a finite matrix with \(r\) columns of norm at most one. Put
\(P=VV^*\succeq0\) and \(M=V^*V\). Let \(Q\) be Hermitian with
\(n_+(Q)\le b\). Define
\[
\Psi(t)=
\begin{cases}
(t-1)^2,&0\le t\le2,\\
2t-3,&t\ge2.
\end{cases}
\]
Then
\[
\boxed{
\|P+Q\|_F^2
\ge
4\operatorname{tr}(P+Q)-3r-4b+\operatorname{tr}\Psi(M).
}
\]

## Proof

Write \(Q=Q_+-Q_-\), with \(Q_\pm\succeq0\),
\(Q_+Q_-=0\), and \(\operatorname{rank}Q_+\le b\).
Positivity gives
\[
\|P+Q\|_F^2\ge \|P-Q_-\|_F^2+\|Q_+\|_F^2.
\]
If \(q_j\) are the positive eigenvalues of \(Q_+\), then
\(q_j^2\ge4q_j-4\), so
\[
\|Q_+\|_F^2\ge4\operatorname{tr}Q_+-4b.
\]

Let \(p_i\) be the eigenvalues of \(M\), padded by zeros, and let \(n_i\)
be the eigenvalues of \(Q_-\). Von Neumann's trace inequality gives
\[
\|P-Q_-\|_F^2+4\operatorname{tr}Q_-
\ge
\sum_i\bigl((p_i-n_i)^2+4n_i\bigr).
\]
For \(p\ge0\),
\[
\min_{n\ge0}\bigl((p-n)^2+4n\bigr)
=2p-1+\Psi(p).
\]
Hence
\[
\|P-Q_-\|_F^2
\ge
2\operatorname{tr}P-r+\operatorname{tr}\Psi(M)
-4\operatorname{tr}Q_-.
\]
Combining the two estimates and using
\(\operatorname{tr}P\le r\) proves the claim.
