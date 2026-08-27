# R-105360 — A positive terminal slope alone does not certify the origin Stieltjes hierarchy

Claim ID: `R-105360`  
Status: **PROVED EXACT ABSTRACT SCOPE REFUTATION**  
Created: 2026-08-23  
Depends on: `L-105350--L-105351`  
RH status: **not assumed**

## 1. Exact odd separator

Put

\[
\boxed{H(z)=z-z^3.}
\tag{R-105360.1}
\]

This function is entire, odd, real on the real axis, and has positive slope

\[
H'(0)=1.
\]

Its origin Hamburger moments are

\[
m_0=1,
\qquad
m_1=0,
\qquad
m_2=-1,
\qquad
m_n=0\quad(n\ge3).
\]

Therefore the second confluent matrix is

\[
\boxed{
\mathsf L_2(0)
=\begin{pmatrix}1&0\\0&-1\end{pmatrix},
\qquad
\det\mathsf L_2(0)=-1<0.
}
\tag{R-105360.2}
\]

Equivalently, in the Stieltjes parity split,

\[
\beta_0=1,
\qquad
\beta_1=-1,
\]

so the shifted one-by-one Hankel block is already negative.

## 2. Consequence for terminal reductions

A statement of the form

```text
H_N'(0) >= 0 at one far boundary
```

controls only the total candidate Stieltjes mass. It gives no sign for the
nonlinear Taylor coefficients and does not imply that `H_N` is a Pick or
Stieltjes function.

Thus the terminal condition in a valid exhaustion theorem must control the
complete nonlinear germ. An affine terminal limit

\[
H_N(z)\longrightarrow az,
\qquad a\ge0,
\]

is sufficient because every higher origin moment vanishes in the limit. A
positive terminal slope without affine-germ control is not.

## 3. Binding firewall

```text
positive terminal slope                         INSUFFICIENT;
positive beta_0 only                             INSUFFICIENT;
vanishing of every higher terminal beta_n        LOAD BEARING;
local uniform terminal convergence to a z        SUFFICIENT TERMINAL FORM.
```

The separator is abstract and is not claimed to arise from Xi. It rules out a
source-free shortcut from one first derivative to the complete all-order
boundary hierarchy.
