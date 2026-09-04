# Online claims and independent review boundary

```text
Search date: 2026-09-04
Purpose: identify concrete public objections to arXiv:2609.04176v1
Result: no stable indexed specialist post with a complete counterargument found
Independent mathematical verdict: the v1 proof is invalid as written
```

## What was searched

The search covered combinations of:

```text
"Catalan's constant is irrational"
"2609.04176"
"Zhi-Wei Sun"
"false" / "error" / "mistake" / "critique"
"Proposition 9.5"
"Theorem 5.1"
"B^2 log B"
"H_B^min"
"F_B"
```

and searches scoped to MathOverflow, Mathstodon, Bluesky, X/Twitter, Reddit,
Hacker News, general mathematical reference pages, and GitHub.

## Search result

The available index showed that the claim was circulating and that current
status pages treated it as unverified. It did not expose a durable specialist
post spelling out a complete error. Therefore this packet does not attribute
the countercheck to an unidentified online commenter and does not treat social
repetition as evidence.

The mathematical review was performed independently from the attached PDF.
It found a concrete obstruction in the proof of Proposition 9.5:

\[
\text{max-summand majorant}
\ge \frac{\rho^2}{2}B^2\log B-O(B^2),
\]

whereas the paper asserts cancellation to a finite `B^2` coefficient. See:

- [`DEEP_HOSTILE_REVIEW.md`](DEEP_HOSTILE_REVIEW.md)
- [`HEIGHT_BOUND_COUNTERCHECK.md`](HEIGHT_BOUND_COUNTERCHECK.md)

## Terminology discipline

The following statements are justified:

```text
The proof in arXiv:2609.04176v1 is invalid as written.
The preprint does not establish that Catalan's constant is irrational.
The irrationality problem remains unresolved pending a corrected proof.
```

The following stronger statement is **not** justified:

```text
Catalan's constant is rational.
```

Nor does the countercheck rule out every possible repair of the determinant
architecture. A repair would need a new signed Cauchy--Binet cancellation,
stronger common divisibility, or a redesigned scalar.

## Current secondary status references

At the search date, the following public pages still described irrationality
as unknown or the new preprint as unverified:

- MathDB, *Irrationality of Catalan's constant*;
- Wolfram MathWorld, *Catalan's Constant*;
- Wikipedia, *Catalan's constant*.

These pages are status indicators, not proof authorities. The repository
verdict rests on the internal asymptotic countercheck, not on those summaries.
