# Independent review: native denominator poles of the canonical cusp quotient

Verdict: PASS for scientific source
2f636755ef8605eff725562094017f501fb1db70.
The actual-source analytic theorem is accepted as a reviewed written proof,
not a machine-certified theorem or a numerical period/zero calculation.

Review date: 2026-08-31.
Authoring parent: 1653565cc80cde6fa882ae9e150626187d3071d0.
Resident scientific import: 932f02132a765f33f6d56c35ee3e676b8fa13731.
The five scientific files and all LS/AW/EP/UQ/CZ/CF parents remain frozen.
This separate audit supplies acceptance without rewriting proposed status
or the scientific fixture's seals.

Root contributed the nested-flag and surviving-coupling strategy before
freeze. Root's additional replay is therefore not the sole independence
claim. A designated non-author reviewer independently read the analytic
proof and reconstructed the arithmetic on the exact frozen source, without
author contact or source edits. Both reviews passed.

## 1. Accepted theorem and quantifiers

For every FIXED 0<delta<12, all sufficiently large even weights k have
exactly one pole, counting multiplicity, in each disc

    |s-(1-24/k)|<delta/k,    |s-24/k|<delta/k.

These are genuine additional poles of the literal first-q-coefficient
quotient Q_k. They are simple, real and reflected, and cannot cancel with
the full numerator determinant. If s_p=1-c_p/k is the right pole, then

    c_p -> 24,
    Res_(s=s_p) Q_k(s) = 1152 A_2(k)/k^2 (1+o(1)) > 0,
    A_N(k)=Gamma(k-1)/(4pi N)^(k-1).

The reflected residue is negative. Every assertion is eventual across
all six native even-weight classes. The sufficient threshold depends on
delta and is NOT calculated. Neither 65536 nor 6144 is inherited as a pole
threshold. This does not count all poles at any fixed weight, exclude
numerator zeros elsewhere in these discs, or give unsigned global divisor
asymptotics.

## 2. Load-bearing analytic review

1. The actual nested flags are W2=ker[q] and W3=ker[q] intersect ker[q^2].
   With k=12d+r and the native E4/E6 chart,

       g1=Delta E4^p E6^b,  g2=Delta^2 E4^(p-3) E6^b,
       t_k=[q^2]g1=60k-744-864b,  h=g1-t_k g2.

   The shear has determinant one and preserves [q], W2 and the quotient.
   It gives h=q+O(q^3) and g2=q^2+O(q^3), with no free coefficient model.

2. On the entire complex q-disc R_k=1/(1000k), native product/series
   bounds give |g_j/q^j|<2. Cauchy's estimates then give, throughout the
   high cusp for all sufficiently large k,

       |h-q|<=4400000 k^2 rho^3,
       |g2-q^2|<=4000 k rho^3.

   These are full convergent-tail estimates, not finite-prefix extrapolation.

3. The cutoff Y=k/10000 resolves the exponentially small coupling scale.
   Global source bounds and the factorial lower estimate give

       M(h;Y)+M(g2;Y)<=100000 k^4 10^-k A_3(k).

   The exact factorial ratio was checked separately:

       1056000 pi eta k^3/(k-1)
           [24pi e eta k/(k-2)]^(k-2)
       <=84480 k^2 10^-k,    eta=1/10000.

   Thus the omitted compact/low-cusp mass is controlled relative to A3,
   not merely relative to the much larger first-direction norm.

4. For c=k(1-s), each fixed closed disc |c-24|<=R<12 lies in the
   W3 coercivity chamber:

       Re(1/(2c))-1/72
         =[324-|c-18|^2]/[72|c|^2]
         >=[324-(6+R)^2]/[72(24+R)^2]>0.

   The imported Parseval moment estimate applies to EVERY f in W3,
   with first Fourier order at least three and the original Petersson norm.
   LS's complex-power perturbation and complex-order Bessel modulus
   bound make the Gram-whitened Hermitian PART uniformly negative,
   of order k. Its minimum singular value, not its eigenvalues alone,
   controls the whole inverse by O_R(1/k).

5. The genuine second flag quotient d_k=det(I_W2)/det(I_W3) is eventually
   holomorphic on that SAME fixed disc. The full absolute form bound gives
   |d_k|<=C_R kG(g2), independent of growing dimension. Real-axis estimates
   from the full source, including its paid self-Schur correction, give

       d_k(c)/(kG(g2)) -> F2(c)=1/48-1/(2c).

   Normal families and the identity theorem promote this real limit to
   locally uniform complex convergence. Cauchy gives derivative convergence;
   Rouche counts one zero with multiplicity. Conjugation gives reality,
   and the zero is simple. Here F2'(24)=1/1152.

6. A denominator zero is not yet a quotient pole. The q-to-q^2 cross-period
   receives its first nonconstant Eisenstein mode with exact coefficient

       4 (native cosine) * 1/2 (x integral)
         * 1/2 (half-order Bessel coefficient) = 1.

   Its exponential weight is exp(-8pi y), so its leading integral is A2.
   The DLMF Gamma-integral substitution gives, for 0<=nu<=1/2,

       1-(1/4-nu^2)/(2x) <= K_nu(x)/K_(1/2)(x) <=1.

   Convexity proves the lower bound, uniformly at x>=2pi Y. Consequently
   B0/A2=1+O(1/k)>0. No special-function samples or hidden factor two enter.

7. Constant-term Fourier orthogonality removes the principal and both
   single-tail cross terms. The remaining full tail costs polynomial
   multiples of A3, A_(5/2) and A_(7/2), all exponentially smaller than A2.
   The entire low-domain cross term is paid by the preceding mass estimate.

8. The actual ALL-W3 dual norms, not a truncated 2x2 panel, satisfy

       ||I(h,.)||<=C[k^4 sqrt(A3)+sqrt(A2)],
       ||I(g2,.)||<=C k^3 sqrt(A3).

   Combining them with the O(1/k) inverse bounds the effective cross
   correction by C[k^6 A3+k^2 sqrt(A2 A3)]=o(A2).
   Therefore b_eff/A2=1+O(1/k)>0. This is the new noncancellation payment.
   A superpolynomial error in the larger sqrt(G(h)G(g2)) normalization
   would not have sufficed.

9. Source reality is proved using x -> -x on the fundamental domain and
   real q coefficients. On the real interval the remaining matrix is
   real symmetric. Analytic continuation keeps row/column entries
   separate; it does not substitute a complex adjoint into a holomorphic
   formula. At the simple d_k zero, the full numerator is
   -det(I_W3)b_eff^2, which is nonzero.

10. The c-residue is -b_eff^2/d_k'(c_p). Since dc/ds=-k, the s-residue is
    positive b_eff^2/[k d_k'(c_p)]. Together with G(g2)/A2 ->1 and the
    Cauchy derivative limit this gives 1152 A2/k^2. Reflection reverses
    the residue sign.

Primary analytic normalization was checked directly against
[DLMF 10.32.8](https://dlmf.nist.gov/10.32.E8) and
[DLMF 10.39.2](https://dlmf.nist.gov/10.39.E2). Their hypotheses are met;
the normal-family tools are those already reviewed in LS.
Remote references are not bytes authenticated by offline Git replay.
No novelty is claimed for Bessel integrals, Schur complements or Rouche.

## 3. Independent finite verification

Root read all five files completely, including the full fixture and source
manifest. The 32 NP tests passed normally (7.256 seconds) and under -O
(8.185 seconds); both checks, Ruff check/format, full base-to-source
whitespace and control-character checks passed.

Root's separate transient exact reconstruction passed in EACH mode:

- Direct finite Euler products for Delta^j and binomial powers of E4-1
  rebuilt 12 native pairs and 24 additional pairs across all six classes.
  Their g1,g2,h prefixes contain 972 exact coefficient checks.
- Eight rational radii and 64 rationally parametrized circle points
  checked the deeper coercivity margin and Rouche reserve.
- Fifteen additional rational Bessel tangent reserves and four exact
  factorial envelopes checked the explicit inequalities.
- Symbolic algebra verified the entire-block Schur identity with distinct
  non-adjoint complex cross directions, the second-scale derivative,
  denominator-cancellation countercontrol and s-coordinate residue sign.
- Thirty-one independently resealed reports were rejected by ACTUAL fresh
  complete reconstruction, without a build_report mock or cache.
- Fifteen literal frozen source bindings, four artifact seals, all five
  scientific blobs, fixture/payload identities and four exact LF emissions
  per replay matched.

The non-author review separately passed all 96 NP+LS+AW tests in both
modes, NP's two checks and four LF emissions, Ruff and the full-base diff.
Its independent Euler-binomial route reconstructed 100 g1/g2 prefixes and
1350 g1/g2/h coefficients, using 94590 exact products; it also checked
224 rational disc identities and six factorial envelopes.
It rejected 24 fully resealed mutations through ACTUAL fresh reconstruction
and 65 further source/type/domain/JSON attacks in EACH mode.
It independently verified the Gamma-integral prefactor and residue algebra.

These are bounded arithmetic controls. They do not machine-prove an
integral estimate, an all-weight limit, or a sufficient pole threshold.

## 4. Frozen identities and remaining boundary

Git blobs:

- Proof: 993a830e2b9b3a7ff266de5bb770e1ffc5735315.
- Producer: bd065125ae110ce9d875998e79ded8a1268fc50f.
- Fixture: e01e1126f63a463a3274b70401af8d3137460f8e.
- Sources: 9c863a41a744e7966765b6e61e71458c77f9d5ac.
- Tests: 7efee0631a8099bcd1943bf459e4915062e20ee1.

Fixture LF SHA-256:
a63794971ac6d940f80009a3687eb22b619b539407df2f9e36f60c40fee7b7b1

Payload SHA-256:
df71eeebf73602d13af59896ff129f516538b3ea0069df9023957e7284134f0b

Independent frozen-source review is satisfied. No scientific repair was
needed. This establishes a genuine eventual additional pole pair, not a
fixed-weight global pole census, a uniform higher-flag ladder, an unsigned
zero asymptotic, an effective onset, RH failure or a new automorphic family.
