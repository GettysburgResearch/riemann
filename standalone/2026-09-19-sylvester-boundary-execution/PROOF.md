# BCP26: cutoff-pivot collapse, the actual energy kernel, and a native sign obstruction

**Proposed component proofs, supplied for independent review. No all-scale
native upper bound and no proof of RH are claimed.**

This continues #903 and #848. It replaces an undefined kernel with an exact
one, and tests the proposed partition on the actual Möbius source. The
algebra below is an application of classical Möbius inversion and finite
Euler products, not a priority claim for a new sieve identity.

## 1. The error being reconstructed is not the energy-bearing correction

Let `*` mean Dirichlet convolution, let `1(n)=1`, and let `delta` be its unit.
For integer Y >= 1 put b=Y+1, B=b^2-1, and

$$g(n)=\mu(n)\mathbf1_{n\le Y},\qquad e=\delta-1*g.$$

Then e(n)=0 for n<b and

$$N(g)=g+g*e=2g-1*g*g,\qquad \mu-N(g)=\mu*e*e. \tag{1}$$

The last convolution is **identically zero on n<b^2**. It proves exact
reconstruction there. It is not the term whose fluctuations generate the
new annular energy. That term is the single-residual correction `g*e`.
At the first excluded index,

$$\mu(b^2)-N(g)(b^2)=e(b)^2.$$

It may be zero at a particular cutoff, but cannot be omitted in a universal
endpoint statement. For Y=2 the error is one.

For b <= x < b^2, the previously established #848 identity is

$$M(x)=M(Y)+\sum_{r\le Y}\mu(r)\sum_{n\le x/r}e(n). \tag{2}$$

The canonical late completion in #848 leaves this entire reconstructed
prefix unchanged. Its full-line energy is not assigned to the raw source g.

## 2. BCP26-1: exact collapse of one least-prime residual channel

Write P^-(n), P^+(n) for the least/largest prime factors, with
P^-(1)=infinity and P^+(1)=1. For every prime p define

$$e_p(n)=e(n)\mathbf1_{n>1,\ P^-(n)=p},$$

$$b_{Y,p}(d)=\mu(d)\mathbf1_{Y/p<d\le Y,\ P^-(d)>p}.$$

Let `mu_<p(a)=mu(a) 1_{P^+(a)<p}`. This has finite support on squarefree
divisors of the product of the primes less than p.

### Theorem

Coefficientwise, on all positive integers,

$$\boxed{\quad \mu*e_p=-\delta_p*b_{Y,p}*\mu_{<p}.\quad} \tag{3}$$

Consequently, for n<b^2,

$$\boxed{\quad (g*e_p)(n)
 =-\sum_{pad=n}\mu(a)\mu(d)
   \mathbf1_{P^+(a)<p<P^-(d),\ d\le Y<pd}.\quad} \tag{4}$$

In particular every channel is zero on nonsquarefree n. On squarefree n its
only possible nonzero value is mu(n), not an unrestricted divisor sum.

### Proof

If n=p^j m with j>=1 and P^-(m)>p, pair squarefree divisors d and pd:

$$e(n)=-\sum_{d\mid m,\ Y/p<d\le Y}\mu(d). \tag{5}$$

Only contributing squarefree divisors are paired; divisors divisible by
p^2 have Möbius weight zero. Introduce the arithmetic sequences

$$U_p=\sum_{j\ge1}\delta_{p^j},\qquad
 R_{>p}(m)=\mathbf1_{P^-(m)>p}.$$

Then (5) gives the exact factorization

$$e_p=-U_p*b_{Y,p}*R_{>p}.$$

Also

$$\mu=\mu_{<p}*(\delta-\delta_p)*\mu_{>p},\qquad
\mu_{>p}*R_{>p}=\delta,\qquad
(\delta-\delta_p)*U_p=\delta_p.$$

Multiplication proves (3). These are formal Dirichlet identities: each
coefficient involves finitely many divisors, so no analytic convergence
or RH assumption is used. Finally `mu-g` and `e_p` both vanish below b,
so `(mu-g)*e_p` vanishes below b^2, proving (4). QED.

The cancellation removes both the complete p-power tail and all rough
multiples **before** taking a square. This is the operative arithmetic
content missing from #903's schematic K.

## 3. BCP26-2: unique cutoff pivot and a disjoint coefficient partition

For squarefree n>Y, list its primes in descending order. Multiply them
until their product first exceeds Y. Let p be the last prime multiplied,
d the product already accumulated, and a the product of the remaining
smaller primes. Then

$$n=pad,\qquad P^+(a)<p<P^-(d),\qquad d\le Y<pd. \tag{6}$$

This representation is unique: positive products of successive descending
prime suffixes strictly increase, and cross a given cutoff once. The
three factors in (6) are pairwise coprime, so
`-mu(a)mu(d)=mu(n)`.

Combining this observation with (4) gives a disjoint partition of the
native output coefficients on the whole stage. This is much stronger than
an antichain marginal condition. It does **not** imply orthogonality of
cumulative functions: after a coefficient jumps, it remains in every
later cumulative value.

A factorization-based reconstruction of (6) is used as an independent
checker, not as a new fast algorithm for generating mu. The producer
uses only mu through Y in `g*e_p`; a sieve through B supplies residual
prime labels. The checker separately factors every output integer.

## 4. BCP26-3: the previously unspecified kernel, with all endpoints

For a boundary atom (p,d), define the finite step function

$$T_{p,d}(x)=\sum_{\substack{a\mid \prod_{q<p}q\\pad\le x}}\mu(a),$$

and put

$$V_p(x)=-\sum_{\substack{Y/p<d\le Y\\P^-(d)>p}}\mu(d)T_{p,d}(x),
\qquad V_0(x)=M(Y). \tag{7}$$

All d with mu(d)=0 may be omitted. Equations (2)-(4) now give, exactly,

$$M(x)=V_0(x)+\sum_{p\le B}V_p(x),\qquad b\le x<b^2. \tag{8}$$

The product of small primes in (7) is notation for a finite Euler
polynomial. In an implementation only a with pad<b^2 are enumerated.
There is no need to construct a gigantic primorial.

The full physical annular kernel is

$$W_Y(n,m)=\begin{cases}
\displaystyle {1\over\max(b,n,m)}-{1\over b^2},&\max(b,n,m)<b^2,\\
0,&\text{otherwise}.
\end{cases}$$

Thus the boundary-atom Gram is the explicit finite expression

$$\boxed{\quad
\mathcal K_Y((p,d),(p',d'))=
\sum_{a\mid\prod_{q<p}q}\sum_{a'\mid\prod_{q<p'}q}
\mu(a)\mu(a')W_Y(pad,p'a'd').\quad} \tag{9}$$

The signed atom coefficients are `-mu(d)`. The mean of T_{p,d} is obtained
from the same formula with `W_Y(n,m)` replaced by
`w_Y(n)=max(1/max(b,n)-1/b^2,0)`.

These kernels are for the exact physical Mertens energy in BNR26/NSR26.
They are **not** PCR26's individual centered-harmonic product kernel or
RCB26's rough-squareclass kernel. No termwise identification between those
different covariance decompositions is asserted.

### Completion price, not only annular energy

Let

$$E_Y=\sum_{k\le Y}{M(k)^2\over k(k+1)},\qquad
 u_Y=\sum_{k\le Y}{M(k)\over k(k+1)}.$$

Set

$$G_{pq}=\int_b^{b^2}V_p(x)V_q(x){dx\over x^2},\qquad
 l_p=\int_b^{b^2}V_p(x){dx\over x^2},$$

including p=0 for the constant channel. Then

$$E_B=E_Y+\mathbf1^TG\mathbf1,\qquad
 u_B=u_Y+\mathbf1^Tl,$$

$$\boxed{\quad \mathcal A_B
 =E_Y+\mathbf1^TG\mathbf1+2b^2(u_Y+\mathbf1^Tl)^2.\quad} \tag{10}$$

The innovation state of NIR26 is, in the same notation,

$$F_B=E_Y+\mathbf1^TG\mathbf1+b^2(u_Y+\mathbf1^Tl)^2.$$

Hence this is an exact interface to both existing completed states, not
a new surrogate RH criterion. It does not by itself compute PCR26's
individual diagonal, covariance or completion cross terms.

The code includes the constant row, every output cell, the full ordered
cross term, and the signed mean before squaring. It checks (10) against
an independently generated full prefix.

## 5. BCP26-4: the raw prime-pivot partition has a large native positive sector

This is a failure of a tempting partition, not a failure of RH or of all
possible signed regroupings. Crucially it occurs on **the actual mu**,
not only on a fake balanced source.

Let Y>=17 and define the prime sets

$$\mathcal P_Y=\{p:3Y/4<p\le4Y/5\},\qquad
\mathcal Q_Y=\{q:4Y/5<q\le9Y/10\},$$

with cardinalities N_P,N_Q.

### Exact finite lower bounds

For p in P_Y, throughout the entire stage,

$$V_p(x)=\#\{q\text{ prime}:p<q\le Y,\ pq\le x\}\ge0. \tag{11}$$

Moreover, with all cross sums ordered,

$$\sum_{p\in\mathcal P_Y}G_{pp}\ge{N_PN_Q^2\over3Y^2}, \tag{12}$$

$$\sum_{\substack{p,p'\in\mathcal P_Y\\p\ne p'}}G_{pp'}
 \ge {N_P(N_P-1)N_Q^2\over3Y^2}. \tag{13}$$

Even the sub-sum using **coprime** semiprimes pq and p'q' has lower bound

$$ {N_P(N_P-1)N_Q(N_Q-1)\over3Y^2}. \tag{14}$$

### Proof

When p>3Y/4 and Y>=17, a squarefree p-rough d<=Y is either 1 or a
prime q>p; d=1 fails d>Y/p. Further,

$$2p^2>{9Y^2\over8}>(Y+1)^2.$$

Thus a>=2 in (6) is impossible anywhere in this stage. Only n=pq
survives, and mu(pq)=+1, proving (11). For the specified p,q bands,

$$pq\le{18Y^2\over25}<{3Y^2\over4}.$$

Consequently V_p(x)>=N_Q on J=[3Y^2/4,Y^2]. The whole channel is
nonnegative outside J as well, and

$$\int_J{dx\over x^2}={1\over3Y^2}.$$

Squaring and pairing proves (12)-(13). If p!=p' and q!=q', the four
primes are distinct because the bands are disjoint; hence pq and p'q'
are coprime and have positive coefficients. Counting these terms proves
(14). All endpoints lie inside the actual stage. QED.

### All-scale consequence (ordinary PNT is the only asymptotic input)

The classical prime number theorem gives

$$N_P\sim {Y\over20\log Y},\qquad N_Q\sim {Y\over10\log Y}.$$

Therefore the raw pivot diagonal satisfies

$$D_{\rm pivot}\ge(1+o(1)){Y\over6000\log^3Y},$$

and its positive ordered cross mass satisfies

$$\sum_{p\ne p'}(G_{pp'})_+
 \ge(1+o(1)){Y^2\over120000\log^4Y}. \tag{15}$$

These are lower bounds for this precisely specified partition. For the
asymptotic input see NIST DLMF 27.12.4-5, or any proof of PNT; no RH-level
prime error term is assumed. Equations (12)-(14) need no PNT at all.

For clarity, the elementary bound |m(k)|<=1, where
`m(k)=sum_(n<=k)mu(n)/n`, follows by dividing
`1=sum_(n<=k)mu(n)floor(k/n)` by k and bounding the fractional parts;
the n=1 part is zero. Thus 1<=F_Y=sum_(k<=Y)m(k)^2<=Y.

It follows that the old #903 proposed positive-excess target
`sum positive blocks <= (log Y)^A F_Y^(1-eta_Y)`, with eta_Y>=0,
**cannot hold for the singleton pivot-pair partition** for any fixed A.
That does not refute a coarser partition that first cancels positive and
negative sectors. It does refute treating all distinct/coprime pivot
interactions as harmless or individually nonpositive.

### Subtracting the annular mean does not repair the diagonal

For p in P_Y, V_p is zero on [b,Y^2/2], whose weighted mass is at least
1/(2Y), and at least N_Q on J, of weighted mass 1/(3Y^2).
For every real constant c, minimizing the two-region lower bound gives

$$\int_b^{b^2}(V_p-c)^2{dx\over x^2}
 \ge {N_Q^2\over6Y^2}.$$

Indeed for 0<=c<=N_Q minimize `m0*c^2+m1*(N_Q-c)^2`;
for c outside that interval the bound is larger. Since m0>=m1, the
minimum is at least m1*N_Q^2/2. Thus even the optimally centered raw
pivot diagonal grows at least `(1+o(1))Y/(12000 log^3 Y)`.

This is not merely an unpaid rank-one mean term.

## 6. The genuine signed bridge that remains

The reported partition uses every p<=Y separately and aggregates p>Y.
For the latter sector d=1, and on x<b^2 all smaller cofactors are <=Y<p.
Therefore its exact formula is

$$V_{>Y}(x)=-\sum_{\substack{p>Y\\p\ \mathrm{prime}}}M(x/p). \tag{16}$$

Equations (7) and (16) retain a specific prime/semiprime/cofactor
cancellation. The finite table shows that it is large, not optional.
The all-scale positive-sector result says that these signed sectors must
be combined **before** taking a positive-part budget.

The existing sufficient whole-state estimate remains

$$1+\mathcal A_{b^2-1}\le2(1+\mathcal A_Y)^{3/2},$$

or the already documented accumulating-gain variant. Neither is proved
here. RCB26's subpower control of within-rough-squareclass harmonic
interactions remains valid in its own coordinates and is not replaced
by the poor raw-pivot diagonal.

A useful next estimate must control jointly the signed rough-core
interactions, using pivot incidence only to retain the forced prime
extensions and their compensating signs. A positive-part bound on the
raw pivot blocks is now excluded. No unproved quasi-orthogonality,
prime independence, or narrow-window randomness is used in this packet.

## 7. What has and has not advanced

Established here as proposed component proofs: the explicit collapse
(3)-(4), unique-pivot support, the completed-state kernel (9)-(10), and
the all-scale native lower bounds (12)-(15). The elementary algebra is
credited as such. The computation checks finite instances independently;
it cannot certify the universal proofs.

Not established: a new native upper bound, an improvement to the best
existing Cauchy budget, a completed bridge from Sylvester divisibility
to a zeta estimate, RH, GRH, or novelty priority.
