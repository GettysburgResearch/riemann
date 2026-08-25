# L-102962 — The canonical equal-pair gauge is horizon-safe on the Boolean balanced source

Claim ID: `L-102962`  
Status: **PROVED EXACT OWNER-GAUGE BYPASS**  
Created: 2026-08-25  
Depends on: `L-102746--L-102749`, `L-102830`, `L-102887`; `L-102957`  
RH status: **not assumed**

Fix a cofinal dyadic horizon \(Y>64\). Let \(S\) be any labelled occurrence contributing to the Boolean balanced row.

## 1. Every label is completion-safe

If one label \(h\in S\) satisfied

\[
h>4\sqrt Y,
\]

then the horizon-safe minimum-owner rule would select \(h\) and the smallest other label. The remaining Boolean balanced core would still contain two disjoint factors larger than \(U=\lfloor Y^{1/6}\rfloor\), contradicting `L-102957`.

Therefore

\[
\boxed{
p\le4\sqrt Y\quad\text{for every physical-prime label }p\in S.}
\tag{L-102962.1}
\]

## 2. Every unordered pair is horizon-safe

Choose any unordered pair \(P\subset S\). Every nonowner label remains at most \(4\sqrt Y\), so the exact positive completion/gauge transfer may be applied to all labels in \(S\setminus P\) at the frozen horizon cutoff.

Thus every pair in the canonical equal-pair Duhamel decomposition has a legal completed realization. No exceptional pair or transfer atom is omitted.

## 3. Canonical equal-pair realization

For \(k=|S|\), assign the occurrence equally to all \(\binom{k}{2}\) unordered pairs, as in `L-102746`. The owner weights sum to one, so the physical realization is coefficient-exact. The repeated labelled-\(67\) pair remains in its already-closed diagonal ledger.

Compared with any concentrated deterministic pair gauge, the equal-pair gauge has no larger labelled energy:

\[
\sum_{|P|=2}
\left\|{v_S\over\binom{k}{2}}\right\|^2
=
{1\over\binom{k}{2}}\|v_S\|^2.
\tag{L-102962.2}
\]

Hence returning from the minimum-owner gauge to the canonical equal-pair gauge costs nothing at free-energy scope and removes the star/cycle transfer current of `L-102961` from the conclusion-facing source.

## 4. Consequence

The minimum-owner rule remains a useful proof coordinate for the inequalities

\[
\lambda^2\le a,
\qquad
P\le a,
\]

but it is not a mandatory physical owner coordinate. On the cofinal Boolean balanced source, one may retain the symmetric equal-pair gauge throughout and introduce phase labels independently through the primewise flat gauge.

Therefore `COCURL102980` is an optional concentrated-owner route, not an intrinsic final obstruction.