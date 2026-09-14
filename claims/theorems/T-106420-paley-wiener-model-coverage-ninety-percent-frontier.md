# T-106420 — One-matrix Paley--Wiener coverage frontier for ninety percent

Claim ID: `T-106420`  
Status: **UNCONDITIONAL REDUCTION TO ONE EXPLICIT SAMPLING TRACE; PWSAMP106420 OPEN**  
Created: 2026-08-24  
Depends on: `L-106400--L-106416`; pinned fixed-order bound `R_2/N>599/625-o(1)`  
RH status: **unproved**

## 1. Complete endpoint source package

Choose

\[
L_T=\log T,
\qquad
\lambda_T=\frac1{200\log T}.
\]

Then \(\lambda_TL_T=1/200\).  The following rows are now proved independently:

```text
endpoint two-rung all-pass telescope             L-106400;
actual Xi exterior-square Hankel numerator       L-106401;
finite four-channel endpoint bank                 L-106413;
complete four-channel source cost < 1/600         L-106410--L-106411;
common-factor/confluent finite ledger             L-105500, L-106413;
Xi Fourier tail at L_T=log T                      L-106414;
model-space sampling matrix normal form           L-106415;
coverage-to-complete-Hankel conversion             L-106416.
```

No frozen-to-actual numerator transfer or generic contour-error term remains.

## 2. The single open matrix

Let \(U_T\) be the reduced endpoint all-pass symbol on a regular dyadic window,
and write

\[
U_T=\omega_T\frac{B_{+,T}}{B_{-,T}}.
\]

Let \(\mathcal S_T\) be the predeclared hard one-sided Paley--Wiener source frame
of `L-106413`, of dimension

\[
\boxed{
d_T=\left(\frac{999}{1000}+o(1)\right)N(T,2T).
}
\tag{T-106420.1}

Form the explicit confluent sampling matrix

\[
\mathcal C_T
=G_T^{-1/2}A_TA_T^*G_T^{-1/2}
\]

of `L-106415`, using every zero and multiplicity jet of \(B_{-,T}\).  It is a
positive contraction on the bad companion model space \(K_{B_{-,T}}\).

Define

\[
\boxed{
\mathrm{PWSAMP}_{106420}:\qquad
\operatorname{tr}(I-\mathcal C_T)_+=o(N(T,2T)).
}
\tag{T-106420.2}

This is one explicit finite-matrix asymptotic.  Its entries are normalized
Paley--Wiener kernel values and jets at the companion zeros; no unknown signs
occur in its definition.

## 3. Conditional conclusion

Let \(H_T=H_{U_T}\).  The four-channel source theorem gives

\[
\|H_TP_{\mathcal S_T}\|_{\mathcal S_2}^2
\le
\left(\frac1{600}+o(1)\right)d_T.
\tag{T-106420.3}

Under `PWSAMP106420`, apply `L-106416` with \(a=1/2\):

\[
\|H_T\|_{\mathcal S_2}^2
\le
\left(\frac2{600}+o(1)\right)d_T.
\tag{T-106420.4}

The endpoint all-pass telescope of `L-106400` gives

\[
R_0(T,2T)
\ge R_2(T,2T)-\|H_T\|_{\mathcal S_2}^2-o(N(T,2T)).
\]

Using the pinned unconditional fixed-order input

\[
\frac{R_2(T,2T)}{N(T,2T)}
>\frac{599}{625}-o(1),
\]

one obtains

\[
\boxed{
\mathrm{PWSAMP}_{106420}
\Longrightarrow
\liminf_{T\to\infty}
\frac{N_0(T,2T)}{N(T,2T)}
>\frac{95507}{100000}
=0.95507.
}
\tag{T-106420.5}

Using the exact source constant instead of \(1/600\) gives the sharper
conditional value

\[
0.9551547236\ldots .
\]

## 4. Scientific meaning

The remaining theorem is no longer:

```text
an all-pass H^(1/2) transfer;
a contour-edge estimate;
a frozen-to-Xi numerator comparison;
a phase-cardinality or physical-occupancy estimate;
a generic zero-separation hypothesis.
```

It is the one-sided lower spectral mass of a completely specified sampling
matrix.  Near collisions are included through confluent derivative kernels.
A proof may use Xi-specific companion-zero geometry, de Branges sampling,
Carleson embedding, a large-sieve trace, or an averaged cluster theorem, but it
must prove (T-106420.2) for the literal matrix.

## 5. Boundary

```text
complete endpoint source package                    PROVED
explicit confluent sampling matrix                  PROVED EXACT
source energy < 1/600                               PROVED EXACT
coverage-to-Hankel charge                           PROVED EXACT
PWSAMP106420 sampling trace                         OPEN / RECORD-BEARING
conditional line fraction > 95.507%                 PROVED IMPLICATION
ninety percent for zeta                             UNPROVED
density one                                         UNPROVED
Riemann Hypothesis                                  UNPROVED
```
