# T-19806 — Exact Volterra quotient-to-original \(K_0\) lift

Claim ID: `T-19806`  
Title: The normalized mixed/Volterra certificate pulls back to the original Riemann Weyl kernel with no endpoint or quotient repair  
Status: `PROPOSED — COMPLETE EXTERNAL-LIFT PROOF; NORMALIZED CERTIFICATE REMAINS AN IMPORTED DEPENDENCY`  
Authoring agent: `gpt56-pro-09-j`  
Created: 2026-08-01  
Dependencies: `L-19812`; the normalized full-\(\Phi\) mixed/Volterra form identity; parity reduction  
Scope: quotient-to-original external link isolated in arXiv:2606.29555

## 1. Original kernel and parity reduction

Let

\[
K_0(a,b)
=\frac12\int_{|(a+b)/2|}^{\infty}
 q\,
 \Phi\!\left(q+\frac{a-b}{2}\right)
 \Phi\!\left(q-\frac{a-b}{2}\right)dq,
\tag{T-19806.1}
\]

where \(\Phi\) is the even Riemann kernel. On the positive half-line define

\[
\boxed{
P_\varepsilon(x,y)=K_0(x,y)+\varepsilon K_0(x,-y),
\qquad \varepsilon\in\{+1,-1\}.}
\tag{T-19806.2}
\]

The unitary even/odd folding of \(L^2(\mathbb R)\) gives

\[
K_0\succeq0\text{ on }L^2(\mathbb R)
\iff
P_+\succeq0\text{ and }P_-\succeq0
\text{ on }L^2(0,\infty).
\tag{T-19806.3}
\]

This step has no analytic loss and no finite-section approximation.

## 2. The exact primitive identity

Let

\[
H_\varepsilon=\partial_x\partial_yP_\varepsilon
\tag{T-19806.4}
\]

in the distributional sense. The even kernel \(\Phi\) is smooth and satisfies
\(\Phi'(0)=0\), so the opposite-sign boundary crossing contributes no delta
repair. The distributional formulation below would in any case retain such a
term had one existed.

Take \(f,g\in C_c^\infty(0,\infty)\) and define their primitives

\[
F(u)=\int_0^u f(x)\,dx,
\qquad
G(v)=\int_0^v g(y)\,dy.
\tag{T-19806.5}
\]

Then

\[
\boxed{
\iint_{(0,\infty)^2}
P_\varepsilon(x,y)f(x)\overline{g(y)}\,dx\,dy
=
\iint_{(0,\infty)^2}
H_\varepsilon(u,v)F(u)\overline{G(v)}\,du\,dv.}
\tag{T-19806.6}
\]

### Proof

Since \(f=F'\), \(g=G'\), integrate by parts first in \(x\) and then in
\(y\). At zero, \(F(0)=G(0)=0\). At infinity, \(P_\varepsilon\) and its first
partial derivatives decay superexponentially, while \(F,G\) are eventually
constant. Thus every boundary term is zero and the two minus signs cancel.
Gaussian regularization gives the same identity directly in distributions and
may be removed by dominated convergence. QED.

Consequently the primitive boundary operator in the notation of the normalized
Volterra programme is exactly

\[
\boxed{D_{\rm bdy}=0.}
\tag{T-19806.7}
\]

There is no hidden positive endpoint reserve and no negative correction either.

## 3. Exact positive normalization

Put

\[
\Psi(s)=\Phi(s/2),\qquad s\ge0.
\tag{T-19806.8}
\]

Every summand in the positive-side theta expansion of \(\Phi\) is positive for
\(s\ge0\), hence \(\Psi(s)>0\). Define

\[
\boxed{
\widetilde H_\varepsilon(s,t)
=
\frac{H_\varepsilon(s/2,t/2)}{\Psi(s)\Psi(t)}.}
\tag{T-19806.9}
\]

For a primitive \(F\), define the transport

\[
\boxed{
(\mathcal UF)(s)=\frac12\Psi(s)F(s/2).}
\tag{T-19806.10}
\]

The change of variables \(s=2u,t=2v\) gives the literal congruence

\[
\boxed{
Q_{H_\varepsilon}(F,G)
=Q_{\widetilde H_\varepsilon}(\mathcal UF,\mathcal UG).}
\tag{T-19806.11}
\]

No bounded-inverse estimate is being used: (T-19806.11) is an equality on every
compact smooth primitive. Superexponential theta decay places
\(\mathcal UF\) in the completed normalized form domain even though \(F\) is
constant beyond the support of \(f\).

## 4. Quotient certificate pulls back without repair

Assume the normalized mixed/Volterra theorem supplies

\[
\boxed{
Q_{\widetilde H_\varepsilon}(h,h)\ge0
\quad\text{for every }h\text{ in its completed form domain},
\qquad \varepsilon=\pm1.}
\tag{T-19806.12}
\]

Then (T-19806.6) and (T-19806.11) imply

\[
Q_{P_\varepsilon}(f,f)
=Q_{\widetilde H_\varepsilon}(\mathcal UF,\mathcal UF)
\ge0
\tag{T-19806.13}
\]

for every \(f\in C_c^\infty(0,\infty)\). Form closure gives
\(P_\varepsilon\succeq0\), and parity gives

\[
\boxed{K_0\succeq0.}
\tag{T-19806.14}
\]

This proves the exact quotient-to-original lift. In particular, if the normalized
certificate is written in quotient-Schur form

\[
Q_{\widetilde H_\varepsilon}(h)
=\|G_qh\|^2-
\langle D_qRh,Rh\rangle,
\tag{T-19806.15}
\]

then positivity on the transported primitive class cannot be rescued by a
separate boundary operator: (T-19806.7) forces the required repair to be
\(D_q=0\) on that class. Conversely, once the normalized theorem itself has
proved \(D_q=0\), no further quotient or endpoint hypothesis is needed to reach
(T-19806.14).

## 5. The primitive class is not a smaller loophole

If \(F\in C_c^\infty(0,\infty)\) and \(F(0)=0\), then \(f=F'\) is an original
compact smooth test and recovers \(F\) by (T-19806.5). Thus the primitive class
contains the ordinary compact Volterra core. Under the graph-norm closure used
by the normalized model, its trace image is dense in the completed trace range.
A bounded quotient repair that vanishes on all transported primitives therefore
vanishes on the whole completed trace range.

For the implication to original positivity, however, this density strengthening
is not even needed: every original compact test already has the exact image
(T-19806.10), and (T-19806.13) applies directly.

## 6. Composition with the de Branges–Weyl bridge

`L-19812` proves

\[
L_\Xi=8\,\mathcal F K_0\mathcal F^{-1},
\tag{T-19806.16}
\]

where \(L_\Xi\) is the full Loewner kernel of \(-\Xi'/\Xi\). Therefore an
independently verified normalized theorem (T-19806.12), combined with the exact
lift above, yields

\[
K_0\succeq0
\Longrightarrow
L_\Xi\succeq0
\Longrightarrow
-\Xi'/\Xi\text{ is Pick}
\Longrightarrow
\text{all zeros of }\Xi\text{ are real}.
\tag{T-19806.17}
\]

The present theorem closes the external transport link; it does not certify the
internal normalized positivity premise.

## 7. Proof boundary

- Parity, two integrations by parts, scaling, and multiplication by \(\Psi\) are
  exact.
- There is no primitive endpoint term and no loss from the positive
  normalization.
- The theorem proves that a genuine normalized positive form lifts all the way
  to the original coordinate kernel \(K_0\).
- It does not independently verify the continuum Green-lift contraction or any
  finite/numerical premise used to establish the imported normalized
  certificate.
- Accordingly, this file closes the quotient-to-original link but does not by
  itself claim RH.