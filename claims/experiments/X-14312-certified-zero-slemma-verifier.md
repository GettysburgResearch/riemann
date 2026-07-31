# X-14312 — Exact certified-zero S-lemma floor verifier

Claim ID: `X-14312`  
Title: Fraction-only verification of a robust visible-cone floor  
Status: `EMPIRICAL`  
Authoring agent: `gpt56-pro-09-c`  
Created: 2026-07-31  
Dependencies: `L-14319`  
Scope: exact finite rational algebra; no zeta or special-function evaluation

`X-14312` checks the rational trust boundary in `L-14319.26`--`L-14319.27`.
It consumes:

```text
form midpoint A0,
visibility midpoint J0,
positive metric G,
relative Loewner radii eps_A and eps_J,
visibility threshold delta^2,
S-lemma multiplier alpha,
claimed floor F,
robust Slater vector.
```

It verifies with exact `fractions.Fraction` arithmetic:

1. rational symmetric matrix structure;
2. strict positive definiteness of `G`;
3. nonnegative radii and multiplier;
4. robust strict feasibility;
5. the complete robust S-lemma LMI by exact semidefinite LDL;
6. production provenance gates when the classification is not synthetic.

The retained exact model has

```text
A0 = diag(2,-1),
J0 = diag(1,0),
delta^2 = 3/4,
alpha = 3,
F = 5/4.
```

The unrestricted coordinate `e2` has form value `-1`, while the certified
visible-cone floor is `5/4`.  Eight adversarial tests are retained.  The checker
does not establish that a supplied matrix is a localized Weil matrix or that a
visibility matrix comes from certified zeta-zero evaluations; those are typed
upstream gates.
