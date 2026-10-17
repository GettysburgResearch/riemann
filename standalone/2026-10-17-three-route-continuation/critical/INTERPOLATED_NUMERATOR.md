# Intermediate-line numerator means for the actual sextic family

Status: proposed analytic component with a complete written proof. This does not prove an estimate for a reciprocal L-function, a bound for the original signed theta sum, or RH. Its application to a new zero-free region requires the separate full contour comparison.

Scope: a fixed number field and a fixed finite set of local choices. Constants may depend on the field, the fixed local data, the ordinate being interpolated, and the arbitrarily small exponent loss. No uniformity in the field or a growing angular character is asserted.

Exact dependencies:

- The actual-family central numerator mean in PR #965, head `d58e3282a9379b6ae165681bc2e21e4f9fd18c26`, `standalone/2026-10-17-subcritical-dedekind/PROOF.md`, Section 3.2, equation (25). That input in turn invokes the choice-compatible sextic-family adapter and the complete BGL approximate-functional-equation argument; this component does not independently reprove those imported analytic estimates.
- The usual primitive functional equation for the same finite-order Hecke characters. Conductor, omitted Euler factors, and complex conjugation are treated explicitly below.
- The scalar three-lines theorem, finite-dimensional duality, and Hölder's inequality. The needed vector interpolation statement is proved here rather than invoked as an additional family theorem.

The proposed improvement over the endpoint-only use in #965 is the exponent `nu(1-y)+1/2` for the sum of numerator absolute values on a zero-selected subset at `0<y<1/2`. The zero-selected set need not be independent of the numerator.

## 1. A finite-family theorem

Fix a number field F. For each U>=2, let J_U be a finite set. Write L_j(s) for a nonprincipal finite-order Hecke L-function with any literal imprimitive omissions retained. Assume the following hypotheses.

1. Each L_j is holomorphic on Re(s)>=1/2 and has at most polynomial vertical growth on each fixed closed strip used below. For a fixed U, uniformity in j is automatic from finiteness; the endpoint estimates below have the displayed uniformity in U.
2. For every eta>0, there are C_eta,A_eta independent of U and t such that

       sum_(j in J_U) |L_j(1/2+it)|^2
          <= C_eta U^(1+eta) (1+|t|)^A_eta.                 (1)

3. For every delta>0,

       sup_(j in J_U, t real) |L_j(1+delta+it)| <= B_delta, (2)

   independently of U. For the actual family, its Euler product and |chi_j(a)|<=1 give B_delta<=zeta_F(1+delta).

**Theorem 1.** For every fixed 1/2<sigma<1, every epsilon>0, and p=1/(1-sigma),

    sum_(j in J_U) |L_j(sigma+it)|^p
       <<_(sigma,epsilon) U^(1+epsilon) (1+|t|)^A.          (3)

The exponent A is finite and may depend on the fixed parameters. If E_U is ANY subset of J_U with #E_U<<U^nu, 0<=nu<=1, then

    sum_(j in E_U) |L_j(sigma+it)|
       << U^(nu sigma+1-sigma+epsilon) (1+|t|)^B.           (4)

At sigma=1/2 the same formula follows directly from (1) and Cauchy--Schwarz. Sets E_U may be defined by the zeros of L_j, by zeros of the conjugate functions, or by other dependent information. No conditional expectation or probabilistic independence enters the proof.

### 1.1 Exact interpolation with a right line beyond one

Fix delta>0 and sigma in (1/2,1+delta). Put

    h=1/2+delta,
    theta=(sigma-1/2)/h,
    p_delta=2/(1-theta)=(1+2delta)/(1+delta-sigma),
    p_delta'=2/(1+theta).

We first prove the exact finite-vector estimate

    || (L_j(sigma+it))_j ||_(ell^p_delta)
       << U^((1+eta)/p_delta) (1+|t|)^A.                   (5)

Here eta can be any positive loss in (1). Fix t=t0. For a dual vector c with sum_j |c_j|^(p_delta')=1, write c_j=e^(i phi_j)|c_j|. A zero coordinate will remain identically zero. For the other coordinates define the analytic functions on 0<=Re(v)<=1

    b_j(v)=e^(i phi_j) |c_j|^(p_delta'(1+v)/2).

Then b_j(theta)=c_j. On the left boundary, ||b(iv)||_2=1; on the right boundary, ||b(1+iv)||_1=1. These equalities use only the real part of the exponent and hold for every real v.

Choose any fixed kappa>0, and consider

    f(v)=exp(kappa(v-theta)^2)
         sum_j L_j(1/2+h v+i t0) b_j(v).                    (6)

On Re(v)=0, Cauchy--Schwarz and (1) bound |f| by

    C U^((1+eta)/2) exp(kappa theta^2-kappa(Im v)^2)
         (1+|t0+h Im v|)^(A_eta/2)
    <= C' U^((1+eta)/2) (1+|t0|)^(A_eta/2).                (7)

On Re(v)=1, (2) and the ell^1 identity bound |f| by

    B_delta exp(kappa(1-theta)^2-kappa(Im v)^2)
    <= B_delta exp(kappa(1-theta)^2).                       (8)

The Gaussian makes f bounded on the closed strip: for a fixed U there are only finitely many coordinates, their vertical growth is polynomial, and the factors b_j have no growth in Im(v) in modulus. Thus the ordinary bounded-strip three-lines theorem applies without any unproved control of horizontal boundary segments. Evaluating at v=theta, where the Gaussian is exactly one, gives

    |sum_j L_j(sigma+i t0)c_j|
       <= C'' U^((1+eta)(1-theta)/2)
          (1+|t0|)^(A_eta(1-theta)/2).                     (9)

Taking the supremum over the unit dual sphere proves (5). The phase of the optimizing dual vector is unrestricted, so this gives the complex ell^p norm as well as the real one.

### 1.2 Passing to the stated exponent

Let p=1/(1-sigma). For 1/2<sigma<1 and delta>0, p_delta<p, and

    1/p_delta -(1-sigma)
       = delta(2sigma-1)/(1+2delta).                       (10)

Counting-measure sequence norms satisfy ||v||_p<=||v||_(p_delta). Combining this with (5), choosing delta sufficiently small in terms of sigma and the desired epsilon, and then choosing eta sufficiently small, gives

    || (L_j(sigma+it))_j ||_p
       << U^((1+epsilon)/p) (1+|t|)^A.

Raising to the p-th power proves (3). This limiting argument is only a choice of fixed parameters; delta is chosen before U tends to infinity. No estimate at the line Re(s)=1 is assumed.

Hölder applied to the arbitrary subset E_U now gives

    sum_E |L_j(sigma+it)|
       <= (#E)^(1-1/p) (sum_J |L_j(sigma+it)|^p)^(1/p).

Since 1-1/p=sigma, this is (4), after renaming the freely chosen small loss. The case nu=0 is included. No estimate for the reciprocal of L_j is used.

## 2. Reflection to the left of the central line

Assume in addition that L_j is induced from a primitive finite-order Hecke character chi_j^* with conductor ideal f_j, and that

    |D_F| N f_j <= C U.                                    (11)

The primitive archimedean types belong to a fixed finite set. Write the original, possibly imprimitive function exactly as

    L_j(s)=L(s,chi_j^*) R_j(s),
    R_j(s)=product_(p in T_j) (1-chi_j^*(p) (N p)^(-s)),     (12)

where T_j records every Euler factor omitted in the original function beyond the primitive conductor. Include the fixed S omissions in T_j; a prime where chi_j^*(p)=0 contributes the factor one. Assume

    product_(p in T_j) N p <= C' U.                        (13)

A fixed constant times any fixed power of U would also suffice in (13), with the arbitrarily small loss renamed. Let bar L_j denote the function with the conjugate character and the SAME omitted primes. Thus the original nonunit zeros are not changed.

**Theorem 2.** Under these hypotheses, for every fixed 0<y<=1/2, every epsilon>0, and every subset E_U with #E_U<<U^nu,

    sum_(j in E_U) |L_j(y+it)|
       << U^(1/2+nu(1-y)+epsilon) (1+|t|)^B.               (14)

This is a numerator estimate. It holds for a subset selected through denominator zeros because Hölder's inequality makes no independence assumption.

### 2.1 The exact role of the primitive functional equation

At fixed 0<y<1/2, the primitive functional equation and Stirling's estimate give

    |L(y+it,chi_j^*)|
       <= C (|D_F| N f_j)^(1/2-y) (1+|t|)^B0
          |L(1-y-it,bar chi_j^*)|.                         (15)

The finitely many archimedean types make C and B0 uniform in j. No gamma pole is met: both y and 1-y are positive. The complex root number has modulus one. The bound for the bounded range of t follows by continuity of the gamma quotient and its nonzero finite denominator; for large |t|, Stirling gives a fixed polynomial. Equation (11) then bounds the conductor factor by C U^(1/2-y).

Multiplying by R_j(y+it), and expressing the right side again in terms of the original conjugate function, gives the exact additional factor

    |R_j(y+it)| / |bar R_j(1-y-it)|
       <= product_(p in T_j)
           [1+(N p)^(-y)]/[1-(N p)^(-(1-y))].              (16)

The denominator factors in (16) are strictly positive; they are Euler factors at positive real part, not unverified zero-free assertions about an L-function.

For every eta>0 and fixed y>0, the right side of (16) is O_(F,y,eta)(U^eta). Here is a direct uniform proof. For sufficiently large Q,

    log((1+Q^(-y))/(1-Q^(-(1-y)))) <= eta log Q.

Choose this cutoff before U. There are only finitely many prime ideals of F below it, and their product contributes a fixed constant, since every prime occurs in T_j at most once. The remaining product is at most (product_(p in T_j) N p)^eta, which is O(U^eta) by (13). This proves

    |L_j(y+it)|
       << U^(1/2-y+eta) (1+|t|)^B0
          |bar L_j(1-y-it)|.                               (17)

In particular, discarding all imprimitive factors before applying the functional equation would not have been an exact identity; (16) is the required controlled adapter.

### 2.2 Applying the mean to the conjugate family

The conjugate family obeys precisely the same endpoint hypotheses. In fact,

    |bar L_j(1/2+it)|=|L_j(1/2-it)|,

so (1) holds after t is replaced by -t, without requiring the conjugate characters to be reindexed inside J_U. The Euler bound (2) is unchanged. Therefore Theorem 1 at sigma=1-y gives, for the same subset of indices,

    sum_(j in E_U) |bar L_j(1-y-it)|
       << U^(nu(1-y)+y+eta) (1+|t|)^B1.                   (18)

Combine (17) and (18). The y terms cancel exactly, leaving 1/2+nu(1-y), which proves (14). At y=1/2 the original central Cauchy bound already has this exponent, so no limiting functional-equation argument is needed.

For comparison, ordinary individual convexity followed by summing the subset gives the exponent nu+(1-y)/2. Subtracting (14)'s exponent gives

    y(nu-1/2).                                           (19)

Thus (14) is strictly stronger when 0<y<1/2 and nu>1/2. When nu<1/2, individual convexity remains the smaller bound; one may use the minimum of the two estimates. Neither estimate requires any independence between the subset and the numerator.

## 3. Application to CT's literal Poisson rows

The intended family is the nonprincipal part of the CT Poisson family already identified in #965, Section 3.2. Its indices are the SIXTH-POWER-FREE exterior ideals u with U<=N u<2U, together with a fixed finite list of S-unit classes. The ordering is by FULL NORM, not conductor norm or radical norm. The unique principal row is handled separately by CT's residue calculation; a principal L-function, with its pole at s=1, is not placed inside the analytic strip argument.

The fixed-twist adapter of #965 gives the central estimate (1) for the actual characters chi_u, including their original zero values at shared primes. The finite number of S-unit classes only changes the constant. Each primitive conductor outside S is supported on the primes dividing u and is bounded there by the fixed-order tame conductor; all primes over six are already in the fixed S. The conductor at S is bounded within the fixed local choices. Consequently N f_u<<N u<<U, as required in (11). The additional omissions are contained in S together with the primes dividing u, giving (13). The archimedean types are finite-order types in a fixed finite list. The angular theta character appearing elsewhere in CT is not treated as such a finite-order twist.

If E_U is one of #965's fixed exceptional sets or differences of nested exceptional sets, with cardinality O(U^(g(sigma_j)+e)), first take the reciprocal and correction bounds exactly as in that source. Theorem 2 can then bound the remaining numerator sum at any fixed 0<y<1/2 by

    U^(1/2+g(sigma_j)(1-y)+O(e)+epsilon) times a height power. (20)

This bound remains valid for the zero-selected set. It does not move the denominator contour across a zero, assert a mean bound for reciprocals, change the set after choosing the later reciprocal loss, or alter the original nonunit extensions.

For the normalization of #965, Section 4, with physical scale X=Y=Z^a, h=1-a, and a central dyad weight U^(-z0), replace its convexity-based numerator exponent by

    R=1/2+nu(1-y)-z0.                                    (21)

The physical monomial remains exactly

    E(x,y,z0)=a/2+x-1+h z0+a(y-1).

At the usual split U=Z^h, the combined exponent simplifies to

    E+hR=x-1/2+[h nu-a](1-y).                             (22)

All correction-domain constraints and all other ranges of the contour comparison still have to be verified. Equation (22) is an algebraic consequence of the new numerator estimate, not a standalone zero-free theorem.

## 4. Scope, review obligations, and checks

What is proved here from its stated hypotheses:

- finite-vector intermediate-line means with the required U exponent;
- arbitrary-subset estimates, retaining dependent zero selection;
- reflection with the actual conductor and all imprimitive Euler factors;
- the resulting strictly better exponent when nu>1/2;
- the replacement monomial for an independently checked contour comparison.

What remains imported or unproved here:

- the actual central family mean and its choice-compatible arithmetic identification;
- the zero-density theorem and the zero-free-rectangle reciprocal estimate;
- the full CT/OpenAI Poisson identity and its analytic correction domain;
- a new global contour comparison, any claimed improved zero-free region, and every endpoint/RH assertion.

This component uses no numerical theorem proof. Its finite rational checker verifies the displayed exponent identities and tests the strict-improvement regime; it does not authenticate the imported analytic hypotheses. Independent mathematical review must check those hypotheses at the exact frozen source head before approving a composed conclusion.
