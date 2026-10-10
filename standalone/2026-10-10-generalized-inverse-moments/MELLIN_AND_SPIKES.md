# A universal Mellin test, replicated moment spikes, and the exact all-moment target

**Status:** independent research contribution for review, 2026-10-10. The elementary propositions below are proved. No new arithmetic upper bound for a fourth or higher moment is proved.

**Scope:** the Möbius/sextic family of the October 5 manuscript over \(K=\mathbb Q(\sqrt{-3})\), with fixed finite-order Hecke character \(\nu\), fixed excluded-prime set \(S\), and \(0<h<6\). The fixed-field Hecke continuation, functional equation, prime-ideal theorem and sextic reciprocity are standard inputs. The final upper characterization also uses the explicitly stated standard uniform reciprocal lemma, whose complex-analytic argument is recalled.

**Exact sources:** the family and prime rows in OpenAI/math at `adc7f1241b42e322a6451854ab7e4b4c146bf78a`, `preprints/The-Quasi-Riemann-Hypothesis-October-5-2026/build/paper2.tex`, equations `eq:intro-family`, `eq:recip`, and `eq:prime-extract`; exact prime-removal recursion in GettysburgResearch/riemann PR #910 at `670a76c1a3a8f325c43c1755b1cfc24d313a3e3c`, `UPSTREAM_HEIGHT_AND_MOMENTS.md`, Proposition 7.2. Standard uniform analytic inputs are stated and proved in the imported September 30 `paper.tex`, lemmas `lem:hecke-strip-growth`, `lem:logarithmic-control`, and `lem:deleted-euler-factors`. None of the new deductions uses the claimed quasi-Riemann theorem as an arithmetic input.

**What was run:** direct source inspection and mathematical derivation. No numerical computation is required for these identities; no Lean formalization or full upstream validation was performed.

**Smallest remaining gap:** any new full-row arithmetic large-value or higher-moment upper bound beyond the imported second moment. The all-moment target is itself equivalent to GRH for the relevant twist family, as made precise below.

## 1. One explicit smooth test suffices

Write

\[
A_u(D;W)=\sum_{(n,S)=1}\mu_K(n)\nu(n)\chi_n(u)W(Nn/D),
\qquad \chi_n(u)=(u/n)_6,
\]

with the original zero extensions. The moment-to-zero argument does not require a separate test for each hypothetical zero. There exists a single nonnegative \(W_*\in C_c^\infty((1,2))\) whose Mellin transform is nonzero throughout \(\Re s>0\).

### Proposition 1.1. Explicit universal test

Set

\[
c=\frac{\log 2}{8},\qquad a_j=\frac{c}{j^2}\quad(j\ge1),
\qquad t_0=\frac{\log2}{2}.
\]

Let \(X_j\) be independent real random variables, uniform on \([-a_j,a_j]\). The sum \(X=\sum_{j\ge1}X_j\) converges absolutely because \(\sum_j a_j<\infty\). Its distribution has a nonnegative smooth density \(f\in C_c^\infty(\mathbb R)\). Define

\[
W_*(y)=f(\log y-t_0).
\]

Then \(W_*\in C_c^\infty((1,2))\), \(W_*\ge0\), \(W_*\not\equiv0\), and

\[
\boxed{\displaystyle
\widehat W_*(s)
=e^{t_0s}\prod_{j=1}^\infty\frac{\sinh(a_js)}{a_js}.}
\tag{1.1}
\]

The quotient is given its removable value \(1\) at zero. The product converges locally uniformly on \(\mathbb C\), and all its zeros lie on \(\Re s=0\). In particular, \(\widehat W_*(s)\ne0\) for every \(\Re s>0\).

**Proof.** The support of \(X\) is contained in \([-A,A]\), where

\[
A=\sum_j a_j=\frac{\pi^2\log2}{48}<\frac{\log2}{2}=t_0.
\]

Its characteristic function is the convergent product

\[
\varphi(t)=\prod_j\frac{\sin(a_jt)}{a_jt}.
\]

For sufficiently large \(|t|\), every \(1\le j\le\lfloor\sqrt{c|t|/2}\rfloor\) satisfies \(a_j|t|\ge2\), so the absolute value of that factor is at most \(1/2\); all other factors have absolute value at most one. Consequently

\[
|\varphi(t)|\le C e^{-c_1\sqrt{|t|}}
\]

for constants \(C,c_1>0\). Thus \(t^m\varphi(t)\in L^1(\mathbb R)\) for every integer \(m\ge0\). Fourier inversion gives a \(C^\infty\) density \(f\) on the whole line. It is nonnegative and supported in \([-A,A]\) because it is the density of the stated probability distribution. Hence \(W_*\) has compact support in \((1,2)\), including smoothness across its support endpoints.

Bounded convergence on the compact support gives, for every complex \(s\),

\[
\int f(t)e^{st}\,dt
=\mathbb E e^{sX}
=\prod_j\mathbb E e^{sX_j}
=\prod_j\frac{\sinh(a_js)}{a_js}.
\]

On every compact \(s\)-set the \(j\)-th factor is \(1+O(a_j^2|s|^2)\), and \(\sum_j a_j^2<\infty\); the product therefore converges locally uniformly. Every factor has its nonzero zeros at \(s=i\pi m/a_j\), \(m\in\mathbb Z\setminus\{0\}\). At a point off the imaginary axis no factor vanishes, and the summable deviations from one make their infinite product nonzero. Changing variables \(t=\log y-t_0\) proves (1.1). \(\square\)

This is an exact analytic test, not a finite numerical approximation to one. Its Mellin transform can be small at a large imaginary part; only nonvanishing is required in the all-scale identity-theorem argument. No quantitative lower bound in height is claimed.

### Corollary 1.2. A single-test cancellation criterion

For any fixed \(u\ne0\), suppose

\[
A_u(D;W_*)\ll_{u,\eta}D^{\alpha+\eta}
\quad\text{for every }\eta>0,
\]

where \(\alpha>0\). Then the primitive Hecke \(L\)-function induced by the coefficient character \(n\mapsto\nu(n)\chi_n(u)\) has no zero with real part greater than \(\alpha\).

**Proof.** Sextic reciprocity makes the coefficient character, away from the finitely many deleted primes, a finite-order Hecke character. If \(\psi_u\) denotes its primitive inducing character, then for \(\Re s>1\)

\[
\sum_{(n,S)=1}\frac{\mu_K(n)\nu(n)\chi_n(u)}{(Nn)^s}
=\frac{E_u(s)}{L_K(s,\psi_u)},
\tag{1.2}
\]

where \(E_u(s)\) is a finite product of reciprocal Euler factors. It is holomorphic and nonzero for \(\Re s>0\). The scale Mellin transform satisfies

\[
\int_0^\infty A_u(D;W_*)D^{-s}\frac{dD}{D}
=\widehat W_*(s)\frac{E_u(s)}{L_K(s,\psi_u)}.
\tag{1.3}
\]

The left side continues holomorphically to \(\Re s>\alpha\). Both factors in its numerator are nonzero at every hypothetical zero there. The identity theorem gives a contradiction. A possible pole of a principal \(L\)-function at \(s=1\) is removed by multiplication by \(s-1\); it creates no issue at a nontrivial zero. \(\square\)

## 2. Exact prime replication works for every fixed base row

Fix a nonzero row \(v\in\mathcal O_K\). Write \(A_v(D)=A_v(D;W_*)\). For a prime ideal \(p\notin S\), \(p\nmid v\), define

\[
B_{v,p}(x)=A_{vp^6}(x),\qquad c_v(p)=\nu(p)\chi_p(v).
\]

The original zero extension gives \(B_{v,p}\) by deleting the multiples of \(p\) from \(A_v\), and \(|c_v(p)|=1\). Exact separation of those multiples yields

\[
A_v(x)=B_{v,p}(x)-c_v(p)B_{v,p}(x/Np),
\tag{2.1}
\]

and therefore

\[
B_{v,p}(x)=\sum_{j\ge0}c_v(p)^jA_v(x/(Np)^j).
\tag{2.2}
\]

The sum is finite by the lower support cutoff. This is the original prime-removal argument with a fixed base row retained. No implied constant is allowed to depend on the moving prime.

For fixed \(v\), take primes

\[
Y/2<Np\le Y,\qquad
Y=(D^h/Nv)^{1/6}.
\tag{2.3}
\]

Their rows \(vp^6\) have norm at most \(D^h\), are distinct, and their number satisfies

\[
J_v(D)\asymp_v D^{h/6}/\log D.
\tag{2.4}
\]

Consequently the existing conditional extraction theorem improves the exponent simultaneously for *every fixed sextic twist of* \(\nu\), not only for the original principal row.

## 3. A zero forces replicated moment spikes

The following lower bound makes the obstruction to the desired upper bound concrete.

### Proposition 3.1. Record-scale lower bound

Suppose \(L_K(s,\psi_v)\) has a zero \(\rho\) with \(b=\Re\rho>0\). Fix an integer \(k\ge1\) and any \(0<\beta<b\). There is a sequence \(D_j\to\infty\) such that

\[
\frac{\displaystyle
\sum_{0<Nu\le D_j^h}|A_u(D_j;W_*)|^{2k}}
{\displaystyle D_j^{2k\beta+h/6}/\log D_j}
\longrightarrow\infty.
\tag{3.1}
\]

**Proof.** If \(A_v(D)=O(D^\beta)\), Corollary 1.2 (or the same Mellin argument without an epsilon loss) would exclude the zero \(\rho\). Thus \(F(D)=|A_v(D)|/D^\beta\) is unbounded. The function \(A_v\) is continuous and vanishes below a positive scale. There are therefore record scales \(D_j\to\infty\), with \(F(D_j)\to\infty\), for which

\[
|A_v(x)|\le F(D_j)x^\beta\quad(0<x\le D_j).
\]

For every prime in (2.3), equation (2.2) gives

\[
|B_{v,p}(D_j)-A_v(D_j)|
\le |A_v(D_j)|\sum_{m\ge1}(Np)^{-m\beta}
\le\frac{|A_v(D_j)|}{(Y/2)^\beta-1}.
\]

Thus every one of the \(J_v(D_j)\) prime replicas satisfies

\[
|A_{vp^6}(D_j)|\ge(1-o(1))|A_v(D_j)|.
\]

Summing these nonnegative contributions to the moment proves

\[
\sum_{0<Nu\le D_j^h}|A_u(D_j)|^{2k}
\ge(1-o(1))J_v(D_j)|A_v(D_j)|^{2k}.
\]

After division by the denominator in (3.1), the right side is bounded below by a positive fixed multiple of \(F(D_j)^{2k}\to\infty\). \(\square\)

This proof does not expand the moment and does not lose cancellation through an absolute bound on off-diagonal terms. It shows that an off-critical zero would require actual large values in at least \(D^{h/6+o(1)}\) allowed rows on an unbounded sequence of scales.

### Corollary 3.2. Moments with a controlled excess

Suppose, for a fixed \(k\), a real \(e_k\ge0\), and every \(\epsilon>0\),

\[
\sum_{0<Nu\le D^h}|A_u(D;W_*)|^{2k}
\ll_{k,\epsilon}D^{k+h+e_k+\epsilon}.
\tag{3.2}
\]

Then every primitive twist \(\psi_v\), for every fixed \(v\ne0\), has no nontrivial zero to the right of

\[
\boxed{\displaystyle
\frac12+\frac{5h}{12k}+\frac{e_k}{2k}.}
\tag{3.3}
\]

**Proof.** A zero further right permits choosing \(\beta\) strictly between its asserted boundary and its real part. Then \(2k\beta+h/6>k+h+e_k\), so (3.1) contradicts (3.2) with a sufficiently small epsilon. \(\square\)

The same conclusion follows from exact prime-removal induction, but (3.1) also describes the moment spikes that a counterexample would force.

In particular, the desired exact diagonal power \(e_k=0\) is stronger than is necessary for an all-moment proof. An unbounded sequence \(k_j\to\infty\) with \(e_{k_j}/k_j\to0\) suffices. No constants uniform in \(k_j\) are needed. Nor is every integer moment required. The row exponent may vary with \(j\) if \(h_j/k_j\to0\), provided the replication and moment statement are available at each fixed \(h_j>0\).

For \(h=1+\theta\), \(e_k=0\), and arbitrarily small fixed \(\theta>0\), (3.3) returns \(11/12,17/24,23/36,\ldots\). These remain conditional consequences, not new upper bounds.

## 4. A strictly weaker large-value target

The full moment is more than the extraction needs. Put \(\mathcal U_D=\{u:0<Nu\le D^h\}\).

### Proposition 4.1. One good replica is enough

Fix \(\alpha>0\) and \(C_0>0\). Suppose, for all sufficiently large \(D\),

\[
\#\{u\in\mathcal U_D:|A_u(D;W_*)|>C_0D^\alpha\}
<J_v(D),
\tag{4.1}
\]

where \(J_v(D)\) is the exact prime-replica count in (2.3). Then

\[
A_v(D;W_*)\ll_{v,\alpha,C_0}D^\alpha.
\]

**Proof.** At least one of the \(J_v(D)\) distinct prime replicas has absolute value at most \(C_0D^\alpha\). For its prime \(p\), (2.2) rearranges to

\[
A_v(D)=B_{v,p}(D)-\sum_{j\ge1}c_v(p)^jA_v(D/(Np)^j).
\]

Under the inductive bound \(|A_v(x)|\le Cx^\alpha\) at smaller scales, the second term is at most

\[
C D^\alpha\big((Y/2)^\alpha-1\big)^{-1}.
\]

For sufficiently large \(D\), the factor in parentheses is at least \(2\), and the scale arguments are below \(D/2\). Choose \(C\ge2C_0\) and large enough on the fixed starting interval. Dyadic induction closes. \(\square\)

For all fixed \(v\), the cleaner sufficient tail condition is

\[
\#\{u\in\mathcal U_D:|A_u(D;W_*)|>C_0D^\alpha\}
=o(D^{h/6}/\log D).
\tag{4.2}
\]

This condition allows arbitrarily large moments on a smaller exceptional set. It is therefore genuinely weaker than a prescribed full moment estimate. It is still an unproved arithmetic input. Applying Markov's inequality to the proposed \(2k\)-th moment yields (4.2) only when \(\alpha>1/2+5h/(12k)\), so this reformulation alone improves no exponent.

## 5. The high-moment growth rate recovers the rightmost zero

The lower statement below is unconditional relative to standard Hecke theory. The upper statement is derived from a standard uniform analytic lemma; its hypotheses are part of the proof and cannot be replaced by bounds for each conductor with uncontrolled constants.

Let

\[
B_\nu=\sup\{\Re\rho: L_K(\rho,\psi_v)=0,
\ 0<\Re\rho<1,\ v\in\mathcal O_K\setminus\{0\}\}.
\]

Thus \(B_\nu\) is the rightmost-zero supremum across the sextic twist family of the fixed \(\nu\), including primitive induction and the original fixed bad-prime convention. Standard functional equations give \(1/2\le B_\nu\le1\). Define

\[
\lambda_k=\limsup_{D\to\infty}
\frac{\log M_{2k}(D)}{\log D},\qquad
M_{2k}(D)=\sum_{0<Nu\le D^h}|A_u(D;W_*)|^{2k},
\]

with \(\log0=-\infty\).

### Standard uniform reciprocal lemma used for the upper bound

For finite-order Hecke characters over this fixed field, assume a subfamily has no zero in \(\Re s>b\), where \(1/2\le b<1\). Then for every fixed \(\delta,\eta>0\),

\[
\frac1{|L_K(\sigma+it,\psi)|}
\ll_{b,\delta,\eta}
\{2Q_\psi(3+|t|)^2\}^{\eta}
\qquad(\sigma\ge b+\delta),
\tag{5.1}
\]

uniformly over the primitive characters in the subfamily. For the principal character, use the removable regularization \((s-1)\zeta_K(s)/(s+1)\) and then pass its reciprocal estimate to \(1/\zeta_K(s)\).

This is the exact type of statement in the imported September 30 `lem:logarithmic-control`; it does **not** assume or prove a new zero-free line. To recall the mechanism, center disks at \(2+it\), keep the outer disk a fixed positive distance right of \(b\), and use the uniform polynomial strip bound to obtain \(\Re\log L\ll\log(2Q(3+|t|)^2)\). Borel--Carathéodory bounds the modulus of this logarithm on a smaller disk. On a disk of radius less than \(1\), Euler convergence bounds it absolutely. Three-circles interpolation between those two disks bounds it by \(C(\log(2Q(3+|t|)^2))^r\) with a fixed \(r<1\) on the required inner disk. Exponentiating both signs gives (5.1). Every shrinkage is fixed by the buffer \(\delta\), so constants are uniform in \(Q,t\). Euler convergence handles the remaining right half-plane.

Sextic reciprocity supplies a fixed polynomial conductor bound

\[
Q_{\psi_u}\ll_{\nu,S}(1+Nu)^C
\tag{5.2}
\]

for an absolute finite \(C\). One does not need the optimal value of \(C\). The support of the additional deleted Euler factors divides a fixed ideal times the radical of \(u\). For every fixed \(\sigma_0,\eta>0\),

\[
|E_u(\sigma+it)|\ll_{\nu,S,\sigma_0,\eta}(1+Nu)^\eta
\quad(\sigma\ge\sigma_0).
\tag{5.3}
\]

Indeed, each reciprocal deleted factor is bounded by \((1-(Np)^{-\sigma_0})^{-1}\); the logarithm of this factor is at most \(\eta\log Np\) at all sufficiently large primes, and the finitely many smaller primes cost a constant. This is the elementary deleted-factor argument of the source. For (5.2), the sextic Kummer character is ramified only at primes dividing \(6u\); at primes away from \(6\), its conductor is supported on the radical of \(u\). At each fixed prime above \(6\), the local quotient \(K_p^\times/(K_p^\times)^6\) is finite; equivalently one reduces the valuation modulo \(6\) and the unit to one of finitely many local classes. Thus the ramified local conductor cost is bounded independently of \(u\). The fixed character \(\nu\) changes only the constant and fixed modulus. Alternatively any polynomial bound from the discriminant of the radical extension suffices.

### Proposition 5.1. Moment-growth characterization

With these standard analytic inputs,

\[
\boxed{\displaystyle
2kB_\nu+\frac h6\ \le\ \lambda_k\ \le\ 2kB_\nu+h.}
\tag{5.4}
\]

Consequently

\[
\boxed{\displaystyle
\lim_{k\to\infty}\frac{\lambda_k}{2k}=B_\nu.}
\tag{5.5}
\]

**Lower bound.** For every zero of every fixed twist, Proposition 3.1 gives \(\lambda_k\ge2k\Re\rho+h/6\), by letting \(\beta\uparrow\Re\rho\). Taking the supremum over the zeros and fixed twists proves the lower bound. No uniform choice of \(v\) or record scales is required.

**Upper bound for \(B_\nu<1\).** Fix \(\epsilon>0\). The entire twist family is zero-free in \(\Re s>B_\nu\) by definition. Shift the Mellin inversion for \(A_u(D;W_*)\) to a line \(\sigma=B_\nu+\delta\), with sufficiently small fixed \(\delta>0\). Equations (5.1)--(5.3), the polynomial conductor bound, \(Nu\le D^h\), and the rapid vertical decay of the fixed smooth Mellin transform show, after taking the reciprocal-bound loss sufficiently small, that

\[
|A_u(D;W_*)|\ll_{\nu,S,h,\epsilon}D^{B_\nu+\epsilon}
\qquad(0<Nu\le D^h).
\tag{5.6}
\]

The contour crosses no pole: poles of \(1/L\) are zeros of \(L\), all to its left, and a pole of a principal \(L\)-function is a zero of its reciprocal. The same uniform analytic estimates control the horizontal contour tails. There are \(O(D^h)\) lattice rows. Therefore \(M_{2k}(D)\ll D^{2kB_\nu+h+2k\epsilon}\), and letting \(\epsilon\downarrow0\) proves the upper bound.

**Upper bound for \(B_\nu=1\).** The elementary ideal count gives \(|A_u(D;W_*)|\ll D\), uniformly in \(u\), hence \(M_{2k}(D)\ll D^{2k+h}\). This handles the endpoint without invoking a reciprocal lemma with a nonexistent right-hand buffer below one.

Dividing (5.4) by \(2k\) proves (5.5). \(\square\)

### Exact logical consequence

For the fixed twist family, the following are equivalent:

1. Every \(L_K(s,\psi_v)\) satisfies GRH.
2. For every fixed integer \(k\ge1\) and every \(\epsilon>0\), the single-test bound \(M_{2k}(D)\ll_{k,\epsilon}D^{k+h+\epsilon}\) holds.
3. Along some unbounded sequence \(k_j\), the single-test bounds \(M_{2k_j}(D)\ll_{k_j,\epsilon}D^{k_j+h+e_j+\epsilon}\) hold with \(e_j/k_j\to0\).
4. The high-moment growth rate in (5.5) is \(1/2\).

The implication from GRH to \(2\) is the upper proof at \(B_\nu=1/2\). The implications from \(2\) or \(3\) to GRH are Corollary 3.2, with the functional equation handling the left half of the critical strip. The characterization (5.5) gives \(4\). With the moment assertion for every fixed finite-order \(\nu\), this is GRH for all finite-order Hecke \(L\)-functions over \(K\), and it entails Dirichlet GRH by the standard quadratic base-change identity used in the upstream source.

This equivalence is a scope clarification, not a proof of an open moment estimate. The difficult part is the new uniform arithmetic upper bound. Arbitrary deterioration of constants with \(k\) is permissible, because a hypothetical fixed off-critical zero determines a single sufficiently large finite \(k\) before \(D\to\infty\).

## 6. What alternate principal amplification can and cannot accomplish

Replacing prime sixth powers by all sixth powers supplies at most \(O(D^{h/6})\) rows, while the prime subset already supplies \(D^{h/6+o(1)}\). Thus this replacement can remove a logarithm but cannot improve the \(5h/(12k)\) power in a deduction using only the same total moment budget. More generally, if \(q(n)=\chi_n(u)\) is identically principal on ideals outside finitely many primes, sextic Kummer theory identifies \(u\) with a sixth-power class. Distinct coprimality masks within that class do not create more than \(H^{1/6+o(1)}\) actual rows of norm at most \(H\).

A weighted amplifier supported on \(J\) exact principal replicas cannot beat this power through Hölder alone: under a moment budget \(M\), its best possible generic bound is of order \((M/J)^{1/(2k)}\). Weights or multiplicative identities can improve that conclusion only by proving additional arithmetic information about the selected rows. The large-value target (4.2) records precisely one sufficient form of such information.

No argument here proves the fourth moment, \(17/24\), or the generalized \(2k\)-th moment. The concrete progress is an explicit universal test, extension of exact extraction to every fixed twist, a replicated-spike lower theorem, and an exact characterization of the asymptotic moment exponent. These eliminate unnecessary test and moment quantifiers while locating the required arithmetic improvement.
