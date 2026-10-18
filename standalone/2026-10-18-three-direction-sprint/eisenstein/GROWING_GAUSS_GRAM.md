# A growing row-Gauss label space, with its Gram hypothesis proved

**PROPOSED source-qualified component theorem. No complete mixed moment or
new zero-free region follows.** This is a ROW projection, not a projection
of the convolution coefficients onto bare Gauss columns.

Let E=Q(omega). Fix the original finite excluded set S, a legal good
primary ray slice, and a nonzero nonnegative smooth annular row weight w.
All constants may depend on these fixed data. Let u run over squarefree
primary ideals in that slice with Nu≈U. For a good sixth-power-free ideal
R define

    v_R(u)=U^(-1/2) w(Nu/U)^(1/2) gamma_1(u) bar chi_u(R).   (1)

Every original nonunit zero is retained. Distinct labels mean distinct
ideals, with prime valuations in {0,1,...,5}. We shall prove the growing
Gram bound rather than assume it.

## 1. A complete squarefree row correlation

Let theta be a finite-order character whose primitive good conductor is
C and let B be a zero-only squarefree mask. For nonprincipal theta,
primitive planar Poisson, followed by divisor expansion of the B mask,
gives for each smooth annular norm profile

    |sum_v theta(v) 1_((v,B)=1) W(Nv/X)|
       << (NC NB X)^epsilon min(X,sqrt(NC)).                (2)

A fixed S-supported conductor and a fixed ray restriction change only the
constant and a finite sum of tests. To see the conductor normalization,
Poisson has prefactor X/NC and primitive Fourier coefficient modulus
sqrt(NC). If X<=NC, the dual lattice count is O(NC/X), giving sqrt(NC).
If X>=NC, the zero frequency vanishes and Fourier decay is stronger.
The trivial count gives X on nonempty annuli. Extra mask divisors replace
X by X/Nb and introduce only a divisor bound; none is divided out.

Insert the exact identity

    1_(u squarefree)=sum_(a^2|u) mu(a), u=a^2 v.

The factor theta(a^2) remains, including its zeros, and has modulus at
most one. The ray condition on v is the original class times [a]^(-2),
one of a fixed finite list. After taking absolute values, (2) implies

    |sum_(u squarefree) theta(u)1_((u,B)=1)w(Nu/U)|
       << (U NC NB)^epsilon
          sum_(Na<<sqrt(U)) min(U/(Na)^2,sqrt(NC))
       << (U NC NB)^epsilon sqrt(U)(NC)^(1/4),              (3)

when NC<=U^2. Indeed split at Na=sqrt(U)(NC)^(-1/4), using the ideal
count O(t) below the split and sum_(Na>A)(Na)^(-2)=O(1/A)
above it. The trivial bound O(U) handles the other conductor range.
All sums include the shared-prime vanishing conditions from a and B.

For R!=R', the nonzero unit part of
`bar chi_u(R) chi_u(R')` has a nonprincipal primitive character.
At a good prime where the two valuations differ, their difference is
nonzero modulo six; the tame Kummer character ramifies there. A fixed
S-supported ray character cannot remove this ramification. Its good
conductor divides rad(RR'), so NC<=NR NR'<=K^2 for labels of norm <=K.
The primes at which the quotient phase becomes principal still impose
its original zero mask rad(RR'); they are not dropped in (3).

## 2. The diagonal and a genuinely growing Gram matrix

Let d_R=||v_R||_2^2. The squarefree lattice count with the coprimality
mask gives

    d_R=c_(S,ray,w) product_(p|R) Np/(Np+1)
              +O_epsilon(U^(-1/2)(UK)^epsilon),             (4)

where c_(S,ray,w)>0. One elementary proof expands the squarefree
condition and the fixed/moving coprimality indicators. The main Euler
factor at a newly deleted prime is
`(1-1/Q)/(1-1/Q^2)=Q/(Q+1)`. The planar lattice error contributes
sqrt(U) sum_(Na<=sqrt(U))1/Na=O(sqrt(U)log U), with the mask's
sum of reciprocal square roots bounded by a prescribed subpower.
After division by U this is (4). Finite primary unit choices are included
in c. In particular d_R>=c_epsilon K^(-epsilon) for large U in the
range used below.

Normalize b_R=v_R/sqrt(d_R), and let G be the Gram matrix of all labels
NR<=K. The Gauss phases cancel in every Gram entry because
|gamma_1(u)|=1 on these squarefree good rows. Equations (3)--(4) give

    G_(R,R)=1,
    |G_(R,R')| <<_epsilon U^(-1/2)K^(1/2)(UK)^epsilon
                                         (R!=R').           (5)

There are O(K) labels. Therefore

    ||G-I|| <= max_R sum_(R'!=R)|G_(R,R')|
       <<_epsilon U^(-1/2)K^(3/2)(UK)^epsilon.                (6)

For every fixed eta>0, if

    K<=U^(1/3-eta),                                         (7)

choose the internal epsilon sufficiently small in terms of eta. For
large enough U the spectrum of G lies in [1/2,3/2]. Thus
`||G||+||G^(-1)||<=7/2`, after that fixed threshold. The conclusion is
uniform over the whole growing label set and all its zero masks.
It is not inferred from pairwise orthogonality at finitely many labels.

## 3. Actual mixed-vector energy on the entire row span

Now take the native matched product

    f_u=M_u(U;W_M) S_u(U^(1/2);W_S),                         (8)

with common character, orientation and height, all d,n powers and shared
primes retained. The pinned original source's inverse amplification has
`e(1)=1` on sixth-power-free rows, hence on the squarefree subset here.
The complete elementary plain mean is U+N^2 at N=U^(1/2). Consequently

    sum_u |M_u|^2 << U^(1+epsilon),
    sum_u |S_u|^2 << U^(1+epsilon),                          (9)

with the fixed polynomial height cost and common-profile seminorms.
The second assertion follows, for example, from the complete primitive
conductor count in `../rational/MIXED_CONDUCTOR_SECTOR.md`. Its auxiliary
positive mean may enlarge the rows before expansion; every power of n
and every shared-prime mask remains.

For ANY bounded flat row multiplier a_u, Cauchy gives

    |U^(-1/2)sum_u a_u M_u S_u|^2 << U^(1+epsilon).          (10)

No Gauss phase cancellation or functional equation is needed for this
fact. That corrects an initially overinterpreted single-vector test.
For b_R, its pointwise multiplier costs d_R^(-1/2)<=K^epsilon, so

    |<f,b_R>|^2 << U^(1+epsilon)K^epsilon.                  (11)

Let V have columns b_R and let
`P=V G^(-1)V*` be the ACTUAL orthogonal row projection. By (6)--(7),

    ||Pf||_2^2
       =<G^(-1)V*f,V*f>
       <=2 sum_(NR<=K)|<f,b_R>|^2
       << U^(1+epsilon)K^(1+epsilon).                      (12)

In particular K=U^(1/5) is inside (7), and the complete growing Gauss
label space costs only

    ||Pf||_2^2 << U^(6/5+epsilon).                         (13)

This is below the representative corner threshold near 1.20783 found
in FEEDBACK_BUDGET.md. It is a summed, uniformly conditioned family,
not just one small overlap. The theorem also pays any smaller fixed-ray
subfamily without assuming that its Gram matrix remains well conditioned
after arbitrary changes: one may simply project onto the full paid span.

Height factors in (9)--(13) have a fixed order before choosing the final
small height exponent, exactly as in the source. This does not permit
arbitrary row-dependent prime coefficients in M or S.

## 4. Comparison and the remaining complement

The row probes (1) are the same family considered in
[rStation paper 10, version 2, Section 8](https://rstation.ai/problems/riemann_hypothesis/papers/10),
where growing Gram conditioning is stated as an additional hypothesis.
The argument above supplies that hypothesis in the range (7), for the
specified fixed row weight and local data. This is an internal proposed
extension, not an independent validation of that paper's analytic theorems.

That paper's continuous-remainder Hilbert--Schmidt cost for labels up to K
is X K^(3/2) at its balanced U=X comparison. At K=U^(1/5) that estimate
costs U^(13/10); it does not by itself justify replacing (12) by a theta
residue form at the desired exponent. Our proof bounds the complete
actual row projection directly and needs no such replacement.

Most importantly, no argument here shows that this span exhausts the
large singular directions. The orthogonal squarefree row component
`(I-P)f`, and every nonsquarefree sixth-power-free physical row, remain.
There is no paid tail theorem for labels R>K, nor a complete spectral
decomposition asserting that only this label space is exceptional.
Those are mathematical gaps, not terms discarded from (12).

Thus the proposed theorem improves the scope of the known-mode test and
closes its explicit Gram gate. It does not establish the complete mixed
mean (1) of MIXED_CONSUMER.md and does not prove a new zeta boundary.

## 5. A full sixth-power-free row variant

The preceding native Gauss probes are supported on squarefree rows. There
is also an independent extension of the Gram mechanism to the entire
physical sixth-power-free row domain. Choose ONE common unit phase q(u)
on those rows, equal to gamma_1(u) on squarefree rows if desired. On
nonsquarefree rows this is a stipulated unit phase, for example a primitive
root-number phase; it is NOT the raw Gauss sum gamma_1(u), which may vanish.
Put

    v_R^(6)(u)=U^(-1/2)w(Nu/U)^(1/2)q(u)bar chi_u(R),
                     u sixth-power-free.                  (14)

The exact expansion

    1_(u sixth-power-free)=sum_(a^6|u)mu(a)

and (2) give the improved off-diagonal correlation

    << (U NC NB)^epsilon
       sum_(Na<<U^(1/6))min(U/(Na)^6,sqrt(NC))
    << (U NC NB)^epsilon U^(1/6)(NC)^(5/12).                (15)

Split at Na=(U/sqrt(NC))^(1/6). This reproduces the complete physical-row
kernel in `../rational/ACTUAL_SIXTHFREE_SECTOR.md`; primes shared with a,
the conductor, or the zero mask still vanish rather than being canceled.
The diagonal density is

    c_(6,S,ray,w) product_(p|R)
          [(1-Q^(-1))/(1-Q^(-6))]
             +O(U^(-1/2)(UK)^epsilon),                    (16)

with positive c. The square-root lattice error is summable because its
a weight is (Na)^(-3). After actual diagonal normalization, (15) and
NC<=K^2 give the Gershgorin bound

    ||G_6-I|| << U^(-5/6)K^(11/6)(UK)^epsilon.              (17)

Hence this full-row family is uniformly conditioned for

    K<=U^(5/11-eta).                                      (18)

The SAME flat-pair argument uses the source's actual sixth-free inverse
moment and the all-element plain norm, so its whole projected mixed
energy is again `U^(1+epsilon)K^(1+epsilon)`. In particular the U^(6/5)
projection budget with K=U^(1/5) also holds on this full row domain.

This is a family of complete row probes with a chosen common unit phase.
It does not identify the nonsquarefree extension with a metaplectic theta
basis, and restricting (14) back to squarefree rows changes its Gram
matrix to the one in Sections 1--2. The full-row projection's orthogonal
complement is still unbounded. Thus (18) does not turn a polynomial
number of probes into coverage of all U physical rows.

## 6. Exact convention fixtures

`gauss_gram_check.py`, in normal Python and under -O, independently
constructs the COMPLETE 37 squarefree primary rows with norms in [128,256),
factors them into actual exterior prime ideals, and computes their sextic
symbols at seven distinct sixth-power-free labels, including powers two,
three and five of a norm-seven prime. All 33 nonunit-zero cases remain.
The Gram matrix is computed exactly over Q(omega). Its seven leading
principal minors are positive rational integers, so finite positive
definiteness is certified without floating eigenvalues. A sixth-power
control retains its coprimality mask instead of being replaced by one.
`GAUSS_GRAM_CHECKS.json` records the exact matrix digest and minors.
These finite conventions checks do not establish the asymptotic Gram
conditioning in (7) or (18); those assertions follow from the analytic
kernel and Gershgorin proofs above.
