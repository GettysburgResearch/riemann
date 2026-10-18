# Compress the original masked source: polynomial core budgets retained

Status: **PROPOSED complete-source reduction. No improving estimate for
the resulting full balanced amplitude, new zeta boundary, or RH is proved.**

This addresses a scope limitation of compressing first and then applying
the reference source's core mask. We instead expand the ALREADY MASKED
original amplitude exactly into R dilates, then compress those dilates.
The mask may use an arbitrary original prefix-dependent core cutoff,
including #1002's polynomial energy-adaptive cutoff. No new reference
small-core estimate is presumed for that cutoff.

## 1. The actual source and the complete theorem

Retain the exact C_Y(q), S_q, R, b=Y+1, N=b^2-1, and native annuli
I_j=[K_j,min(2K_j,b^2)), K_j=2^j b, from the pinned #994 source
recorded in `SOURCES.md`. The output cells are ALL integers b<=k<=N.
For each annulus choose any FIXED real vector |omega_j(q)|<=1,
2<=q<=Y^2. The vector may depend on Y and j, but must remain fixed
throughout that annulus. Define

    V_(Y,omega)(k)=sum_(q>=2)omega_j(q)C_Y(q)S_q(k), k in I_j.  (1)

In particular the intended complete target is

    omega_j(q)=1_(q>floor(K_j^rho),core(q)>S_Y),                (2)

for ANY fixed rho in (1/2,2/3) and ANY integer S_Y>=0. It may depend
on the actual old energy F_Y. There is no subpower restriction on S_Y.
The theorem below in fact does not require rho, because it compresses
the exact vector (1), not a newly projected reference source.

For all sufficiently large Y there is an explicit annular balanced
old-pair amplitude

    B_(Y,omega)(k)=sum_(a,b'<=Y)
         w_j(a,b')mu(a)mu(b')/(ab') R(k/(ab')), k in I_j,       (3)

whose symmetric weights use only squarefree unordered pairs, written
a<b', satisfying

    |a-b'|<=C(ab')^(1/4),
    |w_j(a,b')|<<_epsilon (ab')^(1/4+epsilon).                 (4)

Then, UNIFORMLY in all the fixed vectors omega_j,

    sum_(k=b)^N |V_(Y,omega)(k)-B_(Y,omega)(k)|^2
         <<_epsilon Y^epsilon, every epsilon>0.               (5)

All original masks, shared primes, squares, above-output products,
physical windows and coherent cross terms are retained in (1) and
in the explicit coefficients of (3). No reference denominator/core
projection is applied to (3). In particular its full R terms must
be retained: silently deleting modes from the new source would change
the theorem. Arbitrarily varying omega at each individual output cell
is outside the stated scope.

## 2. Exact annular R coefficients and their uniform bound

For each fixed annulus set

    alpha_(j,d)=sum_(q:d|q)mu(q/d)omega_j(q)C_Y(q), d<=Y^2.    (6)

The full finite inversion S_q(x)=sum_(d|q)mu(q/d)R(x/d) gives

    V_(Y,omega)(k)=sum_d alpha_(j,d)R(k/d), k in I_j.           (7)

Since q>=2 and sum_(d|q)mu(q/d)=0,

    sum_d alpha_(j,d)=0.                                     (8)

This exact identity includes all prime-power centerings. It is not
obtained by discarding the new R coefficient after an approximation.

The pinned source's complete masked reciprocal factorization gives

    |q C_Y(q)|<=a(core(q)),
    a(s)=product_(p|s)(2+1/p), q cubefree,                      (9)

and C_Y(q)=0 on non-cubefree q. Since a(core(q))<=d_3(q), the
elementary divisor bound yields, for every delta>0,

    |C_Y(q)|<<_delta Y^delta/q,
    |alpha_(j,d)|
       <<_delta Y^delta/d sum_(n<=Y^2/d)1/n
       <<_delta Y^(2delta)/d.                                (10)

Every multiple q=dn is included. No independent-coefficient model,
nonzero aggregate assumption, or product cutoff inside the source
factorization is used: (9) is invoked BEFORE the new mask expansion.
The new mask is then bounded only by one.

## 3. Low products and the entire top corner

Put L=floor(sqrt(Y)) and U=Y^2-20Y^(3/2). The low-d source has,
at every native integer k>=Y+1,

    |sum_(d<=L)alpha_(j,d)R(k/d)|
        <<_delta Y^(2delta)L/k,                              (11)

because k/d>=1 and |R(k/d)|<=d/k. Hence its COMPLETE discrete
native energy, with the actual annular choices, is

    <<_delta Y^(4delta)L^2 sum_(k>=Y+1)k^-2
    <<_delta Y^(4delta).                                     (12)

This is a bound for the omitted source itself; we do not falsely say
its already-masked coefficients have zero rough projection.

For d>U and large Y, d>Y^2/2. Thus q in (6) can only equal d, and
the only old product multiple of d is d itself. Consequently

    alpha_(j,d)=omega_j(d)C_Y(d)
                =omega_j(d)z_Y(d)/d.                         (13)

If an actual nonzero old pair a,b'<=Y has ab'>U, both inputs exceed
Y-20sqrt(Y). There are O(Y) ordered integer pairs in that corner.
The total absolute coefficient mass in (13) is therefore O(1/Y),
uniformly in j. On the native range k in [Y+1,(Y+1)^2), d>U,
we have k/d in [c/Y,2] and hence |R(k/d)|<<1+log Y. Thus the full
corner source is pointwise O((1+log Y)/Y), and its COMPLETE discrete
energy is O((1+log Y)^2). This directly handles all endpoints and
does not identify a nonconstant R-dilate with a cellwise constant
interpolation. Squares and shared old primes are included in this
ordered-pair count.

## 4. Compress every remaining product at every annulus

For L<d<=U, use exactly the reference geometry of
`DIAGONAL_COMPRESSION.md` Section 2. Divide targets into integer
dyadic product blocks D<=d<2D, write X=sqrt(D), and take

    H_X=ceil(X^(1/5+eta)), eta=1/100,
    r=floor(sqrt d), T=(r+1)(r+2)-d,
    k_0=max{k>=0:k(k+1)<=T},
    G_d={(r+1-k,r+2+k):k_0<=k<k_0+H_X,
                         both inputs squarefree}.            (14)

All pairs are legal old inputs <=Y by the corner exclusion. All
shared input primes are allowed. Tolev's uniform primary density
theorem gives g_d=|G_d|>=H_X/5 for all sufficiently large Y, uniformly
because X>=cY^(1/4). Every reference product M satisfies

    M is comparable to X^2,
    |M-d|<<X^(7/10+eta), |a-b'|<<sqrt(X).                     (15)

Transport the signed coefficient alpha_(j,d) with probability 1/g_d
to EVERY reference in G_d. The new explicit source on annulus j is

    B_j(x)=sum_(L<d<=U)alpha_(j,d)/g_d
                             sum_((a,b') in G_d)R(x/(ab')).    (16)

The equivalent symmetric old-input weights are

    w_j(a,b')=mu(a)mu(b')ab'/2
                 sum_(d:(a,b') in G_d)alpha_(j,d)/g_d.        (17)

A fixed reference pair receives only O(G_X) distinct integer targets,
each with g_d>=H_X/5. Equation (10), with Y<=CX^4 on these blocks,
gives a per-pair coefficient O_epsilon(X^(-3/2+epsilon)); multiply
by ab' to obtain (4). A pair can lie in only a bounded number of
adjacent product blocks. This is a deterministic finite formula.
It can create aggregate coefficients absent from the original source;
those coefficients and every reference sign are explicitly retained.

For each fixed j and product block the full source difference is

    W_(j,X)(x)=sum_(d in block)alpha_(j,d)
                     [R(x/d)-g_d^-1 sum_(a,b')R(x/(ab'))].     (18)

The compact-flux theorem `FLUX_COMPRESSION.md` Sections 1--4 applies
uniformly: (10) supplies alpha_(j,d)<<X^epsilon/d, and (15) gives
G_X<<X^(71/100). With theta=9/50, its complete global energy is

    ||W_(j,X)||_L2(0,infinity)^2
          <<_epsilon X^(-289/2500+epsilon).                  (19)

Every W_(j,X) has EXACTLY zero total R coefficient and integer
dilations, so it is constant on every full integer cell. Its discrete
native norm, restricted to annulus j, is bounded by the global norm
in (19). Sum the O(log Y) product-block root norms, then all
O(log Y) disjoint annuli. Since every X>=cY^(1/4), the resulting
transport error is a negative power of Y after sufficiently small
divisor losses. No fixed-coefficient sieve has been applied to
arbitrary moving cellwise coefficients.

Finally add the complete low-d error (12) and complete corner error
(13), with their coherent cross terms paid by the root triangle
inequality. Choose delta small for the requested final epsilon.
This proves (5).

## 5. The energy-adaptive original core cutoff and exact consumer

Read #1002 at exact head 1319373815ee408146705b25a426fba6b22ed755,
`standalone/2026-10-18-five-route-zero-preserving-attack/NEWTON_BUDGET.md`.
Its original-source budget, credited there to #994's sector theorem,
is: for ANY G_Y>0, set

    S_Y=min(Y^2,floor(G_Y/[2304 H_Y^2 H_(Y^2)^6])).            (20)

Allow S_Y=0. The COMPLETE original small-core source removed at this
cutoff has root norm at most sqrt(G_Y)/4. Apply the current theorem
with EXACTLY mask (2), using this S_Y, and call (3) B_(Y,G).
Its full reference kernel encodes the original mask through (6)
and (17); no reference core is discarded. At the source-qualified
native crossings, #994 therefore gives

    sqrt(F_((Y+1)^2-1)-F_Y)
       <=||B_(Y,G)||_2+sqrt(G_Y)/4
                                  +O_epsilon(Y^epsilon)+o(1). (21)

The exponent on the root-error epsilon may be renamed at will.
Every output cell and every original mask is retained. In particular
the polynomial cutoff (20) is valid here; this is not a claim that
the new source's different small-core bound permits cutoff G_Y.

Take G_Y=Y^a(1+F_Y)^p, a>=0,1<=p<2. A PROVED bound for the
specified COMPLETE amplitude

    ||B_(Y,G)||_2^2<<_epsilon Y^epsilon G_Y                    (22)

on any unbounded sequence of native crossings would, by the exact
ALL-PREFIX exponent theorem imported from #848, imply

    2kappa<=a+p kappa,
    kappa<=a/(2-p),
    every nontrivial zeta zero has
          Re s<=[1+a/(2-p)]/2.                               (23)

The premise (22) is OPEN. No sparse-cut crossing gap or all-Y
recurrence is silently assumed; the source's all-prefix exponent
limit applies to both Y and (Y+1)^2-1. The current compression
establishes the uniformly small approximation error, not (22).

For a=1/3,p=3/2, (20) uses the ACTUAL prefix energy. If its imported
benchmark exponent were kappa_0 approximately 0.749914, then
S_Y has size roughly Y^(1/3+(3/2)kappa_0) up to logarithms, rather
than merely Y^o(1). Proving (22) would give boundary 5/6 via (23).
Those remain explicit conditional targets.

The new weights (17) encode sums of the original masked C_Y(q),
which already contain their signed Mobius correlations. Assigning
independent reference Mobius cancellation, replacing them by their
positive majorant, or proving a generic balanced-class operator bound
does not prove (22). The actual positive-sector obstruction in
`FLUX_COMPRESSION.md` Section 6 remains a decisive check on such claims.
