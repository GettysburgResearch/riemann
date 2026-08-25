# T-106440 — Corrected hard-band signed spectral frontier for ninety percent

Claim ID: `T-106440`  
Status: **UNCONDITIONAL EXACT REDUCTION; ACTUAL XI SPECTRAL ESTIMATE OPEN**  
Created: 2026-08-25  
Depends on: `L-105290`; `L-106400`; `L-106431--L-106433`; `R-106432`  
RH status: **unproved**

`T-106430` correctly replaces absolute model-space coverage by a signed
source/complement index.  Its inherited visible cost `<1/600`, however, was a
source-density estimate rather than a bound for the actual compressed Hankel
operator.  This theorem records the corrected conclusion-facing statement.

## 1. Literal visible and complement quantities

Let `U_T` be the reduced endpoint all-pass quotient on a cofinal regular Xi
window.  Choose a predeclared hard Paley--Wiener bandwidth `H_T>0` and define

\[
\boxed{
V_T
 =\int_0^\infty
  \min(H_T,\xi)|\widehat U_T(-\xi)|^2d\xi.
}
\tag{T-106440.1}

Define the signed unobserved tail

\[
\boxed{
\Delta_T
 =\int_{H_T}^\infty(\xi-H_T)
  \left(
   |\widehat U_T(-\xi)|^2
   -|\widehat U_T(\xi)|^2
  \right)d\xi.
}
\tag{T-106440.2}

At finite rational scope these are exactly the visible negative Hankel charge
and the signed complement charge.  By `L-106433`, both are explicit confluent
residue/exponential Cauchy Grams at the endpoint companion poles and zeros.

## 2. Correct endpoint descent

`L-106431/L-106432` give

\[
-\operatorname{wind}U_T
\le V_T+(\Delta_T)_+.
\]

The endpoint companion identity gives, with the declared endpoint and
confluent ledger,

\[
\boxed{
R_0(T,2T)
\ge
R_2(T,2T)-V_T-(\Delta_T)_+-o(N(T,2T)).
}
\tag{T-106440.3}

No denominator-multiplied source, inverse Gram, or absolute coverage
hypothesis occurs in (T-106440.3).

## 3. Exact ninety-percent target

The pinned unconditional fixed-order input is

\[
\liminf_{T\to\infty}{R_2(T,2T)\over N(T,2T)}
>{599\over625}.
\]

Its margin above ninety percent is

\[
{599\over625}-{9\over10}
={73\over1250}.
\]

Define

```text
HARDSIGNED106440:

limsup_(T->infinity)
 [ V_T + (Delta_T)_+ ] / N(T,2T)
 < 73/1250.
```

Then

\[
\boxed{
\mathrm{HARDSIGNED}_{106440}
\Longrightarrow
\liminf_{T\to\infty}
{N_0(T,2T)\over N(T,2T)}>0.9.
}
\tag{T-106440.4}

A convenient but strictly stronger two-row version is

\[
\boxed{
\limsup {V_T\over N}< {1\over600},
\qquad
\limsup {(\Delta_T)_+\over N}< {851\over15000}.
}
\tag{T-106440.5}

The first row of (T-106440.5) concerns the actual all-pass quotient.  It is not
proved by the four-channel source-density constant.

## 4. Residue-matrix normal form

For simple upper companion poles `b_j=a_j+i y_j`, write

\[
\widehat U_T(-\xi)=\sum_jc_je^{ib_j\xi}.
\]

Then

\[
V_T
 =\sum_{j,k}c_j\overline{c_k}
 {1-e^{-H_T\alpha_{jk}}\over\alpha_{jk}^2},
\qquad
\alpha_{jk}=y_j+y_k-i(a_j-a_k).
\]

The complement has the same matrix with numerator
`e^(-H_T alpha_(jk))`, and the favorable channel is subtracted before taking
the positive part.  Confluent zeros are handled by derivatives of these
kernels.

Thus `HARDSIGNED106440` is an explicit weighted shallow-companion-residue
estimate with a fixed allowance of `5.84%` of the zero-count scale.

## 5. Relation to the positive Xi source hierarchy

The exact source inequalities `L-106410--L-106413` and the actual current--
Turan hierarchy on sibling PR #729 remain potentially useful for proving
`HARDSIGNED106440`.  What is still required is a theorem transporting those
diagonal source inequalities through the meromorphic quotient and physical
all-pass map.  Equivalently, one may estimate the residue Grams above
directly.

## 6. Boundary

```text
endpoint all-pass telescope                         PROVED EXACT
actual Xi exterior-square Turan source               PROVED UNCONDITIONALLY
four-channel analytic source-density contraction     PROVED EXACT
source density -> visible quotient Hankel cost       REFUTED GENERICALLY
hard-band visible trace formula                      PROVED EXACT
signed complement spectral-tail formula              PROVED EXACT
confluent residue/exponential Gram                    PROVED EXACT
HARDSIGNED106440                                     OPEN / RECORD-BEARING
ninety percent for zeta                              UNPROVED
density one / RH                                     UNPROVED
```
