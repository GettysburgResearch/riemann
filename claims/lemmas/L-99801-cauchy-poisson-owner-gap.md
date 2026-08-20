# L-99801 — Cauchy–Poisson averaging gives an exact owner gap

Put

\[
\beta(n)=\mu(n)-\mathbf1_{67\mid n}\mu(n/67),
\qquad
g(n)=v_{67}(n)+1,
\qquad
a(n)=\beta(n)/g(n),
\]

and use the exact logarithmic owner probability \(\mathbb P_n\) of PR #653.
Define

\[
\mathcal V_\gamma(n)=
\mathbb E_n\left|
a(n/Q)(n/Q)^{-i\gamma}+a(n)n^{-i\gamma}
\right|^2.
\]

For

\[
P_\tau(\gamma)=\frac{\tau}{\pi(\tau^2+\gamma^2)},
\]

the characteristic function is \(e^{-\tau|u|}\), so

\[
\overline{\mathcal V}_\tau(n)
=
\mathbb E_n\!\left[
a(n/Q)^2+a(n)^2+2a(n/Q)a(n)Q^{-\tau}
\right].
\]

For every \(n\) with \(\beta(n)\ne0\),

\[
\boxed{
\overline{\mathcal V}_\tau(n)
\ge 2(1-2^{-\tau})|a(n)|^2.
}
\]

Write \(n=67^em\), with \(m\) squarefree and \(e=0,1,2\).

- For \(e=0,1\), every owner child is \(-a(n)\).
- For \(e=2\), put \(a=a(n)=\mu(m)/3\). A non-67 prime owner gives \(-a\);
  \(Q=67\) gives \(-3a\) and contribution
  \(a^2(10-6\,67^{-\tau})\ge4a^2\);
  \(Q=67^2\) gives \(3a\) and contribution
  \(a^2(10+6\,67^{-2\tau})\ge10a^2\).

Thus the exceptional same-sign owner is fully covered.

With \(\tau_X=1/\log\log X\), the gap loses only \(\log\log X\), while
\(X^{\tau_X}=X^{o(1)}\). This proves local adaptive coercivity, not the signed
off-diagonal packing estimate.
