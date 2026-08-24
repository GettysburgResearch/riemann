# L-106431 — The all-pass index has an exact signed source/complement split

Claim ID: `L-106431`  
Status: **PROVED EXACT FOR TRACE-CLASS ALL-PASS SYMBOLS**  
Created: 2026-08-25  
Depends on: `L-105290`, `L-106400`  
RH status: **not assumed**

Let \(U\) be a scalar rational all-pass symbol, or more generally a unimodular
\(H^{1/2}\) symbol for which the two Hankel operators below are
Hilbert--Schmidt.  Put

\[
A_-=H_U^*H_U,
\qquad
A_+=H_{\overline U}^*H_{\overline U}.
\]

The Fourier degree identity of `L-105290` is

\[
\boxed{
-\operatorname{wind}U
 =\operatorname{tr}A_- -\operatorname{tr}A_+.
}
\tag{L-106431.1}
\]

## 1. Exact split across an arbitrary source projection

Let \(P\) be any orthogonal projection and \(P^\perp=I-P\).  Since the
off-diagonal blocks have zero trace,

\[
\operatorname{tr}A_\pm
 =\operatorname{tr}(PA_\pm P)
  +\operatorname{tr}(P^\perp A_\pm P^\perp).
\]

Define the visible signed charge

\[
\mathcal V_P(U)
 =\operatorname{tr}(PA_-P)-\operatorname{tr}(PA_+P),
\tag{L-106431.2}
\]

and the signed complement charge

\[
\boxed{
\mathcal D_P(U)
 =\operatorname{tr}(P^\perp A_-P^\perp)
  -\operatorname{tr}(P^\perp A_+P^\perp).
}
\tag{L-106431.3}
\]

Then

\[
\boxed{
-\operatorname{wind}U
 =\mathcal V_P(U)+\mathcal D_P(U).
}
\tag{L-106431.4}
\]

The visible charge obeys the one-sided estimate

\[
\mathcal V_P(U)
\le \operatorname{tr}(PA_-P)
 =\|H_UP\|_{\mathcal S_2}^2.
\]

Consequently

\[
\boxed{
-\operatorname{wind}U
\le
\|H_UP\|_{\mathcal S_2}^2
 +\bigl(\mathcal D_P(U)\bigr)_+.
}
\tag{L-106431.5}
\]

This inequality retains every pole--zero cancellation in the unobserved
complement.  It is strictly weaker than separately requiring

\[
\operatorname{tr}(P^\perp A_-P^\perp)=o(N)
\quad\hbox{and}\quad
\operatorname{tr}(P^\perp A_+P^\perp)=o(N).
\]

## 2. Endpoint-companion consequence

For the endpoint Xi symbol of `L-106400`,

\[
\operatorname{wind}U_T=R_0(T,2T)-R_2(T,2T)
\]

up to the declared finite-window endpoint and confluent ledger.  Therefore
(L-106431.5) gives

\[
\boxed{
R_0(T,2T)
\ge
R_2(T,2T)
-\|H_{U_T}P_T\|_{\mathcal S_2}^2
-\bigl(\mathcal D_{P_T}(U_T)\bigr)_+
-o(N(T,2T)).
}
\tag{L-106431.6}

Here \(P_T\) may be the predeclared four-channel Paley--Wiener source projection
of `L-106413`.  The first term on the right is already bounded by the explicit
source constant.  The second is a signed relative-index tail.

## 3. Model-space interpretation

For a reduced factorization

\[
U=\omega B_+/B_-,
\]

the negative and positive Hankel energies have the same model-space
principal-angle overlap:

\[
\|H_U\|_{\mathcal S_2}^2
 =\deg B_- -\operatorname{tr}(P_{K_{B_-}}P_{K_{B_+}}),
\]

\[
\|H_{\overline U}\|_{\mathcal S_2}^2
 =\deg B_+ -\operatorname{tr}(P_{K_{B_-}}P_{K_{B_+}}).
\]

The overlap cancels in their difference.  Equation (L-106431.4) is the
source-compressed version of the same cancellation.  An absolute sampling
condition on \(K_{B_-}\) alone discards this structure; the signed tail does
not.

## 4. Scope

The lemma proves the correct topological decomposition.  It does not estimate
\(\mathcal D_{P_T}(U_T)\) for Xi.  Its purpose is to replace the stronger
absolute-coverage gate by the exact conclusion-facing signed quantity.
