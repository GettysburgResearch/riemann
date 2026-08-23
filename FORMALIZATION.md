# Formalization track

The formalization project lives in [`formal/`](formal/README.md) as a self-contained Lean 4/Lake project inside this repository.

Its first source release is the reviewed scientific integration at commit
`852d8aa05c701ea7818ce8a50543e68987fef5cc`, covering research through PR #707.
Research after that cutoff is intentionally excluded until it receives a later exact-SHA review.

The formal track has three separate notions of status:

1. **scientific status** from `canonical/2026-08-22/claims.tsv`;
2. **statement status**: whether the intended proposition has been expressed in Lean;
3. **proof status**: whether that exact proposition has a sorry-free proof under the declared trust policy.

An open RH-bearing claim may be stated and used as an explicit theorem hypothesis. It must never be installed as an axiom asserting that it holds.

Start with:

- [`formal/README.md`](formal/README.md)
- [`formal/TRUST.md`](formal/TRUST.md)
- [`formal/ROADMAP.md`](formal/ROADMAP.md)
- [`formal/registry/README.md`](formal/registry/README.md)
