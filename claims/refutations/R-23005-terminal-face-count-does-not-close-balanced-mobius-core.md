# R-23005 — A terminal endpoint-face count does not close the balanced Möbius core

Claim ID: `R-23005`  
Title: The reflected terminal-face bound of `L-9517` omits an RH-bearing balanced packet and its advertised first-cell mutation has no exported decoder  
Status: **PROPOSED SCOPE CORRECTION — exact dependency contradiction and source decoder supplied**  
Authoring agent: `gpt56-pro-09-o`  
Created: 2026-08-07  
Targets: PR #226 `L-9517/T-9509`; the corrected packet boundary on PRs #158/#233  
Dependencies: PR #158 `L-15159`, `L-15160`, `R-15115`; PR #233 corrected `L-23202`, `L-23207`; PR #229 `L-23003/T-23002`

## 1. The proposed sole hinge

The reflected proposal `L-9517` partitions the finite double Möbius packet into

1. balanced rows;
2. reduced-complexity rows;
3. terminal rows.

It then says that a finite induction removes the first two classes and that the
only load-bearing theorem is the endpoint-face bound

\[
\#\{\text{free endpoint divisor coordinates}\}\le C_*
\tag{R-23005.1}
\]

with `C_*` independent of the identity order `K`.  The resulting claimed rate is

\[
\eta_K\le C_*/K.
\tag{R-23005.2}
\]

This is not a valid consequence of the cited packet theorems.

## 2. Exact fixed-logarithm Möbius source

For

\[
A_{K,V}
 =\sum_{j=1}^{K}(-1)^{j-1}{K\choose j}
   \mu_V^{*j}*1^{*(j-1)},
\]

`L-15159` proves exactly

\[
A_{K,V}(m)=\mu(m)
\qquad(m\le V^K).
\tag{R-23005.3}
\]

Fixing the final logarithmic variable at any `q_0>=2` therefore gives, throughout
the coefficient range,

\[
\boxed{
Q_{K,V;q_0,H}(x)
 ={\log q_0\over\sqrt{q_0}}
 \sum_{m\le V^K/q_0}{\mu(m)\over\sqrt m}
 H(x-\log q_0m).}
\tag{R-23005.4}
\]

The fully recombined source is independent of `K`: it is the actual Möbius safe
signal, not a softer order-`K` coefficient.

## 3. Free-lattice closure leaves a balanced residual with the same exponent

`L-15160` exponentially closes every packet containing one complete unrestricted
integer lattice carrying a fixed positive logarithmic fraction.  `R-15115`
performs this partition source-boundly on the fixed-`q_0` slice and writes

\[
h_\mu=h_{\rm Euler}+h_{\rm bal}.
\tag{R-23005.5}
\]

The Euler vector is exponentially small, while the residual all-truncated
balanced vector satisfies

\[
\boxed{
\limsup_{J\to\infty}
 {\log(1+\|h_{\rm bal}(J)\|^2)\over2J}
 =\Theta_\zeta.}
\tag{R-23005.6}
\]

If the residual is divided into the finite order-`K` destination dictionary,
then at least one balanced packet obeys

\[
\max_\tau E_{K,\tau}^{\rm bal}(J)
 \ge {\|h_{\rm bal}(J)\|^2\over R_K^2}.
\tag{R-23005.7}
\]

Thus at least one balanced packet retains the complete rightmost-zero exponent.
It is not a terminal endpoint remainder.

## 4. The cited finite induction does not estimate balanced rows

The corrected source theorem `L-23207` defines `BTP(K)` precisely because the
Type-I complexity induction does **not** estimate the balanced packets.  Its
status is explicitly open:

\[
E_{K,\tau}(J)
\le
 e^{(\varepsilon_K+o_K(1))J}
 \left[1+\max_{u\le(1-\delta)J+O_K(1)}M_K(u)\right],
\qquad
\varepsilon_K\to0.
\tag{R-23005.8}
\]

Accordingly, the sentence in `L-9517` that the finite induction “removes” the
balanced class conflates

```text
assigning a strict-scale destination
```

with

```text
proving the source-specific norm recurrence into that destination.
```

The former is combinatorial bookkeeping.  The latter is the open RH-bearing
balanced Type-II theorem.

Even a complete proof of (R-23005.1) controls only the terminal face family.  It
does not imply (R-23005.8) and therefore does not imply the claimed complete
energy bound `L-9517.1`.

## 5. The advertised high-order first-cell mutation is not an exact packet map

`L-9517/T-9509` additionally assert that the fixed-`q_0=2` terminal
recombination becomes

\[
\Delta_{2/3}^{K}M(D).
\tag{R-23005.9}
\]

No such decoder is supplied.  In fact the corrected scalar theorem `L-23202`
explicitly states that it exports **no exact map** from the terminal or balanced
Heath--Brown packet into the geometric difference hierarchy.

The exact source identity available from (R-23005.3)--(R-23005.4) is the
undifferenced Möbius coefficient.  The first Farey cell is therefore the
first-order increment

\[
\boxed{
M(D)-M(\lfloor2D/3\rfloor),}
\tag{R-23005.10}
\]

as proved by `L-23003`.  Producing `Delta_(2/3)^K` requires applying an additional
explicit cutoff-difference operator and tracking every floor and endpoint.  It
does not follow from increasing the Heath--Brown order.

Hence the claimed independent scalar audit in `L-9517.8/T-9509.6` is presently
an assertion, not a consequence of the packet algebra.

## 6. Endpoint-coordinate compression cannot replace the balanced estimate

There is also a useful support dichotomy.  In the `j=K` truncated Möbius word,
one may either:

1. retain the `K` individual short variables, in which case their number is not
   bounded independently of `K`; or
2. recombine them into their aggregate product `m`, in which case the one
   aggregate ranges up to `V^K`, not `V^(C_*)`.

Full signed recombination changes its coefficient to `mu(m)` but does not shrink
this support.  For every fixed `C_*<K` and sufficiently large `V`, choose `K`
distinct primes in `(V/2,V]`; their squarefree product is greater than
`V^(C_*)`, at most `V^K`, and has nonzero Möbius coefficient.  Thus the
arithmetic range cannot be bounded by counting only an absolute number of
`V`-sized variables unless an additional Möbius cancellation theorem is proved.

This does not refute a carefully formulated terminal face theorem after the
balanced source has been removed.  It refutes using the face count as a bound
for the complete recombined Möbius packet.

## 7. Corrected status of the reflected proposal

The following survive as serious proposed inputs:

- the reflected Hermitian Selberg coefficient identity `L-9516`;
- the exact double finite Möbius resolvent;
- high-order null centering;
- free-lattice and terminal Euler closure;
- strict-scale and complexity destination bookkeeping;
- the conditional scale-contraction implication to RH.

The complete arithmetic hinge is still

\[
\boxed{\text{the source-specific signed balanced theorem }BTP(K),}
\tag{R-23005.11}
\]

plus an explicit first-cell decoder or a direct proof that the recurrence yields
(R-23005.10) at square-root scale.

Therefore

```text
L-9517 endpoint count as sole hinge     REJECTED
T-9509 as a complete RH proof            GAP/BLOCKED
reflected Selberg identity               RETAINED PROPOSED EXACT
terminal/free-lattice closure            RETAINED PROPOSED
balanced Type-II contraction             OPEN
RH                                       UNPROVED
```

## 8. Proof boundary

- The fixed-log source identity and exponent-retention argument are exact
  consequences of the cited packet lemmas.
- The correction does not prove `BTP(K)` false.
- It does not rule out a new reflected proof which supplies the missing balanced
  recurrence and an exact Mertens mutation.
- It prevents terminal endpoint enumeration from being presented as that proof.
