# L-28001 — Size-biased fragmentation spine and first-entrance localization

Claim ID: `L-28001`  
Title: Every conservative balanced producer is one descending Markov potential, and all higher generations recombine into a factor-two first-entrance source before the final sign  
Status: **PROPOSED COMPLETE EXACT LEMMA**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-08  
Dependencies: PR #247/#277 `L-23810`, `L-23811`  
Scope: exact finite algebra for the binary–ternary producer; no sign theorem or RH conclusion

## 1. Descending producer

Let `R(1),...,R(X)` be any node source with the size-conservation normalization inherited from the carry divergence. For the frozen half-binary/half-ternary grammar, write

\[
\begin{aligned}
a_2(m)&=\lfloor m/2\rfloor, & b_2(m)&=m-a_2(m),\\
a_3(m)&=\lceil m/3\rceil, & b_3(m)&=m-a_3(m).
\end{aligned}
\]

The exact producer is

\[
A(n)=R(n)+\frac12\sum_{m>n}A(m)
\sum_{c\in\{a_2(m),b_2(m),a_3(m),b_3(m)\}}
\mathbf1_{c=n},
\tag{L-28001.1}
\]

with repeated central children counted with their full multiplicity.

Put

\[
B(n)=nA(n),\qquad S(n)=nR(n).
\tag{L-28001.2}
\]

## 2. Exact stochastic kernel

For `m>n`, define

\[
\boxed{
Q(m,n)=\frac{n}{2m}
\sum_{c\in\{a_2(m),b_2(m),a_3(m),b_3(m)\}}
\mathbf1_{c=n}.}
\tag{L-28001.3}
\]

Because every declared split conserves integer size,

\[
\sum_{n<m}Q(m,n)
=\frac{a_2+b_2+a_3+b_3}{2m}=1.
\tag{L-28001.4}
\]

Thus `Q` is the transition kernel of a strictly descending Markov chain `Z_t`:

```text
choose the binary or ternary split with probability 1/2;
then choose one of its two children with probability proportional to its size.
```

Multiplying (L-28001.1) by `n` gives the conservative Poisson equation

\[
\boxed{
B(n)=S(n)+\sum_{m>n}B(m)Q(m,n).}
\tag{L-28001.5}
\]

The original fragmentation coefficient has disappeared only because its exact sibling coupling has already been incorporated into `Q`.

## 3. Green/hitting representation

For `m>=n`, let

\[
h_n(m)=\mathbb P_m(\exists t: Z_t=n).
\tag{L-28001.6}
\]

The chain is strictly descending, so a state can be visited at most once. Hence its Green kernel is precisely the hitting probability. Back substitution in the triangular equation gives

\[
\boxed{
nA(n)=B(n)=\sum_{m=n}^{X}mR(m)h_n(m).}
\tag{L-28001.7}
\]

This is an exact finite identity for every target and endpoint. It exposes the producer sign as one complete source pairing, not as positivity of a generic matrix entry.

## 4. Exact cut/flux identity

For a threshold `k`, summing (L-28001.5) over `n>=k` gives

\[
\boxed{
\sum_{n=k}^{X}S(n)
=\sum_{m=k}^{X}B(m)\,
\mathbb P_m(Z_1<k).}
\tag{L-28001.8}
\]

For `m=k`, the probability is one because every child is smaller than its parent. Equation (L-28001.8) is the exact size-mass flux crossing the cut `{k,k+1,...}`.

Consequently producer positivity forces every size-weighted source tail to be nonnegative. The converse is not asserted: mixed-size fragmentation has genuine transition constraints beyond scalar cut capacity.

## 5. First-entrance recombination

Fix a target node `n` and let

\[
\tau_n=\inf\{t:Z_t<2n\}.
\tag{L-28001.9}
\]

For `n<=p<2n` define the first-entrance kernel

\[
E_n(m,p)=\mathbb P_m(Z_{\tau_n}=p),
\tag{L-28001.10}
\]

with `E_n(m,p)=delta_(m,p)` when `n<=m<2n`. Paths that jump below `n` contribute zero because they can never return to `n`.

Define the completely recombined transition source

\[
\boxed{
\Sigma_{X,n}(p)
=\sum_{m=n}^{X}mR_X(m)E_n(m,p),
\qquad n\le p<\min(2n,X+1).}
\tag{L-28001.11}
\]

Strong Markov at `tau_n` gives

\[
\boxed{
nA_X(n)
=\sum_{p=n}^{\min(2n-1,X)}
\Sigma_{X,n}(p)h_n(p).}
\tag{L-28001.12}
\]

Every source generation at scale `m>=2n` has therefore been recombined **before** a sign is taken. The unresolved sign is confined to one multiplicative transition annulus `[n,2n)`.

## 6. First-Entrance Positivity criterion

The source-specific theorem

\[
\boxed{
\operatorname{FEP}(X):
\quad \Sigma_{X,n}(p)\ge0
\quad\text{for every }2\le n\le p<\min(2n,X+1)
}
\tag{L-28001.13}
\]

implies

\[
A_X(n)\ge0\qquad(2\le n\le X)
\tag{L-28001.14}
\]

because every hitting probability in (L-28001.12) is nonnegative.

FEP is stronger than producer positivity but substantially more localized. It is not an entrywise positivity theorem for the raw producer, and it is not obtained by taking absolute values of the Möbius source.

## 7. Relation to failed Abel smoothing

Fixed Abel integration acts on the target columns before the full ancestry is assembled. The exact counterexamples in `R-27802/R-28001` show that negative higher generations survive every tested finite order.

Equation (L-28001.11) performs the opposite operation: it propagates and recombines **all** higher generations through the conservative ancestry and only then asks for a sign in the first-entrance band. This is the structural reason the spine route is not another cumulative-kernel surrogate.

## 8. Proof boundary

Closed exactly:

- stochastic size-biased transition kernel;
- conservative Poisson equation;
- Green/hitting formula;
- cut/flux identity;
- first-entrance factor-two localization;
- `FEP -> producer positivity`.

Open:

- FEP for the critical Möbius source;
- producer positivity;
- RH.
