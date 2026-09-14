# L-106434 — Quotient transfer retains the denominator inverse

Claim ID: `L-106434`  
Status: **PROVED EXACT OPERATOR FACTORIZATION; QUOTIENTVIS106440 OPEN FOR XI**  
Created: 2026-08-25  
Depends on: `R-106420`, `R-106432`, `L-106432--L-106433`  
RH status: **not assumed**

Let

\[
U=\frac ND=1+\frac RD,
\qquad R=N-D,
\]

on a finite rational Hardy scope on which all products below are defined.
Assume \(R\) is analytic. For every analytic source vector \(f\),

\[
H_Uf
=
P_-\!\left(\frac RDf\right)
=
H_{1/D}(Rf).
\]

Therefore

\[
\boxed{
H_UP_{\mathcal S}
=
H_{1/D}\,T_RP_{\mathcal S}.
}
\tag{L-106434.1}
\]

This is the exact source-to-physical quotient interface.

## 1. What denominator cancellation proves

Multiplying an observation by \(D\) gives

\[
H_U(Dg)=H_{1/D}(RDg)=P_-(Rg)=0
\]

when \(Rg\) is analytic. Thus denominator multiplication moves the source into
the Hankel kernel; it does not estimate (L-106434.1) on an unmultiplied
conclusion-facing source.

A norm or density estimate for \(R\) controls only \(T_RP_{\mathcal S}\).
To control the actual visible all-pass energy one must also retain

```text
the co-analytic denominator inverse H_(1/D);
its pole/residue or model-space sampling matrix;
the observation map from source coordinates to the scalar Hardy space;
common factors, confluent blocks and finite-window endpoints.
```

## 2. Exact endpoint target

For the endpoint symbol \(U_T=N_T/D_T\) and the literal hard-band projection
\(P_{H_T}\), define

```text
QUOTIENTVIS106440(q):

limsup_(T->infinity)
  || H_(1/D_T) T_(N_T-D_T) P_(H_T) ||_HS^2
  / N(T,2T)
< q.
```

By (L-106434.1), this is exactly the statement

\[
\limsup
\frac{\|H_{U_T}P_{H_T}\|_{\mathcal S_2}^2}{N(T,2T)}
<q.
\]

The value \(q=1/600\) would recover the numerical allowance proposed in
`T-106430`, but it is not proved by the source-density ratio
\(\mathfrak r_L<1/600\).

## 3. Equivalent divisor form

`L-106433` converts `QUOTIENTVIS106440(q)` into a Cauchy--exponential
quadratic-form estimate over the actual endpoint companion pole divisor.
This is an explicit finite matrix theorem, not an unspecified transfer norm.

## 4. Scope

The factorization is exact. It supplies no uniform bound for \(H_{1/D_T}\);
near-boundary companion poles make such a bound topology-sensitive. That is
precisely the information erased by denominator cancellation.
