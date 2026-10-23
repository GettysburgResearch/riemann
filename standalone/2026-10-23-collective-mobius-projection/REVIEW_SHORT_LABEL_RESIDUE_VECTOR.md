# Independent review of the short squarefree-label residue vector

23 October 2026. Reviewed file: `../two-hour-boundary-20261023/SHORT_LABEL_RESIDUE_VECTOR.md`, SHA256 `a003b982e012b3659329bc325b3b7d1f3db8aa7cd85f81b8120876e3c18c329f`.

Verdict: V2 and V3 follow from the explicitly stated scalar and functional-equation inputs and the sixth-power-free large sieve. No additional defect was found. The local coefficients, vector aggregation, completion tails, primitive-density transfer, and stated projection-only scope were checked independently.

The primary large sieve was checked directly in de Faveri, arXiv:2610.04045v1, Theorem 1.1 and definition (1.2). It permits arbitrary column coefficients and sixth-power-free indices on both sides. A squarefree row subset and fixed ray-sector restrictions are legitimate positive restrictions, after the fixed reciprocity-sector decomposition.

## The arithmetic aggregation

For squarefree n and R, the only nontrivial local modulus exponents are exactly 2 on primes of n alone or R alone, and 3 on primes common to both. This gives R=f g R0, n=e g m, and c=e^2 f^2 g^3 c0. The residual m and R0 may share primes absent from c. The proof correctly does not impose an extra coprimality condition between them.

Scaling the local additive character by m and R0 separately gives the two character factors in V7. CRT roots depend on the frozen factors and c0, rather than on either free variable. The remaining normalization is e^-1 f^-1/2 g^-1 c0^-1/2. The unique sixth-power-free encoding r=e^2 c0 absorbs the e factor and produces squared coefficient weight f^-1 g^-2/L=fg/U.

The zero mask in the inverse row r f^2 g^3 enforces coprimality of m with efg. Thus aggregating e does not introduce a row-varying puncture into the actual-coefficient inverse theorem. The outer character similarly enforces (R0,e c0)=1. Norm-coordinate separation produces one common free Möbius polynomial for each e dyad, with the e-dependent smooth multiplier retained in the arbitrary large-sieve coefficient. This justifies the order of the two estimates in V9.

The four factors after expansion are exactly those in V10. Summing f,g with fg<=K gives 1, K^2/U, (K^2/U)^(2/3), and (K^2/U)^(1/6), up to subpowers. Cauchy over f,g costs only a divisor bound for each fixed original label R. This proves the claimed finite-vector improvement V4.

## Completion and primitive residue

All completion ideals are included. In the nonvolume term, the three ranges separated by (Y/K^2)^(1/6) and (Y/K)^(1/6) have square-root weights b^-3/2, b^3/2, and b^-3/2 respectively. Their endpoint sums yield D^(5/12)Y^(1/12) and D^(5/12)K^(7/12). The volume term yields sqrt(Y)+K. These are exactly V13. Empty ranges and Y<K cause no worse term.

Summing the reflected scalar estimate at Y=D gives K^2+D^(5/6)K^(7/6), with no unjustified vector bound inside the reflected small-argument kernel. The exact finite-minus-pole identity therefore gives V2. The third term is the binding condition K<=D^(1/7) for a D^(2/3) residue vector.

For primitive density, (d,R)=1 ensures the new label dR remains squarefree. The three square-root weights after applying V2 are d^-11/6, d^-1/3 with cutoff sqrt(D), and d^-7/6. Squaring yields the three terms stated after V15. The scalar tail d>sqrt(D) yields D^-1/6 K and D^-1/6 K^(4/3), which are harmless in the claimed short-label range. Row-dependent residue-density factors are bounded by one and are removed only from a positive norm.

The final consumer requires the separately supplied Gram conditioning theorem and controls only the pole part of the specified projection. It does not estimate a primitive continuous vector, the orthogonal complement, or the signed return of the initial Poisson formula. No smaller fixed zero-free boundary or RH assertion is certified here.
