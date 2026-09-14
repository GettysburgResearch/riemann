# L-105280 — Companion all-pass winding equals the real-root count

Claim ID: `L-105280`  
Status: **PROVED EXACT FOR REGULAR REAL POLYNOMIALS; ENTIRE-WINDOW VERSION BY EXHAUSTION**  
Created: 2026-08-24  
Depends on: L-104510  
RH status: not assumed

Let \(p\in\mathbb R[x]\) have degree \(n\), with \(\gcd(p,p')=1\), and let
\(\lambda>0\).  Put

\[
E_-(z)=p(z)-i\lambda p'(z),
\qquad
E_+(z)=p(z)+i\lambda p'(z),
\]

and define the real-axis all-pass function

\[
\boxed{
\Theta_{\lambda,p}(x)=\frac{E_-(x)}{E_+(x)}.
}
\tag{1}
\]

For real \(x\), \(E_+(x)=\overline{E_-(x)}\), so
\(|\Theta_{\lambda,p}(x)|=1\).  Moreover \(\Theta\to1\) at both ends of the
compactified real line.

Let \(N_\pm(E_-)\) denote the numbers of zeros of \(E_-\) in the upper and
lower half-planes.  The upper-half-plane argument principle gives

\[
\Delta_{\mathbb R}\arg E_-
=2\pi N_+(E_-)-n\pi
=\pi\bigl(N_+(E_-)-N_-(E_-)\bigr).
\tag{2}
\]

Since the phase of \(E_+\) is the negative of the phase of \(E_-\) on the
real line,

\[
\operatorname{wind}_{\mathbb R}\Theta_{\lambda,p}
=N_+(E_-)-N_-(E_-).
\tag{3}
\]

By the exact Hermite--Biehler index theorem L-104510, the right side is the
number \(R(p)\) of real zeros of \(p\).  Therefore

\[
\boxed{
\operatorname{wind}_{\mathbb R}\Theta_{\lambda,p}=R(p).
}
\tag{4}
\]

The identity is independent of \(\lambda>0\).

For multiple real roots, cancel the common factor of \(E_-\) and \(E_+\), or
pass through regular perturbations.  The winding then counts distinct real
roots, with the confluent correction recorded separately.

For a real entire function of genus at most one, the same identity holds on a
bounded regular window after canonical-product exhaustion, with only the two
endpoint phase charges.  This is a conclusion-facing non-holomorphic index;
it is not subject to the holomorphic carrier cancellation of R-105270.
