# L-32301 — The balanced binary–ternary first-entrance consumer has at most three sites

Claim ID: `L-32301`  
Title: Inside the factor-two transition annulus, the frozen size-biased binary–ternary chain can hit the lower node only directly, so the Green consumer is supported on at most three explicit sites  
Status: **PROPOSED COMPLETE EXACT FINITE LEMMA**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-08  
Dependencies: PR #292 `L-28001-size-biased-fragmentation-spine-and-first-entrance.md`  
Scope: exact Markov/fragmentation geometry; no source sign or RH conclusion

## 1. Frozen chain

For a parent `m>=2`, retain the frozen two splits

\[
 a_2(m)=\lfloor m/2\rfloor,
 \qquad b_2(m)=\lceil m/2\rceil,
\]

and

\[
 a_3(m)=\lceil m/3\rceil,
 \qquad b_3(m)=\lfloor2m/3\rfloor.
\]

The size-biased transition kernel of PR #292 is

\[
 Q(m,r)=\frac{r}{2m}
 \#\{c\in\{a_2(m),b_2(m),a_3(m),b_3(m)\}:c=r\}.
\tag{L-32301.1}
\]

For a fixed target node `n`, write

\[
 h_n(p)=\mathbb P_p(\exists t:Z_t=n).
\]

PR #292 proves the first-entrance representation

\[
 nA_X(n)=
 \sum_{p=n}^{\min(2n-1,X)}
 \Sigma_{X,n}(p)h_n(p).
\tag{L-32301.2}
\]

The purpose of this lemma is to compute every `h_n(p)` appearing in (L-32301.2).

## 2. No indirect return inside the transition annulus

Fix

\[
 n<p<2n.
\]

Every binary child of `p` is at most

\[
 \left\lceil\frac p2\right\rceil\le n.
\]

The only possible binary child equal to `n` occurs at

\[
 p=2n-1,
\tag{L-32301.3}
\]

where the large binary child is exactly `n`.

The small ternary child satisfies

\[
 a_3(p)=\lceil p/3\rceil<n.
\]

The large ternary child satisfies

\[
 b_3(p)=\lfloor2p/3\rfloor<\frac{4n}{3}.
\tag{L-32301.4}
\]

If `b_3(p)>n`, then from any state

\[
 n<r<\frac{4n}{3}
\]

every binary child is at most `2n/3<n`, and every ternary child is at most

\[
 \frac{2r}{3}<\frac{8n}{9}<n.
\]

Thus a child strictly between `n` and `4n/3` can never hit `n` at a later generation. Consequently, for every `n<p<2n`, a path from `p` hits `n` if and only if one of the four **immediate** children is equal to `n`.

Therefore

\[
\boxed{
 h_n(p)=Q(p,n)
 \qquad(n<p<2n).
}
\tag{L-32301.5}
\]

This removes every deeper Green path from the first-entrance consumer.

## 3. Explicit support

The ternary large child equals `n` precisely when

\[
 \left\lfloor\frac{2p}{3}\right\rfloor=n.
\]

Equivalently,

\[
 \frac{3n}{2}\le p<\frac{3(n+1)}{2}.
\tag{L-32301.6}
\]

Hence the ternary support is

\[
 \mathcal T_n
 =\left\{
 p\in\mathbb Z:
 \left\lceil\frac{3n}{2}\right\rceil
 \le p
 \le
 \left\lceil\frac{3(n+1)}{2}\right\rceil-1
 \right\}.
\tag{L-32301.7}
\]

It contains two integers when `n` is even and one integer when `n` is odd, before intersecting with `p<2n` at the smallest cases.

The binary support consists only of

\[
 \mathcal B_n=\{2n-1\}.
\tag{L-32301.8}
\]

Thus

\[
\boxed{
 \operatorname{supp}(h_n|_{[n,2n)})
 \subseteq
 \{n\}\cup\mathcal T_n\cup\{2n-1\},
}
\tag{L-32301.9}
\]

and after coincidences there are at most four sites including `n`, hence at most three nontrivial first-entrance sites.

For `p>n`, let

\[
 m_n(p)
 =\#\{c\in\{a_2(p),b_2(p),a_3(p),b_3(p)\}:c=n\}.
\]

Then the exact weight is

\[
\boxed{
 h_n(p)=\frac{n}{2p}m_n(p).
}
\tag{L-32301.10}
\]

The small coincidences `n=2,3,4` are automatically handled by the multiplicity `m_n(p)`; no exceptional formula is needed.

## 4. Sparse first-entrance identity

Substituting (L-32301.9)--(L-32301.10) into the exact PR #292 representation gives

\[
\boxed{
\begin{aligned}
 nA_X(n)
={}&\Sigma_{X,n}(n)\\
&+\sum_{p\in\mathcal T_n\cap(n,2n)}
 \frac{n\,m_n(p)}{2p}\Sigma_{X,n}(p)\\
&+\frac{n\,m_n(2n-1)}{2(2n-1)}
 \Sigma_{X,n}(2n-1),
\end{aligned}}
\tag{L-32301.11}
\]

with coincident sites combined only once with their full multiplicity.

Thus coordinatewise positivity of the entire transition band, the former `FEP` target, is much stronger than required. Producer positivity is equivalent to the sign of one explicit three-site-or-less functional of the completely recombined first-entrance source.

## 5. Top-site recursion

There is one additional exact simplification. Since `2n-1` is the largest state in `[n,2n)`, a path which hits `2n-1` cannot have entered the band earlier. Therefore

\[
 E_n(m,2n-1)=h_{2n-1}(m),
\]

and PR #292's Green identity gives

\[
\boxed{
 \Sigma_{X,n}(2n-1)=(2n-1)A_X(2n-1).
}
\tag{L-32301.12}
\]

The highest first-entrance coordinate is therefore already the next descending producer coefficient. Only the one/two ternary contact sites and the bottom coordinate remain genuinely new.

## 6. Consequence for research architecture

The exact transition-band problem is not a positivity theorem on `n` coordinates and is not naturally a large finite LP. Its consumer has the form

```text
bottom entrance coordinate
+ one/two ternary contacts near 3n/2
+ the already-constructed top coefficient at 2n-1.
```

A future source-renormalization proof should preserve precisely this functional before any positive/negative split. A five-adic or parity automaton which controls every transition coordinate independently is solving a strictly stronger problem than the producer actually consumes.

## 7. Proof boundary

Proved exactly:

1. no indirect return to `n` after a nontrivial first entrance inside `[n,2n)`;
2. the complete support of the band Green kernel;
3. the explicit size-biased weights;
4. the sparse first-entrance identity;
5. the top-site recursion (L-32301.12).

Not proved here:

1. the sign of the sparse source functional;
2. producer positivity;
3. RH.
