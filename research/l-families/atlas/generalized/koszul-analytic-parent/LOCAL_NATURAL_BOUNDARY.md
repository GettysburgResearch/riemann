# Local parent natural boundaries and fractional critical cutoffs

Status: proposed fifth analytic companion, preserving earlier freezes.
Scope: first the identity input of the canonical Segre source of ranks
`(2,q+1)`, with integer q>=2, and a fixed integer regularization order p>=2.
Section 6 extends the analytic theorems to every nonexceptional finite
mixed-rank profile at identity input; the exact finite controls remain
restricted to the named strips.
This is one local source. No product over primes, Estermann theorem,
arithmetic L-function, or RH/GRH conclusion is involved.

The scalar shadow is rational. The source primitive character and its
canonical regularized determinant have additional continuation obstructions.
Those obstructions concern the same previously constructed Hilbert operator,
not an arbitrarily fitted infinite diagonal matrix.

## 1. Frozen source identities and the meromorphic logarithmic derivatives

Put `rho=1/q`, `d=q+2`, and

    F(t)=(1+qt)/(1-t)^d,
    P(t)=sum_(n>=1)(-1)^(n+1)epsilon_n t^n.

Here epsilon_n is the dimension of the actual degree-n quadratic-dual
Lie parent, not a new definition by scalar factorization. The earlier
source theorem gives epsilon_n~q^n/n and the germ identities

    P(t)=sum_(m>=1) mu(m) log F(t^m)/m,
    log D_p(t)=-sum_(m>=p) a_p(m) log F(t^m)/m,
    a_p(m)=sum_(k|m,k<p)mu(m/k).                       (1.1)

D_p is the regularized superdeterminant of the same block operator
K(t)|M_n=t^n I. Its ordinary S_p domain is |t|<rho^(1/p).
All logarithms in (1.1) are their zero-at-origin germs.

Define the single-valued logarithmic derivatives initially there:

    U(t)=P'(t),       V_p(t)=D'_p(t)/D_p(t).

### Theorem KOSZUL.LOCAL_MEROMORPHIC_NATURAL_BOUNDARY

U and V_p have single-valued meromorphic continuations to |t|<1.
At any point tau with `tau^m=-rho`, their residues are respectively

    res_tau U = mu(m)/m,
    res_tau V_p = -a_p(m)/m,                           (1.2)

where the second residue is zero for m<p. No distinct index contributes
a pole at the same point. In particular, for every prime ell>=p,

    res_tau V_p=1/ell whenever tau^ell=-rho.

Every point of |t|=1 is an accumulation point of these genuine poles.
Neither U nor V_p admits meromorphic continuation across any point of
the unit circle. Thus |t|=1 is a meromorphic natural boundary for these
single-valued functions.

#### Proof

The rational logarithmic derivative is

    F'(z)/F(z)=q/(1+qz)+d/(1-z).

Termwise differentiation of (1.1) gives

    U(t)=sum_(m>=1) mu(m)t^(m-1) F'(t^m)/F(t^m),
    V_p(t)=-sum_(m>=p) a_p(m)t^(m-1) F'(t^m)/F(t^m).  (1.3)

On any compact disk |t|<=r<1, only finitely many indices can have
`|t|^m=rho`. For all sufficiently large m, t^m lies in a fixed small
zero-free disk about zero, and the summands in (1.3) are uniformly
O(r^(m-1)); use |mu(m)|<=1 and |a_p(m)|<=p-1. The remaining finite
terms are rational functions. This proves the stated meromorphic
continuations and local uniform convergence away from their poles.

Inside the unit disk, a singularity can only come from t^m=-rho; the
denominator condition t^m=1 lies on the unit circle. If also t^l=-rho,
then `rho^(1/m)=|t|=rho^(1/l)`. Since 0<rho<1, this forces m=l.
Thus singular indices cannot cancel each other. The zero of F is simple,
and so is the zero of 1+qt^m at a nonzero tau. A term c log F(t^m)
therefore contributes residue c to its derivative. This proves (1.2).

For prime ell>=p, the only divisor k< p of ell is k=1, and hence
`a_p(ell)=mu(ell)=-1`. There are arbitrarily large primes. The ell
solutions of t^ell=-rho have radius rho^(1/ell), tending to one, and
angles `(2j+1)pi/ell` with spacing 2pi/ell. Therefore every point of the
unit circle is an accumulation point of nonzero-residue poles of V_p;
the same argument applies to U, with residue -1/ell.

A meromorphic continuation to a neighborhood of any such boundary point
would have poles accumulating inside that neighborhood. Poles of a
nonconstant meromorphic function are isolated. The uniqueness theorem
would identify its poles with those of (1.3) on the overlap, giving a
contradiction. Neither function is identically infinite. This proves
the natural-boundary assertion.

## 2. What this implies, and does not imply, about branched determinants

The possible branch points t^m=-rho form a locally finite set in the open unit
disk. On its complement, every compact continuation problem involves
only finitely many nontrivial logarithm branches; the high-index tail in
(1.1) remains canonically holomorphic. Thus (1.1) defines analytic
continuation along paths avoiding the branch points.

At a prime-order point tau^ell=-rho with ell>=p, D_p has local form

    (1+qt^ell)^(1/ell) times a nonzero holomorphic factor. (2.1)

Its monodromy is multiplication by exp(2pi i/ell), so this is a genuine
nonmeromorphic branch point. P has logarithmic monodromy -2pi i/ell there.
Other indices may have a zero coefficient or an integral exponent; no
claim that every index is a branch point is needed.

The precise natural-boundary theorem was deliberately stated for the
single-valued meromorphic logarithmic derivatives. In particular no branch
of D_p can have a meromorphic extension across an open unit-circle arc:
its logarithmic derivative would then contradict that theorem. This does
not describe D_p as an ordinary single-valued holomorphic function on
the entire unit disk; its interior branch points already forbid that.

The rational F itself has no such natural boundary. The continued
counterterm F/D_p has the compensating branches. Their cancellation in
the scalar product does not remove the parent continuation obstruction.

## 3. The first S_p boundary has a fractional local zero

For every integer p>=2,

    a_p(p)=-1.                                       (3.1)

Indeed the sum over all divisors k of p of mu(p/k) is zero, and its
omitted k=p term is one. Separating the m=p term in (1.1) gives

    D_p(t)=(1+qt^p)^(1/p) G_p(t),
    G_p(t)=(1-t^p)^(-d/p)
            exp[-sum_(m>p) a_p(m)log F(t^m)/m].        (3.2)

The branches are normalized at zero. The function G_p is holomorphic
and nonzero on the larger disk |t|<rho^(1/(p+1)), since every m>p
argument remains in the zero-free ordinary determinant disk.

Thus all p points tau satisfying tau^p=-rho are genuine branch points
of exponent 1/p on the sharp S_p circle. The operator K(tau) is compact
and 1-K(tau) is invertible, but K(tau) is not S_p. Formula (3.2) is a
branched continuation of the regularized determinant, not its usual
S_p definition at that point.

## 4. Finite source grades detect the fractional cutoff exponent

Let D_(p,N) be the pth regularized superdeterminant of the first N source
grades, using exactly the regularization polynomial from the earlier
packet. For |t|<1 it has the canonical logarithm

    log D_(p,N)(t)
      =sum_(n=1)^N (-1)^(n+1)epsilon_n
                            sum_(j>=p)t^(nj)/j.       (4.1)

### Theorem KOSZUL.FRACTIONAL_CRITICAL_CUTOFF

At every tau with tau^p=-rho,

    N^(1/p) D_(p,N)(tau) -> exp(-gamma/p) G_p(tau),     (4.2)

and the limit is nonzero. The source cutoff therefore tends to zero
at the precise fractional rate N^(-1/p), although every finite operator
1-K_N(tau) is invertible.

#### Proof

Write `epsilon_n rho^n=1/n+e_n`. The earlier strip bound proves e_n
decays exponentially and is absolutely summable. In (4.1), the j=p
term at tau is exactly

    -(1/p) sum_(n=1)^N epsilon_n rho^n
      =-H_N/p-(1/p)sum_(n=1)^N e_n.                   (4.3)

The j>p terms converge absolutely as N tends to infinity, because
`q |tau|^(p+1)=rho^(1/p)<1`. The same estimates show convergence on
a neighborhood of the first S_p circle after the leading j=p
logarithmic term is subtracted. Its limiting holomorphic remainder
is log G_p: inside the S_p disk this follows from (3.2), and then from
the identity theorem. Thus

    log D_(p,N)(tau)+H_N/p -> log G_p(tau).

Use `H_N-log N -> gamma` and exponentiate to obtain (4.2).
The canonical logarithm of G_p exists on the larger disk in (3.2),
so no phase convention is left implicit in the constant.

Explicitly,

    G_p(tau)=(1+rho)^(-d/p)
               exp[-sum_(m>p)a_p(m)log F(tau^m)/m].    (4.4)

This constant uses the normalization by (1+qt^p)^(1/p). In a local
coordinate 1-t/tau, the corresponding prefactor is p^(1/p)G_p(tau).
That change of coordinate does not insert an extra p factor into (4.2).

## 5. Exact independent enclosures for the cutoff constant

The bounded controls use Gaussian-rational tau with tau^p=-1/q and a
rational r such that

    |tau|<=r<1,             q r^(p+1)<1.              (5.1)

Examples are `(q,p,tau,r)=(4,2,i/2,1/2)`,
`(8,3,-1/2,1/2)`, and `(4,4,(1+i)/2,5/7)`. These are source rank
profiles `(2,q+1)`, not a new fitted eigenvalue prescription.

Truncate the source expression for log G_p(tau) after grade N and
block power J>=p+1:

    A_(N,J) = -(1/p)sum_(n=1)^N(epsilon_n rho^n-1/n)
                +sum_(n=1)^N (-1)^(n+1)epsilon_n
                                      sum_(j=p+1)^J tau^(nj)/j.

Since epsilon_n<=3q^n and
`sum_(n>N)|e_n|<=2rho^(floor(N/2))/(1-rho)`, its absolute error is at most

    2rho^(floor(N/2))/[p(1-rho)]
      +3(qr^(p+1))^(N+1)/[(p+1)(1-r)(1-qr^(p+1))]
      +3q r^(J+1)/[(J+1)(1-r)(1-qr^(J+1))].           (5.2)

The last two terms bound omitted source grades and omitted powers,
respectively, by geometric series. Overlap between the two omitted
regions only makes the bound more conservative.

Independently truncate (4.4) at Adams index L>=p+1. Expand each scalar
logarithm through degree B using

    log F(z)=sum_(j>=1)[d+(-1)^(j+1)q^j]z^j/j.

For q>=2 its coefficients obey `|d+(-1)^(j+1)q^j|<=3q^j`.
The scalar-log remainder at z=tau^m is therefore at most

    3(qr^m)^(B+1)/[(B+1)(1-qr^m)].                   (5.3)

Weight (5.3) by |a_p(m)|/m for p<m<=L. The omitted Adams indices
contribute at most

    3q(p-1)r^(L+1)/[(L+1)(1-r)(1-qr^(p+1))].          (5.4)

The real first term `-(d/p)log(1+rho)` is independently enclosed by
the exact log1p Taylor bound. All arithmetic in these enclosures is
rational or Gaussian rational, with outward rounding after weighting.
No approximate complex logarithm or unproved tail scan is used.

Agreement of the two finite enclosures is an arithmetic falsifier for
the exact source/Adams identity. The natural boundary, noncancellation
of poles, and fractional cutoff limit are proved above and are not
inferred from those finite checks.

## 6. Mixed Hilbert roots: only finitely many prime grids can collide

Let a nonexceptional finite Segre rank profile have identity series

    F(t)=product_(j=1)^b(1+lambda_j t)/(1-t)^D,
    lambda_1=R>lambda_2>...>lambda_b>0,       R>1.

The source-pinned mixed-rank root theorem gives precisely these simple
negative roots, and epsilon_n~R^n/n. Put rho=1/R. The same canonical
Adams identities (1.1) hold for this F.

### Theorem KOSZUL.MIXED_LOCAL_NATURAL_BOUNDARY

For every such profile and every p>=2, P' and D'_p/D_p have meromorphic
continuations to |t|<1 with the unit circle as a meromorphic natural
boundary. All but finitely many prime-index grids
`tau^ell=-rho`, ell>=p prime, consist of genuine poles with residues
respectively -1/ell and 1/ell. Arbitrary-index noncancellation is not claimed.

#### Proof

The convergence argument for (1.3) is unchanged: F is rational and
zero-free near zero, its only poles are at t=1, and its finite zeros
are -1/lambda_j. Suppose a point with tau^ell=-1/R also satisfies
tau^n=-1/lambda_j for a lower root. If lambda_j<=1 this is impossible
inside the unit disk. Otherwise equality of moduli forces

    n/ell = log(lambda_j)/log R,       0<n/ell<1.       (6.1)

If this fixed ratio is irrational, no integers n,ell can satisfy it.
If it is a/b in lowest positive terms, then b>=2 and b divides ell.
For prime ell this permits at most the single value ell=b, and only
when b itself is prime. There are finitely many lower roots, so only
finitely many prime indices need exclusion. Possible phase constraints
can remove further coincidences; they cannot add any beyond (6.1).

At every remaining prime-index largest-root point, no lower-root term
can contribute. A second largest-root index also cannot contribute,
by the distinct-radius argument in Section 1. The largest root is simple,
so the residues are exactly -1/ell and 1/ell. Removing finitely many primes
does not affect the density of their root grids at the unit circle.
The meromorphic natural-boundary proof from Section 1 now applies.

### Corollary KOSZUL.MIXED_FRACTIONAL_FIRST_CUTOFF

For any tau with tau^p=-rho, the first critical exponent is still 1/p,
and

    N^(1/p)D_(p,N)(tau) -> exp(-gamma/p)G_p(tau),

where G_p is holomorphic and nonzero on some disk strictly larger than
|t|<rho^(1/p), and locally there

    G_p(t)=[F(t^p)/(1+Rt^p)]^(1/p)
              exp[-sum_(m>p)a_p(m)log F(t^m)/m].       (6.2)

The analytic root is normalized at zero. In particular its first factor
at tau is the positive real root `[rho F'(-rho)]^(1/p)`.

#### Proof

At the first S_p radius, the m=p largest-root contribution is unique:
lower roots at that index have larger lifted radii, and every m>p
largest-root radius is larger. The quotient F(z)/(1+Rz) is holomorphic
and nonzero on a disk strictly larger than |z|<rho. Choose the enlarged
t-disk below rho^(1/(p+1)) and, when a lower root exists with lambda_2>1,
also below lambda_2^(-1/p). This gives a disk strictly larger than the
first S_p disk on which (6.2) is holomorphic and nonzero.

The mixed-rank proof gives exponentially summable
`epsilon_n rho^n-1/n`. The leading j=p logarithm of the finite source
cutoff is therefore again -H_N/p plus a convergent remainder. The j>p
terms converge absolutely on a larger disk. The proof of (4.2) applies
verbatim, with the local factor (6.2). At the simple largest-root zero,
`lim_(z->-rho) F(z)/(1+Rz)=rho F'(-rho)>0`, proving the last assertion.

The larger holomorphy disk in this corollary need not reach
rho^(1/(p+1)); a secondary Hilbert root may intervene earlier.
The finite exceptional profiles, whose Lie parent has only finitely
many nonzero grades, are excluded from both mixed assertions.

## 7. Remaining scope

These are identity-input local theorems. They make no general nonscalar
natural-boundary claim, no global Euler-product assertion, and no comparison
with the active arithmetic Satake/Estermann programmes. Even a local
rational scalar shadow can conceal a genuinely more singular canonical
infinite parent and its regularizations. The exact arithmetic controls
above cover only the named one-root strips; the finite-prime-exception
argument is proved rather than inferred from a census.
