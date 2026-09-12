# Exact finite-theta data do not propagate the cumulant sign

Date: 2026-09-12. Continuation of PR #842.
Parent: 4558dce9cb981a2e8c0e3e058b21a5b17f6a1cf5.
Status: **PROPOSED COMPONENT PROOF; independent mathematical review required.**
**The native all-degree Hankel inequality and RH remain unproved.**

The requested completion was attempted by propagating the certified cumulant
forms using source positivity, the functional equation, endpoint normalization,
and approximation. This note does not accomplish that propagation. It constructs
an explicit family showing why those properties, even with exact agreement of
arbitrarily many native moments, cannot be the whole argument.

The counterfunctions below are NOT xi. They use a changed differential source.
In particular they do not retain the ordinary Euler product, the unmodified
second-order theta differential identity, or confinement of ALL zeros to the
critical strip. Some additional zeros are deliberately inside that strip; others
need not be. No off-line zero of zeta is asserted.

The new point relative to the earlier changed-source examples is simultaneous
EXACT finite-moment and endpoint preservation, unchanged complete real divisor,
positive density, and an explicit whole-line smallness certificate. General
Fourier multiplier constructions, Schur complements, and moment criteria are
classical; no broad originality or priority claim is made.

## 1. The exact native obligation

Use the parent's unstandardized source and entire completion:

    Xi(z)=xi(1/2+iz)=integral_R phi(t) exp(izt)dt,
    phi(t)=sum_(n>=1) exp(t/2-Q_n) P_0(Q_n),
    Q_n=pi n^2 exp(2t),  P_0(Q)=4Q^2-6Q,
    Z=Xi(0)>0,  w=phi/Z.

Jacobi inversion makes phi even. On t>=0 every summand is positive. The full
series is smooth, with double-exponential tails after every fixed derivative.
In particular all exponential moments and all integrations by parts used below
are valid. These classical source facts are reconstructed in the parent theta
papers. Neither their operator determinant nor their metric assertions is used.

For the native cumulants put

    q_n=(-1)^(n+1) kappa_(2n)(w)/[2(2n-1)!],
    H_d=(q_(i+j+2))_(0<=i,j<=d).

The parent proves that positivity of every H_d is RH-equivalent using the
summable genus-zero divisor. Its nine-dimensional certificate establishes only
G_9=(q_(i+j+1))_(0<=i,j<9)>0 and J_9=H_8>0.

There is a direct extension equation. If H_d>0, write

    H_(d+1)=[H_d b; b^T c],
    b_i=q_(i+d+3), i=0,...,d,  c=q_(2d+4).

Completing the square gives, for real x,t,

    [x;t]^T H_(d+1)[x;t]
      =(x+t H_d^(-1)b)^T H_d(x+t H_d^(-1)b)
        +t^2[c-b^T H_d^(-1)b].                            (1)

Thus the next sign is exactly the sign of this Schur remainder. For the first
extension of H_8 the missing scalar is

    q_20-(q_11,...,q_19) H_8^(-1)(q_11,...,q_19)^T.        (2)

A proof that (2) is nonnegative would establish that one extension, not the
entire tower. If a later block is only semidefinite, the range condition and
Moore--Penrose version replace the inverse; they cannot be suppressed.

The finite Newton recursion defining the q_n from theta moments is an identity,
not a lower bound for (1). Ordinary positive probability moment Grams are not
these nonlinear cumulant Grams. The attempted positive-renewal interpretation
of that recursion does not establish a positive kernel: its alternating
convolution terms and the negative Schur term remain. No renewal-sign theorem
is claimed here.

## 2. General construction with exact moment and endpoint preservation

Fix an EVEN integer m>=2 and a real eta with 0<eta<1/2. Define

    f(v)=v^m(v+1/4),
    A=D^(2m)(D^2-1/4),                 D=d/dt.

Because m is even, the Fourier symbol of A is -f(z^2). For a positive real R
put

    z_R=R+i eta,  c_R=f(z_R^2),
    a_R=Re(1/c_R),  b_R=1/|c_R|^2.

For all sufficiently large R, c_R has positive real and imaginary parts,
a_R>0, and b_R>a_R^2. The estimates

    |c_R|>=R^(2m+2),
    0<a_R<=R^(-2m-2),  b_R<=R^(-4m-4)                   (3)

hold once its real part is positive. Indeed |z_R^2|>=R^2 and
Re(z_R^2+1/4)=R^2+1/4-eta^2>=R^2. Its argument is positive and tends to zero.
For example R>=4(m+1)eta together with R>=1 suffices: bound the arguments
of z_R^2 and z_R^2+1/4 by 2eta/R and sum them.

Define the CHANGED source

    phi_R=phi+2a_R A phi+b_R A^2 phi.                      (4)

**FJ1.** For each fixed even m and fixed eta, for all sufficiently large R,
phi_R is strictly positive, even, smooth, and has double-exponential tails.
It has the same total mass Z, moments through degree 2m-1, and transforms at
h=+1/2 and h=-1/2 as phi. Moreover, for every fixed j>=0 and c>=0,

    integral_R exp(c|t|) |D^j(phi_R-phi)(t)|dt ->0.         (5)

Its transform satisfies the exact identity

    Xi_R(z)=Xi(z) B_R(z^2),
    B_R(v)=(1-f(v)/c_R)(1-f(v)/conj(c_R))
          =1-2a_R f(v)+b_R f(v)^2.                       (6)

For every real v, B_R(v)>0. In particular Xi_R has exactly the same real
zeros, multiplicities and signs as Xi. It also has the prescribed additional
zeros R+i eta, R-i eta, -R+i eta, -R-i eta.

The entire function xi_R(s)=Xi_R(-i(s-1/2)) obeys

    xi_R(s)=xi_R(1-s),    xi_R(0)=xi_R(1)=1/2.             (7)

It is an order-one entire function, as is xi, but is not xi.

### 2.1 Positivity is a complete source inequality, not a sampled test

One proof of existence in FJ1 uses the differentiated tail. For any fixed
nonnegative integer j,

    phi^(j)(t)/phi(t)=(-2pi)^j exp(2jt)(1+O_j(exp(-2t)))
                                                        (t->+infinity).

This follows by differentiating the n=1 term and bounding the whole n>=2
series. Reflection handles the other end for even j. Therefore

    g=A phi,  h=A^2 phi

are even, smooth, and both g/phi and h/phi tend to +infinity at the two ends.
Their negative parts have finite suprema C_g,C_h. Consequently, for ALL real t,

    phi_R(t)>=phi(t)[1-2a_R C_g-b_R C_h].                  (8)

Equations (3) make the bracket larger than 1/2 for large R. This proves
strict positivity on the entire line; positivity only near the center would
not suffice. Section 3 supplies fully rational bounds C_g,C_h for the literal
infinite theta series and an explicit R, avoiding an unevaluated tail threshold
in its numerical example.

### 2.2 Exact finite data and the entire transform

Every derivative appearing in phi_R-phi has order at least 2m. For k<2m,
integration by parts gives

    integral t^k (phi_R-phi)(t)dt=0.                      (9)

This includes total mass. Set w_R=phi_R/Z; no new normalizer is needed. Raw
moments, cumulants and their fixed polynomial combinations through that order
are identical, not merely close. The variance and hence standardization also
remain unchanged.

For a complex h, integration by parts gives

    integral exp(ht) A phi(t)dt=h^(2m)(h^2-1/4) M_phi(h).

The factor vanishes at h=+/-1/2; its square handles A^2. This proves the endpoint
part of (7). Taking h=iz proves (6), including the sign from m EVEN. All parameter
compact sets are dominated by the full differentiated theta tails. Thus the
identities hold throughout C, not just as formal Taylor series. Equation (5)
follows immediately from the finite linear combination in (4) and (3).

For real v,

    B_R(v)=(1-a_R f(v))^2+(b_R-a_R^2) f(v)^2>0.           (10)

If f(v)=0 the value is one; otherwise the second summand is strictly positive.
At z=z_R the first factor in (6) vanishes exactly. Reflection and conjugation
supply the other three roots. Their images in the s-plane have real parts
1/2-eta and 1/2+eta. No root finder or original zeta-zero input is used.

The polynomial multiplier has additional zeros, generally outside the critical
strip as well. This is explicitly NOT a new zeta function obeying its full
arithmetic and zero-location conditions. Multiplying an order-one nonzero
entire function by a fixed polynomial preserves its order. Its real divisor
is unchanged because of (10), including any multiple real zeros.

## 3. Explicit native bounds for the current finite certificate

The following calculation proves whole-source positivity using rational
polynomials only. It does not evaluate phi numerically or use a zero list.

Define its derivative polynomials by

    P_(j+1)(Q)=2Q P_j'(Q)+(1/2-2Q)P_j(Q).                 (11)

Then phi_n^(j)(t)=exp(t/2-Q_n)P_j(Q_n). For m=20 put

    g(Q)=P_42(Q)-(1/4)P_40(Q),
    h(Q)=P_84(Q)-(1/2)P_82(Q)+(1/16)P_80(Q).              (12)

These are the term polynomials of A phi and A^2 phi. Their degrees are 44 and
86, with strictly positive leading coefficients. For any rational polynomial
p(Q)=sum_(k=0)^d p_k Q^k of positive leading coefficient, set

    L_p=max(3,1+ceil(sum_(k<d)|p_k|/p_d)),
    C_p=(1/18) sum_(p_k<0) |p_k| L_p^k,
    U_p=sum_(k=0)^d |p_k| (4k)^k, with 0^0=1.             (13)

For Q>=L_p the leading term dominates the absolute sum of all lower terms;
thus p(Q)>=0. For 3<=Q<=L_p its negative part is at most 18 C_p. Since
P_0(Q)=4Q^2-6Q>=18 for Q>=3, this proves

    p(Q)>=-C_p P_0(Q),     Q>=3.                         (14)

Every Q_n(t)>3 on t>=0. Multiply (14) by exp(t/2-Q_n) and sum the COMPLETE
series. Evenness extends the result to all t:

    A phi>=-C_g phi,    A^2 phi>=-C_h phi.                (15)

No number of explicitly computed theta indices is required for (15).

There is also a uniform whole-line envelope. For t>=0,

    t^2+t/2 <=(3/2)exp(2t)<=Q_n(t)/2,
    sum_(n>=1)exp(-Q_n(t)/4)<1.

The second inequality follows from Q_n>3n^2, n^2>=n and exp(3/4)>2. Splitting
the residual exponential once more and maximizing each monomial gives

    exp(t^2)|sum_n exp(t/2-Q_n)p(Q_n)|<=U_p.              (16)

For phi itself, keeping the negative -6Q term discarded only for the upper
bound gives the sharper elementary bound

    0<phi(t)<64 exp(-t^2).                               (17)

Indeed max_(Q>=0)4Q^2 exp(-Q/4)=256/e^2<64, and the same complete geometric
sum pays the rest. Reflection handles negative t.

**FJ2, exact example.** Choose

    m=20, eta=1/4, R=2^324,
    c_R=[(R+i/4)^2]^20[(R+i/4)^2+1/4].                   (18)

Compute (11)--(13) with exact fractions. The accepting checker proves

    2R^(-42) C_g+R^(-84) C_h <2^(-72),
    2R^(-42) U_g+R^(-84) U_h <2^(-13231).                (19)

It also checks Re(c_R)>0, Im(c_R)>0 and all identities in (6). Therefore

    phi_R(t)>(1-2^(-72))phi(t)>0,
    |phi_R(t)-phi(t)|<2^(-13231)exp(-t^2)                 (20)

on the ENTIRE real line. In particular phi_R<65 exp(-t^2)<256 exp(-t^2),
so even the parent's deliberately loose Gaussian source envelope is retained.
The parameters are exact rationals/Gaussian rationals; the large height is not
an approximate numerical zeta ordinate.

Every moment of degree <=39 is unchanged, including all moments through 36
used by G_9 and J_9. Thus those exact two matrices, every pivot, and every
arithmetic conclusion using only their input moments are identical for w_R.
This is conditional only on the original certificate for the original matrices:
we did not rerun that numerical integration in this pass. The equality of their
entries for the changed source follows from (9), not numerical agreement.

Nevertheless xi_R has zeros at 1/4+iR and 3/4+iR, and their conjugates.
They are CHANGED-SOURCE zeros. The example does not assert that xi has such
zeros or is close relative to xi near those high complex points. Entire
compact convergence does not provide an all-height relative error bound.

### 3.1 The unseen cumulant defect is not just a normalization effect

For v near zero, log B_R(v)=O(v^20), so q_n(w_R)=q_n(w) for 1<=n<=19.
Its first correction is q_20(w_R)-q_20(w)=10a_R>0. Thus even the first new
individual cumulant moves in the positive direction; this is not the same
as positive semidefiniteness of the whole future tower.

More generally, for even m the polynomial f(v)=v^m(v+1/4) has only real
critical points: f'(v)=v^(m-1)[(m+1)v+m/4]. Since c_R is nonreal,
f(v)=c_R and f(v)=conj(c_R) have 2(m+1) distinct nonreal roots in v.
They form m+1 conjugate pairs, giving m+1 distinct nonreal Xi_R quartets.
All have nonzero inverse-squared nodes. The parent's complete index proof
applies to Xi_R too: multiplication by this fixed polynomial preserves genus
zero of Xi_R(sqrt(v))/Xi_R(0) and summability. Hence the negative indices of
its cumulant matrices eventually reach at least m+1. For (18) that number
is 21. No witness degree or location of a first negative pivot is computed.
Coincidence with an original divisor does not erase any of these distinct
new locations; the existing divisor, whether real or nonreal, cannot cancel
zeros of an entire product.

## 4. Every prescribed finite cumulant prefix can be preserved

Given any d>=0, choose even m=2d+4. Then 2m-1=4d+7, exceeding the source
moment order 4d+4 needed for H_d. FJ1 yields positive even densities arbitrarily
close to the native theta density in every fixed exponentially weighted
C^j-integral seminorm, with exactly the same H_0,...,H_d and endpoints, but
with prescribed nonreal roots at arbitrarily high R+/-i eta.

This statement does not require H_d to be positive; whenever a native finite
positivity certificate exists, the changed source inherits it EXACTLY.
It rules out a conclusion based solely on finitely many such entries plus the
listed shape/normalization/continuity properties. It does not rule out a
source-specific proof using the full literal theta identity or Euler factors.

There is a further optional extension. Any finite collection of real safe-point
MGF derivative values can also be preserved. Choose a real even differential
polynomial

    A=D^(2m) product_l (D^2-a_l^2)^(r_l),  a_l>0,

with m+sum r_l ODD. Then its Fourier symbol is -f(z^2), where
f(v)=v^m product_l(v+a_l^2)^(r_l). Use the same construction (4), choosing R
large enough. The leading derivative of A has positive coefficient and even
order; A^2 does as well, so the whole-line lower-bound argument still applies.
At h=+/-a_l, the transform correction has a zero of multiplicity r_l, preserving
the indicated derivative values. Polynomial moments below 2m are unchanged.
The real polynomial f has only nonpositive real roots, so its critical values
are real and the same nonreal-root argument applies. This is a finite-constraint
statement, not preservation of the whole analytic germ at any point. The
identity theorem would forbid the latter for a genuinely changed function.
The numeric example and executable controls use only a_1=1/2,r_1=1.

## 5. What was tried, what is new, and what remains missing

The direct extension attempt was to combine the finite G_9/J_9 certificate
with the Newton recurrence and a positive-kernel or continuity argument to
pay every later Schur remainder. No such positive-kernel representation or
all-degree lower bound was obtained. Equations (4)--(20) show that the
finite-data/shape portion of that attempt is insufficient, even with exact
rather than approximate data and with exponentially small whole-line error.

The theorem here is not a refutation of the native positivity target. The
counterfunctions use A phi and A^2 phi instead of phi, have a different
Dirichlet/arithmetic completion, and can have additional zeros outside the
critical strip. They are not pair-ferromagnetic Lee--Yang laws. They cannot
replace xi in any source-sensitive premise of the repository. Their retained
real divisor is not a newly verified zero census.

The actual unproved line is still

    sum_(i,j=0)^d c_i c_j q_(i+j+2)(w)>=0
    for every d>=0 and every real coefficient vector c.   OPEN

A proof of OPEN would finish by the parent's tail-complete witness theorem.
Neither this perturbation theorem nor the block identity (1) establishes OPEN.
This pass produces no new native Hankel order, Ising moment match, spectral
sign, or native zero-free region. Reviewers are asked to review the supplied
component theorem, not to fill the missing RH proof.

## 6. Sources and executed scope

The full supplied 23,854-byte parent proof was read and its Git blob checked:
`b5c071afbac25cc27c4382306b4e8e26debb573c`. Its remote upload is confirmed at
`4558dce9cb981a2e8c0e3e058b21a5b17f6a1cf5`. The PR metadata snapshot initially
still reported its preceding head; the direct branch ref and file read resolved
that mismatch. Prior files and certificates are not modified or reclassified.

Recent #863 and #864 PR descriptions were inspected for overlap, not their full
proofs imported: #863 has a fourteen-moment interacting construction with an
explicit later mismatch; #864 rejects a different, stronger complete-Bernstein
representation. Neither supplies OPEN. #839/#841 remain the credited antecedents
of the native trace-Hankel criterion; no new criterion is claimed here.

External orientation: NIST DLMF 25.4 fixes the standard completion and reflection
convention. Zhang, On Power Sums of Positive Numbers, arXiv:1510.03420v2, is
prior literature for power-sum positivity criteria. Newman--Wu,
arXiv:1901.06596v2, surveys the distinct Lee--Yang/closure programme. Only their
HTML definitions/abstracts were read in this pass; no external proof audit is
claimed and the perturbation proof uses no new theorem from those abstracts.

The checker reconstructs rational derivative polynomials, the full-source
bounds (19), Gaussian-rational root/normalization identities, and finite
moment/Schur controls. It does not numerically evaluate theta or its derivatives,
compute actual zeta zeros, or machine-prove the analytic integrations by parts.
Its role in FJ2 is to certify the exact polynomial arithmetic inside explicit
paper-proved bounds. See VALIDATION.md for commands and limitations.
