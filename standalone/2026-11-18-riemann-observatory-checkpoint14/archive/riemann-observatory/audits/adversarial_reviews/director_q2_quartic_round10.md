# The fixed Q2 quartic and sharp tail: director adjudication

18 November 2026. The director read the full proposed calculation and the independent reconstruction, including the replacement sharp continuous-moment proof. Exact symbolic replay passed. The coefficients and the RH-conditional power-saving error are accepted as scoped reconstructions. Their constants have not been numerically allocated, so the quartic splice is not a rigorous infinite-tail enclosure.

Put Q2(s)=2*2^(-s)-1, q=log2 and zeta(1+z)=1/z+sum_(j>=0)c_j z^j, with c_j=(-1)^j gamma_j/j!. Let L=log(t/(2pi)). The exact density is D2=D1+Delta, where

```text
D1 = L^4/12 + (2c0/3)L^3 + (c0^2+2c1)L^2
   + (-2c0^3+10c0c1-2c2)L
   + 2c0^4-12c0^2c1+16c0c2+14c1^2-20c3;
Delta = (2q/3)L^3+(4c0q+q^2)L^2
      + (4c0^2q+4c0q^2+8c1q-16q^3/3)L
      -4c0^3q+2c0^2q^2+20c0c1q-32c0q^3/3
      +4c1q^2-4c2q+49q^4/6.
```

Write P_minus=sum_(j=0)^4 (-1)^j D2^(j) and P_plus=sum_(j=0)^4 D2^(j). The unconditional reflected mixed prefix sum zeta'(rho)zeta'(1-rho)Q2(rho)Q2(1-rho) is T P_minus(log(T/2pi))/(2pi)+O_A(T log^(-A)T). Under RH it is nonnegative, and the argument also gives O_epsilon(T^(7/8+epsilon)). The strict two-sign nonnegative tail is therefore P_plus(log(Y/2pi))/(pi Y)+O_epsilon(Y^(-9/8+epsilon)). The ordinary kernel change from 1/(t^2+1/4) to 1/t^2 costs only O(log^4Y/Y^3).

## Arithmetic and analytic checks

The reduced coefficient pairs are (1,1),(2,1),(1,2) with weights 3,-1,-1. In HLZ's primitive-character error the support factor a(kq') leaves only conductor 2, which has no primitive character. Thus the entire nonprincipal error vanishes, not merely its exceptional part. This is special to this support; it is not a general removal of Siegel ineffectivity.

Both derivations obtain the local factor 3-V-(U+W-1-UWV/2)/(1-V/2), with U=2^(-u), V=2^(-v), W=2^(-w). A direct parity Perron kernel independently matches all three residues. The auxiliary derivative has its minus sign from 1/zeta(1-g)=-g+O(g^2). The transposed term includes the source's conjugation of both complex shifts. Hyperplane pole cancellations are checked before intersecting them. Different Laurent rays in the two implementations give the same mixed coefficient and all six density/prefix/tail polynomials. The untwisted coefficients match Milinovich's proved thesis coefficients, not an inconsistent adjacent conjectural transcription.

For the sharper error, the smooth Pratt–Robles theorem alone does not license a sharp endpoint. Both reviewers instead use its primary product approximate functional equation with fixed h,k in {1,2}. A Gaussian Mellin weight annihilates the shifted zeta pole. On a dyadic interval X, one sharp integration by parts and integer gaps give an off-diagonal O(sqrt(X) log^C T). Moving the diagonal Mellin line to -1/4 gives O(X^(3/4) log^C T) after integration. Nested shift circles keep their sum away from zero during Cauchy differentiation; the resulting combined analytic expression extends to coincident shifts. No shrinking smoothing interval is assumed.

Differentiate the principal Perron integrand before moving its line to 3/4. Under RH the zeta logarithmic derivative is O(log(|Im s|+2)) on the relevant separated edges. Elementary Euler bounds for the two zeta factors, Perron height U=T^(1/4), and truncation window T/sqrt(U) produce O_epsilon(T^(7/8+epsilon)). The support length T^(1/8), stationary-phase and bounded endpoint adjustments are smaller or of that order. The error is uniform on the specified fixed Cauchy circles. Stieltjes integration uses inclusive A(Y) for the strict tail and is valid for small positive epsilon; larger stated epsilons follow by weakening the bound.

## Computation and next step

The director replayed the exact symbolic script and the finite certificate at 192 bits through 1000. A separate 160-bit run exhausts all 10142 positive zeros below 10000, proves each simple, and records outward partial-sum intervals. The quartic splice values are approximately 0.6522176262, 0.6534648947, 0.6534615142 and 0.6533938577 at heights 100,400,1000,10000. A deliberately incorrect three-times-untwisted tail changes far more. This supports an arithmetic consistency check; the unknown error constant prevents any claim that 0.65339 encloses the limit.

To turn this into a practical certificate, allocate explicit gamma/Stirling, product-AFE, stationary-phase, Perron, Cauchy-radius and endpoint constants. The unconditional Hardy bounds are a different, presently much looser certificate and must stay separate.

[Full proof and source pointers](prime64_q2_full_polynomial.md) · [Independent reconstruction](positivity64_q2_polynomial_skeptic.md) · [Sharp J proof](prime64_q2_sharp_j.md) · [Finite certificates](prime64_q2_partial_tail_observation.md) · [Director replay](../../experiments/results/director64_round10b_checks.json)
