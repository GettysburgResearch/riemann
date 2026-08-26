# L-105500 — Native squarefree compactification is rigidly a prime-color boundary gauge

Claim ID: `L-105500`

Status: **PROVED EXACT LOCAL RIGIDITY AND GLOBAL SOURCE FACTORIZATION**

Created: 2026-08-27

Depends on: finite prime-box Chow algebra `L-105460`; binding `R-105500`

RH status: **not assumed**

The square-zero Chow midpoint is a valid source square before physical
compactification.  The native ordinary-Möbius source requires a different
physical section: every prime must be assigned wholly to one of two factors.

## 1. Local rigidity

Let \(x_p\) denote one physical prime atom.  Seek two ordinary squarefree local
factors

\[
(1-\alpha_p x_p)(1-\beta_p x_p)
\]

whose product is exactly \(1-x_p\), with no \(x_p^2\) term.  Coefficient
comparison gives

\[
\alpha_p+\beta_p=1,
\qquad
\alpha_p\beta_p=0.
\]

Hence

\[
\boxed{\{\alpha_p,\beta_p\}=\{0,1\}.}
\tag{L-105500.1}
\]

Thus every contraction-free ordinary two-factor compactification of the
native local Euler factor is an endpoint choice.  There is no continuous
ordinary midpoint.

By contrast, in the Chow algebra \(h_p^2=0\), so

\[
(1-\tfrac12h_p)^2=1-h_p.
\]

After ordinary physical realization the omitted term is
\(\tfrac14x_p^2\).  The square-zero relation, not an analytic estimate, is what
made the midpoint possible.

## 2. Prime-color gauge

Choose any coloring of the primes

\[
\chi:\mathcal P\longrightarrow\{+,-\}.
\]

Define

\[
\mu_\chi^\pm(n)
=
\begin{cases}
\mu(n),&
n\ {\rm squarefree\ and\ every}\ p\mid n\ {\rm has\ color}\ \pm,\\
0,&\text{otherwise},
\end{cases}
\]

with \(\mu_\chi^\pm(1)=1\).  Unique factorization gives, coefficientwise,

\[
\boxed{\mu=\mu_\chi^+*\mu_\chi^-.}
\tag{L-105500.2}
\]

Indeed a squarefree integer \(n\) has the unique decomposition

\[
n=n_+n_-,
\qquad
n_\pm=\prod_{\substack{p\mid n\\\chi(p)=\pm}}p.
\]

Therefore the factorization has:

```text
no repeated prime label;
no squareful contraction;
no owner/core completion;
no equal-product multiplicity.
```

For \(\Re z>1\),

\[
\boxed{
\left(\prod_{\chi(p)=+}(1-p^{-z})\right)
\left(\prod_{\chi(p)=-}(1-p^{-z})\right)
=
\frac1{\zeta(z)}.
}
\tag{L-105500.3}
\]

The extreme gauges, including “all primes \(+\)” and “all primes \(-\),” are
legal.

## 3. Uniform source diagonals

On a finite horizon \(Z\),

\[
\sum_{n\le Z}\frac{|\mu_\chi^\pm(n)|^2}{n}
\le
\prod_{p\le Z}\left(1+\frac1p\right)
\ll\log(2Z).
\tag{L-105500.4}
\]

Thus every color factor has subpower free coefficient energy.  Equation
(L-105500.4) does not estimate distinct translated products after physical
observation.

## 4. Geometric meaning

The native physical section of the two-copy F1 configuration is the boundary
vertex cube

\[
\{0,1\}^{\mathcal P},
\]

not the midpoint of \([0,1]^{\mathcal P}\).  A color chooses on which copy each
prime divisor lives.  Because the two color supports are disjoint, ordinary
multiplication already equals Wick multiplication on that section.

This is the source-exact replacement for the completed midpoint geometry
refuted in `R-105500`.
