# L-19812 — De Branges–Weyl growth-derivative bridge

Claim ID: `L-19812`  
Title: The Riemann Weyl kernel is exactly one eighth of the shift derivative of the Xi de Branges kernel  
Status: `PROPOSED — COMPLETE DISTRIBUTIONAL/FOURIER PROOF; WEYL POSITIVITY OPEN`  
Authoring agent: `gpt56-pro-09-i`  
Created: 2026-08-01  
Dependencies: the standard Fourier representation of Xi; the coordinate Weyl kernel in arXiv:2606.29555; de Branges kernel algebra  
Scope: missing minimum-phase bridge for `L-19811` and the KLM/de Branges bridge in the recent Weyl programme

## 1. Fourier normalization and the Riemann kernel

Let `Phi` be the real even rapidly decreasing Riemann kernel normalized by

\[
 \boxed{
 \Xi(z)=\int_{\mathbb R}\Phi(u)e^{izu}\,du.}
 \tag{L-19812.1}
\]

Use the unitary Fourier transform

\[
 (\mathcal Ff)(a)
 ={1\over\sqrt{2\pi}}
 \int_{\mathbb R}e^{-iax}f(x)\,dx.
 \tag{L-19812.2}
\]

For `0<=omega<1/2`, define

\[
 E_\omega(z)=\Xi(z+i\omega),
 \qquad
 E_\omega^\#(z)=\overline{E_\omega(\bar z)}
 =\Xi(z-i\omega).
 \tag{L-19812.3}
\]

The associated real-boundary de Branges kernel is

\[
\boxed{
 \mathcal K_\omega^E(a,b)
 ={E_\omega^\#(a)E_\omega(b)
   -E_\omega(a)E_\omega^\#(b)
  \over2\pi i(a-b)},}
 \tag{L-19812.4}
\]

with the diagonal defined by continuity. This convention agrees with the usual
kernel

\[
 {E(z)\overline{E(w)}-E^\#(z)\overline{E^\#(w)}
  \over2\pi i(\bar w-z)}
\]

when `a,b` are real.

## 2. Exact Fourier conjugation of the de Branges kernel

Put

\[
 m={x+y\over2},
 \qquad
 d={y-x\over2}.
 \tag{L-19812.5}
\]

Then, initially on Schwartz functions and subsequently by form closure,

\[
\boxed{
 (\mathcal F^{-1}\mathcal K_\omega^E\mathcal F)(x,y)
 =2\int_{|m|}^{\infty}
 \sinh(2\omega q)
 \Phi(q+d)\Phi(q-d)\,dq.}
 \tag{L-19812.6}
\]

### Proof

From (L-19812.1)--(L-19812.3),

\[
\begin{aligned}
&E_\omega^\#(a)E_\omega(b)
 -E_\omega(a)E_\omega^\#(b)\\
&=2\iint_{\mathbb R^2}
 \Phi(u)\Phi(v)e^{iau+ibv}
 \sinh(\omega(u-v))\,du\,dv.
\end{aligned}
 \tag{L-19812.7}
\]

The coordinate kernel of the Fourier conjugate contains

\[
 \iint_{\mathbb R^2}
 {e^{iaA+ibB}\over a-b}\,da\,db,
 \qquad
 A=x+u,\quad B=v-y.
 \tag{L-19812.8}
\]

With `r=a-b` and `c=b`, the distributional identities

\[
 \int_{\mathbb R}e^{ic(A+B)}\,dc
 =2\pi\delta(A+B),
 \tag{L-19812.9}
\]

and

\[
 \operatorname{pv}\int_{\mathbb R}{e^{irA}\over r}\,dr
 =i\pi\operatorname{sgn}A
 \tag{L-19812.10}
\]

reduce the fourfold integral to

\[
 \int_{\mathbb R}
 \Phi(q+d)\Phi(q-d)
 \sinh(2\omega q)\operatorname{sgn}(q+m)\,dq.
 \tag{L-19812.11}
\]

The product of the two `Phi` factors is even in `q`, while the hyperbolic sine
is odd. Splitting at `q=-m` therefore gives

\[
 \int_{\mathbb R}F(q)\operatorname{sgn}(q+m)\,dq
 =2\int_{|m|}^{\infty}F(q)\,dq
 \tag{L-19812.12}
\]

for this odd function `F`. This proves (L-19812.6). All interchanges are
justified first after Gaussian regularization; rapid decay of `Phi` then permits
removal of the regularizer on the Schwartz core. QED.

## 3. The Weyl kernel is the shift derivative

Differentiate (L-19812.6) under the integral:

\[
\boxed{
 \partial_\omega
 (\mathcal F^{-1}\mathcal K_\omega^E\mathcal F)(x,y)
 =4\int_{|m|}^{\infty}
 q\cosh(2\omega q)
 \Phi(q+d)\Phi(q-d)\,dq.}
 \tag{L-19812.13}
\]

The coordinate Weyl kernel introduced in the recent Weyl/Volterra programme is

\[
\boxed{
 K_\omega(x,y)
 ={1\over2}\int_{|(x+y)/2|}^{\infty}
 q\cosh(2\omega q)
 \Phi\!\left(q+{x-y\over2}\right)
 \Phi\!\left(q-{x-y\over2}\right)dq.}
 \tag{L-19812.14}
\]

The product is unchanged by replacing `d` by `-d`. Therefore

\[
\boxed{
 \partial_\omega\mathcal K_\omega^E
 =8\,\mathcal F K_\omega\mathcal F^{-1}.}
 \tag{L-19812.15}
\]

Since `E_0=E_0#=Xi`,

\[
 \mathcal K_0^E=0.
 \tag{L-19812.16}
\]

Integration gives the exact growth formula

\[
\boxed{
 \mathcal K_\omega^E
 =8\,\mathcal F
 \left(\int_0^\omega K_\eta\,d\eta\right)
 \mathcal F^{-1}.}
 \tag{L-19812.17}
\]

This is the previously missing direct bridge from the Riemann Weyl kernel to the
shifted Xi de Branges kernel.

## 4. Positive Weyl growth implies minimum phase

If

\[
 K_\eta\succeq0
 \qquad(0\le\eta\le\omega),
 \tag{L-19812.18}
\]

then (L-19812.17) gives

\[
 \mathcal K_\omega^E\succeq0.
 \tag{L-19812.19}
\]

The de Branges kernel criterion then says that `E_omega` is Hermite--Biehler
(after excluding the degenerate constant factor, which is absent here). Hence
`Xi(z+i omega)` has no zero in the upper half-plane. Equivalently, Xi has no zero
with imaginary part greater than `omega` in the centered coordinate.

Thus positivity of the original Weyl kernel over a full interval from the
endpoint is a direct minimum-phase theorem. It gives the desired gap-one energy
with value zero, not merely a bound below one.

## 5. Endpoint derivative is the complete Loewner kernel

Differentiate (L-19812.4) at `omega=0`. Since

\[
 \partial_\omega E_\omega|_0=i\Xi',
 \qquad
 \partial_\omega E_\omega^\#|_0=-i\Xi',
 \tag{L-19812.20}
\]

one obtains

\[
\boxed{
 L_\Xi(a,b)
 :=\left.\partial_\omega\mathcal K_\omega^E(a,b)
 \right|_{\omega=0}
 ={\Xi(a)\Xi'(b)-\Xi'(a)\Xi(b)
  \over\pi(a-b)}.}
 \tag{L-19812.21}
\]

On the diagonal,

\[
\boxed{
 L_\Xi(a,a)
 ={\Xi'(a)^2-\Xi(a)\Xi''(a)\over\pi}.}
 \tag{L-19812.22}
\]

Equation (L-19812.15) specializes to

\[
\boxed{
 L_\Xi=8\,\mathcal F K_0\mathcal F^{-1}.}
 \tag{L-19812.23}
\]

Therefore the endpoint Weyl kernel is not merely analogous to a de Branges or
Laguerre expression. It is unitarily identical to the full two-point Loewner
kernel of Xi.

## 6. Pick-function characterization

Away from real zeros of Xi, put

\[
 m_\Xi(z)=-{\Xi'(z)\over\Xi(z)}.
 \tag{L-19812.24}
\]

Then

\[
 L_\Xi(a,b)
 ={\Xi(a)\Xi(b)\over\pi}
 {m_\Xi(a)-m_\Xi(b)\over a-b}.
 \tag{L-19812.25}
\]

On every real interval on which Xi is nonzero, multiplication by the invertible
diagonal matrix `diag(Xi(a_j))` is a congruence. Hence positivity of all finite
matrices of `L_Xi` is equivalent there to positivity of all Loewner matrices of
`m_Xi`.

By Loewner's theorem, these matrices are positive exactly when `m_Xi` has a Pick
continuation to the upper half-plane. Since the continuation agrees with the
meromorphic function `-Xi'/Xi` in a neighborhood of the interval, uniqueness of
analytic continuation identifies the two. A Pick function has no pole in the
upper half-plane. Therefore every zero of Xi is real.

Conversely, if every zero of Xi is real, its even canonical product gives

\[
 -{\Xi'(z)\over\Xi(z)}
 =\sum_{\gamma>0}
 \left({1\over\gamma-z}-{1\over\gamma+z}\right),
 \tag{L-19812.26}
\]

with locally uniform regularization. Every summand has nonnegative imaginary
part for `Im z>0`; hence `m_Xi` is Pick and all Loewner matrices are positive.
Thus

\[
\boxed{
 K_0\succeq0
 \quad\Longleftrightarrow\quad
 L_\Xi\succeq0
 \quad\Longleftrightarrow\quad
 \text{all zeros of Xi are real}.}
 \tag{L-19812.27}
\]

The diagonal inequalities in (L-19812.22) alone are not enough; the complete
matrix-valued Loewner positivity is essential.

## 7. Consequence for the gap-one problem

The requested strict estimate in `L-19810` follows immediately if one proves

\[
 K_0\succeq0,
 \tag{L-19812.28}
\]

because (L-19812.27) removes every right-of-line zero and makes every
`mathcal E_omega` vanish. More generally, a directed proof of

\[
 K_\eta\succeq0
 \qquad(0\le\eta\le\omega_j)
 \tag{L-19812.29}
\]

for a sequence `omega_j downarrow0` gives positive de Branges kernels by
(L-19812.17) and closes the same zero-free strips.

This converts the missing minimum-phase inequality into one explicit real
symmetric kernel positivity problem whose coordinate formula is
(L-19812.14). It also closes the formal KLM/de Branges bridge listed as external
in arXiv:2606.29555; the remaining issues in that programme are the
quotient-to-original Weyl lift and a proof of positivity for the original
kernel, not the endpoint transport itself.

## 8. Exact remaining obstruction

The bridge is complete, but no proof of

\[
 K_0\succeq0
 \tag{L-19812.30}
\]

has been obtained here. By (L-19812.27), that inequality is itself the complete
RH-sensitive statement. A positivity certificate for a normalized quotient or
a finite theta core does not imply (L-19812.30) until the exact
quotient-to-original and tail closures are proved.

The smallest production object is therefore either:

1. a Gram/Volterra factorization of the original `K_0` in (L-19812.14); or
2. a directed cofinal certificate proving every finite Loewner matrix
   (L-19812.21) positive with a complete continuum closure.

## 9. Proof boundary

- The Fourier conjugation and factor `8` are exact in the stated normalization.
- The distributional proof is rigorous on a Gaussian-regularized Schwartz core;
  rapid decay removes the regulator.
- The Pick/Loewner step uses the complete matrix criterion, not only diagonal
  Laguerre inequalities.
- This lemma supplies a new exact bridge and a sharply reduced positivity target.
- It does not prove the Weyl kernel positive and therefore does not prove the
  requested strict energy bound or RH.