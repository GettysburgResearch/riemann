# Active conductors and a short neutral-divisor window

Status: PROPOSED component proofs. No full native moment, improved zero-free
boundary, or RH proof is claimed. Independent mathematical review is needed.

Scope: K=Q(omega), omega^2+omega+1=0; every fixed even moment order; all
nonzero element rows; fixed row-independent column arrays on ideals Nn<=X.
The result estimates actual nonprincipal tuple contributions, not a random
model. It does not use the imported quasi-Riemann/theta or large-sieve claims.

Sources: #942 BANDLIMITED_PRUNING.md and PROOF.md at 377f548cab8759399aca80ed3188c495667d562a;
#943 at 24cb2cdd6e768c2c35ef87227ed8319cfc2d14ed is the publication parent.
The band-limited majorant and small-modulus quadrature are inherited from
#942. Poisson summation, inclusion-exclusion and rapid-decay estimates are
classical. The contribution is the conductor/mask reorganization, the uniform
short divisor window, and the beyond-total-radical gap consequences below.

## 1. One fixed physical majorant, and the actual character

Use <z,w>=Re(z conjugate(w)) and hat(f)(xi)=integral f(z)exp(-2pi i<z,xi>)dz.
Choose one radial, nonnegative, smooth g supported in |xi|<1/16 with integral
one. Put f=check(g), Phi=4 f^2. Then Phi is radial, nonnegative and Schwartz,
Phi>=1 on |z|<=1, Phi(0)=4, and supp hat(Phi) lies in |xi|<=1/8. This is the
fixed construction of #942. In particular its entire row mass is O(H), H>=1;
the complete Schwartz tail is retained, not replaced by a sharp cutoff.

For a Hermitian tuple t=(n_1,...,n_k;m_1,...,m_k), define the total radical Q
and the residue exponent at each good prime ideal p by

    Q=rad(product_i n_i m_i),
    e_p=sum_i v_p(n_i)-sum_i v_p(m_i) modulo 6.

Let C be the product of primes with e_p!=0, and R=Q/C. Thus C and R are
squarefree and coprime. Write c=NC. At p|C the character chi_p^e_p is
nontrivial on the residue field and zero at zero. Their product chi is a
nonprincipal primitive finite character modulo C when C!=1. At p|R the
local factor is the indicator of a unit, even when a positive column exponent
has become zero modulo six. Therefore the literal tuple function is

    h_t(u)=chi(u) 1_{(u,R)=1}.                                  (1)

Ideals, not their norms, label factors. Equal-norm conjugate ideals stay
separate. This applies to both squarefree Mobius and unrestricted Liouville
columns. Fixed finite twists belong in the outside tuple coefficient.

Only nonprincipal tuples C!=1 are considered below; chi(0)=0. Choose a
generator d of each ideal divisor when an element argument chi(d) is used.

## 2. A two-ended estimate for the unmasked conductor sum

Define, for T>0,

    S_chi(T)=sum_{v!=0} Phi(v/sqrt(T)) chi(v).

### Lemma 1

Uniformly in C and chi as above:

(a) S_chi(T)=0 whenever T>=c.

(b) For every real A>1 there is K_{A,Phi}, independent of C and chi, such that

    |S_chi(T)| <= K_{A,Phi} T^A,       0<T<=1.                  (2)

(c) |S_chi(T)| <= K_Phi T for every T>0.

Proof of (a). The ideal lattice C has covolume (sqrt(3)/2)c and its dual
has shortest nonzero length 2/sqrt(3c). Poisson periodization on a residue
coset modulo C gives

    sum_{v in a+C} Phi(v/sqrt(T))
      = T/((sqrt(3)/2)c) sum_{xi in C*}
               hat(Phi)(sqrt(T)xi) exp(2pi i<a,xi>).

For T>=c all nonzero terms vanish by Fourier support. Every coset has the
same total weight. The complete sum of chi is zero, by finite-field
orthogonality and CRT. Removing v=0 changes nothing because chi(0)=0.
This proves (a), including both finite-field orders two and three that can
occur among the local powers of a sextic character. The chosen c cutoff is
conservative; fixed numerical improvements to it are not the point.

For (b), |chi(v)|<=1 and Nv>=1 for every nonzero integral element. A fixed
Schwartz seminorm bounds |Phi(v/sqrt(T))| by K T^A (Nv)^(-A). The sum of
(Nv)^(-A) converges for A>1, by the O(t) Eisenstein lattice count. This
proves uniformity. For T>=1, lattice annuli and Schwartz decay give sum
|Phi(v/sqrt(T))|=O(T). For T<=1, (b) with A=2 implies (c). QED.

Radiality is used in the dilation formulas below. A nonradial version needs
rotated tests, not the unrotated S_chi displayed here. Also a character
nontrivial on the six units has S_chi(T)=0 for every T by unit averaging;
this further cancellation is valid but is not needed for the estimates.

## 2A. An explicit fixed majorant with nearly exponential decay

The arbitrary Schwartz choice gives (4). For a sharper, order-uniform
window, make the following ONE fixed choice, with s>1 fixed independently
of X,H,k. Put

    M_s=1+1/(s-1),          r_j=1/(64 M_s j^s),
    c_s=(log 2)/(128 M_s)^(1/s),
    B_s=192 c_s^(-2s) Gamma(1+2s).                            (G1)

Let mu_j be normalized area measure on the disk of radius r_j, and let g be
the density of the infinite convolution mu_1*mu_2*... . This density exists,
is nonnegative, radial and C-infinity, is supported in |xi|<=1/64, and has
integral one. Set f=check(g) and Phi_s=4f^2. Then Phi_s has every property
used in Section 1 and, additionally,

    |Phi_s(z)| <= 16 exp(-2 c_s |z|^(1/s)).                    (G2)

Here are details establishing the construction rather than merely assuming
a Gevrey cutoff. Since sum j^(-s)<=M_s, the sum of the support radii is at
most 1/64. The finite convolutions converge weakly: their tails translate
any bounded uniformly continuous test by at most sum_{j>N} r_j, tending to
zero. Their limit is a radial probability measure of the stated support.

If phi_j is the Fourier transform of mu_j, the divergence theorem on its
disk gives

    |phi_j(z)| <= min(1, 1/(pi r_j |z|)).                      (G3)

Indeed integrate a directional derivative of exp(2pi i<z,xi>) in the z
direction, and bound the boundary integral by the perimeter 2pi r_j.
For j<=N=floor((|z|/(128 M_s))^(1/s)), one has r_j|z|>=2, and hence
|phi_j(z)|<=1/2. Every other factor has modulus at most one. Taking limits,

    |f(z)|<=2^(-N)<=2 exp(-c_s |z|^(1/s)).                    (G4)

The limit transform is integrable against every polynomial. Fourier
inversion therefore gives a C-infinity density for the limiting measure.
It has compact support, is nonnegative, and integrates to one. Thus g is
indeed a radial smooth compact function, and f and Phi_s are Schwartz.
This also proves (G2). Since the support of g is inside 1/64, for |z|<=1
its real inverse transform is at least cos(pi/32)>1/2, so Phi_s>=1 there.
The Fourier support of Phi_s is in |xi|<=1/32, inside the previous 1/8 cap.
This construction changes NO arithmetic coefficient or row divisibility
law. Infinite convolutions are used only to specify a deterministic test.

Let nu=1/(2s). For 0<T<=1, (G2) and Nv>=1 give

    |S_chi(T)| <= 16 exp(-c_s T^(-nu))
                         sum_{v!=0} exp(-c_s (Nv)^nu)
                <= B_s exp(-c_s T^(-1/(2s))).                (G5)

For the first inequality use 2ab>=a+b for a,b>=1. For the second, the
number of nonzero lattice elements with norm <=t is at most 12t, t>=1.
Stieltjes integration then bounds the sum by
12 c_s^(-1/nu) Gamma(1+1/nu). One elementary verification of the lattice
count is |a|,|b|<=2 sqrt(t/3) for Nv=a^2-ab+b^2<=t, whence at most
(4 sqrt(t/3)+1)^2<12t coordinate pairs. This proves (G5) with the explicit
B_s in (G1), uniformly in C and chi.

## 3. Exact neutral-mask reunion and localization

Put

    K_{C,R}(H)=sum_{u!=0} Phi(u/sqrt(H)) chi(u)1_{(u,R)=1}.

### Theorem 2 (neutral-divisor window)

For H>=1 the following finite divisor identity is exact:

    K_{C,R}(H)=sum_{d|R} mu_K(d) chi(d) S_chi(H/Nd).            (3)

For every L>=1 and every A>1 it follows that

    K_{C,R}(H)
      = sum_{d|R, H/c<Nd<=HL} mu_K(d)chi(d)S_chi(H/Nd)
        + E_{C,R}(H,L),
    |E_{C,R}(H,L)| <= K_{A,Phi} tau(R) L^(-A).               (4)

Proof. Expand the unit indicator in (1) by inclusion-exclusion. Multiplication
by a generator d bijects nonzero elements of O_K with the nonzero elements
of the ideal d. Complete multiplicativity of chi, including its zeros, and
radiality give Phi(dv/sqrt(H))=Phi(v/sqrt(H/Nd)), proving (3). There is no
new condition (d,v)=1. Such a condition would change the formula.

For Nd<=H/c, H/Nd>=c and Lemma 1(a) gives exact zero. For Nd>HL the
remaining dilation is <1/L, so Lemma 1(b) bounds each summand by K L^(-A).
There are at most tau(R) summands. This proves (4). Choice of a different
unit multiple of d cannot change (3): either chi is unit-trivial or the
corresponding S_chi is zero. QED.

Thus active conductor C, neutral mask R and total period CR have different
roles. Replacing R by 1 is not permitted. The middle sum is still SIGNED;
no sign or diagonal-size estimate is supplied for it.

### Corollary 3 (uniform full-moment localization)

Let |a_n|<=1 be supported on good ideals Nn<=X, X>=2, and independent of u.
All original masks and additional column exclusions are allowed. Fix k, delta>0
and B>0. If P_{2k}^Phi denotes the actual principal sector, then

    M_{2k}^Phi(X,H)=P_{2k}^Phi(X,H)+W_{k,delta}(X,H)+O(X^(-B)), (5)

uniformly for H>=1. Here W is the sum over ALL original nonprincipal tuples,
with their original complex coefficients, of precisely the middle divisor
sum in (4) with L=X^delta. Swapping the two tuple halves conjugates each
summand and preserves C, R and the cutoff, so W is real.

Proof. There are O_K(X) possible columns and O_k(X^(2k)) tuples. Also NR<=X^(2k)
and the elementary fixed-field divisor estimate gives tau(R)<<_{k,eta}X^eta
for any fixed eta>0. Thus summing the errors in (4) costs at most
O(X^(2k+eta-A delta)). Choose A>(2k+eta+B)/delta. All constants are independent
of H and the array; every chosen parameter k,delta,B is fixed before X grows.
Finite tuple sums and absolutely convergent row sums can be exchanged. QED.

The same conclusion holds for any row-independent tuple selector of modulus
at most one, with the corresponding selected principal term. No positivity of
a selected tuple union is assumed. Fixed divisor-bounded arrays can be included
by paying their stated arbitrarily small powers before choosing A.

This is a genuinely signed localization. Bounding W from above by H X^(k+epsilon)
with native coefficients would suffice for the native sharp-ball moment,
using #942's principal estimate and Phi>=1 on the unit disk. That bound is OPEN.

### Theorem 3A (a polylogarithmic window, uniform in the moment order)

Use Phi_s from Section 2A. For EVERY integer k>=1, X>=2, H>=1 and B>0,
put

    Y=[(3k+B)log X + 2k log 2 + log B_s]/c_s,
    L=Y^(2s).                                                 (8a)

Then Y>1, and replacing each nonprincipal tuple kernel by its exact middle
sum over H/c<Nd<=HL changes the COMPLETE moment by at most

    |M_{2k}^{Phi_s}-P_{2k}^{Phi_s}-W_{k,L}| <= X^(-B).          (8b)

There is no suppressed order-dependent constant in this error bound.
For any fixed eta>0 choose s=1+eta/2 once. The upper neutral-divisor cutoff is

    HL <<_{eta} H [ (k+B+1)log(2X) ]^(2+eta).                 (8c)

The same error bound applies to ANY row-independent tuple selector of
modulus at most one, with its selected principal and nonprincipal sums.
It does not assert that the remaining window sum or full moment is small.

Proof. Lemma 1(a) still removes Nd<=H/c exactly. From (G5), the discarded
upper tail for one tuple is at most B_s tau(R)exp(-c_s L^(1/(2s))).
Every integral ideal has six generators in K, so the coordinate count above
in fact gives I_K(X)<=2X for X>=1: the stronger constant
(4/sqrt(3)+1)^2/6 is less than two. There are at most (2X)^(2k) tuples.
Every neutral prime occurs at least twice across the tuple, so NR<=X^k.
Since R is squarefree, tau(R)=2^omega(R)<=NR<=X^k. Thus the aggregate
error is at most

    B_s 2^(2k) X^(3k) exp(-c_s L^(1/(2s))).                   (8d)

Substitute (8a); this is exactly X^(-B). All constants in G1 are fixed
before k grows. No fixed-order divisor estimate is used in this proof.
Formula (8c) follows directly from (8a) with s fixed. QED.

This provides growing-order LOCALIZATION, not a growing-order upper moment
bound. In particular the principal estimate imported from #942 retains its
own fixed-k constants. Nor is the endpoint eta=0 established: the summable
support construction explicitly requires s>1.

The divisor-gap corollaries below can now use L from (8a) instead of X^delta,
with the same explicit X^(-B) aggregate error. Their simpler power-gap
versions remain useful for displaying strict exponent margins.

## 4. Beyond the old total-radical cutoff

### Corollary 4 (divisor gap)

Suppose C!=1 and R has NO divisor in

    H/c < Nd <= H X^delta.                                    (6)

Then K_{C,R}(H)=O_A(tau(R)X^(-A delta)) for every A>1. Every union of such
native tuples contributes O_{k,delta,B}(X^(-B)) for every B>0.

This follows immediately from (4) and the counting in Corollary 3. It is
rapid suppression, not exact annihilation: the upper divisor tail remains.
Condition N(CR)<=H from #942 implies that every divisor is in the exact-zero
range, and then (3) is exactly zero. Condition (6) also admits CR much larger
than H. An empty middle interval is the precise extra opportunity.

### Corollary 5 (block criterion without listing all divisors)

Write R=R_0 R_1 with coprime factors. For j>=0 let U_j be the product of the
j largest prime norms in R_1, with U_0=1, and let L_{j+1} be the product of
its j+1 smallest prime norms. If j>=omega(R_1), replace the first condition
below by c NR<=H and obtain exact zero. Otherwise assume

    c N(R_0) U_j <= H,             L_{j+1} > H X^delta.         (7)

Then Corollary 4 applies. Indeed a divisor using at most j primes of R_1 is
at most N(R_0)U_j; a divisor using at least j+1 is at least L_{j+1}. These
cover ALL divisors, including overlaps of neutral masks across columns.

In the simple j=1 case it is enough that every individual neutral prime is
small enough for conductor quadrature, while every product of two of them
is too large to affect more than the rapidly decaying row tail. Higher j
prices more complicated neutral supports without asserting new cancellation.

## 5. Genuine annular native tuples with long singleton primes

Here is a family outside the old low-total-radical domain and the log-square
singleton domain. Let a and bar(a) be the distinct conjugate prime ideals
above a rational prime t=1 mod 3. Let p,q_2,...,q_k be distinct good prime
ideals different from these two. For k>=2 take

    left:  a p, q_2,...,q_k;
    right: bar(a) p, q_2,...,q_k.                              (8)

All columns are squarefree. C=a bar(a) has norm t^2 and local charges +1,-1;
R=p q_2...q_k is neutral. The character is NOT killed by unit averaging:
the two conjugate norm-t primes have the same unit exponent, which cancels.
It is nonprincipal by the two nontrivial local components. All source zeros
and any fixed twist remain in the general theorem.

Choose norms t asymp D^alpha, Np asymp D/t and Nq_i asymp D, in fixed intervals
which put EVERY column in D/2<Nn<D. There is no conflict of annular scales
because Na=Nbar(a). With H=D^h, the j=1 conditions hold eventually when

    2alpha+1<h,              2-alpha>h+delta.                    (9)

Indeed c max(Np,Nq_i) is O(D^(2alpha+1)), and the smallest product of two neutral
prime norms is of order D^(2-alpha). The full radical has norm of order D^(k+alpha),
well beyond H for k>=2 and h<2. For example h=21/20, alpha=1/100, delta=2/5
satisfy (9) strictly. The active singleton primes then have norm D^(1/100),
not bounded by (log D)^2. The entire selected nonprincipal contribution is
O_B(D^(-B)) for every fixed B. This is NOT the full fourth or 2k-th moment.
Existence of prime choices in the indicated fixed relative intervals can be
obtained from the classical prime number theorem in 1 mod 3; that input is
used only for asymptotic nonemptiness, not for any upper estimate above.

A completely finite instance, requiring only trial-division primality checks,
is D=X=16384, H=2097152, t=7, Np=1801, Nq_2=12007, and delta=1/8. The four
column norms are 12607,12007;12607,12007. Here c=49, NR=21624607,
c max(Np,Nq_2)=588343<=H, while (NR/H)^8>X. The total radical norm is
1059605743>H. The inequalities certify the pruning hypotheses, NOT a
numerical evaluation of an infinite Schwartz row sum.

## 6. What survives the attack

If the active conductor c>H then d=1 is always in the middle window in (4).
The completely separated long-singleton configurations have just this form,
often with R=1 and c as large as X^(2k). Nothing in this proof makes their
native signed sum small. Taking absolute values there returns the old power
loss; the divisor gap is not an all-tuple condition.

The theorem concerns the complete Phi-weighted row sum. Sharp rows cannot
be substituted inside individual tuple cancellations. For example the active
character chi_a conjugate(chi_bar(a)) at the two norm-7 ideals has sharp sum
-6 over 0<Nu<=49, although c=H=49. Its Phi-weighted sum is zero. A selected
signed sum is not monotone under replacing its row weights by a majorant;
only the COMPLETE nonnegative moment has the majorization property used in (5).

No prior microscopic-phase or matching-geometry claim is promoted or needed.
The smallest remaining statement is the one-sided native upper bound for W
in (5), or for a further signed localization of its large-active-conductor
part, with the source's full test/twist/shortened-scale uniformity.
