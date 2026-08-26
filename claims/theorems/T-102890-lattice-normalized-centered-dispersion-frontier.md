# T-102890 — Lattice-normalized derivative detector and centered dispersion frontier

Claim ID: `T-102890`  
Status: **MAJOR UNCONDITIONAL ARITHMETIC REDUCTION; RH UNPROVED**  
Created: 2026-08-24  
Base: PR #719  
RH status: **unproved**

The latest stopped-Vaughan layer is corrected and recompiled around the logarithmic derivative of the fixed outer kernel.

## 1. Binding correction

`R-102868` proves that the unrestricted `R_L` Type-I term is

\[
4(\sqrt2-1)(\log2)^2
\left(\sum_{d\le Y^{1/6}}{\mu(d)\over d}\right)^2
+O(Y^{-1/6}).
\]

The main term is favorable but not power-small.  Only its negative part is `O(Y^(-1/6))`.  The former whole-magnitude claim is rejected.

## 2. Zero-moment derivative detector

Put

\[
K_L=DR_L.
\]

Then

\[
\int_1^8K_L(y){dy\over y}=0
\]

and

\[
\sum_{m\ge1}{1\over m}K_L(Z/m^2)=O(Z^{-1/2}).
\]

Consequently the unrestricted derivative Type-I lattice is `O(Y^(-1/6))` in absolute value.

The derivative observation is fixed and zero-safe.  Its negative-mass criterion implies the original outer criterion by the positive Volterra identity

\[
H_R(X)=\int_1^XH_K(t){dt\over t}.
\]

Therefore

\[
\boxed{
\int_1^Y(H_K)_-{dX\over X}=Y^{o(1)}
\Longrightarrow
\mathrm{RH}.
}
\tag{T-102890.1}

## 3. Exact stopped source

`L-102881` gives the literal stopped derivative decomposition

\[
\mathcal C^K_{p,q}
=(\mathcal T^K_{p,q})^{\rm full}
+(\mathcal T^K_{p,q})^{\rm bdry}
+\mathcal B^K_{p,q}.
\]

The full lattice is closed.  The two retained source rows are:

```text
KSCB102881:
  the derivative smooth-boundary current;

KBCQDSP102881:
  the stopped balanced Type-II current.
```

No unrestricted integer or zero phase is substituted for either row.

## 4. Coherent nonzero-phase packing

`L-102882` proves the exact centered phase kernel

\[
\sum_{\mathbf h\ne0}\|S_{\mathbf h}\|^2
=
\sum_{b,b'}\langle c_b,c_{b'}\rangle
\prod_i
[\ell_i\mathbf1_{\ell_i\mid b^2-b'^2}-1].
\]

`L-102883` then sums entire dyadic prime families with their natural weights.  For a core octave `B<=b<2B`, semiprime source weight `Q`, and two modulus ranges `L_1,L_2`,

\[
\boxed{
\mathcal E
\ll {Y^{o(1)}\over Q}
\left[
1+{L_1L_2\over B\log(2L_1)\log(2L_2)}
\right].
}
\tag{T-102890.2}

Thus the complete coherent **weighted** long-core phase transform is subpower whenever

\[
B\ge L_1L_2.
\]

This is a global packing theorem, not a sum of fixed-quadruple bounds.

## 5. Smooth-boundary source costs

`L-102884` proves that the derivative smooth boundary has:

```text
free source energy                    O((log log Y)^2);
equal-product collapse                Y^o(1).
```

Its only remaining operation is a distinct-product cross-owner restriction, of the same physical type as the stopped balanced current.

## Exact remaining theorem

Define

```text
SLCD102890:
  after exact carrier, gauge, stopped-prime and owner recombination,
  the combined distinct-product centered-dispersion current consisting of

    (i) the derivative smooth boundary, and
    (ii) the stopped balanced blocks not covered by the weighted long-core
         theorem T-102890.2,

  has subpower logarithmic negative mass in the fixed ratio-eight derivative
  observation.
```

Then

\[
\boxed{
\mathrm{SLCD}_{102890}
\Longrightarrow
\int_1^Y(H_K)_-{dX\over X}=Y^{o(1)}
\Longrightarrow
\mathrm{OER}_{102780}
\Longrightarrow
\mathrm{RH}.
}
\tag{T-102890.3}

The owner weights used in (T-102890.2) are one source resource.  A fixed-pair argument which first spends them against phase cardinality may not reuse them in the coherent energy theorem.

```text
R_L Type-I sign/magnitude correction       PROVED EXACT
zero-moment derivative detector            PROVED EXACT
unrestricted derivative Type-I             PROVED POWER-SMALL
stopped derivative Vaughan                  PROVED EXACT
centered nonzero-phase identity             PROVED EXACT
coherent weighted long-core packing         PROVED
smooth-boundary source/equal products       PROVED SUBPOWER
SLCD102890                                  OPEN / RH-BEARING
Riemann Hypothesis                          UNPROVED
```
