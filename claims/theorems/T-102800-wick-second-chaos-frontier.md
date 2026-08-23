# T-102800 — The prime-carrier-quotiented defect is one root-free Wick second-chaos restriction

Claim ID: `T-102800`  
Status: **MAJOR UNCONDITIONAL CHAOS REDUCTION; RH UNPROVED**  
Created: 2026-08-23  
Base: PR #719  
RH status: **unproved**

The live common-mother programme had reduced its conclusion-facing scalar to
the carrier-subtracted outer-ray current `OER102780`.

`L-102741--L-102743` now identify the exact source after that carrier quotient.

## 1. Exact Wick decomposition

For labelled prime shifts `x_l=p_l^(-1/2)U_l`, put

```text
E = product_l (1-x_l),
S = product_l (1-x_l^2),
L = sum_l x_l,
R = product_l exp(x_l)/(1+x_l).
```

Then

\[
E=SRe^{-L}.
\]

After moving the exact gauge-covariant prime carrier

\[
\mathcal P_{\rm W}=-RSL
\]

once, the remainder is

\[
\boxed{
\mathcal D_{\ge2}
=RS\int_0^1(1-t)W_t^2dt+(R-1)S,
\qquad
W_t=Le^{-tL/2}.
}
\tag{T-102800.1}
\]

Every `W_t` is root-free. The complete first chaos is absent.

## 2. Closed costs

Uniformly for `0<=t<=1` and every horizon `Y`:

```text
Wick and squared gauges                    polylogarithmic;
free labelled W_t^2 energy                polylogarithmic;
same-product convolution multiplicity     subpower;
duplicate-67 owner multiplicity           constant;
root and singleton-prime carrier           removed exactly once.
```

Thus neither the root, first chaos, labelled Fock energy nor same-product
collapse remains conclusion-bearing.

## 3. Exact remaining current

Let `O_*` denote the fixed carrier-centered outer-ray observation of
`T-102780`, including the exact regional and gauge recombinations already
frozen on PR #719. Define

\[
\mathcal J_{\rm Wick}(X)
=
\int_0^1(1-t)
\,\mathcal O_*[RSW_t^2](X)\,dt.
\tag{T-102800.2}
\]

The gauge boundary `(R-1)S` has only subcritical source activity and is charged
in the already-closed polylogarithmic ledger.

The final arithmetic statement is

```text
WNC102743:
  after exact greatest-owner and source-region recombination, the
  distinct-product physical restriction of J_Wick has subpower logarithmic
  negative mass.
```

Then

\[
\boxed{
\mathrm{WNC}_{102743}
\Longrightarrow
\mathrm{OER}_{102780}
\Longrightarrow
\mathrm{AR\!-\!DEFECT}_{102600}
\Longrightarrow
\mathrm{RH}.
}
\tag{T-102800.3}
\]

The first implication is exact modulo the closed polylogarithmic gauge term and
the exact prime-carrier transfer. The final arrows are the fixed outer-ray and
Mellin--Landau consumers already proved on this branch.

## 4. Relation to the half-divisor frontier

`WNC102743`, `PHDNC102710` and `HDNC102703` are three gauges of the same
physical cross-owner restriction:

```text
Wick gauge:
  no first chaos; identical root-free square field;

half-divisor gauge:
  ratio-four two-field factorization;

Euler gauge:
  exact owner/activation cancellation.
```

The Wick gauge is the sharpest chaos normal form: the hard packet begins at two
distinct prime labels and has polylogarithmic free energy.

## Exact boundary

```text
Wick factorization                         PROVED EXACT
prime-carrier quotient                     PROVED EXACT
root-free second-chaos square              PROVED EXACT
free labelled energy                       PROVED POLYLOG
same-product collapse                      PROVED SUBPOWER
physical distinct-product restriction      OPEN / RH-BEARING
Riemann Hypothesis                         UNPROVED
```
