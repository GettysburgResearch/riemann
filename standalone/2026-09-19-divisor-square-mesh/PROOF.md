# DSE27: prime-mode square cancellation and divisor-first critical meshes

**Status: proposed component proofs and rigorously bounded finite computations.**
**The native unbounded energy gain and RH are not proved.**
Date: 19 September 2026. Continuation of issue #902 and #848, read at
`617cfaca6130addd2d16bbce6af117a55aef761b`.

This pass does not pretend that its new finite bound is a new asymptotic bound.
It contributes (i) an exact prime-frequency negative-square identity and an
all-cutoff upper budget for the entire prime-denominator contribution;
(ii) a complete logarithmic interpolation-error budget, allowing the FULL
native physical energy to be enclosed from a critical sparse mesh; and
(iii) a divisor-first finite certificate through 16,777,215, with no future
Mobius values in the recurrence generating its samples. A second, independent
full-length sieve checks those samples and the complete energy.

The new prime-mode partition is NOT RCB26's partition by product squareclass.
The physical energy below is E, NOT the reciprocal-innovation energy F, the
balanced energy A, or a truncated harmonic covariance. No inequality for one
of those other objects is inferred just by giving it the same name.

Finite Fourier inversion, elementary sampling inequalities, Mobius inversion,
and the Huxley-Watt short-source Newton identity are classical. No general
priority claim is made. The application and fully specified budgets are the
proposed research components here. The current NSR26 counterfamilies remain
valid for their declared nonnative classes.

## 1. Exact rational Fourier decomposition of the physical Newton output

Let c be a real finite source supported through L, with

    sum_n c(n)/n = 0.

Use ordinary Dirichlet convolution, put z=c*c, S=sum c(n), and define

    V(k) = 2 A_c(k) - sum_d z(d) floor(k/d),
    A_c(k) = sum_(n<=k)c(n),                    k>=1.

This is the actual cumulative function of 2c-1*c*c. Products are coalesced
before defining any mode. All d<=L^2 remain, including d greater than k.

For an integer d>=1 define the rational-valued periodic function

    T_d(k)=(d-1)/2 - (k mod d).

For q>=2 put

    R_q(k)=sum_(d|q) mu(q/d) T_d(k),
    B_q=sum_(d<=L^2, q|d) z(d)/d.                       (1)

Ordinary finite divisor inversion gives T_d=sum_(q|d,q>=2) R_q, since T_1=0.
Also {k/d}=(d-1)/(2d)-T_d(k)/d. The reciprocal balance implies
sum z(d)/d=0. Substituting floor(k/d)=k/d-{k/d} therefore proves, at EVERY
integer k>=1,

    V(k)=2A_c(k)+S^2/2-sum_(q=2)^(L^2) B_q R_q(k).      (2)

There is no midpoint convention, integer-boundary omission, infinite Fourier
series, or missing tail in (2). The constant and the possibly nonconstant
collar 2A_c(k) are indispensable.

For interpretation, with e(t)=exp(2*pi*i*t), finite Fourier inversion gives

    R_q(k)=sum_(1<=a<q, gcd(a,q)=1) e(ak/q)/(1-e(-a/q)).  (3)

One proves this first for T_d by multiplying the finite geometric-derivative
sum by 1-e(-a/d), then groups frequencies by reduced denominator. Formula (1)
is an exact rational implementation of (3); the checker uses (1), not floating
complex exponentials. Despite the complex form, R_q is real and half-integral.

## 2. A complete upper bound for ALL prime-denominator modes

Write U_p=sum_(p|n)c(n)/n for a prime p. Since p|rs means p|r or p|s,
inclusion-exclusion BEFORE taking a norm gives

    B_p = 2 (sum c(n)/n) U_p-U_p^2 = -U_p^2.            (4)

This is a genuine cancellation, not an assumption about random signs. The
identity uses reciprocal balance. At composite denominators it is false in
this form. For c=delta_1-2delta_2, B_2=-1 but B_4=+1.

As R_p=T_p and |R_p(k)|<p/2, the entire prime-denominator contribution

    P_c(k)=-sum_(p prime) B_p R_p(k)
           =sum_(p<=L) U_p^2 R_p(k)

satisfies a uniform pointwise bound. If |c(n)|<=K, then

    |U_p| <= (K/p) H_floor(L/p) <= K H_L/p,
    |P_c(k)| <= (K^2 H_L^2/2) sum_(p<=L)1/p
               <= (K^2/2) H_L^3.                       (5)

Here H_n=sum_(j<=n)1/j. Thus, for b>=1 and B=b^2-1,

    sum_(k=b)^B P_c(k)^2/[k(k+1)]
        <= (K^4/4) H_L^6 (1/b-1/b^2).                  (6)

This covers every prime denominator through L, including primes much larger
than the polylogarithmic bank in RCB26. It is a bound on their whole combined
function, not a period average or a diagonal-only approximation.

For PCR26's ACTUAL clipped completion, K=3 and L<=2Y. Formula (6) therefore
pays this complete sector at every cutoff, with the explicit factor 81/4.
It does not use the full native divisor equations and is not a native global
gain. Those qualifications matter.

### A sharper native bound at reciprocal crossings

Let Y>=2 satisfy mu(Y)!=0 and m(Y-1)m(Y)<=0, where
m(x)=sum_(n<=x)mu(n)/n. Then |m(Y)|<=1/Y. Use the one-atom balanced source

    c(n)=mu(n), n<=Y;   c(b)=-b m(Y), b=Y+1.

For every prime p,

    U_p=-(1/p)m_p(Y/p)-m(Y)1_(p|b),
    m_p(x)=sum_(n<=x,p does not divide n)mu(n)/n.         (7)

The elementary native bound |m_p(x)|<=1 follows from the FULL divisor inverse
identities, not from arbitrary coefficient caps. Here is a self-contained
proof. For integer N, let C_p(N) count powers of p through N and let R_p^*(N)
count positive integers through N not divisible by p. Divisor inversion gives

    sum_(n<=N,p does not divide n)mu(n) floor(N/n)=C_p(N).

Since {N/n}<=1-1/n and |mu(n)|<=1,

    |N m_p(N)| <= C_p(N)+R_p^*(N)
                           -sum_(n<=N,p does not divide n)1/n <= N.

Indeed the two counted sets intersect only at 1 and their union is a subset
of {1,...,N}; the harmonic sum is at least 1. Real x follows by its integer
part; below 1 the sum is zero. In (7), the divisible terms of mu are exactly
mu(pr)=-mu(r) when p does not divide r, and zero otherwise.

If U_p is nonzero then p<=b. Consequently

    |U_p| <= 1/p+1/Y <= 3/p,
    |P_c(k)| <= (9/2) H_b,
    sum_(k=b)^B P_c(k)^2/[k(k+1)] <= 81 H_b^2/(4b).      (8)

This sharper component estimate DOES use actual Mobius inversion. It is valid
at every cutoff satisfying the displayed finite crossing predicate. No
existence or spacing theorem for crossings is needed for its proof.

### What has not been bounded

Set W_c=V-P_c. It includes EVERY composite denominator, the constant, and the
collar. The valid composition is

    ||V|| <= ||W_c||+||P_c||                             (9)

in the declared annular physical norm. The mixed term has not disappeared.
In particular B_p<=0 is NOT a sign theorem for P_c(k), and (6)/(8) do NOT
justify deleting prime squares, higher composite modes, the zero frequency,
or correlations between these modes. They do not bound W_c.

## 3. Critical-mesh theorem: bound the FULL signed native energy

For any real arithmetic source with |a(n)|<=1, let A(k)=sum_(n<=k)a(n), and

    I(lo,last)=sum_(k=lo)^last A(k)^2/[k(k+1)].

Choose integer sample nodes lo=t_0<...<t_m=last. On a gap [a,b), put h=b-a,
and let R(k) equal the nearer sampled value A(a) or A(b), with ties assigned
to a. Retain the last cell k=last with R(last)=A(last). Define

    S_mesh=sum_(k=lo)^last R(k)^2/[k(k+1)],
    Z_mesh=sum_gaps floor(h/2)^2 * h/(a*b).              (10)

Both quantities can be computed in O(number of nodes) rational operations.
For each gap the switch is t=a+floor(h/2)+1, so its contribution to S_mesh is

    A(a)^2(1/a-1/t)+A(b)^2(1/t-1/b).

The last cell contributes A(last)^2/[last(last+1)]. Since bounded increments
give |A(k)-R(k)|<=floor(h/2), the COMPLETE weighted error is at most Z_mesh.
The Hilbert-space triangle inequality and its reverse now give

    (sqrt(S_mesh)-sqrt(Z_mesh))_+^2
        <= I(lo,last)
        <= (sqrt(S_mesh)+sqrt(Z_mesh))^2.               (11)

Every integer cell is covered. Agreement at the sample points is not used as
an interpolation assumption; (10) pays for all possible unseen excursions.

If every gap with h>=2 satisfies h<=eta sqrt(a), then

    Z_mesh <= (eta^2/4) sum_gaps h/b
            <= (eta^2/4) log(last/lo).                 (12)

The last inequality uses h/b<=log(b/a). Unit gaps have zero error. Thus the
entire between-sample error is logarithmic at the square-root mesh scale.
The cross term between sampled values and error is kept by (11).

### The actual mesh

The implementation uses all distinct floor(j^2/16) between lo and last,
plus the endpoints. For positive a its nontrivial gaps satisfy h<=sqrt(a):
for a>=9 use h<sqrt(a+1)/2+17/16<=sqrt(a), and check the finitely many earlier
gaps directly. Adding endpoints only shortens a gap. Thus (12) applies with
eta=1, while the accepting calculation uses the sharper EXACT rational Z_mesh.
There are O(sqrt(last)) nodes, not O(last) nodes.

This is a statement about certificate/sample size. It is NOT an O(sqrt(last))
claim for total arithmetic runtime: the exact sample producer has additional
recursive work, and the independent full sieve is linear-length work.

### Why coarser generic meshes would change the problem

The exponent 1/2 is the critical generic scale. In a block [X,2X], take a
mesh of spacing h comparable to X^theta, with 1/2<theta<1. Between successive
pair of zero sampled values, use an integer tent of increments +1 then -1
(with a zero step at the apex if needed). This is a valid bounded-coefficient
NONNATIVE source, identically zero at every sample point.

On the middle half of each gap its absolute cumulative value is at least
h/4-O(1). There are a constant times X/h gaps, and the weights are a constant
times X^-2. Its total missed energy is therefore at least

    c h^2/X >= c' X^(2theta-1)

for all large X. Hence a generic coarser mesh can hide power-sized energy.
At the critical scale the same construction has order-one cost per dyadic
block, consistent with the logarithmic error budget. This is a sharpness
statement for the bounded-increment class, not a counterexample to RH.

## 4. The samples use the literal inverse equations

For mu, write M(n)=sum_(r<=n)mu(r). Exact divisor inversion gives

    sum_(k=1)^n M(floor(n/k))=1,
    M(n)=1-sum_(k=2)^n M(floor(n/k)).                    (13)

All arguments on the right are smaller than n. Equal quotients are combined
before arithmetic. Given mu only through Y, and hence M through Y, (13)
reconstructs every required future sample exactly without a future Mobius
oracle. The implementations cache integer values; no random coefficient or
floating special-function value is involved.

For a balanced c agreeing with mu through Y, the exact Newton identity is
mu-(2c-1*c*c)=mu*(delta-1*c)*(delta-1*c). The error starts at (Y+1)^2.
Thus (2) really is M(k) for every k<=B=(Y+1)^2-1. Equality at (Y+1)^2 is
not assumed. This is the inherited short-source identity, not a new theorem.

This is a classical recurrence. Its use does not prove a magnitude bound for
its solution. Unlike a generic energy estimate, however, the finite samples
in (11) are generated by the exact native inverse constraints themselves.

For the square-ladder stage B=(Y+1)^2-1, add the exactly computed old energy

    E_Y=sum_(k<=Y)M(k)^2/[k(k+1)]

to (11) with lo=Y+1 and last=B. This bounds E_B, including ALL of its signed
pair correlations. It is not an estimate of an isolated favorable group.

The checker verifies the FINITE comparison

    (1+E_B)^2 <= 4(1+E_Y)^3.                            (14)

If such a comparison held at every sufficiently late square-ladder stage,
it would imply E_X=X^o(1). As in the existing BNR26/NIR26 proofs,
Cauchy-Schwarz on dyadic intervals would make
integral_1^infinity M(x)x^(-s-1) dx holomorphic for Re s>1/2, with s times
that integral equal to 1/zeta(s) in Re s>1. Analytic continuation and the
functional equation then exclude off-critical zeros. This conditional
consumer is inherited, not a new RH theorem.

**No unbounded version of (14) is proved.** Nor is (14) identified with the
original finite A-energy inequality: E,F,A are distinct finite quantities.
Working with E avoids adding a needless recompletion hypothesis to this
particular sufficient route. It does not remove its arithmetic difficulty.

## 5. Exact access to quadratic-phase covariance

This is an analytic continuation target, not an established cancellation gain.
Fix ONE balanced short source c, and use (2) at the mesh points. On each
residue class j=16t+r,

    floor(j^2/16)=16t^2+2rt+floor(r^2/16).               (15)

Consequently the rational Fourier factors in (3) become exact quadratic
exponentials on each of sixteen progressions. The nearest-endpoint weights
in S_mesh are explicit positive rational weights. Formula (2) therefore gives
an exact weighted quadratic-phase covariance for the actual source, while
(10)-(12) have already paid for ALL physical cells between the mesh points.

At most two inserted mesh endpoints are separate exact channels, not deleted
or asserted to lie on those quadratic progressions. Any samples in the
nonconstant collar retain the exact 2A_c(k) term.

Retain the zero-frequency coefficient and the collar from (2). Distinct
rational frequencies are not orthogonal after quadratic sampling. For example

    (1/4)sum_(t=0)^3 e(t^2/4)=(1+i)/2 !=0.             (16)

Thus replacing this covariance by its frequency diagonal is false even on
one complete short period. A standard quadratic large sieve for real
characters cannot be imported by name as a bound for these rational-frequency
amplitudes. A valid transfer would need the actual B_q, degeneracies,
zero frequency, weights, and all composite denominators.

The new prime-mode estimate pays one entire sector of this formulation. The
unpaid part is a precise COMPOSITE-mode weighted quadratic covariance. This
is not asserted to be easier than the prior cross-core covariance. The test
of this coordinate is whether it yields a NEW estimate for that native part,
not whether another equivalent statement can be written.

## 6. Executed native finite result and its precise limits

For Y=4095 and B=16,777,215, 16,129 samples cover the ENTIRE new annulus of
16,773,120 integer cells. The accepting outward computation gives

    E_4095 in (1.50575360154261, 1.50575360154262),
    S_mesh in (0.24137973263070, 0.24137973263072),
    Z_mesh in (0.51606312879715, 0.51606312879718),
    E_B < 2.96907798291454 < 3.

This certifies (14) at that specified native stage. The source-first sample
SHA256 is

    a0607d0ed174b3e9d2cb19cc0974e3e5d29a13e05ff9e22ddbf6c07676f89bc8.

A separate full-length Mobius sieve, run AFTER sample generation, verifies
every sampled M(n) and independently encloses the whole energy in

    (1.7465305178196, 1.7465305178206).

That second computation DOES compute future Mobius values, for finite
cross-checking only. It is not an input to the recurrence or the sparse
certificate. The sparse upper bound is deliberately less sharp than the
full sum; its complete error budget explains the difference.

These are not new records for zero verification or Mertens computation. They
are reproducible finite controls of a possible proof instrument. The finite
result does not verify every stage up to Y=4095, and does not certify the
original RCB26 cross-core scalar or A-energy by an unstated norm transfer.

Normal and optimized Python front ends, the compiled exact source producer,
the independent full sieve, and the bounded tests are documented separately
in VALIDATION.md. Same-author implementation agreement is not independent
mathematical review. No asymptotic source bound, full-repository validator,
Lean build, remote CI success or RH proof is claimed.
