# All sixth-power-free rows, masks, and a coherent divisor mark

**Status:** proposed component deductions from Theorems A--B in PROOF.md
and their stated external inputs. These are positive row norms of the
specified Gauss sums, not bounds for a selected indefinite Poisson sector.
Throughout 4/9<=p<1/2, p=(2 beta+1)/6. All common profiles are radial,
smooth and compactly supported away from zero; fixed bad-prime/ray data
are as in PROOF.md. Constants are uniform in the moving moduli.

## 1. Fixed extra masks

Inserting 1_((a,m)=1) in Theorem B costs at most (Nm)^epsilon. Primes of
m already in fc impose no new condition. Expand the others exactly over
squarefree d|rad(m), put a=dv, and use

    g_tilde(dv)=g_tilde(d)g_tilde(v)conjugate((v/d)_3).

The new fixed matching part is f0*d, so K becomes K Nd, while X becomes
X/Nd. Row factors chi_c(d), including their zeros, are contractions of
the positive row norm. The maximum in (2) satisfies

    H_p(K D,C)<=D^(1-p) H_p(K,C),  D>=1.                 (18)

The root cost of a divisor d is therefore at most
(Nd)^((1-3p)/2)<=1. Summing all divisors costs only a subpower. If
X/Nd<1, the compact annulus makes the term empty below a fixed positive
scale; the remaining bounded scales change only a profile constant.
This argument keeps every shared prime, rather than replacing a
zero-extended character by a coprimality-free phase.

## 2. Coherent short marks in the squarefree conductor family

For |b_v|<=1, fixed independently of c, and A,B>=1, set

    T_(f,c)(A,B)=sum_(a,v) b_v g_tilde(av) psi_(f,c)(av)
             W_A(Na/A) W_B(Nv/B) 1_((av,m)=1).           (19)

Only squarefree v coprime to fcm contributes. Freeze v. Multiplicativity
turns the inner expression into the sum of Theorem B with fixed modulus
fv, character psi_f*conjugate(kappa_v), effective level K Nv, and scale A.
Its outside scalar is b_v W_B(Nv/B)g_tilde(v)psi_(f,c)(v), of bounded
modulus; its c-dependent part is again a row multiplier. The varying
c>1 quadratic dual factor ensures that no main term appears.

Minkowski over the O(B) ideals in the annulus, with monotonicity of H
and the mask result, gives

    sum_c |T_(f,c)(A,B)|^2
       << (ABFC Nm)^epsilon A^(2p) B^2 H_p(KB,C).         (20)

This is a genuine coherent mark, not an independent randomized copy of
v. It allows b_v=mu_E(v) times any fixed bounded coefficient. Cancellation
in b_v itself is NOT used: the v-sum is still treated by triangle.
For a fixed joint smooth W(Na/A,Nv/B), freeze Nv/B; the finitely many
required first-variable seminorms stay uniformly bounded. Thus (20)
also permits that common joint profile.

## 3. Pointwise input for the purely powerful rows

We recall the needed individual estimate, including its proof resource,
so that no unspecified fixed-character constant enters the next step.
For a primitive character psi modulo squarefree r, partition r=r0 r1
as in PROOF.md and put K_r=Nr0 (Nr1)^2. The general periodic-twist
functional equation, the actual coefficients (9), and all Ramanujan
local factors give on a line -eta

    Q_psi(-eta+it)<< K_r^(1/2) (Nr)^O(eta)+epsilon
                                  (1+|t|)^A.

The right line 1+eta is absolutely bounded. The complete Ramanujan
local factor at a matching prime of norm q on Re(w)>=1 is

    1+(q-1)q^(-w)
       +(q-1)(1+q^(-w))q^(1/2-3w)/(1-q^(1/2-3w)) <=2.

Its product is a subpower. Nonmatching primes keep the actual scalar
q from the finite transform, not sqrt(q). Pole-cleared strip
Phragmen--Lindelof therefore gives Q_psi(s)<<K_r^((1-Re(s))/2+epsilon)
with polynomial height cost. The reciprocal argument of Section 7 and
Mellin inversion yield

    S_psi(X)-P_psi(X)<< (X Nr)^epsilon X^p K_r^((1-p)/2). (21)

The main term is zero except when psi=conjugate(kappa_r). In that case

    P_psi(X)=c_E W_hat(5/6) X^(5/6)
             conjugate(g(r)) phi_E(r)/[(Nr)^(5/3)L^(3r)(2,1)],
    c_E=(2 pi)^(5/3)/[3^(7/2)Gamma(2/3)].                (22)

This is exactly the residue in #1010 and [DR, Proposition 5.2]. For
r=1 retain its principal residue too. A bounded divisor mark in (21)
has root bound A^p B^((3-p)/2) K_r^((1-p)/2), by the same fixed-v
argument as in Section 2. Its residue is the sum of the exact residues
(22), not zero by default.

## 4. Complete sixth-power-free row theorem

For a sixth-power-free primary u prime to 6 let

    chi_u(a)=(a/u)_6,
    S_u(X)=sum_a g_tilde(a)chi_u(a)W(Na/X).

Every such row has a UNIQUE decomposition u=e z, where e is squarefree,
z has all nonzero valuations in {2,3,4,5}, and (e,z)=1. The modulus of
chi_z is f=rad(z), still squarefree, and chi_z is primitive at every
prime of f. Its matching part consists exactly of primes of valuation
4 in z. Thus its effective level obeys

    K_z=N(product_(v_p(z)=4) p)
            *N(product_(v_p(z) in {2,3,5}) p)^2 <= Nz.   (23)

For fixed z with e>1, Theorem B applies at C about U/Nz with fixed
character psi_f=chi_z. Moving zeros at shared primes are retained by
(e,z)=1. If the dyadic range for e is bounded, use a fixed enlargement
C about 1, not an asymptotic density assertion. The estimate

    H_p(K_z,C)<=K_z^(1-p) C^(2-7p/4)

holds because each K exponent in H is at most 1-p and each C exponent
is at most 2-7p/4. Summing over z costs

    U^(2-7p/4) sum_(z powerful) (Nz)^(-1+3p/4).

This ideal Euler series converges: its first possible local term has
valuation 2, and 1-3p/4>=5/8>1/2. All subpower losses can be chosen
smaller than that strict convergence margin. All primes and all
valuations {2,3,4,5} are included.

For e=1 use (21), not Theorem B's c>1 statement. The number of powerful
ideals up to U is O(U^(1/2+epsilon)), as follows by writing z=a^2 b^3
with b squarefree and summing (Nb)^(-3/2). Since K_z<=Nz, the centered
squared norm of these rows is at most

    (XU)^epsilon X^(2p) U^(3/2-p),

which is bounded by X^(2p) U^(2-7p/4) on the stated p range.

Consequently, for U>=2,

    sum_(U<Nu<=2U, u sixth-power-free, (u,6)=1)
        |S_u(X)-P_u(X)|^2
      << (XU)^epsilon X^(2p) U^(2-7p/4).                (24)

Here P_u is (22) if u=r^4, with r squarefree, and is zero otherwise.
The principal row is not in U<Nu for U>=2. Such fourth-power rows are
not silently removed. Their residue has magnitude at most
X^(5/6)(Nr)^(-1/6+epsilon). Hence

    sum_(Nu~U)|P_u(X)|^2 << (XU)^epsilon X^(5/3) U^(1/6).

Adding this term gives an uncentered version of (24). The theorem
controls the entire indicated row family; it does not assert square-root
cancellation of the exceptional cubic bias.

## 5. Complete marked row mean

Define T_u(A,B) as in (19) with psi_(f,c) replaced by chi_u. Define its
residue P_u^mark by summing the literal residues (22) after freezing v;
it can be nonzero only for u=r^4. More explicitly, in that case,

    P_u^mark=sum_(v sf,(v,rm)=1) b_v W_B(Nv/B)
                  g_tilde(v)conjugate(kappa_r(v))
                  P_(conjugate(kappa_(rv)); W_A,mask m)(A).

The masked P is the exact finite inclusion-exclusion of (22). This
formula also defines the residue for a joint smooth profile by freezing
its second variable. In all other rows the same finite transform has
zero constant term and P_u^mark=0.

For e>1 apply (20) with K=K_z and C about U/Nz. The two elementary
bounds required for the z-sum are

    H_p(K_z B,C)<=K_z^(1-p) H_p(B,C),
    H_p(B,U/Z)<=Z^(-(2-2p)) H_p(B,U), 1<=Z<=U.          (25)

Indeed 2-2p is the smallest C exponent among the three monomials.
Combining K_z<=Z leaves the powerful series sum Z^(-(1-p)). It
converges for p<1/2. The margin may be small when beta approaches 1;
constants are allowed to depend on beta, and the internal epsilon
losses must be chosen after that margin.

For e=1, (21) with the marked root cost in Section 3 gives a total at
most A^(2p) B^(3-p) U^(3/2-p) times prescribed small powers. This is
absorbed by the third monomial of A^(2p) B^2 H_p(B,U), since
3/2-p<=2-2p. Fixed dyadic endpoint enlargements change only constants.
Thus the complete centered theorem is

    sum_(Nu~U, u sixth-power-free, (u,6)=1)
        |T_u(A,B)-P_u^mark(A,B)|^2
      << (ABU Nm)^epsilon A^(2p) B^2 H_p(B,U).           (26)

Masks at m are paid by Section 1, or inside the exact fixed-v
inclusion-exclusion before the powerful-row sum. All resulting losses
are prescribed subpowers, not hidden constants depending on m.

For completeness, triangle in the residue formula bounds its v-sum by
A^(5/6)B^(5/6)(Nr)^(-1/6) times subpowers: each new matched prime in v
contributes its actual (Nv)^(-1/6) residue cost. The additional mask
divisors have cost (Nd)^(-1). Therefore the uncentered version of (26)
may add (AB)^(5/3)U^(1/6) times the same subpowers. No mean-zero claim is
made for this residue.

## 6. A useful comparison, with its scope kept explicit

At beta=7/8 one has p=11/24 and

    H_p(K,C)=max(K^(5/16)C^(115/96),
                 K^(1/2)C^(7/6), K^(13/24)C^(13/12)).

For A=Y^(3/4), B=Y^(1/4), U=Y^(3/10), the middle regime applies.
Equation (26) gives

    [U^(-1) sum_u |T_u-P_u^mark|^2]^(1/2)
          << Y^(109/160+epsilon).

For the squarefree conductor rows the residue is already zero. The
Euler-only version of the same averaged method has exponent 153/220,
so the saving against that comparable baseline is 5/352. The earlier
#1010 pointwise estimate had exponent 791/960 for each row in its
stated squarefree conductor range. An average theorem is not a
replacement for an every-row theorem.

At X=U, equation (24) for S_u/sqrt(X) has squared-mean exponent 107/96.
The generic sextic sieve at equal row and column lengths costs 7/6;
the difference 5/96 comes from using the specific Gauss coefficients.
Neither 107/96 nor 115/96 is the exponent of PR #1006's inverse/plain
product. In particular (24)--(26) do not supply its missing hypothesis.
