# From prime-coefficient rigidity to determinant completions

**Status:** PROPOSED component proofs and a conditional hierarchy transfer.
No improved native moment exponent, zero-free boundary, or RH proof is claimed.
The proof and diagnostic have one author; independent review is required.

**Scope:** the fixed Eisenstein field K=Q(omega); all nonzero element rows;
fixed finite coefficient data and fixed moment orders. The nonabelian
extension in Section 4 assumes a larger explicitly defined family of probes,
not merely the finite-order Hecke twists of the original problem. Section 5
is conditional, and is stated only for abelian determinant data.

**Starting source:** PR #935 at a7a7fad2c5fa1929c7e04570cde4188e3191b071,
MATHEMATICS.md, especially its square-convolution comparison and finite-ray
rigidity theorem. This note generalizes that theorem's bound |a|<=1 and
connects the resulting discrete coefficient class to actual determinant
coefficients. Fourier integrality, Euler-factor comparison, and determinant
identities are classical mechanisms, not claimed as newly discovered tools.

## 1. Set-up and why the small-prime exclusion is explicit

Let G be a fixed finite abelian quotient of a ray class group of K, let g(n)
be its ideal class map, and let a:G->C satisfy |a(g)|<=R for a fixed R>=1.
Let S include the modulus primes, primes above 2 and 3, and every prime ideal
p with Np<=4 R^2. Additional original exclusions may be included. All sums
use ideals prime to S. Enlarging S here is an explicit hypothesis, not an
unproved adapter from a moment estimate with another excluded set.

The large fixed cutoff makes all local linear factors nonzero in a fixed
neighborhood of s=1 and controls both directions of the later completion at
Re(s)>1/2. This issue was absent at |a|<=1 in #935. Section 6 exhibits a
small-prime failure of the unrestricted comparison kernel.

On squarefree ideals define

    f_a(n) = product_{p|n} a(g(p)),   f_a(1)=1,

and set f_a(n)=0 on nonsquarefree ideals. For eta in the dual group G^,
put

    T_{eta,u}(D) = sum_n f_a(n) conjugate(eta(g(n))) chi_n(u) W(Nn/D),
    M_{eta,2k}(D,H) = sum_{0<Nu<=H} |T_{eta,u}(D)|^(2k),
    c_eta = |G|^(-1) sum_g a(g) conjugate(eta(g)).

W is fixed, smooth, nonzero, nonnegative, and supported on [alpha,beta]
inside (0,infinity). The sextic symbols are the original ones. Every
nonunit value stays zero. Ideals, including distinct conjugate ideals with
the same norm, are never identified by their norms.

The elementary bound R^omega(n)<<_{R,epsilon}(Nn)^epsilon will be used.
For example, separate the finitely many primes of norm below R^(1/epsilon);
on all others each local factor R is at most (Np)^epsilon. Squarefreeness
bounds the contribution of the separated finite prime set by a constant.

## 2. A bounded-rank necessity theorem

### Theorem 2.1 (finite-ray rank rigidity)

Fix k>=1 and 0<h<6k/5. If, for every eta in G^ and every epsilon>0,

    M_{eta,2k}(D,D^h) <<_{eta,epsilon} D^(h+k+epsilon),             (2.1)

then there are nonnegative integers m_eta such that

    a(g) = -sum_eta m_eta eta(g),
    r := sum_eta m_eta <= floor(R).                             (2.2)

Thus -a is the character of an actual representation of G of dimension r,
not a virtual character with coefficients of both signs. Rank zero is
allowed. Conversely (2.2) removes the particular singularity-at-one
obstruction proved below; it does NOT prove (2.1).

More specifically, an individual coefficient c_eta outside Z_{<=0} forces

    limsup_{D->infinity} log(1+M_{eta,2k}(D,D^h))/log D
        >= 2k+h/6                                               (2.3)

for every fixed h>0 and k>=1.

#### Proof

For Re(s)>1 the Euler series of the principal row is

    F_eta(s) = product_{p not in S}
           (1+a(g(p)) conjugate(eta(g(p))) (Np)^(-s)).

Fourier inversion and cancellation of the first-degree local logarithms give

    F_eta(s) = E_eta(s) product_psi L^S(s,psi conjugate(eta))^(c_psi).
                                                                    (2.4)

This is first an identity on Re(s)>1 with consistent Euler logarithms.
The remainder's local logarithms are O_R((Np)^(-2 Re(s))), normally
convergent on compact subsets of Re(s)>1/2. Our fixed cutoff guarantees
that none of its local numerator or denominator factors vanishes there.
In particular E_eta has a holomorphic nonzero germ at one.

The classical fixed-field inputs are that the principal Hecke L-function
has a simple pole at one and every nonprincipal finite-order Hecke
L-function is holomorphic and nonzero there. Therefore, on a sufficiently
small slit neighborhood of one,

    F_eta(s) = (s-1)^(-c_eta) U_eta(s),   U_eta(1)!=0.             (2.5)

A nonzero holomorphic germ has an integer nonnegative vanishing order.
Its logarithmic derivative shows that (2.5) can be holomorphic across one
only when c_eta is a nonpositive integer. This includes exclusion of
positive integral c_eta, which gives a pole, not a branch point.

If T_{eta,1}(D)=O(D^(1-delta)) for any delta>0, its scale Mellin integral
would be holomorphic for Re(s)>1-delta. On Re(s)>1 it equals
W_hat(s) F_eta(s). The sums vanish for D<1/beta, so there is no small-scale
integrability problem. Since W_hat(1)>0, this contradicts (2.5) whenever
c_eta is illegal. Thus for every delta>0 there are arbitrarily large D
with |T_{eta,1}(D)|>D^(1-delta).

To pass to the actual row moment, put Y=D^(h/6). Each prime ideal l outside
S with Y/2<Nl<=Y has a generator ell because K has class number one, and
gives a distinct row u=ell^6 with Nu<=D^h. On this row

    chi_n(ell^6) = 1_{(n,l)=1}.

The omission of multiples of l costs at most

    |T_{eta,ell^6}(D)-T_{eta,1}(D)|
       << D^epsilon (D/Nl+1),                                  (2.6)

by ideal counting; the difference is zero if Nl>beta D. Fix delta and
epsilon small enough that delta+epsilon<min(h/6,1). On the large-value
scales just obtained, (2.6) is less than half the principal value for
sufficiently large D. The fixed-field prime ideal theorem supplies
>>Y/log Y distinct copying prime ideals. Positivity of the full moment
then gives

    M_{eta,2k}(D,D^h) >> D^(2k(1-delta)+h/6)/log D.

Taking the upper limit and then delta down to zero proves (2.3). This is
the #933/#935 singularity-and-copying mechanism, with divisor-bounded
rather than unit-bounded coefficients. It does not require a moving-ray
prime ideal theorem.

Under (2.1), the inequality h<6k/5 excludes every illegal c_eta.
Write c_eta=-m_eta, m_eta in Z_{>=0}, and use Fourier inversion. At the
identity element e, every eta(e)=1, so

    r=sum_eta m_eta=-a(e)<=|a(e)|<=R.

This proves (2.2). In particular the rank bound is R, not R^2. QED.

### Example 2.2

For G=C2 with nontrivial character epsilon, the rank-two pattern

    a=-(1+epsilon)

has values -2 and 0. It doubles the negative coefficient on one ray class
and removes primes in the other. It passes the necessary integrality test.
It is not a theorem that its native moments are small. A continuous path
of bounded prime patterns satisfying (2.1) at every point must be constant,
because only finitely many tuples (m_eta) with sum at most floor(R) exist.
No uniformity of the constants along that path is needed for this statement.

## 3. Complete the rigid prime data, with an explicit two-way norm bound

Let rho be a fixed unitary representation of any finite group of dimension
r>=1. At each good prime p let zeta_{p,1},...,zeta_{p,r} be the eigenvalues
of rho(g_p). They have modulus one. This section is purely local and does
not need the g_p to be Frobenius elements.

Define the local polynomials

    P_p(z) = 1 - tr(rho(g_p)) z,
    D_p(z) = det(I-z rho(g_p))
           = product_{j=1}^r (1-zeta_{p,j} z).

Let f be the multiplicative coefficient function with factors P_p, and c
that with factors D_p. Thus f is squarefree-supported, while c(p^e) is
(-1)^e times the trace on the e-th exterior power, and is zero for e>r.
Their coefficients at every retained prime are exactly the same.

Let kappa and iota be multiplicative coefficient functions defined by

    sum_e kappa(p^e) z^e = D_p(z)/P_p(z),
    sum_e iota(p^e) z^e = P_p(z)/D_p(z).                          (3.1)

Both start with 1+0z; their coefficients are supported on ideals with no
prime of exponent exactly one. They are exact Dirichlet-convolution
inverses. No signs in either series are discarded in these identities.

### Theorem 3.1 (critical-line comparison)

Suppose S includes every prime ideal with Np<=4r^2. For sigma>1/2,

    sum_n |kappa(n)| (Nn)^(-sigma) <= zeta_K(2sigma)^(4r^2),
    sum_n |iota(n)| (Nn)^(-sigma) <= zeta_K(2sigma)^(4r^2).       (3.2)

For any original exclusion Q, finite nonnegative row measure w, fixed
unitary multiplicative twist nu, compact test W, and p>=1, form the two
physical sums with coefficients f and c, multiplied by nu(n) chi_n(u),
with symbols extended completely multiplicatively including their zeros.
For the SAME w and Q at every shorter column scale, define

    E_f(sigma,X) = sup_{1/beta<=D<=X} D^(-sigma)||T_f(D)||_Lp(w),

and similarly E_c. Then both inequalities

    E_c <= zeta_K(2sigma)^(4r^2) E_f,
    E_f <= zeta_K(2sigma)^(4r^2) E_c                             (3.3)

hold. At the critical normalization sigma=1/2, both inequalities hold
instead with a factor

    O_{K,r,beta}(log(2+X)^(4r^2)).                              (3.4)

The exponent 4r^2 is a convenient uniform bound, not asserted optimal.
For fixed 2k, (3.4) gives logarithmic, not power, loss in the moment.

#### Proof of the coefficient bound

Write a_p=-tr rho(g_p), so |a_p|<=r and
D_p(z)=1+a_p z+sum_{j=2}^r d_j z^j, with |d_j|<=binom(r,j).
For 0<t<=1/(2r), the sum of absolute nonconstant coefficients of D_p/P_p,
evaluated at t, is bounded by

    U_r(t)/(1-rt),
    U_r(t)=(1+t)^r-1-rt.                                      (3.5)

For P_p/D_p the corresponding bound is

    U_r(t)(1-t)^(-r).                                         (3.6)

Indeed subtract 1 in each ratio; the numerator then begins at degree two.
For (3.6), the coefficient absolute series for D_p^(-1) is bounded by
(1-t)^(-r). Both bounds preserve the cancellation of the linear term.

Since rt<=1/2, Taylor's estimate yields
U_r(t)<=exp(1/2) r^2 t^2/2. Also (1-rt)^(-1)<=2 and
(1-t)^(-r)<=exp(rt/(1-t))<=exp(1). Each of (3.5),(3.6) is therefore
at most 4r^2 t^2. Put t=(Np)^(-sigma). The prime cutoff guarantees the
required range. Multiplying local absolute series, then using

    sum_p (Np)^(-2sigma) <= log zeta_K(2sigma),

proves (3.2) by absolute convergence and monotone limits.

#### Proof for the physical sums

Coefficientwise convolution gives the finite identities

    T_c(D,u) = sum_{(d,SQ)=1} kappa(d) nu(d) chi_d(u) T_f(D/Nd,u),
    T_f(D,u) = sum_{(d,SQ)=1} iota(d) nu(d) chi_d(u) T_c(D/Nd,u). (3.7)

There is no coprimality condition between d and its residual ideal.
Every summand with D/Nd<1/beta vanishes. Multiplication by nu(d)chi_d(u)
is a contraction on Lp(w). Minkowski and (3.2) prove (3.3).

For the critical line use delta=1/log(2+beta X), enlarged harmlessly on
bounded X. The finite coefficient mass obeys

    sum_{Nd<=beta X} |kappa(d)|/sqrt(Nd)
      <= (beta X)^delta zeta_K(1+2delta)^(4r^2),                 (3.8)

and likewise for iota. Ideal counting gives zeta_K(1+v)<<_K 1+1/v for
v>0. Since (beta X)^delta<=e when beta X>=1, (3.8) proves (3.4).
All constants are independent of the actual rows, their nonunit masks,
Q, and nu. This does not compare two different physical heights. QED.

### Corollary 3.2 (abelian determinant model)

For the pattern in Theorem 2.1, take
rho=direct_sum_eta eta^(direct_sum m_eta). On Re(s)>1 the completed
physical Euler series is exactly

    sum_n c(n) nu(n) chi_n(u) (Nn)^(-s)
       = product_eta L^{SQ}(s,eta nu chi_u)^(-m_eta),             (3.9)

Here the L-notation means the Euler product with good-prime values
eta(g(p)) nu(p) chi_p(u), with the source's fixed ray conventions and
literal Euler deletions. No reciprocity normalization is being changed.
Equation (3.9) is an Euler-factor identity. It is not an assertion of
convergence or absence of poles on the critical line. Zeros of the underlying L-functions can still produce poles of the
reciprocal product.

For the C2 example, the local completion is

    class epsilon=+1:  1-2z  -->  1-2z+z^2,
    class epsilon=-1:  1     -->  1-z^2.

Both have the correct unchanged prime coefficient. The inserted square
terms are essential. The completed series is the product of two native
inverse Hecke series. It is not the inverse of their average.

## 4. Nonabelian version: the additional probes are part of the hypothesis

This extension gives the representation-theoretic meaning of the integrality
argument. It is NOT obtained from the original one-dimensional twist
hypothesis alone.

Fix a finite Galois extension F/K with group G, a central function a on G
with |a(g)|<=R, and let d_max=max_{tau in Irr(G)} dim(tau). Enlarge S to
include the ramified primes and all Np<=4(R d_max)^2. For each irreducible
tau define a squarefree coefficient function by the prime values

    b_tau(p) = a(Frob_p) conjugate(chi_tau(Frob_p)).

Multiply these coefficients by the original sextic chi_n(u) and W(Nn/D).
The product over primes of character values is intended; it is not the
trace of one group element associated to the whole ideal.

### Theorem 4.1

If the resulting physical moments have diagonal size at one k and
0<h<6k/5 for EVERY irreducible probe tau, then

    a(g) = -sum_{tau in Irr(G)} m_tau chi_tau(g),
    m_tau in Z_{>=0},   sum_tau m_tau dim(tau) <= floor(R).       (4.1)

Thus -a is the character of a genuine finite-dimensional representation.
The two-way comparison of Section 3 applies to its determinant completion.
No Artin holomorphy conjecture is assumed or proved.

#### Proof

For any central b, expansion in irreducible characters and first-degree
Euler cancellation factor its squarefree Euler series locally as

    E_b(s) product_rho L^S(s,rho,F/K)^(<b,chi_rho>).

Only the local behavior at one is needed. Here is the reduction to the
classical inputs, rather than an invocation of Artin's conjecture.
Brauer induction writes a virtual character rho as an integral sum
sum_j n_j Ind_{H_j}^G psi_j of one-dimensional subgroup characters.
Artin formalism identifies its L-function with the corresponding product
of finite-order Hecke L-functions over the fixed intermediate fields.
Those have order -1 at one for the principal character and zero for a
nonprincipal character. Frobenius reciprocity therefore gives

    ord_{s=1} L(s,rho) = -sum_j n_j 1_{psi_j=1}
                       = -<chi_rho,1_G>.                       (4.2)

In particular nontrivial irreducible Artin L-functions have holomorphic
nonzero germs at one, irrespective of their behavior elsewhere.
Brauer induction, Artin formalism, and the quoted Hecke facts are named
classical inputs; (4.2) explains their exact use.

For b=b_tau the exponent of the principal singularity is
<b_tau,1>=<a,chi_tau>. The argument of Section 2 applies verbatim, with
coefficient bound (R dim(tau))^omega(n), to force every <a,chi_tau> to be
a nonpositive integer. Irreducible characters form an orthonormal basis
of central functions, so Fourier inversion gives (4.1). Evaluation at
the identity gives the displayed dimension bound. QED.

For S3 the standard irreducible character on the identity, transpositions,
and three-cycles is (2,0,-1). Its negative (-2,0,1) is allowed by (4.1).
The three determinant factors are respectively

    (1-z)^2,   1-z^2,   1+z+z^2.

This is a finite character-table illustration. No assertion is made that
its native physical moment bound has been established. In the nonabelian
case Section 5's product of rank-one Hecke sums need not be available.

## 5. Conditional hierarchy transfer in the abelian case

The completion is useful only if its structured coefficients can be
estimated. This section states exactly what follows from native moment
inputs, with the moment-order cost visible.

Let rho=eta_1 direct_sum ... direct_sum eta_r, r>=1, and let c be its
determinant coefficient function. Coefficientwise,

    c=(mu_K eta_1)*...*(mu_K eta_r),                             (5.1)

where the convolution allows unrestricted common factors. After multiplying
by the completely multiplicative nu(n)chi_n(u), (5.1) still holds including
zeros. Thus its smooth sum is a hyperbolic, not rectangular, product sum:

    T_c(D,u)=sum_{n_1,...,n_r} product_j [mu(n_j)eta_j(n_j)
          nu(n_j)chi_{n_j}(u)] W(product_j Nn_j/D).               (5.2)

Fix a smooth multiplicative dyadic partition theta supported on [1/2,2].
The following input is explicit: for each j, every epsilon>0, all shorter
X in [1/2,C_r beta D] at the SAME physical measure w_H of mass O(H), and
every real t, suppose

    ||A_{eta_j nu}(X;theta(v)v^(-it))||_{L^(2kr)(w_H)}
      << H^(1/(2kr)) X^(1/2) D^((e_{kr}+epsilon)/(2kr))
          (1+|t|)^B,                                          (5.3)

where e_{kr}>=0, B and the implied constant are independent of X,D,H,t.
The fixed factor C_r accommodates the dyadic support. Original exclusions
and finite twists are retained. Any claimed uniformity in a moving Q is
part of input (5.3); the elementary completion adds no new Q-dependence.
The low bounded scales can equivalently
be handled by their trivial O(1) sums. This is a hypothesis, not a deduction
from an estimate only on H=X^h.

### Theorem 5.1

Under (5.3), the complete determinant sum, and by Section 3 its squarefree
prime-trace version, satisfy

    sum_u w_H(u)|T_c(D,u)|^(2k) << H D^(k+e_{kr}+epsilon),        (5.4)

with an arbitrarily adjusted epsilon. No higher moment on c is assumed.
If the native e_j are sublinear along the requisite orders j=rk, then the
transferred excess is sublinear for fixed r. A linear native excess remains
linear: this theorem creates no power saving by itself.

#### Proof

Insert the dyadic partition separately in each n_j. Only boxes with
product_j X_j comparable to D can meet the support of W. There are
O_r(log(2+D)^(r-1)) such boxes, up to constants depending on the support;
each X_j lies in the input range. Mellin inversion on Re(s)=0 gives a box
as

    (1/(2pi)) integral_R W_hat(it) (product_j X_j/D)^(-it)
                  product_j A_{eta_j nu}(X_j;theta(v)v^(-it)) dt.

The Mellin transform is rapidly decreasing to every fixed order. Apply
Minkowski in t, and Holder with r factors on the SAME row measure:

    ||product_j A_j||_{2k} <= product_j ||A_j||_{2kr}.

Using (5.3), the norm of each box is
O(H^(1/(2k)) D^(1/2) D^((e_{kr}+epsilon)/(2k))). The integral of the fixed
Mellin transform against (1+|t|)^(rB) is finite. Sum the boxes and raise
to the 2k-th power. The logarithmic box count is absorbed in epsilon.

For the raw prime-trace sum use the inverse in (3.7). The same argument at
every shorter D/Nd gives a factor (Nd)^(-1/2); the global budget D and
physical H remain fixed. Bound its finite coefficient mass by (3.8).
Its logarithmic cost is again absorbed in epsilon. QED.

## 6. Tests of tempting shortcuts, and the remaining arithmetic step

**A small prime can invalidate the inverse-kernel bound.** For rank three
with three trivial eigenvalues,

    D(z)/P(z)=(1-z)^3/(1-3z)
            =1+3z^2+8z^3+24z^4+72z^5+... .

At a prime ideal of norm 7, its degree-e coefficients for e>=3 are
8*3^(e-3). Their square-root-weighted sum diverges because 9/7>1.
Thus a prime-uniform logarithmic bound on this inverse kernel is false
without controlling the finitely many small factors. This demonstrates
a failure of that claimed operator bound, not a counterexample to the
original rank-one Mobius moment.

**Neither completion nor rank rigidity makes the native covariance small.**
For r=1 the determinant coefficient is exactly mu times its character:
(5.4) simply returns its input. For r>1 it consumes moment order 2kr,
rather than proving a new native order from 2k. The nonabelian necessity
theorem additionally assumes character-valued probes not present in the
original hypothesis. There is no hidden bootstrapping of (5.3) from itself.

The direct Liouville target of #935 is still

    sum_{0<Nu<=H} |sum_n lambda_K(n)nu(n)chi_n(u)d_{k,W,X}(n)|^2
         << H X^(k+epsilon),                                  (6.1)

at all required shorter scales and the common physical height. None of
Sections 2--5 proves (6.1). The algebra identifies a natural discrete
family of coefficient completions and prices their transfer. A signed
arithmetic estimate with genuinely smaller excess is still required.

## Sources and scope of reconstruction

- #935 at a7a7fad2c5fa1929c7e04570cde4188e3191b071: actual complete
  MATHEMATICS.md and verify.py were read from the supplied packet; blob
  identities were checked against its manifest. #933's singularity/copying
  mechanism is credited through #935, not relabeled as a new method.
- #931: current PR description read. Its independent-prime finite-group
  Haar determinant theorem is prior work and concerns a different measure.
  It does not imply the physical determinant estimates assumed here.
- #936 at eb8d23decc003d36ded287dc98868308192cc889: PROOF.md read for
  growing smooth-residual-conductor control and the open cross-block term.
  Its bound is not silently extended to the full native measure.
- #937: PR description read for prime freezing and inverse noise. Its
  randomized bounds are not imported as native endpoint bounds.
- NIST DLMF 27.6: classical convolution background.
- Gorodetsky, *Magic squares, the symmetric group and Mobius randomness*,
  arXiv:2102.11966: abstract read for prior symmetric/exterior-power and
  Liouville-moment context. No theorem from it is an analytic input here.
- Gun--Hazra--Sahu, *On holomorphy and non-vanishing of Artin L-functions*,
  Monatshefte fur Mathematik 206 (2025), 853--883,
  DOI 10.1007/s00605-025-02060-7: introductory Brauer/Artin framework and
  Section 6 Euler-factor comparison read. Our Section 4 spells out the
  local order-at-one deduction. No global Artin holomorphy theorem is used.
- Fixed-field ideal counting, the prime ideal theorem, finite-order Hecke
  nonvanishing at one, Brauer induction, Artin formalism, and finite-group
  character theory are classical inputs. No October 2026 quasi-RH theorem,
  new large sieve, or conjectural zero-free estimate is used.

No exhaustive literature or repository priority audit was performed. These
are proposed deductions at the explicitly stated scope, not integrated or
independently accepted mathematical results.
