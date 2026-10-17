# Pointwise additive power cancellation for the complete capped norm tensor

Status: component proof. Its arithmetic input is an explicitly stated uniform
additive power estimate for the native column. The common Dirichlet zero-free
half-plane discussed below is a hypothesis here; citing a recent paper that
asserts it is not an independent verification of that paper. No stronger
zero-free half-plane or RH proof is claimed.

The new conclusion relative to #964 is a POWER bound at EVERY endpoint and
additive frequency, with all original column caps and Gaussian weights kept.
It has a more restricted phase class than #964's polynomial supremum. The
cap propagation below is elementary and is not a new cancellation theorem
for arbitrary divisor-bounded sequences: the native Fourier estimate is its
load-bearing arithmetic premise.

## 1. An abstract capped-column lemma

Fix k>=1 and nu>=1. For each i let A_i(n) satisfy |A_i(n)|<=d_nu(n), where
d_nu is the ordinary nu-fold divisor function. Suppose, for some 0<lambda<1,
every eta>0 has a constant such that

    sup_alpha |sum_(n<=Y) A_i(n)e(alpha n)|
                         <= C_eta Y^(lambda+eta), Y>=1.       (1)

Constants may depend on the finitely many fixed columns, but are uniform in
alpha and Y. Put

    lambda_k=1-(1-lambda)/k.

For any k intervals (L_i,U_i], with 0<=L_i<U_i<=infinity, define

    T(n)=sum_(n_1...n_k=n; L_i<n_i<=U_i) product_i A_i(n_i).

Then, uniformly in all intervals, X>=1 and alpha,

    |sum_(n<=X) T(n)e(alpha n)| <<_eta X^(lambda_k+eta). (2)

Proof. Assign each tuple to its largest n_j, breaking ties by the first
index. Fix j and every other factor, and put a=product_(i!=j)n_i. The
product bound and maximality imply a<=X^(1-1/k). Every restriction on the
free variable n_j is an interval restriction: its original cap, n_j<=X/a,
and the exact weak/strict inequalities implementing this tie rule.
Consequently (1), applied to a difference of two prefixes, bounds the free
sum by 2C_eta(X/a)^(lambda+eta), with the LITERAL phase alpha*a.

The absolute weights of all other factors are at most
d_(nu(k-1))(a). For every fixed integer h>=1 and 0<s<1,

    sum_(a<=Y) d_h(a)a^(-s)
          <<_(h,s) Y^(1-s)(1+log(2Y))^(h-1).           (3)

Indeed sum_(a<=Y)d_h(a)<=Y(1+log Y)^(h-1) by repeated harmonic summation,
and partial summation proves (3). It follows that the sum over the fixed
factors costs X^((1-1/k)(1-lambda-eta)) times a fixed logarithmic power.
The total power is lambda_k+eta/k. Relabel eta and absorb the logarithm.
For k=1 there are no fixed factors and (2) is directly (1). Every tuple
has exactly one owner; shared primes and equal factors remain. QED.

The same assertion holds if every original A_i(n_i) is multiplied by a
separately fixed n_i^(it_i). Partial summation in (1) changes its constant
by at most a fixed multiple of 1+|t_i|. This is a priced fixed-height
statement, not a constant uniform over all heights.

## 2. The actual Eisenstein coefficients and completion kernels

Let K=Q(omega), omega^2+omega+1=0. Its complete native norm coefficient is

    A_K(n)=sum_(NI=n) mu_K(I)=(mu*(mu chi_-3))(n).        (4)

At split rational primes its Euler polynomial is (1-x)^2; at inert primes
it is 1-x^2; at 3 it is 1-x. Thus both split prime ideals are included and
|A_K(n)|<=d_2(n). A fixed norm Dirichlet character xi gives

    A_K(n)xi(n)=((mu xi)*(mu xi chi_-3))(n).             (5)

The literal zeros of xi are preserved by complete multiplicativity.

For each column fix a finite set S_i of excluded IDEAL primes. At a good
ideal prime of norm q use precisely one of the local sources

    native:       1-x;
    coupled:      1-(1-1/q)x-z_p q^(m/2-1)x^m;
    two-channel:  (1-x)(1-z_p q^(m/2-1)x^m);
    geometric:    1-(1-1/q)x/(1-z_p q^(m/2-1)x^m),       (6)

where m>=2 and |z_p|<=1. At an excluded ideal prime the ENTIRE source
factor is 1. Different columns can have different families, degrees,
profiles and exclusions. Optional fixed norm Dirichlet twists are allowed.

Divide (6) formally by the unmasked native factor 1-x, and call the ideal
correction coefficients b_i(I). At an excluded ideal prime the correction
is (1-x)^(-1), not 1. For every fixed sigma>1/2,

    sum_I |b_i(I)|(NI)^(-sigma) <= C_(sigma,S_i),        (7)

uniformly in all m>=2 and profiles. The same bound holds after aggregation
by rational norm or multiplication by a norm character of modulus at most
one.

Here is the local proof. Put delta=sigma-1/2, t=q^(-sigma), and
B=z_p q^(m/2-1)x^m. Its absolute coefficient mass at x=t is at most
q^(-1-m delta). The coupled correction minus 1 is (x/q-B)/(1-x), the
two-channel correction minus 1 is -B, and the geometric correction minus
1 is (x/q-xB)/((1-x)(1-B)). Their nonconstant masses are therefore

    O_sigma(q^(-1-sigma)+q^(-1-m delta))
        <= O_sigma(q^(-1-sigma)+q^(-1-2delta)).         (8)

All geometric denominators are uniformly positive in these absolute
majorants. The prime-ideal sums converge. The finitely many omitted factors
have masses (1-q^(-sigma))^(-1). Multiplication proves (7). This is an
absolute coefficient argument; no Euler product is asserted to converge
on Re s=1/2.

Let B_i(d)=sum_(NI=d)b_i(I), including the optional norm twist, and let C_i(n)
be the full rational-norm aggregate of the completed ideal column. Then

    C_i=A_i*B_i                                             (9)

exactly, with A_i as in (5). Asymmetric ideal exclusions at a split rational
prime are permitted. Neither (9) nor its proof replaces the two conjugate
ideals by a single rational prime.

## 3. Complete cap and BV-weight propagation

Assume (1) for the native A_i in (9), now with nu=2 and lambda>1/2.
For each i let W_i be a left-continuous complex BV function on (0,infinity),
tending to zero at infinity, with total variation V_i. Choose ANY D_i>0.
The exact tensor in #964 is

    a_D(n)=sum_(product_i NI_i=n)
                    product_i[c_i(I_i) W_i(NI_i/D_i)].

Then, for every eta>0,

    sup_alpha |sum_(n<=X) a_D(n)e(alpha n)|
         <<_eta (product_i V_i) X^(1-(1-lambda)/k+eta).  (10)

The constant is uniform in D_i, m_i>=2 and every powerful profile. The
parameters k, S_i and ordinary norm Dirichlet characters remain fixed.

Proof for hard interval tests. Insert (9) SEPARATELY in each original
column. Fix correction norms d_i and put d=product d_i. The native cap is
the original column interval divided by d_i; the native product is <=X/d;
and the additive phase becomes alpha*d. Lemma (2) therefore bounds this
term by C(X/d)^(lambda_k+eta). Summing the absolute correction coefficients
costs at most

    product_i sum_(d_i>=1)|B_i(d_i)|d_i^(-lambda_k-eta),

which is finite and uniform by (7). Terms with d>X are empty. No cap is
deleted before cancellation and no additional coprimality is inserted.

For BV tests, use the left-continuous Stieltjes representation

    W_i(v/D_i)=-integral_[v,infinity) d[W_i(t/D_i)].     (11)

Thus each coefficient is an integral of exact hard-cap coefficients, with
total variation V_i. For n<=X all ideal norms involved are <=X, so the
coefficient sums are finite. Fubini and the triangle inequality against
the finite variation measures apply to (10)'s already canceled hard-cap
sums. They give (10), uniformly in the scales. In particular the original
noncompact logarithmic Gaussian is included, with no omitted tails. QED.

## 4. The proved arithmetic input and its exact exponent

Let (ZF_theta) mean that EVERY primitive Dirichlet L-function is zero-free
on Re s>theta, with one common theta in [2/3,1). This is a global hypothesis
about all conductors and heights; a finite computation is not a substitute.

The companion DIRECT_FOURIER.md, using the analytic adapter in
STRIP_AND_MAJOR_ARCS.md, proves for every fixed finite set of ordinary
Dirichlet characters xi_j that

    sup_alpha |sum_(n<=Y)[(mu xi_1)*...*(mu xi_r)](n)e(alpha n)|
                <<_eta Y^((1+theta)/2+eta).            (12)

The direct finite inverse identity and major/minor-arc proof apply to the
UNCAPPED reciprocal product. Taking the two factors in (5) therefore gives

    lambda_K=(1+theta)/2.

Equation (10) now gives the COMPLETE actual k-column tensor exponent

    beta_k=1-(1-theta)/(2k).                            (13)

For theta=7/8 the native and completed single-column exponent is 15/16,
and the complete capped k-column exponent is 1-1/(16k). The direct product
proof, rather than a claim that a one-bounded theorem applies to A_K,
supplies the stronger native input. This is a positive power saving at
every additive frequency. At frequency zero the imported strip already
gives the stronger native exponent theta+eta by ordinary Perron inversion.

For historical comparison, the classical Baker--Harman weak-GRH theorem
already gives (12) for rational mu when theta>=3/5. A fixed character has
a finite additive Fourier expansion, so the same rational exponent holds
for mu xi. Applying Section 1 to those two rational factors, without the
direct product proof, would give only lambda_K=(3+theta)/4 and the capped
exponent 1-(1-theta)/(4k). This is a valid weaker route, including 31/32
for one norm column at theta=7/8. We credit that classical starting point
separately from the companion's proved fixed-product adapter.

## 5. Pointwise local and growing-shift consequences

Write beta=1-(1-lambda)/k for whichever native input has actually been
proved. Estimate (10) controls every prefix and hence every interval in
[1,3X]. The indicator of a residue class modulo ANY integer q has additive
Fourier coefficients of total absolute mass 1. Consequently

    sup_(alpha,Q AP in (x,x+H])
          |sum_(n in Q)a_D(n)e(alpha n)| <<_eta X^(beta+eta) (14)

for X<=x<=2X and 1<=H<=X. The AP and frequency may change with x; q can
grow arbitrarily. This uses the already uniform additive estimate, not a
new uniform Dirichlet-conductor assertion. For H>=X^(beta+rho), rho>0,
(14) is a pointwise power saving relative to H. It is not relative to
the number of terms in a sparse progression, and it is for LINEAR phases.

For clarity, there is also a complete correlation consequence. Normalize
product V_i<=1. The full source satisfies, for every eta>0,

    sum_(n<=X)|a_D(n)|^2 <<_eta X^(1+eta).              (15a)

Here is a self-contained proof with no claim of a uniform logarithmic
loss at the critical weight. Put J_0=|B_1|*...*|B_k|. The coefficientwise
bound is |a_D|<=J_0*d_(2k), even with all separate weights and caps.
The elementary inequality d_h(n)^2<=d_(h^2)(n) and repeated harmonic
summation give sum_(n<=Y)d_(2k)(n)^2<<Y(log(3Y))^C_k.
Minkowski therefore gives

    (sum_(n<=X)|a_D(n)|^2)^(1/2)
       << X^(1/2)(log(3X))^(C_k/2)
                          sum_(d<=X) J_0(d)d^(-1/2)
       <= X^(1/2+rho)(log(3X))^(C_k/2)
                          sum_(d>=1) J_0(d)d^(-1/2-rho).

The last series is finite by (7), for every rho>0. Choosing rho first
sufficiently small proves (15a), uniformly in the original scales, degrees
and profiles. For completeness d_h(p^v)^2<=d_(h^2)(p^v) follows because
every pair of length-h weak compositions of v is the pair of margins of
at least one nonnegative h-by-h integer matrix of total sum v; counting
those matrices and multiplying over primes gives the stated inequality.

Let G, extended by zero outside [1,2X], satisfy sum|G|^2<=A X. For

    C_h(Y)=sum_(n<=Y)a_D(n)conjugate(G(n+h)),

global Fourier Parseval and (10), uniformly at each endpoint Y<=X, give

    sum_(h in Z) |C_h(Y)|^2
                       <<_eta A X^(1+2beta+eta).      (15b)

A square-mass endpoint partition then gives, for 1<=H<=X,

    sum_(1<=h<=H)max_(Y<=X)|C_h(Y)|
       <<_eta sqrt(A) HX (X^(2beta-1)/H)^(1/4) X^eta,  (16)

in the nontrivial range H>=X^(2beta-1). Here is the complete maximal step.
Let L=sum_(n<=X)|a_D(n)|^2; the assertion is trivial if L=0. For an integer
J>=1, put an endpoint immediately before and at the first index where
each cumulative mass level jL/J, 1<=j<J, is reached, and include 0 and
floor(X). There are O(J) endpoints. Heavy atoms are thus isolated, and
every residual prefix after its preceding endpoint has square mass <=L/J.
For each h its correlation is a coarse endpoint value plus that residual.
By Cauchy the residual squared is at most (L/J) A X. Summing the coarse
endpoint squares over all h uses (15b) O(J) times. Summing the residual
over 1<=h<=H and then using (15a) proves

    sum_(1<=h<=H) max_(Y<=X)|C_h(Y)|^2
        <<_eta A H X^(2+eta)
                          [J X^(2beta-1)/H + 1/J].

Choose J comparable with (H/X^(2beta-1))^(1/2), and absorb fixed logarithms
and all previously allocated small losses into the final X^eta. Cauchy
in h proves (16). The endpoint partition depends only on a_D; all signs
inside every correlation and all selected endpoints remain. No individual
fixed-shift Chowla theorem follows.

For theta=7/8 and k columns, beta=1-1/(16k). The shift threshold is
H>=X^(1-1/(8k)); at H=X, (16) saves X^(1/(32k)-eta) over HX. In particular
one complete norm column gives a saving X^(1/32-eta). These are stronger
than every fixed logarithmic saving in that range, conditional on the
common-strip input. They do not supply square-root cancellation or a
subpower bound for the whole native critical energy.

## 6. Source record and mathematical limits

1. R. C. Baker and G. Harman, *Exponential Sums Formed with the Mobius
   Function*, J. London Math. Soc. s2-43 (1991), 193--198.
   https://doi.org/10.1112/jlms/s2-43.2.193
   Publisher bibliographic record was inspected. The full original PDF was
   not accessible in this session and is not claimed to have been rebuilt.

2. Wei Zhang, *On an exponential sum related to the Mobius function*,
   arXiv:2204.04613v2 (16 October 2022), introduction and Lemma 2.2.
   https://arxiv.org/html/2204.04613v2
   This primary paper explicitly states the exact Baker--Harman global
   piecewise exponent and its linear major-arc estimate
   X^(theta+eta)q^(1/2)(1+X|alpha-a/q|)^(1/2). The full short paper was read.
   Its separate proposed improvement for theta<=4/7 is not used here.

3. Xiaoguang He and Bingrong Huang, *Exponential sums involving the Mobius
   function*, author manuscript dated 10 April 2015.
   https://bingronghuang.github.io/expsum2016he.pdf
   Its (1.3)--(1.4) independently state the common-strip hypothesis and
   Baker--Harman exponent. Lemma 2 gives the conductor-uniform reciprocal
   bound on an interior margin. Its Lemma 3 is stated for monomial degrees
   >=3 and is NOT substituted as a linear-phase theorem. Those statements
   and the analytic proof mechanism were read.

4. #964 at 09ab9bc067bc66278fad8fcd883e8c8569b0cbc9:
   standalone/2026-10-17-native-local-uniformity/PROOF.md,
   blob 554d5d3f3b48a7c7e86356b7c28e2a5c3ccf75a3. Full proof read.
   The exact norm factorization, cap preservation, ideal exclusions and
   BV endpoint convention are retained. Its unconditional polynomial
   uniformity gives arbitrary logarithmic savings in a different range;
   it does not itself imply (12) or (13).

5. #963 at c91fd9ddfb37668338d9aec22c0e29cfe741cf07:
   standalone/2026-10-17-archimedean-ideal-resolution/PROOF.md,
   blob 2874d4e3d107d65df756633b191d5113412d113b. Main proof read.
   Its extra angular/radial probability average is not removed here.

All arithmetic uses rational norm twists. General sextic physical rows,
arbitrary number fields, growing ordinary conductors, growing tensor order,
and growing polynomial degree have not been added to these statements.
The estimates at alpha=0 cannot improve their own imported zero-free boundary:
the displayed exponents are larger than theta. A full RH proof still needs
new information at the native coherent component, not repeated propagation
of these bounds.

## 7. Exact finite validation

Run `python check_capped_norm_transfer.py`. It writes CAPPED_CHECK_RESULTS.json
beside the script, and prints exactly that file's contents. The fixture uses
integers and rational fractions throughout; no floating point comparison or
sampled frequency grid is treated as evidence for an asymptotic estimate.

The completed run checks 40 complete norm-source cases through norm 256,
including all four source families, even powerful degrees 2,4,6, a fixed
Dirichlet twist with literal zeros, and asymmetric exclusions of one prime
above 7 together with the ramified prime. It verifies 2,380 ideal-local
coefficient identities and 10,240 complete norm coefficients. Three exact
largest-factor partitions retain all 1,086 original tuples, including 156
ties and 437 tuples with shared prime factors. Three completed cap tests
check all 288 output coefficients after separately rescaling every original
cap by its own correction norm; they retain 228 correction tuples. Nine BV
atomic tensor terms reproduce all 96 weighted coefficients exactly.

For the maximal step, 24 quantile partitions include deliberately heavy
atoms and test 408 residual prefixes and 384 exact endpoint inequalities.
There are also 51 full-shift quadratic expansions and six rational exponent
checks. Three negative controls are rejected: deleting an excluded-prime
repair, failing to rescale each cap, and substituting an index grid for
the square-mass quantiles. All gates use explicit exceptions and remain
active under Python's -O mode. The exact checked coefficient stream has SHA-256

    41fbd30d115f3424ef91db154801d4039bbab6e51843597cc357ad25d5be15fe

These are implementation and bookkeeping fixtures for the displayed
identities. The analytic proof is in the text and its two companions; none
of these finite checks proves the imported common strip, an asymptotic
cancellation theorem, a priority claim, or RH.
