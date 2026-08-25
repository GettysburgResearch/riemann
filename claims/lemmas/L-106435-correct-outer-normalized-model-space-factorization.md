# L-106435 — Correct outer-normalized model-space factorization of the endpoint Hankel operator

Claim ID: `L-106435`  
Status: **PROVED EXACT FOR FINITE BOUNDED-TYPE ENDPOINT SYMBOLS**  
Created: 2026-08-25  
Depends on: `R-106420`; `L-106415`; `L-106434`  
RH status: **not assumed**

The false denominator-multiplied transfer uses the complete analytic
denominator and therefore lands in the Hankel kernel.  The correct
factorization removes only the zero-free outer denominator and retains the bad
inner factor as the model-space projection.

## 1. Canonical factorization

Let

\[
U=N/D
\]

be a reduced rational all-pass symbol in the upper half-plane, normalized to
have a finite boundary value at infinity.  Factor the analytic denominator in
`C_+` as

\[
\boxed{D=B_-O_-,}
\tag{L-106435.1}
\]

where `B_-` is the finite Blaschke product of the upper-half-plane zeros of
`D` and `O_-` is analytic and zero-free in `C_+`.  Put

\[
\boxed{g_-={N-D\over O_-}.}
\tag{L-106435.2}
\]

Then `g_-` is analytic in `C_+`.  Since `1/B_-=bar B_-` almost everywhere on
the boundary,

\[
\boxed{U-1=\overline{B_-}\,g_-.}
\tag{L-106435.3}
\]

For every `f in H^2`, `g_-f` is analytic on the finite rational scope, and
therefore

\[
\boxed{
H_Uf
 =H_{\overline{B_-}}(g_-f).
}
\tag{L-106435.4}
\]

The Hankel operator of an inner conjugate is a partial isometry with

\[
H_{\overline{B_-}}^*H_{\overline{B_-}}
 =P_{K_{B_-}}.
\]

Consequently

\[
\boxed{
H_U=H_{\overline{B_-}}T_{g_-},
\qquad
H_U^*H_U=T_{g_-}^*P_{K_{B_-}}T_{g_-}.
}
\tag{L-106435.5}
\]

For every finite source projection `P`,

\[
\boxed{
\|H_UP\|_{\mathcal S_2}^2
 =\|P_{K_{B_-}}T_{g_-}P\|_{\mathcal S_2}^2.
}
\tag{L-106435.6}
\]

This is the correct source-to-topology interface.

## 2. Favorable orientation

Factor the analytic numerator as

\[
N=B_+O_+
\]

and put

\[
g_+={D-N\over O_+}.
\]

The reflected Hankel energy obeys

\[
\boxed{
H_{\overline U}^*H_{\overline U}
 =T_{g_+}^*P_{K_{B_+}}T_{g_+}.
}
\tag{L-106435.7}
\]

Because `|N|=|D|` on the boundary and inner factors have unit modulus,

\[
\boxed{|g_-|=|g_+|=|U-1|\quad\hbox{a.e.}}
\tag{L-106435.8}
\]

Thus the signed index compares two model-space compressions carrying equal
boundary multiplier magnitude; the pole/zero geometry and analytic phases,
not an arbitrary numerator norm, determine the sign.

## 3. Endpoint Turán specialization

For the endpoint quotient,

\[
N-D=2i\lambda\mathcal T_F,
\]

so

\[
\boxed{
g_-={2i\lambda\mathcal T_F\over O_-}.}
\tag{L-106435.9}
\]

At a simple bad companion zero `b`,

\[
D'(b)=B_-'(b)O_-(b),
\]

and the samples in `L-106434` become

\[
{2i\lambda\mathcal T_F(b)\over D'(b)}
 ={g_-(b)\over B_-'(b)}.
\]

Hence the residue/exponential Gram and the model-space factorization are the
same exact object in Lagrange and operator coordinates.

## 4. Safe bounds and the remaining theorem

On the boundary,

\[
|g_-|
 ={ |N-D|\over|D|}
 =|U-1|
 \le2.
\]

Therefore `g_-` is a bounded analytic multiplier with norm at most two on the
finite outer-normalized scope, and

\[
\|H_UP\|_{\mathcal S_2}^2
\le4\operatorname{rank}P.
\]

This universal estimate is far too weak for ninety percent, but it is honest.
To recover a small constant one must prove that the actual Xi multiplier
`2i lambda T_Xi/O_-` is small on the declared source after projection to the
bad companion model space, or exploit cancellation against the favorable
`g_+` compression.

The analytic four-channel numerator ratio does not by itself estimate
`T_(g_-)^*P_(K_B-)T_(g_-)`; the missing outer normalization and model-space
projection are now explicit.
