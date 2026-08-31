# An effective full-support minor for the native physical source

This theorem uses the executed fixed-shift certificate to make the
one-sided existence result effective. It concerns the fixed primes 2,3,5,
their literal source, and the full complex tensor observation. Its finite
horizon bounds are deliberately very conservative.

The four-file computational contract is frozen at
`c6610c2f8e08cc838de6f81802e21633ccb04fd0`:
`native_full_support_minor.py`, `FULL_SUPPORT_MINOR_PREREGISTRATION.md`,
`FULL_SUPPORT_MINOR_REPLAY.md`, and
`tests/test_native_six_hour_full_support_minor.py`. Its resulting artifact
`native_full_support_minor.verification.json` is frozen at
`0103b95130de0f8151c529a0911a52842732227d`, with proof-object SHA256
`b036cc774cee43b10652efdf40a81c89d5913a388dc84e629d1d0fcc42b50109`.
The root reports successful write, check, optimized check, and all twelve
controls in ordinary and optimized modes. This note adds a proof-only
row-norm refinement; it does not change that registered artifact.

## 1. Literal source and the coordinate change

The source is L-102707 at
`ec6635b4c7dcd08fe433b7ae7e1d9a8c9495dfcc`, blob
`6810bcece309b0c54ae6c8fc84b314990004549c`. The fixed-prime completion and
original physical normalization are frozen at
`822646ffea23d906c385f0273a8c45693e982c4d` in
`FIXED_PRIME_INFINITE_HORIZON_COMPLETION.md` and
`INFINITE_NATIVE_PHYSICAL_FAITHFULNESS.md`. The exact 1/d alias formula is
also authenticated by the contract against the literal helper at
`3ba479241acf9db1554af067d5e2bea85533dde5`.

Write

    A(z)=sqrt(1-z^2), C(z)=sqrt(1-z),
    ell_u(z)=(1-u)A(z)+u C(z),
    S(u,z)=product_(i=1)^3 ell_(u_i)(z_i).

All square roots have value 1 at zero. Let v_n denote the eight-entry
coefficient vector in the declared (A,C) tensor basis. If v_n^orig is the
vector for the original monomial schedule basis (1,u), then

    v_n^orig=T v_n, T=[[1,0],[-1,1]] tensor power 3.

Consequently the original path matrix and the declared matrix are related
by the exact congruence

    M_orig[a,c]=2 integral d(u^a) u^c,
    M_AC=T^t M_orig T.

Equivalently M_AC[a,c]=2 integral d(psi_a) psi_c, with local schedule
basis psi=(1-u,u). Thus no current factor, path, or physical weight is
changed by choosing (A,C) columns.

For any constant complex eight by eight matrix M in these declared
coordinates, the original tensor field at horizon H is

    F_H(M)(t)=sum_(nm<=H) (v_n^t M v_m)/sqrt(nm) * (n/m)^(it).

There are 64 independent tensor entries in this assertion. They are not
being identified with 64 actual curvature directions: the three-schedule
path-variation space has dimension 20 and embeds in this tensor space.

## 2. The actual 64 rows and their certified infinite inverse

Use exactly the 64 denominator labels

    b=2^beta_1 3^beta_2 5^beta_3,
    (beta_1,beta_2,beta_3) in {1,2,3,4}^3.              (1)

Every label is divisible by 30 and the largest is 30^4=810000. At the
physical ratio 1/b the field's Fourier coefficient is

    b^(-1/2) R_(H,b)(M),
    R_(H,b)(M)=sum_(d^2 b<=H) (v_d^t M v_(db))/d.      (2)

The matrix R_H in this note is the unscaled 64 by 64 matrix in (2).
Physical row scaling by b^(-1/2) is nonzero, so it preserves rank.
The sum is over d supported on 2,3,5; no arithmetic alias is dropped.

For one prime put q=1/p and f_0=A,f_1=C. The infinite local matrix has
rows beta=1,2,3,4, columns (AA,AC,CA,CC), and entries

    K_p[beta,(i,j)]
      =sum_(k>=0) q^k f_(i,k) f_(j,k+beta).             (3)

Here q=1/p, not 1/sqrt(p): the latter enters only the physical row
scaling. Indeed w=p^(-1/2) exp(-it log p) makes the positive Laurent
power w^beta correspond to the ratio 1/p^beta. Equation (3) is its exact
unscaled coefficient.

The executed certificate constructs the partial sum through k=64,
reconstructing coefficients only through 68. Since |f_(i,k)|<=1, each
entry tail is bounded by t_p=q^65/(1-q). Both inverse identities of
each partial matrix were checked exactly. For

    eta_p=|| |K_(p,64)^(-1)| (t_p times all-ones matrix) ||_infinity,

all three strict comparisons eta_p<1 passed. The stored rational bounds
||K_(p,64)^(-1)||_infinity/(1-eta_p) have certified integer ceilings

    p:                     2    3     5
    inverse-norm ceiling: 541  752  1189.

Neumann's lemma therefore proves that each actual infinite K_p is
invertible, with the indicated upper bound on its inverse norm.
Absolute convergence factors the complete aliases in (2), so, in the
declared tensor order,

    R_infinity=K_2 tensor K_3 tensor K_5,
    ||R_infinity^(-1)||_infinity
      <= B=541*752*1189=483723248.                     (4)

No local shift was selected after seeing the comparisons. Singular or
noncontractive partial matrices would have remained UNKNOWN under this
contract; the recorded outcome is that the specified three panels passed.

Thus the actual 64 full-support rows (1) distinguish all 64 tensor
coordinates at infinite horizon. In particular they distinguish all
20 actual curvature directions. Selecting a rank-20 subfamily is possible,
but this certificate does not select or claim a particular 20-row subset.

## 3. The registered finite-horizon conclusion

The absolute coefficient sums of A and C are each 2. Tensoring gives

    S=sum_n ||v_n||_1=4^3=64.                          (5)

For d^2 b>H, one has 1/d<sqrt(b/H). Bounding a single omitted matrix
entry by S^2 sqrt(b/H), and then summing 64 columns, gives the registered
bound

    ||R_H-R_infinity||_infinity <= L_0/sqrt(H),
    L_0=64*900*64^2=235929600.

With B from (4), the executed artifact records the exact integer

    H_0=floor((2 B L_0)^2)+1
       =52097726892094636089489814978560001.            (6)

For every integer H>=H_0 the comparison
||R_infinity^(-1)(R_H-R_infinity)||_infinity is strictly less than 1/2.
Hence R_H is invertible at every such horizon. This is a proved
all-future conclusion, not an enumeration of these horizons.

## 4. A separate analytic row-norm refinement

The extra factor 64 in L_0 can be removed by summing column absolute
values before bounding the alias tail. For a fixed denominator b,

    sum_(a,c) |(R_H-R_infinity)[b,(a,c)]|
      <=sum_(d^2 b>H) ||v_d||_1 ||v_(db)||_1 / d
      <=sqrt(b/H) sum_d ||v_d||_1 ||v_(db)||_1
      <=sqrt(b/H) S^2.                                (7)

The last inequality follows from nonnegativity and the bound by the
product of the two sums; both are at most S. It does not assume that
the finite hyperbolic cutoff factorizes. Therefore

    ||R_H-R_infinity||_infinity <= L_1/sqrt(H),
    L_1=900*64^2=3686400.

The same certified inverse bound (4) now gives the strictly improved,
still conservative analytic threshold

    H_1=(2*541*752*1189*3686400)^2+1
       =(3566394762854400)^2+1
       =(H_0-1)/4096+1.                               (8)

For every integer H>=H_1 the unscaled matrix R_H, and hence the physical
64-row matrix, is invertible. Equation (8) is a proof-only consequence
of the accepted certificate and (7); it is not a new producer output or
a revision of the preregistered H_0 record. No additional computation is
used to derive it.

## 5. A stronger bound using full prime support

The fact that all three beta_i are positive yields a substantially better
constant. Write a_n=[z^n]A(z), c_n=[z^n]C(z), and u_n=|a_n|+|c_n|.
The exact recurrence for c_n gives strictly decreasing |c_n| for n>=1.
For odd n>=1, a_n=0 and u_n<=1/2. For even n=2k>=2,

    u_(2k)=|c_k|+|c_(2k)|<=|c_1|+|c_2|=1/2+1/8=5/8.

Thus u_n<=5/8 for every positive local exponent n. This does not include
u_0=2. It is precisely the full-support assumption that permits its use:
for every supported d and every selected b in (1), the three exponents
of db are positive. In the declared (A,C) tensor basis,

    ||v_(db)||_1=product_(i=1)^3 u_(ord_(p_i)(db))<=(5/8)^3.

Consequently the last sum in (7) satisfies the stronger uniform bound

    sum_d ||v_d||_1 ||v_(db)||_1
       <=S*(5/8)^3=64*125/512=125/8.

There is still no factor 64 for the number of columns: it has already
been included by summing all column absolute values inside (7). Therefore

    ||R_H-R_infinity||_infinity <= L_2/sqrt(H),
    L_2=900*125/8=28125/2.

With exactly the same accepted inverse bound B, define

    H_2=(2 B L_2)^2+1
       =(28125*483723248)^2+1
       =(13604716350000)^2+1.                          (9)

For every integer H>=H_2, the comparison to R_infinity is strictly less
than 1/2, so all 64 full-support physical rows are independent on the
64-dimensional tensor space. In particular the original 20 curvature
directions are distinguished. This stronger H_2 is another exact analytic
corollary, not an acquisition result, replacement of H_0, or bound obtained
by fitting further numerical cases. It uses the original declared source
coefficients and the full-support property of the already fixed labels.

## 6. Limits of the conclusion

The theorem supplies a concrete replacement for a singular limiting
minor. It does not rescue the former pure-prime-heavy 20-row selection,
alter any of its UNKNOWN tail results, or assert invertibility of that
former selection at all finite horizons.

None of H_0, H_1, H_2 is claimed to be optimal or close to a first full-rank
horizon. The independent literal/physical rank result at H=450 concerns
the 20-dimensional actual curvature space and a different bounded
observation; it is not a first-threshold claim for this 64-row tensor
matrix. No untested interval below H_2 is filled by the present theorem.

The input here is the original field, or its specified frequency
coefficients, not its single scalar energy. No stable recovery from a
finite weighted interval, uniformity in a growing prime set, source
identification for the full retained-gamma object, or new global energy
minimum is asserted.
