# L-106081 — The minimum-owner horizon gauge forces a core-paid phase prime

Claim ID: `L-106081`  
Programme aliases: `LFAM1.MINIMUM_OWNER_GAUGE`, `STRESS.CORE_PAID_OWNER_PHASE`, `LFAM2.SOURCE_OWNED_SMALL_CONDUCTOR`  
Status: **PROVED EXACT OWNER/CORE GEOMETRY THEOREM**  
Created: 2026-08-25  
Depends on: parent `L-102746--L-102749`, `L-102887`; `L-106080`  
Programme issues: #743, #736, #737  
RH status: **not assumed**

Fix one dyadic physical horizon `Y<=X<2Y`.  As in parent `L-102887`, every
active squarefree labelled occurrence has at most one prime label greater than
`4 sqrt(Y)`.  The repeated physical-`67` sector has already been assigned to
the closed repeated-label diagonal.

## 1. Deterministic minimum-owner rule

For each remaining occurrence of depth at least two, choose its unordered owner
pair by the following frozen rule.

```text
If a unique label h>4 sqrt(Y) occurs:
  choose h and the smallest other physical-prime label.

Otherwise:
  choose the two smallest physical-prime labels.
```

The rule depends only on the labelled source occurrence and the declared
horizon.  It is fixed before Vaughan decomposition, additive phases, a norm, a
negative part, or a hypothetical zero.

It is horizon-safe: the only potentially uncompletable label is selected as an
owner.  Every nonowner is therefore completable by the exact parent gauge.
Moving the canonical equal-pair allocation to this pair costs at most

\[
\binom{k}{2}\ll(\log(2Y))^2
\]

on a depth-`k` occurrence, exactly as in `L-102747` and `L-102887`.

## 2. Distinguished owner

Let

\[
P=\lambda\Lambda
\]

be the selected pair with `lambda<Lambda`, and call `lambda` the distinguished
owner.  After completing every nonowner, the physical monomial is

\[
N=P a^2,
\qquad \mu^2(a)=1,
\qquad(a,P)=1.
\]

Suppose the Boolean balanced coefficient of `L-106080` at `a` is nonzero.
Then `a` contains at least two distinct prime labels.

If no exceptional large label occurs, both owners are the two smallest labels,
so every prime in `a` is at least `lambda`.

If the exceptional label occurs, the other owner `lambda` is the smallest of
all remaining labels, so again every prime in `a` is at least `lambda`.

In either case, two distinct core primes give

\[
\boxed{
\lambda^2\le a.
}
\tag{L-106081.1}
\]

This is coefficient-exact.  It does not use an average prime size or a
congruence-density heuristic.

## 3. Static source blocks

Partition the already carrier-recombined balanced source linearly by

\[
B\le a<2B,
\qquad
L\le\lambda<2L.
\]

Equation (L-106081.1) implies

\[
\boxed{L^2\le\lambda^2\le a<2B.}
\tag{L-106081.2}
\]

Thus every nonempty block automatically lies in the core-paid range

\[
L^2<2B.
\]

The co-owner `Lambda`, the Boolean Vaughan representation, the marked-`67`
sector, the carrier chart, the shell and all overlap-renewal labels remain in
the Hilbert coordinate.  No source occurrence is duplicated.

## 4. Clean cross terms

After the inherited shared-owner and owner/core renewals, two different owner
packets have clean products

\[
N=\lambda\Lambda a^2,
\qquad
M=\rho R b^2,
\]

with four distinct owner labels and neither distinguished owner dividing the
opposite core.  Hence

\[
\lambda\mid N,\quad\lambda\nmid M,
\qquad
\rho\mid M,\quad\rho\nmid N.
\]

The two prime Ramanujan identities are therefore nonzero and source-exact:

\[
1=-\sum_{h=1}^{\lambda-1}e_\lambda(h(N-M)),
\qquad
1=-\sum_{k=1}^{\rho-1}e_\rho(k(N-M)).
\tag{L-106081.3}
\]

Their product is `+1`.  The selected phases are the distinguished-owner
coordinates of the two linear source atoms; they are not chosen after the
cross term is numerically evaluated.

## Meaning

The former short-core obstruction arose because an arbitrary owner gauge could
select phase primes much larger than the core.  The minimum-owner gauge and the
literal squarefree balanced support remove exactly that mismatch:

```text
balanced source atom
  -> two distinct core primes
  -> distinguished owner squared <= core
  -> owner phase range squared <= core octave.
```

The theorem proves this geometry, not the coherent phase estimate.  The latter
is the content of `L-106082`.