# Independent audit of the actual-Xi odd-current scaling packet

Audited source: **af809698fe6cb5046a5bcc00e9175296e4597060**.
Authoring base: 1904d20cdb76ecd26e0e63472625da930075303e.
Review date: 2026-08-31.
Verdict: **PASS in the stated scalar-current scope**, with the explicit
normalized-majorant clarification in section 4 below.
No source files were changed; this audit has its own identity.

The two analytic notes, exact producer, numerical scout, fixture, source
manifest and 24-test module were read in full. All four pinned source notes
were read at their literal frozen identities. This review does not import
a subsequently extended all-growing-order saddle theorem.

## 1. Literal source, compact-kappa limit, and normalization

The pinned actual-kernel proof supplies the full-line normalization
Phi_Xi=2 phi_0, strict even positivity, and the all-real product bound
H_xi(d)/H_xi(0)<=9 exp[-2pi exp(xi)(cosh d-1)].
The exterior |d|>xi is included: its additional factor
exp[9(|d|-xi)/2-2pi sinh(|d|-xi)] is at most one.
No balanced-only asymptotic has been used on that exterior.

For positive odd K, the current factor is positive and has the exact
integral resummation F_K(x)=(1/2)int_(-1)^1(1+tx)^(K-1)dt.
The exponent K-1 is even, so this formula and the global bound
F_K(x)<=exp(K|x|) remain valid for |x|>1.
The pushforward density really is proportional to
u^2 F_K(delta u)R_xi(u); its two extra powers are not optional.

On |epsilon u|<=1 the first-orbit correction is 1+O(exp(-xi)),
uniformly, and the exponent correction is nonnegative O(u^4 exp(-xi)).
Combining this with 1-exp(-v)<=v yields the stated weighted kernel error.
Outside that region, the all-real Gaussian majorant makes every fixed
polynomial/exponential-weight tail negligible at the claimed error scale.

The logarithm comparison for |delta u|<=1/2 incurs
O(delta(|u|+A u^2)) uniformly for kappa<=A. Choosing A delta<=1/4
leaves a common Gaussian majorant. The omitted |u|>1/(2delta)
region is controlled by exp(A|u|-u^2), not by a truncated current
polynomial. Thus the unnormalized weighted L1 error is
O(delta+exp(-xi)) for every stated fixed weight.

The independent Gaussian normalization is
int u^2 sinhc(kappa u)exp(-u^2)du
=sqrt(pi)exp(kappa^2/4)/2.
Its uniform positive lower bound justifies division. The normalized
weighted L1 theorem in double-scaling equation (2.2) therefore passes,
including fixed K and kappa tending to zero.

Differentiating the ordinary Gaussian exponential integral gives exactly
exp(t^2/4)[cosh(kappa t/2)+(t/kappa)sinh(kappa t/2)].
The continuous kappa=0 value is exp(t^2/4)(1+t^2/2).
This confirms both displayed moments and the all-fixed-moment derivative
recurrence. Integrating two sinh factors also gives exactly
exp(tau^2/4)sinhc(kappa tau/2) for the untranslated current ratio.
There is no extra exp(-h xi) factor.

Cancelling Q_K in the literal scalar definitions gives the two ratios
in double-scaling (3.3), hence the stated gain, phase and
2K rho=1+kappa^2/2-4w+O(delta+exp(-xi)).
This is scalar evaluation at changing source parameters, not permission
to replace a prescribed physical constant by a multiplier.

## 2. Separated saddles and all-real weighted domination

For bounded b=K/(xi exp(xi)), the saddle equation
K/(xi+a)=2pi exp(xi)sinh(a) has one positive solution.
It bounds a above by arsinh(B/(2pi)).
It also gives a sqrt(exp(xi))>=c_B kappa and
J/exp(xi) bounded above and below. Thus kappa tending to infinity
places d=0 increasingly many Gaussian widths from the positive saddle,
even when b tends to zero.

The logarithmic majorant has derivative zero at a and global curvature
at most -2pi exp(xi). Its local third derivative divided by J^(3/2)
tends to zero. On every fixed rescaled interval, d/a tends to one,
both kernel arguments tend to positive infinity, and
|((xi-d)/(xi+d))|^K tends to zero.
For the last assertion the interval is eventually d<xi and
Kd/xi>=c_B kappa^2. This local use is not extended incorrectly to d>xi.

The exact bracket 1-r(d)^K lies between zero and two everywhere d>0.
The global kernel bound and concavity therefore give
(d/a)exp[-pi exp(xi)(d-a)^2]
<=C_B(1+|v|)exp(-c_B v^2).
This is integrable against every fixed polynomial times exp(T|v|).
A positive local normalization closes the weighted L1 Gaussian limit.
Both reflected halves and the moving lower endpoint are handled.

Repeating the argument for the plus integrals and for each fixed
nonnegative power d^r gives the scalar gain/phase limits without invoking
a singular inverse-d moment. It yields the macroscopic two-point law,
the fixed-h sinhc profile, and the stated scalar carrier zero and width.
The proof does not cover unbounded b or increasing moment/weight orders.
The use of the exact saddle a, rather than its limiting location a_0,
is essential and correctly retained.

## 3. The third scale uses the plus measure

The carrier-transition note correctly derives
p_K/g_K=E_(nu_K^+)[d^2]/xi^2.
The measure nu_K^+ is weighted by P_K H, not by the current weight.
At K=1 its leading second moment is 1/(2pi exp(xi)), whereas
the current's is 3/(2pi exp(xi)).

For P_(K+2)/P_K, the shared coefficient ratios strictly increase
with the degree index, and the new highest coefficient is positive.
The coefficient-pair formula for B'A-BA' is therefore positive for z>0.
The covariance of z with this strictly increasing likelihood ratio is
strictly positive under the full positive density. This proves strict
monotonicity, not only nondecrease.

On any compact interval [D,D+1], the factor
1+((xi-d)/(xi+d))^K has a uniform positive lower bound over odd K,
because the ratio has absolute value strictly less than one there.
Comparison with [0,R], D>R, proves escape of the probability mass.
Hence the plus second moment tends to infinity. The initial-positive
statement is correctly asserted only for sufficiently large xi.
There is at most one equality and one sign change on the odd lattice;
no noninteger current is thereby defined.

## 4. Critical Taylor coefficient and explicit tail normalization

Put q=xi, M=pi exp(2q), r=d-q and ell=1+1/(2q).
The high factor has logarithm
constant+(9/4)r-M exp(r)+log theta_*(exp(2q+r)).
The low factor is the literal even function Phi_Xi(r/2).
The latter cannot be replaced by its high-argument first orbit.

The logarithm of the density, in y=sqrt(M)r, has leading terms
-ell y^2/2 + M^(-1/2)[u y-A y^3/6],
where u=Delta/(2q)+9/4 and A=1-1/(2q^2).
The next polynomial is even and equals the displayed L_2 up to
terms already within the stated remainder.
The theta correction's first derivative is O(1/M), giving
O(M^(-3/2)|y|), not an omitted order-M^(-1/2) term.
Evenness of the low kernel eliminates another possible linear term.

After exponentiation, the order-M^(-1/2) term is odd and the
order-M^(-1) term is even. Gaussian integration gives
E[r]=M^(-1)[u/ell-A/(2ell^2)]+O(M^(-2))
and E[r^2]=(M ell)^(-1)+O(M^(-2)).
The first remainder uses parity of the intermediate term; estimating it
without parity would lose the advertised threshold accuracy.

Consequently
M ell(m_K^+-q^2)=Delta+9q/2+1-qA/ell+O(q/M).
The exact simplification
qA/ell=q-1/2-1/(4q+2)
gives Delta+7q/2+3/2+1/(4q+2), independently confirming every
displayed correction and the O(q exp(-2q)) threshold uncertainty.
The odd-lattice caveat is necessary and correctly stated.

**Normalized-majorant clarification.** Carrier-transition lines 165--171
say "a constant times exp F_0". The omitted common prefactor depends on q;
one must not interpret this as a bare uniform constant.
For the unnormalized density with its harmless (2q)^(-K) removed,
a valid global majorant is
18 H_q(0)exp(2pi exp(q))exp(F_0(d)).
At d=q, its ratio to the exact unnormalized density tends to
72pi^2 exp(-pi)/Phi_Xi(0), a finite positive constant.
Indeed the exact ratio is that constant times
theta_*(exp(q))^2/theta_*(exp(2q)).
This proves the uniform normalized comparison asserted by the source.
The common factor cancels and creates no additional saddle derivative.

Also F_0'(q)=Delta/(2q)+pi=O_C(1), and on |d-q|<=1
F_0''<=-cM. Away from that interval the global strict concavity and
the two endpoint slopes give exponentially small tails. The central
window |y|<=M^(1/24) has positive normalization comparable to one in
y-coordinates. Polynomial Taylor remainders are Gaussian-integrable;
the complement is smaller than every fixed inverse power of M.
Thus the whole-line integration and normalized remainder in the theorem
are justified. No new analytic hypothesis is needed for this clarification.

## 5. Frozen replay and independent finite checks

The fresh review worktree initially checked out exact af809698:

- 24 original tests passed normally in 10.956 seconds;
- 24 passed with -O in 10.836 seconds;
- both producer --check runs passed;
- producer --emit-report and --emit-manifest matched the frozen fixture
  and manifest bytewise after CRLF-to-LF normalization, in both modes;
- Ruff check and format --check passed for both producers and tests;
- the complete S1904-to-af809698 diff passed git diff --check.

Independent in-memory controls, run normal and -O, reconstructed all
four source Git identities and LF hashes and all six artifact hashes
without the producer's hash helper. They additionally checked:

- 16 arbitrary rational q/Delta panels using Gaussian monomial moments
  and parity, independently recovering the third-scale coefficient;
- 30 balanced/exterior current identities at K=65,81,127, beyond the
  source producer's declared K<=63 finite panel, with a separate exact
  binomial/integral expansion.

These extra finite checks do not prove any asymptotic quantifier.
The canonical JSON report SHA-256 independently computed for this audit is
435ee4cb1d5f469e8bff6aec7d31f0e62133b2117a39d8634961ad252c7d3e62.

The artifact LF SHA-256 values are:

| artifact | SHA-256 |
|---|---|
| double-scaling note | 3c7c16677311d40d8219a88ffb236984ea8704a8ef4e1a30f8b9da1637342e41 |
| carrier-transition note | b7f3b85a56dba60b1b249ddd447d68f6cd9421423fa7fc1c27aa32804891becc |
| exact producer | 3ec353766ba53206af647adc84eec139503d7404a5113057fd00de985b62bd95 |
| scout | c9726967a842e1f0b9343bc6eae4cf54e17a45ebc0fe23f2d1f32caf6145626b |
| manifest | 40faa58ea354d2f7f86ee9859d1112227ed5b12e716546c28b6d20320142bdda |
| tests | 98ae7beab3a0d970b5760076783dcbf30e71d025503f1db96451e62219cb96e9 |

One additional NON-DIRECTED scout was run at xi=4, boundary-offset=0,
40 decimal digits and radius 16. It selected K=74905; the critical
coordinate was approximately 0.9098535547 and the scaled moment
approximately 0.9122172604. Its residual 0.0023637058 is recorded only
as a finite attempted falsifier, not a sign certificate or error bound.
The scout's output explicitly reports certified=false and bounded
quadrature without a full-integral certificate.

## 6. Machine and scientific scope

The exact producer authenticates the declared finite polynomial, rational,
Gaussian-coefficient and source panel. Its public scientific parameters
have strict odd-order, moment-index and 64-bit rational-input caps; bool,
float and forbidden orders are rejected under -O. Fresh canonical rebuild
rejects altered source contracts, coefficient panels and scope assertions.

This audit does not upgrade the producer into a hostile byte-stream API:
its JSON loader is ordinary json.loads, with no explicit duplicate-key,
byte-count or nesting limits. It validates the resulting parsed report.
Any future untrusted-input deployment should add separate parser/resource
hardening. The frozen fixed-source replay does not require such a deployment,
and the notes do not claim it.

The numerical scout remains a separate non-directed discovery tool; its
outputs are not loaded as evidence by the exact producer. No finite
calculation verifies the analytic proofs formally.

All accepted conclusions concern the changed family of positive odd
currents and its literal scalar observables. They establish no physical
constant-scale transfer, innerness, source-Pick congruence, nonlocal
cofinal capture, topological free-energy bound, or RH percentage.
No novelty or publication-priority claim is accepted.
