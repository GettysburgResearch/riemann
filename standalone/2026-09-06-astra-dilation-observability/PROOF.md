# Dilation observability, arithmetic support, and the actual Schur gain

**Status:** proposed complete component proofs; independent review required.
**RH is not proved.** DO26.1–DO26.9 below have proofs. The uniform estimate
in DO26.G is a proposed sufficient target, not a theorem.

The space, the integer Nyman–Beurling criterion, and Vasyunin's dual system
are classical. This packet contributes a reconstructed connection between
local observation of a projection residual, finite dilation leakage,
positive Schur improvement, and explicit arithmetic-support obstructions.
No external novelty or priority is claimed. See [SOURCES.md](SOURCES.md).
All inner products in the projection arguments are real; complexification
is used only for Mellin transforms. No repository analytic gate is assumed.

## 1. The literal discrete space

Let

\[
\mathcal H=\left\{f:\mathbb N_{\ge1}\to\mathbb R:
 \|f\|^2=\sum_{n\ge1}\frac{f(n)^2}{n(n+1)}<\infty\right\}.
\]

Set \(f(0)=0\). Identify \(f\) with the step function equal to \(f(n)\)
on \([n,n+1)\), and zero on \((0,1)\). This is an isometry into
\(L^2((0,\infty),dt/t^2)\), since
\(\int_n^{n+1}t^{-2}dt=1/[n(n+1)]\). Evaluation on the first cell is
continuous: \(|f(1)|\le\sqrt2\|f\|\).

Define the fixed target and dictionary

\[
\chi(n)=1,\qquad h_k(n)=\{n/k\}\quad(k\ge2),\qquad h_1=0.
\]

As continuous step functions,
\(h_k(t)=\{t/k\}-\{t\}/k\); the second term must not be omitted.
In particular \(\|\chi\|^2=1\). Write

\[
\mathcal B_N=\operatorname{span}(h_2,\ldots,h_N),\quad
\mathcal B=\overline{\bigcup_{N\ge2}\mathcal B_N}.
\]

Let \(P_N,P\) be the orthogonal projections onto these spaces, and set

\[
g_N=P_N\chi,\quad r_N=\chi-g_N,\quad\delta_N=\|r_N\|^2,
\qquad g=P\chi,\quad r=\chi-g,\quad\delta=\|r\|^2.
\]

Increasing-subspace projection convergence gives
\(g_N\to g\), \(r_N\to r\), and \(\delta_N\downarrow\delta\).
For completeness, if \(M\ge N\), orthogonality gives
\(\|g_M-g_N\|^2=\|g_M\|^2-\|g_N\|^2\). Thus \(g_N\) is Cauchy;
its limit lies in \(\mathcal B\), and the limiting residual is orthogonal
to every generator, which identifies the limit as \(P\chi\).

The **imported classical theorem** is

\[
\boxed{\chi\in\mathcal B\quad\Longleftrightarrow\quad\mathrm{RH}.}
\tag{NB}
\]

This is the integer/step-space form of Báez-Duarte's strengthening of the
Nyman–Beurling criterion (Balazard, Proposition 10). Only the reverse
implication in (NB) is needed as a deep import here: the implication
\(\delta=0\Rightarrow\mathrm{RH}\) is also proved directly in §7.

## 2. DO26.1 — exact dilation and invariant closure

For an integer \(m\ge2\), define

\[
(D_m f)(n)=f(\lfloor n/m\rfloor).
\]

Then

\[
\|D_m f\|^2=\frac1m\|f\|^2,
\qquad
D_mh_k=h_{mk}-\frac1k h_m.\tag{1}
\]

**Proof.** Group the norm sum into \(mj\le n<m(j+1)\). The weight sum is
\(1/(mj)-1/[m(j+1)]=1/[m j(j+1)]\) for \(j\ge1\); the \(j=0\)
block contributes zero. For the generator identity, put
\(n=m\lfloor n/m\rfloor+(n\bmod m)\) and use
\(\lfloor\lfloor n/m\rfloor/k\rfloor=\lfloor n/(mk)\rfloor\).
Expanding both fractional parts gives (1).

Consequently \(D_m\mathcal B_N\subset\mathcal B_{mN}\) and
\(D_m\mathcal B\subset\mathcal B\). Continuity of \(D_m\) proves the
second inclusion after closure. Notice that the finite inclusion is **not**
\(D_m\mathcal B_N\subset\mathcal B_N\).

More generally, the closed span \(\mathcal B_S\) of \(h_k\), \(k\in S\),
is invariant under \(D_m\) whenever \(m\in S\) and \(mk\in S\) for every
\(k\in S\). No zeta-zero assumption enters. ∎

## 3. DO26.2 — local observation controls the limiting residual

Let \(V\subset\mathcal H\) be any closed real subspace invariant under
\(D_m\), let \(g=P_V\chi\), \(r=\chi-g\), and \(\delta=\|r\|^2\).
Define

\[
Q_m(r)=\sum_{n=1}^{m-1}\frac{r(n)}{n(n+1)}.
\]

Then

\[
Q_m(r)=\delta-\langle r,D_mr\rangle,\qquad
(1-m^{-1/2})\delta\le Q_m(r)\le(1+m^{-1/2})\delta.
\tag{2}
\]

**Proof.** Since \(r\perp V\), \(\langle r,\chi\rangle=\delta\).
Invariance gives \(D_mg\in V\), so
\(\langle r,D_m\chi\rangle=\langle r,D_mr\rangle\).
But \(\chi-D_m\chi\) is exactly the indicator of cells \(1,\ldots,m-1\).
This proves the equality. Cauchy–Schwarz and (1) give
\(|\langle r,D_mr\rangle|\le\delta/\sqrt m\). ∎

For \(m=2\), putting \(a=r(1)=1-g(1)\), (2) becomes

\[
\boxed{(2-\sqrt2)\delta\le a\le(2+\sqrt2)\delta.}\tag{3}
\]

Thus for the **limiting orthogonal projection onto the full dictionary**,

\[
\mathrm{RH}
\quad\Longleftrightarrow\quad g(1)=1
\quad\Longleftrightarrow\quad
\lim_{N\to\infty}\sum_{k=2}^N\frac{c_{k,N}}k=1,
\qquad g_N=\sum_{k=2}^N c_{k,N}h_k.\tag{4}
\]

The limit in (4) exists unconditionally because first-cell evaluation is
continuous. Its value is Balazard's \(\nu_0(1)\). Formula (3), not a
finite observation, is the reason that this single coordinate is enough.
In particular \(g(1)\le1\) unconditionally. This does **not** say
\(g_N(1)\le1\), nor prove that the limit is 1.

An equivalent qualitative target is
\(\limsup_{N\to\infty}g_N(1)\ge1\). Proving arbitrarily late overshoots
would suffice, but no such cofinal theorem is proved in this packet.

## 4. DO26.3 — the finite-stage leakage identity

Fix \(N,m\ge2\), and put

\[
\Delta_{m,N}=\delta_N-\delta_{mN}
 =\|g_{mN}-g_N\|^2,\quad
L_{m,N}=\langle r_N,D_mg_N\rangle.
\]

Then

\[
Q_m(r_N)=\delta_N-\langle r_N,D_mr_N\rangle-L_{m,N},\tag{5}
\]

\[
L_{m,N}=\langle g_{mN}-g_N,D_mg_N\rangle,\quad
|L_{m,N}|\le
\sqrt{\frac{(1-\delta_N)\Delta_{m,N}}m},\tag{6}
\]

and hence

\[
\boxed{|Q_m(r_N)-\delta_N|
 \le\frac{\delta_N}{\sqrt m}
  +\sqrt{\frac{(1-\delta_N)\Delta_{m,N}}m}.}\tag{7}
\]

**Proof.** Expand \(D_m\chi=D_mg_N+D_mr_N\) to obtain (5).
The vector \(D_mg_N\) belongs to \(\mathcal B_{mN}\), so it is orthogonal
to \(r_{mN}\). Since
\(r_N=r_{mN}+g_{mN}-g_N\), the equality in (6) follows. Apply Cauchy–Schwarz,
(1), and \(\|g_N\|^2=1-\delta_N\). Apply (1) again to the remaining
correlation in (5) for (7). ∎

For each fixed \(m\), \(\Delta_{m,N}\to0\) as \(N\to\infty\),
**without assuming RH**: both endpoint distances converge to \(\delta\).
Therefore (7) tends to (2). Vanishing leakage is not vanishing residual.

## 5. DO26.4 — a quantitative non-stagnation alternative

Set \(v=(I-P_N)D_mg_N\) and \(\eta=\|v\|^2\). Then

\[
v\in\mathcal B_{mN}\cap\mathcal B_N^\perp,
\quad \eta\le\frac{1-\delta_N}m,
\quad\langle r_N,v\rangle=L_{m,N}.\tag{8}
\]

If \(\eta>0\), minimizing the norm of \(r_N-tv\) gives

\[
\Delta_{m,N}\ge\frac{L_{m,N}^2}{\eta}.\tag{9}
\]

If \(\eta=0\), then \(v=0\) and \(L_{m,N}=0\); (9) is not used.

**Proof.** The inclusions follow from (1) and the definition of \(P_N\).
Projection is contractive, which gives the bound on \(\eta\). Orthogonality
removes \(P_ND_mg_N\) from the pairing with \(r_N\). Finally
\(g_N+tv\in\mathcal B_{mN}\), so the optimal projection onto the latter
space does at least as well as the one-variable minimizer. ∎

Combining (5), the upper bound
\(\langle r_N,D_mr_N\rangle\le\delta_N/\sqrt m\), and (8)–(9) gives

\[
\boxed{
\Delta_{m,N}\ge\frac{m}{1-\delta_N}
\left[(1-m^{-1/2})\delta_N-Q_m(r_N)\right]_+^2.
}\tag{10}
\]

Here \([x]_+=\max(x,0)\). If the bracket is positive, \(L_{m,N}>0\),
so \(\eta>0\) and the preceding division is legal. If it is zero the
assertion is the already known \(\Delta_{m,N}\ge0\). Also
\(1-\delta_N>0\), since \(\langle\chi,h_2\rangle>0\).

In particular, if \(g_N(1)\ge1\), then

\[
\delta_N-\delta_{2N}\ge
 (3-2\sqrt2)\frac{\delta_N^2}{1-\delta_N}.\tag{11}
\]

This is an unconditional implication with a finite, checkable premise.
It is not an unconditional assertion that that premise holds cofinally.
It makes the obstruction precise: absent an appreciable Schur improvement,
a persistent residual must be visible already on the first cell.

## 6. DO26.5 — the literal positive Gram and Schur formulas

The Gram entries and target pairings are

\[
G_{jk}=\sum_{n\ge1}\frac{\{n/j\}\{n/k\}}{n(n+1)},
\qquad b_k=\langle\chi,h_k\rangle=\frac{\log k}{k}.\tag{12}
\]

The formula for \(b_k\) follows either by taking the removable value at
\(s=1\) in (18) below, or by telescoping the weighted fractional-part sum.
All sums in (12) are absolutely convergent. Every finite principal Gram
matrix is positive definite: a finite linear dependence among the \(h_k\)
is separated by the explicit dual vectors of §8. Thus

\[
c_N=G_N^{-1}b_N,\quad
\delta_N=1-b_N^TG_N^{-1}b_N,\quad
g_N(1)=\sum_{k=2}^N\frac{(c_N)_k}{k}.\tag{13}
\]

For every finite \(N\), \(0<\delta_N<1\). For strict positivity, all
finite linear combinations of the dictionary are periodic of period
\(\operatorname{lcm}(2,\ldots,N)\), and vanish on cells indexed by a
multiple of that period. They cannot equal \(\chi\) in \(\mathcal H\).

Partition \(G_{2N}\) into old indices \(2,\ldots,N\) and new indices
\(N+1,\ldots,2N\):

\[
G_{2N}=\begin{pmatrix}G_N&C\\ C^T&D\end{pmatrix},\qquad
S_N=D-C^TG_N^{-1}C,\quad z_N=b_{\rm new}-C^TG_N^{-1}b_N.
\]

Then \(S_N\) is positive definite, and

\[
\boxed{\delta_N-\delta_{2N}=z_N^TS_N^{-1}z_N.}\tag{14}
\]

**Proof.** Subtract the projection onto \(\mathcal B_N\) from each new
generator. Their Gram is \(S_N\); they are independent by independence of
the full dictionary. Their target pairings are \(z_N\). Projecting the
old residual onto their span gives (14). Equivalently, complete the square
in the quadratic objective for the block matrix. ∎

The one-dilation quantities are also explicitly finite Gram calculations.
With old indices \(i,k\in\{2,\ldots,N\}\), put

\[
H^{(m)}_{ik}=G_{i,mk}-G_{i,m}/k,\quad d=H^{(m)}c_N.
\]

Whenever the indicated Gram entries have been acquired,

\[
L_{m,N}=\frac{1-\delta_N}{m}-c_N^TH^{(m)}c_N,
\qquad
\eta=\frac{1-\delta_N}{m}-d^TG_N^{-1}d.\tag{15}
\]

Indeed \(d_i=\langle h_i,D_mg_N\rangle\), and
\(\langle\chi,D_mg_N\rangle=\langle\chi,g_N\rangle/m\), by the same
weight grouping as (1). Projection onto the old basis yields the expression
for \(\eta\). No inverse on an infinite-dimensional space is used.

### DO26.6 — the exact cumulative-gain criterion

Fix \(N_0\ge2\) before considering any hypothetical zero, let
\(N_j=2^jN_0\), and set

\[
\kappa_j=\frac{z_{N_j}^TS_{N_j}^{-1}z_{N_j}}{\delta_{N_j}}\in[0,1).
\]

Then

\[
\delta_{N_J}=\delta_{N_0}\prod_{j<J}(1-\kappa_j),\qquad
\boxed{\mathrm{RH}\Longleftrightarrow\sum_{j\ge0}\kappa_j=\infty.}\tag{16}
\]

The product identity is (14). If \(\sum\kappa_j=\infty\), use
\(1-x\le e^{-x}\) to get zero limit. If the sum is finite, eventually
\(\kappa_j\le1/2\), and \(-\log(1-\kappa_j)\le2\kappa_j\), so the
product has positive limit. Combine this with (NB).

**DO26.G — open proposed sufficient estimate.** There exist constants
\(c>0\) and \(j_0\) such that

\[
\boxed{z_{2^jN_0}^TS_{2^jN_0}^{-1}z_{2^jN_0}
       \ge c\,\delta_{2^jN_0}^2\qquad(j\ge j_0).}\tag{G}
\]

If (G) holds, then

\[
\frac1{\delta_{N_{j+1}}}-\frac1{\delta_{N_j}}
 =\frac{\delta_{N_j}-\delta_{N_{j+1}}}{\delta_{N_j}\delta_{N_{j+1}}}
 \ge c,
\]

so \(\delta_{N_j}=O(1/j)=O(1/\log N_j)\) and RH follows. This is a
complete **conditional** end-to-end route. Estimate (G) itself is not proved,
and is not asserted to be necessary for RH. Mere positivity of every \(S_N\)
does not establish (G), nor the divergence in (16).

## 7. DO26.7 — a hypothetical zero has a quantitative first-cell cost

For \(\Re s>1/2\), the functional

\[
\mathcal M_s(f)=\int_1^\infty f(t)t^{-s-1}\,dt
\]

is bounded on \(\mathcal H\), with

\[
|\mathcal M_s(f)|\le\frac{\|f\|}{\sqrt{2\Re s-1}}.\tag{17}
\]

This is Cauchy–Schwarz against \(t^{1-\overline s}\) in \(L^2(dt/t^2)\).
Expanding the jumps of \(h_k\) initially for \(\Re s>1\) gives

\[
\mathcal M_s(h_k)=\frac{\zeta(s)}s(1/k-k^{-s}),
\quad \mathcal M_s(\chi)=1/s.\tag{18}
\]

To see the jump calculation directly,
\(h_k(n)-h_k(n-1)=1/k-1_{k\mid n}\). Summation by parts against
\(n^{-s}\) proves (18) in its initial domain. Boundedness of \(h_k\)
makes its integral holomorphic for \(\Re s>0\); analytic continuation
extends the formula. At \(s=1\), the factor zero cancels the simple zeta
pole and the value is \(\log k/k\), not zero.

If \(\zeta(\rho)=0\), \(\beta=\Re\rho>1/2\), (17) and (18) imply
\(\mathcal M_\rho(g)=0\) and \(\mathcal M_\rho(r)=1/\rho\). Hence

\[
\delta\ge\frac{2\beta-1}{|\rho|^2},\qquad
\boxed{1-g(1)\ge(2-\sqrt2)\frac{2\beta-1}{|\rho|^2}.}\tag{19}
\]

No assumption on the multiplicity of \(\rho\) is needed. In particular
\(\delta=0\) excludes all zeros in \(\Re s>1/2\); the standard functional
equation reflects any nontrivial zero with real part below \(1/2\) to one
above it. This proves the forward RH implication in (NB) directly.
The dictionary, the first interval and every doubling schedule are fixed
independently of \(\rho\). Inequality (19) is a lower bound conditional on
a hypothetical zero, not a proof that its right-hand side vanishes.

## 8. DO26.8 — arithmetic support is an independent obstruction

For \(q\ge1\), define finite-support vectors

\[
\phi_q(n)=q(q-1)1_{n=q-1}-q(q+1)1_{n=q},
\quad
f_q=\sum_{d\mid q}\mu(q/d)\phi_d.
\]

The first summand of \(\phi_1\) is zero, so no cell 0 belongs to the space.
Then, for \(k,q\ge2\),

\[
\langle h_k,\phi_q\rangle=1_{k\mid q}-1/k,
\quad\langle\chi,\phi_q\rangle=-1_{q=1},
\]

\[
\boxed{\langle h_k,f_q\rangle=1_{k=q},\qquad
        \langle\chi,f_q\rangle=-\mu(q).}\tag{20}
\]

**Proof.** The weighted pairing against \(\phi_q\) is the finite difference
\(h_k(q-1)-h_k(q)\). This is the first formula, including \(q=1\).
Möbius inversion gives
\(\sum_{k\mid d\mid q}\mu(q/d)=1_{k=q}\), while
\(\sum_{d\mid q}\mu(q/d)=0\) for \(q>1\), proving (20). ∎

This is the classical Vasyunin biorthogonal construction; its consequence
for a selected arithmetic dictionary is as follows. If \(q\notin S\),
then \(f_q\perp\mathcal B_S\), by (20) and continuity. Therefore

\[
\operatorname{dist}(\chi,\mathcal B_S)^2
\ge\frac{\mu(q)^2}{\|f_q\|^2}.\tag{21}
\]

In particular, every dictionary that approximates \(\chi\) must contain
every squarefree index \(q\ge2\). For a prime \(q\ge3\),
\(f_q=\phi_q-\phi_1\) has disjoint contributions, and
\(\|f_q\|^2=2(q^2+1)\). The prime 2 is an overlap exception:
\(f_2(1)=4,f_2(2)=-6\), so \(\|f_2\|^2=14\), not 10.
This packet claims the necessary support condition, not an unconditional
sufficiency theorem for squarefree-only dictionaries.

### DO26.9 — same common Mellin zeros, but distance at least 1/52

Take

\[
S=\{2^a3^b:a,b\ge0\}\setminus\{1\}.
\]

This space is invariant under \(D_2,D_3\). It omits 5, and the exact witness is

\[
f_5(1)=2,\quad f_5(4)=20,\quad f_5(5)=-30,
\]

with all other entries zero. Direct calculation gives

\[
\langle\chi,f_5\rangle=1+1-1=1,
\quad \|f_5\|^2=2+20+30=52.
\]

Consequently, writing \(g_S=P_{\mathcal B_S}\chi\),

\[
\boxed{\|\chi-g_S\|^2\ge1/52,\qquad
1-g_S(1)\ge(2-\sqrt2)/52.}\tag{22}
\]

Nevertheless, the common zero set of the Mellin transforms of this sparse
dictionary in \(\Re s>1/2\) is exactly the zeta zero set there. Indeed,
\(h_2,h_3\) are included. If \(s\ne1\), \(\zeta(s)\ne0\), and both
transforms vanish, then

\[
(1-s)\log2\in2\pi i\mathbb Z,\qquad
(1-s)\log3\in2\pi i\mathbb Z.
\]

If either integer is zero then \(s=1\), already excluded. Otherwise
\(\log2/\log3\) would be rational, contradicting unique factorization.
At \(s=1\), both transforms instead have the nonzero removable values from
(18). Zeta zeros do give common zeros by (18); in this half-plane their
multiplicities are not canceled by these factors. The same argument applies
to the full dictionary, since it also contains \(h_2,h_3\).

Thus unchanged common Mellin zeros, dilation invariance and positive finite
Grams can coexist with a definite failure of target approximation. The
conclusion is about **this sparse dictionary**. It does not refute full
Nyman–Beurling, and does not refute any repository construction that keeps
all prime factors while marking or correcting finitely many of them.

## 9. Where the attempted completion stops

The proposed escape from the repository's repeated positivity obstructions
was to use genuine orthogonal prediction instead of assuming positivity of
a signed arithmetic energy. That succeeds in making every finite Gram and
Schur matrix positive by construction, and in supplying exact improvement
formulas (9), (14). It does not make the cumulative improvement large enough.

Three actual attempted shortcuts fail:

1. Exact agreement on the first interval at finite \(N\) does not imply
   zero distance: \(g_2=2h_2\), \(g_2(1)=1\),
   \(\delta_2=1-\log2>0\). The leakage in (5) is essential.
2. The naive sign \(L_{2,N}\ge0\) is false: the full infinite-Gram
   enclosure gives \(-0.001714996317<L_{2,8}<-0.001714996316\).
   Squaring that leakage still gives a valid improvement, but only about
   3.12 percent of the whole \(8\to16\) Schur gain in this bounded example.
3. Compressing to the two incommensurable prime dilations preserves the
   common-zero signature but loses source completeness, by (22).

The surviving ambitious target is (G), or the weaker divergence (16).
The available proofs do not establish either. This is the exact missing
estimate in the conditional end-to-end route, not an omitted finishing step.
