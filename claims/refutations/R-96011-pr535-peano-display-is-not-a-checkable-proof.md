# R-96011 — PR #535's displayed four-block Peano formula is not yet a checkable proof of annular positivity

Claim ID: `R-96011`  
Status: **PROOF-COMPLETENESS FIREWALL; THE POSITIVITY STATEMENT IS NOT REFUTED**  
Created: 2026-08-16  
Frozen target: `L-94201` on PR #535  
RH status: **unproved**

The theorem claimed in PR #535 is

\[
a_X^{(4)}(n)=c_X(n)-c_{X/4}(n)\ge0.
\]

The retained triangular computations support this statement. They do not
validate the displayed Peano proof. The load-bearing display `L-94201.5` has
three reconstruction failures:

1. the set \(\mathcal J_{X,n,h}\) is described but never defined as a formula;
2. the two edge terms \(\mathcal E^{\rm left},\mathcal E^{\rm right}\) are not
   given, so their equality to the omitted cut blocks cannot be checked;
3. the sentence that all Möbius signs disappear under a four-block switch is
   not accompanied by a coefficient-preserving involution or an algebraic
   expansion.

The direct verifier on PR #535 checks the original triangular inverse. It does
not evaluate the right side of `L-94201.5`, because that right side is not fully
specified. Thus the display cannot be imported as a theorem.

This successor keeps the following exact facts:

```text
triangular inverse                    exact
scale-four annular target             exact
finite annular telescope              exact
large deterministic positivity scans evidence
universal annular positivity proof    not yet certified
```

The scientific response is to replace the stale endpoint consumer and reduce
the positivity producer to the two smallest rows, rather than conceal the
missing Peano algebra.
