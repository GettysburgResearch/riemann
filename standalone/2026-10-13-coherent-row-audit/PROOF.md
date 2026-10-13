# Coherent sixth-power rows and the degree Gram: an exact separation

Status: PROPOSED component mathematics with complete proofs at the stated scope.
The new finite census is exact. The asymptotic corollary below uses a named
classical Mobius estimate, not RH. No full native moment or improved zero-free
exponent is proved. Author and computational checker author are the same;
independent mathematical review remains required.

## 1. Source and normalization

Let K=Q(omega), O=Z[omega], N(a+b omega)=a^2-ab+b^2. Ideals, not generators,
index the columns. S is a fixed finite prime-ideal set containing the primes
above 2 and 3. Use the literal sextic residue symbol chi_n(u), multiplicative
on squarefree good ideals, with value ZERO when (n,u)>1.

Fix a nonnegative real W supported in [a,b], 0<a<b<infinity, of bounded
variation, with integral W(t)dt>0. Smooth compact tests and the hard window 1/2<x<=1 are both allowed.
Take the trivial fixed twist in the statements involving positive profiles.
For D>=2 define

    C_j(u)=sum_{n squarefree, (n,S)=1, omega_K(n)=j}
                       W(Nn/D) chi_n(u),
    P_u(z)=sum_j C_j(u) z^j,
    P_u(z)^k=sum_j B_j(u) z^j.                              (1.1)

Here k>=1 is fixed. The native polynomial is P_u(-1). If J is the maximum
number of prime ideals in a supported column, B has m=kJ+1 coordinates, with
zero coordinates retained. For any nonnegative row measure w of finite mass,

    G_{jl}=sum_{u!=0} w(u) B_j(u) conjugate(B_l(u)),
    v_j=(-1)^j,
    M=v*Gv,        T=trace(G),        O=M-T.                 (1.2)

(The notation v* means conjugate transpose; v is real.) The bounded column
support and finite row mass justify every exchange. G is positive semidefinite.
T is the moment averaged over ONE GLOBAL phase z on the unit circle. It is NOT
an independent-prime moment or the principal-tuple reference.

The complete degree Gram is inherited from #943, DEGREE_GEOMETRY.md Sections
1--2 at 24cb2cdd6e768c2c35ef87227ed8319cfc2d14ed. The new step separates its
actual coherent physical rows, rather than treating the size of O as a proxy
for the unresolved conductor covariance.

## 2. A rank-one physical contribution, with exact masks

Put c_j=C_j(1), c(z)=sum c_j z^j, and let V be the coefficient vector of c(z)^k.
Then c_j>=0. Let R be ANY set of actual rows u=b_0^6 such that every prime ideal
of (b_0) is in S. Write Z_R=sum_{u in R}w(u).

### Theorem 2.1 (exact coherent-row separation)

    G_R=Z_R V V^T,       G=G_R+G_{R^c},       G_{R^c}>=0,    (2.1)
    M_R=Z_R |A_1(D;W)|^(2k),
    T_R=Z_R ||V||_2^2,
    O_R=-T_R+Z_R |A_1(D;W)|^(2k),                           (2.2)

where A_1(D;W)=sum mu_K(n) W(Nn/D), over good ideals.

Proof. Every supported n is coprime to b_0. At each prime of n, the sixth power
b_0^6 is a unit sixth power, so chi_n(b_0^6)=1. Thus C_j(u)=c_j and B_j(u)=V_j,
with no zero erased. Summing the identical outer products proves (2.1).
The complement is a sum of actual nonnegative-weight outer products, hence
positive semidefinite. Evaluating at -1 gives (2.2). QED.

This rank-one removal is a ROW restriction. It is not subtraction of the
principal part of a character expansion in COLUMN tuples. Those operations
have different meanings and, in general, different sizes and signs.

For the minimal excluded set S={p_2,p_3}, with Np_2=4 and Np_3=3, the complete
S-supported sixth-power rows are

    R_S(H)={64^a (-27)^b : a,b>=0, 4^a 3^b <= H^(1/6)}.    (2.3)

Indeed 2^6=64 and (1-omega)^6=-27. Six generators of one ideal have the SAME
sixth power; ideals above conjugate split primes are not identified.
At H=12855 the exact list is {1,-27,64}. At this height these are also ALL
sixth-power rows: the sixth root's ideal norm is less than 7, and only norms
1,3,4 are available. Multiplication of u by an arbitrary unit is NOT included
in the definition of a sixth power; for example -1 is not b_0^6 in K.

Counting the integer points in the triangle in (2.3) also gives

    #R_S(H)=(log H)^2/(72 log 4 log 3)+O(log(2H)).            (2.4)

The main area follows by replacing a,b with real nonnegative variables; the
boundary intersects O(log H) unit squares. This is only a count of this small
row subset, not a description of all sixth-power replicas.

## 3. A classical, unconditional explanation of near-total degree cancellation

### Lemma 3.1 (two scalar estimates)

For the fixed S and W,

    U(D):=c(1)=c_{S,W}D+O_{S,W}(sqrt(D) log(2D)), c_{S,W}>0,
    |c(-1)| <<_{S,W,A} D/(log(2D))^A   for every fixed A>0. (3.1)

The second assertion imports only the classical Mobius estimates (1.1)--(1.2)
on page 2 of Green--Tao, *Quadratic Uniformity of the Mobius Function*,
arXiv:math/0606087v2. It does not import that paper's quadratic nilsequence
theorem. Here are complete adapters to the present field and exclusions.

For the first assertion, the ideal count is

    I_K(x)=c_K x+O(sqrt(x)),       c_K=pi/(3 sqrt(3)).

This follows by counting Eisenstein lattice points in a disk, with an O(sqrt(x))
boundary-square error, and dividing by the six units. Inclusion-exclusion of
a FIXED S gives the analogous count for ideals coprime to S. Use
mu_K(n)^2=sum_{d^2|n}mu_K(d). The main sum over d is absolutely convergent;
the error is O(sqrt(x) sum_{Nd<=sqrt(x)}1/Nd)=O(sqrt(x) log(2x)), and the
main-series tail has size O(sqrt(x)). Thus the squarefree good density is

    c_K / zeta_K(2) * product_{p in S}(1+1/Np)^(-1)>0.

Partial summation against W proves the first line of (3.1), with that density
multiplied by integral W(t)dt.

For the second, zeta_K(s)=zeta(s)L(s,chi_-3) on Re(s)>1, as checked directly
at split, inert and ramified rational primes. Accordingly the norm-grouped
coefficients of 1/zeta_K are the convolution mu*(mu chi_-3). The classical
bounds cited above give, for each B>0,

    sum_{n<=x}mu(n), sum_{n<=x}mu(n)chi_-3(n) <<_B x/log^B(2x).

The Dirichlet hyperbola decomposition of their convolution at sqrt(x) gives
O_B(x/log^(B-1)(2x)): in the two long inner sums, their arguments are at least
sqrt(x), and summing 1/n costs at most log(2x). The square overlap has the same
or a smaller bound. B may be chosen arbitrarily large.

Excluding S multiplies the reciprocal Euler series by
product_{p in S}(1-(Np)^(-s))^(-1). Its norm-grouped coefficients are the
positive S-supported ideal counts. In their dilation convolution split at
Nd=sqrt(x). For Nd<=sqrt(x), sum 1/Nd is bounded by the fixed convergent finite
Euler product at 1. The rest has sum 1/Nd <= x^(-1/4) sum_S (Nd)^(-1/2), by
positivity, so contributes O_S(x^(3/4)) using the trivial ideal bound.
This preserves every logarithmic saving. Partial summation proves the
second line of (3.1) for bounded-variation W. These arguments also retain
split-prime norm multiplicities; they do not replace mu_K by mu of the norm.
QED.

### Theorem 3.2 (all fixed orders on the specified physical row sector)

For the R of Theorem 2.1 with Z_R>0, and every B>0,

    T_R >= c_{k,S,W} Z_R D^(2k)/(kJ+1),                     (3.2)
    0 <= M_R/T_R <<_{k,S,W,B} (log(2D))^(-B),              (3.3)
    O_R/T_R=-1+O_{k,S,W,B}((log(2D))^(-B)).                (3.4)

These are asymptotic statements for each fixed k; no uniform growing-k constant
is asserted.

Proof. Nonnegativity of the V_j gives sum V_j=U(D)^k. Cauchy gives
||V||_2^2 >= U(D)^(2k)/(kJ+1). Lemma 3.1 proves (3.2).
Ideal counting bounds the j-th smallest distinct prime-ideal norm below by
j/C_K'. Their product is at least j!/(C_K')^j, hence a column of norm <=bD
has J=O_K(log(2D)/log log(3D)). The second line of (3.1), with its arbitrary
A, and (2.2)--(3.2) give (3.3). Finally O_R=M_R-T_R proves (3.4). QED.

This is actual signed cancellation on an actual sparse row set. It is much
weaker than square-root Mobius cancellation: D/log^A D is NOT D^(1/2+epsilon).
The statement that a huge degree-diagonal contribution nearly cancels can
therefore be true for entirely classical reasons, without paying the desired
native moment at order four or higher. No asymptotic claim that R dominates
the ENTIRE physical degree Gram is made; that dominance below is finite data.

## 4. Prime sixth-power rows: an approximate rank-one theorem WITH the mask

Let p be a good prime ideal, choose any generator b_p, and let u_p=b_p^6. Then

    chi_n(u_p)=1_{(n,p)=1},
    c_p(z)=sum_{(n,pS)=1} W(Nn/D) z^{omega_K(n)}.             (4.1)

Let V_p be the coefficient vector of c_p(z)^k. Put U=||c||_1 and
Delta_p=||c-c_p||_1. Nonnegative W gives

    0<=Delta_p<=C_{K,W}D/Np,
    ||V-V_p||_1<=k U^(k-1) Delta_p.                         (4.2)

The first estimate counts ideals divisible by p, with all other restrictions
only decreasing the sum. For the second use the telescoping convolution
identity c^{*k}-c_p^{*k}=sum_{r=0}^{k-1}c^{*r}*(c-c_p)*c_p^{*(k-1-r)}
and ||c_p||_1<=U. In fact the coefficient differences are nonnegative.

### Theorem 4.1 (uniform mask-preserving row-collection estimate)

Let P>=2 and let Pset be any finite set of good prime ideals with Np>=P,
whose u_p lie inside the chosen physical row domain. Give them nonnegative
weights of total mass R. Then

    ||G_Pset - R V V^T||_op <= C_{k,K,W} R D^(2k)/P.         (4.3)

All implied constants are independent of the moving primes and row set.
The difference in (4.3) is NOT asserted positive or negative semidefinite.
If P>=D^delta for fixed delta>0 and R>0, then

    trace(G_Pset)=R ||V||_2^2[1+O_{k,K,S,W}((kJ+1)/P)],       (4.4)
    M_Pset/trace(G_Pset) <<_{k,K,S,W,delta,B} log^(-B)(2D)  (4.5)

for every B>0 and large enough D.

Proof. Write d_p=V-V_p. Since ||V||_2<=U^k=O(D^k) and (4.2) implies
||d_p||_2=O(D^k/Np), expansion of the two rank-one matrices bounds their
operator-norm difference by 2||V||_2||d_p||_2+||d_p||_2^2
=O(D^(2k)/Np). Sum with the stated weights. The same bound for the trace
follows directly from the difference of the two squared norms, WITHOUT
multiplying (4.3) by the dimension. Apply (3.2) to obtain (4.4); its
relative constant depends on the fixed S through the positive density c_{S,W}.
At z=-1 the polynomial difference is at most Delta_p. Hence
|c_p(-1)|<=|c(-1)|+C D/P. Use Lemma 3.1 and P>=D^delta, sum its 2k-th power,
and divide by (4.4) and (3.2). This proves (4.5). QED.

For H=D^h, the primes with H^(1/6)/2<=Np<=H^(1/6) give genuine examples of
these rows with polynomial P, as in #941. No estimate of their number is needed
for Theorem 4.1, which is stated in terms of their actual total weight R.
In particular this proof does not erase p's nonunit mask merely because the
row is a sixth power.

## 5. What the complete census actually says

The hard-window census includes ALL squarefree good ideals D/2<Nn<=D and ALL
nonzero Eisenstein elements Nu<=H. It recomputes the full degree Grams and the
fourth-order principal-tuple reference, rather than fitting an asymptotic.

At D=8192,H=12855 the individual column-degree counts are

    (c_1,c_2,c_3)=(459,562,124).

Thus c(-1)=-21, and for k=2 the nonzero entries of V are

    (V_2,V_3,V_4,V_5,V_6)
      =(210681,515916,429676,139376,15376).

The three rows 1,-27,64 give exactly 3 V V^T. The census yields

| Row set | Native fourth moment | Degree-diagonal energy | Signed cross-degree term |
|---|---:|---:|---:|
| All 46,608 rows | 114923460372 | 1652703692676 | -1537780232304 |
| Three sixth powers | 583443 | 1544518075635 | -1544517492192 |
| Other 46,605 rows | 114922876929 | 108185617041 | +6737259888 |

The first row exactly reproduces #943. The separation is new to this packet.
More than the full negative cross-degree total comes from the three explicit
rows. On their complement the cross-degree term has the OPPOSITE sign.
This statement is finite and does not say the complement remains positive as
D grows or for different column tests/twists.

The ACTUAL principal-tuple references and remaining covariances are different:

| Row set | Principal-tuple reference | Native minus that reference |
|---|---:|---:|
| All rows | 114879621108 | +43839264 |
| Three sixth powers | 8416731 | -7833288 |
| Complement | 114871204377 | +51672552 |

At the same D but H=8192, the complement's latter remainder is -1184937090.
Thus even after the coherent-row separation, the actual nonprincipal tuple
remainder still changes sign; no favorable general sign is inferred.

## 6. Consequence for the attack, and the exact unproved estimates

The row split is disjoint and positive at the FULL moment level. For the
complement, Cauchy gives the universally valid bound

    M_Rc <= (kJ+1) trace(G_Rc).                              (6.1)

Consequently simultaneous bounds M_R<<HD^(k+epsilon) and
trace(G_Rc)<<HD^(k+epsilon), with arbitrary epsilon losses, would suffice for
the native moment for this measure and test. NEITHER bound at the required
power is proved here. In particular Theorem 3.2 is only a logarithmic relative
saving, and it does not supply the first bound. The converse implication from
a native moment bound to the trace bound is not asserted.

The useful change is a better diagnostic: measure the native signed conductor
covariance separately from the easily explained coherent degree energy.
The #942 band-limited annihilation and #940 singleton-sector theorem remain
valid at their own stated scopes. This hard-window/sharp-row census does not
numerically implement their Schwartz majorant, and cannot be used as a proof
of their remaining analytic bounds.

No native full fourth/sixth moment, cofinal generalized hierarchy, improved
zero-free half-plane, or RH conclusion is established by this packet.
