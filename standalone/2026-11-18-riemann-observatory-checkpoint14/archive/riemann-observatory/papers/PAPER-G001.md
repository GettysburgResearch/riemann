# PAPER-G001: Numbers of solutions of equations in finite fields

André Weil. Bulletin of the American Mathematical Society 55 (5), 497–508 (1949). DOI: 10.1090/S0002-9904-1949-09219-4. [Primary source](https://math.ucr.edu/~res/math205B-2021/app2number-theory/weil-conjectures1949.pdf).

**Audit status:** L1; full substantive reading = True. All twelve printed pages 497–508 read. Independently reconstructed the finite Gauss-sum norm argument in equation (4); character/Jacobi/Davenport–Hasse architecture traced. Not a full L2 audit of every lifting argument or antecedent.

**Source identity:** Original 1949 journal paper, university-hosted scan; SHA-256 `55cb48abcb191cb344c01587afed7c9fea809b31826c5803c5dbd3092d1dd468`. Corrections: Not systematically searched; no assertion that all corrections or later versions were located.

## Main mathematical results

- **Equation (4), pp. 500–501:** For a nontrivial multiplicative character χ and nontrivial additive character ψ of Fq, the Gauss sum has squared absolute value q.
- **Formula (3), p. 500; estimate p. 502:** For ai∈Fq* and positive ni, the number N of affine solutions of Σ(i=0..r) ai xi^ni=0 satisfies |N−q^r|≤M(q−1)q^((r−1)/2), with M the number of rational tuples 0<αi<1, ni αi∈Z, Σαi∈Z. The actual character sum is restricted by di=gcd(ni,q−1); the stated M is a q-independent upper bound.
- **Equation (5), pp. 503–505:** For degree-v finite-field extension, lifted characters χ′=χ∘Norm and ψ′=ψ∘Trace satisfy −G(χ′,ψ′)=(−G(χ,ψ))^v.
- **pp. 505–507, equation (8):** Diagonal projective examples yield rational generating functions with eigenvalue magnitudes matching their expected weights. The general higher-dimensional statements on p. 507 are explicitly conjectural in this paper.

## Definitions and notation

- Multiplicative and additive characters; gcd di=gcd(ni,q−1).
- Source Jacobi sum j(α), defined for nonzero character exponents summing to zero modulo 1.
- Extension-field norm/trace; generating series of point counts; conjectural Betti factors.

## Proof architecture

- Express power-preimage counts by multiplicative character orthogonality.
- Reduce nonzero character contributions to Jacobi sums.
- Evaluate Gauss-sum norms and express Jacobi sums as products divided by q.
- Use norm/trace lift and a formal Euler product of monic polynomials to compare extensions.
- Pass from homogeneous affine counts to projective counts; infer diagonal zeta weights; formulate general conjectures.

## Limitations

- The general Weil-conjecture package is conjectural here, not proved.
- Smooth proper/projective hypotheses must be explicit in modern restatement; open A1/Gm refute unrestricted proper-curve factorization.
- Square-root Gauss cancellation does not constitute a general cohomological purity proof.
- No implication to classical RH is established.

## Concrete research questions

- Formalize the small Gauss-norm proof with both nontriviality hypotheses.
- Track exactly which diagonal equations give pure cohomological factors versus degenerations when characteristic divides the exponent.
- Compare formal Euler-product positivity with the genuinely geometric pole-control hypotheses.

## Context and reuse

The source belongs to the finite-field/geometry program. The campaign’s reusable outputs are a precise purity statement, a hypothesis-deletion countermodel, and a quantified tensor-amplification requirement. None constitutes a result about classical ζ zeros. Later uses/corrections were not systematically mapped in this round. Preserve original notation in the source; this record uses F for geometric Frobenius and q for the finite-field cardinality.
