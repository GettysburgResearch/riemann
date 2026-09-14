# T-106610 — Fifth-residue coherence and projective-variation gates for more than ninety percent

Claim ID: `T-106610`  
Status: **UNCONDITIONAL EXACT COMPOSITION; RESCOH106610 / RESEDGE106610 OPEN**  
Created: 2026-08-26  
Depends on: `L-106610--L-106611`; `L-105102`; branch-pinned \(R_5/N>997/1000-o(1)\)  
RH status: **unproved**

Let \(c_j\) be the ordered simple real zeros of \(\Xi^{(5)}\) on one cofinal
regular window, and put

\[
\rho_j=\frac{\Xi(c_j)}{\Xi^{(6)}(c_j)}.
\]

Remove and credit common Xi zeros. Retain the multiple, confluent and endpoint
charge as \(\mathcal E_{\rm reg}(T)\).

Define

\[
\mathfrak C_5(T)
=
\frac{\left|\sum_j\rho_j\right|^2}
     {M_T\sum_j\rho_j^2}
\tag{T-106610.1}
\]

and the projective edge energy

\[
\mathfrak E_5(T)
=
\sum_j
\frac{(\rho_{j+1}-\rho_j)^2}
     {\rho_j^2+\rho_{j+1}^2}.
\tag{T-106610.2}
\]

## 1. Two exact sufficient routes

`L-106610--L-106611` give

\[
R_0(T,2T)
\ge
(2\mathfrak C_5(T)-1)M_T
-\mathcal E_{\rm reg}(T)-O(1),
\tag{T-106610.3}
\]

and independently

\[
R_0(T,2T)
\ge
M_T-\mathfrak E_5(T)
-\mathcal E_{\rm reg}(T)-O(1).
\tag{T-106610.4}
\]

Therefore either of the following conclusion-facing statements is sufficient.

```text
RESCOH106610:
  M_T/N > 997/1000-o(1),
  E_reg=o(N),
  liminf C_5 > 1897/1994;

RESEDGE106610:
  M_T/N > 997/1000-o(1),
  limsup [E_5+E_reg]/N < 97/1000.
```

Under either statement,

\[
\boxed{
\liminf_{T\to\infty}
\frac{N_0(T,2T)}{N(T,2T)}
>0.9.
}
\tag{T-106610.5}
\]

## 2. Exact contour interface

The first two moments in (T-106610.1) are precisely the real critical-residue
moments in `L-105102`:

\[
-\sum_j\rho_j=\Phi_1-C_1,
\qquad
\sum_j\rho_j^2=B-C_2-D_2.
\tag{T-106610.6}
\]

Thus `RESCOH106610` is not an unidentified sign condition. It is the explicit
fixed-order inequality

\[
\boxed{
\frac{(\Phi_1-C_1)_+^2}
     {M_T(B-C_2-D_2)}
>
\frac{1897}{1994},
}
\tag{T-106610.7}
\]

with the literal boundary, nonreal-critical and adjacent-derivative Bézout
terms retained.

The projective route is more local. It asks for one graph-Dirichlet energy of
the same residues and may be attacked by adjacent-window Poisson/Bézout
localization without proving a uniform residue magnitude.

## 3. Relation to the all-pass gates

The fifth-endpoint all-pass charge of `T-106540`, the shallow canonical
correlation of `T-106590/T-106600`, and the residue gates above all measure the
same reverse–Rolle loss but in different coordinates:

```text
all-pass phase angle:     continuous oriented boundary charge;
canonical correlation:   model-space overlap deficit;
residue coherence:        global first/second critical moments;
projective edge energy:   discrete sign-variation charge.
```

No implication from positive Fourier source alone to any one of these
conclusion estimates is asserted.

## Boundary

```text
fifth-residue sign-transition identity          PROVED EXACT
coherence -> transition count                    PROVED EXACT
projective energy -> transition count            PROVED EXACT
exact 1897/1994 and 97/1000 constants            PROVED EXACT
contour moment identification                    INHERITED EXACT
RESCOH106610 / RESEDGE106610                      OPEN / 90%-BEARING
ninety percent for zeta                          UNPROVED
density one / RH                                 UNPROVED
```
