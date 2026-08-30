# L-108300 — A direct fifth-endpoint companion phase counts residue orientation

Claim ID: `L-108300`  
Status: **PROVED EXACT REAL-ANALYTIC THEOREM**  
Created: 2026-08-31  
Depends on: `L-107200` for the adjacent-rung Cauchy-layer model  
RH status: **not assumed**

Let \(f\) be real analytic on a neighbourhood of a compact interval
\(I=[a,b]\). Put

\[
g=f^{(5)},\qquad
W_5=f'g-fg'.
\]

Assume initially that \(f\) and \(g\) have no common zero in \(I\), and that
neither vanishes at the endpoints. For \(\sigma\in\{+1,-1\}\) and
\(\varepsilon>0\), define the entire companion

\[
E_{\sigma,\varepsilon}=g+i\sigma\varepsilon f.
\]

Choose a continuous phase \(\vartheta_{\sigma,\varepsilon}\) along \(I\).
Since \(E_{\sigma,\varepsilon}\) has no real zero under the noncommon-zero
hypothesis,

\[
\boxed{
\vartheta_{\sigma,\varepsilon}'(x)
=
{\sigma\varepsilon W_5(x)\over
 g(x)^2+\varepsilon^2f(x)^2}.
}
\tag{L-108300.1}
\]

Define its normalized negative phase variation

\[
\boxed{
\mathscr U_{\sigma,\varepsilon}(f;I)
=
{1\over\pi}\int_I
\left(-\vartheta_{\sigma,\varepsilon}'(x)\right)_+\,dx
=
{1\over\pi}\int_I
{\varepsilon(-\sigma W_5(x))_+
 \over g(x)^2+\varepsilon^2f(x)^2}\,dx.
}
\tag{L-108300.2}
\]

This is one direct endpoint observable. It does not sum the five adjacent
reverse--Rolle rungs.

## 1. Local orientation weights

Let \(c\in(a,b)\) be a zero of \(g\) with \(f(c)\ne0\), and put

\[
q={g\over f}.
\]

If \(r=\operatorname{ord}_c g\), then locally

\[
q(x)=\alpha(x-c)^r+O((x-c)^{r+1}),\qquad \alpha\ne0.
\]

Because

\[
W_5=-f^2q',
\]

the local contribution of \(c\) to (L-108300.2) has the limit

\[
\omega_{\sigma}(c)=
\begin{cases}
1,&r\text{ odd and }\sigma\alpha>0,\\
0,&r\text{ odd and }\sigma\alpha<0,\\
1/2,&r\text{ even}.
\end{cases}
\tag{L-108300.3}
\]

Consequently

\[
\boxed{
\lim_{\varepsilon\downarrow0}
\mathscr U_{\sigma,\varepsilon}(f;I)
=
\sum_{\substack{c\in(a,b)\\g(c)=0,\ f(c)\ne0}}
\omega_\sigma(c).
}
\tag{L-108300.4}
\]

The proof is the exact local substitution \(y=q(x)\) in the Cauchy phase
kernel. A zero of \(f\) not shared with \(g\) creates no atom:
\(E_{\sigma,\varepsilon}\) remains nonzero there and its phase derivative is
\(O(\varepsilon)\).

For a simple zero \(c\) of \(g\), define the fifth residue

\[
\rho_c={f(c)\over g'(c)}={f(c)\over f^{(6)}(c)}.
\]

Then \(\alpha=g'(c)/f(c)=1/\rho_c\), and therefore

\[
\boxed{
\omega_\sigma(c)=\mathbf 1_{\{\sigma\rho_c>0\}}.
}
\tag{L-108300.5}
\]

Thus the two companion orientations count the two residue signs exactly.

## 2. Exact Wronskian sign

At a simple fifth-derivative zero,

\[
W_5(c)
=
-f(c)f^{(6)}(c)
=
-\rho_c\,f^{(6)}(c)^2.
\tag{L-108300.6}
\]

A positive fifth residue is therefore exactly a negative value of the fifth
odd current \(W_5\) at a real zero of \(f^{(5)}\).

## 3. Scalar phase-variation form

For every fixed \(\varepsilon>0\),

\[
\boxed{
\mathscr U_{\sigma,\varepsilon}
=
{\operatorname{Var}_I(\vartheta_{\sigma,\varepsilon})
-
[\vartheta_{\sigma,\varepsilon}(b)
-\vartheta_{\sigma,\varepsilon}(a)]
\over2\pi}.
}
\tag{L-108300.7}
\]

Hence the endpoint defect is one ordinary total-variation problem for the
entire companion \(f^{(5)}+i\sigma\varepsilon f\). No meromorphic pole of
\(f^{(5)}/f\) is introduced.

## 4. Common zeros and exhaustion

If \(f\) and \(f^{(5)}\) share zeros, remove small symmetric intervals around
the finite common set, apply the theorem on the regular components, and retain
the local common-zero multiplicities as a separate nonnegative ledger.
Nothing in (L-108300.1)--(L-108300.7) permits that ledger to be discarded.

## Scope

This theorem exactly identifies the direct fifth-endpoint phase quantity.
It does not estimate it for \(\Xi\), prove a critical-line proportion, or
prove RH.
