# Prime-degree coherence and the signed distinct-column moment

**Status:** proposed mathematical obstruction and exact native identities. No
full native moment, improved zero-free half-plane, or RH conclusion is proved.

**Authorship:** native_structural_attack. This is new work for the structural
strike requested on 13 October 2026. The author did not write the root's
resonant-short-trace theorem. Any review of that theorem is recorded separately.

**Scope:** an exact, coefficient-uniform finite partition identity is applied
to the original Eisenstein sextic symbols and original Möbius coefficients,
after the explicitly stated prime-column selection. The resulting lower bound
is for the complete signed all-distinct prime-column contribution. It does
**not** refute the full composite-column native singleton core. An optional
Euler-parameter calculation explains why exact Möbius parity cannot be replaced
by a coefficient-insensitive random model.

**Sources inspected:**

- Repository `AGENTS.md` and `docs/REVIEWING.md`.
- PR #927, commit `f9939c957f5aac6b2099b591e4988991700a152b`,
  `standalone/2026-10-10-sextic-signed-reunion/SIGNED_AUXILIARY_REUNION.md`
  and `SMALL_W_CORE_AUDIT.md`: the complete signed inversion returns the native
  covariance and leaves its small-divisor primitive core.
- PR #913, commit `6498d6cc2eded03159c7332b25fd224ad07f89c1`,
  `standalone/2026-10-10-sextic-moment-descent/MOMENT_OBSTRUCTIONS.md`,
  Sections 2, 3, 6, 8, 10: the earlier broad multiplicative-coefficient
  counterexample, literal sixth-power masks, diagonal count, extraction, and
  family-GRH equivalence. The lower bound for a full prime-selected moment is
  not claimed as a new idea. The distinct-column lower bound below is the new
  strengthening.
- Classical analytic inputs: ideal counting in this fixed field;
  the prime ideal theorem `pi_K(x) ~ x/log x`; and the meromorphic continuation
  of the Dedekind zeta function with a simple pole of positive residue at one.
  No moving-field or moving-modulus prime ideal theorem is used. A primary
  account of the prime input is A. Burgin, *A New Elementary Proof of
  Landau's Prime Ideal Theorem, and Associated Results*,
  [arXiv:2406.08565v2](https://arxiv.org/html/2406.08565v2), Theorem 1,
  Lemma 1, and Section 1.3. These displayed statements were read; their
  complete proof is a named classical input and was not reconstructed here.

**What was actually run:** source reading and symbolic derivation; a separate
finite diagnostic checks the partition identity and selected inequalities.
Such a diagnostic does not prove the prime ideal theorem or an infinite moment.

**Smallest positive gap:** a signed estimate coupling the prime contribution
to its complete composite Möbius completion. Neither independent-prime
orthogonality nor collision subtraction supplies that estimate.

## 1. The relevant distinction

For a nonnegative fixed smooth norm profile W, the original family with trivial
fixed finite datum is

\[
 A_u(D)=\sum_{(n,S)=1}\mu_K(n)\chi_n(u)W(Nn/D),
 \qquad \chi_n(u)=(u/n)_6.
 \tag{1.1}
\]

Every symbol is zero at nonunits. An exponent divisible by six keeps that
zero. The rows are elements, and all units belong to the row family.

The prime-selected piece is

\[
 P_u(D)=-\sum_{\substack{\mathfrak p\notin S\\\mathfrak p\text{ prime}}}
                W(N\mathfrak p/D)\chi_{\mathfrak p}(u).
 \tag{1.2}
\]

Its coefficients are literally the native coefficients because
\(\mu_K(\mathfrak p)=-1\). However, primality is an additional arithmetic
column selector. It cannot be absorbed into a fixed smooth function of
\(Nn/D\), a finite-order Hecke twist, or a polynomially bounded moving
exclusion. The theorem below is about (1.2), not (1.1).

One might hope that removal of every repeated column makes (1.2) harmless:
the remaining tuples are the most strongly separated singleton tuples, and
the algebraic diagonal is absent. The next exact inequality shows that this
hope is false. A large coherent value survives complete collision subtraction.

## 2. A finite collision-free moment inequality

Let \(b_1,\ldots,b_N\) be complex numbers with \(|b_j|\le1\), and write

\[
 B=\sum_{j=1}^N b_j,\qquad V=\sum_{j=1}^N|b_j|^2.
 \tag{2.1}
\]

For a fixed integer \(k\ge1\), define the ordered, completely distinct
Hermitian moment polynomial

\[
 Q_k(b)=\sum_{\substack{j_1,\ldots,j_k,\ell_1,\ldots,\ell_k\\
                    \text{all }2k\text{ indices distinct}}}
       b_{j_1}\cdots b_{j_k}
       \overline{b_{\ell_1}\cdots b_{\ell_k}}.
 \tag{2.2}
\]

This is real: conjugation exchanges the two ordered groups of slots.
It need not be nonnegative at each individual vector.

### Theorem 2.1. Collision subtraction preserves a coherent spike

For every fixed \(k\) and every \(0<\delta<1\), there exists
\(C_{k,\delta}\), independent of \(N\) and of the vector, such that

\[
 \boxed{
 |Q_k(b)-|B|^{2k}|
 \le \delta |B|^{2k}+C_{k,\delta}(1+V)^k.
 }
 \tag{2.3}
\]

In particular,

\[
 Q_k(b)\ge(1-\delta)|B|^{2k}
                   -C_{k,\delta}(1+V)^k.
 \tag{2.4}
\]

One valid explicit choice is
\(C_{k,\delta}=((2k)!-1)^k\delta^{1-k}\).

**Proof.** Label the first k slots by + and the last k slots by −. For a
block C of a set partition of these 2k slots, let r(C) and s(C) be its
numbers of + and − slots, and put

\[
 p_{r,s}=\sum_j b_j^r\overline{b_j}^{s}.
 \tag{2.5}
\]

The exact partition-lattice inversion is

\[
 Q_k(b)=\sum_{\pi\in\Pi_{2k}}
       \left[\prod_{C\in\pi}(-1)^{|C|-1}(|C|-1)!\right]
       \prod_{C\in\pi}p_{r(C),s(C)}.
 \tag{2.6}
\]

To verify it without invoking an unproved combinatorial convention, fix an
index assignment to the 2k slots. If its equality partition is \(\rho\),
its coefficient on the right is the sum of the displayed partition Möbius
factor over \(\pi\le\rho\). This sum is one when every block of \(\rho\)
is a singleton and zero otherwise. For a block of size m, the relevant
sum is the signed number of permutations of m letters by cycle partition,
equal to \(1\cdot(1-1)\cdots(1-m+1)\): it is one at m=1 and zero at
m>1. This proves (2.6), including its signs.

The singleton partition contributes \(B^k\overline B^k=|B|^{2k}\).
For a different partition, let j be the number of nonsingleton blocks and
t its number of singleton blocks. Then j>=1 and

\[
 2j+t\le2k,\qquad t\le2k-2.
 \tag{2.7}
\]

Every nonsingleton block obeys \(|p_{r,s}|\le V\), because
\(r+s\ge2\) and \(|b_j|\le1\). Every singleton block has modulus |B|.
Consequently its unsigned monomial is at most \(V^j|B|^t\).
With \(U=1+V\ge1\) and \(y=|B|/\sqrt U\),

\[
 V^j|B|^t\le U^{j+t/2}y^t\le U^k y^t.
 \tag{2.8}
\]

For each of the finitely many integers \(0\le t\le2k-2\), and every
\(\eta>0\), one has \(y^t\le\eta y^{2k}+C_{k,\eta}\) for all
\(y\ge0\). For example split at
\(y=\max(1,\eta^{-1/2})\), increasing the finite constant if needed.
Sum (2.8) with the absolute values of the finite coefficients in (2.6),
and choose \(\eta\) sufficiently small in terms of \(k,\delta\).
This proves (2.3); realness gives (2.4). QED.

For the explicit constant, the sum of those absolute coefficients over
nontrivial partitions is \(A=(2k)!-1\): a partition with its cyclic
orders is a permutation. Set \(\eta=\delta/A\le1\). The split just
used gives \(y^t\le\eta y^{2k}+\eta^{-(k-1)}\), and hence total
constant \(A\eta^{-(k-1)}=A^k\delta^{1-k}\).

The bound is not an arbitrary lower bound for a positive kernel. Q_k itself
can have either sign. It says that all collision terms have a smaller
degree in the normalized large-value parameter \(|B|/\sqrt{1+V}\).
This is the finite U-statistic or Wick-polynomial mechanism, proved here
with its actual complex Hermitian slots.

### Corollary 2.2. Weighted row version

Let nonnegative weights w(u) satisfy \(\sum_u w(u)\le C_0 H\). For
each row let \(|b_j(u)|\le1\) and
\(\sum_j|b_j(u)|^2\le V_0\). Then

\[
 \sum_u w(u)Q_k(b(u))
 \ge(1-\delta)\sum_u w(u)|B(u)|^{2k}
           -C_0C_{k,\delta}H(1+V_0)^k.
 \tag{2.9}
\]

This follows by summing (2.4). There is no termwise positivity assertion
for the distinct tuple sums and no exchange of a signed selector with a
positive norm.

## 3. An actual signed all-singleton lower bound

Let \(0\le W\le1\) be nonzero, smooth, and supported in a fixed
\([a,b]\subset(0,\infty)\). Let S be a fixed finite bad-prime set.
For each fixed \(h>0\), put \(H=D^h\). Use either the sharp row weight
\(w_H(u)=\mathbf1_{0<Nu\le H}\), or a fixed nonnegative Schwartz
majorant \(w_H(u)=\Phi(u/\sqrt H)\) with \(\Phi\ge1\) on the unit
disk. In both cases \(\sum_{u\ne0}w_H(u)\ll H\).

Define the complete signed prime singleton sector

\[
 \begin{split}
 \mathcal S^{\rm prime}_{2k}(D,H)
 =\sum_{u\ne0}w_H(u)
 \sum_{\substack{\mathfrak p_1,\ldots,\mathfrak p_k,
                        \mathfrak q_1,\ldots,\mathfrak q_k\notin S\\
                  \text{all distinct prime ideals}}}
 &\prod_{i=1}^k[-W(N\mathfrak p_i/D)\chi_{\mathfrak p_i}(u)]\\
 {}\cdot&\prod_{j=1}^k
 [-W(N\mathfrak q_j/D)\overline{\chi_{\mathfrak q_j}(u)}].
 \end{split}
 \tag{3.1}
\]

Every nonempty tuple has 2k distinct prime ideals, hence every prime is a
singleton and every pair of its ideal columns is coprime. For k=2 it lies
in the completely separated four-axis prime subfamily. Every source zero
is retained; no complete-residue principal replacement is made.

### Theorem 3.1. The prime-selected signed singleton sector is too large

If \(k\ge1\) is fixed and

\[
                     0<h<\frac{6k}{5},
 \tag{3.2}
\]

then, for all sufficiently large D,

\[
 \boxed{
 \mathcal S^{\rm prime}_{2k}(D,D^h)
 \gg_{K,S,W,h,k}\frac{D^{2k+h/6}}{(\log D)^{2k+1}}.
 }
 \tag{3.3}
\]

In particular it exceeds the proposed diagonal power
\(HD^{k+\epsilon}\) for every sufficiently small fixed positive epsilon.
The bound is for the whole signed distinct-prime row sum, not just its
positive contribution from selected rows.

**Proof.** Write

\[
 L_D=\sum_{\mathfrak p\notin S}W(N\mathfrak p/D),\qquad
 V_D=\sum_{\mathfrak p\notin S}W(N\mathfrak p/D)^2.
 \tag{3.4}
\]

The fixed-field prime ideal theorem and partial summation give

\[
 L_D\sim\frac D{\log D}\int_0^\infty W(t)\,dt,
 \qquad V_D\ll\frac D{\log D}.
 \tag{3.5}
\]

Let \(Y=H^{1/6}\), and choose a prime ideal \(\mathfrak r\notin S\)
with \(Y/2<N\mathfrak r\le Y\). Choose its primary generator r and
the literal element row \(u=r^6\). Distinct prime ideals give distinct
sixth-power element rows: equality would imply equality of their principal
ideals. These rows satisfy \(Nu\le H\), so their weight is at least one.
For every column prime \(\mathfrak p\ne\mathfrak r\),

\[
 \chi_{\mathfrak p}(r^6)=1,
 \qquad \chi_{\mathfrak r}(r^6)=0.
 \tag{3.6}
\]

Hence \(|P_{r^6}(D)|=L_D-W(N\mathfrak r/D)\ge L_D-1\).
This calculation remains true when the copying prime is much larger or
smaller than D. There is no need to assume h<6, and no false coprimality
condition is imposed on the copying row.

There are \(\gg Y/\log Y\) copying prime ideals. Positivity of the full
prime moment therefore gives

\[
 \sum_{u\ne0}w_H(u)|P_u(D)|^{2k}
 \gg \frac{H^{1/6}}{\log H}(L_D-1)^{2k}
 \gg\frac{D^{2k+h/6}}{(\log D)^{2k+1}}.
 \tag{3.7}
\]

Apply Corollary 2.2 with
\(b_{\mathfrak p}(u)=-W(N\mathfrak p/D)\chi_{\mathfrak p}(u)\),
\(V_0=V_D\), and \(\delta=1/2\). Its left side is exactly (3.1),
and its error is

\[
 O_{k,W}(H(1+V_D)^k)
       \ll\frac{D^{k+h}}{(\log D)^k}.
 \tag{3.8}
\]

By (3.2), the power in (3.7) exceeds that in (3.8): their difference is
\(k-5h/6>0\). The smaller error is eventually at most half the main
lower bound. This proves (3.3). QED.

### What this changes, and what it does not

The earlier broad coefficient obstruction already prevents arbitrary
multiplicative twists from inheriting the native theorem. Theorem 3.1 is
stronger in a different direction: **with the original coefficients on
every retained column, the complete signed all-distinct prime subfamily
is itself too large**. An algebraic diagonal subtraction or a connected
tuple restriction does not eliminate the coherent sixth-power spikes.

Consequently a proof of the full native singleton theorem cannot be stable
under every arithmetic column selector. In particular, a prime-by-prime
degree decomposition followed by an absolute sum of separate bounds is
not an admissible route to the desired moment. It would need cancellation
between the prime part and its complete composite completion.

The composite native singleton sector is still unrefuted. The signs
\((-1)^{\omega(n)}\) vary across its prime degrees, so it can cancel the
large prime-selected sector. Theorem 3.1 supplies no lower bound for that
full sum and no counterexample to the original native moment hypothesis.

## 4. A short analytic explanation of the parity instability

This section is a separate exact deduction, not an estimate for the native
family. It uses only local behavior of the Dedekind zeta function at one;
no Selberg–Delange asymptotic or conjectural zero-free half-plane is needed.

For fixed \(z\) with \(|z+1|<1/2\), define

\[
 a_z(n)=\mu_K(n)^2z^{\omega_K(n)}\mathbf1_{(n,S)=1},
 \quad A_z(D)=\sum_n a_z(n)W(Nn/D).
 \tag{4.1}
\]

At z=-1 this is the literal principal-row Möbius sum. Initially for
\(\Re s>1\), its Dirichlet series factors as

\[
 F_z(s)=\prod_{\mathfrak p\notin S}(1+z(N\mathfrak p)^{-s})
       =\zeta_K(s)^z E_z(s).
 \tag{4.2}
\]

Near s=1, the factor E_z is analytic and nonzero. Indeed its good-prime
local factors are
\((1+zq^{-s})(1-q^{-s})^z=1+O_z(q^{-2\Re s})\);
the linear terms cancel, so their logarithms converge normally for
\(\Re s>1/2\) after separating finitely many primes. The omitted S factors
are analytic and nonzero near one. Since \(|z|<3/2\) and every allowed
prime norm is at least two, no factor \(1+z/q\) vanishes there.

Writing \(\zeta_K(s)=\kappa_K(s-1)^{-1}g(s)\), with \(g(1)=1\),
gives on a slit neighborhood

\[
             F_z(s)=(s-1)^{-z}U_z(s),\qquad U_z(1)\ne0.
 \tag{4.3}
\]

For z in this disk with z!=−1, the factor has a noninteger local order
and cannot extend holomorphically through one. For a direct verification,
if such an extension were nonzero it would have an integer zero order m,
whereas along the positive real axis
\((s-1)F_z'(s)/F_z(s)\to-z\), forcing m=-z. An identically zero
extension is impossible because the Euler product is nonzero for real
s sufficiently large. At z=-1 the simple zero at one is allowed.

### Proposition 4.1. Every fixed noninteger perturbation recreates a
principal-row obstruction

For every z in the stated punctured disk and every \(\eta>0\),

\[
                         A_z(D)\ne O(D^{1-\eta}).
 \tag{4.4}
\]

**Proof.** Take W nonnegative and nonzero as in Section 3. Its Mellin
transform \(\widehat W(1)=\int W(t)\,dt\) is positive. If the indicated
bound held, the integral

\[
 \int_0^\infty A_z(D)D^{-s-1}\,dD
 \tag{4.5}
\]

would be holomorphic for \(\Re s>1-\eta\), because A_z vanishes below a
fixed positive support threshold. For \(\Re s>1\), termwise integration
identifies it with \(\widehat W(s)F_z(s)\). Division by the nonzero
\(\widehat W\) near one would extend F_z holomorphically there,
contradicting (4.3). QED.

The same instability is visible in a tangent coefficient. Differentiating
at z=-1 gives \(\partial_z a_z(n)|_{-1}=-\mu_K(n)\omega_K(n)\).
Its Dirichlet series is

\[
 \left.\partial_zF_z(s)\right|_{z=-1}
   =F_{-1}(s)\sum_{\mathfrak p\notin S}
                         \frac1{(N\mathfrak p)^s-1}.
 \tag{4.6}
\]

The prime sum equals \(\log\zeta_K(s)+R(s)\), with R analytic near
one: the difference of the prime-power coefficients is absolutely
convergent for \(\Re s>1/2\), apart from the finitely omitted factors.
Since \(F_{-1}(s)\) has a simple zero there, (4.6) contains a nonzero
\((s-1)\log(s-1)\) term and is not holomorphic at one. Thus even the
fixed logarithmically bounded weight \(\omega_K(n)\) prevents every
power-saving bound at the principal row. This is distinct from a weight
\(\log Nn\), which differentiates F with respect to s and preserves
holomorphy wherever F is holomorphic.

### Proposition 4.2. The deformation obstruction persists after full
arithmetic row averaging

Define \(A_{z,u}(D)=\sum_n a_z(n)\chi_n(u)W(Nn/D)\) and its sharp
\(2k\)-th row moment \(M_{2k,z}(D,H)\). For every fixed \(h>0\),
\(k\ge1\), and punctured-disk z as above,

\[
 \boxed{
 \limsup_{D\to\infty}
 \frac{\log(1+M_{2k,z}(D,D^h))}{\log D}
 \ge2k+\frac h6.
 }
 \tag{4.7}
\]

In particular, a diagonal-size moment fails whenever \(h<6k/5\).

**Proof.** For every fixed \(\varepsilon>0\), the elementary fixed-order
divisor bound gives \(|a_z(n)|\ll_{z,\varepsilon}(Nn)^\varepsilon\).
Let \(Y=D^{h/6}\), and let \(Y/2<N\mathfrak r\le Y\) be a copying
prime outside S. On the row r^6, the only deletion is at r. Its total
absolute effect is

\[
 \begin{split}
 |A_z(D)-A_{z,r^6}(D)|
 &\le\sum_{\mathfrak r\mid n}|a_z(n)W(Nn/D)|\\
 &\ll_{z,\varepsilon,W} D^\varepsilon(D/N\mathfrak r+1).
 \end{split}
 \tag{4.8}
\]

If \(N\mathfrak r>bD\), the sum is exactly empty. Otherwise the
right side is \(O(D^{1+\varepsilon-h/6}+D^\varepsilon)\).

By Proposition 4.1, for every sufficiently small fixed \(\eta>0\)
there are arbitrarily large D with \(|A_z(D)|>D^{1-\eta}\).
Choose \(\eta,\varepsilon>0\) with
\(\eta+\varepsilon<h/6\) and \(\eta+\varepsilon<1\). Then (4.8)
is at most half this value on all the copying primes once D is large.
There are \(\gg D^{h/6}/\log D\) such primes. Consequently, along
those arbitrarily large scales,

\[
 M_{2k,z}(D,D^h)
 \gg \frac{D^{2k(1-\eta)+h/6}}{\log D}.
 \tag{4.9}
\]

Taking the upper limit and then arbitrarily small eta proves (4.7).
No asymptotic formula for A_z, induction on scales, or moving-character
bound was used. QED.

The same argument applies to the tangent coefficient
\(\mu_K(n)\omega_K(n)\): it is divisor-bounded and its Mellin series
has the nonremovable singularity described above.

## 5. Why the independent-residue benchmark misses this issue

Give each good prime ideal an independent uniform sixth root of unity
X_p, and put \(X_n=\prod_{p\mid n}X_p\) on squarefree ideals.
For every fixed k and every family of coefficients \(|c(n)|\le1\)
supported on squarefree \(Nn\asymp D\),

\[
 \mathbb E\left|\sum_n c(n)X_n\right|^{2k}
 \ll_{k,\varepsilon}D^{k+\varepsilon}.
 \tag{5.1}
\]

Here is the complete counting reason. A tuple survives expectation only
if at every prime the number of left occurrences minus right occurrences
is divisible by six. Thus every occurring prime has multiplicity at least
two. Assign each prime its nonempty incidence subset of the 2k slots.
There are finitely many possible subsets; their squarefree ideal products
q_I have
\(\prod_I(Nq_I)^{|I|}\ll D^{2k}\), and hence
\(\prod_I Nq_I\ll D^k\). Fixed-order divisor counting then gives at
most \(D^{k+\varepsilon}\) surviving tuples. Take absolute values of
their coefficients. This is the diagonal count already present in
#913; it is included only to make the contrast's exact logical scope clear.

The benchmark (5.1) holds for every unit-modulus perturbation
\(c(n)=\mu_K(n)^2z^{\omega_K(n)}W(Nn/D)\), with \(|z|=1\).
For k<6 its moment is even unchanged by arbitrary primewise phase
rotations, since local balance modulo six then forces exact left/right
balance. At k>=6 aliases can change the value, but the same bound remains.

Proposition 4.2 shows that arbitrarily small rotations away from z=-1
have large arithmetic row moments. Therefore this independent-residue
benchmark cannot be transferred to the actual row measure by an argument
that is insensitive to the exact Möbius phase. This is a precise failure
of a proposed comparison strategy, not a claim that probabilistic methods
can never help.

## 6. An exact native prime-rooting identity to retain in a repair

The positive result of this lane is algebraic: prime extraction can be
done while retaining its complete composite Möbius companion. This does
not yet supply an upper bound, but it fixes the source that a repaired
analytic approach must estimate.

Write \(\xi_u(n)=\nu(n)\chi_n(u)\), with every original zero, and
let D be large enough that the support of W excludes the unit ideal.
Define

\[
 J_{u,p}(D)=
 \sum_{\substack{(m,pS)=1}}
  \mu_K(m)\xi_u(m)
  \frac{W(Np\,Nm/D)}{\log(Np\,Nm)}.
 \tag{6.1}
\]

There is no singular denominator: every nonzero term has
\(Np\,Nm\ge aD>1\). The sum includes m=1 when its physical support
permits it. It is the actual shorter native inverse sum at scale D/Np,
with the exact p exclusion and a coupled smooth logarithmic profile.

### Proposition 6.1. Exact prime-rooting, with no prime-degree loss

\[
 \boxed{
 A_u(D;W)=-\sum_{p\notin S}(\log Np)\xi_u(p)J_{u,p}(D).
 }
 \tag{6.2}
\]

All sums are finite. A row nonunit at p annihilates both sides' relevant
terms. The identity holds for arbitrary fixed finite-order nu and all
original finite or moving exclusions included in S.

**Proof.** A squarefree nonunit ideal n appears on the right once for
each prime p dividing n, with m=n/p. Its coefficient is
\(-\mu_K(n/p)\xi_u(p)\xi_u(n/p)=\mu_K(n)\xi_u(n)\), including
the zero case. The sum of its weights is
\(\sum_{p\mid n}\log Np/\log Nn=1\), because n is squarefree.
Conversely every nonzero summand on the right reconstructs a squarefree
n prime to the exclusions. This proves the identity coefficientwise.
QED.

For a nonnegative row weight the resulting exact Ward pairing is

\[
 \sum_u w_H(u)|A_u|^{2k}
 =-\sum_p\log Np\sum_u w_H(u)\xi_u(p)J_{u,p}
                                      \overline{A_u}|A_u|^{2k-2}.
 \tag{6.3}
\]

This identity applies to the native nonlinear test on the right; it does
not grant an arbitrary-test dual norm. The m=1 part of (6.2) is exactly
the large prime piece (1.2). Every m>1 term is its required composite
companion. Taking a norm of the m=1 part first loses the possible
cancellation certified as necessary by Theorem 3.1.

An equivalent logarithmically weighted identity is

\[
 \sum_n\mu_K(n)\xi_u(n)(\log Nn)W(Nn/D)
 =-\sum_p(\log Np)\xi_u(p)
         A_u^{(p)}(D/Np;W),
 \tag{6.4}
\]

where \(A_u^{(p)}\) is the same native polynomial with p excluded.
It should not be replaced by an independently centered prime random
variable: the conditioning needed to make different residue coordinates
independent is not available from a short arithmetic row ball.

Equations (6.2)–(6.4) are proposed as a source-preserving interface for a
future signed integration-by-parts or dispersion argument. Estimating
their Ward pairing at \(HD^{k+\varepsilon}\) remains open; writing
the identity itself does not reduce that analytic difficulty. The rigorous
advance here is the obstruction to a tempting larger class and the exact
identification of the cancellation that class discards.
