# L-105281 — Wrong extrema are adjacent all-pass negative winding

Claim ID: `L-105281`  
Status: **PROVED EXACT AT FINITE REGULAR SCOPE**  
Created: 2026-08-24  
Depends on: L-105280; exact Rolle count; degree formula for circle-valued H^(1/2) maps  
RH status: not assumed

Let \(p_k=p^{(k)}\).  For positive parameters \(\lambda_k\), put

\[
\Theta_k=\Theta_{\lambda_k,p_k}.
\]

Let \(E_k\) be the number of nonreal conjugate pairs lost when differentiating
from \(p_{k-1}\) to \(p_k\); equivalently, the number of wrong extrema at that
step.  Degree and Rolle counting give

\[
R(p_{k-1})-R(p_k)=1-2E_k.
\tag{1}
\]

Let

\[
A(x)=\frac{x-i}{x+i},
\qquad \operatorname{wind}_{\mathbb R}A=1,
\]

and define

\[
\boxed{
U_k(x)=\frac{\Theta_{k-1}(x)}{A(x)\Theta_k(x)}.
}
\tag{2}
\]

Then L-105280 and (1) give

\[
\boxed{
\operatorname{wind}_{\mathbb R}U_k=-2E_k.
}
\tag{3}
\]

After the Cayley compactification of the real line, write

\[
U_k(e^{it})=\sum_{m\in\mathbb Z}\widehat U_k(m)e^{imt}.
\]

For every circle-valued \(H^{1/2}\) map, the degree formula is

\[
\operatorname{deg}U_k
=\sum_{m\in\mathbb Z}m|\widehat U_k(m)|^2.
\tag{4}
\]

Consequently

\[
\boxed{
2E_k
\le
\sum_{m<0}|m|\,|\widehat U_k(m)|^2
\le
\|U_k\|_{\dot H^{1/2}}^2.
}
\tag{5}
\]

This is a true conclusion-facing carrier: every wrong extremum costs two units
of negative topological winding, and negative winding must be paid by a
half-derivative Hardy energy.

## Pointwise Lorentz coordinate

At a real point where the ratios are finite, put

\[
a=\lambda_{k-1}\frac{p_k}{p_{k-1}},
\qquad
b=\lambda_k\frac{p_{k+1}}{p_k},
\qquad
\vartheta(t)=\frac{1-it}{1+it}.
\]

Then \(\Theta_{k-1}=\vartheta(a)\) and
\(\Theta_k=\vartheta(b)\).  The exact algebraic identity

\[
\boxed{
\left|-\frac{\vartheta(a)}{\vartheta(b)}-1\right|^2
=
\frac{4(1+ab)^2}{(1+a^2)(1+b^2)}
}
\tag{6}
\]

shows that the adjacent all-pass defect is the continuous Lorentz-normalized
version of the residue square defect.  The monochromatic relation \(ab=-1\)
annihilates it exactly.

Equation (6) controls an \(L^2\) defect.  Equation (5) shows why the actual
Levinson problem requires the stronger \(H^{1/2}\) control: arbitrarily narrow
phase slips carry integer winding while having arbitrarily small ordinary
\(L^2\) mass.
