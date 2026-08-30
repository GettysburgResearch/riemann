# T-108300 — Direct fifth-companion minority-phase frontier for ninety percent

Claim ID: `T-108300`  
Status: **EXACT SINGLE-COMPANION REDUCTION; XI ESTIMATE AND NINETY PERCENT OPEN**  
Created: 2026-08-31  
Base: PR #773 at `8d28e706de724c8a6a66fa1980bf4ef879871ae2`  
RH status: **unproved**

For \(F=\Xi\), define

\[
G=F^{(5)},\qquad
W_5=F'F^{(5)}-FF^{(6)}
\]

and, on a regular dyadic height window,

\[
\mathscr U_{\sigma,\varepsilon}(T)
=
{1\over\pi}\int_T^{2T}
{\varepsilon(-\sigma W_5(t))_+
\over G(t)^2+\varepsilon^2F(t)^2}\,dt.
\]

`L-108300` proves that the limits as \(\varepsilon\downarrow0\) count the two
signs of the fifth residues

\[
{\Xi(c)\over\Xi^{(6)}(c)}
\]

at simple real zeros \(c\) of \(\Xi^{(5)}\). `L-108301` proves the exact
direct descent

\[
\boxed{
N_0(T,2T)
\ge
M_5(T,2T)-1
-
2\min_{\sigma=\pm1}
\lim_{\varepsilon\downarrow0}
\mathscr U_{\sigma,\varepsilon}(T)
-
\mathcal E_{\rm reg}(T).
}
\tag{T-108300.1}
\]

The complete five-rung screened-curvature sum from T-107200 is not required
for this percentage theorem.

Define `XI5MINPHASE108300` by

\[
\boxed{
\limsup_{T\to\infty}
{
2\min_\sigma\lim_{\varepsilon\downarrow0}
\mathscr U_{\sigma,\varepsilon}(T)
+
\mathcal E_{\rm reg}(T)
\over N(T,2T)}
<
{863\over10000},
}
\tag{T-108300.2}
\]

when using the inherited simple-real fifth-derivative input
\(M_5/N>9863/10000-o(1)\). Then

\[
\boxed{
\mathrm{XI5MINPHASE}_{108300}
\Longrightarrow
\liminf_{T\to\infty}{N_0(T,2T)\over N(T,2T)}
>{9\over10}.
}
\tag{T-108300.3}
\]

With an input \(M_5/N>997/1000-o(1)\), the right side of
(T-108300.2) may be replaced by \(97/1000\).

## What was attempted

The direct current \(W_5\) has the positive Fourier-density structure already
identified in the Xi endpoint programme. `R-108300` proves that this fact,
even together with complete real-rootedness of the fifth derivative, cannot
orient the phase variation in the ambient positive-source class. Hence a
formal promotion from positive source density would be false.

The surviving analytic target is one literal Xi statement:

```text
XI5MINPHASE108300:
  bound the minority negative phase variation of
  Xi^(5)+i sigma epsilon Xi at the exact threshold above,
  retaining common zeros, multiplicities and endpoints.
```

It is smaller than the former source-Pick/free-energy gate and smaller than
the five-rung curvature sum, but it remains unproved.

```text
direct companion identity                    PROVED EXACT
direct residue-sign counting                 PROVED EXACT
minority transition bound                    PROVED EXACT
single-companion 90% implication             PROVED EXACT
positive-source formal closure               REFUTED
XI5MINPHASE108300                             OPEN
more than 90 percent                         UNPROVED
density one / RH                             UNPROVED
```
