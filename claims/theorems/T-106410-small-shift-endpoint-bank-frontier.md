# T-106410 — Small-shift endpoint-bank frontier for ninety percent

Claim ID: `T-106410`  
Status: **UNCONDITIONAL SOURCE CONTRACTION + CONDITIONAL ONE-ADAPTER THEOREM**  
Created: 2026-08-24  
Strengthened: 2026-08-24  
Depends on: `L-105260`, `L-106400--L-106412`; comparison with PR #726 `L-105542`  
RH status: **unproved**

## 1. Exact source-side payment

Choose a cofinal positive-frequency cutoff \(L_T\to\infty\) and the companion
shift

\[
\boxed{
\lambda_TL_T=\frac1{200}.
}
\tag{T-106410.1}

The companion winding and the endpoint zero-count index are independent of the
positive value of \(\lambda_T\).

`L-106410` and `L-106411` prove, before any asymptotic Xi estimate, that the
complete two-boundary endpoint-Turán source has normalized finite-section
Hilbert--Schmidt cost at most

\[
\boxed{
\mathfrak r_*
=\frac{2547232}{1568239201}
=0.0016242624\ldots
<\frac1{600}.
}
\tag{T-106410.2}

relative to the corresponding positive endpoint-denominator bank.  The four
channels paid in (T-106410.2) are:

```text
two conjugate same-sign Hankel channels;
two oriented reflected Toeplitz channels.
```

No large-sieve, zero-density, or RH input is used in this source inequality.

## 2. The sole bank adapter

Define `ENDPOINTBANK106410` to be the following cofinal statement.

```text
1. The actual Xi endpoint companion block of L-106400 is represented by the
   two-boundary Paley--Wiener bank of L-105260 with lambda_T L_T=1/200,
   source-for-source and before physical quotienting.

2. Its positive endpoint-denominator Gram G_T has a source reference G0_T of
   dimension d_T >= (999/1000-o(1)) N(T) and satisfies

     tr[(I-G0_T^(-1/2) G_T G0_T^(-1/2))_+] = o(d_T).

3. The Fourier tail beyond L_T, finite-window endpoints, common-zero,
   multiplicity and confluent ledgers contribute o(d_T) to the bank codimension
   and to the normalized endpoint-Turan trace.
```

The negative-trace form in item 2 is deliberately chosen to match the existing
horizontal-bank output on PR #726.  `L-106412` shows that it loses only \(o(d_T)\)
dimensions and gives inverse-frame cost at most two after discarding the
subspace below \(1/2\).

Under `ENDPOINTBANK106410`, the exact endpoint block therefore satisfies

\[
\boxed{
4\lambda_T^2\operatorname{tr}(G_T^{-1}Q_T)
\le(2\mathfrak r_*+o(1))d_T.
}
\tag{T-106410.3}

## 3. Quantitative conclusion

Combining `L-106400` with

\[
\frac{R_2(T)}{N(T)}>\frac{599}{625}-o(1)
\]

and \(d_T/N(T)\ge999/1000-o(1)\) gives the sharper conditional bound

\[
\boxed{
\frac{R_0(T)}{N(T)}
\ge
\frac{599}{625}
-\frac1{1000}
-2\mathfrak r_*\frac{999}{1000}
-o(1)
=0.9541547236\ldots-o(1).
}
\tag{T-106410.4}

In particular, using only \(\mathfrak r_*<1/600\),

\[
\boxed{
\mathrm{ENDPOINTBANK}_{106410}
\Longrightarrow
\liminf_{T\to\infty}
\frac{N_0(T,2T)}{N(T,2T)}
>\frac{95407}{100000}
=0.95407.
}
\tag{T-106410.5}

Thus the exact source contraction has far more numerical room than required
for ninety percent.  The remaining issue is not the Turán numerator, its sign,
or its channel energy.  It is the cofinal source-to-endpoint-bank
identification in `ENDPOINTBANK106410`.

## 4. Relation to the earlier two-scalar gate

`ROBUSTFRAME106400` remains a valid standalone sufficient condition.  The new
route is stronger when the endpoint bank adapter is available:

```text
ROBUSTFRAME106400:
  1% Frobenius denominator comparison + 0.5% raw leakage;

ENDPOINTBANK106410:
  o(1) one-sided denominator deficit + exact four-channel source contraction.
```

The second formulation replaces two numerical hypotheses by one typed
compositional interface.  It does not silently identify the endpoint bank with
PR #726's horizontal bank; that source-level equality is the explicit open
statement.

## 5. Boundary

```text
same-sign Xi half-source contraction          PROVED EXACT
reflected Xi channel contraction              PROVED EXACT
complete four-channel cost < 1/600            PROVED EXACT
negative-trace quantile absorption            PROVED EXACT
ENDPOINTBANK106410                            OPEN / RECORD-BEARING
conditional line fraction > 95.407%           PROVED IMPLICATION
ninety percent for zeta                       UNPROVED
density one                                   UNPROVED
Riemann Hypothesis                            UNPROVED
```
