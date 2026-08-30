# R-108300 — Positive Fourier source does not orient the direct fifth companion phase

Claim ID: `R-108300`  
Status: **PROVED EXACT COUNTERMODEL**  
Created: 2026-08-31  
RH status: **not assumed**

Fix \(c>1\) and \(n\ge1\), and put

\[
F(t)=c+\cos(nt).
\]

Its Fourier source is the positive even measure

\[
c\,\delta_0+\frac12\delta_n+\frac12\delta_{-n}.
\]

Moreover,

\[
F^{(5)}(t)=-n^5\sin(nt),
\qquad
F^{(6)}(t)=-n^6\cos(nt).
\]

At \(c_j=j\pi/n\),

\[
\rho_j={F(c_j)\over F^{(6)}(c_j)}
=
\begin{cases}
-(c+1)n^{-6},&j\text{ even},\\
(c-1)n^{-6},&j\text{ odd}.
\end{cases}
\]

Thus every adjacent residue edge changes sign, while \(F\) has no real zero.

The fifth Wronskian is

\[
\boxed{
F'F^{(5)}-FF^{(6)}
=
n^6(1+c\cos nt).
}
\tag{R-108300.1}
\]

It too has a positive even Fourier source,

\[
n^6\delta_0+
\frac{cn^6}{2}\delta_n+
\frac{cn^6}{2}\delta_{-n},
\]

but is negative whenever \(\cos(nt)<-1/c\).

Therefore none of the following implies the open Xi phase estimate:

```text
positive even Fourier source for F;
positive even Fourier source for the fifth Wronskian;
all fifth-derivative zeros simple and real;
arbitrarily small companion scale;
exact direct endpoint phase algebra.
```

The missing theorem must use more of the actual Xi source than positivity or
a diagonal Fourier-density comparison.
