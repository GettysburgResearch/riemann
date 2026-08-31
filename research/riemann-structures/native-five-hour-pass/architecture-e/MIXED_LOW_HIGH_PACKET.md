# One low node coupled to three high nodes

Status: PROPOSED source-exact mixed-domain theorem; review/replay pending.
Scope: one node in[1/2,256], at most three other nodes>=2^30, and all partial
confluences within the high cluster. No claim covers two low nodes.
Declared before the new bounded mixed-domain acquisition.

## 1. Statement and dependence

Use Y(x)=xi(1/2+x), F=Y'/Y, H(x,y)=(F(x)+F(y))/(x+y) and C(x,y)=1/(x+y).
Assume the E4 theorem and finite-space identities in FOUR_NODE_HIGH_AXIS.md.
Its exact frozen pin will be recorded before the mixed producer accepts.

**Theorem EM.** If x is real with1/2<=x<=256 and each of at most three real
nodes y_j satisfies y_j>=2^30, then

    [H(z_i,z_j)] >=(1/100)[C(z_i,z_j)], z=(x,y_1,...,y_m).       (EM.1)

The high nodes may coincide in the exponential-jet/Newton interpretation.
The low node is separated from them by the declared gap. In particular, for
four distinct nodes the last normalized Newton Schur residual is at least

    1/[200 z_4 product_(i<4)(z_i+z_4)^2].                     (EM.2)

The endpoint x=1/2 is included by actual-source analyticity, without using a
divergent Euler series there. Ordinary safe-axis applications may restrict
to x>1/2.

## 2. The actual theta source controls the low scalar

The pinned PR765 actual kernel is Phi=2phi_0, where for u>=0

    phi_0(u)=sum_(n>=1)
      [2pi^2 n^4 exp(9u/2)-3pi n^2 exp(5u/2)]
                                  exp[-pi n^2 exp(2u)].

Its even extension is strictly positive and has superexponential tails.
The source proof establishes Y(x)=integral_R Phi(u)exp(xu)du. Consequently

    F'(x)=Var_(Phi(u)exp(xu)du/Y(x))(u)>0,        F(0)=0.

All differentiation is justified by the original two-sided tail bounds.
Thus F is strictly increasing on the real axis; no zero-location theorem
or generic assertion about positive kernels is used.

At the endpoint, the Laurent coefficient of zeta at1 and the gamma
duplication identity give

    F(1/2)=xi'(1)/xi(1)=1+gamma/2-(1/2)log(4pi).              (EM.3)

Here gamma is Euler's constant. The following exact elementary bounds suffice:

    gamma>57/100,       log(4pi)<127/50,
    hence F(1/2)>3/200.                                    (EM.4)

To prove the first, convexity of1/t on each[k,k+1] gives

    H_N-log N-gamma
      =sum_(k=N)^infinity [log(1+1/k)-1/(k+1)] <1/(2N).

Take N10. The positive Taylor polynomial for exp(2303/1000) through degree16
is greater than10, so log10<2303/1000. Therefore

    gamma>H_10-2303/1000-1/20>57/100.

For the second, pi<22/7 and the positive degree16 Taylor polynomial for
exp(127/50) exceeds88/7. These rational comparisons are separately replayed.

For y>=256, the literal E4 scalar gamma/prime decomposition, discarding only
nonnegative scalar subtractions, gives

    0<F(y)<(1/2)log(2y)+1.                                 (EM.5)

Indeed the two positive rational terms total less than1, and the logarithm
argument (y+1/2)/(2pi) is less than2y. At y256 we can instead use
log(256+1/2)<log257<6: the degree7 Taylor polynomial for exp6 exceeds257.
The rational terms still total less than1, so F(256)<4. Hence

    3/200<F(x)<4       for1/2<=x<=256.                      (EM.6)

The prime-pole cancellation at x=1/2 is never split into two unbounded terms.

## 3. Exact block elimination

Order the finite orthonormal exponential basis with the low node first.
The E4 source matrix is

    A = [ x  v ; 0  B ],

where B is the same Malmquist matrix for the high node list, and
v_j=2sqrt(x y_j). The high block is unitarily represented by the corresponding
standalone high-node source space. Define r=v(B-xI)^(-1). An exact triangular
similarity gives

    F(A) = [ F(x)  w ; 0  F(B) ],
    w = rF(B)-F(x)r.                                       (EM.7)

The explicit row is

    r_j=2sqrt(x y_j)/(y_j-x)
            product_(k<j) [-(y_k+x)/(y_k-x)].                (EM.8)

The product sign is material. It follows either by direct substitution into
r(B-x)=v or from the E4 resolvent product. None of these formulas uses a
closed ambient operator, and F is holomorphic around the finite spectrum,
including the low endpoint by xi's regular value there.

For R>=2^16, x<=256 and all y_j>=R, set a=256/R<=1/256. There are at most two
intermediate factors, so

    |r_j| <=32/sqrt(y_j) * (256/255)*(257/255)^2
           <36/sqrt(y_j).                                 (EM.9)

This retains arbitrarily large ratios among the high nodes and their collisions.

## 4. Uniform high-block entries with both source remainders retained

E4 gives Re F(B)>=1/8. Its source decomposition also gives every strictly
upper-triangular entry the bound |F(B)_ij|<2. For completeness, the separate
bounds at minimum node256 are

    logarithmic term <=1,
    (B-1/2)^(-1) entry <= its norm <1/32,
    (B+1/2)^(-1) entry <=7/256,
    gamma remainder entry <=27/256,
    prime remainder entry <1/1024.

Their sum is1193/1024<2. The positive-shift resolvent bound follows from
the product formula: diagonal<=1/(R+1/2), off-diagonal<=2/(R+1/2), and
at most four entries in a row or column. The slightly larger n4 constant
is harmless for this block of dimension at most3. Thus neither the
archimedean nor the Euler-prime contribution is omitted.

Using (EM.5), (EM.6) and (EM.9) in the literal row (EM.7), for each j,

    |w_j| <=36[(1/2)log(2R)+9]/sqrt(R).                     (EM.10)

There are at most two earlier high indices, each costing
2*36/sqrt(R); the diagonal contributes
36[(1/2)log(2y_j)+1]/sqrt(y_j), and the low scalar contributes
4*36/sqrt(y_j). The function[(1/2)log(2y)+1]/sqrt(y) decreases for y>1/2,
which justifies the uniform replacement y_j->R.

Since sqrt(3)<2, at the preregistered R=2^30 and using log2<1,

    ||w|| <36[log(2R)+18]/sqrt(R)
           <1764/32768<1/16.                               (EM.11)

These are analytic bounds; no packet eigenvalue is sampled.

## 5. The Schur estimate

Subtract delta=1/200 from Re F(A). Its low diagonal is greater than1/100,
its high block is at least(1/8-1/200)I=(3/25)I, and its off-diagonal block
has norm less than||w||/2<1/32. The exact comparison

    (1/100)*(3/25)=3/2500>1/1024=(1/32)^2

therefore makes the block Schur complement positive. Thus

    Re F(A)>(1/200)I.

The literal Gram identity gives (EM.1). Variational Schur complements and
the normalized Cauchy determinant give (EM.2). The high-node confluent
statement follows directly from the finite jet-space construction, without
a divided-difference condition-number assumption.

## 6. Source and evidence boundary

Actual theta source: PR765 at8f01064df805624c045877655893c324a220975d,
research/exploratory/XI_ACTUAL_KERNEL_LAPLACE_CONCENTRATION.md,
blob fa24f9c8e0a87709d1a297a4e72136c1135d066c, especially XL1--XL4.
Only its source identity, positivity and tail regularity are imported here;
its separate asymptotic concentration theorem is not needed.

The standard xi completion, zeta Laurent coefficient and special digamma
value are classical (DLMF25.4,25.2,5.4). The main high block imports E4's
proved finite-space estimates, not an unverified all-order positivity claim.

The new finite replay checks exact endpoint constants, actual block/resolvent
identities and the final Schur margin. It does not infer continuum source
positivity or all-node estimates from finitely many examples. This result
extends a different part of the domain from E4: one genuinely low node is
allowed. Two or more low nodes, and the intervening moderate high range,
remain outside this theorem. RH remains open.

