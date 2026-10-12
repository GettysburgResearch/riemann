# Exact short-polynomial transport of the suppressed Mellin tube

Status: proved norm-filtered representation and negligible tube contribution.
This gives neither an all-frequency moment bound nor a zero-free boundary.
The negligible component is defined in the new short-polynomial representation;
it is not identified with the tube component of the original Euler integrand.

## SC1. The finite source factors and the norm window

Use the literal P1–P4 finite factorization in `PRIME_SLOT_CANCELLATION.md`,
SHA256 `d37ad696b46c7dda15a7faf314c46cda2d7d67e25ac8d3288c7f138aac373c13`.
Fix r=2k, the source field/ray data, source smooth norm tests W_i supported
in a fixed `[a,b]` with a>0, D sufficiently large, and Y=bD. At an exact
P8 incidence allocation q_I, put `c_i=product_(I contains i)q_I`,
`Q=product_I q_I`, with Nc_i<=Y and NQ<=Y^k. The source external row
factor omega_q(u) retains every principal nonunit mask and satisfies
|omega_q(u)|<=1. Left/right phases theta_i retain nu and its conjugate.

For the finite primes Np<=Y outside S,Q, including the automatic zeros
at primes dividing u, define

\[
 B_i(s_i)=\prod_p(1-\theta_i(p)(Np)^{-s_i}),\quad
 C(\mathbf s)=\prod_p(1-\sum_i\theta_i(p)(Np)^{-s_i}),\quad
 Q_{\rm coll}=C/\prod_i B_i.
\tag{SC1}
\]

Every B_i is nonzero for Re(s_i)>0. In this note Q_coll denotes the
collision factor, distinct from the squarefree incidence mask Q.

## SC2. Truncation is exact after norm filtering

Replace B_i by its short polynomial

\[
 T_{i,Y}(s_i)=\sum_{\substack{Nn\le Y\\(n,SQ)=1}}
                 \mu(n)\theta_i(n)(Nn)^{-s_i}.
\tag{SC2}
\]

All ideals here have prime factors of norm at most Y automatically.
Their u nonunit zeros remain in theta_i, and all source coefficients
are retained. T_i is exactly the coefficient truncation of B_i to norm
at most Y, not an arbitrary short Dirichlet polynomial.

The local collision series is

\[
 \frac{1-\sum_i z_i}{\prod_i(1-z_i)}
  =\sum_{e_1,\ldots,e_r\ge0}
       (1-\#\{i:e_i>0\})\prod_i z_i^{e_i}.
\tag{SC3}
\]

The zero multi-index has coefficient one. Every coordinate exponent is
nonnegative, and the series is absolutely convergent for |z_i|<1.
The finite product of these series is absolutely convergent on every
fixed positive-real-part contour. Its column ideals have norm at least
one. Hence removing a term of B_i with norm greater than Y cannot
change any coefficient whose final i-th column ideal has norm at most Y.
Consequently C and `(product_i T_i) Q_coll` have exactly the same
multivariate ideal coefficients whenever every column norm is at most Y.

The literal weight W_i(Nc_i Nn_i/D) vanishes outside Nn_i<=Y/Nc_i<=Y.
Thus applying all the source norm weights gives the exact identity

\[
 \sum_{\mathbf n}[C]_{\mathbf n}
           \prod_i W_i(Nc_i Nn_i/D)
 =\frac1{(2\pi)^r}\int_{\mathbb R^r}
       Q_{\rm coll}(\sigma+i\mathbf t)
       \prod_i T_{i,Y}(\sigma+it_i)
        (D/Nc_i)^{\sigma+it_i}\widehat W_i(\sigma+it_i)
                                                   \,d\mathbf t.
\tag{SC4}
\]

Here any fixed sigma>0 is allowed. For each fixed finite Y, absolute
convergence of SC3 and rapid Mellin decay justify termwise inversion;
the post-weighted coefficient identity then proves SC4. No infinite
reciprocal L-function or contour crossing is involved.

## SC3. The literal short factors cost only a polynomial

Fix 1/3<sigma<1/2. The ideal count gives the uniform bound

\[
 |T_{i,Y}(\sigma+it_i)|
 \le\sum_{Nn\le Y}(Nn)^{-\sigma}\ll Y^{1-\sigma}.
\tag{SC5}
\]

Moving exclusions can only decrease this positive upper bound. The
source scale factor has magnitude `(D/Nc_i)^sigma<=D^sigma`.
The complete product of these two costs is at most C Y^r, because
D is comparable to Y. The Mellin transforms are integrable with any
fixed polynomial frequency weight. This does not claim a polynomial
pointwise bound for B_i; SC2 is used only in the exact filtered identity.

## SC4. The narrow tube component is negligible at every fixed power

Use RD5–RD6 of `SUBCRITICAL_RAPID_COLLISION_DECAY.md`, SHA256
`a41b84b54f0e4052e6700887bad5cd82552ab452744f29c1b5f70e68cbf0735e`.
Fix 0<kappa<1/[2(2k-1)]. Let T_Y be precisely the set of frequencies
for which there exists a central t with
`|t_i-t|<=kappa/logY` for every left slot and
`|t_(k+j)+t|<=kappa/logY` for every right slot. This is the ST6 tube
with every slot frequency independent inside its specified width.

For every A>0, RD6 gives
`|Q_coll|<=C_A Y^(-A)(1+Nu/H)^(epsilon_0)` throughout T_Y,
for all source rows, where H=D^h and the fixed h is positive.
The source spatial majorant Phi is Schwartz; therefore

\[
 \sum_{u\ne0}|\Phi(u/\sqrt H)|(1+Nu/H)^{\epsilon_0}
                                                     \ll H.
\tag{SC6}
\]

SC5, absolute Mellin integration over the tube (bounded by integration
over all frequencies), and SC6 prove that for each exact incidence
allocation, the omega_q-weighted row sum of the T_Y component of SC4
is O_A(H Y^(r-A)), uniformly in that allocation. The central frequency
is unrestricted. This is a magnitude bound, not an assumed sign.

## SC5. Complete incidence summation preserves negligibility

At fixed r, each eligible squarefree mask has NQ<=Y^k. Each of its
prime factors is assigned to one of the finitely many subsets I with
|I|>=2. The number of assignments is at most d_m(Q) for a fixed m
depending on r, so the elementary fixed-order divisor bound gives
O_epsilon(Y^(k+epsilon)) complete eligible allocations. The factors
outside the row trace have modulus at most one. Choosing the A in RD6
larger than M+r+k+epsilon proves

\[
 \boxed{\left|\text{sum of all source-incidence tube components
 in the exact representation SC4}\right|
                         \ll_M H Y^{-M}\quad(M>0).}
\tag{SC7}
\]

This applies to the exact full smooth moment's incidence representation.
It is not a separate bound on the source's coupled critical-sector cutoff
R_k. The complete signed remainder is controlled only after a bound for
the full moment plus its imported controlled sectors, as in P14–P16.

## SC6. The remaining analytic target

Decompose SC4 into T_Y and its complement. SC7 pays T_Y. A source-faithful
estimate for the complementary contribution is still required; it contains
all independent left/right frequencies away from this common conjugate
tube. The original finite-Euler integrand and the short integrand need
not agree pointwise, so their partial tube integrals need not coincide.
Only their complete norm-filtered integrals agree exactly.

No part of SC7 bounds that complement, or supplies the P13 trace contract.
This reduction neither proves R_k's moment power nor changes the imported
zero-free extraction price. The new paid result is a negligible component
of an exact literal source representation, with every row and incidence
retained.

`check_short_collision_transport.py` supplies independent exact low-column
coefficient controls for the source good prime-ideal norms 7,7,13,13.
It preserves their separate ideal labels, including equal norms, and
checks both the local collision coefficients and every discarded-high-term
obstruction. These finite controls authenticate the truncation identity,
not the asymptotic rapid-decay proof or the complementary source estimate.
