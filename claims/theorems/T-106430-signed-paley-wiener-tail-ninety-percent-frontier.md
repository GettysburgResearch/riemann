# T-106430 — Signed Paley–Wiener complement frontier for ninety percent

Claim ID: `T-106430`  
Status: **UNCONDITIONAL REDUCTION TO A FIXED SIGNED TRACE; SIGNEDTAIL106430 OPEN**  
Created: 2026-08-25  
Depends on: `L-106400--L-106431`; pinned fixed-order input `R_2/N>599/625-o(1)`  
RH status: **unproved**

The absolute coverage theorem `PWSAMP106420` remains a valid sufficient route,
but `L-106430/R-106430` show that it is stronger than the all-pass index
requires.  This theorem records the exact weaker route.

## 1. Source projection and signed complement

Let \(U_T\) be the reduced endpoint all-pass symbol and let \(P_T\) be the
predeclared four-channel Paley--Wiener source projection of `L-106413`.  Put

\[
A_{-,T}=H_{U_T}^*H_{U_T},
\qquad
A_{+,T}=H_{\overline{U_T}}^*H_{\overline{U_T}}.
\]

Define the signed unobserved charge

\[
\boxed{
\Delta_T
 =\operatorname{tr}\bigl(P_T^\perp A_{-,T}P_T^\perp\bigr)
 -\operatorname{tr}\bigl(P_T^\perp A_{+,T}P_T^\perp\bigr).
}
\tag{T-106430.1}

Both traces are explicit confluent model-space sampling traces.  Their
difference, not either absolute trace separately, is the unobserved all-pass
index.

By `L-106431`,

\[
-\operatorname{wind}U_T
\le
\|H_{U_T}P_T\|_{\mathcal S_2}^2+(\Delta_T)_+.
\tag{T-106430.2}

The four-channel endpoint source theorem gives

\[
\boxed{
\|H_{U_T}P_T\|_{\mathcal S_2}^2
 <\left(\frac1{600}+o(1)\right)N(T,2T).
}
\tag{T-106430.3}

No coverage or inverse-frame estimate is used in (T-106430.2)--(T-106430.3).

## 2. Exact ninety-percent constant

The pinned unconditional fixed-order theorem gives

\[
\frac{R_2(T,2T)}{N(T,2T)}
 >\frac{599}{625}-o(1).
\]

The available margin above ninety percent is

\[
\frac{599}{625}-\frac9{10}=\frac{73}{1250}.
\]

After paying the conservative source cost \(1/600\), the signed complement
allowance is

\[
\boxed{
\frac{73}{1250}-\frac1{600}
 =\frac{851}{15000}
 =0.056733333\ldots .
}
\tag{T-106430.4}

Define

```text
SIGNEDTAIL106430:

limsup_(T->infinity)
  (Delta_T)_+ / N(T,2T)
< 851/15000.
```

Then the endpoint winding identity gives

\[
\boxed{
\mathrm{SIGNEDTAIL}_{106430}
\Longrightarrow
\liminf_{T\to\infty}
\frac{N_0(T,2T)}{N(T,2T)}>0.9.
}
\tag{T-106430.5}

For a ninety-five-percent conclusion, the corresponding signed-tail threshold
is

\[
\boxed{
\frac{599}{625}-\frac{19}{20}-\frac1{600}
 =\frac{101}{15000}.
}
\tag{T-106430.6}

## 3. Relation to the former matrix gate

Since

\[
(\Delta_T)_+
\le
\operatorname{tr}(P_T^\perp A_{-,T}P_T^\perp),
\]

any absolute-coverage theorem strong enough to prove `PWSAMP106420` also proves
`SIGNEDTAIL106430`.  The converse is false in general: equal pole and zero
model-space tails can both be large while their signed difference is zero.

Thus the new theorem changes the last arithmetic/analytic target from

```text
absolute missed model-space mass = o(N)
```

to

```text
positive part of the signed missed index < 5.6734% of N.
```

This is a fixed constant theorem, not an RH-strength subpower estimate.

## 4. Explicit matrix form

Let \(C_{-,T}\) and \(C_{+,T}\) be the confluent source-compression matrices on
the pole and zero model spaces, and let \(K_{-,T},K_{+,T}\) be the corresponding
Hankel-energy matrices.  Then

\[
\Delta_T
 =\operatorname{tr}\bigl(K_{-,T}(I-C_{-,T})\bigr)
 -\operatorname{tr}\bigl(K_{+,T}(I-C_{+,T})\bigr),
\tag{T-106430.7}

with the usual basis-independent interpretation when the sampling matrices do
not commute with the energy matrices.  Every entry is a normalized
Paley--Wiener Cauchy/exponential kernel value or confluent jet at an endpoint
companion zero.

## 5. Boundary

```text
confluent Paley--Wiener deficit formula       PROVED EXACT
small-shift absolute-coverage shortcut        REFUTED GENERICALLY
signed source/complement index split          PROVED EXACT
four-channel visible source cost < 1/600      INHERITED PROVED
SIGNEDTAIL106430 fixed 5.6733% estimate        OPEN / RECORD-BEARING
ninety percent for zeta                       UNPROVED
density one                                   UNPROVED
Riemann Hypothesis                            UNPROVED
```
