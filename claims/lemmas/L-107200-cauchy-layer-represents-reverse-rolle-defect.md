# L-107200 — Cauchy layers represent the complete reverse–Rolle defect

Claim ID: `L-107200`  
Status: **PROVED EXACT REAL-ANALYTIC THEOREM**  
Created: 2026-08-30  
Depends on: `L-107100`, `L-107101`  
RH status: **not assumed**

Let \(f\) be real analytic on a neighbourhood of a compact interval
\(I=[a,b]\), with

\[
f(a)f'(a)f(b)f'(b)\ne0.
\]

Put

\[
r_f=\frac{f'}f,
\qquad
Q_f=-r_f'
=\frac{f'^2-ff''}{f^2}
\]

away from the real zeros of \(f\).  Let \(\mathcal C_I(f)\) be the finite set
of zeros \(c\in(a,b)\) of \(f'\) for which \(f(c)\ne0\), and write

\[
m_c=\operatorname{ord}_c(f').
\]

For \(\varepsilon>0\), define the positive Cauchy layer

\[
\boxed{
\mathscr C_{\varepsilon,I}(f)
=
\frac1\pi
\int_{I\setminus Z(f)}
\frac{\varepsilon\,(r_f')_+}
     {r_f^2+\varepsilon^2}\,dx
=
\frac1\pi
\int_{I\setminus Z(f)}
\frac{\varepsilon\,(Q_f)_-}
     {r_f^2+\varepsilon^2}\,dx.
}
\tag{L-107200.1}
\]

The two expressions are identical because \(r_f'=-Q_f\).

## 1. Local Cauchy weights

Near \(c\in\mathcal C_I(f)\),

\[
r_f(x)=\alpha_c(x-c)^{m_c}+O((x-c)^{m_c+1}),
\qquad \alpha_c\ne0.
\]

Define

\[
\omega_c=
\begin{cases}
1,&m_c\text{ odd and }r_f\text{ crosses upward},\\
0,&m_c\text{ odd and }r_f\text{ crosses downward},\\
1/2,&m_c\text{ even}.
\end{cases}
\tag{L-107200.2}
\]

Then

\[
\boxed{
\lim_{\varepsilon\downarrow0}
\mathscr C_{\varepsilon,I}(f)
=
\sum_{c\in\mathcal C_I(f)}\omega_c.
}
\tag{L-107200.3}
\]

### Proof

Choose disjoint small neighbourhoods of the finitely many points in
\(\mathcal C_I(f)\) and of the real zeros of \(f\).

At a critical point, the leading monomial has the same oriented local
Cauchy integral as \(r_f\).  On every interval on which \(r_f\) is
monotone and \(r_f'>0\), substitution \(y=r_f(x)\) gives

\[
\frac1\pi
\int\frac{\varepsilon r_f'}{r_f^2+\varepsilon^2}\,dx
=
\frac1\pi
\left[
\arctan\frac{r_f(x)}{\varepsilon}
\right].
\]

An odd upward crossing runs from a negative to a positive value and tends to
one unit.  An odd downward crossing has no positive-derivative contribution.
At an even-order touch exactly one side has positive derivative and its
Cauchy angle tends to \(\pi/2\), hence weight \(1/2\).

At a real zero \(z\) of \(f\) of multiplicity \(q\),

\[
r_f(x)=\frac q{x-z}+O(1),
\qquad
r_f'(x)=-\frac q{(x-z)^2}+O(1),
\]

so the positive part vanishes in a sufficiently small punctured
neighbourhood, up to a term tending to zero.  Away from all zeros of \(f\)
and \(f'\), the integrand tends uniformly to zero.  Summing the local limits
proves (L-107200.3).

## 2. Exact multiplicity-sensitive defect

Let \(\iota_c\in\{-1,0,1\}\) be the orientation from `L-107100`.  The local
identity

\[
m_c+\iota_c
=
(m_c-1)+2\omega_c
\tag{L-107200.4}
\]

holds in all three cases:

```text
odd downward:  (m-1)+0 = m-1;
odd upward:    (m-1)+2 = m+1;
even touch:    (m-1)+1 = m.
```

Therefore the exact reverse–Rolle defect of `L-107100` satisfies

\[
\boxed{
\mathfrak R_I(f)
=
\sum_{c\in\mathcal C_I(f)}(m_c-1)
+
2\lim_{\varepsilon\downarrow0}
\mathscr C_{\varepsilon,I}(f).
}
\tag{L-107200.5}
\]

In the Morse case every \(m_c=1\), and if \(E_I(f)\) denotes the number of
wrong-sign extrema,

\[
\boxed{
E_I(f)
=
\lim_{\varepsilon\downarrow0}
\mathscr C_{\varepsilon,I}(f).
}
\tag{L-107200.6}
\]

This removes the auxiliary depth and separation hypotheses from
`L-107101.6`: the denominator \(r_f^2+\varepsilon^2\) supplies the intrinsic
critical-point localization.

## 3. A fixed-scale quantitative lower bound

Suppose \(c\) is a simple upward zero of \(r_f\), and on
\([c-h,c+h]\),

\[
r_f'(x)\ge\alpha>0.
\]

Then

\[
r_f(c+h)\ge\alpha h,
\qquad
r_f(c-h)\le-\alpha h,
\]

and hence

\[
\boxed{
\frac1\pi
\int_{c-h}^{c+h}
\frac{\varepsilon(r_f')_+}{r_f^2+\varepsilon^2}\,dx
\ge
\frac2\pi\arctan\frac{\alpha h}{\varepsilon}.
}
\tag{L-107200.7}
\]

For disjoint such corridors,

\[
\boxed{
E_{\alpha,h}
\le
\frac{\mathscr C_{\varepsilon,I}(f)}
     {(2/\pi)\arctan(\alpha h/\varepsilon)}.
}
\tag{L-107200.8}
\]

Thus a finite \(\varepsilon\) theorem can be used whenever an Xi-specific
transversality/separation estimate is available.

## 4. Pair budget at finite screening scale

Since

\[
\frac{\varepsilon}{r_f^2+\varepsilon^2}\le\frac1\varepsilon,
\]

`L-107101` gives

\[
\boxed{
\mathscr C_{\varepsilon,I}(f)
\le
\frac1{\pi\varepsilon}
\int_I(Q_f)_-\,dx
\le
\frac2{\pi\varepsilon}
\sum_{\Im\rho>0}\frac{m(\rho)}{\Im\rho},
}
\tag{L-107200.9}
\]

with the usual finite canonical-product interpretation if the right side
diverges.

Equation (L-107200.9) is deliberately finite-scale.  Sending
\(\varepsilon\) to zero before supplying Xi-specific control loses the
estimate.

## Scope

The theorem converts the discrete reverse–Rolle defect into an exact
continuous screened-curvature observable.  It does not estimate that
observable for Xi and does not prove a zero proportion or RH.
