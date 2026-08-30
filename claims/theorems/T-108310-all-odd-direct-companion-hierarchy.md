# T-108310 — All-odd direct companion hierarchy and the endpoint-31 ninety-percent frontier

Claim ID: `T-108310`  
Status: **EXACT HIERARCHY AND ENDPOINT-31 MOAT; PHYSICAL XI TRANSFER AND NINETY PERCENT OPEN**  
Created: 2026-08-31  
Base: PR #777 at `34eb08d532de909d6c284b1586778e88b10f871a`  
Sibling input: PR #772 at `93726d7f4a4c17ee530d064c19aa3a4519fd5465`  
RH status: **unproved**

For every fixed positive odd `K`, define

\[
E_{K,\sigma,\epsilon}
=
\Xi^{(K)}+i\sigma\epsilon\Xi,
\qquad \sigma\in\{+1,-1\}.
\]

`L-108310` proves that the limiting negative phase variations count the two
signs of

\[
{\Xi(c)\over\Xi^{(K+1)}(c)}
\]

at the simple real zeros of `Xi^(K)`. `L-108311` proves the direct endpoint
ledger

\[
\boxed{
N_0(T,2T)
\ge
M_K(T,2T)-1
-2\min_{\sigma=\pm1}U_{K,\sigma}(T)
-\mathcal E_{K,\rm reg}(T).
}
\tag{T-108310.1}
\]

No intermediate derivative rung appears.

## Endpoint 31

PR #772 proves

\[
{M_{31}(T,2T)\over N(T,2T)}
>{999\over1000}-o(1).
\]

Therefore the exact conclusion-facing condition is

\[
\boxed{
\limsup_{T\to\infty}
{\min_\sigma U_{31,\sigma}(T)
 +\tfrac12\mathcal E_{31,\rm reg}(T)
 \over N(T,2T)}
<{99\over2000}.
}
\tag{T-108310.2}
\]

The carrier-adapted source constant at this endpoint is `1/62`. Hence the
source-aligned sufficient interface is

\[
\boxed{
\mathrm{XI31MINPHASE}_{108310}(\delta):
\quad
\limsup
{\min_\sigma U_{31,\sigma}
 +\tfrac12\mathcal E_{31,\rm reg}
 \over N}
\le
{1\over62}+\delta,
\quad
\delta<{2069\over62000}.
}
\tag{T-108310.3}
\]

Then

\[
\boxed{
\mathrm{XI31MINPHASE}_{108310}
\Longrightarrow
\liminf_{T\to\infty}{N_0(T,2T)\over N(T,2T)}>0.9.
}
\tag{T-108310.4}
\]

The implication is exact. The premise is not proved.

## Density-one hierarchy

If there is an unbounded sequence of fixed odd endpoints with

\[
\alpha_K\to1
\]

and physical phase transfer

\[
{\min_\sigma U_{K,\sigma}\over N}
\le{1\over2K}+o_K(1),
\]

with the regularization ledger negligible, then

\[
\liminf{N_0\over N}
\ge
\alpha_K-{1\over K}-o_K(1),
\]

and letting `K` tend to infinity gives density one. This remains weaker than
RH.

## Binding boundary

`R-108310` proves that positive parent and Wronskian Fourier sources together
with complete real-rootedness of the odd derivative do not control the
minority phase. Thus `L-107401`'s source ratio cannot be inserted into
(T-108310.3) without a new physical Xi theorem.

```text
all-odd direct companion identity      PROVED EXACT
all-odd positive Fourier source         PROVED EXACT
all-odd minority transition ledger      PROVED EXACT
endpoint-31 source-aligned moat          PROVED EXACT
XI31MINPHASE108310                       OPEN
more than 90 percent                     UNPROVED
density one / RH                         UNPROVED
```
