# T-106540 — Corrected oriented fifth-endpoint phase-angle majorant for more than ninety percent

Claim ID: `T-106540`  
Status: **UNCONDITIONAL SCALAR MAJORANT REDUCTION; ONE POSITIVE PHASE-ANGLE MEAN OPEN**  
Created: 2026-08-25  
Corrected: 2026-08-26  
Depends on: `L-106500`, `L-106501`, corrected `L-106514`; the pinned
\(R_5/N>997/1000-o(1)\) input  
RH status: **unproved**

Let \(F=\Xi\), and on each cofinal regular window form the reduced endpoint
quotient

\[
U_{5,\lambda_T}
=
\frac{
(F-i\lambda_TF')(F^{(5)}+i\lambda_TF^{(6)})
}{
(F+i\lambda_TF')(F^{(5)}-i\lambda_TF^{(6)})
}.
\]

Normalize its finite inner factors at infinity and let
\(\beta_{5,\lambda_T}'\) be the positive boundary phase density of the reduced
denominator inner factor.

The original version of this theorem called the phase statistic the exact
Hankel charge.  `L-106514` now proves the correct majorization and
`R-106640` gives a one-pole strict counterexample to equality.

## 1. Correct scalar majorant

Put

\[
\mathcal L_5=F'F^{(5)}-FF^{(6)}.
\]

Then

\[
\boxed{
\|H_{U_{5,\lambda_T}}\|_{\mathcal S_2}^2
\le
\frac{\lambda_T^2}{\pi}
\int_{\mathbb R}
\beta_{5,\lambda_T}'(t)
\frac{\mathcal L_5(t)^2}
{(F^2+\lambda_T^2F'^2)
 ((F^{(5)})^2+\lambda_T^2(F^{(6)})^2)}
\,dt.
}
\tag{T-106540.1}
\]

The right side is nonnegative and sharply denominator-oriented.  It pays
neither favorable numerator degree nor an artificial inverse-frame condition
number, but it may exceed the exact canonical defect by the cross-Hankel
phase-alignment slack of `L-106514.9`.

## 2. Sufficient condition

Define `ORIENTEDANGLE106540` by

\[
\boxed{
\limsup_{T\to\infty}\frac1{N(T,2T)}
\left[
\frac{\lambda_T^2}{\pi}
\int
\beta_{5,\lambda_T}'
\frac{\mathcal L_5^2}
{(F^2+\lambda_T^2F'^2)
 ((F^{(5)})^2+\lambda_T^2(F^{(6)})^2)}
\,dt
+\mathcal E_{\rm reg,T}
\right]
<
\frac{97}{1000},
}
\tag{T-106540.2}
\]

where \(\mathcal E_{\rm reg,T}\) is the literal common-zero, confluent,
finite-window, and cofinal-exhaustion ledger.

By (T-106540.1), this condition bounds the exact adverse Hankel charge by the
same allowance.  The endpoint index identity gives

\[
R_0(T,2T)
\ge
R_5(T,2T)
-\|H_{U_{5,\lambda_T}}\|_{\mathcal S_2}^2
-o(N).
\]

Together with

\[
\liminf\frac{R_5(T,2T)}{N(T,2T)}>\frac{997}{1000},
\]

one still obtains

\[
\boxed{
\mathrm{ORIENTEDANGLE}_{106540}
\Longrightarrow
\liminf_{T\to\infty}
\frac{N_0(T,2T)}{N(T,2T)}
>0.9.
}
\tag{T-106540.3}
\]

Thus the conclusion survives the correction: the open phase estimate is a
stronger sufficient condition, not an exact reformulation.

## 3. Correct relation among the surviving coordinates

The following three quantities remain exactly equal:

```text
negative H^(1/2) Fourier energy of the endpoint all-pass symbol;
Hilbert--Schmidt square of its Hankel operator;
denominator model dimension minus canonical-correlation overlap.
```

The denominator phase average

```text
(1/4pi) integral beta_-' |1-U|^2
```

is an explicit positive upper bound for them.  It is generally not equal to
them.

## 4. Source information already available

`L-106500` proves

\[
\widehat{\mathcal L_5}
=
\frac1{16}
(5\xi^4\Lambda_2+10\xi^2\Lambda_4+\Lambda_6)
\ge0
\]

and supplies a positive all-order cross current.  `R-106508`,
`R-106513`, and `R-106640` show why those diagonal facts cannot be substituted
for either the exact canonical defect or the stronger phase-weighted mean.

## 5. Boundary

```text
fifth-endpoint telescope                         PROVED EXACT
positive fifth Wronskian/current hierarchy       PROVED EXACT
canonical-correlation adverse charge             PROVED EXACT
denominator phase-angle upper bound               PROVED EXACT
phase-angle equality with canonical charge        REFUTED
fixed allowance 97/1000                          PROVED EXACT
ORIENTEDANGLE106540                               OPEN / 90%-BEARING
ninety percent for zeta                          UNPROVED
Riemann Hypothesis                               UNPROVED
```
