# Selected manuscript equations, transcribed for the import

Attribution: Dean Cureton and Jesse Thorner, with AxiomProver, *A quasi-Riemann
hypothesis for Dedekind zeta functions*, Hexagon 2610.00200v2 (2026).
Source: https://hexagonmath.org/api/v1/works/2610.00200v2/source?path=DedekindZeta.tex
License: Creative Commons Attribution 4.0, https://creativecommons.org/licenses/by/4.0/

These are selected mathematical transcriptions with ASCII notation and local
annotations, not a byte-identical copy of the full TeX or an endorsement by
the authors. The full version-specific source is linked above.

**Theorem 1.1:** for any number field K, zeta_K(s) is nonzero when
Re(s)>31/32 and s!=1. Corollary 1.2 treats finite-order Hecke L-functions
wherever they are holomorphic.

**Equation (2.1):**

    f(Z)=(1/(2pi i)) integral_(2) Z^(s-61/100)
                  exp((s-5/6)^2) H(s)/zeta_F^S(s) ds.

**Equation (11.3):** with Q=Np,

    H_p(s)=(1-Q^(-2))
      * [1-(1-Q^(-1))Q^(-s)-vartheta(p)^6 Q^(2-6s)]
      / [(1-vartheta(p)^6 Q^(3-6s))(1-Q^(-s))].

**Lemma 11.1:** H is holomorphic and nowhere zero on Re(s)>2/3, and H and
its reciprocal are bounded on every closed half-plane inside that region.

**Section 13 / equation (13.3):**

    I_Z=c0 f(Z)+O(Z^(717/2000)),  c0!=0,
    |I_Z| <<_epsilon Z^(287/800+epsilon),
    61/100+287/800=31/32.

Import annotation: nonvanishing of the numerator, identity of the fixed
weights in both evaluations, and all common-prime terms are essential.
The source's transformed mean square is not automatically the original
full 2k-th native moment. See IMPORT.md and the separately proposed proofs.
