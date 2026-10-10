# Cross-gcd graphs: overlapping fourth-moment events and all-order matchings

Status: proposed source-conditional inequalities for actual signed sectors of the inverse sextic moments. Complete proofs are supplied below. The fourth-moment union is controlled without the earlier disjointness hypothesis, with its sharper single-edge cost through a substantially larger range. A separate theorem controls every fixed disjoint cross matching in every fixed even moment. Neither result bounds the remaining balanced, mutually separated sector or establishes a new zero-free boundary.

Scope: the zero-extended Möbius/sextic family over the Eisenstein field, every nonzero element row, fixed finite-order character and smooth tests. All repeated row primes and sixth-power copies remain. The optional exponent b<1 is an explicitly uniform pointwise premise; b=1 uses only the native second moment and elementary counting.

Exact source dependencies:

- PR #923, commit `1a1152008706f7e24fa1efe4990588f8f99c5d8d`, `standalone/2026-10-10-sextic-separated-cores/CROSS_SIDE_SEPARATION_SECTOR.md`: the precise smaller-scale moving-exclusion native second moment (1.2), the single-edge theorem (7.6), and its carefully scoped pointwise premise (7.1). The present proof rederives the single-edge estimate as a special case of its matching theorem.
- PR #915, commit `9959364671f89b86f3992ec5ed5e19f804eb607b`, `standalone/2026-10-10-sextic-critical-core/ANISOTROPIC_SINGLETON_CORES.md`: the exact forward Euler correction and its anisotropic norm proof, Sections 2–3. The proof there permits any chosen second-moment axis, kept fixed throughout its convolution; choosing the largest merely optimizes the result.
- PR #913, commit `6498d6cc2eded03159c7332b25fd224ad07f89c1`, `standalone/2026-10-10-sextic-moment-descent/GENERAL_MOMENT_ATTACK.md`: the exact shared-prime incidence decomposition and elementary ideal counting. No new sieve estimate is assumed here.
- PR #914, commit `0cc0428fedbbfc340044c7451b3d392c1da9a103`, `CONDUCTOR_SECTORS.md`, preserved in `standalone/2026-10-10-sextic-joint-core/sources/pr914/CONDUCTOR_SECTORS.md`: positive absolute accounting for the complementary full-tuple regions. This is used only to pass a proved complete signed-sector estimate to the hard conductor region.
- PR #919, commit `9b04a887e171b3104a66cf57296ce5b0b2920d78`, `standalone/2026-10-10-averaged-conductor-frontier/SMALL_GCD_CONDUCTOR_REDUCTION.md`: the existing fourth-moment reduction with its two original within-side gcd thresholds.

The inherited analytic inputs retain their own source conditions and proof status. Finite algebra diagnostics, if accompanying this note, do not prove those inputs or the infinite estimates below.

## 1. Objects and exactly quantified inputs

Fix the Eisenstein field K, a finite excluded set S, a finite-order character nu, and fixed compact smooth tests W_i supported in [alpha_i,beta_i] inside (0,infinity). Write

\[
\eta_u(n)=\nu(n)\chi_n(u),\qquad
A_{i,u}^{(q)}(X)
=\sum_{(n,qS)=1}\mu_K(n)\eta_u(n)W_i(Nn/X).
\tag{1.1}
\]

The sextic symbols have their literal zeros at nonunits. Ideals use the fixed primary-generator convention. Let D>=2 and H=D^h, with h>1 fixed. Use one fixed nonnegative compact smooth radial row test Phi, whose support is contained in Nu<=c_Phi H after scaling. The radial hypothesis matches the inherited hard-complement accounting used in Section 7. Every smaller column scale below uses this same physical row range.

Assume the native moving-exclusion input

\[
\sum_{0<Nu\le c_\Phi H}|A_{i,u}^{(q)}(X)|^2
\ll_\epsilon D^\epsilon H X,
\qquad 1/\beta_i\le X\le D,
\quad Nq\le D^{A_0},
\tag{NM2}
\]

for each fixed polynomial bound A_0, uniformly in q, X, and the row range. The implicit constants may depend on the fixed data. Empty scales vanish. As in #923, the single zero row introduced by shortened unit columns is O(1) and can be absorbed when passing to the complete smooth norm

\[
\|F\|_{\Phi,H}^2=\sum_u\Phi(u/\sqrt H)|F(u)|^2.
\]

For the stronger estimates assume, separately,

\[
|A_{i,u}^{(1)}(X)|\ll_\epsilon D^\epsilon X^b,
\qquad \tfrac12<b\le1,
\quad 0<Nu\le c_\Phi H,
\quad 1/\beta_i\le X\le D.
\tag{PW}
\]

At b=1, this follows from elementary ideal counting. At b<1, it must hold uniformly in the moving row; a fixed-character estimate with unspecified conductor constants is not enough. Set

\[
a=2b-1>0.
\tag{1.2}
\]

The inherited anisotropic core result is used in the following explicit form: for any fixed index j and any polynomial exclusion ell,

\[
\left\|
\sum_{\substack{(n_i,n_l)=1\ (i\ne l)\\(\prod n_i,\ell S)=1}}
\prod_i\mu_K(n_i)\eta_u(n_i)W_i(Nn_i/Y_i)
\right\|_{\Phi,H}
\ll D^\epsilon\sqrt H\,Y_j^{1/2}\prod_{i\ne j}Y_i^b.
\tag{1.3}
\]

The index j need not maximize the Y_i: the source's exact forward correction applies with weights alpha_j=1/2 and alpha_i=b otherwise. Every pairwise sum of these weights exceeds one. Formula (1.3) therefore follows from (NM2), (PW), and that exact correction, with the same fixed tests and row height at every shortening. No higher-moment premise enters.

## 2. A bounded gcd selector between two native polynomials

The following elementary covariance lemma is useful when a graph cycle creates an extra condition between two otherwise free factors.

### Lemma 2.1

Let Q be a polynomially bounded squarefree ideal. Let omega(u) be any row multiplier with |omega(u)|<=1. Let f be any function on ideals with |f(c)|<=1, allowed to depend on D, X, Y, Q, and other frozen polynomial labels. Then

\[
\begin{aligned}
\mathcal K_f(X,Y;Q)
={}&\sum_u\Phi(u/\sqrt H)\omega(u)
\sum_{(nm,QS)=1}
\mu_K(n)\mu_K(m)\eta_u(n)\overline{\eta_u(m)}\\
&\hspace{20mm}\cdot W_i(Nn/X)\overline{W_l(Nm/Y)}
f((n,m))
\end{aligned}
\]
satisfies
\[
\boxed{|\mathcal K_f(X,Y;Q)|
\ll_\epsilon D^\epsilon H\sqrt{XY}.}
\tag{2.1}
\]

Only (NM2) is used. This is an integrated covariance estimate, not a pointwise assertion in u and not a bound for arbitrary row-dependent column coefficients.

**Proof.** Put c=(n,m), n=c n_0, m=c m_0. The remaining factors are prime to cQ and mutually coprime. Remove only their mutual coprimality by

\[
{\bf1}_{(n_0,m_0)=1}=\sum_{e\mid(n_0,m_0)}\mu_K(e).
\]

After n_0=e r and m_0=e s, the exact identity is

\[
\begin{aligned}
\mathcal K_f
=\sum_{\substack{c,e\ {\rm squarefree}\\(ce,QS)=1,\ (c,e)=1}}
f(c)\mu_K(e)
\sum_u\Phi(u/\sqrt H)\omega(u)
{\bf1}_{(u,ce)=1}\\
\hspace{12mm}\cdot
A_{i,u}^{(Qce)}(X/N(ce))
\overline{A_{l,u}^{(Qce)}(Y/N(ce))}.
\end{aligned}
\tag{2.2}
\]

This is finite on physical support. No character division appears. The two equal factors at ce multiply to the literal coprimality indicator; the surviving sign mu(e) comes from the exact inclusion–exclusion.

Cauchy–Schwarz and (NM2) bound each complete row covariance by

\[
D^\epsilon H\sqrt{XY}/N(ce).
\]

All nonempty labels satisfy N(ce)<<D, and Qce remains polynomially bounded. The absolute majorant is therefore bounded by

\[
D^\epsilon H\sqrt{XY}
\left(\sum_{Nc\ll D}(Nc)^{-1}\right)
\left(\sum_{Ne\ll D}(Ne)^{-1}\right)
\ll D^\epsilon H\sqrt{XY}(\log(2D))^2.
\]

Absorb the fixed logarithmic power by reassigning epsilon. The arbitrary f and omega have only been discarded after this exact identity and the covariance bound. Squarefree restrictions and support conditions are removed only in this positive majorant. This proves (2.1). QED.

In particular, arbitrary upper or lower thresholds on the residual gcd are allowed. This supplies precisely the additional endpoint condition in the four-cycle argument below.

## 3. Fixed divisibility and a one-sided incidence selector

For a tuple of squarefree ideals, its shared incidence labels c_I, |I|>=2, consist of the primes occurring in exactly the indicated coordinates. A one-sided incidence selector Theta is any bounded function of those shared labels, with |Theta|<=1, independent of the singleton ideals after they are fixed. It may vary with D and fixed norm thresholds.

Examples include: all pairwise gcds below a threshold; the singleton-length cost selector used in the earlier incidence reductions; and any intersection of conditions on shared-label norms. An arbitrary selector involving individual singleton ideals is not included.

For good squarefree q_1,...,q_k with Nq_i<=beta_i D, put X_i=D/Nq_i and define

\[
\begin{aligned}
F_{\mathbf q,\Theta}(u)
=\sum_{(a_i,q_iS)=1}
\Theta(q_1a_1,\ldots,q_ka_k)
\prod_i\mu_K(a_i)\eta_u(a_i)W_i(Na_i/X_i).
\end{aligned}
\tag{3.1}
\]

Thus the original polynomial restricted to q_i|n_i equals
prod_i mu(q_i) eta_u(q_i) times (3.1), with its zeros preserved. Formula (3.1) is a definition, not division by that possibly zero scalar.

### Lemma 3.1

For every fixed index j,

\[
\boxed{
\|F_{\mathbf q,\Theta}\|_{\Phi,H}^2
\ll_\epsilon D^\epsilon H X_j\prod_{i\ne j}X_i^{2b}.
}
\tag{3.2}
\]

The estimate is uniform in the fixed divisibility labels and in every selector of the stated kind. In particular,

\[
\|F_{\mathbf q,\Theta}\|_{\Phi,H}^2
\ll D^\epsilon H D^{1+2b(k-1)}
\frac{1}{Nq_j}\prod_{i\ne j}(Nq_i)^{-2b}.
\tag{3.3}
\]

**Proof.** Let Q=lcm(q_1,...,q_k). Split exactly the primes of each a_i that lie in Q:

\[
a_i=t_i x_i,\qquad t_i\mid Q/q_i,\qquad (x_i,Q)=1.
\]

The t_i may overlap each other; no pairwise coprimality between them is imposed. They are fixed divisors of a polynomial label, so they cost only subpower divisor sums. The prime-incidence pattern inside Q is now fixed.

Outside Q, use the exact shared labels c_I of the squarefree x_i. Their singleton factors are pairwise coprime and avoid Q times every shared c_I. After fixing the t_i and c_I, the selector Theta is a scalar of modulus at most one, and the remaining core has lengths

\[
Y_i=\frac{X_i}{Nt_i\prod_{I\ni i}Nc_I}.
\]

All exterior character factors have modulus at most one. Apply (1.3) with the same chosen index j in every term. Set alpha_j=1/2, alpha_i=b for i!=j. Minkowski bounds the norm by

\[
D^\epsilon\sqrt H\prod_iX_i^{\alpha_i}
\prod_i\sum_{t_i\mid Q/q_i}(Nt_i)^{-\alpha_i}
\prod_{|I|\ge2}\sum_{c_I}(Nc_I)^{-\sum_{i\in I}\alpha_i}.
\tag{3.4}
\]

Every shared-label exponent exceeds one: its smallest possible value is 1/2+b>1. Thus those ideal sums converge. The finite divisor products are bounded by (NQ)^eta for every eta>0, with NQ polynomially bounded. All moving core exclusions remain polynomially bounded by physical support. Choose preliminary losses and eta in terms of the requested final epsilon, then square. This proves (3.2).

The argument never chooses a second-moment index after a convolution shortening. A choice depending on the already frozen q_i is permitted, because (3.2) is separately proved for each of the finitely many indices. QED.

## 4. Disjoint cross matchings in every fixed even moment

For identical fixed tests, let the one-sided coefficient be

\[
z_\Theta(\mathbf n;u)
=\Theta(\mathbf n)\prod_{i=1}^k
\mu_K(n_i)\eta_u(n_i)W(Nn_i/D).
\]

Fix m disjoint cross edges, relabeled as (n_i,m_i), 1<=i<=m, and impose N(n_i,m_i)>=T. Let G_m^Theta(T) be the literal complete smooth signed covariance with those constraints and coefficients z_Theta(n;u) conjugate(z_Theta(m;u)). There are no other cross conditions. A different fixed pairing can be handled by relabeling the right tests and selector and applying Cauchy–Schwarz to the resulting two polynomials.

### Theorem 4.1

For every fixed k>=2, 1<=T<=D and 1<=R<=D with T=D/R,

\[
\boxed{
|\mathcal G_m^\Theta(D/R)|
\ll_\epsilon
H D^{k+a(k-1-m)+\epsilon}R^{am},
\qquad 0\le m\le k-1.
}
\tag{4.1}
\]

A full k-edge matching satisfies

\[
\boxed{
|\mathcal G_k^\Theta(D/R)|
\ll_\epsilon HD^{k+\epsilon}R^{a(k-1)}.
}
\tag{4.2}
\]

The threshold may be replaced by a fixed comparable multiple without changing exponents. The full matching has the same upper bound as k-1 edges. All quantities are actual signed moment sectors, with the original row zeros and permitted one-sided selectors retained.

**Proof.** For each prescribed edge put c_i=(n_i,m_i). Remove the residual mutual coprimality on that edge using a separate label e_i, exactly as in Lemma 2.1. Set q_i=c_i e_i for i<=m and q_i=1 otherwise. No coprimality is required between labels belonging to different edges.

The exact identity is

\[
\begin{aligned}
\mathcal G_m^\Theta(T)
=\sum_{\substack{Nc_i\ge T\ (i\le m)\\
c_i,e_i\ {\rm squarefree},\ (c_i,e_i)=1,\ (c_ie_i,S)=1}}
\left(\prod_{i\le m}\mu_K(e_i)\right)
\sum_u\Phi(u/\sqrt H)
{\bf1}_{(u,\prod_{i\le m}q_i)=1}
|F_{\mathbf q,\Theta}(u)|^2.
\end{aligned}
\tag{4.3}
\]

The label conditions in this sum apply separately to each prescribed edge. Their original support conditions are implicit in F and make the identity finite. Shared primes between different q_i survive literally in F and in its one-sided selector. The scalar characters at each common q_i cancel between the two sides to their nonunit-zero mask. No division occurs.

Suppose m<=k-1. Choose the second-moment index j among the unmatched coordinates. Then q_j=1, and (3.3) bounds the row square by

\[
D^\epsilon H D^{1+2b(k-1)}\prod_{i\le m}(Nq_i)^{-2b}.
\]

For each q_i the number of decompositions q_i=c_i e_i is divisor-bounded. Since Nc_i>=T implies Nq_i>=T, elementary ideal counting gives

\[
\sum_{Nq\ge T}(Nq)^{-2b}\ll_b T^{1-2b}.
\]

Consequently the absolute majorant is

\[
D^\epsilon H D^{1+2b(k-1)}T^{-am},
\]

which is (4.1). The case m=0 follows directly from Lemma 3.1 with every q_i=1.

For m=k, choose j with Nq_j=min_i Nq_i. The finite number of choices only costs k. Sum (3.3) in increasing order of this minimum, writing t=Nq_j. All other q_i have norm at least t, so

\[
\begin{aligned}
\sum_{\substack{Nq_i\ge T}}
\frac1{Nq_j}\prod_{i\ne j}(Nq_i)^{-2b}
&\ll_k\sum_{Nq\ge T}\frac1{Nq}
\left(\sum_{Nr\ge Nq}(Nr)^{-2b}\right)^{k-1}\\
&\ll_{k,b}\sum_{Nq\ge T}(Nq)^{-1-a(k-1)}\\
&\ll_{k,b}T^{-a(k-1)}.
\end{aligned}
\tag{4.4}
\]

Fixed-order divisor losses are absorbed into D^epsilon before applying these tails, or equivalently with a preliminary positive loss smaller than a(k-1). Multiplying by H D^{1+2b(k-1)} proves (4.2). QED.

For k=2, this rederives #923's single-edge theorem and proves the equally strong two-edge matching intersection, with no disjoint-event or conductor-size hypothesis. For k=3, two specified near cross matches have the diagonal-scale bound HD^{3+epsilon} when R is any chosen subpower function. For general fixed k, k-1 matches suffice for the same conclusion at HD^{k+epsilon}.

The theorem does not automatically control a union over different matchings: additional intersections can have cycles and must be treated. The fourth-moment case is completed next rather than assuming such monotonicity for signed sums.

## 5. The fourth moment as a four-edge graph

Take k=2 and the exact within-side selector

\[
N(n_1,n_2)<C,\qquad N(m_1,m_2)<C,
\qquad C\ge1.
\tag{5.1}
\]

For each cross edge (i,j), let E_ij be the condition N(n_i,m_j)>=T. The signed covariance for any subset of edges retains (5.1). There are four kinds of nonempty edge intersections:

- One edge.
- Two edges: a disjoint matching or a two-edge star.
- Three edges: a path through all four vertices.
- Four edges: the complete four-cycle.

Theorem 4.1 handles one edge and the two-edge matching. The following lemmas handle the remaining shapes while keeping their extra selectors inside exact native polynomials.

### Lemma 5.1. A star intersection

For any star consisting of two cross edges, its complete smooth signed contribution satisfies

\[
\boxed{
|\mathcal S_{\rm star}(C,D/R)|
\ll_\epsilon H D^{3/2+\epsilon}R^{b+1/2}.
}
\tag{5.2}
\]

**Proof.** By symmetry take center n=n_1 and edges (n,m_1),(n,m_2). The remaining left factor is

\[
B_{n,C}(u)=\sum_{N(l,n)<C}
\mu_K(l)\eta_u(l)W(Nl/D),
\qquad \|B_{n,C}\|_{\Phi,H}\ll D^\epsilon\sqrt{HD},
\tag{5.3}
\]

by #923, Lemma 2.1, or its exact divisor expansion and (NM2).

On the opposite side define the actual polynomial

\[
L_{n;C,T}(u)=
\sum_{\substack{N(m_1,n),N(m_2,n)\ge T\\N(m_1,m_2)<C}}
\prod_{i=1}^2\mu_K(m_i)\eta_u(m_i)W(Nm_i/D).
\tag{5.4}
\]

Set d_i=(m_i,n)|n, m_i=d_i x_i, (x_i,n)=1. Every retained divisor has Nd_i>=T, so its scale X_i=D/Nd_i is at most R. The within-side gcd is exactly (d_1,d_2)(x_1,x_2). Put c=(x_1,x_2) and separate the two coprime residual factors. The resulting two-factor core has scales X_1/Nc and X_2/Nc, mask nc, and exact scalar character factors of modulus at most one. Its norm is at most

\[
D^\epsilon\sqrt H\,
\max(X_1,X_2)^{1/2}\min(X_1,X_2)^b
(Nc)^{-b-1/2}.
\]

The c-sum converges because b+1/2>1. The d_i are divisors of the frozen n and cost only D^epsilon. The upper cutoff on N((d_1,d_2)c) is removed only from this positive norm majorant. Thus

\[
\|L_{n;C,T}\|_{\Phi,H}
\ll D^\epsilon\sqrt H\,R^{b+1/2}.
\tag{5.5}
\]

The star sector is exactly

\[
\sum_n\mu_K(n)\nu(n)W(Nn/D)
\sum_u\Phi(u/\sqrt H)\chi_n(u)
B_{n,C}(u)\overline{L_{n;C,T}(u)}.
\]

The fixed coefficient and row multiplier are bounded. Apply Cauchy–Schwarz in the complete row norm, use (5.3)–(5.5), and sum over O(D) possible center ideals. This gives (5.2). No hard conductor selector is inserted into either native polynomial. QED.

### Lemma 5.2. Paths and the four-cycle

Every three-edge path and the full four-edge intersection satisfy

\[
\boxed{
|\mathcal S_{\rm path}(C,D/R)|,
|\mathcal S_{\rm cycle}(C,D/R)|
\ll_\epsilon H D^{1+\epsilon}R^2.
}
\tag{5.6}
\]

**Proof.** Use the path n_1—m_1—n_2—m_2; the possible fourth edge joins n_1 to m_2. Freeze the middle pair v=n_2, w=m_1, which satisfies N(v,w)>=T. There are O_epsilon(D^{1+epsilon}R) possible ordered pairs. Indeed, for fixed v, the exact divisor c=(v,w)|v has Nc>=T, and w=c z has at most O(D/Nc)<=O(R) choices for each of the subpower number of divisors c.

Let Q=lcm(v,w). Split the endpoints exactly as

\[
n_1=d x,\quad d=(n_1,Q)|Q,\quad(x,Q)=1,
\qquad
m_2=e y,\quad e=(m_2,Q)|Q,\quad(y,Q)=1.
\tag{5.7}
\]

The two endpoint-to-middle edge conditions, and both original within-side conditions, are now entirely conditions on the frozen divisors d,e:

\[
N(d,w)\ge T,\quad N(e,v)\ge T,
\quad N(d,v)<C,\quad N(e,w)<C.
\tag{5.8}
\]

In particular Nd,Ne>=T, so X=D/Nd and Y=D/Ne are at most R. The two endpoint polynomials have their original smooth tests at these smaller scales and exclusion Q.

If the fourth edge is absent, their row covariance is bounded by (NM2) and Cauchy–Schwarz, with a row multiplier of modulus at most one from v,w,d,e. If the fourth edge is present, its exact remaining condition is

\[
N(d,e)\,N(x,y)\ge T.
\tag{5.9}
\]

Apply Lemma 2.1 with f(c)=1_{N(d,e)Nc>=T}. In both cases the full endpoint covariance is O_epsilon(D^epsilon H sqrt(XY))<=O_epsilon(D^epsilon HR). All fixed phase multipliers, including their zeros, are contractions. There are only a subpower number of pairs d,e dividing Q.

Multiply HR by the O_epsilon(D^{1+epsilon}R) middle-pair count. This proves (5.6). In particular, the fourth-edge selector is not dropped by appealing to positivity of a signed covariance: it is handled by its exact gcd identity. QED.

## 6. The complete fourth-moment union, with no disjointness condition

Let U_C(T) be the complete smooth signed contribution satisfying the within-side restrictions (5.1) and at least one of the four conditions E_ij. This selector is invariant under exchanging the two sides, so U_C(T) is real.

### Theorem 6.1

For every C>=1 and 1<=R<=D,

\[
\boxed{
|\mathcal U_C(D/R)|
\ll_\epsilon D^\epsilon H
\left[D^2R^a+D^{3/2}R^{b+1/2}+DR^2\right].
}
\tag{6.1}
\]

In particular,

\[
\boxed{
1\le R\le D^{1/(3-2b)}
\quad\Longrightarrow\quad
|\mathcal U_C(D/R)|
\ll_\epsilon HD^{2+\epsilon}R^{2b-1}.
}
\tag{6.2}
\]

**Proof.** Apply the exact finite inclusion–exclusion formula for the union of four events. There are four single edges, two matching pairs, four star pairs, four three-edge paths, and one four-cycle. Theorem 4.1 gives the first term in (6.1) for the singles and matching pairs. Lemma 5.1 gives the second term for stars; Lemma 5.2 gives the third for paths and the cycle. There are finitely many terms, and every sign was retained up to this exact identity.

To obtain (6.2), compare each latter term with the first. Their ratios are

\[
D^{-1/2}R^{3/2-b},\qquad D^{-1}R^{3-2b}.
\]

The former is the square root of the latter. Both are at most one exactly on the stated range. QED.

At b=7/8, the theorem gives

\[
\boxed{
R\le D^{4/5}
\quad\Longrightarrow\quad
|\mathcal U_C(D/R)|\ll HD^{2+\epsilon}R^{3/4}.
}
\tag{6.3}
\]

The earlier result required r<(1+h)/14 for R=D^r at its chosen C. Here no relation between C, H, and T is used beyond the native analytic inputs. For example, R=D^{1/4} now gives the actual bound HD^{2+3/16+epsilon}; the earlier disjointness range near h=1 did not cover that threshold. For R=D^{1/2}, the new bound is HD^{2+3/8+epsilon}. At the largest displayed endpoint it is HD^{2+3/5+epsilon}.

At b=1, the only nonclassical analytic premise is (NM2), and the sharper union cost HD^{2+epsilon}R holds throughout 1<=R<=D. The pointwise estimate at this exponent is elementary.

## 7. Passing to the hard conductor domain and the existing remainder

Let the original full-tuple hard conditions be g_1!=1 and E=Ng_1 sqrt(Ng_2)>H, in the conventions of #914/#919. Their complement has positive absolute accounting O_epsilon(HD^{k+epsilon}) for each fixed even moment. This bound survives every additional tuple restriction.

First prove the complete signed estimates above; only then remove this controlled complement. Thus the same bounds hold in the hard region, with an additional O_epsilon(HD^{k+epsilon}) term. This is absorbed by the displayed right sides, which are at least the diagonal scale.

For the fourth moment with 1<h<=11/10 and C=D^{(6-h)/7}, subtract from #919's hard small-gcd remainder exactly the union U_C^hard(D/R). Its residual is the literal signed sum with

\[
\begin{gathered}
N(n_1,n_2),N(m_1,m_2)<D^{(6-h)/7},\\
g_1\ne1,\qquad Ng_1\sqrt{Ng_2}>D^h,\\
N(n_i,m_j)<D/R\quad\text{for every }i,j.
\end{gathered}
\tag{7.1}
\]

The proof now justifies this subtraction with cost R^a on the entire range R<=D^{1/(3-2b)}, not merely the old range in which the four removed events happened to be disjoint. In a polynomial choice R=D^r, the proved excess is ar. No assertion about the remaining signed average follows merely from having fewer tuples.

For a chosen subpower R(D), this is again diagonal-scale control. The main new fourth-moment content is the stronger polynomial range and the exact treatment of the formerly uncontrolled intersections. The all-order matching theorem independently controls additional fixed sectors of every higher moment, including sectors with only one unmatched long pair and a hard conductor.

## 8. What this does and does not resolve

The new covariance lemma shows that a residual gcd threshold between two native Möbius polynomials can be handled at their native diagonal covariance scale, even with an arbitrary bounded frozen gcd selector and a bounded row multiplier. This is the mechanism that closes the four-cycle intersection; estimating individual expanded terms would lose a factor of R there.

The all-order matching theorem gains one factor T^(2b-1) per matched cross edge until k-1 edges have been used. This is a genuine estimate for complete signed sectors, retaining arbitrary permitted one-sided incidence selectors. It supplies a general moment component without assuming the desired general moment itself.

The bounds still leave four mutually coprime long factors in the fourth moment, and the analogous nearly coprime balanced tuple sectors in higher moments. They do not prove M_4(D,D^h)<<D^{h+2+epsilon} for h down to one, do not establish the cofinal diagonal hierarchy, and do not yield the boundary 17/24 or a shrinking zero-height band. H here is an arithmetic row height, not a zeta-zero ordinate.

The smallest analytic premises on which these deductions depend are the fully uniform smaller-scale (NM2) and, for b<1, (PW). The new algebraic point most sensitive to a mistake is the fixed-prime endpoint decomposition (5.7)–(5.9), together with the cross-gcd inversion (2.2)/(4.3). Those are finite exact identities and are suitable for independent exhaustive diagnostics. Such diagnostics do not replace the convergence and uniformity arguments in the proofs above.
