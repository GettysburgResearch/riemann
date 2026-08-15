# L-91752 — The factor-67 root `Y_4` cost is directly logarithmic

Claim ID: `L-91752`  
Status: **PROVED CONDITIONAL ON THE EXPLICIT FROZEN ALL-COLUMN/ENDPOINT ESTIMATES — NO RH-BEARING BENCHMARK BRIDGE**  
Created: 2026-08-15  
Frozen inputs: PR #479 at `518b6a5ec2b49b7decbd4c2e349d0ee5b26bfc9b`; `L-91377/L-91378`; the exact uncorrected root-capacity identity; fixed terminal and base estimates  
RH status: **unproved**

## 1. Correct scalar and exact ideal saturation

Let

\[
 K=\left\lfloor X/67\right\rfloor+1,
 \qquad
 \tau_K=\frac{\sqrt K}{\sqrt K+130}.
\]

Before omissions, thinning and finite realization, the exact factor-67
common-parent identity is the native equality packet. Hence its complete ideal
radix-four coordinate is

\[
 \Xi(P_X^{\rm ideal})=\Omega_X.
\tag{L-91752.1}
\]

After the actual one-shot common-parent realization of `L-91753`, put

\[
 r_X=\Omega_X-\Xi(P_X^{\rm root})\ge0
\]

and

\[
 \delta_X=\langle Y_4,r_X\rangle.
\tag{L-91752.2}
\]

The proof estimates this literal native slack. It never estimates
`4 sqrt(X)-H(d_X)` and never assumes an eventual upper bound for
`J_Lambda(X)-4 sqrt(X)`.

## 2. Sparse `Y_4` sums

The exact radix-four dual support is

\[
 Y_4(2^e)=\bigl(2^{\lceil e/2\rceil}-1\bigr)\log2,
\]

\[
 Y_4(4^vp^a)=2^v\log p
 \quad(p\text{ odd prime}),
\]

and `Y_4(q)=0` otherwise. The elementary estimates of the frozen native-slack
packet give

\[
 \boxed{\sum_{q\ge2}\frac{Y_4(q)}{q^{3/2}}<11,}
\tag{L-91752.3}
\]

\[
 \boxed{
 \sum_{q\le X}\frac{Y_4(q)}q
 \le3+2L+2L^2,
 \qquad L=\log(2X).
 }
\tag{L-91752.4}
\]

## 3. All-column finite realization

PR #479 proves, after exact inner/outer carry-cell ownership, that every
nonterminal physical column satisfies

\[
 |e_X(q)|<\frac{971}{4q\sqrt K}
 \qquad(2\le q\le X/4).
\tag{L-91752.5}
\]

Pairing with (L-91752.4),

\[
 \sum_{2\le q\le X/4}Y_4(q)|e_X(q)|
 <\frac{971}{4\sqrt K}(3+2L+2L^2)=o(1).
\tag{L-91752.6}
\]

This estimate includes the formerly omitted columns `q<K`.

The positive same-cell refinement is chosen inside the remaining all-column
reserve so that its complete native-dual cost is below `X^-2`. The finitely
many activation collars are removed before the split. Their native-score
measure is absolutely continuous: on the compact root window the packet
benchmark is bounded and the endpoint density is bounded. Therefore the
collars may also be chosen to have native cost below `X^-2`.

## 4. Bottom and top omissions

On the bottom width-two interval in the endpoint variable `s`, one has
`s>=K`, the endpoint density is below `4 ds/s`, and the root-fibre benchmark is
bounded on `1<=x<67`. Thus its native cost is `O(K^-1)=o(1)`.

The fixed top omission is a positive current-owned endpoint packet. The frozen
terminal estimate gives directly

\[
 \langle Y_4,\Xi(P_X^{\rm top})\rangle
 =O(WX^{-1/2}\log^2(2X))=o(1)
\tag{L-91752.7}
\]

for the fixed width `W=10000`. It simultaneously supplies the strict terminal
capacity margin. No sign or estimate for `J_Lambda-4 sqrt(X)` is involved.

## 5. Square-root thinning

The common scalar thinning removes at most the fraction

\[
 1-\tau_K<\frac{130}{\sqrt K}
\]

of the exact native packet. Its native cost is therefore at most

\[
 (1-\tau_K)J_\Lambda(X).
\tag{L-91752.8}
\]

Unconditionally,

\[
 \Lambda(n)\le\log X
 \qquad(n\le X)
\]

and the decreasing-function integral estimate gives

\[
 \sum_{n\le X}n^{-1/2}\log(X/n)<4\sqrt X.
\]

Hence

\[
 J_\Lambda(X)<4\sqrt X\log X.
\tag{L-91752.9}
\]

Since `K>X/67` and `sqrt(67)<33/4`,

\[
 \boxed{
 (1-\tau_K)J_\Lambda(X)<4290\log X.
 }
\tag{L-91752.10}
\]

This is an elementary upper bound on the positive benchmark itself. It is not
the RH-equivalent estimate `J_Lambda-4 sqrt(X)=O(log X)` rejected by PR #484.

## 6. Base and port

The finite base packet has fixed finite support. On the frozen base-packet
realization its exact radix-four response is a fixed finite vector, and
therefore its `Y_4` pairing is one absolute constant. The root matrix port is a
separate PSD coordinate, has no radix-four component, and contributes exactly
zero to the pairing with `Y_4`. Its role is feasibility only.

All finite mismatch, taper and base corrections are current-owned once. No
correction cost is copied into a child.

## 7. Root bound

The ideal native identity (L-91752.1) and positivity show that the final root
slack is bounded above by the sum of the preceding discarded/error packets.
Therefore, for one absolute constant `A_0`,

\[
 \boxed{
 \delta_X=\langle Y_4,r_X\rangle
 \le A_0+4290\log(2X).
 }
\tag{L-91752.11}
\]

The leading logarithmic term is caused only by the explicit common square-root
thinning. Every other root charge is `O(1)` or `o(1)`.

## 8. Boundary

```text
ideal root packet saturates native detail        FROZEN EXACT IDENTITY
all columns q>=2                                 PR #479 / EXACT ON INPUT
mismatch/refinement/collar native cost           o(1)
bottom/top omission native cost                  o(1)
common thinning native cost                      <4290 log X
finite base native cost                          O(1)
root port Y4 cost                                exactly zero
local root slack                                 A0+4290 log(2X) ON FROZEN ESTIMATES
RH-bearing benchmark bridge                      NOT USED
Riemann Hypothesis                               UNPROVEN
```
