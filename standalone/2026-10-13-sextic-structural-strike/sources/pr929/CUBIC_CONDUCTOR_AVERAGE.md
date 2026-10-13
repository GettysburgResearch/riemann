# Averaging the cubic double-prime conductor in every fixed even moment

**Status:** proposed source-dependent theorem, with the deduction proved
below. The imported input is Proposition 8.1 of Alexandre de Faveri,
*Optimal large sieve for fixed order characters*, arXiv:2610.04045v1
(2 October 2026). Its full external proof is not independently certified
here. This note obtains a new positive bound for a specified portion of the
actual moment. The full generalized moment and the Riemann hypothesis
remain open.

**Scope:** the Eisenstein field, squarefree good column ideals, all
nonzero element rows, a fixed smooth radial row majorant, arbitrary
bounded column coefficients, and every fixed integer moment order.
Constants may depend on that order. No statement uniform in the order is
made. No native Möbius second moment or zero-free assumption is used.

**Sources.**

1. Alexandre de Faveri,
   [arXiv:2610.04045v1](https://arxiv.org/html/2610.04045v1),
   Proposition 8.1, Sections 2.3–2.5, and the proof of Theorem 1.2.
   The arbitrary-coefficient inequality in Proposition 8.1 is the analytic
   input. Theorem 1.2 has a constant depending on its fixed twist and is
   **not** invoked uniformly in a growing twist.
2. PR #925, frozen source
   [5ad900ff27d34f1a8f94d28e19c47a3b37de6e39](https://github.com/GettysburgResearch/riemann/commit/5ad900ff27d34f1a8f94d28e19c47a3b37de6e39),
   [SIGNED_CONDUCTOR_PROGRESS.md](../2026-10-10-joint-divisor-covariance/SIGNED_CONDUCTOR_PROGRESS.md),
   Sections 1–4: exact element-row projection, principal masks,
   incidence counting, and the older pointwise subconvex branches.
   The relevant identities and count are repeated here.
3. PR #919, source
   [9b04a887e171b3104a66cf57296ce5b0b2920d78](https://github.com/GettysburgResearch/riemann/commit/9b04a887e171b3104a66cf57296ce5b0b2920d78),
   SMALL_GCD_CONDUCTOR_REDUCTION.md, for the signed remainder comparison
   in Section 6. It is not needed for the new estimate.
4. PR #926, comparison source
   [086bf0560c0c2679a1fe41418f583d2c5ca743c3](https://github.com/GettysburgResearch/riemann/commit/086bf0560c0c2679a1fe41418f583d2c5ca743c3),
   [MOBIUS_OVERLAP_TAILS.md](https://github.com/GettysburgResearch/riemann/blob/086bf0560c0c2679a1fe41418f583d2c5ca743c3/standalone/2026-10-10-mobius-overlaps-and-sampled-moments/MOBIUS_OVERLAP_TAILS.md),
   Theorem 6.2: a different estimate for complete smooth signed
   incidence blocks. Section 5 below states the precise distinction.

## 1. The imported cubic polynomial inequality

Fix \(K=\mathbb Q(\sqrt{-3})\), a finite bad set \(S\), and the fixed
cubic Hecke family \(\{\xi_a\}\) of the first source, using its
Eisenstein normalization in Example 2.2. In that normalization,
\(\xi_{(a)}((b))=(a/b)_3\) for primary generators congruent to one
modulo three. Enlarge \(S\)
once, if necessary, to include the fixed ray moduli in its construction.
It is never enlarged to include a moving conductor. Write \(I(S)\) for
the good integral ideals. A star restricts a sum to squarefree ideals.
All norms are ideal norms.

For \(A,B,Q\ge1\), put
\[
M=\min(A,B),\qquad N=\max(A,B).
\]
The source input, with arbitrary complex coefficients \(\lambda_q\), is
\[
\sum_{a\sim A}\sum_{b\sim B}
\left|\sum_{q\sim Q}^{*}\lambda_q\,\xi_q(ab^2)\right|^2
\ll_{\epsilon,S,K}
(ABQ)^\epsilon
\left[AB+M^{2/3}N^{1/3}Q+
M^{1/3}N^{2/3}Q^{2/3}\right]\sum_q|\lambda_q|^2.
\tag{1.1}
\]
The \(a,b\) sums in this inequality are unrestricted good ideals.
Squarefreeness, coprimality, and fixed ray restrictions may therefore be
imposed on these rows by positivity. Coefficients may contain the values
and zeros of any moving character, without changing the constant.

By cubic reciprocity, the same bound applies with
\(\xi_{ab^2}(q)\) in the inner sum after a fixed finite ray partition.
Indeed the reciprocity factor depends only on the fixed classes of
\(a,b,q\); once the first two are fixed, it is a bounded factor in the
coefficient of \(q\). The number of classes is independent of
\(A,B,Q\) and all moving conductors.

## 2. Uniformity in a moving background character

### Theorem 2.1. A twisted conductor mean with its dependence displayed

Let \(\psi\) be a primitive finite-order Hecke character of trivial
infinite type whose conductor outside \(S\) is \(\mathfrak r\), with
\(R=N\mathfrak r\ge1\). Its local conductor at \(S\) belongs to a fixed
finite list. Its order is bounded, as is sufficient for the sextic
application. For squarefree coprime \(a,b\), also impose
\((ab,\mathfrak r)=1\). Then, for every real \(t\),
\[
\boxed{
\begin{aligned}
&\sum_{\substack{a\sim A,\ b\sim B\\
 a,b\ {\rm squarefree},\ (a,b)=(ab,\mathfrak r)=1}}
 |L(1/2+it,\psi\xi_{ab^2})|^2\\
&\quad\ll_{\epsilon,S,K}
(RAB)^\epsilon(2+|t|)^{C_\epsilon}
AB\left[
1+R^{1/2}(M/N)^{1/6}+(R/M)^{1/3}
\right]\\
&\quad\ll_{\epsilon,S,K}
(RAB)^\epsilon(2+|t|)^{C_\epsilon}ABR^{1/2}.
\end{aligned}}
\tag{2.1}
\]
The character in \(L\) means its primitive associate. Fixed incomplete
Euler factors at \(S\) may be inserted or removed at a bounded cost on
this line. Fixed ray restrictions are permitted. The constants are
uniform in \(\psi,\mathfrak r,A,B,t\); \(C_\epsilon\) is finite and
independent of those variables.

**Proof.** Outside \(S\), the conductor of the product is exactly
\(\mathfrak r ab\). At each prime of \(ab\), the cubic character has a
nontrivial local character of conductor that prime and \(\psi\) is
unramified. At the primes of \(\mathfrak r\), the cubic character is
unramified. There can be no cancellation between these disjoint local
conductors. The conductor at \(S\) has only finitely many possibilities.
After a finite partition, the analytic conductor is consequently
comparable to
\[
R\,Na\,Nb\,(2+|t|)^2.
\tag{2.2}
\]
The functional equation over the fixed imaginary quadratic field has a
fixed complex gamma factor. Its standard smoothed approximate functional
equation consists of a direct polynomial and a dual polynomial, each
of length at most
\[
Y=(RAB)^{1/2+\delta}(2+|t|)^{C_\delta}
\tag{2.3}
\]
with an arbitrarily small negative-power error in \(RAB\), times a
polynomial in \(2+|t|\). Here \(\delta>0\) can be as small as required.
Both polynomials have coefficients of modulus at most
\((Nn)^{-1/2}\) before their smooth weights.

We record why this use is uniform and does not insert a hidden power of
\(R\). Take the usual entire auxiliary factor \(\exp(z^2)\) in the
approximate functional equation. The weight is an inverse Mellin
integral of a gamma ratio times the conductor to the power \(z/2\).
On \(\Re z=\delta\), its real conductor factor is at most
\((RAB)^{\delta/2}\). Its imaginary conductor factor is a row multiplier
of modulus one. The gamma ratio has polynomial dependence on \(t\)
and integrable, rapidly decreasing dependence on its Mellin height
after the Gaussian factor is included. Truncation at (2.3) follows by
shifting the weight's contour far to the right. There are finitely many
possible fixed local gamma and bad-prime data. Thus Mellin inversion and
Cauchy–Schwarz reduce the desired mean to polynomially weighted
integrals of squared Dirichlet polynomials with a **common** cutoff
\(Nn\le Y\). On indices prime to \(S\), their coefficients, apart
from the cubic character, are
\[
\psi(n)(Nn)^{-1/2-\delta-i\tau},
\tag{2.4}
\]
and their conjugate versions. At primes in \(S\), use the actual
primitive product character's local values, which have modulus at
most one. They need not equal the product of its imprimitive factors
when a local conductor cancels. This fixed bad-prime part is separated
as \(s\) in (2.5) and does not affect the inner good-index coefficient.
The factors depending on \(Na\,Nb\)
outside the inner polynomial have modulus at most
\((RAB)^{O(\delta)}\). The dual root number has modulus one and is
outside its own polynomial; use
\(|P+\varepsilon_{\psi\xi}Q|^2\le2|P|^2+2|Q|^2\)
before summing. No splitting of that root number is required. The
principal-character case can occur here only when
\(\mathfrak r=a=b=1\), apart from fixed \(S\)-data; its bounded
number of extra approximate-functional-equation residue terms is
absorbed by the stated polynomial in \(t\).

It remains to reduce the unrestricted index \(n\) in (2.4) to the
squarefree index in (1.1). Uniquely write
\[
n=sqr^2,\qquad s\mid S^\infty,\quad q,r\in I(S),
\quad q\ {\rm squarefree}.
\tag{2.5}
\]
There is **no** coprimality condition between \(q\) and \(r\). The
factor from \(s\) and \(r^2\) is
\((\psi\xi_{ab^2})^{\rm prim}(s)\psi(r^2)\xi_{ab^2}(r^2)\).
Including its zeros, it has modulus at most one and is constant in
the inner \(q\)-sum for fixed \(s,r,a,b\).
Weighted Cauchy–Schwarz applies since
\[
\sum_{s\mid S^\infty}\sum_{r\in I(S)}
(N(sr^2))^{-1/2-\delta}<\infty.
\tag{2.6}
\]
Indeed the \(s\)-sum is a finite product of geometric series and the
\(r\)-sum is bounded by \(\zeta_K(1+2\delta)\). After this inequality,
the squared inner \(q\)-sum has the same weight as (2.6), cutoff
\(Nq\le Y/N(sr^2)\), and coefficients
\(\psi(q)(Nq)^{-1/2-\delta-i\tau}\). Their squared norm on a dyadic
block is \(O_\delta(Q^{-2\delta})\), and hence \(O_\delta(1)\).
The zero extension of \(\psi(q)\) imposes every moving conductor
exclusion within the coefficient vector.

Split the \(q\)-sum into dyadic blocks, use the finite reciprocity
partition described after (1.1), and apply (1.1). Dropping the row
restrictions only **after** taking its nonnegative squared modulus is
legitimate. Every \(Q\) is at most \(Y\); all powers of \(Q\) in
(1.1) are nonnegative. The convergent sum (2.6), the logarithmic
number of dyadic blocks, and \((RAB)^{O(\delta)}\) are absorbed by
reassigning the arbitrarily small loss. This gives
\[
(RAB)^\epsilon(2+|t|)^{C_\epsilon}
\left[
AB+M^{2/3}N^{1/3}(RAB)^{1/2}
+M^{1/3}N^{2/3}(RAB)^{1/3}
\right].
\tag{2.7}
\]
Dividing the last two terms by \(AB=MN\) gives exactly the two
ratios in (2.1). Since \(R\ge1\), \(M\ge1\), and \(M/N\le1\),
both ratios are at most \(R^{1/2}\). This proves the theorem.
\(\square\)

The sharper first line of (2.1) is retained because it records the
relative sizes of the two cubic labels. The simpler \(R^{1/2}\)
bound is sufficient for the all-order result below.

## 3. The exact Hermitian moment kernel

Fix an integer \(k\ge1\), \(D\ge2\), \(H\ge1\), and a fixed support
constant \(B_0\ge1\). Let
\[
A_u=\sum_n a_n\chi_n(u),\qquad |a_n|\le1,
\tag{3.1}
\]
where \(a_n=0\) unless \(n\) is good and squarefree with
\(Nn\le B_0D\). Here \(\chi_n\) is the zero-extended physical sextic
residue symbol of the pinned source. Fix a nonnegative radial
\(\Phi\in C_c^\infty(\mathbb C)\) that is at least one on the unit
disk. The smooth moment majorizes the full sharp element-row moment.

For a tuple
\(\mathbf t=(n_1,\ldots,n_k;m_1,\ldots,m_k)\), let \(r_p,s_p\)
be the numbers of occurrences of \(p\) in the two halves. Define
\[
c(\mathbf t)=\prod_i a_{n_i}\prod_i\overline{a_{m_i}},\quad
f=\prod_{r_p-s_p\not\equiv0\ (6)}p,\quad
q_0=\prod_{r_p-s_p\equiv0\ (6),\ r_p+s_p>0}p.
\tag{3.2}
\]
The residual character is \(\psi_{\mathbf t}\), primitive modulo
\(f\) when \(f\ne1\). The exact kernel is
\[
S_{\mathbf t}^{\Phi}(H)=
\sum_{u\in\mathcal O_K}
\Phi(u/\sqrt H)\psi_{\mathbf t}(u)
{\bf1}_{(u,q_0)=1}.
\tag{3.3}
\]
The character has its zero at every nonunit modulo \(f\).
Consequently this is the exact character product even when \(u\)
meets a tuple prime. There are no removed physical rows.

Let \(g_m\) be the product of the nonprincipal primes occurring
exactly \(m\) times in the full tuple. These ideals are pairwise
coprime, \(f=\prod_{m=1}^{2k}g_m\), and each is coprime to \(q_0\).
In particular \(g_1\) is the singleton product. A nonprincipal prime
with multiplicity two occurs twice on the same side, so
\[
g_2=ab,\qquad
a=\prod_{r_p=2,s_p=0}p,\qquad
b=\prod_{r_p=0,s_p=2}p.
\tag{3.4}
\]
Its contribution to the sextic character is cubic:
\(\chi_a^2\chi_b^4\).

Unit averaging makes (3.3) zero unless
\(\psi_{\mathbf t}\) is trivial on \(\mathcal O_K^\times\). In the
remaining case it descends to a finite-order Hecke ideal character,
denoted \(\widetilde\psi_{\mathbf t}\). If \(f\ne1\), it is
nonprincipal. Writing \(\Phi(z)=\phi(|z|^2)\), Mellin inversion and
the six generators per nonzero ideal give the exact identity
\[
S_{\mathbf t}^{\Phi}(H)=
\frac6{2\pi i}\int_{(1/2)}
\widehat\phi(s)H^sL(s,\widetilde\psi_{\mathbf t})
\prod_{p\mid q_0}(1-\widetilde\psi_{\mathbf t}(p)(Np)^{-s})\,ds.
\tag{3.5}
\]
Initially use \(\Re s>1\) and then shift. No pole is crossed because
the character is nonprincipal and the Mellin transform is holomorphic
for \(\Re s>0\). It decreases faster than every power on the new
vertical line, even if \(\phi(0)\ne0\). The retained principal mask
satisfies, uniformly in the tuple and in \(t\),
\[
\prod_{p\mid q_0}|1-\widetilde\psi_{\mathbf t}(p)(Np)^{-1/2-it}|
\le\prod_{p\mid q_0}(1+(Np)^{-1/2})
\ll_\eta(Nq_0)^\eta.
\tag{3.6}
\]
Thus this argument uses \(L\), with every exclusion still present,
and never an inverse \(L\)-factor.

### Lemma 3.1. The cubic family with its unit correction

Fix the ideals \(g_1,g_3,\ldots,g_{2k}\) and the residual exponent
at each of their primes. Partition \(a,b\) in (3.4) into the fixed
finite ray classes used in Section 1, and retain the classes for which
the total character is trivial on units. In each such class,
\[
\widetilde\psi_{\mathbf t}
=\psi_{\mathrm{bg}}\xi_{ab^2},
\qquad
N\operatorname{cond}^{S}(\psi_{\mathrm{bg}})
=Ng_1\prod_{m\ge3}Ng_m=:R.
\tag{3.7}
\]
Here \(\psi_{\mathrm{bg}}\) is independent of \(a,b\) within the
class. Its conductor at \(S\) is bounded by fixed data. The product
in (3.7) includes its primitive extension at \(S\).

**Proof.** Cubic reciprocity and the source's construction of
\(\xi_{ab^2}\) give precisely the local components
\(\chi_a^2\chi_b^4\) outside \(S\), up to its fixed bad-prime and
unit correction. That correction depends only on the finite classes
of \(a,b\). After fixing those classes, remove it from the fixed
remaining local character. The total character is unit-trivial, and
\(\xi_{ab^2}\) is already an ideal Hecke character, so their quotient
is an ideal Hecke character. Its nontrivial good local components
are exactly the primes of \(g_1g_3\cdots g_{2k}\), all disjoint
from \(ab\). Its fixed bad local component is the inverse of the
fixed component of \(\xi_{ab^2}\). No further finite-order
unramified ambiguity survives, since \(K\) has class number one.
This proves the conductor formula and the independence of \(a,b\).
It also explains why assuming the uncorrected background
element character to be unit-trivial would be unjustified.
\(\square\)

## 4. A new all-order sector bound

Define the positive accounting sum
\[
\mathcal Q_L^\Phi=
\sum_{\substack{\mathbf t:\ f\ne1\\L\le Ng_1<2L}}
|c(\mathbf t)|\,|S_{\mathbf t}^{\Phi}(H)|,\qquad L\ge1.
\tag{4.1}
\]
All double-prime conductors and all higher nonprincipal
multiplicities are included. Any additional tuple selector can be
imposed, since the accounting sum is nonnegative.

### Theorem 4.1. Average over the double-prime conductor

For every fixed \(k,B_0,S,\Phi\) and every \(\epsilon>0\),
\[
\boxed{
\mathcal Q_L^\Phi
\ll_{k,B_0,S,\Phi,\epsilon}
D^{k+\epsilon}H^{1/2}L^{3/4}.
}
\tag{4.2}
\]

**Proof.** Every principal-mask prime occurs at least twice. The
column support therefore implies
\[
(Nq_0)^2(Ng_1)(Nab)^2
\prod_{m\ge3}(Ng_m)^m\le(B_0D)^{2k}.
\tag{4.3}
\]
For fixed nonprincipal labels there are at most
\[
O_{k,B_0}\left(
D^k(Ng_1)^{-1/2}(Nab)^{-1}
\prod_{m\ge3}(Ng_m)^{-m/2}\right)
\tag{4.4}
\]
possible ideals \(q_0\). If the upper bound on its norm is below
one, there are no such tuples. Assignment of primes to their exact
incidence pattern among \(2k\) positions costs at most
\((2^{2k}-1)^{\omega(q_0f)}\ll_{k,\eta}(N(q_0f))^\eta\).
All tuple norms are bounded by a fixed power of \(D\), so this and
(3.6) cost \(D^\epsilon\) after choosing \(\eta\) sufficiently small.

For the background labels, first freeze their residual exponents.
There are at most \(5^{\omega(g_1g_3\cdots g_{2k})}\) possibilities,
also absorbed in the same loss. For the cubic labels, collect primes
with positive double exponent into \(a\) and those with negative
double exponent into \(b\) before counting their position assignments.
Their remaining position assignments contribute only the indicated
divisor loss. The background character in Lemma 3.1 is then genuinely
independent of the varying cubic labels; no supremum depending on
\(a,b\) is substituted inside a large-sieve average.

Fix \(g_1,g_3,\ldots,g_{2k}\) and dyadic ranges \(a\sim A,b\sim B\).
Theorem 2.1 and Cauchy–Schwarz over \(a,b\) imply
\[
\sum_{\substack{a\sim A,\ b\sim B\\
\text{permitted squarefree coprime labels}}}
|L(1/2+it,\widetilde\psi_{\mathbf t})|
\ll_\eta
(RAB)^\eta(2+|t|)^{C_\eta}ABR^{1/4}.
\tag{4.5}
\]
The \((AB)^{1/2}\) from the number of labels multiplies the square
root of the mean in (2.1). Finite class partitions add fixed factors.
The factor \(AB\) in (4.5) cancels the factor \((Nab)^{-1}\)
in (4.4) on this block. Integrate (4.5) against the rapidly
decreasing \(|\widehat\phi(1/2+it)|\) in (3.5). This leaves
\[
D^{k+\epsilon}H^{1/2}
(Ng_1)^{-1/2}\prod_{m\ge3}(Ng_m)^{-m/2}
\left(Ng_1\prod_{m\ge3}Ng_m\right)^{1/4}.
\tag{4.6}
\]
Every permitted \(a,b\) has norm at most \((B_0D)^k\), so there
are \(O_k(\log^2(2D))\) such blocks. This factor is absorbed into
the arbitrarily small loss.

Finally
\[
\sum_{g_1\sim L}(Ng_1)^{-1/4}\ll L^{3/4},
\qquad
\sum_g(Ng)^{-m/2+1/4}<\infty\quad(m\ge3).
\tag{4.7}
\]
The latter sums converge strictly, already with exponent \(5/4\)
at \(m=3\). Their residual positive losses can be chosen smaller
than that margin. Dropping all remaining coprimality and support
conditions in these nonnegative majorants proves (4.2).
\(\square\)

### Corollary 4.2. A diagonal-size part of every fixed moment

For all \(H\ge1,D\ge2\), the entire nonprincipal region
\[
\boxed{Ng_1\le H^{2/3}}
\tag{4.8}
\]
contributes at most \(O(HD^{k+\epsilon})\) to positive accounting.
Indeed sum (4.2) over the dyadic blocks with lower endpoint
\(L\le H^{2/3}\); the last block has the same bound up to a fixed
constant, and all earlier blocks form a geometric series.

This conclusion is valid for arbitrary bounded coefficient phases
and hence for the native Möbius coefficients within the stated
column support. It can be combined with all earlier positive
controlled regions by taking their union and counting overlaps once.
It is not a bound for the union's complement.

### Corollary 4.3. Retaining the two cubic conductor sizes

If (4.1) is additionally restricted to \(a\sim A,b\sim B\), write
it as \(\mathcal Q_{L;A,B}^\Phi\), and put
\(M=\min(A,B)\), \(N=\max(A,B)\). Then
\[
\boxed{
\mathcal Q_{L;A,B}^\Phi
\ll D^{k+\epsilon}H^{1/2}
\left[
L^{1/2}+L^{3/4}(M/N)^{1/12}
+L^{2/3}M^{-1/6}
\right].
}
\tag{4.9}
\]
Indeed use the first bound in (2.1) in (4.5), with
\(\sqrt{1+x+y}\le1+\sqrt x+\sqrt y\). The three remaining
background weights in (4.6) are \(1\),
\(R^{1/4}(M/N)^{1/12}\), and \(R^{1/6}M^{-1/6}\).
Summing \(g_1\) gives the displayed powers. For \(m\ge3\),
each of the three higher-multiplicity sums converges, since its
positive conductor exponent is at most \(1/4\).

Consequently another entire region, specified by the actual cubic
labels \(a,b\) of each tuple, has cost \(O(HD^{k+\epsilon})\):
\[
\boxed{
Ng_1\le H,\qquad
(Ng_1)^9\,\frac{\min(Na,Nb)}{\max(Na,Nb)}\le H^6,
\qquad
(Ng_1)^4\le H^3\min(Na,Nb).
}
\tag{4.10}
\]
These are exactly the conditions making each term in the brackets
of (4.9) at most \(H^{1/2}\). Dyadic partition changes only fixed
constants and logarithmic factors. This anisotropic region can
extend (4.8); no compatibility of arbitrary proposed norm scales
with the original column supports is assumed.

## 5. A strict gain over the pointwise-conductor accounting branches

Use eight pairwise coprime good squarefree labels and the tuple pattern
\[
(n_1,n_2;m_1,m_2)
=(ce a_1,\ cf_0 a_2;\ de b_1,\ df_0 b_2).
\tag{5.1}
\]
Choose norm scales
\[
Nc,Nd\asymp D^{3/5},\quad
Ne,Nf_0\asymp D^{7/30},\quad
Na_i,Nb_i\asymp D^{1/6}.
\tag{5.2}
\]
Each original factor has scale \(D\), since
\(3/5+7/30+1/6=1\). Take all rational prime supports disjoint,
so conjugate-prime incidence cannot supply a hidden reduction of the
singleton count. Good split primes in a fixed congruence class can
realize these scales, with unit-trivial residual characters if desired.
These are feasible scale comparisons, not lower bounds on a signed sum.

At \(H=D^{21/20}\), one has
\[
Ng_1\asymp D^{2/3},\quad Ng_2\asymp D^{6/5},
\quad Nq_0\asymp D^{7/15}.
\tag{5.3}
\]
The new average gives
\[
\boxed{\mathcal Q^\Phi\ll HD^{2-1/40+\epsilon}},
\qquad
-\frac{21}{40}+\frac34\frac23=-\frac1{40}.
\tag{5.4}
\]
For comparison, the older classical completion excess over \(HD^2\)
is \(2/3+(6/5)/2-21/20=13/60>0\). The old Wu branch has excess
\[
-\frac{21}{40}+\frac{359}{512}\frac23
+\frac{103}{512}\frac65>0.
\tag{5.5}
\]
Even the older balanced-divisor branch has positive excess, since
\[
4\cdot\frac23+\frac65=\frac{58}{15}>
3\cdot\frac{21}{20}=\frac{63}{20}.
\tag{5.6}
\]
Its prime-sensitive version is therefore also insufficient here.
For rational-prime incidence, the disjoint rational supports give
the same \(L,G\) and \(T=U=1\), so the previous pointwise rational
branches do not produce (5.4) either.

Both one-sided gcds have exponent \(3/5<99/140\), placing this
pattern inside the old small-gcd remainder at \(h=21/20\).
The matched cross-separation exponents are \(1-7/30=23/30\);
the unmatched factors are coprime. Thus the gain reaches a genuinely
separated part of that remainder. The word “gain” compares proved
upper bounds on the whole indicated incidence collection.

This comparison concerns **positive tuplewise absolute accounting**,
which persists under arbitrary extra tuple selectors and bounded
column coefficients. It is not a claim that every prior signed
method fails on the complete smooth block. For example, PR #926
Theorem 6.2, with its elementary \(b=1\) input and the two even
axes \(c,d\), already gives an upper bound
\(HD^{107/60+\epsilon}\) for the unselected complete signed block
with the source's structured coefficients. Each selected cubic
axis has cost exponent \(13/40\); the other labels cost
\(2/3+7/15\), giving \(107/60=2-13/60\).
That signed block bound does not bound the sum of the individual
absolute tuple kernels or arbitrary subsets of its terms. The new
result is the latter bound, not an improvement of that signed
complete-block estimate.

## 6. What changes in the remaining moment problem

At every fixed \(k\), remove (4.8) from any inherited signed
remainder by positive accounting. The cost is \(O(HD^{k+\epsilon})\).
For the fourth moment, if \(U(D,H)\) is the exact real signed
small-gcd remainder of the pinned #919 source, let \(U_{\rm new}\)
be its contribution restricted to \(Ng_1>H^{2/3}\), after removing
also any earlier controlled regions one wishes to retain. Then the
same source decomposition gives, with adjusted constants,
\[
M_4(D,D^h)\le C_\epsilon D^{h+2+\epsilon}
+2U_{\rm new}(D,D^h),\qquad
U_{\rm new}(D,D^h)\ge-C_\epsilon D^{h+2+\epsilon}.
\tag{6.1}
\]
Here \(1<h\le11/10\), and the native coefficients, smooth tests,
normalization, and other hypotheses are exactly those of that source.
These statements concern the exact real signed sum; they do not
replace it by an absolute sum or assert an upper bound for it.
The narrower complement still needs the requisite signed estimate.

In particular, a tuple of \(2k\) mutually coprime columns at scale
\(D\) has \(Ng_1\asymp D^{2k}\). In the physical range near
\(H=D\), it is far outside (4.8). Applied indiscriminately to that
block, (4.2) would have size \(H^{1/2}D^{5k/2+\epsilon}\),
which exceeds the desired \(HD^{k+\epsilon}\). Thus the result
does not close the generalized moment, imply its sampled version,
or improve the current zero-free half-plane.

The smallest new analytic dependency is (1.1); the smallest new
native bridge is the uniform-in-\(R\) deduction (2.1) with the
finite unit/ray adapter (3.7). The remaining arithmetic problem is
the signed large-singleton conductor average, not a missing
deterministic scale interpolation.
