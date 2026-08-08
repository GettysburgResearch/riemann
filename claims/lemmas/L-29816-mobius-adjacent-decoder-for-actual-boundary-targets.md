# L-29816 — Möbius–adjacent decoder for actual boundary targets

Claim ID: `L-29816`  
Title: Every finite boundary target is realized exactly in the actual integer carry coordinates by its multiples-Möbius transform and the sparse adjacent-tree commutators; its negative capacity debt is bounded by one divisor-weighted source norm  
Status: **PROPOSED COMPLETE EXACT/ANALYTIC LEMMA**  
Authoring agent: `gpt56-02-r`  
Created: 2026-08-08  
Dependencies: `L-26205`, `L-27207`; elementary divisor switching  
Scope: arbitrary finite target on carry columns; no positivity or RH assumption

## 1. Exact target decoder

Fix an endpoint `X` and let

\[
 h(2),\ldots,h(X)
\]

be an arbitrary real target on the carry columns. Define its multiples-Möbius
transform

\[
 \boxed{
 u_m=\sum_{k\le X/m}\mu(k)h(mk),
 \qquad 2\le m\le X,}
\tag{L-29816.1}
\]

and put `u_(X+1)=0`.

By `L-26205`, the unique size-zero node divergence producing `h` has

\[
 r_m=u_m-u_{m+1}
 \qquad(m\ge2).
\tag{L-29816.2}
\]

Let

\[
 E_m=T_{m+1}-T_m
\]

be the adjacent-tree commutator of `L-27207`, with

\[
 \partial E_m=e_{m+1}-e_m-e_1.
\tag{L-29816.3}
\]

Define the signed balanced flow

\[
 \boxed{
 \mathscr A(h)
 =\sum_{m=1}^{X-1}u_{m+1}E_m.}
\tag{L-29816.4}
\]

For every node `n>=2`, its divergence coefficient is

\[
 u_n-u_{n+1}=r_n.
\]

Each `E_m` is size-zero, so the node-one coefficient is automatically the
required size-conservation completion. Therefore

\[
 \boxed{
 \partial\mathscr A(h)=r^{(h)},}
\tag{L-29816.5}
\]

and `L-26205` gives

\[
 \boxed{
 \operatorname{load}_q\mathscr A(h)=h(q)
 \qquad(2\le q\le X).}
\tag{L-29816.6}
\]

This is an exact source-to-carry intertwiner in the actual integer coordinates.
No tensor scaling, coprimality assumption, or formal parity node is used.

## 2. Absolute capacity of one commutator

Put

\[
 \|v\|_{\omega,1}=\sum_e\omega_e|v(e)|.
\tag{L-29816.7}
\]

The sparse recursions of `L-27207` and the elementary edge bound
`omega_e<=2sqrt(parent(e))` give

\[
 \|E_n\|_{\omega,1}
 \le4\sqrt{n+1}+\|E_{\lfloor n/2\rfloor}\|_{\omega,1}.
\tag{L-29816.8}
\]

Iterating the geometric parent descent yields the safe explicit bound

\[
 \boxed{
 \|E_n\|_{\omega,1}
 \le4(2+\sqrt2)\sqrt{n+1}.}
\tag{L-29816.9}
\]

The exceptional initial cancellations only improve this estimate.

Consequently

\[
 \mathcal N_\omega(\mathscr A(h))
 \le4(2+\sqrt2)
 \sum_{m=1}^{X-1}\sqrt{m+1}\,|u_{m+1}|.
\tag{L-29816.10}
\]

## 3. Divisor-switch bound

Insert (L-29816.1), discard only the Möbius signs for this upper bound, and
write `n=(m+1)k`:

\[
\begin{aligned}
\sum_{m=1}^{X-1}\sqrt{m+1}|u_{m+1}|
&\le
 \sum_{m=1}^{X-1}\sqrt{m+1}
 \sum_{k\le X/(m+1)}|h((m+1)k)|\\
&=
 \sum_{n=2}^{X}|h(n)|
 \sum_{\substack{d\mid n\\d\ge2}}\sqrt d.
\end{aligned}
\tag{L-29816.11}
\]

Since

\[
 \sum_{d\mid n}\sqrt d\le\tau(n)\sqrt n,
\]

we obtain

\[
 \boxed{
 \mathcal N_\omega(\mathscr A(h))
 \le4(2+\sqrt2)
 \sum_{n=2}^{X}\tau(n)\sqrt n\,|h(n)|.}
\tag{L-29816.12}
\]

Thus the proof-facing boundary norm is

\[
 \boxed{
 \|h\|_{\rm bd}
 :=\sum_{n=2}^{X}\tau(n)\sqrt n\,|h(n)|.}
\tag{L-29816.13}
\]

Any polylogarithmic bound for this explicit norm gives a polylogarithmic
negative-debt realization in the correct carry metric.

## 4. Shifted cutoff sources

The boundary functions emitted by `L-28402` are finite combinations of:

\[
 \Delta_k^j f(kq+a),
 \qquad a\in\{-1,0\},
\]

at first omitted quotient indices, plus the exact Euler remainder.  They are
actual functions of the carry column `q`; hence (L-29816.1)--(L-29816.13) apply
directly after all equal arithmetic destinations are recombined.

For a derivative-type source satisfying

\[
 |h(n)|\le Cn^{-3/2}[1+\log(X/n)]
\tag{L-29816.14}
\]

one has, by the elementary average divisor bound,

\[
\begin{aligned}
\|h\|_{\rm bd}
&\le C\sum_{n\le X}{\tau(n)\over n}
 [1+\log(X/n)]\\
&=O(\log^3(2X)).
\end{aligned}
\tag{L-29816.15}
\]

More generally, every additional finite-difference order improves the power of
`n` and remains polylogarithmic in this norm.

This supplies the exact algebra behind the divisor-switch sentence in
`L-28402.10`.

## 5. Why this replaces the false scaled sibling map

The withdrawn `L-29815` tried to scale one univariate Pascal sibling by a common
multiplicative destination.  The exact counterexample there shows that carry
columns do not tensor through noncoprime residue chains.

The present decoder instead:

1. retains the full boundary target `h(q)` on actual carry columns;
2. performs the exact multiples-Möbius inversion;
3. realizes the resulting actual node divergence by `E_m`;
4. charges every gcd/noncoprime chain inside the divisor sum (L-29816.11).

No arithmetic source is omitted.

## 6. Consequence for DCD

For a complete boundary bank `h_a` at cascade depth `a`,

\[
 \boxed{
 \mathcal D_{\rm boundary}
 \le4(2+\sqrt2)\sum_a\|h_a\|_{\rm bd}.}
\tag{L-29816.16}
\]

Therefore the remaining all-generation theorem can be stated without formal
parity nodes:

\[
 \boxed{
 \sum_a\|h_a\|_{\rm bd}=O(\log^A(2X)).}
\tag{L-29816.17}
\]

Combined with the exact analytic/cutoff Duhamel expansion of `L-28402`, this
would prove DCD in the actual carry coordinates.

## 7. Proof boundary

Proved here:

- exact Möbius decoder for every finite target;
- exact adjacent-tree flow realizing the decoded divergence;
- explicit square-root absolute capacity of every commutator;
- exact divisor-switch boundary norm;
- polylog bound for derivative-type first-generation sources.

Open:

- the all-generation sum (L-29816.17) for the complete Duhamel bank;
- DCD;
- RH.
