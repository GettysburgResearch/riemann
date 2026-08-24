# L-106430 — Exact confluent Paley–Wiener coverage and the rank ledger

Claim ID: `L-106430`  
Status: **PROVED EXACT FOR FINITE BLASCHKE MODEL SPACES**  
Created: 2026-08-25  
Depends on: `L-106415` and standard model-space Fourier theory  
RH status: **not assumed**

This lemma audits the live sampling gate `PWSAMP106420` at the literal
Paley–Wiener scale.  It does not estimate Xi.

## 1. One confluent companion cluster

Let

\[
b=a+iy,\qquad y>0,
\]

and let

\[
B_b(z)=\frac{z-b}{z-\overline b}.
\]

For the multiplicity-\(r\) model space

\[
K_{B_b^r}=H^2(\mathbb C_+)\ominus B_b^rH^2(\mathbb C_+),
\]

the Fourier transform to \(L^2(0,\infty)\) has the orthonormal Laguerre basis

\[
\boxed{
\phi_q(u)=\sqrt{2y}\,e^{-yu}e^{-iau}L_q(2yu),
\qquad 0\le q<r,
}
\tag{L-106430.1}
\]

where \(L_q\) is the ordinary Laguerre polynomial.  Orthogonality is exactly

\[
\int_0^\infty e^{-t}L_q(t)L_j(t)\,dt=\delta_{qj}.
\]

Let \(P_{[0,H]}\) be the hard one-sided Paley–Wiener projection.  The complete
coverage and deficit traces of this confluent block are therefore

\[
\boxed{
\operatorname{tr}_{K_{B_b^r}}P_{[0,H]}
 =\sum_{q=0}^{r-1}
  \int_0^{2yH}e^{-t}L_q(t)^2\,dt,
}
\tag{L-106430.2}
\]

\[
\boxed{
\operatorname{tr}_{K_{B_b^r}}(I-P_{[0,H]})
 =\sum_{q=0}^{r-1}
  \int_{2yH}^{\infty}e^{-t}L_q(t)^2\,dt.
}
\tag{L-106430.3}
\]

For every fixed \(q\), the final integral is

\[
e^{-2yH}P_q(2yH)
\]

for an explicit polynomial \(P_q\) with rational coefficients, obtained from

\[
\int_x^\infty e^{-t}t^m\,dt
 =e^{-x}m!\sum_{j=0}^m\frac{x^j}{j!}.
\]

Thus multiplicities and collisions are not hidden in an unspecified
conditioning constant.

For one simple factor,

\[
\boxed{
\operatorname{tr}_{K_{B_b}}(I-P_{[0,H]})=e^{-2yH}.
}
\tag{L-106430.4}
\]

At the live small-shift scale \(yH=1/200\),

\[
e^{-2yH}=e^{-1/100}>1-\frac1{100}=\frac{99}{100}.
\tag{L-106430.5}
\]

So a single near-boundary companion pole is almost entirely outside the hard
band when charged **individually**.

## 2. Every finite source frame obeys the same lower firewall

Let \(\mathcal S\subseteq PW_H\) be any finite-dimensional source space, and
let \(C=P_{K_B}P_{\mathcal S}P_{K_B}\) be the coverage operator of
`L-106415`.  Since

\[
P_{\mathcal S}\preceq P_{[0,H]},
\]

one has

\[
\boxed{
\operatorname{tr}_{K_{B_b^r}}(I-C)
\ge
\sum_{q=0}^{r-1}
\int_{2yH}^{\infty}e^{-t}L_q(t)^2\,dt.
}
\tag{L-106430.6}
\]

This is a source-generic lower bound.  It does not rule out Xi-specific
collective cancellation between different zero and pole model spaces; it does
rule out proving full one-sided coverage from the small parameter
\(\lambda H=1/200\) alone.

## 3. Dimension ledger

For an arbitrary finite Blaschke product \(B\) of degree \(m\), and an arbitrary
source space \(\mathcal S\) of dimension \(d\),

\[
0\preceq C=P_{K_B}P_{\mathcal S}P_{K_B}\preceq I_{K_B},
\qquad
\operatorname{rank}C\le d.
\]

Consequently

\[
\boxed{
\operatorname{tr}(I_{K_B}-C)
\ge (m-d)_+.
}
\tag{L-106430.7}
\]

Any cofinal use of `PWSAMP106420` must therefore include an explicit comparison
between the reduced denominator degree \(m_T\) and the declared source
dimension \(d_T\).  Sampling-kernel algebra alone does not supply that
comparison.

## 4. Scientific disposition

Equations (L-106430.2)--(L-106430.7) do not refute an Xi-specific theorem for
the complete sampling matrix.  They show that the current requirement

\[
\operatorname{tr}(I-C_T)=o(N(T))
\]

is a strong **absolute coverage** statement.  It charges pole and zero model
spaces separately and suppresses the cancellation which the all-pass degree
formula is designed to retain.  The signed replacement is developed in
`L-106431` and `T-106430`.
