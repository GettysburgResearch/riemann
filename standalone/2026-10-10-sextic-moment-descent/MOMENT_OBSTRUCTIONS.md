# The actual higher moment: exceptional rows, exact core reduction, and a long-row theorem

**Status:** new mathematical components and an obstruction audit, 2026-10-10. The identities, conditional reductions, and long-row theorem below have complete proofs. The desired near-diagonal fourth or higher moment is not proved or disproved.

**Scope:** the original October 5 Möbius/sextic family, with fixed finite-order Hecke twist, fixed bad-prime set, exact nonunit zero extensions, and all nonzero element rows retained. This is a new note; it does not modify the prior research packet or its review.

**Exact sources:** OpenAI `math` commit `adc7f1241b42e322a6451854ab7e4b4c146bf78a`; October 5 `paper2.tex` lines 215–275 and 660–755 for the family, fixed-data quantifiers, and extraction, and lines 3287–3369 for the completed theta series and its removed constant mode. September 30 `paper.tex` lines 12343–12496 for the raw inverse moment, scale supremum, and sixth-power amplification. The preceding research packet is PR 910, head `670a76c1a3a8f325c43c1755b1cfc24d313a3e3c`.

**What was actually done:** source inspection; exact character and divisor identities; a proof of a core-to-all-row transfer with its precise stronger converse; an elementary Poisson proof of a long-row general moment; an audit of the prime-extraction induction and its quantifiers. This review does not establish a near-diagonal moment estimate and does not include a zero computation or Lean build. Publication of the research packet does not enlarge that validation scope.

**Smallest remaining gap:** a near-diagonal moment for the actual Möbius family that retains the exceptional sixth-power copies. Controlling a primitive or nonexceptional family and then adding a known target Mertens bound does not improve that bound.

## 1. The hypothesis that is actually being proposed

Let \(K=\mathbb Q(\sqrt{-3})\), let \(\mathcal O\) be its ring of integers, and write \(N\) for its norm. Fix a finite-order Hecke character \(\nu\), a finite set \(S\) containing the primes above \(6\) and the defining conductor of \(\nu\), and \(W\in C_c^\infty((0,\infty))\). Put

\[
A_u(D;W)=\sum_{(n,S)=1}\mu_K(n)\nu(n)\chi_n(u)W(Nn/D),
\qquad \chi_n(u)=(u/n)_6.
\tag{1.1}
\]

Here \(n\) is an ideal, represented by its primary generator when a symbol is evaluated. The rows \(u\) are nonzero elements. The symbol is zero when \(n\) meets \(u\), including when a displayed exponent is divisible by six.

For fixed \(k\ge1\) and \(h>0\), the proposed hypothesis is

\[
\mathcal M_{2k}(D,D^h):=
\sum_{0<Nu\le D^h}|A_u(D;W)|^{2k}
\ll_{k,h,\nu,S,W,\epsilon}D^{k+h+\epsilon}.
\tag{1.2}
\]

The intended useful range is \(h=1+\theta\), with arbitrarily small fixed \(\theta>0\). The twist, test, and bad-prime set are fixed before \(D\) varies. A moving row is not part of this fixed datum. For a zero-free conclusion, (1.2) must hold for every fixed smooth test needed by the Mellin argument.

The following are different statements:

* a moment with the sixth-power or other exceptional rows removed;
* a moment for squarefree rows only;
* a bound for every fixed row with an uncontrolled row-dependent constant;
* a moment uniform in every bounded multiplicative coefficient;
* a moment for a test chosen anew with \(D\), without a stated seminorm bound.

None can silently replace (1.2).

## 2. A genuine counterexample to a broader coefficient class

The finite-order restriction matters. If it were replaced by arbitrary completely multiplicative unit coefficients, take the ideal Liouville function

\[
\nu(n)=(-1)^{\Omega_K(n)}.
\]

Then \(\mu_K(n)\nu(n)=\mu_K(n)^2\). Choose nonnegative nonzero \(W\). For prime ideals \(p\notin S\) with \(Y/2<Np\le Y\), where \(Y=D^{h/6}\),

\[
A_{p^6}(D)=\sum_{(n,Sp)=1}\mu_K(n)^2W(Nn/D)\gg_{S,W}D
\]

for sufficiently large \(D\). Indeed the fixed-\(S\) squarefree sum has a positive density main term, while excluding multiples of \(p\) costs \(O_W(D/Np+1)\). There are \(\asymp Y/\log Y\) such prime ideals. Therefore

\[
\mathcal M_{2k}(D,D^h)
\gg \frac{D^{2k+h/6}}{\log D}.
\tag{2.1}
\]

A diagonal-size assertion \(D^{k+h+\epsilon}\) in this broader class requires

\[
h\ge \frac{6k}{5}.
\tag{2.2}
\]

This refutes an arbitrary-multiplicative-coefficient version in the proposed near-\(D\) range. It is **not** a counterexample to (1.2): Liouville is not a fixed finite-order Hecke character.

Likewise, choosing a different finite-order character of increasingly large conductor to mimic finitely many prescribed prime values does not refute a fixed-character asymptotic whose implied constant may depend on that character. Such a construction would only attack a stronger conductor-uniform formulation, which would need to be stated separately.

## 3. Exact decomposition of every row into its sixth-power-free core

For a row \(u\ne0\), factor uniquely

\[
u=r v^6,
\tag{3.1}
\]

where the ideal \((r)\) has each prime valuation between zero and five and \(v\) represents an integral ideal. There is no condition \((r,v)=1\). Units are retained in \(r\). Since every unit has sixth power one, \(v^6\) is independent of the chosen generator of its ideal; this makes the element factorization unambiguous after the ideal factorization is chosen.

Write

\[
\xi_r(n)=\nu(n)\chi_n(r)
\]

with the original zero extensions. The core and its lifted rows satisfy

\[
A_{rv^6}(D)
=\sum_{(n,Sv)=1}\mu_K(n)\xi_r(n)W(Nn/D).
\tag{3.2}
\]

Deleting an Euler factor is not the same as removing a row. The variable \(v\) produces a moving coprimality mask.

### Lemma 3.1. Exact inverse of the moving mask

For every \(D>0\),

\[
A_{rv^6}(D)
=\sum_{d\mid v^\infty}\xi_r(d)A_r(D/Nd).
\tag{3.3}
\]

The notation \(d\mid v^\infty\) means that all prime divisors of \(d\) divide \(v\), with unrestricted exponents. The sum is finite at each \(D\), because the test has compact support away from zero.

**Proof.** For each prime dividing \(v\), the coefficient convolution is

\[
(1-\xi_r(p)z)\sum_{j\ge0}\xi_r(p)^jz^j=1.
\]

At a zero-extended prime, \(\xi_r(p)=0\), so the same identity still holds. At primes not dividing \(v\), the original inverse Euler coefficient is unchanged. Multiplying the finite-prime local identities and then evaluating the exact norm-rescaled test gives (3.3). Equivalently, the coefficient of an ideal divisible by a prime of \(v\) cancels, while all other coefficients remain \(\mu_K(n)\xi_r(n)\). No convergence argument is needed for a fixed physical scale. \(\square\)

For comparison, the opposite finite identity is

\[
A_r(D)=\sum_{d\mid\operatorname{rad}v}
\mu_K(d)\xi_r(d)A_{rv^6}(D/Nd).
\tag{3.4}
\]

It is the identity used by the source's sixth-power amplification.

### Lemma 3.2. Subpower norm of the exact mask inverse

For every fixed \(b>0\) and every \(\epsilon>0\),

\[
\sum_{d\mid v^\infty}(Nd)^{-b}
=\prod_{p\mid v}(1-(Np)^{-b})^{-1}
\ll_{b,\epsilon}(Nv)^\epsilon.
\tag{3.5}
\]

**Proof.** For sufficiently large \(Np\), depending only on \(b,\epsilon\),

\[
-\log(1-(Np)^{-b})\le\epsilon\log Np.
\]

The finitely many smaller primes contribute a fixed constant. Sum this inequality over the distinct prime divisors of \(v\), and use \(\prod_{p\mid v}Np\le Nv\). \(\square\)

This lemma controls a moving exclusion without putting it into the fixed character datum. The constants are uniform in \(v\).

## 4. A precise sufficient core moment, and its stronger converse

Normalize

\[
M_u(x)=x^{-1/2}A_u(x),\qquad
\Gamma_{2k}(D,R)=
\sum_{\substack{0<Nr\le R\\r\ {\rm sixth\text{-}power\text{-}free}}}
\sup_{0<x\le D}|M_r(x)|^{2k}.
\tag{4.1}
\]

In (4.1), “sixth-power-free” refers to all valuations of the row ideal being at most five; it includes the unit rows. Small \(x\) cause no divergence, since \(A_r(x)=0\) below a fixed support threshold.

### Theorem 4.1. Core-to-all-row transfer

For every fixed \(k\ge1\), \(D,H\ge2\), and \(\epsilon>0\),

\[
\sum_{0<Nu\le H}|M_u(D)|^{2k}
\ll_{k,W,\epsilon}(HD)^\epsilon
\sum_{\substack{R\le H\\R\ {\rm dyadic}}}
\left(\frac HR\right)^{1/6}\Gamma_{2k}(D,2R).
\tag{4.2}
\]

In particular, a uniform envelope with \(\lambda\ge0\),

\[
\Gamma_{2k}(D,R)
\ll (DR)^\epsilon\left(R+R^{1/6}D^\lambda\right)
\quad(1\le R\le 2H)
\tag{4.3}
\]

implies

\[
\mathcal M_{2k}(D,H)
\ll (DH)^\epsilon D^k
\left(H+H^{1/6}D^\lambda\right).
\tag{4.4}
\]

**Proof.** Divide (3.3) by \(D^{1/2}\). Its coefficient at scale \(D/Nd\) is \(\xi_r(d)(Nd)^{-1/2}\). Lemma 3.2, with \(b=1/2\), gives

\[
|M_{rv^6}(D)|^{2k}
\ll_{k,\epsilon}(Nv)^\epsilon
\sup_{0<x\le D}|M_r(x)|^{2k}.
\]

For a fixed core \(r\), the number of ideals \(v\) with \(Nv\le(H/Nr)^{1/6}\) is \(O((H/Nr)^{1/6})\). Sum over these ideals and then split the cores into dyadic norm ranges. This proves (4.2), after shrinking the preliminary loss.

Insert (4.3). The first contribution is

\[
H^{1/6}\sum_{R\le H}R^{5/6}\ll H.
\]

The second is \(H^{1/6}D^\lambda\) per dyadic interval, so it costs only an additional logarithm. Absorb that logarithm into the arbitrarily small power loss and restore the factor \(D^k\). \(\square\)

For \(H=D^h\), the desired diagonal-size moment follows from (4.3) only when

\[
\lambda\le\frac{5h}{6}.
\tag{4.5}
\]

Already the unit row in (4.3) forces

\[
|A_1(D)|\ll D^{1/2+\lambda/(2k)+\epsilon}.
\tag{4.6}
\]

Thus the required core estimate contains the target cancellation on its short-core boundary. It is not a way to avoid that boundary.

### Theorem 4.2. Converse for a rectangular moment hypothesis

Fix \(h_0>0\). Suppose the stronger assertion

\[
\sum_{0<Nu\le H}|M_u(x;V)|^{2k}
\ll_{V,\epsilon}(Hx)^\epsilon H
\quad\text{for all }H\ge\max(2,x^{h_0})
\tag{4.7}
\]

holds for \(V=W\) and \(V(y)=-W(y)/2-yW'(y)\), uniformly over the polynomially bounded ranges being used. Then

\[
\Gamma_{2k}(D,R)
\ll (DR)^\epsilon
\left(R+R^{1/6}D^{5h_0/6}\right).
\tag{4.8}
\]

Together with Theorem 4.1, this identifies the short-core envelope for the **rectangular**, all-longer-row version of the moment.

**Proof.** The one-dimensional \(W^{1,2k}\) bound on unit logarithmic intervals, and

\[
\frac{\partial}{\partial\log x}M_u(x;W)
=M_u(x;-W/2-yW'),
\]

give

\[
\sum_{0<Nu\le C H}\sup_{0<x\le D}|M_u(x)|^{2k}
\ll H(HD)^\epsilon
\quad(H\ge\max(2,D^{h_0})).
\tag{4.9}
\]

There are \(O(\log(2+D))\) logarithmic intervals, and the initial bounded range is harmless. The row range in (4.7) is admissible at every smaller scale \(x\le D\); this is the reason for its rectangular form.

For cores in a fixed dyad \(Nr\asymp R\), put \(H_0=\max(4R,D^{h_0},2)\) and choose ideals \(a\) outside \(S\) with \(Na\le P\asymp(H_0/R)^{1/6}\). There are \(\gg_S P\) choices. From (3.4), its normalized coefficient mass, and a finite Hölder inequality,

\[
\sup_{x\le D}|M_r(x)|^{2k}
\ll P^\epsilon\sup_{y\le D}|M_{ra^6}(y)|^{2k}.
\]

The map \((r,a)\mapsto ra^6\) is injective because valuation reduction modulo six recovers \(r\), including its unit. Coprimality of \(r\) and \(a\) is unnecessary. Its image has norm \(O(H_0)\). Average over \(a\), sum over \(r\), and use (4.9). The result is

\[
\ll (DR)^\epsilon\frac{H_0}{P}
\ll (DR)^\epsilon R^{1/6}\max(R,D^{h_0})^{5/6}.
\]

Dyadic summation gives (4.8). \(\square\)

**Quantifier warning.** The original hypothesis (1.2) is only stated on \(H=D^h\). It does not by itself grant (4.7) for all longer row ranges at every smaller column scale. Replacing \(D\) by a larger scale and rescaling the test changes its support and seminorms; that is not a free argument. The converse above explicitly assumes the rectangular formulation. The core-to-all-row implication does not require this extra assertion.

At \(k=1\), the source's raw all-row bound and its scale supremum have this stronger range. The source's amplified envelope is exactly the case \(\lambda=5(1+c)/6\), up to arbitrarily small losses. Reusing that envelope for \(k\ge2\) would be a new theorem.

## 5. Why adding an old Mertens bound cannot repair deleted exceptional rows

### Proposition 5.1. Contribution of a fixed collection of cores

Let \(\mathcal C\) be a fixed finite collection of sixth-power-free cores. Suppose, for some \(\beta>0\),

\[
|A_r(x;W)|\le C_{r,W,\beta}x^\beta
\quad(r\in\mathcal C)
\tag{5.1}
\]

at every scale above the lower support threshold. Then

\[
\sum_{r\in\mathcal C}\ \sum_{N(rv^6)\le H}
|A_{rv^6}(D;W)|^{2k}
\ll D^{2k\beta+\epsilon}H^{1/6}.
\tag{5.2}
\]

**Proof.** Apply (3.3), then (5.1), then Lemma 3.2 with \(b=\beta\):

\[
|A_{rv^6}(D)|\le C_rD^\beta
\sum_{d\mid v^\infty}(Nd)^{-\beta}
\ll C_rD^\beta(Nv)^\epsilon.
\]

Count \(v\) and sum over the fixed finite list. \(\square\)

Under the source's tame conductor classification, cores whose induced character belongs to a fixed finite family supported on \(S\) have no prime outside \(S\) in their sixth-power-free ideal part. Their valuations at the finitely many primes of \(S\), and their units, have only finitely many possibilities. Thus the proposition covers the usual fixed-family exceptional cores, and in particular the core \(r=1\).

Suppose a new theorem bounds the remaining rows by \(D^{k+\epsilon}H\), while (5.1) is the only input for the exceptional cores. The resulting full moment is merely

\[
\mathcal M_{2k}(D,H)
\ll D^\epsilon
\left(D^kH+D^{2k\beta}H^{1/6}\right).
\tag{5.3}
\]

At \(H=D^h\), the exact prime extraction applied to (5.3) returns

\[
\boxed{\quad
\beta_{\rm output}
=\max\left\{\frac12+\frac{5h}{12k},\ \beta\right\}.
\quad}
\tag{5.4}
\]

Indeed dividing the moment by the number \(D^{h/6-o(1)}\) of copying prime rows and taking the \(2k\)-th root leaves \(D^\beta\) from the second term. The exact lower-scale recursion removes the omitted-prime error but does not remove this moment contribution.

For \(k=2\), a previous \(7/8\) or \(139999/160000\) Mertens exponent therefore cannot patch an exceptional-row deletion to produce \(17/24\). The old exponent is fed back unchanged. A proof that controls only the nonexceptional rows has left the target-copy obligation unresolved.

There is also a separate interpolation obstruction. Here one needs the stronger, separately justified estimate

\[
\max_{0<Nu\le D^h}|A_u(D)|\ll D^{\beta+\epsilon}
\tag{5.5a}
\]

uniformly in the moving row, together with the imported second moment. The fixed-core premise (5.1) alone does not give (5.5a). Section 8 of the companion FOURTH_MOMENT_ATTACK.md proves this uniform adapter from a common zero-free half-plane for the relevant finite-order Hecke characters, including conductor bounds and the literal imprimitive masks. Under these uniform premises, interpolation gives

\[
\mathcal M_{2k}(D,D^h)
\ll D^{1+(2k-2)\beta+h+\epsilon}.
\]

Its extracted exponent is

\[
\beta+\frac{1-2\beta+5h/6}{2k}.
\tag{5.5}
\]

As \(h\downarrow1\), its fixed point is \(11/12\), independently of \(k\). In particular it cannot bootstrap the stronger imported bound near \(7/8\) downward. A genuinely stronger joint arithmetic estimate is needed.

## 6. Square and cube rows: no oversized algebraic diagonal found

If \(u=v^2\), then \(\chi_n(u)\) is cubic in \(v\). If \(u=v^3\), it is quadratic. These are thinner row sets, of sizes \(O(H^{1/2})\) and \(O(H^{1/3})\), but their row sums still retain their exact zero extensions. Thinness alone does not prove their moment is harmless.

Their full algebraic diagonal has the expected upper size. More generally, let \(m\ge2\) and let \(k\) be fixed. Consider \(2k\) squarefree ideal factors \(n_1,\ldots,n_k,n'_1,\ldots,n'_k\), all of norm \(\asymp D\), for which

\[
\sum_i v_p(n_i)-\sum_i v_p(n'_i)\equiv0\pmod m
\quad\text{at every prime }p.
\tag{6.1}
\]

Every prime has an incidence pattern \((I,J)\) recording the left and right factors in which it occurs. A nonempty permitted pattern has \(|I|+|J|\ge2\): a single occurrence would give difference \(\pm1\), which is not zero modulo \(m\). If \(q_{I,J}\) is the product of primes with that pattern, then

\[
\prod_{I,J}(Nq_{I,J})^{|I|+|J|}\ll D^{2k},
\qquad
\prod_{I,J}Nq_{I,J}\ll D^k.
\]

There are only finitely many patterns for each fixed \(k\). Dropping coprimality and squarefreeness and applying the fixed-order ideal divisor bound gives \(O(D^{k+\epsilon})\) tuples. This covers orders \(m=2,3,6\), including the extra sixth-power diagonals at high \(k\).

For \(m=1\), a single occurrence is allowed. That is exactly the trivial-character situation, where the algebraic diagonal count can instead be \(D^{2k}\), and actual Möbius cancellation is indispensable. The sixth-power copying stratum therefore cannot be justified by the same diagonal argument.

This counting result does not bound the nonprincipal row correlations. Nor does it prove that quadratic and cubic strata have no analytic off-diagonal main terms. It rules out one specific proposed contradiction, an oversized purely algebraic principal-character diagonal, for the nontrivial orders.

## 7. An unconditional general moment in a genuinely long row range

The following estimate is useful as a check on the family and its diagonals. It uses no imported quasi-RH conclusion, no Möbius cancellation, and no theta transformation.

### Theorem 7.1. Elementary long-row moment

Fix \(k\ge1\), \(\delta>0\), \(D\ge2\), and a compact norm interval \([aD,bD]\), where \(0<a<b\). Let \(c(n)\) be arbitrary row-independent coefficients supported on squarefree ideals prime to \(6\) in that interval, with \(|c(n)|\le C\). Then for every \(\epsilon>0\),

\[
\sum_{0<Nu\le H}
\left|\sum_n c(n)\chi_n(u)\right|^{2k}
\ll_{K,k,a,b,C,\delta,\epsilon}HD^{k+\epsilon}
\quad\text{if }H\ge D^{2k+\delta}.
\tag{7.1}
\]

In particular, (7.1) applies to the actual coefficients in (1.1), uniformly in the unit phases of \(\nu\).

**Proof.** Choose a fixed nonnegative smooth compactly supported function \(\Phi\) on the complex plane, at least one on the unit disk. Majorize the row sum by the sum over all \(u\in\mathcal O\) weighted by \(\Phi(u/\sqrt H)\), and expand the \(2k\)-th power.

For each pair of \(k\)-tuples, its row character is

\[
\psi(u)=\prod_{i=1}^k\chi_{n_i}(u)
\prod_{j=1}^k\overline{\chi_{n'_j}(u)}.
\]

It is periodic modulo the squarefree ideal

\[
q=\operatorname{rad}\left(\prod_i n_i\prod_j n'_j\right),
\qquad Q=Nq\le (bD)^{2k}.
\]

At a prime \(p\mid q\), its local factor on units is a power of the exact order-six finite-field character, and it is zero on nonunits even if that power is divisible by six. The complete mean of \(\psi\) is zero unless the exponent difference at every prime is divisible by six. In the latter case \(\psi\) is the principal character with the exact \(q\)-mask.

For the principal pairs, the incidence argument of Section 6 bounds their number by \(O(D^{k+\epsilon})\), and each smoothed row sum is \(O(H)\). Their total contribution is \(O(HD^{k+\epsilon})\).

For a nonprincipal pair, use ordinary two-dimensional lattice Poisson summation after splitting into residue classes modulo \(q\). The zero frequency vanishes. Bound every finite Fourier coefficient trivially by \(Q\). Since the Eisenstein lattice is a principal ideal lattice, its dual has shortest nonzero length \(\gg Q^{-1/2}\), with a fixed normalized shape. For every fixed integer \(N>2\), rapid Fourier decay consequently gives, when \(H\ge C_K Q\),

\[
\left|\sum_{u\in\mathcal O}\psi(u)\Phi(u/\sqrt H)\right|
\ll_N H\left(\frac QH\right)^{N/2}.
\tag{7.2}
\]

To see the normalization directly, Poisson contributes \(H/\operatorname{covol}(q)\), the trivial finite Fourier bound contributes \(Q\), and the remaining dual-lattice sum is

\[
\sum_{\xi\in q^*,\ \xi\ne0}(1+\sqrt H|\xi|)^{-N}
\ll_N (Q/H)^{N/2}.
\]

There are \(O(D^{2k})\) pairs of tuples. Since \(H\ge D^{2k+\delta}\), choose \(N\) so large that \(\delta N/2\ge k+1\). Their total nonprincipal contribution is then

\[
\ll H D^{2k}\left(\frac{(bD)^{2k}}H\right)^{N/2}
\ll HD^{k-1}.
\]

All sufficiently large \(D\) satisfy the needed relation \(H\ge C_KQ\); the bounded remaining range is absorbed by the direct estimate. This proves (7.1). All redundant local zeros were present in the periodic character throughout. \(\square\)

This is an independent elementary all-row theorem for every fixed moment, but it is far from the desired row range. It is stronger than a bare pointwise interpolation in its stated long range and uses an explicit diagonal/off-diagonal separation. The companion incidence decomposition combined with the established sextic large sieve reaches the slightly stronger threshold \(H\ge D^{2k}\); the argument here deliberately proves its own weaker \(D^{2k+\delta}\) threshold without that large-sieve input. Neither is a near-diagonal advance.

At \(H=D^h\), its threshold is \(h>2k\). The formal copying exponent is then at least

\[
\frac12+\frac{5(2k)}{12k}=\frac43.
\]

For \(k\ge3\) that row range is also beyond the \(h<6\) range of the preceding packet's stated extraction proposition. Thus this elementary theorem gives no useful new zero-free exponent. Its purpose is to establish an unconditional baseline and make the missing range explicit.

## 8. Audit of the exact prime-extraction induction

The previous packet's Proposition 7.2 is not circular under its stated hypothesis. The moment input is applied only at the current top scale \(D\). With \(Y=D^{h/6}\), the prime rows \(p^6\) satisfy \(Np\le Y\), so they are in the allowed row range. The exact identity

\[
A_1(x)=B_p(x)-\nu(p)B_p(x/Np),
\qquad B_p(x)=A_{p^6}(x),
\]

is valid for complex \(W\) and every fixed \(\nu\). Iteration uses the same test and the same fixed datum. Its smaller-scale terms are original \(A_1\) values, not an invocation of the moment with a moving excluded prime.

For \(0<h<6\), every smaller argument is at most \(2D/Y<D/2\) at a fixed sufficiently large threshold. A strong induction bound \(C x^\beta\), with \(\beta>1/2+5h/(12k)>0\), makes their averaged sum at most

\[
C_\beta C D^\beta Y^{-\beta},
\]

which is below half the proposed bound at sufficiently large \(D\). The finitely bounded initial range is absorbed into \(C\). The moment loss is chosen before this induction so that the top-scale term has a fixed smaller exponent. There is no self-assumption at scale \(D\).

The following quantifiers remain essential:

1. The moment must hold at all sufficiently large real scales, or at a cofinal family with an explicit interpolation adapter; a sparse empirical sequence does not suffice.
2. The prime ideal count is for one fixed field and fixed \(S\); no moving-conductor prime theorem is used.
3. The moment must include the sixth-power copying rows. Removing them makes the first step unavailable.
4. To exclude a prescribed zero \(\rho\), one may fix \(W(y)=y^{-\rho}\phi(y)\) and then apply the theorem for that fixed test. Its constants may depend on \(\rho\). They do not need to be uniform over all hypothetical zeros to obtain the stated open half-plane.
5. For the limiting \(17/24\), the moment must be available for arbitrarily small fixed positive \(\theta\). A theorem at one fixed \(\theta\) gives the correspondingly larger exponent.
6. To approach \(1/2\) through all moments, each fixed \(k\) may have its own constants. This hierarchy would be extremely strong, not a consequence of the \(k=1\) theorem or of log-convexity.

A useful general form is: if the moment is bounded by \(D^{B+\epsilon}\), the same induction yields an exponent \((B-h/6)/(2k)\), provided a positive larger induction exponent is chosen. This explains both (5.4) and the interpolation obstruction (5.5).

## 9. Theta poles and the classical large sieve do not remove these obligations

The original completed theta series is not an arbitrary multiplicative coefficient family. The source specializes its twist to a fixed ray character times the actual sextic row and fourth-power label. In its Mellin argument, a horizontal derivative removes the constant term in each cusp; the source explicitly obtains an entire completed series at lines 3345–3369. One therefore cannot point to the untwisted cubic-theta residue and assert an unremoved pole in the actual inverse family without tracing the derivative and coefficient conversion.

Conversely, a tensor or balanced-divisor extension must check its own transformed constant modes. Entireness of the original scalar completion does not automatically prove entireness, admissibility, or the same norm bound for a new coefficient family.

The primary classical reference [Blomer–Goldmakher–Louvel, Theorem 1.3](https://arxiv.org/pdf/1112.1650) bounds squarefree rows and columns by the factor \(M+N+(MN)^{2/3}\), times an arbitrarily small power and the coefficient square norm. Its stars explicitly impose squarefreeness. Section 2 also uses primitive inducing characters: a sixth-power label becomes the trivial character without the redundant nonunit mask. These conventions differ from the original family (1.1). Passing between them requires an explicit core and exclusion adapter, such as (3.3); simply enlarging the row set is not justified by that theorem.

No actual finite-order-character counterexample to (1.2) was found in this audit. The absence of such a counterexample is not evidence that the near-diagonal moment follows from the supplied inputs. The precise unresolved statements are the all-row arithmetic estimate itself, or a sufficient uniform core estimate with its short-core boundary retained. The stronger rectangular moment has the precise converse proved in Theorem 4.2; no converse from the original one-parameter surface is asserted. A proposed proof that removes this boundary and restores it using the old exponent has not advanced it.

## 10. The unbounded moment hierarchy is an RH-level assertion

The limiting general-moment goal can be stated precisely as an equivalence. This does not prove either side.

Fix one \(\nu,S\) as in Section 1 and one \(h>0\). For every nonzero fixed element \(r\), let \(\xi_r\) denote the finite-order Hecke character represented on good ideals by

\[
\xi_r(n)=\nu(n)\chi_n(r).
\]

Use sextic reciprocity, or the corresponding Kummer character, to identify its primitive inducing character. Keep the original zero extensions at primes dividing \(rS\). This is the same character interpretation used by Section 8 of FOURTH_MOMENT_ATTACK.md: a defining modulus has norm at most \(C_{\nu,S}Nr\). By “GRH for this family” below we mean that every nontrivial zero of every such primitive inducing Hecke \(L\)-function lies on \(\Re s=1/2\).

### Theorem 10.1. Fixed-twist family equivalence

The following assertions are equivalent:

1. There is an unbounded set of fixed positive integers \(k\) such that, for every fixed \(W\in C_c^\infty((0,\infty))\) and every \(\epsilon>0\),

   \[
   \sum_{0<Nu\le D^h}|A_u(D;W)|^{2k}
   \ll_{\nu,S,W,h,k,\epsilon}D^{k+h+\epsilon}.
   \tag{10.1}
   \]

2. GRH holds for the entire sextic row-twist family \(\{\xi_r:r\ne0\}\).

The implication from assertion 2 in fact supplies (10.1) for every fixed \(k\) and every fixed \(h>0\). The unbounded orders in assertion 1 need not share an implied constant, and \(h\) need not tend to zero or one.

**Proof that 1 implies 2.** Fix a nonzero row \(r\) and a test \(W\). Once \(D\) is sufficiently large, this row occurs in (10.1), so positivity gives directly

\[
|A_r(D;W)|\ll D^{1/2+h/(2k)+\epsilon/(2k)}.
\tag{10.2}
\]

Given any \(\gamma>1/2\), choose one permitted fixed \(k\) sufficiently large and then a sufficiently small moment loss. The allowed orders are unbounded, so this proves

\[
A_r(D;W)\ll_{r,W,\gamma}D^\gamma
\quad\text{for every fixed }r,W,\gamma>1/2.
\tag{10.3}
\]

Only the original surface moment at the current scale was used. In particular, this qualitative hierarchy implication does not even require copying rows. At a finite fixed moment order the exact rough-base copying argument gives the sharper exponent \(1/2+5h/(12k)\) discussed in Section 8 and the companion GENERAL_MOMENT_ATTACK.md. Either exponent tends to \(1/2\) along unbounded orders.

For completeness, this excludes a zero \(\rho\) with \(\Re\rho>1/2\) by a local Mellin argument. Choose \(1/2<\gamma<\Re\rho\) and \(W(y)=y^{-\rho}\phi(y)\), with nonnegative nonzero smooth compactly supported \(\phi\). Then

\[
\mathcal MW(\rho)=\int_0^\infty\phi(y)\,\frac{dy}{y}>0.
\]

The integral \(\int_0^\infty A_r(D;W)D^{-s-1}\,dD\) is holomorphic for \(\Re s>\gamma\), by (10.3) and the lower support cutoff. For \(\Re s>1\) it equals \(\mathcal MW(s)\) times the reciprocal \(L\)-series of the literal masked character. The finite missing Euler factors are holomorphic and nonzero in \(\Re s>0\). Thus a zero at \(\rho\) would give a pole on one side and a holomorphic value on the other, a contradiction. The primitive functional equation and complex conjugation reflect any nontrivial zero to \(1-\overline{\rho}\) for the same character, so the nontrivial zeros all have real part \(1/2\).

**Proof that 2 implies 1.** Apply the proof of Lemma 8.1 in FOURTH_MOMENT_ATTACK.md to this family. That proof needs a common zero-free half-plane only for the characters under consideration: its polynomial conductor bound comes from periodic finite-order character sums on the fixed Eisenstein lattice, and its analytic logarithm argument has constants independent of the individual character. Under assertion 2, take any fixed \(\beta>1/2\) as the zero-free boundary there. For every fixed \(\gamma>0,\eta>0\), its conclusion and the imprimitive Euler-factor estimate give

\[
|L(\sigma+it,\xi_u)^{-1}|
\ll_{\nu,S,\gamma,\eta}
\bigl[(1+Nu)(2+|t|)\bigr]^\eta,
\qquad \sigma\ge\frac12+\gamma.
\tag{10.4}
\]

The same bound holds for the reciprocal series with the fixed \(S\)-mask; at a principal pole the reciprocal is holomorphic and vanishes. Mellin shifting against the fixed test therefore yields

\[
|A_u(D;W)|\ll D^{1/2+\gamma}(1+Nu)^\eta.
\]

For \(Nu\le D^h\), choose \(\gamma,\eta>0\) so small that \(2k(\gamma+h\eta)<\epsilon\). Raise this bound to the \(2k\)-th power and sum over the \(O_K(D^h)\) rows. This proves (10.1). The second-moment theorem and the imported quasi-RH conclusion are not used in this direction. \(\square\)

**Exact scope of the RH consequence.** With \(\nu=1\), the member \(r=1\) is \(\zeta_K(s)=\zeta(s)L(s,\chi_{-3})\). Assertion 1 therefore implies ordinary RH, as well as GRH for \(L(s,\chi_{-3})\) and the other sextic row twists. RH for \(\zeta_K\) alone is not the converse assumption: assertion 2 concerns the entire moving-row character family. If (10.1) is asserted for every fixed finite-order \(\nu\), Theorem 10.1 is exactly equivalent to GRH for all finite-order Hecke \(L\)-functions over this field. Its forward direction uses \(r=1\) for each \(\nu\); its reverse direction covers every row twist.

Thus proving the unbounded hierarchy at one polynomial row scale would settle an RH-level statement outright. A finite number of moment estimates only yields their corresponding open half-planes; no finite computation or established second moment supplies this hierarchy.
