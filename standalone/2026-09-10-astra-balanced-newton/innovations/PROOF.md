# NIR26: orthogonal arithmetic innovations and lossless Newton recompletion

**Status: PROPOSED component proofs. The native all-scale gain and RH remain OPEN.**
Date: 2026-09-10. Author: Astra. Parent: PR848 at
`a1b4625f9775df1fdbd431b5198309a2fce9b038`.

The interrupted preceding run did publish BNR26. This is new, separately scoped
mathematics, not a claim that the interruption concealed a proof of RH. Basic
Cholesky factorization, summation by parts and short-source Mobius/Newton inversion
are classical. No external priority is claimed. The contribution is their exact
combination: one moment instead of two, an isometric innovation coordinate, an
orthogonal scale projection of norm one, and an explicit mixed-difference kernel
for the still-unproved native estimate. Every assertion below is rederived.

## 0. Conventions

All coefficients are real and indexed by positive integers. Dirichlet convolution
is `(a*b)(n)=sum_(d|n) a(d)b(n/d)`; `1(n)=1` and delta is its identity.
`1*mu=delta`. For a finite source a put

    A_a(x)=sum_(n<=x) a_n,    P_a(s)=sum_n a_n n^(-s),
    J(a)=integral_1^infinity A_a(x)^2 dx/x^2,
    m_a(k)=sum_(n<=k) a_n/n,  m_a(0)=0,  m_a(infinity)=P_a(1).

All physical future is retained in J. At an integer cutoff N,

    J(a)=sum_(k<N) A_a(k)^2/[k(k+1)] + A_a(N)^2/N

when supp(a)<=N. No finite-window norm is substituted for this whole norm.
For the literal Mobius prefix write M(k)=sum_(n<=k)mu(n), m(k)=sum_(n<=k)mu(n)/n,

    b=Y+1,  E_Y=sum_(k<=Y) M(k)^2/[k(k+1)],
    u_Y=sum_(k<=Y) M(k)/[k(k+1)],
    F_Y=E_Y+b u_Y^2,  A_Y=E_Y+2b u_Y^2.

A_Y is the parent BNR26 two-moment energy, not the cumulative function A_a.

## 1. NIR26-1: exact isometry, variance and orthogonal innovations

For every finite a,

    J(a)=sum_(k>=0) (m_a(infinity)-m_a(k))^2.                  (1)

Proof: `1/max(r,s)=min(r,s)/(rs)`. Expand the finite sum

    sum_(r,s) a_r a_s/max(r,s)
       =sum_(k>=0) [sum_(n>k) a_n/n]^2.

The left side is the cell-integral expression for J. Everything is finite;
there is no exchange of conditionally convergent sums. In particular, if P_a(1)=0,

    J(a)=sum_(k>=1) m_a(k)^2.                                (2)

Define finite source atoms e_0=delta_1 and

    e_k = k delta_k-(k+1)delta_(k+1),  k>=1.

Their actual cumulative functions are k on [k,k+1), -1 afterward, and zero
before k. Their reciprocal partial sums equal 1 at k and 0 elsewhere. Thus
these atoms are orthonormal in J, and every finite a has the exact expansion

    a=m_a(infinity)e_0
      +sum_(k>=1) [m_a(k)-m_a(infinity)] e_k.                (3)

The finite span of e_k, k>=1, identifies isometrically with finite sequences in
ell2. Its Hilbert completion is the zero-P(1) subspace of the completed source
space. No claim identifies that space with all of L2(0,infinity).

Apply the elementary recurrence to any prescribed prefix, not just mu. It gives

    F_Y=sum_(k=1)^Y m(k)^2,
    F_Y-F_(Y-1)=m(Y)^2,  F_0=0,
    u_Y=(1/b)sum_(k=0)^Y m(k),
    E_Y=sum_(k=0)^Y (m(k)-u_Y)^2.                           (4)

For example, expanding `F_Y-F_(Y-1)` gives
`[u_(Y-1)+M(Y)/Y]^2=m(Y)^2`. Summation by parts gives the mean formula;
the variance formula follows. Equivalently,

    E_Y=(1/b)sum_(0<=i<j<=Y) [m(j)-m(i)]^2.                (5)

The normalization cost is exactly the constant component of these reciprocal
partial sums. It has NOT been discarded. In particular

    E_Y<=F_Y<=A_Y<=2F_Y.                                   (6)

F is monotone although the parent A need not be. These identities make the
meaning of the proposed scalar state explicit; they do not bound its growth.

## 2. NIR26-2: one late coefficient is the exact orthogonal state

Define the finite canonical source

    c_Y(n)=mu(n) for n<=Y,
    c_Y(b)=-b m(Y),    c_Y(n)=0 for n>b.                    (7)

It has P_c(1)=0, but its total is generally NOT zero:

    S=sum c_Y=M(Y)-b m(Y)=-b u_Y.

Its innovation vector is exactly `(m(1),...,m(Y),0,0,...)`. Consequently

    J(c_Y)=F_Y.                                            (8)

For every finite a preserving the whole prefix and satisfying P_a(1)=0,

    J(a)=F_Y+sum_(k>=b) m_a(k)^2.                          (9)

Thus c_Y is the unique minimizer, with support already at b. This is PR836's
one-safe-point optimizer, now explicitly an orthogonal projection. The parent
BNR26 compact two-moment source pays an additional b*u_Y^2. That source and
its claims are preserved, not retroactively changed.

More generally, for any zero-P(1) source in the innovation completion,
projection onto e_1,...,e_Y is contraction of norm one. When the prescribed
prefix exists, the projected source is (7). The complete orthogonal tail in
(9) is retained as discarded energy, not reclassified as zero physical output.

## 3. NIR26-3: one moment already gives a legitimate full Newton stage

Take any finite c with P_c(1)=0, supported through b. Let

    v=N(c)=2c-1*c*c,
    V(x)=2A_c(x)-sum_(r,s<=b)c_r c_s floor(x/(rs)),
    q(k)=sum_(n<=k) v(n)/n.

The coefficient source v usually has infinite support. Nevertheless it defines
an ordinary finite-energy cumulative source. Set

    L=sum |c_r|,  S=sum c_r,  K=2|S|+L^2.

For x>=b, the reciprocal moment cancels the linear floor term, so

    V(x)=2S+sum_(r,s)c_r c_s {x/(rs)},  |V(x)|<=K,
    integral_X^infinity V(x)^2 dx/x^2<=K^2/X, X>=b.        (10)

The total moment sum c=0 is unnecessary for this conclusion. A constant
cumulative tail still gives an integrable physical function e^(-t/2)V(e^t).
We do not pretend that the constant term vanishes.

Writing H_0=0 and H_j=sum_(l=1)^j 1/l gives an exact, finite formula at every k:

    q(k)=2m_c(k)-sum_(r,s) (c_r/r)(c_s/s) H_floor(k/(rs)). (11)

As k tends to infinity, `H_floor(k/d)=log k-log d+gamma+o(1)` for each fixed
positive d. In the finite sum, the log k and constant terms cancel by
`sum c_r/r=0`; the log(rs) term cancels by its separation into log r+log s.
Hence q(k)->0. This uses only the elementary convergence of H_n-log n, not
PNT, RH, a zero calculation, or a full-line bound for an inverse zeta function.

Summation by parts and (10) now yield

    q(k)=V(k)/k-integral_k^infinity V(x) dx/x^2,
    |q(k)|<=2K/k, k>=b,
    sum_(k>=R) q(k)^2<=4K^2/(R-1), R>=max(b,2).           (12)

Thus the whole innovation sequence is in ell2. To prove, rather than assume,
its norm equals the physical norm, apply (4) to the first N coefficients of v.
Its signed u_N is `sum_(k<=N)V(k)/[k(k+1)]`. Its limit is zero by q(infinity)=0,
and `|u_N|<=K/(N+1)` once N>=b. Therefore

    sum_(k<=N) q(k)^2
       =sum_(k<=N) V(k)^2/[k(k+1)]+(N+1)u_N^2
       ->J(v).

In particular

    J(v)=sum_(k>=1)q(k)^2.                                (13)

Both the infinite source domain and its omitted-tail bounds have been proved.
The bounds can be large and do not constitute a native gain estimate.

## 4. NIR26-4: the exact lossless arithmetic scale map

Now let c=c_Y from (7), e=delta-1*c and B=b^2-1. Dirichlet algebra gives

    mu-v=mu*e*e,   e(n)=0 for n<b,
    v(n)=mu(n) for n<=B,
    mu(b^2)-v(b^2)=e(b)^2.                                (14)

This is classical short-source Newton inversion; the last coefficient must
not be included by accident. Late changes of c cannot alter the prefix in
(14). Explicitly `N(c+d)-N(c)=2e*d-1*d*d` vanishes below b^2 if d does below b.

By (11), q(k)=m(k) for k<=B. Projecting v onto e_1,...,e_B therefore gives
EXACTLY c_B, with

    F_B=sum_(k<=B)q(k)^2<=J(v),
    J(v)=F_B+sum_(k>B)q(k)^2.                              (15)

Recompletion has factor ONE, not the factor-two estimate for BNR26's different
state. This improvement is at the operator/projection layer, not a proof that
J(v), F_B, or their growth is small.

### A single mixed-difference kernel, with no unknown future coefficient

Put x_r=m(r) for 1<=r<=Y, and x_0=x_b=0. Then

    c_r/r=x_r-x_(r-1), 1<=r<=b.

Two exact finite summations by parts turn (11) into

    q(k)=2x_k-sum_(r,s=1)^Y x_r x_s D_k(r,s),              (16)

where x_k=0 beyond Y, and

    D_k(r,s)=H_floor(k/(rs))
       -H_floor(k/((r+1)s))-H_floor(k/(r(s+1)))
       +H_floor(k/((r+1)(s+1))).                          (17)

For the new annulus b<=k<=B there is no 2x_k term. Every kernel entry is an
exact rational. There is no Fourier midpoint convention or unrecorded collar.
The mixed difference automatically kills the separated log(k)-log r-log s
main term, but not its arithmetic remainder.

For a completely discrete check, define a=rs, c=min((r+1)s,r(s+1)),
d=max((r+1)s,r(s+1)), e=(r+1)(s+1). Then

    D_k(r,s)=sum_(j>=1) [1_(ja<=k<jc)-1_(jd<=k<je)]/j.    (18)

Only j<=k/a can contribute. The endpoints are exactly the inclusive/exclusive
integer inequalities shown. This signed boundary formula is not positive.

Consequently the ENTIRE scalar update is

    F_B=F_Y+sum_(k=b)^B |x^T D_k x|^2.                    (19)

Equivalently its increment is the explicitly positive quartic tensor
`sum_k D_k tensor D_k` evaluated on the ONE native vector x tensor x. All
signs and all reciprocal-product coincidences are retained before squaring.
No matrix norm on arbitrary vectors is silently substituted for that value.

The source vector is prescribed by exact divisor inversion, which can also be
written with no unknown mu input:

    sum_(r=1)^n [r floor(n/r)-(r+1)floor(n/(r+1))] x_r=1,
                                                    1<=n<=Y. (20)

The triangular system has diagonal n and a unique solution. To derive it,
substitute mu(r)=r(x_r-x_(r-1)) in `sum mu(r)floor(n/r)=1`.
This does not estimate the solution: it states the native arithmetic constraint
that a proof must use before replacing (19) by a larger all-vector norm.

Starting at x_1=1, (14)-(16) generate all later prefixes on the ladder
`Y=1,3,15,255,65535,...`. The tests compare generated coefficients with an
independent primitive Mobius construction. Exact generation is not a gain proof.

## 5. NIR26-5: complete closing implication, but the gain remains open

One sufficient OPEN native estimate is, eventually on the above ladder,

    1+F_(b^2-1)<=C (log b)^K (1+F_(b-1))^(2-delta),       (21)

with fixed C>=1, K>=0 and 0<delta<1. This would prove RH, not merely a bounded
height or a particular source family. It is the source-specific estimate of
the actual quartic expression (19), not an arbitrary balanced-vector bound.

Indeed set t_j=log(Y_j+1)=2^j log 2 and L_j=log(1+F_(Y_j)). Then
`L_(j+1)<=(2-delta)L_j+O(j+1)`, whence

    F_X<=exp(O((log X)^theta)), theta=log_2(2-delta)<1.    (22)

Use monotonicity of F and adjacent ladder values to pass to every X. More
generally delta_j in [0,1] may tend to zero: divergent sum delta_j and
`sum 2^(-j)log C_j<infinity` force `L_j/2^j->0` by the same product/forcing
argument as BNR26. Constants from finitely many initial stages are harmless.

For completeness, E_X<=F_X=X^o(1) makes
`I(s)=integral_1^infinity M(x)x^(-s-1)dx` holomorphic for Re s>1/2.
On [2^j,2^(j+1)], Cauchy--Schwarz bounds its absolute integral, for fixed
sigma>1/2, by

    O(2^(j(epsilon/2+1/2-sigma)))

using E_(2^(j+1))=O(2^(j epsilon)) with epsilon<2sigma-1. Logarithmic derivatives
are controlled similarly. On Re s>1, `s I(s)=1/zeta(s)` by absolute Mobius
inversion. The identity theorem gives

    (s-1)zeta(s)s I(s)=s-1, Re s>1/2.

A nontrivial zero in that half-plane contradicts this identity. The functional
equation excludes the reflected left-half-plane zeros. This proves the
conditional RH implication without assuming any zero table or simplicity.

**No estimate (21), or divergent sequence of native gains, is proved here.**
Because F<=A<=2F, fixed exponent-gain targets for F and BNR26's A are equivalent
up to constants. The new coordinate removes artificial balancing/projection
losses and exposes the exact form to attack; it does not weaken the arithmetic
strength required. Merely noting that (19) is positive cannot upper-bound it.

## 6. NIR26-6: exact barriers to generic substitutes for the native estimate

### Unit-energy localized innovation

For any Y>=3 let x_Y=1 and all other x_r=0. Its source is
`c=Y delta_Y-(Y+1)delta_(Y+1)`; P_c(1)=0 and J(c)=1.
On b<=k<b^2, (16)-(17) give

    q(k)=-1 for Y^2<=k<Y(Y+1),
    q(k)=+1 for Y(Y+1)<=k<(Y+1)^2,
    q(k)=0 elsewhere in that annulus.

Here `(Y+1)^2<2Y^2` is why Y>=3 is retained. Exactly,

    sum_(k=b)^(b^2-1) q(k)^2=2Y+1.                       (23)

There is no dimension-independent bound for this quadratic map in the bare
innovation ell2 norm. This example does not have a Mobius prefix or bounded
ordinary prefix coefficients; it is not a counterexample to (21).

### Even bounded fake prefix coefficients do not give subquadratic growth

For even b>=16 use fake prefix a_1=1, a_2=...=a_(b-1)=0 and its one-moment
completion `c=delta_1-b delta_b`. Input J(c)=b-1. For b^2/2<=k<b^2,

    V(k)=2-2b-k+2b floor(k/b)>=k-4b+2>=k/2.

It follows that the output prefix energy is at least b^2/16, hence its
innovation energy obeys

    sum_(k<=b^2-1)q(k)^2>=b^2/16>=J(c)^2/16.              (24)

Thus bounded original prefix coefficients, P_c(1)=0 and positivity of J alone
do not give any fixed subquadratic exponent with polylogarithmic losses.
These fake prefixes violate (20), already at n=2. That exact native constraint
is the missing input, not another removal of the explicit harmonic main term.

## 7. Research conclusion and test boundary

The proposed contribution supplies a full-source isometry, exact variance and
innovation identities, norm-one projection, a smaller canonical source, a
valid infinite quadratic stage, and the explicit signed arithmetic boundary
kernel for a one-coordinate renormalization. It supplies a complete conditional
RH ending and exact controls against the first generic operator shortcut.

The actual Mobius-specific quartic saving is unresolved. No finite test proves
it cofinally. The source and its future have not been replaced, and no free
choice of correction can alter the exact new native prefix. A complete solution
would require a new estimate of (19) using (20), or a genuinely different
full-problem argument. The computational acceptance checks finite arithmetic,
not that universal estimate. Both implementations have the same author.
