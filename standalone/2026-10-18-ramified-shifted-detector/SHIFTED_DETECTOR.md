# Shift the detector line before estimating the mollifier

Status: PROPOSED complete source-qualified component proof; no independent
review or formal verification. This improves the exceptional-character count
of #966, not the full critical native moment or the all-field zero-free bound.
Deep inputs: the specified de Faveri sixth-order sieve and the classical Hecke
approximate functional equation. A shifted zero detector is reconstructed
below rather than asserted to be the literal printed BGL (5.3).

## 1. The exact family and the new count

Use exactly #966's fixed field F containing mu_6, admissible fixed S and DF
choice-dependent character family chi_a indexed by SIXTH-POWER-FREE exterior
ideals a. Retain the fixed finite-order S-supported twist psi. Every ideal
norm is the FULL norm, not the radical norm; every nonunit zero remains.
Constants can depend on all this data. Omit inducing-principal rows from the
zero count. Their bounded central values are harmless in a moment sum.

The source input, DF Theorem 1.1 at n=6, is the operator bound

 sum_(Na<=U)^flat |sum_(Nc<=V)^flat lambda_c (psi chi_a)(c)|^2
     << (UV)^eta V6(U,V) sum_c |lambda_c|^2,
 V6(U,V)=U+V+U^(5/6)V^(1/3)+U^(1/3)V^(5/6).                 (1)

Both indices are sixth-free. The printed source does not allow arbitrary
full columns without an adapter. The complete-column adapter is supplied
below. The fixed twist changes only the common column coefficients.

**Theorem D.** For every epsilon>0 there is a fixed rho>0 such that

 #{a: Na<=U, a sixth-free, L(s,psi chi_a) has a zero
                Re s>=3/4, |Im s|<=4U^rho}
                 << U^(395/552+epsilon).                  (2)

This is a count of indices with a zero, not an optimized total-zero count
or height-aspect theorem. Choose rho sufficiently small for the finite
height exponents below; constants are not asserted uniform as rho changes.
At a common sufficiently small positive height exponent, (2) improves
#966's 43/60 by EXACTLY 1/920. Compared with DF's displayed 8/11 the gain
is 71/6072. This is a new deduction relative to the inspected packets, not
a worldwide priority claim for off-central moments or zero detection.

The main parameter is an auxiliary detector line lambda=6/11 rather than
1/2. Moving this line changes BOTH the factor B^(lambda-sigma) and the
weights of the actual mollifier. Omitting either change would be invalid.

## 2. A complete off-central fourth-moment bound

**Lemma D1.** For fixed 1/2<=lambda<=7/12 and every eta>0,

 sum_(Na<=U)^flat |L^S(lambda+it,psi chi_a)|^4
      << U^(kappa(lambda)+eta)(2+|t|)^C,
 kappa(lambda)=max(1,13/6-2lambda).                        (3)

In particular lambda=6/11 gives kappa=71/66. This is a numerator-L moment,
not the unknown fourth moment of an inverse-L/Mobius source. Height powers
and constants need not be uniform near moving parameters.

**Proof.** Subdivide the inducing conductor into dyads Q0<=Ncond<2Q0,
Q0<<U, and the fixed S/gamma types into their finite list. The AFE for
L(s)^2 has two polynomial pieces of length Q0 times a polynomial in height,
with complete divisor coefficients d_2(n). A zero-conductor or bounded-
conductor piece is treated with Q0 comparable to one. The dual prefactor
has modulus O(Q0^(1-2lambda)(2+|t|)^C). Squaring its modulus in the row
second norm gives Q0^(2-4lambda), NOT a power of U silently substituted
for a negative conductor exponent.

Mellin inversion separates the row-dependent conductor weight within each
dyad. A small positive shift costs U^O(eta) and polynomial height. Rapid
AFE tails are summed by dyads before changing the final loss name. For a
complete main-piece dyad of product norm V, the coefficients have modulus
at most V^(-lambda+eta). Factor each column n=c d^6 uniquely, with c flat.
No coprimality (c,d)=1 is imposed, and the character identity is

 (psi chi_a)(c d^6)=psi(c)psi(d)^6 chi_a(c) 1_((a,d)=1).     (4)

For fixed d, its square-coefficient mass is at most
V^(1-2lambda+O(eta))/(Nd)^6. Use (1), dropping only the positive row mask
in this upper norm. Minkowski over d costs sum_d (Nd)^(-3+O(eta)), which
converges. It follows that the row second norm squared of that full dyad is

                   << V^(1-2lambda+O(eta)) V6(U,V).       (5)

The same argument applies to the dual coefficients, with lambda replaced
by 1-lambda. All sums remain over actual ideals, including equal-norm
conjugates and shared-prime factors.

For main dyads 1<=V<=Q0 up to the harmless height/loss factor, the largest
value in (5) is bounded by U^eta times

 U + Q0^(2-2lambda)
     + U^(5/6)Q0^(4/3-2lambda)
     + U^(1/3)Q0^(11/6-2lambda).

At the present lambda range the last two Q0 exponents are positive, so
Q0<=C U gives U^max(1,13/6-2lambda). For the dual sum, V^(2lambda-1)V6(U,V)
is increasing for V>=1. Multiplying its endpoint at Q0 by the ACTUAL
Q0^(2-4lambda) gives exactly Q0^(1-2lambda)V6(U,Q0), within the same bound.
This is why small inducing conductors do not invalidate the argument.
The Mellin norms, conductor dyads, common height integrals and rapid tails
cost only the stated arbitrary power and polynomial height. The estimate
|A+B|^2<=2(|A|^2+|B|^2) keeps both AFE pieces; their root numbers have
modulus one. Fixed removed S factors can be separated in a finite sum.
This proves (3). QED.

The argument also proves the neighboring fixed-line estimates needed for
Cauchy/Sobolev control. At endpoints use a sufficiently small enlargement
and the unreduced maximum of the four monomials above, not a claimed
uniform endpoint constant.

**Lemma D2 (the same-line mollifier).** Put
M_A(s,chi)=sum_(Nd<=A) mu_F(d)chi(d)(Nd)^(-s). For lambda>1/2,

 sum_(Na<=U)^flat |M_A(lambda+it,psi chi_a)|^2
       << (UA)^eta [U+sup_(1<=V<=A) V^(1-2lambda)V6(U,V)]. (6)

The coefficients are squarefree and hence already flat. Decompose by norm
dyads, apply (1) with the actual coefficient mass V^(1-2lambda+eta), and
retain the unit column. At lambda=1/2 the analogous bound holds with a
logarithm absorbed in eta. Uniformity in t is immediate from unit twists.
For A=U^a, the exponent in (6) is

 m(lambda,a)=max(1,
     1+(1-2lambda)a, (2-2lambda)a,
     5/6+(4/3-2lambda)a, 1/3+(11/6-2lambda)a).             (7)

These weights are stronger than merely applying the critical-line bound
to M_A; no orthogonality to a zero-selected subset is being assumed.

## 3. A shifted rowwise zero detector, with its maxima paid

Fix 1/2<lambda<sigma<1, 1<=A<=B, U>=2 and 1<=T<=U. Write a_A(n)=sum_(d|n,Nd<=A)mu_F(d).
Then a_A(1)=1, a_A(n)=0 for 1<Nn<=A, and |a_A(n)|<<_eta(Nn)^eta.
For each exceptional index choose ONE zero beta+i gamma with beta>=sigma
and |gamma|<=T. The choice is only for a proof, not a numerical zero census.
There are no such zeros with beta>1. Nonprincipal L is entire. At this zero,

 S= sum_n a_A(n)chi(n)(Nn)^(-beta-i gamma) exp(-Nn/B)
   = (1/(2pi i)) integral_(2) L(beta+i gamma+v,chi)
                       M_A(beta+i gamma+v,chi)Gamma(v)B^v dv.    (8)

Move the contour to Re v=lambda-beta, which is between -1 and 0 with fixed
margins away from the integer poles. The only crossed Gamma pole is v=0;
its residue is zero because L(beta+i gamma)=0. The Gamma factor makes the
horizontal limits vanish using ordinary polynomial strip bounds. Thus

 |S| << B^(lambda-sigma)
       integral_R |L(lambda+i(gamma+t))M_A(lambda+i(gamma+t))|
                    (1+|t|)^C exp(-pi |t|/2) dt.          (9)

The unit term on the left is exp(-1/B). We may assume B tends to infinity
as a fixed positive power of U; bounded initial scales are absorbed later.
The terms beyond B U^delta are negligible by the divisor bound and the
exponential, uniformly in gamma. Therefore at least one of the following
holds: the right side of (9) is bounded below, or the remaining polynomial
on A<Nn<=B U^delta is bounded below. Divide those terms into O(log U) dyads
and partially sum the monotone weight (Nn)^(sigma-beta)exp(-Nn/B). This
forces a weighted dyadic PREFIX maximum at real part sigma. Dyadic endpoint
intervals straddling A are included, not replaced by a complete dyad value.

Here are the costs of these maxima. For the first type, sum the integrals
in (9) over the selected rows, and cover possible gamma by a height interval
of length O(T+log^2 U); the exponentially small remainder is negligible.
The selected rowwise height maximum is bounded by integrated |L M_A|
using the subharmonic disk mean inequality with fixed radius r>0. Work at
nearby real parts within r of lambda. Sum the positive integrals before
Holder. Lemmas D1-D2 hold there with exponent at most the value at lambda
plus O(r)(1+a+b). Choose r small enough for the requested arbitrary loss.
This costs a fixed power of T and arbitrary powers of U, NOT an extra
factor U or R. The SAME selected set is used in Holder at every integration
point. Gamma factors and the finite S-data only change polynomial heights.

For the second type, sort ideals by norm (ties fixed) and decompose every
prefix into binary intervals. Cauchy costs logarithms. To bound each rowwise
height supremum on a unit interval use the elementary Sobolev bound by the
integral of |P|^2+|P'|^2 on a larger interval. Derivatives insert only log Nn.
The full complete-column sieve (4)-(5), now with coefficients of size
V^eta rather than V^-lambda, bounds each second mean by
(UV)^eta V V6(U,V). Binary disjointness at each level retains its total
coefficient mass. Summing the height intervals costs O(T+log^2 U).
Renaming losses and letting delta be sufficiently small proves the usable
inequality for the exceptional count R:

 R << U^eta(2+T)^C [
       B^(lambda-sigma) R^(1/4) U^(kappa(lambda)/4)
                               U^(m(lambda,a)/2)
       + B^(2-2sigma)+U A^(1-2sigma)
       + sup_(A<=V<=B)(U^(1/3)V^(11/6-2sigma)
                         +U^(5/6)V^(4/3-2sigma)) ],       (10)

when A=U^a, B=U^b with fixed a,b. On the first term we used
sum_E |L M| <= R^(1/4)(sum_all |L|^4)^(1/4)(sum_all |M|^2)^(1/2).
All four contributions of V6 are retained in the second type. Replacing
B U^delta by B in its endpoint exponents costs O(delta), already allotted.

The reconstruction follows the classical Mellin zero detector underlying
BGL (5.3); BGL print lambda=1/2, not (10) verbatim. The argument above
supplies the changed-line and maximal interfaces. Only one zero per index
is used, so a total-zero multiplicity theorem is not asserted.

## 4. Exact parameters and elimination

Set

 sigma=3/4, lambda=6/11,
 a=65/92, b=211/184, A=U^a, B=U^b.                      (11)

Here 1/2<lambda<sigma and 0<a<b. Equations (3) and (7) give

 kappa=71/66,
 m=max(1,947/1012,325/506,1525/1518,5209/6072)=1525/1518.

The exponent multiplying R^(1/4) in (10) is

 (lambda-sigma)b+kappa/4+m/2 = 395/736.                  (12)

After solving R<=C R^(1/4)U^(395/736)+C U^g, its cost is
(4/3)(395/736)=395/552. The other six endpoint exponents in (10) are

 211/368, 119/184, 157/276, 395/552, 395/552, 709/1104,  (13)

all at most 395/552. If R<=a0 R^(1/4)+b0 with nonnegative quantities,
then R<=max(2b0,(2a0)^(4/3)). Applying this to (10), choosing all initial
losses sufficiently small, and then a sufficiently small fixed rho>0 to
absorb (2+4U^rho)^C proves (2).

All inequalities above concern fixed parameters. Nearby strips were used
only with an explicitly arbitrarily small cost, not assumed to have the
exact same exponent without loss. Exact comparisons are

 43/60-395/552=1/920,
 8/11-395/552=71/6072.                                  (14)

A numerical optimization suggested these parameters but is not part of
the proof or verifier. The displayed rational choice is not claimed optimal.

## 5. Full-proof boundary

This density input can replace the corresponding threshold in a separately
reconstructed Poisson stratification. It does not itself prove a new all-
number-field boundary: every other contour and the short-support theta
adapter would still need to be budgeted. In this pass no such global
consequence is promoted. The actual critical fixed-twist signed estimate
and RH remain unproved. The new ramified-factor theorem is logically
independent of the present detector proof; neither result is smuggled
into the other's hypotheses.
