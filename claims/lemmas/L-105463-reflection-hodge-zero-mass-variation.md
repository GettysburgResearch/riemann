# L-105463 — The remaining F1 trace is a reflection-odd Hodge variation with zero total mass

Claim ID: `L-105463`

Status: **PROVED EXACT HILBERT-SIGNATURE AND VARIATION EQUIVALENCE**

Let \(F_{U,\theta}\) and \(\mathcal J_U^\diamond\) be as in `L-105462`, and put

\[
\mathcal D_{\rm out}
 =
 \frac12D(D-1)(5D+3/2)(2D-1).
\tag{L-105463.1}
\]

The exact common-mother calculation of `L-106134`, composed with
`L-105462`, gives

\[
H_K^{\rm live}
 =
 \mathcal D_{\rm out}\mathcal J_U^\diamond
 +H_{\rm closed}.
\tag{L-105463.2}
\]

Using the ordinary completion and the diagonal ledger,

\[
\boxed{
H_K^{\rm live}
 =
 \mathcal D_{\rm out}\mathcal J_U
 +\widetilde H_{\rm closed},
}
\tag{L-105463.3}
\]

where the closed field has subpower logarithmic total variation.

## 1. Reflection Hodge decomposition

Write \(x=\log X\),

\[
f_\theta(u)=F_{U,\theta}(e^u),
\qquad
(R_xf)(u)=f(x-u).
\]

The operator \(R_x\) is a self-adjoint unitary involution.  Define

\[
E_x=\frac12(I+R_x),
\qquad
O_x=\frac12(I-R_x).
\]

After the Beta average, put

\[
\begin{aligned}
\mathcal E_U(x)
 &=
 \int_0^1(1-\theta)\|E_xf_\theta\|_2^2\,d\theta,\\
\mathcal O_U(x)
 &=
 \int_0^1(1-\theta)\|O_xf_\theta\|_2^2\,d\theta,\\
\mathcal N_U
 &=
 \int_0^1(1-\theta)\|f_\theta\|_2^2\,d\theta.
\end{aligned}
\]

Then

\[
\boxed{
\mathcal E_U+\mathcal O_U=\mathcal N_U,
\qquad
\mathcal J_U=\mathcal E_U-\mathcal O_U.
}
\tag{L-105463.4}
\]

Since \(\mathcal D_{\rm out}\) contains \(D\),

\[
\boxed{
\mathcal D_{\rm out}\mathcal J_U
 =
 2\mathcal D_{\rm out}\mathcal E_U
 =
 -2\mathcal D_{\rm out}\mathcal O_U.
}
\tag{L-105463.5}
\]

Moreover,

\[
\boxed{
\mathcal O_U(x)
 =
 \frac14\int_0^1(1-\theta)
 \int_{\mathbf R}|f_\theta(u)-f_\theta(x-u)|^2\,du\,d\theta.
}
\tag{L-105463.6}
\]

Thus the adverse physical trace is the differential variation of the
anti-invariant Hodge norm.

## 2. Zero mass and total variation

For one frozen finite source block, \(\mathcal J_U\) is compactly supported in
logarithmic coordinate.  Since

\[
\mathcal O_U-\frac12\mathcal N_U
 =
 -\frac12\mathcal J_U,
\]

the signed measure

\[
\nu_U
 =
 \mathcal D_{\rm out}\mathcal O_U
\tag{L-105463.7}
\]

is compactly supported.  The leading factor \(D\) gives

\[
\boxed{\nu_U(\mathbf R)=0.}
\tag{L-105463.8}
\]

Consequently its Jordan masses satisfy

\[
\boxed{
\nu_U^+(\mathbf R)
 =
 \nu_U^-(\mathbf R)
 =
 \frac12\|\nu_U\|_{\rm TV}.
}
\tag{L-105463.9}
\]

Therefore the one-sided reflection gate is exactly a total-variation gate.
Define

```text
F1VAR105460:
  on every frozen dyadic horizon,
  || D_out O_U ||_TV = Y^(o(1)).
```

Then, with the same frozen boundary convention,

\[
\boxed{
\mathrm{F1VAR}_{105460}
\Longleftrightarrow
\mathrm{REFSIG}_{106150}.
}
\tag{L-105463.10}
\]

The factor of two is immaterial and explicit.

## 3. Four exact primitive moments

Let

\[
P(z)=\frac12z(z-1)(5z+3/2)(2z-1).
\]

Put \(q_U=\mathcal O_U-\mathcal N_U/2=-\mathcal J_U/2\).  For every root

\[
\lambda\in\left\{0,1,-\frac3{10},\frac12\right\},
\]

compact distributional integration by parts gives

\[
\boxed{
\int_{\mathbf R}e^{-\lambda x}\,d\nu_U(x)
 =
 P(\lambda)
 \int_{\mathbf R}e^{-\lambda x}q_U(x)\,dx
 =
 0.
}
\tag{L-105463.11}
\]

Thus the final F1 trace is a compact four-moment primitive wavelet applied to
one positive reflection-mismatch energy.

## Boundary

This lemma identifies the exact norm whose subpower variation would prove the
remaining arithmetic theorem.  It does not estimate that variation.
`F1VAR105460`, `REFSIG106150`, `BCI102990`, and RH remain unproved.
