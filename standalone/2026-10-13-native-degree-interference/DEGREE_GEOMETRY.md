# Exact prime-degree interference on the physical sextic rows

Status: proposed finite identities and fully enumerated finite computations.
No asymptotic native moment bound or RH conclusion. Proof and code have the
same author; the second checker is an independent assembly, not an independent
arithmetic backend or mathematical referee.

The computation uses the exact #942 helper, Git blob
2a074ccede483324392a729056ccbf43a1f26eac, recovered unchanged in the adjacent
matching-geometry directory. All numerical claims below are integer/rational
identities on their complete stated finite domains.

## 1. Grade the FULL product rather than its prime-selected part

Let the original squarefree ideal columns have fixed real weights W_n,
supported on Nn<=X. For the census W_n is the hard window D/2<Nn<=D.
The fixed twist is trivial. Put

 C_j(u)=sum_{omega_K(n)=j} W_n chi_n(u),
 P_u(z)=sum_j C_j(u) z^j.

Thus the full native Möbius sum is P_u(-1), and the unsigned-squarefree sum
is P_u(1). No prime or composite degree is omitted. For fixed k, write

 P_u(z)^k=sum_j B_j(u) z^j,
 G_{j,l}=sum_u w(u) B_j(u) conjugate(B_l(u)),   w(u)>=0.

Then the COMPLETE physical moment is exactly

 M_{2k}(z)=sum_{j,l} z^j conjugate(z)^l G_{j,l}.               (1.1)

G is a positive semidefinite Hermitian matrix. This is ordinary Gram algebra,
not an arithmetic upper bound. Its dimension is at most k J(X)+1, where
J(X)=max_{Nn<=X,n squarefree} omega_K(n)=O_K(log X/log log X).
For the last bound, ideal counting gives the j-th distinct prime norm at
least j/C_K, so a product of j such norms is at least j!/C_K^j. Taking
logarithms gives the asserted estimate. No growing-order estimate for G follows.

If the columns and rows are invariant under field conjugation, G is real:
conjugating every ideal and element conjugates the product and reindexes the
whole sum. This holds for the complete norm windows and sharp norm balls used
here. Arbitrary twists/exclusions need not retain that realness.

For |z|=1, write z=exp(it), R_l=sum_j G_{j,j+l}. Then

 M_{2k}(exp(it))=R_0+2 sum_{l>=1} R_l cos(lt),
 M_{2k}(-1)=R_0+2 sum_{l>=1}(-1)^l R_l.                      (1.2)

R_0 is exactly the moment averaged over the single GLOBAL prime phase t.
It is not the principal character reference: equal prime degree does not
imply equal ideal product or principal sextic charge. No independence of
prime phases or physical row equidistribution has been invoked.

## 2. Unit symmetry gives six exactly orthogonal blocks

Let epsilon=1+omega be the complex sixth root of unity and define, for every
good ideal (including nonsquarefree products),

 t(n)=((Nn-1)/6) modulo 6.

Every good prime-ideal norm is 1 modulo 6. The local residue definition gives
chi_p(epsilon)=epsilon^((Np-1)/6). Complete multiplicativity, with zeros
retained, gives

 chi_n(epsilon u)=epsilon^{t(n)} chi_n(u).                   (2.1)

The formula for t is additive modulo six because
(1+6a)(1+6b)=1+6(a+b) modulo 36. Equal-norm conjugate ideals are NOT identified;
only this finite label agrees for them.

Refine C_j and B_j by the type a in Z/6Z. If the physical row weight is
unit-invariant, then

 sum_u w(u) B_{a,j}(u) conjugate(B_{b,l}(u))=0  when a!=b.    (2.2)

Indeed multiplication of every row by epsilon multiplies that sum by
exp(2pi i(a-b)/6) while leaving its value unchanged. Therefore

 G=sum_{a mod 6} G_a

is an exact six-block compression of the same full moment. Equation (2.2)
is checked with literal characters, including zero values. Unit symmetry
saves work and removes impossible cross terms; it supplies no power saving
for the remaining blocks.

## 3. Resolve the complete singleton union at order four

For a pair product f=n_1 n_2, let m(f) count its ordered factorizations in the
original window. All prime exponents in f are at most two. Pair products
f,g specify a no-singleton quartet exactly when every prime occurring once
in f occurs in g, and every prime occurring once in g occurs in f. Primes
occurring twice in one product and zero times in the other are permitted.
This criterion loses no overlaps and is not merely a selected matching.

Let N be the analogue of G retaining precisely these no-singleton pairs.
The remaining singleton matrix is S=G-N. With v_j=(-1)^j,

 M_4(native)=v^T G v,
 N_4(native)=v^T N v,
 S_4(native)=v^T S v.                                      (3.1)

Neither N nor S is asserted positive semidefinite. For squarefree fourth
moments principal pairs are exactly f=g, because differences of their prime
exponents lie between -2 and 2. This special fact is not used at higher orders
or for unrestricted Liouville columns.

The implementation groups by product IDEAL using prime-index tuples, retains
its full multiplicity and unit type, and evaluates every permitted pair over
ALL rows. Each complete character kernel retains zeros from the union of the
two product supports. A separate ordered-quartet loop checks this assembly
on the small cases; the principal subtotal is checked against the earlier
independent divisor-mask formula.

## 4. A true finite counterexample to a Möbius-phase minimum principle

At D=256 and H=338, include all 37 good squarefree columns in
128<Nn<=256 and all 1,236 nonzero rows with Nu<=338. Only prime degrees one
and two occur in individual columns. In product degrees j=2,3,4, the complete
real Gram matrix is

 G = [[1259340, 260616, 133698],
      [ 260616,1720944,  99228],
      [ 133698,  99228, 493254]].                            (4.1)

With x=Re z on the unit circle, its complete fourth moment is

 F(x)=3206142+719688 x+534792 x^2.                           (4.2)

Consequently

 F(-1)=3021246,
 F(-2/3)=8892106/3,
 F(-1)-F(-2/3)=171632/3>0,
 F'(-1)=-349896<0.                                         (4.3)

The alternative phase is exactly z=(-2+i sqrt(5))/3. Thus z=-1 is not even
a local minimum on this finite circle, and is not a global minimum. The
checker independently evaluates the complete moment in the exact algebra
Q[omega,Z]/(omega^2+omega+1,Z^2+4Z+9), with z=Z/3. It does not accept a floating
optimizer's residual or a selected row subset as the counterexample.

This refutes that proposed FINITE phase-minimum principle only. These
coefficients are changed when z!=-1; the example does not refute the native
moment conjecture. It also does not imply a better ASYMPTOTIC exponent at a
fixed alternative phase. MICROSCOPIC_PHASE.md explains that distinction.

At the same D,H, the complete no-singleton contribution is 3,035,334,
so the complete native singleton contribution is -14,088. The singleton
matrix has S_{4,4}=-9,744, hence is not positive semidefinite. At D=64,H=79,
the complete singleton contribution is instead +2,496. Thus neither
universal nonnegativity nor universal nonpositivity of this whole signed
sector is available even on the actual unmodified finite data.

## 5. Large degree energies almost cancel at the largest enumerated scale

The complete degree census covers D=64,128,...,8192 at
H=ceil(D^(21/20)), plus the retained sharp-height D=H=512 pilot.
It includes every good squarefree ideal column in each hard annulus and every
nonzero Eisenstein row in the stated norm ball. The degree Gram is complete
through D=8192; the separate singleton resolution is complete only through
D=1024. Those are different coverage limits and are recorded per case.

At D=8192,H=12855:

 rows                     46608
 squarefree columns        1145
 native M4                 114923460372
 sum of degree energies   1652703692676
 cross-degree contribution -1537780232304.

The off-degree terms cancel approximately 93.0463% of the diagonal degree
energy. The full native value agrees exactly with the prior #942 census.
This is a finite observation of cancellation, not a rate, an upper bound at
unbounded scales, or evidence that the cancellation margin is uniform in k.

The following smaller cases retain the whole singleton/no-singleton split:

 D     H       native M4      no-singleton     singleton
 64    79          26472           23976          2496
128   164         359664          382968        -23304
256   338        3021246         3035334        -14088
512   700       24073938        25261602      -1187664
1024 1449      181593786       185445018      -3851232.

All retained cases, not just favorable signs, are in results.json.

## 6. Attempt boundary

At the exact degree level the missing bound is v^T G v<<HD^(k+epsilon), with
v_j=(-1)^j, whereas the diagonal phase average is trace G. Replacing v by an
arbitrary vector or taking trace G loses the observed cancellation. Positivity
of G does not compare these two values in the favorable direction. Likewise
the singleton difference G-N is not a positive form.

This is a compact way to measure the full signed arithmetic target and test
false closure principles. It is not a new upper-moment theorem. The scalar
Euler deformation and sixth-power copying barriers in #933/#935 are credited;
the exact physical Gram, complete singleton census, and finite phase witness
are the additional work recorded here.
