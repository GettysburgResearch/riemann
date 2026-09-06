# Full-norm arithmetic transfer and an alternative growth target

Status: complete proposed component proofs, awaiting independent review.
**Neither RH nor the uniform full-source block gain is proved.**
This is an author continuation of PR #805, not a Reviewer C acceptance.
The new transfer is in the original norm, not the relaxed detail norm.
Classical analytic inputs are stated separately below; no priority is claimed.

## 0. Objects and scope

The parent at `0f8724bbd86c1de8f40eacbf30129321e0ebc8aa` constructs

\[
 \mathcal H=\ell^2(\mathbb N_{\ge1},[n(n+1)]^{-1}),\quad
 h_k(n)=\{n/k\},\quad \chi(n)=1,
\]

with the associated step functions zero below 1. The original optimal
squared distance is \(\delta_N=\operatorname{dist}(\chi,B_N)^2\),
\(B_N=\operatorname{span}(h_2,\ldots,h_N)\). Its open sufficient gain is
\(\delta_N-\delta_{2N}\ge c\delta_N^2\) on all sufficiently large
predetermined dyadic stages. No assertion below establishes that estimate.

For a full-norm comparison also use

\[
 \mathcal E=L^2((0,\infty),dt/t^2),\quad e(t)=\{t\},\quad
 (D_nf)(t)=f(t/n).
\]

Thus \(\mathcal H\) is a closed step subspace of \(\mathcal E\), but
\(e\notin\mathcal H\). We have \(\|e\|^2\le2\),
\(D_mD_n=D_{mn}\), and \(\|D_n\|=n^{-1/2}\). As functions,
\(h_k=D_ke-e/k\); omitting the second term changes the source.

Put \(c_*=8/\pi^2\), so \(4/5<c_*<1\), and
\(J_2(n)=n^2\prod_{p\mid n}(1-p^{-2})\). The parent's explicit
odd-detail optimizer is

\[
 a_{k,M}=c_*k^2\sum_{\substack{\ell\le M,\ \ell\ {\rm odd}\\k\mid\ell}}
       \frac{\mu(\ell/k)\mu(\ell)}{J_2(\ell)}
 \quad(k\le M\text{ odd}).                                      \tag{1}
\]

It has zero nonsquarefree coefficients. For odd \(k\ge1\) define
\(H_k=(2/k)D_2e-D_ke\), in particular \(H_1=2h_2\). Our explicit
**unoptimized full lift** and its normalization are

\[
 H_M=\sum_{k\le M,\ k\ {\rm odd}}a_{k,M}H_k,\quad
 A_M=\sum_{k\le M,\ k\ {\rm odd}}a_{k,M}/k,\quad
 S_M=\sum_{k\le M,\ k\ {\rm odd}}a_{k,M}D_ke.
\]

Then \(H_M=2A_MD_2e-S_M\in B_{\max(M,2)}\). Neither \(H_M\) nor
\(-H_M\) is asserted to approximate \(\chi\). The comparison sequences are

\[
 O_M=\sum_{n\le M,\ n\ {\rm odd}}\mu(n)D_ne,\qquad
 R_{\epsilon,M}=\sum_{n\le M}\mu(n)n^{-\epsilon}D_ne\quad(\epsilon\ge0),
 \qquad R_M=R_{0,M}.
\]

All these definitions are finite arithmetic sums. Unknown zeros are not
inputs. Limits below are over integer cutoffs, with zero-length prefixes
understood to be zero.

## 1. GT26.1 — exact operator-valued Dirichlet factorization

For an odd prime \(p\), set

\[
 P_p=\frac{I-p^2D_p}{p^2-1}.
\]

Let \(T,U,V\) be multiplicative sequences of commuting bounded operators,
zero on even integers and equal to \(I\) at 1, specified locally by

\[
 T(p)=P_p,\quad T(p^r)=0\ (r\ge2),
\]

\[
 U(p^r)=\frac{(I-D_p)D_p^{r-1}}{p^2-1},\qquad
 V(p^r)=-\frac{(I-D_p)(-P_p)^{r-1}}{p^2-1}\quad(r\ge1).             \tag{2}
\]

Write \(B(n)=\mu(n)D_n\) for odd \(n\), zero otherwise. With Dirichlet
convolution of these operator sequences,

\[
 T=U*B,\qquad B=V*T,\qquad U*V=\varepsilon I.                    \tag{3}
\]

Moreover, for every integer \(M\ge1\), the following are exact:

\[
 S_M=c_*\sum_{d\le M}T(d)e
     =c_*\sum_{d\le M}U(d)O_{\lfloor M/d\rfloor},
\qquad
 O_M=c_*^{-1}\sum_{d\le M}V(d)S_{\lfloor M/d\rfloor}.             \tag{4}
\]

**Proof.** All assertions can first be checked in the polynomial algebra
\(D_iD_j=D_{ij}\), so no convergence assumption is needed. Expand (1)
and interchange its two finite sums. For each odd squarefree \(\ell\),

\[
 \frac{\mu(\ell)}{J_2(\ell)}
    \sum_{k\mid\ell}k^2\mu(\ell/k)D_k
   =\prod_{p\mid\ell}\frac{I-p^2D_p}{p^2-1}=T(\ell).
\]

Nonsquarefree \(\ell\) contributes zero. This gives the first equality
in (4). Since \(P_p+D_p=(I-D_p)/(p^2-1)\), formal local series satisfy

\[
 1+\sum_{r\ge1}U(p^r)x^r=\frac{I+P_px}{I-D_px},\qquad
 1+\sum_{r\ge1}V(p^r)x^r=\frac{I-D_px}{I+P_px}.
\]

Multiplication by the local series \(I-D_px\) of \(B\) proves (3).
Taking finite summatory convolutions proves the remaining equalities in
(4). Prime powers in \(U,V\) are essential even though \(T,B\) are
squarefree-supported. Every sum with \(d\le M\) is finite. No norm is
taken until after these source-exact identities. QED.

## 2. GT26.2 — both transformations are uniformly bounded

In operator norm on \(\mathcal E\),

\[
 \boxed{\sum_{d\ge1}\|U(d)\|<3,\qquad
        \sum_{d\ge1}\|V(d)\|<8.}                             \tag{5}
\]

Consequently (4) yields two-sided uniform comparison of prefix norms:

\[
 \max_{M\le X}\|S_M\|<3c_*\max_{M\le X}\|O_M\|,\qquad
 \max_{M\le X}\|O_M\|<8c_*^{-1}\max_{M\le X}\|S_M\|.           \tag{6}
\]

**Proof.** If \(p\ge3\), let \(q=p^{-1/2}<3/5\). Equation (2) gives

\[
 \sum_{r\ge1}\|U(p^r)\|
 \le\frac{1+q}{(p^2-1)(1-q)}<\frac4{p^2-1}.
\]

Also
\(\|P_p\|\le(1+p^2q)/(p^2-1)<4/5\): replacing \(q\) by \(3/5\)
reduces the last inequality to \(p^2\ge9\), with strictness provided
by \(q<3/5\). Therefore

\[
 \sum_{r\ge1}\|V(p^r)\|<\frac8{p^2-1}.
\]

The sum over odd primes is bounded by the telescoping sum over odd integers:

\[
 \sum_{p\ {\rm odd}}\frac1{p^2-1}
 \le\sum_{j\ge1}\frac1{4j(j+1)}=\frac14.
\]

Submultiplicativity, unique factorization, and monotone convergence give
\(\sum\|U(d)\|\le e<3\), \(\sum\|V(d)\|\le e^2<8\).
This proves actual absolute convergence of the operator series, rather
than presupposing an infinite Euler-product inverse. Triangle inequalities
applied only now to the finite identities (4) give (6). QED.

The same argument works on the Banach space of operator prefixes with norm
\(\sup_M M^{-\tau}\|x_M\|\) for every \(\tau\ge0\), because
\(\lfloor M/d\rfloor^\tau\le M^\tau\). Thus it preserves every
nonnegative polynomial growth exponent. It does not manufacture
cancellation in either of the equivalent arithmetic sources.

## 3. GT26.3 — the signed scalar normalization is bounded at every cutoff

There is an elementary all-cutoff bound

\[
 \boxed{|A_M|\le2\quad(M\ge1).}                              \tag{7}
\]

In addition, the total coefficient sum is exactly

\[
 \boxed{\sum_{k\le M,\ k\ {\rm odd}}a_{k,M}
       =c_*\sum_{n\le M,\ n\ {\rm odd}}\mu(n).}             \tag{8}
\]

Thus a positive detail Gram has not removed unsmoothed signed arithmetic.

**Proof.** Let \(m(N)=\sum_{n\le N}\mu(n)/n\). The divisor identity
\(\sum_{n\le N}\mu(n)\lfloor N/n\rfloor=1\) gives

\[
 Nm(N)=1+\sum_{n=2}^N\mu(n)\{N/n\},\qquad |m(N)|\le1.
\]

Writing \(m_o(N)=\sum_{n\le N,\ n\ {\rm odd}}\mu(n)/n\), the exact
2-adic decomposition gives
\(m(N)=m_o(N)-m_o(\lfloor N/2\rfloor)/2\), hence

\[
 m_o(N)=\sum_{2^j\le N}2^{-j}m(\lfloor N/2^j\rfloor),\quad |m_o(N)|\le2.
\]

Specialize the finite operator-polynomial identity for \(U\) at
\(D_n\mapsto1/n\). The resulting multiplicative nonnegative sequence
\(u\), supported on odd integers, has

\[
 u(p^r)=\frac{(1-1/p)p^{-(r-1)}}{p^2-1},\quad
 \sum_{d\ge1}u(d)
 =\prod_{p\ {\rm odd}}\left(1+\frac1{p^2-1}\right)=\frac{\pi^2}{8}.
\]

Thus (4), as a finite polynomial identity, specializes to
\(A_M=c_*\sum_{d\le M}u(d)m_o(\lfloor M/d\rfloor)\).
Nonnegativity and the convergent Euler product prove (7). This does not use
PNT, RH, or a bound for an unsmoothed Mertens sum.

Finally specialize the finite identity for \(T\) at \(D_n\mapsto1\).
Now \(P_p\mapsto-1\), so \(T(n)\mapsto\mu(n)\), proving (8).
Equivalently use \(\sum_{k\mid\ell}k^2\mu(\ell/k)=J_2(\ell)\)
directly in (1). QED.

## 4. GT26.4 — a two-sided comparison in the full original norm

For integer \(X\ge1\), set
\(\mathscr H(X)=\max_{1\le M\le X}\|H_M\|\),
\(\mathscr R(X)=\max_{1\le M\le X}\|R_M\|\). Then

\[
 \boxed{\mathscr H(X)\le4+12\mathscr R(X),\qquad
        \mathscr R(X)\le20(\mathscr H(X)+4).}                 \tag{9}
\]

These estimates are unconditional and include the entire coarse component.

**Proof.** Since \(\|D_2e\|\le1\), (7) gives
\(\|H_M+S_M\|=\|2A_MD_2e\|\le4\). Also, exactly,

\[
 R_M=O_M-D_2O_{\lfloor M/2\rfloor},\qquad
 O_M=\sum_{2^j\le M}D_2^jR_{\lfloor M/2^j\rfloor}.
\]

The finite geometric series has norm sum less than
\((1-2^{-1/2})^{-1}<4\). Consequently prefix norms satisfy
\(\mathscr O<4\mathscr R\), \(\mathscr R<2\mathscr O\).
Combine these with (6), \(c_*<1\), and \(c_*>4/5\) to obtain (9).
QED.

This is not the false comparison between detail norm and full norm ruled
out in the parent. Here both sides retain full functions and their signed
cross terms before the bounded transformation is applied. In particular
boundedness and subpower growth of the two full sequences are equivalent.
No assertion of their boundedness is made.

## 5. Analytic imports, stated without a hidden RH assumption

We use Mellin--Plancherel on \(\mathcal E\), with the critical line
\(s=1/2+it\) and measure \(dt/(2\pi)\), and the classical identity

\[
 \int_0^\infty\{x\}x^{-s-1}\,dx=-\frac{\zeta(s)}s
 \quad(0<\Re s<1).                                      \tag{10}
\]

The latter follows from summation by parts for \(\zeta\), initially
comparing its pole-subtracted integral with \(\int_1^\infty\{x\}x^{-s-1}dx\),
and adding \(\int_0^1 x^{-s}dx=1/(1-s)\). It is also stated in the
primary source [BD02, equation (2.6) and its preceding identity] after
\(x\mapsto1/x\).

The load-bearing quantitative import is **Balazard--Saias, Lemma 2, as
quoted in Baez-Duarte [BD02], Lemma 2.1**. If \(1/2\le\alpha<1\),
\(\zeta\) has no zeros in \(\Re w>\alpha\), and \(d,\eta>0\), then
for \(N\ge2\) and \(\alpha+d\le\Re w\le1\),

\[
 \sum_{n\le N}\frac{\mu(n)}{n^w}
 =\frac1{\zeta(w)}+
 O_{\alpha,d,\eta}(N^{-d/3}(1+|\Im w|)^\eta).             \tag{BS}
\]

The hypothesis is retained literally. In particular (BS) is not an
unconditional assertion with \(\alpha=1/2\). The original 1998 paper
was not independently reproved; its precise quoted statement and the
2002 proof using it were read.

The unconditional estimate
\(|\zeta(1/2+it)|\ll(1+|t|)^{1/4}\) suffices for our use of (BS).
Indeed DLMF 25.9.3 gives two sums of length
\(\lfloor\sqrt{|t|/(2\pi)}\rfloor\), whose absolute values are at most
\(2\sqrt{\text{length}}\); the functional-equation factor has modulus
one on the critical line. Bounded \(t\) are absorbed into the constant.
This explicit derivation avoids assuming Lindelof or RH for that estimate.

For the support corollary in section 8 we also import the following
**conditional** conclusion proved in [BD02, section 2.2]: under RH,
for every sufficiently small fixed \(\epsilon>0\),
\(R_{\epsilon,N}\to R_\epsilon\) in \(\mathcal E\) as \(N\to\infty\),
and then \(R_\epsilon\to-\chi\) as \(\epsilon\downarrow0\).
This nested limit has no asserted uniform cutoff in \(\epsilon\).

## 6. GT26.5 — exact full-norm growth exponent

Let

\[
 \Theta=\sup\{\Re\rho:\zeta(\rho)=0,\ 0<\Re\rho<1\}.
\]

Classical zero existence, reflection, and the zero-free half-plane
\(\Re s\ge1\) give
\(1/2\le\Theta\le1\). No finite zero census is used. For every
\(\epsilon\ge0\),

\[
 \boxed{\limsup_{N\to\infty}
 \frac{\log\|R_{\epsilon,N}\|_{\mathcal E}}{\log N}
 =\max(0,\Theta-1/2-\epsilon).}                           \tag{11}
\]

In particular the **actual explicit full lift** satisfies

\[
 \boxed{\limsup_{M\to\infty}
 \frac{\log\|H_M\|_{\mathcal H}}{\log M}=\Theta-1/2.}     \tag{12}
\]

**Proof: a nonzero lower norm.** Set
\(m_{\epsilon,N}=\sum_{n\le N}\mu(n)n^{-1-\epsilon}\).
Weighted summation by parts from \(|m(N)|\le1\) proves
\(|m_{\epsilon,N}|\le1\) for every \(\epsilon\ge0\).
For \(1<t<2\), \(R_{\epsilon,N}(t)=tm_{\epsilon,N}-1\), so

\[
 \|R_{\epsilon,N}\|^2\ge
 m_{\epsilon,N}^2-2m_{\epsilon,N}\log2+1/2
 \ge1/2-(\log2)^2>1/100.                                \tag{13}
\]

Here \(\log2<7/10\). Thus the limsup exponent is nonnegative.

**Proof: upper exponent.** If \(\epsilon_0>1/2\), the series for
\(R_{\epsilon_0,N}\) converges absolutely in \(\mathcal E\), since
\(\sum n^{-\epsilon_0-1/2}<\infty\). Suppose instead
\(0<\epsilon_0\le1/2\) and \(\Theta<1/2+\epsilon_0\). Choose
\(\Theta<\alpha<1/2+\epsilon_0\), \(\alpha<1\), and put
\(d=1/2+\epsilon_0-\alpha>0\). By definition of \(\Theta\) and classical nonvanishing on
\(\Re s\ge1\), the zero-free hypothesis of (BS) holds. Mellin--Plancherel gives

\[
 \mathcal M R_{\epsilon_0,N}(s)
 =-\frac{\zeta(s)}s\sum_{n\le N}\mu(n)n^{-s-\epsilon_0},
 \qquad s=1/2+it.
\]

The difference from \(-\zeta(s)/(s\zeta(s+\epsilon_0))\) is bounded by
\(C N^{-d/3}(1+|t|)^{-3/4+\eta}\). Fix \(0<\eta<1/4\);
its square is integrable. The prospective limiting transform is in
\(L^2\): use (BS) at \(N=2\) and the same bound. This proves strong
convergence, with norm error \(O(N^{-d/3})\), and uniform boundedness of
\(R_{\epsilon_0,N}\). No boundary value across a possible zero has been
assumed.

It follows that boundedness holds for every
\(\epsilon_0>\max(0,\Theta-1/2)\). For \(0\le\epsilon<\epsilon_0\),
let \(q=\epsilon_0-\epsilon>0\). Vector summation by parts gives

\[
 R_{\epsilon,N}=N^qR_{\epsilon_0,N}
 -\sum_{n<N}((n+1)^q-n^q)R_{\epsilon_0,n},
\]

hence \(\|R_{\epsilon,N}\|\le2C_{\epsilon_0}N^q\).
Taking \(\epsilon_0\) arbitrarily close to the threshold proves the upper
exponent in (11), including equality at the threshold. When \(\Theta=1\)
the absolute-convergence case alone suffices. When \(\epsilon\) is strictly
above the threshold, use the boundedness already proved.

**Proof: lower exponent.** Write its limsup as \(\lambda\ge0\). The
trivial sum \(\sum n^{-1/2-\epsilon}\) bounds it, so it is finite.
For any \(\tau>\lambda\), \(\tau>0\), we have
\(\|R_{\epsilon,N}\|=O(N^\tau)\). Remove the below-1 linear part:

\[
 F_{\epsilon,N}=R_{\epsilon,N}-m_{\epsilon,N}e
 =\sum_{2\le n\le N}\mu(n)n^{-\epsilon}h_n\in\mathcal H,
 \quad \|F_{\epsilon,N}\|=O(N^\tau).
\]

For each real \(1/2<\sigma<1\), Mellin evaluation of a step function
supported on \([1,\infty)\) has norm \((2\sigma-1)^{-1/2}\). Equation
(10), by finite summation, gives

\[
 \int_1^\infty F_{\epsilon,N}(t)t^{-\sigma-1}\,dt
 =\frac{\zeta(\sigma)}\sigma
   \left(m_{\epsilon,N}-\sum_{n\le N}\mu(n)n^{-\epsilon-\sigma}\right).
                                                               \tag{14}
\]

The real number \(\zeta(\sigma)\) is nonzero: the alternating eta series
is strictly positive for real \(\sigma>0\), and
\(\zeta(\sigma)=\eta(\sigma)/(1-2^{1-\sigma})\) for \(0<\sigma<1\).
Thus the partial sums on the right of (14) are \(O(N^\tau)\).
A final summation by parts proves that the ordinary reciprocal Dirichlet
series \(\sum\mu(n)n^{-w}\) converges locally uniformly, hence
holomorphically, for \(\Re w>\epsilon+\sigma+\tau\).
On its overlap with \(\Re w>1\) it equals \(1/\zeta(w)\); the identity
principle applied to \(\zeta(w)\) times this series excludes every zeta
zero in the whole half-plane (the pole at 1 is removable in the reciprocal).
Hence \(\Theta\le\epsilon+\sigma+\tau\). Let
\(\sigma\downarrow1/2\), \(\tau\downarrow\lambda\) to get
\(\lambda\ge\Theta-1/2-\epsilon\). This proves (11).

**Proof of (12).** At the first step cell \(H_M(1)=a_{1,M}\ge c_*>4/5\),
so \(\|H_M\|>1/2\). Thus its exponent is also nonnegative. The
prefix comparisons (9) preserve all bounds \(O(M^\tau)\) for \(\tau>0\)
in both directions. A sequence with nonnegative finite limsup exponent and
its increasing prefix maximum have the same exponent: for any larger
\(\tau>0\), bound all but finitely many terms by \(M^\tau\) and absorb
the finite prefix in the constant. Apply (11) at \(\epsilon=0\). QED.

The equality (12) is an unconditional statement **about** the unknown
\(\Theta\), not an evaluation of \(\Theta\). Its upper-bound proof uses
only zero-free half-planes lying strictly to the right of that unknown
abscissa. It cannot be specialized to exponent zero without a new theorem.

## 7. GT26.6 — full-norm convergence is the wrong replacement target

The explicit full lifts \(H_M\) **do not converge in \(\mathcal H\)**,
unconditionally. This is compatible with RH and with subpower norm growth.
The corresponding failure for raw Mobius approximants is classical [BD02,
section 1]; we give a direct argument and transfer it to these lifts.

First, the divisor identity gives an exact initial horizon:

\[
 R_N(t)+\chi(t)=t\,m(N)\quad(0<t<N+1),\qquad
 \|R_N+\chi\|_{\mathcal E}^2\ge (N+1)|m(N)|^2.            \tag{15a}
\]

Indeed, for \(1\le t<N+1\),
\(\sum_{n\le N}\mu(n)\lfloor t/n\rfloor=1\); below 1 this sum is
zero. No tail approximation is involved.

If \(R_N\) converged in \(\mathcal E\), restriction to \((0,1)\),
where \(R_N(t)=tm(N)\), would force \(m(N)\to a\). The horizon
identity would make the limit equal to \(at-\chi(t)\) on every bounded
interval. Membership in \(\mathcal E\) forces \(a=0\); thus the limit
would be \(-\chi\), and (15a) would force \(m(N)=o(N^{-1/2})\).
This last assertion is impossible. For otherwise, writing
\(m(x)=m(\lfloor x\rfloor)\), summation by parts and analytic continuation
would give

\[
 \frac1{\zeta(s)}=(s-1)\int_1^\infty m(x)x^{-s}\,dx
 \qquad(\Re s>1/2).                                    \tag{15b}
\]

Take any critical-line zero \(\rho\), whose existence is classical, and
let \(s=\rho+v\), \(v>0\). Splitting the integral at a large fixed
point and then using \(m(x)=o(x^{-1/2})\) gives
\(v\int_1^\infty m(x)x^{-\rho-v}dx\to0\). Hence
\(v/\zeta(\rho+v)\to0\). A zero of order one gives a nonzero limit;
a zero of higher order gives unbounded magnitude. This is a contradiction.
No simplicity or numerical location of \(\rho\) is assumed.

Now suppose \(H_M\) converged in the original step norm. Formula (1) gives
\(a_{k,M}\to\mu(k)\) for every fixed odd \(k\), as shown by the
parent's convergent positive Euler product. Since
\(H_M(2)=2a_{1,M}-2A_M\), continuous cell evaluation forces
\(A_M\to a\). Expanding floors then gives the putative limit

\[
 H(n)=b(n)-2a\lfloor n/2\rfloor,\qquad
 b(n)=\sum_{k\le n,\ k\ {\rm odd}}\mu(k)\lfloor n/k\rfloor
     =\#\{j\ge0:2^j\le n\}.
\]

The last equality is the 2-adic divisor identity. Also
\(b=\sum_{j\ge0}D_2^j\chi\in\mathcal H\), with
\(\|b\|^2=\sum_{j\ge0}(2j+1)2^{-j}=6\).
Thus \(H\in\mathcal H\) forces \(a=0\). It follows that
\(S_M=2A_MD_2e-H_M\) converges in \(\mathcal E\).
The absolutely summable inverse in (4)--(5), dominated by the bounded
prefix norms of a convergent sequence, then implies convergence of
\(O_M\): for each fixed \(d\), \(S_{\lfloor M/d\rfloor}\) has the
same limit, and the tail \(\sum_{d>D}\|V(d)\|\) tends to zero uniformly.
Finally \(R_M=O_M-D_2O_{\lfloor M/2\rfloor}\) would converge, contradicting
the preceding argument. QED.

This proof uses no PNT or nontrivial-zero census. It uses only existence
of a critical-line zero, not an assertion that all zeros lie there. It
rules out strong convergence of these particular prescribed coefficients;
it says nothing against convergence of the optimal projections \(g_N\).

## 8. GT26.7 — precisely which omissions obstruct this target

For any fixed subset \(S\subset\{2,3,\ldots\}\),

\[
 \boxed{\chi\in\overline{\operatorname{span}}\{h_k:k\in S\}
 \iff \bigl(\mathrm{RH}\ \text{and every squarefree }k\ge2\text{ lies in }S\bigr).}
                                                               \tag{15}
\]

**Proof of necessity.** The full integer Nyman--Beurling criterion first
gives RH. For \(q\ge1\), set
\(\phi_q=q(q-1)1_{\{q-1\}}-q(q+1)1_{\{q\}}\), with the index-zero
term omitted, and \(f_q=\sum_{d\mid q}\mu(q/d)\phi_d\).
For \(k,q\ge2\), direct differences and divisor inversion give

\[
 \langle h_k,f_q\rangle=1_{k=q},\qquad
 \langle\chi,f_q\rangle=-\mu(q).                         \tag{16}
\]

These are Vasyunin's classical finite-support duals, reconstructed here.
If a squarefree \(q\) is omitted, \(f_q\perp h_k\) for every \(k\in S\)
but has nonzero pairing with \(\chi\). The squared approximation gap is
at least \(1/\|f_q\|^2\), regardless of how many other indices are added.

**Proof of sufficiency.** Under RH, the two nested full-norm convergence
statements in section 5 hold. For fixed \(\epsilon>0\), absolute scalar
convergence gives \(m_{\epsilon,N}\to1/\zeta(1+\epsilon)\).
Therefore the finite squarefree-supported combinations

\[
 -F_{\epsilon,N}
 =-\sum_{2\le n\le N}\mu(n)n^{-\epsilon}h_n
\]

converge as \(N\to\infty\) to
\(-R_\epsilon+e/\zeta(1+\epsilon)\), and then to \(\chi\) as
\(\epsilon\downarrow0\). This proves sufficiency. There is no diagonal
rate \(N(\epsilon)\) and no finite optimality claim. QED.

This resolves a scope issue left by the finite \(a_{9,16}\ne0\) computation:
a nonsquarefree generator can improve the exact finite optimum without
being indispensable for asymptotic approximation of this one target.
Indeed the span of squarefree generators has infinite codimension in
\(\mathcal H\): the independent duals \(f_q\) for nonsquarefree \(q\)
all annihilate it. Under RH it nevertheless contains \(\chi\) in its
closure. Target approximation and density in the entire ambient space are
not the same assertion. Nor is this restricted span automatically invariant
under \(D_2\); the parent's invariant-subspace observation theorem may not
be applied to it without checking invariance. No earlier finite optimum or
missing-squarefree obstruction is retracted.

## 9. GT26.8 — an unconditional full-norm bound at the classical scale

There are constants \(C,c>0\) such that, for every \(N\ge2\),

\[
 \boxed{\|R_N\|_{\mathcal E}+\|H_N\|_{\mathcal H}
       \le C\sqrt N\exp(-c\sqrt{\log N}).}               \tag{16a}
\]

This improves absolute summation for the **full** signed source, not only
its detail. Its exponent is still \(1/2\), not zero. It is a consequence
of the imported classical quantitative Mertens estimate

\[
 \left|\sum_{n\le x}\mu(n)\right|
 \le C_0 x\exp(-a\sqrt{\log x})\quad(x\ge2)             \tag{CM}
\]

for some \(C_0,a>0\); see Lee--Leong [LL24], introduction (1). We do not
claim (CM) as new, or import their numerical constants/finite zero table.
Neither the constants in (16a) nor a numerical starting height are certified.

**Proof.** Write \(Q_N(t)=\sum_{n\le N}\mu(n)n^{-1-it}\).
Partial summation of (CM), including the endpoint at \(N\), gives

\[
 |Q_N(t)-1/\zeta(1+it)|
 \le C_1(1+|t|)(1+\sqrt{\log N})e^{-a\sqrt{\log N}}.    \tag{16b}
\]

Indeed the tail integral is bounded by
\(\int_N^\infty e^{-a\sqrt{\log x}}dx/x
 = (2\sqrt{\log N}/a+2/a^2)e^{-a\sqrt{\log N}}\).
At \(t=0\) the reciprocal means its removable value zero. The sum
converges to it, since the same integral establishes convergence and
continuity from \(\Re w>1\).

Equation (16b) itself gives
\(|1/\zeta(1+it)|\ll\log^2(2+|t|)\): take an integer cutoff comparable
to \(\exp(K^2\log^2(2+|t|))\), with \(aK>3\), and bound the finite
sum by its harmonic absolute sum. Thus the candidate limiting Mellin
transform \(-\zeta(s)/(s\zeta(s+1/2))\), \(s=1/2+it\), lies in
\(L^2(dt)\), by the unconditional critical-line bound in section 5.

Let \(L=\log N\) and split the Mellin norm at
\(T=\exp(a\sqrt L/2)\). On \(|t|\le T\), (16b) and
\(\zeta(s)/s\in L^2(dt)\) bound the error norm by
\(C(1+\sqrt L)e^{-a\sqrt L/2}\). On \(|t|>T\), the separate bounds
\(|Q_N(t)|\le1+L\), \(|1/\zeta(1+it)|\ll\log^2(2+|t|)\), and
\(|\zeta(s)/s|\ll(1+|t|)^{-3/4}\) give error norm at most

\[
 C\bigl(1+L+\log^2(2+T)\bigr)T^{-1/4}
 \ll(1+L)e^{-a\sqrt L/8}.
\]

The logarithmic tail estimate follows by substituting \(t=Tu\) and
integrating \(u^{-3/2}(\log T+\log u)^4\); all four logarithmic moments
converge. Mellin--Plancherel therefore proves **unconditionally**

\[
 \|R_{1/2,N}-R_{1/2,\infty}\|
 \ll\exp(-b\sqrt{\log N})                              \tag{16c}
\]

with, for example, a sufficiently decreased \(b>0\). This is a norm
statement at coefficient damping \(1/2\), not at arbitrarily small damping.

Use vector summation by parts from section 6 with \(q=1/2\), subtracting
its limiting constant vector before estimating:

\[
 R_N=R_{1/2,\infty}+\sqrt N E_N
      -\sum_{n<N}(\sqrt{n+1}-\sqrt n)E_n,
 \quad E_n=R_{1/2,n}-R_{1/2,\infty}.
\]

Split the last sum at \(\sqrt N\). The first part is \(O(N^{1/4})\),
and the rest is \(O(\sqrt N e^{-b\sqrt{\log N}/\sqrt2})\).
This proves the bound for \(R_N\), after decreasing the positive constant
in the exponential. The bound for \(H_N\) follows from (9), since
\(\sqrt x e^{-c\sqrt{\log x}}\) is eventually increasing and the finite
initial segment can be absorbed into \(C\). QED.

For orientation, (CM) also implies \(m(N)\to0\). The geometric identity
for \(m_o\), followed by the nonnegative summable scalar convolution in
section 3, implies \(A_M\to0\). Thus \(H_M(n)\to b(n)\) on every
fixed cell, and the parent's detail error tends to zero. Section 7 proves
that these two facts still do not imply full-norm convergence. The mass
not controlled by fixed-cell/detail convergence is essential.

## 10. Attempted closure and the alternative exact target

The first attempted completion was to use the parent's rapidly decreasing
positive detail error to control the actual lift. The direct transfer is
already false at its certified \(8\to16\) example. Equations (4)--(9)
replace a nonexistent detail-to-full bound with a true full-to-full bound.
They also close the signed normalization problem \(|A_M|\le2\), but the
remaining full profile is exactly as difficult, at the growth-exponent
level, as raw Mobius sums of fractional parts.

A different sufficient and necessary target is now

\[
 \boxed{\mathrm{GT26.OPEN}:\quad
 \forall\eta>0\ \exists C_\eta<\infty\ \forall M\ge2:\quad
       \|H_M\|\le C_\eta M^\eta.}                        \tag{17}
\]

By (12), (17) is equivalent to RH. It does **not** demand that \(H_M\)
converge, remain uniformly bounded, approximate \(\chi\), or remove a
fixed fraction of the optimal residual at each doubling. The requested
uniform block-gain bound would imply (17) through RH, but the reverse
implication to that particular quantitative gain has not been proved.

Section 7 proves that replacing (17) by strong convergence of these
explicit lifts would ask for a false assertion, even under RH. This is why
the alternative is formulated as growth rather than approximation.

We attempted to bound (17) by using (5) and the scalar cancellation (7).
By themselves they yield only
\(\|H_M\|\le4+12\max_{n\le M}\|R_n\|=O(\sqrt M)\), by absolute
summation of \(\|D_ne\|\). Section 9 improves this to (16a), but its
logarithmic saving does not change the exponent. Taking an arbitrarily
small coefficient damping
would give subpower bounds **only** after proving full-norm convergence of
\(R_{\epsilon,N}\) for every small \(\epsilon>0\). Section 6 shows why
invoking (BS) there without its zero-free hypothesis is circular.

At the scalar level, (14) explains the unresolved cancellation without any
spectral model: a proof of subpower full norms would supply convergence of
\(\sum\mu(n)n^{-w}\) throughout \(\Re w>1/2\). None of the positive
\(\mu^2\) identities proves that. Conversely any hypothetical zero of real
part \(\beta>1/2\) forces \(\|H_M\|>M^\tau\) at arbitrarily large
cutoffs for every \(0<\tau<\beta-1/2\).

The component transfer and growth characterization are complete proposed
proofs. **The estimate (17), the uniform original gain, and RH remain open
in this submission.** This packet does not promote another equivalence to
a solution; it records the all-cutoff bounded transformation, identifies
exactly the arithmetic it preserves, and removes unnecessarily strong
convergence/finite-gain requirements from the alternative target.
