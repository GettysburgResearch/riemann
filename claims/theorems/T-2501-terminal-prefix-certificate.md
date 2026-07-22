# T-2501 — Terminal streams certify a finite canonical search forest

Claim ID: T-2501  
Title: Deterministic terminal streams cover and certify a finite canonical search forest  
Status: PROPOSED  
Authoring agent: `gpt56-03-c`  
Reviewing agents: none  
Created: 2026-07-23  
Last updated: 2026-07-23  
Dependencies: L-2501; L-2502; rigorous dyadic enclosures for the Robin right-hand side  
Scope: finite proof-certificate semantics  
Related counterexample candidates: Robin witnesses

## Statement

Fix \(B>5040\) and form the finite canonical forest of L-2501, with one tree for
each \(1\le K\le K_B\).

A terminal token identifies either:

1. an internal prefix with a valid strict L-2502 prune; or
2. a full vector classified as below the Robin domain, strict satisfaction,
   rigorous violation, or unresolved.

Suppose a verifier reconstructs the forest in one fixed depth-first order and
obeys the following rules:

- at an internal node, a matching prune token terminates the entire subtree only
  after the L-2502 inequality is recomputed and proved;
- if no prune token matches, every exact child from L-2501 is reconstructed and
  visited;
- at a leaf, exactly one matching leaf token is consumed and its classification
  is recomputed;
- after the final tree, no token remains.

Then the token streams cover every canonical vector with integer at most \(B\)
exactly once.

If no above-domain leaf is unresolved or violating, every canonical integer
\(5041\le n\le B\) satisfies Robin's strict inequality.

For every strict terminal \(t\), let \(U_t\) be its exact abundancy value or
ceiling, let \(N_t\) be its leaf integer or minimum subtree integer, and let
\(L_t\) be a rigorous positive lower bound for
\(e^\gamma\log\log N_t\). Then

\[
C_t=\frac{U_t}{L_t}<1
\]

bounds the normalized Robin quotient of every integer covered by that terminal.
Consequently

\[
C_{\mathrm{can}}=\max_t C_t<1
\]

is a rigorous normalized-quotient upper bound throughout the finite canonical
region.

## Definitions

A token **matches** a node when its support and exponent prefix are exactly the
node's. The deterministic order is part of the schema, not an implementation
hint.

For a strict leaf, \(U_t=\sigma(n)/n\) and \(N_t=n\). For a prune, \(U_t\) and
\(N_t\) are the L-2502 ceiling and all-ones minimum completion.

## Motivation

Valid local prunes are insufficient if the search silently omits a support,
child, or leaf. This theorem separates mathematical coverage from the untrusted
search strategy and also extracts a quantitative global margin rather than a
list of isolated signs.

## Proof

Fix one support tree. Proceed recursively from its root.

At an internal node with an accepted prune token, L-2502 proves Robin's strict
inequality for every full vector in that subtree, so no descendant token is
needed. If no matching prune is present, the verifier visits the complete and
exact child set given by L-2501. By induction, each child subtree is covered
exactly once. At a leaf, the rules require exactly one matching token and a
recomputed classification. Thus every leaf below the node is covered exactly
once.

Applying this argument to every support \(1\le K\le K_B\), and using L-2501's
support completeness, proves exact coverage of the forest. Exhaustion of each
stream excludes extra or duplicate terminals.

If every above-domain terminal is strict satisfaction or a valid strict prune,
then every covered canonical integer satisfies Robin's inequality.

For a leaf, the exact abundancy is at most \(U_t\) and its right-hand side is at
least \(L_t\), so its normalized quotient is at most \(C_t\). For a pruned
subtree, L-2502 gives abundancy at most \(U_t\), while monotonicity of the Robin
right-hand side gives a denominator at least \(L_t\) for every completion.
Taking the maximum over the finite terminal set proves the global bound. ∎

## Analytic domain audit

The theorem uses only positive real values of the Robin right-hand side for
integers above 5040. The dyadic kernel's logarithm, Euler-constant, and
exponential enclosure proofs are separate dependencies.

## Dependency audit

- L-2501: exact support and child coverage.
- L-2502: soundness of every prune.
- Exact multiplicative arithmetic at leaves.
- Rigorous lower and upper dyadic enclosures for every sign.

## Gap audit

- The result stops at the exact bound \(B\).
- A verifier written by the same agent is an internal replay, not independent
  repository verification.
- Search and verifier sharing one interval kernel leaves that kernel as a common
  dependency.
- SHA-256 integrity does not replace arithmetic recomputation.

## Adversarial tests

- Delete, duplicate, or reorder one token.
- Insert a root prune, which L-2502 does not license.
- Tamper with the stored tightest-terminal summary while refreshing the outer
  digest.
- Compare all small-box vectors against a separately written brute-force list.
- Lower precision until one formerly strict terminal becomes unsupported and
  require rejection.

## Remaining uncertainty

The proof is elementary and complete-looking. The main remaining uncertainty is
implementation review of the two traversals and shared dyadic arithmetic.

## Suggested next attack

Have a verifier agent reproduce the certificate with an independent interval or
ball backend and a third traversal implementation.
