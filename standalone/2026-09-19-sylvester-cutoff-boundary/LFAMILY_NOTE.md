# Relevance to L-family programme #738

This note records a **separate** use of Burungale--Tian's Sylvester proof. It is not part of the Möbius-to-RH implication.

Issue #738 asks for GL(2) twist-family stress tests that distinguish:
- forced central zeros;
- simple versus higher central multiplicity;
- legitimate rank effects;
- off-critical zero geometry.

Burungale--Tian prove an exact rank-one theorem for the CM cubic-twist family
[
E_m:y^2=x^3+m^2/4.
]
For every prime (pequiv8pmod9), both (E_p) and (E_{p^2}) have analytic rank one. Their proof factors an auxiliary Rankin--Selberg L-function into the target factor and a complementary rank-zero factor, proves the relevant Heegner component non-torsion via a division boundary, and uses Gross--Zagier to obtain nonzero first derivative.

This gives #738 a theorem-backed set of sign (-1), exactly-simple-central-zero examples where the source of the simplicity is arithmetic rather than numerical zero finding.

Recommended bounded import:

1. Add a 'CM cubic-twist rank-one reference family' subsection to #738.
2. Treat it as an extension beyond the original quadratic-twist scope, not silently as the same family.
3. For (p=17) use the paper's explicit (q=13) example as a small exact fixture:
   - nontrivial cubic residue;
   - explicit first division;
   - nonzero division boundary;
   - integral cubic projector.
4. Compare detector behaviour before and after deflating the forced central zero.
5. Preserve the paper's evidence distinction: exact algebraic identities versus numerical recognition of some CM evaluations.

The most interesting detector question is whether a proposed 'rank correction' reacts only to the forced simple zero or also to the auxiliary arithmetic structure that proves simplicity. A detector that falsely treats this family as anomalous would be suspect.

Do **not** infer GRH information from the rank-one theorem; it controls the central order of vanishing, not all zeros.
