# An all-order, all-line numerator theorem, with the actual losses

Status: PROPOSED source-qualified mathematical deductions, with complete arguments below.
No independent referee or formal verification. No new zero-free region or RH proof.
The imported input is de Faveri, arXiv:2610.04045v1, Theorem 1.1, freshly read
in primary HTML. This generalizes the specific fourth/eighth moment arguments;
#968 already states the central fixed-order specialization. No global novelty
claim is made for powering an approximate functional equation (AFE).

## 1. Definitions and input

Fix n>=3, a number field F containing mu_n, degree d, and all the admissible
fixed S, generator and ray-class data in DF Section 2. Rows a are n-th-power-free
integral ideals outside S, indexed by their FULL norm Na<=U. Let psi be a fixed
finite-order Hecke character of S-supported conductor. Write L_a=L_F^S(s,psi chi_a).
Characters include their original nonunit zeros. Extra common column exclusions
can be put in the coefficients of the polynomial estimates, but not silently
in the L-function theorem. The L-function constants retain F,S,psi,n.

For arbitrary complex coefficients on n-free columns, DF supplies

  sum_(Na<=U)^flat |sum_(Nc<=V)^flat lambda_c chi_a(c)|^2
    <<_eta (UV)^eta K_n(U,V) sum_c |lambda_c|^2,
  K_n(U,V)=U+V+U^(1-1/n)V^(2/n)+U^(2/n)V^(1-1/n).      (1)

Both indices in (1) are n-free. A fixed psi is a common column phase.
The usual Hecke functional equation and complete AFE are the other analytic
inputs. No reciprocal L-function estimate is assumed.

## 2. The theorem

For every FIXED integer r>=1, fixed 0<sigma<1, and epsilon>0, put
T=2+|t| and C=U T^d. Then

  sum_(Na<=U)^flat |L_a(sigma+it)|^(2r)
   <<_(fixed data,r,sigma,epsilon) (UT)^epsilon [
       U C^(r(1-2sigma)_+)
       + C^(r(1-sigma))
       + U^(1-1/n) C^(r(1/2+1/n-sigma))
       + U^(2/n) C^(r(1-1/(2n)-sigma)) ].             (2)

Constants are not asserted uniform in growing r, n, conductor of psi,
discriminant, or sigma approaching 0 or 1. Negative exponents of C in the
last two terms are intentional; the U term already pays their small-length
endpoints. For bounded t the norm exponent is

 K_(n,r)(sigma)=max{
   1+r(1-2sigma)_+, r(1-sigma),
   1-1/n+r(1/2+1/n-sigma),
   2/n+r(1-1/(2n)-sigma)}.                            (3)

This is an upper-bound exponent, not a matching lower bound for actual L-values.
The theorem concerns NUMERATOR values, not the native inverse-L coefficient sums.

### Proof of the complete-column step

A dyadic ideal polynomial supported on V/2<Nb<=V has coefficients
|c_b|<<_delta (Nb)^(-s0+delta), with any fixed divisor-function loss included.
Write uniquely b=c e^n with c n-free. Do NOT require (c,e)=1. Exactly,

  (psi chi_a)(c e^n)=psi(c)psi(e)^n chi_a(c) 1_((a,e)=1). (4)

For fixed e, its c-coefficient square mass is
O(V^(1-2s0+O(delta))/(Ne)^n), by ideal counting. If V/(Ne)^n<1 the
range is empty. Apply (1), drop the nonnegative row restriction only after
forming its square, and use monotonicity in V. Minkowski in row l2 and
sum_e (Ne)^(-n/2+O(delta))<infinity (n>=3) give

  sum_a |full dyadic polynomial|^2
       << (UV)^O(delta) V^(1-2s0) K_n(U,V).           (5)

This retains every product ideal, conjugate prime, shared factor and row mask.
The coefficient arrays must be common across rows. The proof does not cover
arbitrary coefficients independently selected for each row.

### AFE and the conductor that must not be replaced

First partition the rows by their actual primitive conductor norm Q into
dyads and their finite gamma/S types. We only know Q<<U, not Q~U. The analytic
conductor is comparable to C_Q=Q T^d, with fixed-field constants. Apply the
complete AFE to L(s)^r. Its two pieces have balanced length C_Q^(r/2), up to
arbitrarily small powers and rapidly decreasing dyadic tails. Their coefficients
are d_r(b)(Nb)^(-s) and the conjugate d_r(b)(Nb)^(-(1-s)). The dual scalar has
modulus C_Q^(r(1/2-sigma)) up to a fixed factor on the chosen sigma line.
Thus its SQUARED modulus is C_Q^(r(1-2sigma)).

Mellin inversion on small positive lines separates conductor-dependent weights.
After extracting their analytic-conductor scale, Stirling's formula bounds
fixed derivative/Mellin seminorms by powers of the integration variable, uniformly
in T>=2. A Gaussian auxiliary Mellin factor absorbs those powers and permits
arbitrarily rapid tails. All finite divisor and preliminary-shift costs can be
made smaller than the requested (UT)^epsilon for each fixed r. Imaginary Q
powers are unit row phases. This does not create row-dependent free coefficients.
Both AFE terms and root numbers are kept; use |A+B|^2<=2|A|^2+2|B|^2.
Inducing-principal rows are a fixed finite set (outside S an n-free nonunit
index has nontrivial local conductor); their fixed-function convexity bounds,
including AFE polar terms, are absorbed by the right side of (2).

Suppose first sigma>=1/2. For a kernel monomial U^a V^b in (1), main-piece
(5) is U^a V^(1+b-2sigma). Its maximum on 1<=V<=C_Q^(r/2) occurs at an
endpoint. The lower endpoint is <=U. The upper endpoint is

  U^a C_Q^((r/2)(1+b-2sigma)).                         (6)

The dual V exponent is b+2sigma-1>=0. Multiplying its upper endpoint by
the ACTUAL dual factor C_Q^(r(1-2sigma)) gives exactly (6). If (6)'s conductor
exponent is negative it is <=U; otherwise C_Q<<C can be used in that positive
power. Summing conductor/length dyads, types, Mellin integrals and rapid tails
proves (2) for sigma>=1/2. This proof never substitutes U into a negative Q power.

For sigma<1/2 the functional equation gives

  |L_a(sigma+it)|^(2r)
   << C_Q^(r(1-2sigma)) |L_bar_a(1-sigma-it)|^(2r).

Now the conductor exponent is positive, so it can be bounded by C's power.
Apply the right-half theorem to the conjugate family. The four terms become
precisely (2). Removed S factors are fixed finite Euler products and their
ratios are bounded on each fixed interior line. This proves the theorem. QED.

## 3. Arbitrary selected sets and mixed moments

For E any subset of at most U^nu rows, 0<=nu<=1, and bounded t, Holder gives

  sum_E |L_a(sigma+it)|
       << U^(nu+(K_(n,r)(sigma)-nu)/(2r)+epsilon).      (7)

No independence from denominator-zero selection is required. Uniform reciprocal
and correction bounds must be supplied separately before applying (7) to a ratio.
For positive integers r_j and weights theta_j>=0 with sum theta_j=1, Holder also
bounds products of powers at distinct fixed lines/heights by the corresponding
product of (2). This does not turn numerator moments into negative moments.

## 4. The full order range saturates for EVERY character order n>=3

For every n>=3 and r>=4, both cross terms in (3) are dominated by r(1-sigma):

 [1-1/n+r(1/2+1/n-sigma)]-r(1-sigma)
       =(n-1)/n-r(n-2)/(2n) <= (3-n)/n <=0,
 [2/n+r(1-1/(2n)-sigma)]-r(1-sigma)=(4-r)/(2n)<=0.

Consequently the complete fixed-order hierarchy simplifies to

 K_(n,r)(sigma)=max(1+r(1-2sigma)_+, r(1-sigma)), r>=4. (8)

This is independent of n at the EXPONENT level; constants still depend on the
fixed field and n. Increasing the character order does not remove this loss.
At the central line the general pattern is

 r=1: 1; r=2: 1+1/n; r=3: 3/2+1/(2n); r>=4: r/2.

For the sextic case, central exponents at r=1,2,3,4,8 are
1,7/6,19/12,2,4. The diagonal-family bound U^(1+epsilon) is obtained at and
to the right of the following fixed lines:

 r=1: 1/2; r=2: 1/2+1/(2n);
 r=3: 2/3+1/(6n); r>=4: 1-1/r.                       (9)

At n=6 the first three are 1/2,7/12,25/36. These sufficient lines move RIGHT,
toward 1, not left toward 1/2. The centered normalized root bound from this
hierarchy is U^((K_(n,r)(1/2)-1)/(2r)+epsilon), tending to U^(1/4), not U^0.
This is not a lower theorem ruling out better L-value moments. It identifies
the loss retained by this particular AFE-plus-sieve argument.

## 5. An attempted escape: unbalanced AFE lengths

It is tempting to replace the balanced lengths by C_Q^v and C_Q^(r-v), 0<=v<=r.
At sigma>=1/2, a kernel monomial U^a V^b would give endpoint powers

  U^a C_Q^(v(1+b-2sigma)),
  U^a C_Q^((r-v)b+v(1-2sigma)).                         (10)

Small endpoints are paid by U. The balanced exponent (3) is already the minimum
of this endpoint model. To see this, select any monomial whose balanced power
exceeds U. Necessarily 1+b-2sigma>0. If v>=r/2 the main term is at least the
balanced term; if v<=r/2 the dual term exceeds it by
(r/2-v)(b+2sigma-1)>=0. Apply this to a balanced maximizing monomial. If none
exceeds U, the U endpoint is already the model's floor. This proves the claim.

Thus merely making the AFE asymmetric does not remove the growing-order loss.
The tests check the formula, not the validity of the imported AFE or sieve.
