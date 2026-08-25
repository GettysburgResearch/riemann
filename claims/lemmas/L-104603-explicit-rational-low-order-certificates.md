# L-104603 — Explicit rational low-order Conrey certificates

Claim ID: `L-104603`  
Status: **PROVED UNCONDITIONAL CERTIFICATES**  
Created: 2026-08-26  
Depends on: `L-104602`, `X-104620`  
RH status: **not assumed**

All four certificates use `R=1` and `phi(1)=0`.

## 1. Zeroth derivative

Take

\[
m=0,\qquad \phi(x)=1-x.
\]

The exact rational interval replay proves

\[
\mathcal F_0(1,\phi)<e^{7/10}.
\]

Hence

\[
\boxed{\alpha_0>\frac3{10}.}
\tag{L-104603.1}
\]

## 2. First derivative

Take

\[
m=1,\qquad
\phi(x)=1-x+\frac35x(1-x)(1-2x).
\]

This polynomial is admissible because `phi(x)+phi(1-x)=1`. The replay proves

\[
\mathcal F_1(1,\phi)<e^{1/5},
\]

and therefore

\[
\boxed{\alpha_1>\frac45.}
\tag{L-104603.2}
\]

## 3. Second derivative

Take

\[
m=2,\qquad\phi(x)=1-x.
\]

The replay proves

\[
\mathcal F_2(1,\phi)<e^{3/40},
\]

so

\[
\boxed{\alpha_2>\frac{37}{40}=0.925.}
\tag{L-104603.3}
\]

## 4. Third derivative

Take

\[
m=3,\qquad\phi(x)=1-x.
\]

The replay proves

\[
\mathcal F_3(1,\phi)<e^{1/25},
\]

hence

\[
\boxed{\alpha_3>\frac{24}{25}=0.96.}
\tag{L-104603.4}
\]

## 5. Exact arithmetic

At `R=1`,

\[
I_n=\int_0^1x^ne^{2x}\,dx
\]

satisfies

\[
I_0=\frac{e^2-1}{2},
\qquad
I_n=\frac{e^2}{2}-\frac n2I_{n-1}.
\]

Thus every `Phi_m` and `Psi_m` above is affine over `Q(e^2)`.

`X-104620` bounds `e^2`, every square root, every hyperbolic cotangent, and
every comparison exponential by exact `Fraction` Taylor intervals. No
floating-point sign decision appears.

## 6. Scope

These bounds are deliberately simple, independently replayable certificates.
They are not numerical records: Conrey's optimized published table is stronger.
Their role is to establish a trusted end-to-end reconstruction on which a
higher-degree rational optimization can safely build.
