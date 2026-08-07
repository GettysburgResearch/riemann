# L-15159 — Exact Möbius core of the finite Heath–Brown packet

Claim ID: `L-15159`  
Title: The signed truncated Heath–Brown packet reconstructs the Möbius function before the logarithmic factor, and every fixed-log slice contains an exact Möbius source  
Status: **PROPOSED EXACT LEMMA PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-04-f`  
Created: 2026-08-07  
Dependencies: elementary Dirichlet convolution; the packet notation of `L-15156`  
Scope: exact finite decoder and proof-boundary theorem; no asymptotic Möbius estimate

## 1. Packet inverse

Fix integers

\[
 K\ge 1,
 \qquad V\ge 1,
 \qquad X=V^K.
\]

Let

\[
 \mu_V(n)=\mu(n)\mathbf 1_{n\le V},
\]

let `1` denote the constant-one arithmetic function, and let `delta` be the
Dirichlet-convolution identity. Define

\[
 \boxed{
 A_{K,V}
 =\sum_{j=1}^{K}(-1)^{j-1}{K\choose j}
   \mu_V^{*j}*1^{*(j-1)}.}
 \tag{L-15159.1}
\]

This is the coefficient packet occurring in the Heath–Brown identity before
the final `log` convolution.

## 2. Exact Möbius reconstruction

Put

\[
 B=\mu_V*1,
 \qquad
 R=\delta-B.
 \tag{L-15159.2}
\]

For every integer `n<=V`, all divisors of `n` occur in `mu_V`, so

\[
 B(n)=(\mu*1)(n)=\delta(n).
\]

Consequently

\[
 R(n)=0\qquad(n\le V).
 \tag{L-15159.3}
\]

Convolving (L-15159.1) with `1` and using the binomial theorem in the
Dirichlet-convolution algebra gives

\[
\begin{aligned}
 A_{K,V}*1
 &=\sum_{j=1}^{K}(-1)^{j-1}{K\choose j}B^{*j}\\
 &=\delta-(\delta-B)^{*K}\\
 &=\delta-R^{*K}.
\end{aligned}
 \tag{L-15159.4}
\]

Every nonzero factor in `R` is supported above `V`. Therefore every nonzero
coefficient of `R^{*K}` is supported above `V^K=X`, and

\[
 (A_{K,V}*1)(n)=\delta(n)
 \qquad(n\le X).
 \tag{L-15159.5}
\]

Convolve this finite coefficient identity with `mu`. For `n<=X`, the
coefficient at `n` only uses divisors of `n`, so no coefficient above `X` is
needed. Since `1*mu=delta`,

\[
 \boxed{
 A_{K,V}(n)=\mu(n)
 \qquad(n\le V^K).}
 \tag{L-15159.6}
\]

Thus increasing the Heath–Brown order does not replace the Möbius source by an
arithmetically easier coefficient. The signed binomial packet reconstructs it
exactly throughout the declared coefficient range.

## 3. Recovery of the von Mangoldt identity

The classical convolution identity is

\[
 \Lambda=\mu*\log.
 \tag{L-15159.7}
\]

Equation (L-15159.6) therefore gives

\[
 \boxed{
 (A_{K,V}*\log)(n)=\Lambda(n)
 \qquad(n\le V^K).}
 \tag{L-15159.8}
\]

Expanding `A_(K,V)` in (L-15159.8) is precisely the finite Heath–Brown formula
of `L-15156`.

The identity has two equally important readings:

```text
recombine the log variable:
    the packet is exactly Lambda;

freeze the log variable:
    the remaining signed packet is exactly mu.
```

## 4. Fixed-logarithm slices

In the tuple notation of `L-15156`, let the final logarithmic variable be fixed
at one integer `q0>=2`. Write the product of all remaining tuple variables as
`m`. The sum of all signed tuple coefficients with that fixed `q0` is

\[
 \log q_0\,A_{K,V}(m).
 \tag{L-15159.9}
\]

Hence, whenever `q0*m<=V^K`,

\[
 \boxed{
 \text{fixed-}q_0\text{ packet coefficient}
 =\mu(m)\log q_0.}
 \tag{L-15159.10}
\]

For a compact logarithmic window `H`, the normalized finite signal of this
slice is therefore

\[
\begin{aligned}
 Q_{K,V;q_0,H}(x)
 &=\sum_{m\le V^K/q_0}
   {\mu(m)\log q_0\over\sqrt{q_0m}}
   H(x-\log(q_0m))\\
 &=\boxed{
 {\log q_0\over\sqrt{q_0}}
 Q_{\mu,H}^{(V^K/q_0)}(x-\log q_0),}
\end{aligned}
 \tag{L-15159.11}
\]

where

\[
 Q_{\mu,H}^{(Y)}(x)
 =\sum_{m\le Y}{\mu(m)\over\sqrt m}H(x-\log m).
 \tag{L-15159.12}
\]

On every output block whose compact support lies inside `q0*m<=V^K`, this is an
exact identity with no omitted endpoint term.

The smallest slice `q0=2` already contains the full Möbius cancellation
problem.

## 5. Consequence for destination packets

Suppose a deterministic first-crossing rule divides the fixed-`q0` packet into
`R_K` signed destination packets. Let their block vectors in the Gram Hilbert
space be

\[
 h_{K,1},\ldots,h_{K,R_K},
 \qquad
 \sum_{\tau=1}^{R_K}h_{K,\tau}=h_{\mu,q_0}.
 \tag{L-15159.13}
\]

Subtracting certified null companions does not change any Gram vector. If

\[
 E_{K,\tau}=\|h_{K,\tau}\|^2,
 \qquad
 E_{\mu,q_0}=\|h_{\mu,q_0}\|^2,
\]

then

\[
 E_{\mu,q_0}^{1/2}
 \le\sum_{\tau=1}^{R_K}E_{K,\tau}^{1/2}
 \le\sqrt{R_K\sum_{\tau=1}^{R_K}E_{K,\tau}}.
 \tag{L-15159.14}
\]

In particular,

\[
 \boxed{
 \max_\tau E_{K,\tau}
 \ge {E_{\mu,q_0}\over R_K^2}.}
 \tag{L-15159.15}
\]

For fixed `K`, `R_K` is independent of the block scale. Therefore partitioning
the packet cannot reduce the upper exponential growth exponent of every
component below that of the Möbius slice.

## 6. Interpretation for `CP(K)`

The exact packet architecture in `L-15156` is useful bookkeeping, but the
analytic theorem `CP(K)` cannot follow from that bookkeeping alone:

1. after full recombination, the source is exactly `Lambda`;
2. after fixing one logarithmic variable, the source is exactly `mu`;
3. after any finite destination partition, at least one packet retains the
   Möbius block exponent by (L-15159.15).

Thus an estimate proving all packet energies subexponential necessarily proves
a genuine Möbius-cancellation theorem. It is not a routine consequence of the
number of variables, the binomial identity, or the fixed scale reserve.

This statement does not prove that `CP(K)` is false. It identifies its exact
arithmetic content.

## 7. Proof boundary

Closed exactly:

- `A_(K,V)=mu` through `V^K`;
- `A_(K,V)*log=Lambda` through `V^K`;
- every fixed-logarithm Möbius slice;
- the finite-packet energy lower bound (L-15159.15).

Open:

- a subexponential estimate for the Möbius safe signal;
- `CP(K)`;
- RH.
