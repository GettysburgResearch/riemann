# The actual mixed vector has a small complete Gauss projection resource

**PROPOSED.** This is an unconditional arithmetic projection estimate over
the Eisenstein field, using the classical cubic large sieve. It applies to
the complete synchronized inverse/plain coefficient, including every
powerful part and its shared primes. It does not prove that these Gauss
projections exhaust the bad part of the sextic operator, or bound the
remaining full mixed moment. No zero-free improvement is claimed.

## 1. Complete coefficient and the projection family

Use the actual coefficient c_A from `MIXED_CONDUCTOR_SECTOR.md`:

    c_A=(DN)^(-1/2) nu(A)
          sum_(dn=A) mu(d) W_M(Nd/D) W_S(Nn/N),
    L=DN.                                               (1)

The profiles have fixed annular support and uniformly bounded smooth
seminorms. They include the common detector height. There is no restriction
that d and n be coprime, or that n be squarefree. The original fixed-S
zeros are retained.

Every ideal A factors uniquely as

    A=r*c,  r powerful,  c squarefree,  (r,c)=1,         (2)

where powerful means that every nonzero prime exponent of r is at least
two. The entire prime-power part of A lies in r, not just its radical.
Let gamma_j(c) be the normalized Gauss root of chi_c^j at numerator one,
for j in {1,2,4,5}; on squarefree good c it has modulus one. We permit
either gamma_j or its conjugate in what follows.

For each powerful r choose any bounded multiplicative function eta_r on
the good ideals, `|eta_r(c)|<=1`, a fixed ray slice, and a smooth annular
function H_r from one uniformly bounded family. Put B_r=L/Nr and define

    P_r=sum_(c squarefree,(c,r)=1)
             c_(rc) gamma_j(c) eta_r(c) H_r(Nc/B_r).    (3)

Every factor in (3) is part of the projection; in particular zeros of
eta_r or the coprimality mask are not inverted. The choices of eta_r may
vary with r. They may include moving residue-character twists, finite
ray characters, angular Hecke phases, and coprimality masks. They may
not be arbitrary bounded functions that fail multiplicativity.

The main estimate is

    sum_(r powerful) |P_r|^2
       <<_epsilon (DN)^epsilon
                    [D+N+(DN)^(2/3)].                 (4)

Only r with nonempty original support occur. The sum covers every
powerful label, without a fixed cutoff or a coprime-old-products shortcut.
At D=U,N=U^(1/2), it is `O_epsilon(U^(1+epsilon))`.

## 2. The exact local factorization

Fix r. Since d in (1) is squarefree, all its primes lying over r form
a squarefree divisor d_0 of rad(r). Write

    d=d_0*d_1,    n=n_0*n_1,    n_0=r/d_0,
    d_1*n_1=c,
    (d_1,n_1)=1,   (d_1*n_1,r)=1.                    (5)

Conversely every term in (5) is an original term of (1). In particular
d_0 and n_0 may share primes; those are the actual shared-power terms.
Their product is r exactly. We have

    mu(d)=mu(d_0)mu(d_1),
    nu(rc)=nu(r)nu(d_1)nu(n_1).

For coprime squarefree d_1,n_1 the primitive CRT identity is

    gamma_j(d_1*n_1)
      =gamma_j(d_1)gamma_j(n_1)
           chi_(d_1)(n_1)^j chi_(n_1)(d_1)^j.         (6)

After a finite fixed ray subdivision, sextic reciprocity makes the last
two factors a fixed unit phase times `chi_(d_1)(n_1)^(2j)`.
For the stated j this is a nontrivial cubic character, with either
orientation. The factor eta_r(d_1*n_1) splits exactly. All remaining
factors have absolute value at most a fixed constant.

The noncoprime collision d_1,n_1 is absent because c is squarefree;
it is also exactly a zero of the cubic symbol in (6). It is not replaced
by a principal value. Primes of r remain as separate coefficient masks
on d_1 and n_1 throughout.

For each d_0, the two residual scales are

    D'=D/Nd_0,    N'=N/Nn_0=N*Nd_0/Nr,
    D'N'=L/Nr.                                         (7)

The factor in (1) is `(Nr)^(-1/2)*(D'N')^(-1/2)`.
The extra H_r factor depends smoothly on the product of the two residual
normalized variables. Logarithmic Fourier inversion separates it with
a uniformly bounded L1 measure. Both resulting powers have the same
frequency. Thus applying the next estimate at every common frequency
and then Minkowski pays a uniform constant. No rowwise independent
choice of frequency is introduced.

## 3. The cubic bilinear estimate and summation of every powerful part

The classical cubic large sieve gives, for arbitrary squarefree
coefficient vectors |a_d|,|b_n|<=C with the stated annular lengths,

    |(D'N')^(-1/2) sum_(d_1,n_1)
                  a_(d_1)b_(n_1) chi_(d_1)(n_1)^(2j)|^2
       <<_epsilon (D'N')^epsilon
                    [D'+N'+(D'N')^(2/3)].             (8)

Indeed apply Cauchy in d_1, use its O(D') support size, and then the
cubic large sieve on the n_1 polynomial. Its coefficient square mass
is O(N'). The normalizing product D'N' cancels those two counts.
Bounded fixed ray subdivisions change the constant. The unit-scale
cases are covered by the same estimate after replacing the scales by
comparable numbers at least one; a nonempty fixed annulus ensures this
changes only a fixed constant.

Using (5)--(8) and Cauchy over d_0 gives

    |P_r|^2 <<_epsilon L^epsilon tau(r)^2
       [(D+N)/Nr + L^(2/3)/(Nr)^(5/3)].               (9)

For clarity, before the last simplification the right side is

    C L^epsilon tau(r)/Nr
       sum_(d_0|rad(r))
         [D/Nd_0 + N*Nd_0/Nr + (L/Nr)^(2/3)].

Each of the first two summands is at most respectively D or N, and
there are at most tau(r) choices. This proves (9) with every shared
prime present.

Finally the two series

    sum_(r powerful) tau(r)^2/Nr,
    sum_(r powerful) tau(r)^2/(Nr)^(5/3)               (10)

converge absolutely. Their local factors are
`1+sum_(e>=2)(e+1)^2/(NP)^(s e)`, and the first possible prime term is
O((NP)^(-2s)); take s=1 or 5/3. The prime ideal series therefore
converges. Summing (9) proves (4).

The proof even permits independent bounded multiplicative eta_r at every
label, because the cubic large-sieve constant is independent of the
coefficients. No distribution theorem for those moving twists is needed.

## 4. The exact known sextic bad-vector family

Xu--Sang, [arXiv:2610.17675v1, Section 5.5](https://arxiv.org/html/2610.17675v1#S5.SS5),
construct the squarefree column vector

    lambda_c^(e)=B^(-1) W(Nc/B)(Nc/B)^(-1/2)
                    conjugate(gamma_1(c)) chi_c(-e),  (11)

with their fixed good-prime and ray restrictions; e is one of the six
units. Equation (3) with j=1 is precisely the corresponding UNNORMALIZED
mixed-coefficient Gauss pairing after conjugation, including extra
multiplicative twists and zero masks. At r=1 and B≈L, (8) gives

    |sum_c c_c conjugate(lambda_c^(e))|^2
          <<_epsilon L^(-2+epsilon)
                         [D+N+L^(2/3)].              (12)

For the fixed nonzero W, fixed S/ray, and fixed unit twist in (11),
elementary squarefree ideal counting gives `||lambda||_2^2≈1/L`.
Thus the projection onto the unit-normalized known vector has square
at most

    L^epsilon [D+N+L^(2/3)]/L,

which is `O_epsilon(U^(-1/2+epsilon))` at the corner. This last
normalization statement is for the specified nonzero fixed-data vector;
an arbitrary moving mask can shrink its norm and is not assigned a
uniform lower norm by fiat. The raw bounds (4), (9), and (12) remain
uniform with those masks.

This proves that the actual mixed convolution is poorly aligned with
the explicit known sextic Gauss witness, and supplies a summed resource
for all its canonical powerful-part analogues. It does NOT assert that
the published witness is a complete eigenbasis, that its upper-bound
counterpart is a rank-one operator, or that controlling each such
pairing proves the mixed mean. A full spectral or Poisson decomposition
with a paid remainder would still be required. In particular a growing
family of modes must be summed with its actual measure; pointwise
orthogonality is not an operator norm estimate.

There is a further range caveat at our corner. The explicit vector (11)
is constructed in a row-length-larger-than-column-length range. For the
mixed matrix with rows U and columns L=U^(3/2), the applicable Xu--Sang
construction has the matrix TRANSPOSED: its explicit Gauss vector lives
on length U, and the induced bad column is a Gauss-character transform
on length L, rather than the bare gamma_1(A) in (12). The estimates
above do not by themselves control that induced vector. The separate
`TRANSPOSED_GAUSS_MODE.md` addresses its actual row-side pairing by
reflecting the plain factor, with its additional source-qualified
inverse-moment dependency stated explicitly.

## Primary interfaces and checks

The cubic large sieve in (8) is the n=3 case of
[Blomer--Goldmakher--Louvel, arXiv:1112.1650v1, Theorem 1.3](https://arxiv.org/pdf/1112.1650),
PDF page 4, with both indices squarefree and fixed bad primes. The primary
PDF was read directly. Its primitive-character convention is reconciled
with the raw zero-extended symbols by the fixed ray subdivisions; for
the squarefree cubic indices, shared-prime values are zero in both.
The newer paper's Section 5.5 was also read directly for the exact
coefficient (11); its squarefree-row transfer may change that vector,
so no assertion about that changed vector is inferred here.

All arithmetic transformations in this proof are exact ideal identities.
The estimate is analytic and uses the stated infinite cubic sieve; no
finite experiment is offered as proof of it.
