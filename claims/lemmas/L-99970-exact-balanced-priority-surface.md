# L-99970 — The signed Euler scalar is the balanced priority surface

Claim ID: `L-99970`  
Status: **PROVED EXACT FINITE IDENTITY AND COAREA**  
Created: 2026-08-20  
Depends on: `L-99920/L-99922`; the native first-owner identity  
RH status: **not assumed**

Use the notation of `L-99920`.  Let `Phi(A)=F(P_A)>=0` be product-monotone,
let

\[
 \delta_{i,A}
 :=J_{i,A}[\Phi(A)-\Phi(A\cup\{i\})]\ge0,
\]

and split the complete priority surface by the parity of the suffix endpoint:

\[
 \mathcal U_\Phi
 =\sum_i\sum_{|A|\ {m odd}}\delta_{i,A},
 \qquad
 \mathcal V_\Phi
 =\sum_i\sum_{|A|\ {m even}}\delta_{i,A}.
\tag{L-99970.1}
\]

Here `U_Phi` is the positive upward flux retained in `T-99920`, while
`V_Phi` is the even surface discarded there.  Put

\[
 \mathscr A_\Phi
 =\sum_A(-1)^{|A|}w(A)\Phi(A),
 \qquad
 s_k=\prod_i(1-a_i).
\]

Then exactly

\[
\boxed{
 \mathscr A_\Phi
 =s_k\Phi(\varnothing)+\mathcal V_\Phi-\mathcal U_\Phi.
}
\tag{L-99970.2}
\]

Consequently

\[
\boxed{
 [-\mathscr A_\Phi]_+
 =[\mathcal U_\Phi-\mathcal V_\Phi-s_k\Phi(\varnothing)]_+.
}
\tag{L-99970.3}
\]

Thus the conclusion-facing quantity is a **balanced signed surface**, not the
positive majorant `U_Phi`.

## Proof

The native first-owner identity is

\[
 \prod_i(I-a_iU_i)
 =s_kI+\sum_i\lambda_i(I-U_i)
       \prod_{h>i}(I-a_hU_h).
\]

Apply it to `Phi` at the empty vertex and expand the future product.  The
`i`th current is

\[
 \sum_{A\subseteq\{i+1,\ldots,k\}}
 (-1)^{|A|}J_{i,A}
 [\Phi(A)-\Phi(A\cup\{i\})].
\]

Even suffixes contribute `+V_Phi`, odd suffixes contribute `-U_Phi`, proving
(L-99970.2).

## Signed Stieltjes coarea

Let `dnu=-dF`.  Define

\[
 \mathcal C_{\rm even}(t)
 =\sum_i\sum_{|A|\ {m even}}
 J_{i,A}\mathbf1_{P_A\le t<p_iP_A},
\]

\[
 \mathcal C_{\rm odd}(t)
 =\sum_i\sum_{|A|\ {m odd}}
 J_{i,A}\mathbf1_{P_A\le t<p_iP_A}.
\]

Finite Fubini gives

\[
 \mathcal V_\Phi-\mathcal U_\Phi
 =\int[\mathcal C_{\rm even}(t)-\mathcal C_{\rm odd}(t)]\,d\nu(t).
\tag{L-99970.4}
\]

Let the native weighted Euler prefix be

\[
 E(t)=\sum_{P_A\le t}(-1)^{|A|}w(A).
\tag{L-99970.5}
\]

Applying the same first-owner identity to the threshold potential
`1_(P_A<=t)` gives

\[
\boxed{
 E(t)=s_k+\mathcal C_{\rm even}(t)-\mathcal C_{\rm odd}(t).
}
\tag{L-99970.6}
\]

If `F(infinity)=0`, then `nu([1,infinity))=Phi(empty)`, and (L-99970.2)--
(L-99970.6) reduce to the exact ordinary coarea

\[
\boxed{
 \mathscr A_\Phi=\int E(t)\,d\nu(t).
}
\tag{L-99970.7}
\]

For the native duplicate-67 box,

\[
 E(t)=\sum_{n\le t}{\beta(n)\over n}.
\]

Equation (L-99970.7) is source-faithful and order-independent.  It also shows
why changing the priority order cannot remove the final cancellation: every
order reconstructs the same signed reciprocal prefix after the even surface
and survival terms are restored.
