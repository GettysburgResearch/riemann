# Mixed Segre ranks and the canonical regularization counterterm

Status: proposed extension of the frozen `(2,3)` source construction at
`4c04db224fedde5d589f05f7183e004a67441a9c`.
Scope: finite lists of positive ranks, complex Hermitian source spaces,
unitary input automorphisms, and explicitly stated operator-ideal disks.
No arithmetic L-function or RH/GRH conclusion is claimed. Classical Koszul,
PBW, and regularized-determinant theory are not claimed as new.

This is a separate extension. The first checkpoint's source, proof, tests,
and fixture remain unchanged. Its [proof](MATHEMATICS.md) supplies the
construction conventions; the frozen precursor at
`8834fdc7a0dfe15f6bb95eefe0729cb77c93c807` supplies the native
simple-negative-root theorem for arbitrary Segre Hilbert numerators.

## 1. Source and the sharp growth parameter for every rank list

Let `s>=1` and let `V_1,...,V_s` be nonzero finite-dimensional Hermitian complex spaces,
`r_i=dim V_i`, and

    R = direct_sum_(m>=0) tensor_i Sym^m(V_i),
    E = tensor_i V_i,
    Q = ker(E tensor E -> tensor_i Sym^2(V_i)).

These formulas define the algebra and its quadratic relations before any
scalar function is selected. It is the iterated Segre product of the
polynomial algebras. Put

    B = T(E*)/(Q-perp) = U(L),
    L = FreeLieSuper(E* odd)/(Q-perp),
    M_n = (L_n)*,       epsilon_n = dim M_n.

The imported Segre-Koszul theorem applies successively to all factors.
The same canonical equivariant Koszul complex and super PBW argument as
in the first checkpoint therefore gives

    F_g(t) := sum_(m>=0) tr(g|R_m)t^m
      = product_(n even) det(1-t^n rho_n(g))
          / product_(n odd) det(1-t^n rho_n(g)),          (1.1)

formally, for `g in product_i U(V_i)`. The norms, naturality, and dual
convention are inherited from the source constructions, without fitting
any new spectral list.

Set `a_i=r_i-1`, `A=sum_i a_i`, `M=max_i a_i`, `D=A+1`, and `d=A-M`.
At the identity,

    F_1(t) = h(t)/(1-t)^D,
    h(0)=1,       deg h=d.                              (1.2)

The precursor's theorem `GLO764.MULREC.UNEQUAL_SEGRE_ROOTS` proves, by
an explicit differential recurrence and interlacing, that when d>0 the
roots of h are simple and negative. Write

    h(t) = product_(j=1)^d (1+lambda_j t),
    lambda_1 > lambda_2 > ... > lambda_d > 0.            (1.3)

### Theorem KOSZUL.MIXED_RANK_GROWTH

Exactly the following profiles have finitely many nonzero M_n:

* At most one rank is greater than one. Then only M_1=E occurs.
* Exactly two ranks are two and all others are one. Then M_1 has
  dimension four, M_2 has dimension one, and all later M_n vanish.

For every other profile, `lambda_1>1`, and

    epsilon_n ~ lambda_1^n/n.                           (1.4)

In particular both parities have infinitely many nonzero grades. All
statements concern these actual quadratic-dual source modules.

#### Proof

The coefficient of t in (1.2) gives

    h_1 = product_i(a_i+1)-A-1
        = sum_(subsets J, |J|>=2) product_(i in J) a_i.  (1.5)

Discard indices with a_i=0. If the largest positive a_i is M>=2 and
there are at least two positive indices, the pair terms involving that
index already sum to `M(A-M)=Md>d`. If every positive a_i is one and
there are b>=3 such indices, then `h_1=2^b-b-1>b-1=d`.
Thus in every nonexceptional case, `sum_j lambda_j=h_1>d`, implying
`lambda_1>1`. Simplicity of the roots makes this largest lambda unique.

Taking the formal logarithm of (1.1) and applying Mobius inversion gives

    n(-1)^(n+1) epsilon_n
      = sum_(k|n) mu(k)
          [D+(-1)^(n/k+1) sum_j lambda_j^(n/k)].        (1.6)

For n>1 the terms D cancel. The k=1 contribution to `n epsilon_n` is
`sum_j lambda_j^n`. The other at most n-1 terms have absolute sum at most

    (n-1)d lambda_1^(n/2).                              (1.7)

When d=1 there is no secondary root. Otherwise the secondary contribution
is bounded by `(d-1)lambda_2^n`. Dividing (1.7) and that bound by
`lambda_1^n` proves (1.4), since lambda_1>1 and lambda_2<lambda_1.

In the first exceptional case R is a polynomial algebra on E, up to the
natural rank-one tensor factors, and `F_1=(1-t)^(-dim E)`.
In the second, `F_1=(1+t)/(1-t)^3=(1-t^2)/(1-t)^4`.
The signed Euler exponents are unique by the same Mobius inversion.
Therefore the actual dimensions epsilon_n have exactly the finite lists
stated above. A vector space of dimension zero vanishes. This also proves
the converse and completes the classification.

For the strip `(2,k)`, k>=3, these formulas become particularly explicit:

    F_1(t) = (1+(k-1)t)/(1-t)^(k+1),
    epsilon_n ~ (k-1)^n/n.                             (1.8)

The first identity follows by applying `1+t d/dt` to `(1-t)^(-k)`;
it does not require factoring a polynomial numerically.

## 2. Uniform operator domains and a sharp common zero-free disk

In a nonexceptional profile let `rho=1/lambda_1`, so `0<rho<1`. Form
the same Hilbert direct sum and block operator

    H = Hilbert_direct_sum_(n>=1) M_n,
    K_g(t)|M_n = t^n rho_n(g).

### Theorem KOSZUL.MIXED_ANALYTIC_DOMAIN

For every unitary input tuple g and every real p>=1,

    K_g(t) belongs to S_p  iff  |t|<rho^(1/p).           (2.1)

The map is holomorphic in the S_p norm on that strict disk. It is compact
exactly on `|t|<1`, bounded but noncompact on `|t|=1`, and unbounded
outside. On `|t|<rho`, its ordinary Fredholm superdeterminant is F_g(t).
In particular F_g is nonzero there for every unitary g. This common disk
is sharp: F_1 has a simple zero at t=-rho.

#### Proof

The singular values are `|t|^n`, each repeated epsilon_n times. The growth
theorem reduces every Schatten sum to comparison with
`sum_n (lambda_1 |t|^p)^n/n`. Its endpoint is harmonic, so strictness in
(2.1) is necessary. The remaining compactness, holomorphy, and determinant
arguments are exactly the direct block estimates in the first checkpoint,
with 2 replaced by lambda_1 and an eventual constant bound supplied by
(1.4). Each F_g is analytic on `|t|<1`: its coefficients are bounded by
the polynomially growing dimensions of R_m. Equation (1.1) thus gives
ordinary determinant recovery on the trace-class disk, where both
determinant factors are nonzero. Finally (1.2)--(1.3) show the asserted
simple identity zero, with no denominator zero there.

For the finite exceptional profiles K_g(t) is a finite matrix for every
t. There is no finite Schatten radius; the ratio of its finite determinants
is the corresponding rational function wherever its denominator is nonzero.

This theorem does not classify every input attaining a boundary zero.
The first checkpoint supplies that stronger characterization for `(2,3)`.

## 3. Regularization is performed on the same operator

Fix a nonexceptional rank profile and an integer p>=2. For an S_p
operator T define the standard regularization

    R_p(T) = (1-T) exp(sum_(j=1)^(p-1) T^j/j)-1,
    det_p(1-T) = det_F(1+R_p(T)).                       (3.1)

The scalar entire function defining R_p has a zero of order p at zero.
For our block-normal T=K_g(t), its absolute block trace bounds therefore
show directly that R_p(T) is trace class on `|t|<rho^(1/p)`. The usual
definition is basis independent and also applies to general S_p operators.
See Britz--Carey--Gesztesy--Nichols--Sukochev--Zanin,
[*The product formula for regularized Fredholm determinants*](https://arxiv.org/abs/2007.12834),
Section 1, equation (1.3), and Kostenko,
[*Trace Ideals with Applications*](https://users.fmf.uni-lj.si/kostenko/teach/IdealsNotes.pdf),
Section 3.6, especially Remark 3.6.1. Those sections were read directly.
No general determinant multiplicativity is assumed: regularized
determinants can have a multiplicative anomaly.

Define from the same source operator, without a new fitted spectrum,

    D_(p,g)(t) = det_p(1-K_g(t)|H_even)
                  / det_p(1-K_g(t)|H_odd).             (3.2)

Both factors and their quotient are holomorphic and nonzero on the full
strict S_p disk. Indeed their logarithms are the absolutely convergent
series obtained by deleting powers j<p from each block log determinant.
Uniform convergence on compact subdisks follows from

    sum_n epsilon_n sum_(j>=p) |t|^(nj)/j
       <= [p(1-|t|)]^(-1) sum_n epsilon_n |t|^(np).

This also identifies (3.2) with (3.1). Since `||K_g(t)||=|t|<1`,
the unregularized operator `1-K_g(t)` is invertible throughout this disk.

## 4. Exact Adams formula on the enlarged disk

Define the source primitive-character germ

    P_g(t) = sum_(n>=1) (-1)^(n+1) tr(rho_n(g)) t^n.

It converges absolutely on `|t|<rho`. The formal and analytic identities
near zero are

    log F_g(t) = sum_(k>=1) P_(g^k)(t^k)/k,
    P_g(t) = sum_(m>=1) mu(m) log F_(g^m)(t^m)/m.       (4.1)

All logarithms in this note start with value zero at t=0. The second
formula follows by substituting the first and using
`sum_(m|l)mu(m)=0` for l>1. The operation g -> g^m is induced by the
actual source representation; it is not an independent choice of local
coefficients.

Set, for positive integers l,

    a_p(l) = sum_(k|l, k<p) mu(l/k).                    (4.2)

Then `a_p(1)=1` and `a_p(l)=0` for `1<l<p`.

### Theorem KOSZUL.CANONICAL_ADAMS_REGULARIZATION

On the entire disk `|t|<rho^(1/p)`,

    log D_(p,g)(t)
       = -sum_(l>=p) a_p(l) log F_(g^l)(t^l)/l.        (4.3)

The right side converges locally uniformly and uses only canonical
zero-free logarithms inside the ordinary determinant disk. In particular
for p=2,

    log D_(2,g)(t) = -sum_(l>=2) mu(l) log F_(g^l)(t^l)/l.

#### Proof

For `|t|<rho`, deleting the first p-1 powers in the block logarithm gives

    log D_(p,g)(t) = sum_(k>=p) P_(g^k)(t^k)/k.

Hence the deleted counterterm germ is

    C_(p,g)(t) := sum_(k=1)^(p-1) P_(g^k)(t^k)/k
      = sum_(l>=1) a_p(l) log F_(g^l)(t^l)/l.          (4.4)

All regroupings converge absolutely on smaller disks. Since
`log F=log D_p+C_p`, cancelling the l=1 term of (4.4) proves (4.3)
there.

Now take `|t|<=r<rho^(1/p)`. Every l>=p satisfies `|t^l|<=r^p<rho`,
so the zero-free theorem chooses the logarithm uniquely. For sufficiently
large l, the uniform bound `log F_h(z)=O(|z|)` for all unitary h follows
from `|tr(h|R_m)|<=dim R_m` and a fixed small disk about zero. Moreover
`|a_p(l)|<=p-1`. The tail is therefore bounded by a constant times
`sum_l r^l/l`. The finite initial portion has no singularity. Local uniform
convergence and the identity theorem extend (4.3) to the full S_p disk.

Thus a regularized determinant exists beyond trace class and has an
explicit source-compatible recovery expression. It is generally not F_g.

## 5. The necessary zero and monodromy of the counterterm

The multiplicative counterterm has a unique holomorphic continuation
to the full S_p disk:

    Q_(p,g)(t) := F_g(t)/D_(p,g)(t).                    (5.1)

On the ordinary disk it equals `exp C_(p,g)` for the deleted source-trace
germ (4.4). Its continuation is therefore fixed by that germ and by the
same operator, not chosen arbitrarily after seeing F_g.

### Theorem KOSZUL.COUNTERTERM_ZERO_OBSTRUCTION

For identity input, Q_(p,1) has a simple zero at t=-rho. There cannot be
a holomorphic function c on the full S_p disk such that

    F_1(t) = exp(c(t)) D_(p,1)(t).                      (5.2)

On the punctured disk obtained by removing zeros of F_g, the additive
counterterm has analytic continuation along every path, on the universal
cover. Around a zero of F_g of order m its monodromy is `2 pi i m`.
Equivalently, its derivative has residue m there. No lower trace power
outside its trace-class domain is being assigned an ordinary operator trace.

#### Proof

The denominator in (5.1) is holomorphic and nonzero. Thus Q has exactly
the zeros of F_g, with the same orders. At identity, the sharp zero theorem
gives the simple zero -rho, which lies strictly inside the S_p disk since
0<rho<1 and p>1. An exponential of a holomorphic function never vanishes,
proving the impossibility of (5.2). On a simply connected zero-free
subdomain, take the continuation of `log F_g-log D_(p,g)` from its germ.
Its logarithmic derivative is `F'_g/F_g-(log D_(p,g))'`. The second term
is holomorphic, and the first has residue m at a zero of order m. The
residue theorem gives the stated monodromy. F_g has no poles on `|t|<1`
because its original coefficient series is holomorphic there.

This identifies the exact limitation of the analytic escape: source-natural
regularization enlarges the operator domain, but recovery of the scalar
zero requires a vanishing multiplicative counterterm, or a logarithm with
the specified singularity. The scalar zero is not an eigenvalue-one event
for K_g at that point; `||K_g(-rho)||=rho<1`.

For the strip `(2,k)`, k>=3, the obstruction occurs exactly at
`t=-1/(k-1)` for identity input. With all source matrices scalar, their
product phase c rotates this point to `-1/((k-1)c)`.

## 6. What remains outside this theorem

The construction now covers all finite rank profiles and all unitary
input tuples, with a canonical regularization on every finite-order
Schatten disk. It does not produce a single fixed finite p valid up to
`|t|=1`; the required order tends to infinity as the radius tends to one.
No regularized determinant at the compactness boundary is claimed.

The common zero-free radius is sharp, but a complete classification of
all inputs attaining it, outside `(2,3)`, is not asserted. Nor are positivity
of virtual relation grades, a global arithmetic completion, a conductor,
or functional-equation compatibility imported from this algebraic parent.
Those require additional source data and separate theorems.

## 7. Exact error bounds used by the bounded companion replay

This section concerns the `(2,3)` identity input only. It supplies the
infinite-tail guarantees behind rational, finite arithmetic controls of
the new analytic identity. Put `r=|t|<1` and assume `2r^p<1`.
The first checkpoint proves `epsilon_n<=3*2^n` for all n. Truncate the
direct regularized logarithm after grade N and block power J>=p:

    L_direct = sum_(n=1)^N sum_(j=p)^J
                 (-1)^(n+1) epsilon_n t^(nj)/j.

The absolute omitted tail is at most

    E_direct = 3(2r^p)^(N+1)/[p(1-r)(1-2r^p)]
                +6r^(J+1)/[(J+1)(1-r)(1-2r^(J+1))].   (7.1)

For n>N, use `sum_(j>=p)r^(nj)/j <= r^(np)/[p(1-r)]`
and sum a geometric series in n. For j>J, use the analogous bound with
p replaced by J+1 and sum over all n>=1. This may double-count an
omitted corner, which is harmless for an upper bound.

Independently, truncate (4.3) after Adams index L>=p, and expand each
identity scalar logarithm through power B:

    log F_1(z) = sum_(j>=1) [4+(-1)^(j+1)2^j] z^j/j.

Its omitted tail through B is at most

    3(2|z|)^(B+1)/[(B+1)(1-2|z|)],                    (7.2)

since `|4+(-1)^(j+1)2^j|<=3*2^j`. Sum (7.2) for
z=t^l, p<=l<=L, weighted by `|a_p(l)|/l`. The omitted Adams indices
l>L contribute at most

    E_Adams_tail = 6(p-1)r^(L+1)
                    /[(L+1)(1-r)(1-2r^p)].            (7.3)

Here `|log F_1(z)|<=6|z|/(1-2|z|)`, `|a_p(l)|<=p-1`,
and the remaining geometric series gives (7.3). All denominators in
(7.1)--(7.3) are strictly positive under the stated hypotheses.

For real rational t, both finite logarithm sums and these bounds are
rational. They produce rigorous intervals for the same real `log D_p`;
the replay checks that the intervals overlap at the stated held-out
points. This is a useful arithmetic falsifier, while the exact equality
and convergence follow from the preceding proofs. No floating-point
logarithm or unproved numerical tail estimate enters the check.
