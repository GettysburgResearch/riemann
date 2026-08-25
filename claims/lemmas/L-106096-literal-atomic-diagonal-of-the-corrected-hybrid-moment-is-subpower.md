# L-106096 — The literal atomic diagonal of the corrected hybrid moment is subpower

Claim ID: `L-106096`  
Programme aliases: `LFAM1.CORRECTED_ATOMIC_DIAGONAL`, `LFAM2.FULLY_AMPLIFIED_DIAGONAL`, `STRESS.OWNER_CORE_RECIPROCAL_PAYMENT`  
Status: **PROVED UNCONDITIONAL SUBPOWER ATOMIC DIAGONAL**  
Created: 2026-08-25  
Depends on: `L-106095`; `L-106090--L-106092`; parent equal-product and free-energy ledgers  
Programme issues: #743, #736, #737  
RH status: **not assumed**

Expand the corrected moment `L-106095.9` into literal source atoms

\[
(\alpha,\beta)
=
\bigl((g,c,P,\ldots),(g,Q,d,\ldots)\bigr).
\]

The atomic diagonal means the same \((\alpha,\beta)\) occurs on both sides of
the square.

The two physical coefficients satisfy

\[
|a_\alpha|
\le {X^{o(1)}\over g\,c\sqrt P},
\qquad
|b_\beta|
\le {X^{o(1)}\over g\,d\sqrt Q}.
\tag{L-106096.1}
\]

Summing the nonzero phases contributes \(\ell-1\).  Multiplication by the
correct moment weight \(g^2\ell\) gives

\[
\begin{aligned}
g^2\ell(\ell-1)|a_\alpha|^2|b_\beta|^2
&\ll
X^{o(1)}
{\ell^2\over g^2c^2d^2PQ}.
\end{aligned}
\tag{L-106096.2}
\]

Write

\[
c=\ell m,\qquad \ell<P^-(m),
\tag{L-106096.3}
\]

with the convention \(m>1\), which holds in the two-sided balanced sector.
Then

\[
{\ell^2\over c^2}={1\over m^2}.
\tag{L-106096.4}
\]

For fixed \(m\), the number of possible primes \(\ell<P^-(m)\) is at most
\(m\).  Hence, on a finite horizon,

\[
\sum_{\substack{c\\P^-(c)=\ell}}
{\ell^2\over c^2}
\le
\sum_{m\le X}{1\over m}
\ll\log X.
\tag{L-106096.5}
\]

Also,

\[
\sum_g{1\over g^2}<\infty,\qquad
\sum_d{1\over d^2}<\infty,
\tag{L-106096.6}
\]

and

\[
\sum_{P=pq}{1\over P},
\quad
\sum_{Q=rs}{1\over Q}
\ll(\log\log X)^2.
\tag{L-106096.7}
\]

The Boolean representation, equal-pair, shell, carrier and finite renewal
multiplicities are \(X^{o(1)}\).

Therefore

\[
\boxed{
\widetilde{\mathfrak M}_{\rm LDRT}^{\rm literal\ atomic\ diagonal}(Y)
=
Y^{o(1)}.
}
\tag{L-106096.8}
\]

## Exact remaining packet

Every remaining term differs in at least one literal source incidence:

```text
different left anchor;
different opposite owner/core atom;
or both.
```

Equal physical products and inherited representation diagonals are already
closed by the parent ledgers.  The live theorem is therefore a genuinely
off-diagonal fully amplified family correlation.

## Scope

The lemma does not claim that the whole same-anchor block is diagonal: two
different opposite owner/core atoms may still interfere coherently.  It pays
only the exact atomic diagonal and leaves every genuine cross-incidence term
visible in `T-106100`.
