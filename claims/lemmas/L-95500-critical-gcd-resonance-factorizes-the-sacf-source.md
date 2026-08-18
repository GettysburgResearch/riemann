# L-95500 — Critical gcd resonance exactly factorizes the SACF arithmetic source

Claim ID: `L-95500`  
Status: **PROPOSED COMPLETE EXACT ARITHMETIC THEOREM — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-18  
Frozen parent: PR #580 at `812e7fcbaff2dd1c2c53c885def7b6c0d0e68a05`  
Scope: source and dual-frequency factorization; no pointwise SACF estimate and no RH conclusion

## 1. Odd squarefree reciprocal state

Let \(\mathscr S_o\) be the odd squarefree integers and put

\[
M_o(s)
=
\sum_{n\in\mathscr S_o}\frac{\mu(n)}{n^s}
=
\prod_{p>2}(1-p^{-s})
=
\frac{1}{(1-2^{-s})\zeta(s)}
\tag{L-95500.1}
\]

for \(\Re s>1\).

For \(m,n\in\mathscr S_o\), write uniquely

\[
d=(m,n),\qquad m=da,\qquad n=db.
\]

Then \(a,b,d\in\mathscr S_o\) are pairwise coprime and

\[
\mu(m)\mu(n)=\mu(a)\mu(b).
\tag{L-95500.2}
\]

## 2. Exact resonant triple series

For \(\Re s_1,\Re s_2>1\), the gcd change of variables gives

\[
\boxed{
\begin{aligned}
M_o(s_1)M_o(s_2)
&=
\sum_{\substack{a,b,d\in\mathscr S_o\\
(a,b)=(a,d)=(b,d)=1}}
\frac{\mu(a)\mu(b)}
{a^{s_1}b^{s_2}d^{s_1+s_2}}.
\end{aligned}
}
\tag{L-95500.3}
\]

At one odd prime put

\[
u=p^{-s_1},\qquad v=p^{-s_2}.
\]

The four source-owned choices are:

```text
prime absent:       +1;
prime in a:         -u;
prime in b:         -v;
prime in d:         +uv.
```

Hence the local factor is

\[
\boxed{1-u-v+uv=(1-u)(1-v).}
\tag{L-95500.4}
\]

This identity is the critical gcd resonance. The sign-free common-divisor
state supplies exactly the product term needed to reconstruct two independent
Möbius Euler factors.

## 3. Why the critical exponents are forced

In the Q4 square, the exact gcd-coordinate weight is

\[
\frac{1}{d\sqrt{ab}}
\Psi_1(da/X)\Psi_2(db/Y).
\]

After Mellin inversion with variables \(z_1,z_2\), the exponents are

\[
s_1=\frac12+z_1,\qquad
s_2=\frac12+z_2,
\]

and the common-divisor exponent is

\[
1+z_1+z_2=s_1+s_2.
\tag{L-95500.5}
\]

Thus the physical \(1/(d\sqrt{ab})\) normalization lies exactly on the
resonant hyperplane where (L-95500.4) factorizes. This is not an approximate
singular-series calculation.

## 4. Two-scale Mellin identity

For compactly supported kernels \(\Psi_1,\Psi_2\), define

\[
\mathcal B_{\Psi_1,\Psi_2}(X,Y)
=
\sum_{m,n\in\mathscr S_o}
\frac{\mu(m)\mu(n)}{\sqrt{mn}}
\Psi_1(m/X)\Psi_2(n/Y).
\]

For initially large real parts,

\[
\boxed{
\begin{aligned}
&\int_1^\infty\int_1^\infty
\mathcal B_{\Psi_1,\Psi_2}(X,Y)
X^{-z_1-1}Y^{-z_2-1}\,dX\,dY\\
&\qquad=
\widehat\Psi_1(z_1)\widehat\Psi_2(z_2)
M_o(z_1+\tfrac12)M_o(z_2+\tfrac12).
\end{aligned}
}
\tag{L-95500.6}
\]

The same formula follows from the triple series (L-95500.3), with the
common-divisor exponent (L-95500.5).

On the dual-frequency slice

\[
z_1=\sigma+it,\qquad z_2=\sigma-it,
\]

the arithmetic factor is

\[
\boxed{
M_o(\sigma+\tfrac12+it)
M_o(\sigma+\tfrac12-it)
=
\left|M_o(\sigma+\tfrac12+it)\right|^2.
}
\tag{L-95500.7}
\]

The exact coprime/gcd Type-II source is therefore a reciprocal-zeta square on
its natural dual-frequency line.

## 5. Logarithmic channels are exact derivatives

The PR #580 packet contains both \(\mu(m)\log m\) and \(\mu(m)\) channels.
In gcd coordinates,

\[
\log m=\log a+\log d,
\qquad
\log n=\log b+\log d.
\]

Differentiating (L-95500.3) in \(s_1\) or \(s_2\) produces these complete
logarithmic factors exactly. Thus every `J0` logarithmic term and every `J1`
boundary term is a derivative or zeroth-order component of the same tensor
product. No source term is lost by the gcd parameterization.

## 6. Determinant/product parameterization

If the common-divisor state is temporarily omitted, the coprime pair local
factor is

\[
1-u-v.
\]

The common-divisor state restores \(+uv\), giving the exact determinant
completion

\[
1-u-v+uv=(1-u)(1-v).
\]

Equivalently, after putting \(k=ab\) with \((a,b)=1\), the balanced divisor
sum is a finite coefficient presentation of the same two reciprocal-zeta
legs. The determinant parameterization does not manufacture a third source of
oscillation.

## 7. Boundary

```text
unique gcd/source decomposition             EXACT
critical common-divisor exponent             EXACT
local Euler completion (1-u)(1-v)            EXACT
full triple Dirichlet factorization           EXACT
logarithmic derivative channels              EXACT
dual-frequency reciprocal-zeta square        EXACT
SACF pointwise bound                          OPEN / RH-BEARING
Riemann Hypothesis                            UNPROVEN
```
