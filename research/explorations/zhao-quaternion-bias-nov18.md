# A field outside the spectral census with an eventual positive mean on GRH

Let \(K=\mathbb Q(\alpha)\), where
\[
 \alpha^8+12\alpha^6+36\alpha^4+36\alpha^2+9=0 .
\]
Unconditionally its completed Dedekind zeta function has **a central zero of order exactly two**, no other nontrivial real zero, and
\[
 12.7594<B_K^*=2\Xi'_K(1)/\Xi_K(1)<12.7596 .
\]
Assume GRH for this field. The [integrated prime-ideal harmonic Mertens error](zhao-field-sign-equivalence-nov18.md) then satisfies
\[
 \liminf_{X\to\infty}\frac{\log X}{\sqrt X}J_K(X)
 \ge 18-B_K^*>5.2404.
\]
Thus the strict \(B_K<2\) census omits an actual eventually positive field on GRH. Linear independence of zero ordinates is unnecessary. Further, the eventual positivity of this particular \(J_K\) is equivalent to the individual Riemann hypothesis for \(\zeta_K\). [Reproducible interval certificate](../../scripts/check_zhao_quaternion_bias_nov18.py) · [Field record](https://www.lmfdb.org/NumberField/8.0.12230590464.1) · [Source question](https://doi.org/10.1007/s40993-025-00640-y)

## Root number and logarithmic derivative

PARI's exact Galois identification gives the quaternion group \(Q_8\) (small group \([8,4]\)) for this degree-eight totally complex field. The fixed field \(F\) of its center is the unique quartic subfield. The three quadratic subfields have discriminants \(8,12,24\). The absolute discriminants of \(K,F\) are \(12230590464,2304\) respectively. The quaternion regular representation gives
\[
 \zeta_K=\zeta_F L(s,V)^2
\]
where \(V\) is the faithful irreducible plane representation, induced from a nontrivial character of a cyclic order-four subgroup. Its completed Hecke L-function \(\Lambda(s)\) is entire. Complex conjugation is the central involution and has both eigenvalues \(-1\) on \(V\), so its archimedean gamma factors are both odd. The conductor-discriminant formula gives the Artin conductor \(q=2304\). The representation is self-dual, so its functional equation has sign \(\epsilon\in\{1,-1\}\).

Put \(c=2\pi/\sqrt q=2\pi/48\), \(L(s,V)=\sum a_n n^{-s}\) and
\[
 \theta(t)=\sum_{n\ge1} a_n (cnt)K_0(cnt).
\]
Mellin inversion of \(x K_0(x)\) gives \(\Lambda(s)\) up to a positive constant independent of \(s\), since \(\int_0^\infty x^{s}K_0(x)dx=2^{s-1}\Gamma((s+1)/2)^2\). Consequently \(\theta(1/t)=\epsilon t\theta(t)\) on the right half-plane. To evaluate \(a_n\), divide the exact ideal-count Dirichlet series of \(K\) by that of \(F\), and take its unique Dirichlet square root with coefficient one at 1. At a prime power the local coefficients have modulus at most the coefficient of \((1-T)^{-2}\), giving \(|a_n|\le d(n)\le n\).

The checker uses 2,048 exact coefficients. For \(t=1/2,2\) it encloses both theta values; the omitted terms above index \(N\) cost at most \(2\sum_{n>N}n\exp(-cnt/2)\), summed as a geometric derivative. This follows from \(K_0(x)\le\sqrt{\pi/(2x)}e^{-x}\) for \(x>0\). The resulting bounds give \(\theta(1/2)<-0.7462\) and \(\theta(2)>0.3731\), forcing \(\epsilon=-1\). Thus \(\Lambda(1/2)=0\), contributing at least two to the Dedekind central multiplicity.

The logarithmic derivative \(\Lambda'(1)/\Lambda(1)\) is the ratio of the integrals of \(u e^u\theta(e^u)\) and \(e^u\theta(e^u)\) on the real line. Pair the positive and negative samples in the [cubic trapezoid proof](zhao-cubic-fields-nov18.md). For sign minus, the paired weights become \(u(e^u+1)\) and \(e^u-1\), and \(\theta(1)=0\). The strip and truncation bounds from that proof hold with the same absolute radius \(10^{-12}\) on each integral. In detail, throughout \(|\arg z|\le1/2\), the integral bound for \(K_0\) gives \(|zK_0(z)|\le2e^{-\Re z/2}\); on the positive side of either contour line \(\Re(cne^u)/2>ne^{\Re u}/80\). In the real mesh omit only \(z>256\), extracting \(e^{-64}\) and bounding the remainder by \(2e^{-z/4}\). Since \(c>1/8\), the remaining decay dominates the one used in the cubic proof. The computation verifies a positive denominator before division. Adding the three quadratic logarithmic derivatives and the rational field gives \(B_F^*\), and the factorization gives \(B_K^*=B_F^*+4\Lambda'(1)/\Lambda(1)\) with the stated bounds.

Every nontrivial zero contributes positively to the real-part formula for \(B_K^*\). A central zero costs four per occurrence. The completed Dedekind functional equation is even around its center, so the multiplicity, already at least two, must be exactly two since \(B_K^*<16\). Any distinct real pair \(\beta,1-\beta\) costs at least eight, also impossible in addition to the known central weight eight. On GRH, the noncentral absolute coefficient mass is \(B_K^*-8\), while the constant term of the mean profile is \(2+8\), yielding the lower bound \(18-B_K^*\). If GRH fails there must instead be a nonreal off-line zero; the [Mellin-Landau argument](zhao-field-sign-equivalence-nov18.md) gives infinitely many excursions of each sign. This proves the individual equivalence.

## Twelve eventual-positive fields beyond the strict bound

The same argument gives twelve explicit quaternion examples, three totally complex and nine totally real, on GRH for the individual fields. The [complete twelve-field checker](../../scripts/check_zhao_quaternion_examples_nov18.py) includes every defining polynomial, verifies the Galois group and signature, identifies the quartic fixed field, and supplies opposite nonzero interval signs for \(\theta(1/2)\) and \(\theta(2)\). For a real field the kernel is \(K_0(cnt)\); for a complex field it is \((cnt)K_0(cnt)\). The omitted exponential arguments exceed 96 and both tails are bounded by \(2\sum_{n>N} n e^{-cnt/2}\). The [finite prime test](zhao-field-prime-test-nov18.md) at \(P=4096\) then gives the following upper bounds rounded upwards. [Interval results](zhao-quaternion-bias-nov18.jsonl)

| Field label | Artin conductor | Upper bound for \(B_K\) on GRH |
|---|---:|---:|
| 8.0.12230590464.1 | 2304 | 12.897 |
| 8.0.1340095640625.1 | 11025 | 16.346 |
| 8.0.7644119040000.1 | 57600 | 17.359 |
| 8.8.29365647704064.1 | 112896 | 15.735 |
| 8.8.47775744000000.2 | 57600 | 15.774 |
| 8.8.74220378765625.1 | 42025 | 16.398 |
| 8.8.101240302206976.2 | 73984 | 16.008 |
| 8.8.116507435287321.1 | 48841 | 17.083 |
| 8.8.151939915084881.1 | 53361 | 17.353 |
| 8.8.179068074983424.2 | 278784 | 17.054 |
| 8.8.343064484000000.1 | 176400 | 16.868 |
| 8.8.359729184374784.2 | 112896 | 17.853 |

Each forced central multiplicity is at least two. Consequently the normalized mean has limiting inferior at least \(18-B_K>0\), while the central terms alone give \(B_K\ge8\). Under global Dedekind GRH, the 2,580 fields in the strict census and these twelve distinct additional fields give **at least 2,592 fields with eventually positive integrated prime-ideal harmonic Mertens error**. The unconditional exclusion of other real zeros and the individual equivalence above were proved separately for the first field.
