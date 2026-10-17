# Which all-moment theorem would actually reach the critical line?

Status: exact finite identities and proposed deductions from named source
inputs. The critical native upper estimate is OPEN. This file does not turn
a theta or positive L-value theorem into a reciprocal-L theorem. It records
both the attempted route and the exact price that remains.

## 1. Three genuinely different moments

The new Theorem T concerns CT's reflected theta row B_m(Z). The numerator
hierarchy concerns L(s,chi_a). The native object that directly detects zeros
is instead

    A_u(D)=sum_n mu_F(n) chi_u(n) W_c(Nn/D),
    W_c(y)=y^(-c) exp[-(log y)^2/4]/(2sqrt(pi)).             (1)

Here u=1 is principal, and finite S exclusions are retained. On Re s>1,

    integral_0^infinity A_1(D) D^(-s) dD/D
                   =exp((s-c)^2)/zeta_F^S(s).             (2)

The numerator in (2) never vanishes. Conversely, B_m is not (1) and has
no proved pointwise/same-height inverse-L identification. Its route to (2)
passes through a SIGNED additive/theta pairing and Poisson projection.
The principal finite-part identity in #974 similarly retains -zeta'/zeta,
but its physical signed projection has no established bound at the required
strength. We read that actual finite-part proof; we do not replace its
unproved projection by a bound on the bare residue.

## 2. A full native all-even upper theorem actually supplied by S6

This step tests the most direct proposed shortcut against the real product
length and repeated-row cost. It is a complete upper theorem, but NOT the
critical diagonal theorem.

Use the full de Faveri family chi_u on integral exterior IDEAL indices u.
Choose its identity representative so chi_1 is principal. Fixed allowed
common column phases and finite twists are harmless. For a bounded test
W supported in (0,1], put

    A_u(D;W)=sum_(Nn<=D) mu_F(n) chi_u(n) W(Nn/D).

For every fixed integer k>=1, H,D>=2 and epsilon>0, S6 yields

    sum_(Nu<=H) |A_u(D;W)|^(2k)
      << ||W||_infinity^(2k) (HD)^epsilon D^k
          [H+H^(1/6)D^k+H^(5/6)D^(k/3)+H^(1/3)D^(5k/6)]. (3)

For the full Gaussian, the same bound holds with a constant depending on
k,c, replacing the displayed test norm. All original ideals and masks occur.
This is an IDEAL-indexed family theorem. Passing to balanced element rows
requires the usual finite local-class/generator adapter; no infinite norm-only
element ball or new all-field physical identification is hidden here. In the
Eisenstein principal-generator setting only the fixed unit classes are added.

Proof: initially restrict u to sixth-free indices, Nu<=H. Expand A_u^k
exactly, keeping each of the k original column caps. Its product coefficients
b(v) satisfy |b(v)|<=||W||^k d_k(v), and q_v<=D^k. Write v=e r^6, e sixth-free,
allowing shared primes e,r. The exact character law is

    chi_u(e r^6)=chi_u(e) 1_((u,r)=1).                   (4)

For fixed r, the square coefficient sum over e is
<<||W||^(2k) D^(k+eta)/(Nr)^6, using the fixed-order divisor bound. Applying
S6 and summing r by Minkowski costs sum_r (Nr)^(-3+eta)<infinity. Thus

    sum_(Nu<=H)^flat |A_u|^(2k)
       << ||W||^(2k) (HD)^epsilon D^k K(H,D^k).          (5)

Now write the row index uniquely as u=a b^6, a sixth-free, with NO condition
(a,b)=1. Complete multiplicativity and the original nonunit extension give

    chi_(a b^6)(n)=chi_a(n) 1_((b,n)=1).                 (6)

For each fixed b the extra factor is a common column mask, so (5) applies
with H replaced by H/(Nb)^6. Sum over all b<=H^(1/6). The four terms of K
cost respectively

    H sum_b (Nb)^(-6),
    D^k I_F(H^(1/6)),
    H^(5/6)D^(k/3) sum_b (Nb)^(-5),
    H^(1/3)D^(5k/6) sum_b (Nb)^(-2).

This proves (3) by ideal counting. Each original u belongs to exactly one
row pair (a,b), including their shared primes. The full Gaussian follows
by splitting columns into dyadic norm bands, applying Minkowski in the
SAME row l^(2k) norm (H does not change with the band), and summing the
Gaussian band weights against the finitely many fixed powers of 2^j in
(3). Bands with upper norm below1 are empty; all other upper and lower tails
remain. Gaussian decay dominates those fixed powers. QED.

Set H=D^h with h fixed. Relative to the desired H D^k scale, (3) gives the
excess exponent

    e_k=max(0,k-5h/6,k/3-h/6,5k/6-2h/3).                (7)

In particular e_k/k tends to ONE, not zero. The complete all-order theorem
(3) therefore does not improve the principal square-root target by taking
k large. The term H^(1/6)D^(2k) reflects actual sixth-power row repetition;
it cannot be deleted because chi_(b^6) is a principal character with a mask,
not an independent random character. This is the full-source manifestation
of the uniform-coefficient limitations already discussed in #955.

The upper bound (3) is not asserted sharp for the native signs. Its derivation
uses only divisor majorants, so it leaves open the coefficient-specific saving
that the user asks for. It is a quantitative failed attempt at that saving,
not a lower bound refuting it.

## 3. The cofinal native theorem sufficient for the entire critical line

Here is the exact all-moment goal; only an UNBOUNDED SUBSEQUENCE of orders is
needed. No uniform growing-k constant is necessary.

Let K0 be an unbounded subset of positive integers, h>0 fixed, and e_k>=0
with e_k/k ->0 along K0. Suppose that for the ACTUAL Gaussian sums (1), for
each fixed k in K0 and every epsilon>0,

    sum_(Nu<=D^h) |A_u(D)|^(2k)
             <<_(k,epsilon) D^(h+k+e_k+epsilon).         (OPEN-N)

Every such sum contains the original principal row u=1 with weight1. Therefore

    |A_1(D)| << D^(1/2+(h+e_k+epsilon)/(2k)).             (8)

Given delta>0, choose one sufficiently large FIXED k so (h+e_k)/(2k)<delta/2,
then choose its preliminary loss small enough to make (8) at most
D^(1/2+delta). Now let D tend to infinity. The constant can depend arbitrarily
on that fixed k and delta. There is no exchange of the limits k,D.

Thus OPEN-N implies |A_1(D)|<<_delta D^(1/2+delta) for every delta>0. At D=0
the Gaussian sum is flat by absolute ideal counting. Consequently the left
side of (2) converges absolutely and is holomorphic for Re s>1/2. The initial
identity continues there, and its nowhere-zero Gaussian numerator makes a
zero of zeta_F^S impossible in that half-plane. Finite S Euler factors have
no zeros in Re s>0. The functional equation then gives the critical-line
zero statement for zeta_F. Over the Eisenstein field, zeta_F=zeta L(chi_-3)
and the nonprincipal Dirichlet factor has no poles, so this would imply RH
for the ordinary zeta function as well.

This proof of the implication is elementary once OPEN-N is known. OPEN-N
ITSELF IS NOT PROVED. It is weaker than asking for all consecutive orders
with zero excess, but stronger in the exact needed way than (3). The theta
moments in Theorem T and numerator moments in (2) of the other file do not
satisfy or imply this source-faithful condition. A rowwise-positive cofinal
projection from them to (1) is a substantive missing theorem, not a routine
change of notation.

## 4. Why the new theta all-moment theorem does not remove the signed pairing

Let N=XY, let n be the actual number of physical rows (n<<N), and let the
original additive factor be A_t(m;X,Y). Its available positive estimate is

    ||A_t||_2^2 << 1/X+1/Y.                              (9)

Pairing with the theta 2k-moment using Holder requires q=2k/(2k-1). The only
estimate on this q-norm supplied by (9) and support is

    ||A_t||_q <= n^(1/2-1/(2k)) ||A_t||_2.

With L=N^2/Z, Theorem T therefore gives, away from the separately available
rapid-decay factor,

    |I| << (1/X+1/Y)^(1/2)
                    N^(1/2-1/(2k))(N+L^k)^(1/(2k)).     (10)

This keeps the full support price. In the range N>=1, L>=0,

    N^(1/2-1/(2k))(N+L^k)^(1/(2k))
                            >= (N+L)^(1/2)/sqrt(2).     (11)

Indeed if L<=N its left side is at least sqrt(N); if L>=N it is at least
sqrt(L), since N^(1/2-1/(2k))>=1. Hence (10) cannot improve the POWER of the
k=1 norm-product estimate merely by raising k. Arbitrarily rapid decay when
Z>>N^2 is already available at k=1 and does not evade the separate Poisson
comparison. Inequality (11) is an envelope comparison, not an arithmetic
lower bound on I. Better signed pairing, an actual stronger q-norm theorem
for A, or a different zero-sensitive projection remains possible.

In particular, the new fourth-theta-moment saving in Theorem T is real but
is canceled by this support price in the naive Holder composition. Omitting
the price would manufacture a spurious critical-line proof. One negative
control in the checker explicitly rejects that omission.

## 5. An optimistic all-order budget still stops above the critical line

This is a LIMITED exponent-model theorem, not a lower bound for I or a
no-go theorem for RH. Grant a substantially stronger situation than proved:
all nonprincipal denominators can be moved as far as x=1/2 plus a fixed
positive buffer; there are no exceptional-row costs; and every needed
positive numerator moment is diagonal-sized on the right of 1/2. Even these
grants leave the full-good-class absolute first mean of order U, and the
same z=1/6 principal detector normalization. They do not grant signed
cancellation of the row sum or a different principal projection.

Write X=Z^alpha, Y=Z^beta, M=alpha+beta, h=1-alpha. For the regime 0<alpha<1
of the usual Poisson cutoff U=Z^h, the Mellin shift is

    b=5/6-alpha/3.

For 1/2<=M<=1, the positive theta estimate has exponent
Theta=max(alpha,beta)/2. The optimistic full-good-class estimate on the
critical numerator/denominator lines has exponent G=(1-M)/2. Moving the
numerator to y<1/2 does not improve it: even perfect right-half-plane
moments and the functional equation give first mean U^(3/2-y), hence
G(y)=x+1/2-M+(M-1)y, minimized at y=1/2 when M<=1. For y>=1/2 the physical
Y cost is minimized at y=1/2 as well.

Thus this optimistic comparison has zero-free BUDGET

    B(alpha,beta)=5/6-alpha/3
          +max(alpha/2,beta/2,(1-alpha-beta)/2).          (13)

A positive dual identity proves for every alpha,beta that B>=8/9. The
three displayed affine candidates, with weights 7/9,1/9,1/9 respectively,
sum exactly to 8/9:

    (7/9)(5/6+alpha/6)
     +(1/9)(5/6-alpha/3+beta/2)
     +(1/9)(4/3-5alpha/6-beta/2)=8/9.                   (14)

Equality in the relaxed limiting model occurs at alpha=beta=1/3. This
value is NOT announced as a proved zero-free region; the granted critical
reciprocal control is unproved, and actual exceptional classes also cost.

Neither adjacent support regime avoids this model limitation. If M>=1,
the actual positive theta term has exponent (2M-1-min(alpha,beta))/2;
a direct two-case calculation gives b+Theta>=11/12. If M<1/2, allow the
arbitrary rapid theta decay proved in Theorem T. The unchanged optimistic
good class alone still costs

    b+G=4/3-alpha/3-M/2>=4/3-5M/6>11/12.

Thus the rapid short-support theorem is not a hidden extraction of RH.
The conclusion is only that THIS fixed principal residue, absolute
full-good-class mean and separate positive theta norm cannot reach 1/2,
even after granting perfect all-order numerator estimates. An actual
signed pairing or a genuinely different zero-sensitive projection lies
outside this model and is not ruled out. This is why no further scalar
fraction is the headline of this continuation.

## 6. A precise alternative to more scalar fractions

The #974 principal finite-part identity, read at commit
`89c37b6707cb77fc5a86143ea98d8756759fdcbc`, gives a zero-sensitive first
transverse coefficient equal, after explicit holomorphic normalization, to
-zeta_F^S'(s)/zeta_F^S(s) on 1/2<Re s<1. Its bare normal residue has already
canceled the zeros and is not an acceptable replacement. The physical
monomial there is Z^(-1/2)(Z/Y)^s Y^v, not the old fixed z=1/6 residue.

This is a different candidate for using the theta hierarchy: an estimate
for the FIRST TRANSVERSE FINITE PART with a bounded projection norm, or a
controlled remainder whose norm grows only subexponentially in the native
moment order. The present Lp estimate is in the physical row variable, not
a bound on that meromorphic transverse extraction. We did not establish
such a projection. We therefore publish the actual all-moment theorems,
the exact failed shortcut, and the remaining native estimate rather than
announcing another fraction near 0.9 or claiming a descent to 1/2.
