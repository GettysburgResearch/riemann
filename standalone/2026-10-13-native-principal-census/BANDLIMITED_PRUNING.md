# Exact low-radical pruning with a positive row majorant

Status: PROPOSED component proof, not a full native moment bound. Same-author
reconstruction only. This addendum was developed after the interrupted census
publication. It directly treats a portion of the nonprincipal sum; it does not
pretend that the remaining large-radical portion is small.

The construction is a classical band-limited Poisson argument, specialized to
the exact Eisenstein tuple characters and their masks. No global novelty claim
is made. An explicit primary reference for the Fourier convention and Poisson
identity is Andrew V. Sutherland, MIT 18.785, Fall 2021, Lecture 17, Sections
17.1 and Theorem 17.8, pages 1--3:
https://math.mit.edu/classes/18.785/2021fa/LectureNotes17.pdf . The two-dimensional
lattice version below follows by periodization in two coordinates. We give the
normalization and the relevant proof instead of importing a conductor estimate.

## 1. One fixed admissible weight

Use the real Euclidean pairing on C and the Fourier convention

    hat(f)(xi)=integral_C f(z) exp(-2 pi i <z,xi>) dz.

Choose an even nonnegative smooth function g, supported in the disk |xi|<1/16,
with integral one. It can be chosen radial. Define

    f(z)=integral_C g(xi) exp(2 pi i <z,xi>) dxi,
    Phi(z)=4 f(z)^2.

Then f is real and Schwartz; Phi is nonnegative, Schwartz, and independent of
X,H,k and all arithmetic data. For |z|<=1, every cosine in the integral is
at least cos(pi/8)>1/2. Consequently Phi(z)>=1 on the unit disk. Moreover

    Phi(0)=4,       supp hat(Phi) subset {|xi|<=1/8}.             (BL1)

The Fourier support follows from hat(Phi)=4(g*g). Set v_K=sqrt(3)/2 and
c_Phi=hat(Phi)(0)/v_K. This is a fixed finite positive constant. In particular

    sum_(0<Nu<=H) |F(u)|^(2k)
          <= sum_(u!=0) Phi(u/sqrt(H)) |F(u)|^(2k), H>=1.        (BL2)

The right side includes the ENTIRE Schwartz tail. It is not a compactly
supported row measure or the sharp row measure from the finite census.

## 2. Exact quadrature on a small ideal modulus

Let Q be a nonzero integral ideal and let h_Q be any function on O_K/Q, extended
periodically to O_K. It need not be a character. Define

    av_Q(h_Q)=(NQ)^(-1) sum_(a mod Q) h_Q(a).

**Theorem BL1.** Whenever NQ<=H and H>=1,

    sum_(u!=0) Phi(u/sqrt(H)) h_Q(u)
       = c_Phi H av_Q(h_Q) - 4 h_Q(0).                         (BL3)

This is an exact identity, not an estimate with an omitted Poisson tail.

**Proof.** Write Q=(q). Its lattice has covolume v_K NQ. The shortest nonzero
vector of the Euclidean dual lattice O_K^* has squared length 4/3: the vectors
have squared norms (4/3)(m^2+mn+n^2), for integers m,n. Multiplication by q
rotates and scales the primal lattice, so Q^* has shortest nonzero length
2/sqrt(3 NQ). Poisson summation on each coset gives

    sum_(u in a+Q) Phi(u/sqrt(H))
      = H/(v_K NQ) sum_(xi in Q^*)
            hat(Phi)(sqrt(H) xi) exp(2 pi i <a,xi>).             (BL4)

For every nonzero xi, |sqrt(H)xi|>=2/sqrt(3)>1/8. Thus (BL1) leaves ONLY the
zero frequency. Each coset has precisely the same total Phi weight,
c_Phi H/NQ. Multiply by h_Q(a) and sum over cosets. Removing the original
zero row subtracts h_Q(0)Phi(0), giving (BL3).

For completeness, (BL4) also follows directly by periodizing the Schwartz
function on the lattice Q. Its Fourier coefficient at xi in Q^* is
H hat(Phi)(sqrt(H)xi)/(v_K NQ). Absolute convergence permits evaluation at a.
This proves the normalization and the sign in (BL4). QED.

The cutoff NQ<=H is deliberately conservative; no optimization of its fixed
constant is claimed. The compact Fourier support and the complete row tail
are BOTH essential. Cutting off that tail invalidates the exact identity.

## 3. Application to the actual signed tuple expansion

Use all definitions of PROOF.md. For a Hermitian tuple t let

    Q(t)=rad(product_i n_i m_i),
    e_p(t)=sum_i v_p(n_i)-sum_i v_p(m_i) modulo 6.

At every prime dividing Q(t), its periodic local factor is chi_p(u)^e_p when
e_p!=0, and 1_(p does not divide u) when e_p=0. In particular a zero exponent
modulo six NEVER erases a nonunit zero. The full tuple character h_t has period
Q(t), and, for Q(t)>1, h_t(0)=0.

Finite-field character orthogonality and the Chinese remainder theorem give

    av_Q(h_t)=0                                      if t is nonprincipal,
    av_Q(h_t)=product_(p|Q)(1-1/Np)                  if t is principal. (BL5)

All good prime sextic characters have exact order six. A nonzero exponent
modulo six therefore has zero complete finite-field sum. A neutral local
factor instead has sum Np-1. This proves (BL5) including split/inert primes.

**Corollary BL2 (nonprincipal annihilation).** For each individual nonprincipal
tuple with NQ(t)<=H,

    sum_(u!=0) Phi(u/sqrt(H)) h_t(u) = 0.                       (BL6)

Thus every chosen union of these tuples vanishes exactly after the complete
row sum, with the actual Mobius signs, Liouville signs or arbitrary fixed
complex column coefficients. Tuple selectors must be independent of u. There
is no positivity claim for the selected union and no replacement of the
physical measure by independent prime residues outside the proved modulus
range.

**Corollary BL3 (localized sufficient target).** The full Phi-weighted moment is

    M_(2k)^Phi = P_(2k)^Phi + R_(2k),>H^Phi,                    (BL7)

where the last sum contains only NONPRINCIPAL tuples with NQ(t)>H. Combining
PROOF.md Theorem 2, Lemma 1 and (BL2), the open one-sided estimate

    R_(2k),>H^Phi <= C_(k,epsilon) H X^(k+epsilon)               (OPEN-BL)

would imply the native sharp-ball upper moment at the same X,H, for the
coefficient data for which it is proved. No lower bound for R or absolute
bound on its individual tuples is required. OPEN-BL has NOT been proved here.

The original smooth-column, finite-twist and shortened-scale uniformities must
still be supplied when using this implication in the repository's zero detector.
A bound only for the hard-window, trivial-twist census does not supply them.

A principal tuple has squarefull total product, so NQ(t)<=X^k. Accordingly, if
H>=X^k, every principal tuple is exactly in the quadrature range. At those
heights one has the sharper exact formula

    P_(2k)^Phi = c_Phi H B_(2k) - 4 |c_1|^(2k).                (BL8)

The unit-ideal endpoint term appears only when the unit column is present.
For an annular window excluding it, c_1=0. The statement H>=X^k does NOT put
all nonprincipal tuples in the range: their radicals can reach X^(2k).

## 4. Why narrowing the Fourier support cannot solve the remainder for free

One might try to shrink the Fourier support with X until every tuple is in
(BL6). The total row mass then changes by a power; it cannot remain O(H).

**Lemma BL4 (mass cost).** If Psi>=0 is Schwartz, Psi(0)>=1, and hat(Psi) is
supported in the disk |xi|<=B with B>0, then

    integral Psi >= 1/(pi B^2).                               (BL9)

**Proof.** Nonnegativity gives |hat(Psi)(xi)|<=integral Psi. Fourier inversion
at zero then yields
1<=Psi(0)<=integral_(|xi|<=B)|hat(Psi)(xi)| dxi
           <=pi B^2 integral Psi. QED.

For the same sufficient dual-gap test to cover every modulus norm up to T,
one imposes B<2 sqrt(H/(3T)). Its physical zero-frequency coefficient obeys

    c_Psi H=H/v_K integral Psi > 3T/(4pi v_K).                 (BL10)

For T>=1 this also gives a lower bound for the total NONZERO row mass. The
base-lattice nonzero dual frequencies vanish since B<2 sqrt(H/3), so
sum_(u!=0)Psi(u/sqrt(H))=H/v_K integral Psi-Psi(0). Using
Psi(0)<=pi B^2 integral Psi, we obtain
S>= (H/v_K-pi B^2) integral Psi. If this prefactor is nonnegative,
(BL9) gives S>=H/(v_K pi B^2)-1. If it is negative, the desired
lower bound below is negative and S>=0 suffices. In both cases,

    sum_(u!=0)Psi(u/sqrt(H)) > 3T/(4pi v_K)-1.                 (BL11)

Thus an attempt to cover the whole a priori tuple range T=X^(2k) by this
uniform small-support criterion necessarily raises the row mass to order T,
not H. This is a limitation of that sufficient Fourier-support scheme, not
of all possible cancellations or alternative row weights. It is not a lower
bound for the native signed remainder.

The fixed Phi in Sections 1--3 does not incur a moving power cost. It gives a
legitimate exact pruning of low radicals while leaving the genuinely long
signed conductor sum visible.

## 5. Diagnostics and scope

verify_bandlimited.py checks complete finite residue averages and masks,
Euclidean-dual norm identities, and a finite cyclic analogue of band-limited
coset quadrature by exact cyclotomic polynomial reduction. It also rejects
an over-wide support and the replacement of a neutral nonunit mask by one.
It does not evaluate the infinite Phi sum numerically or certify the analytic
Poisson theorem. Those conclusions rest on the written proof above. Both
programs and this addendum have the same author.
