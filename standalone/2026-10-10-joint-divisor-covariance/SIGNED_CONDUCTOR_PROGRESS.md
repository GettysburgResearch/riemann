# Subconvex and divisor-sensitive bounds inside the signed conductor remainder

**Status:** proposed deductions from two published Hecke subconvexity estimates,
with complete adapters and incidence proofs below. The new estimates control
additional portions of the actual generalized moment at diagonal size. They
apply at every fixed order, preserve every principal mask, and do not require
the imported native Möbius second moment or a zero-free hypothesis. They do not
bound the remaining far-separated signed covariance, prove a full fourth or
higher moment, or improve the zero-free half-plane.

**Scope:** $K=\mathbb Q(\sqrt{-3})$; squarefree column ideals away from the
fixed bad set $S$; every nonzero element row; a fixed smooth radial row test;
every fixed moment order. Coefficients can have arbitrary bounded phases. The
new arithmetic input is cancellation in a complete smooth residual-character
sum, before any absolute accounting over tuples.

**Exact sources and dependencies.**

1. Han Wu, *Burgess-like subconvexity for* $\mathrm{GL}_1$,
   [arXiv:1604.08551v6](https://arxiv.org/html/1604.08551v6), Theorem 1.1;
   Compositio Mathematica **155** (2019), 1457–1499,
   [DOI](https://doi.org/10.1112/S0010437X19007309). We use the stated hybrid
   bound for all unitary Hecke characters. The proof of that external theorem
   is not newly verified here.
2. Valentin Blomer and Farrell Brumley, *On the Ramanujan conjecture over
   number fields*, Theorem 1, Annals of Mathematics **174** (2011), 581–605,
   [published paper](https://annals.math.princeton.edu/wp-content/uploads/annals-v174-n1-p18-p.pdf).
   This supplies the admissible $\theta=7/64$ in Wu's theorem.
3. Peter Söhne, *An upper bound for Hecke zeta-functions with
   Grössencharacters*, Journal of Number Theory **66** (1997), 225–250,
   [DOI](https://doi.org/10.1006/jnth.1997.2167). The divisor-sensitive input is
   its theorem as explicitly quoted in Wu's introduction, immediately before
   Theorem 1.1. That precise quoted statement, reproduced as an input below,
   is the source used for the additional divisor-sensitive deduction. The
   original 1997 proof has not been independently replayed here.
4. PR #914, commit
   `0cc0428fedbbfc340044c7451b3d392c1da9a103`,
   [CONDUCTOR_SECTORS.md](https://github.com/GettysburgResearch/riemann/blob/0cc0428fedbbfc340044c7451b3d392c1da9a103/standalone/2026-10-10-sextic-moment-conductor-core/CONDUCTOR_SECTORS.md),
   Sections 3–8. We give the required incidence count again below.
5. PR #919, commit
   `9b04a887e171b3104a66cf57296ce5b0b2920d78`,
   [SMALL_GCD_CONDUCTOR_REDUCTION.md](https://github.com/GettysburgResearch/riemann/blob/9b04a887e171b3104a66cf57296ce5b0b2920d78/standalone/2026-10-10-averaged-conductor-frontier/SMALL_GCD_CONDUCTOR_REDUCTION.md),
   supplies the exact small-gcd signed remainder and its classical tail bound.
6. PR #923, commit
   `1a1152008706f7e24fa1efe4990588f8f99c5d8d`,
   [CROSS_SIDE_SEPARATION_SECTOR.md](https://github.com/GettysburgResearch/riemann/blob/1a1152008706f7e24fa1efe4990588f8f99c5d8d/standalone/2026-10-10-sextic-separated-cores/CROSS_SIDE_SEPARATION_SECTOR.md)
   and
   [SUBSET_PRODUCT_INCIDENCE.md](https://github.com/GettysburgResearch/riemann/blob/1a1152008706f7e24fa1efe4990588f8f99c5d8d/standalone/2026-10-10-sextic-separated-cores/SUBSET_PRODUCT_INCIDENCE.md),
   are comparison sources. Neither is an analytic premise of the new block
   bounds.

No published packet is modified. The finite arithmetic checks mentioned at the
end concern the displayed exponents, not the external subconvexity theorems.

## 1. The complete row kernel and its unit projection

Fix $k\ge1$, $D\ge2$, $H\ge1$, and a fixed $B\ge1$. Let $a_n$ be
arbitrary coefficients with $a_n=0$ unless $n$ is a good squarefree ideal
with $Nn\le BD$, and $\lvert a_n\rvert\le1$. The inverse coefficients
are covered after a fixed rescaling of their test. Use the same primary
generators and zero-extended sextic symbols as the pinned source, and put

\[
A_u=\sum_n a_n\chi_n(u).
\tag{1.1}
\]

Let $\Phi\in C_c^\infty(\mathbb C)$ be radial, nonnegative and at least
one on the unit disk. For a Hermitian tuple

\[
\mathbf t=(n_1,\ldots,n_k;m_1,\ldots,m_k),
\qquad
c(\mathbf t)=\prod_i a_{n_i}\prod_i\overline{a_{m_i}},
\]

write $r_p,s_p$ for its two multiplicities at a prime $p$, and

\[
q=\operatorname{rad}\!\left(\prod_i n_i m_i\right),\quad
f=\prod_{p\mid q:\ r_p-s_p\not\equiv0\ (6)}p,\quad q_0=q/f.
\tag{1.2}
\]

The exact row character is

\[
\prod_i\chi_{n_i}(u)\prod_i\overline{\chi_{m_i}(u)}
=\psi_{\mathbf t}(u){\bf1}_{(u,q_0)=1},
\tag{1.3}
\]

where $\psi_{\mathbf t}$ is primitive modulo $f$ when $f\ne1$. Each
nontrivial local character at a good prime has conductor that prime, even
when its order is three or two. All residual-zero primes remain in $q_0$.
In particular (1.3) is an identity at nonunits, not merely on invertible
residues. The complete smooth kernel is

\[
S_{\mathbf t}^{\Phi}(H)=
\sum_{u\in\mathcal O_K}\Phi(u/\sqrt H)
\psi_{\mathbf t}(u){\bf1}_{(u,q_0)=1}.
\tag{1.4}
\]

All new row bounds assume $f\ne1$. Its zero row is then zero.
The conductor norm is $F=Nf=\prod_m Ng_m$, not the complexity
$Ng_1\sqrt{Ng_2}$. Only in the examples, which have no higher
nonprincipal multiplicities, does it reduce to $F=Ng_1Ng_2$.

### Lemma 1.1. Exact unit projection and a Hecke integral

If $\psi_{\mathbf t}$ is nontrivial on $\mathcal O_K^\times$, then

\[
S_{\mathbf t}^{\Phi}(H)=0.
\tag{1.5}
\]

Otherwise it defines a nonprincipal primitive finite-order Hecke ideal
character $\widetilde\psi$ of conductor $f$ and trivial infinite type.
Writing $\Phi(z)=\phi(|z|^2)$, one has, initially for a fixed $\sigma>1$,

\[
S_{\mathbf t}^{\Phi}(H)
=\frac{6}{2\pi i}\int_{(\sigma)}
 \widehat\phi(s)H^s L(s,\widetilde\psi)
 \prod_{p\mid q_0}\left(1-\widetilde\psi(p)(Np)^{-s}\right)\,ds,
\tag{1.6}
\]

where $\widehat\phi(s)=\int_0^\infty\phi(x)x^{s-1}\,dx$.

**Proof.** Multiplication of $u$ by a unit preserves both its norm and the
principal mask. It multiplies (1.4) by the unit's character value, proving
(1.5). In the other case, $\widetilde\psi((u))=\psi_{\mathbf t}(u)$ is
well defined. Every ideal is principal, and every nonzero ideal has six
generators. Thus (1.4) is exactly

\[
6\sum_{\mathfrak a}
 \widetilde\psi(\mathfrak a){\bf1}_{(\mathfrak a,q_0)=1}
 \phi(N\mathfrak a/H).
\]

Primitivity modulo $f$ and nonprincipality are preserved in this passage:
a residue on which the original primitive character is nontrivial can be
represented by a nonzero element prime to $f$, hence by its principal
ideal. Mellin inversion and absolute convergence give (1.6). Smooth
radiality of $\Phi$ implies that $\phi$ is smooth on $[0,\infty)$.
Although $\phi(0)$ need not vanish, its Mellin transform is holomorphic for
$\Re s>0$ and rapidly decreasing in vertical strips bounded away from
zero, by repeated integration by parts. This suffices for every contour
used below. \(\square\)

The factor six and the unit projection are specific to the full element-row
normalization. No restriction to primary, squarefree, or exceptional rows
has been substituted for that normalization.

## 2. Two uniform row estimates with every mask retained

Set

\[
\beta_0=\frac14-\frac{1-2(7/64)}{16}=\frac{103}{512}.
\tag{2.1}
\]

The first published input, applied to the unitary norm twist of
$\widetilde\psi$, is

\[
|L(1/2+it,\widetilde\psi)|
\ll_{K,\epsilon}
\left(Nf\,(2+|t|)^2\right)^{\beta_0+\epsilon}.
\tag{WU}
\]

The fixed field discriminant is absorbed into the constant. The second
published input, in the form quoted by Wu, is that for every ideal $d\mid f$,
with $F=Nf$, $d_*=Nd$, and $T\asymp_K(2+|t|)^2$,

\[
|L(1/2+it,\widetilde\psi)|
\ll_{K,\epsilon}
(TF)^{1/6+\epsilon}
+d_*^{1/2+\epsilon}+(F/d_*)^{1/4+\epsilon}.
\tag{SO}
\]

These are estimates for $L$, not for its reciprocal. In particular zeros
of $L$ do not obstruct the following contour shift.

### Theorem 2.1. Subconvex completion and conductor divisors

Uniformly for nonprincipal residual characters and all principal masks,

\[
\boxed{
|S_{\mathbf t}^{\Phi}(H)|
\ll_{\Phi,K,\epsilon}
H^{1/2}(Nf\,Nq_0)^\epsilon (Nf)^{\beta_0}.
}
\tag{2.2}
\]

For every $d\mid f$, one also has

\[
\boxed{
|S_{\mathbf t}^{\Phi}(H)|
\ll_{\Phi,K,\epsilon}
H^{1/2}(F Nq_0)^\epsilon
\left[F^{1/6}+d_*^{1/2}+(F/d_*)^{1/4}\right].
}
\tag{2.3}
\]

**Proof.** The unit-nontrivial case is zero by Lemma 1.1. In the remaining
case $L(s,\widetilde\psi)$ is entire, since the character is
nonprincipal. Shift (1.6) to $\Re s=1/2$. No pole of the Mellin test is
crossed. Polynomial growth of the fixed-character $L$-function in this
strip and the rapid vertical decay of $\widehat\phi$ justify the shift.
On the new line,

\[
\left|\prod_{p\mid q_0}(1-\widetilde\psi(p)(Np)^{-s})\right|
\le\prod_{p\mid q_0}(1+(Np)^{-1/2})
\ll_{K,\epsilon}(Nq_0)^\epsilon.
\tag{2.4}
\]

For the last estimate, at all sufficiently large primes the logarithm of
the local factor is at most $\epsilon\log Np$; the finitely many small
primes give a constant because $q_0$ is squarefree. Apply (WU) or (SO)
inside the absolutely convergent integral and reassign the positive loss.
This gives (2.2) and (2.3), with constants independent of the moving
conductor and mask. The entire mask was represented by its exact Euler
polynomial before any bound was taken. \(\square\)

### Lemma 2.2. A divisor chosen from the actual conductor

Let $P(f)=\max_{p\mid f}Np$. Then

\[
\boxed{
|S_{\mathbf t}^{\Phi}(H)|
\ll_{\Phi,K,\epsilon}
H^{1/2}(F Nq_0)^\epsilon (F P(f))^{1/6}.
}
\tag{2.5}
\]

**Proof.** Put $P=P(f)$ and $a=F^{1/3}P^{-2/3}$. There is a divisor
$d\mid f$ such that

\[
F^{1/3}P^{-2/3}\le Nd\le F^{1/3}P^{1/3}.
\tag{2.6}
\]

If $a\le1$, choose $d=1$; its upper bound holds since $FP\ge1$.
If $a>1$, multiply prime divisors of $f$, in any fixed order, until the
product norm first reaches $a$. The previous product was smaller than
$a$, and the last prime norm is at most $P$. This proves (2.6).
Consequently

\[
(Nd)^{1/2}\le(FP)^{1/6},\qquad
(F/Nd)^{1/4}\le(FP)^{1/6},\qquad
F^{1/6}\le(FP)^{1/6}.
\]

Insert this actual divisor into (2.3). \(\square\)

More precisely, whenever $f$ has a divisor with
$Nd\asymp F^{1/3}$, (2.3) gives the exponent $F^{1/6}$ itself, with the
comparison constant retained. No claim that every conductor has such a
divisor is made.

## 3. New block bounds at every fixed moment order

For $1\le m\le2k$, let $g_m$ be the product of nonprincipal primes
which occur exactly $m$ times in the full Hermitian tuple. Thus
$f=\prod_mg_m$, and these ideals and $q_0$ are pairwise coprime.
In particular $g_1$ is the singleton product, and $g_2$ is the product
of same-side double primes. Set

\[
\mathcal Q_{L,G}^{\Phi}
=\sum_{\substack{\mathbf t:f\ne1\,,\ L\le Ng_1<2L\,,\ G\le Ng_2<2G}}
|c(\mathbf t)|\,|S_{\mathbf t}^{\Phi}(H)|,
\qquad L,G\ge1.
\tag{3.1}
\]

An extra arbitrary tuple selector can be imposed in every bound below,
because the quantity being bounded is a positive accounting sum.

### Theorem 3.1. An additional subconvex branch

For every fixed $k$ and every $\epsilon>0$,

\[
\boxed{
\mathcal Q_{L,G}^{\Phi}
\ll_{k,B,S,\Phi,\epsilon}
D^{k+\epsilon}
\min\left\{
H\sqrt L,\ L\sqrt G,\
H^{1/2}L^{359/512}G^{103/512}
\right\}.
}
\tag{3.2}
\]

The first two branches are the pinned classical accounting bound. The
third is new to this packet and uses (WU).

**Proof of the third branch.** Fix all $g_m$. Every prime in the
principal mask occurs at least twice, so the support gives

\[
(Nq_0)^2\prod_{m=1}^{2k}(Ng_m)^m\le(BD)^{2k}.
\tag{3.3}
\]

There are therefore at most
$O_{k,B}(D^k\prod_m(Ng_m)^{-m/2})$ possible ideals $q_0$; if its
unrounded upper cutoff is below one there are no tuples. Once $q_0$ and
the $g_m$ are fixed, assigning each prime to its exact nonempty incidence
pattern among $2k$ positions costs at most

\[
(2^{2k}-1)^{\omega_K(q)}\ll_{k,\eta}(Nq)^\eta.
\tag{3.4}
\]

Indeed the constant $2^{2k}-1$ is at most $(Np)^\eta$ for all
sufficiently large primes, and the finite smaller set contributes a fixed
constant. Since $Nq\le(BD)^{2k}$, all these losses, and the factor
$(NfNq_0)^\eta$ in (2.2), are absorbed in $D^\epsilon$.
Multiplying the count by (2.2) leaves

\[
D^{k+\epsilon}H^{1/2}
\prod_m(Ng_m)^{\beta_0-m/2}.
\tag{3.5}
\]

The block sum for $g_1$ is
$O(L^{1/2+\beta_0})$, and that for $g_2$ is $O(G^{\beta_0})$.
For every $m\ge3$, the sum over all integral ideals converges, because
$m/2-\beta_0>1$. Dropping all remaining incidence and coprimality
restrictions in this positive majorant is legitimate. This proves the
third branch. The minimum of it and the two already proved classical
bounds gives (3.2). \(\square\)

The convergence for multiplicity three is strict here. It replaces the
harmonic loss in the older completion argument by an absolutely convergent
sum. Constants still depend on the fixed order $k$; no uniform-in-$k$
constant is asserted.

### Theorem 3.2. Prime-factor and balanced-divisor branches

Restrict (3.1) to tuples satisfying $P(f)\le Y$, for any $Y\ge1$.
Then

\[
\boxed{
\mathcal Q_{L,G;P\le Y}^{\Phi}
\ll_{k,B,S,\Phi,\epsilon}
D^{k+\epsilon}H^{1/2}Y^{1/6}L^{2/3}G^{1/6}.
}
\tag{3.6}
\]

Alternatively, restrict to conductors having a divisor $d\mid f$ with
$C_1^{-1}F^{1/3}\le Nd\le C_1F^{1/3}$, where $C_1\ge1$ is fixed.
Then

\[
\boxed{
\mathcal Q_{L,G;\mathrm{balanced}\ d}^{\Phi}
\ll_{k,B,S,\Phi,C_1,\epsilon}
D^{k+\epsilon}H^{1/2}L^{2/3}G^{1/6}.
}
\tag{3.7}
\]

**Proof.** Use (2.5) with $P(f)\le Y$, or (2.3) with the stipulated
divisor, in the same fixed-incidence count. The exponent $\beta_0$ in
(3.5) becomes $1/6$, and the first case has the factor $Y^{1/6}$.
The singleton and double block sums are consequently $L^{2/3}$ and
$G^{1/6}$. Every higher-multiplicity sum still converges. Existence of
the selected divisor or the prime bound is imposed before this estimate;
only the resulting positive count is enlarged afterward. \(\square\)

## 4. Additional diagonal-size domains

In terms of the actual tuple ideals, (3.2) controls the entire region

\[
\boxed{
(Ng_1)^{359/256}(Ng_2)^{103/256}\le H
}
\tag{4.1}
\]

at total cost $O(HD^{k+\epsilon})$. There are only
$O_k((\log(2D))^2)$ nonempty $L,G$ blocks, which are absorbed in the
positive loss. Within each selected block its lower dyadic endpoints
satisfy (4.1), so the third branch in (3.2) is at most $HD^{k+\epsilon}$.

For any chosen $Y\ge1$, (3.6) additionally controls

\[
\boxed{
P(f)\le Y,\qquad Y(Ng_1)^4Ng_2\le H^3.
}
\tag{4.2}
\]

The actual largest prime can be used instead: partition $P(f)$ into
dyadic blocks and use their upper endpoints. The harmless factor two in
(4.2) changes only the bound's constant. Thus the more intrinsic region

\[
\boxed{
P(f)(Ng_1)^4Ng_2\le H^3
}
\tag{4.3}
\]

has the same total cost. There are only $O_k(\log(2D))$ additional
nonempty prime-size blocks. Finally, on the stated balanced-divisor
subfamily, (3.7) controls

\[
\boxed{
(Ng_1)^4Ng_2\le H^3.
}
\tag{4.4}
\]

All these are positive accounting bounds for nonprincipal tuples. They
can be combined with the no-singleton and classical
$Ng_1\sqrt{Ng_2}\le H$ regions by taking their literal union, counting
overlaps once. Their validity is preserved under the two small-gcd
conditions of #919 or any of #923's remaining cross-separation conditions.
No use of positivity is made on an isolated signed sector.

For comparison, inserting mere convexity $\beta=1/4$ in the first new
criterion would give $(Ng_1)^{3/2}(Ng_2)^{1/2}\le H$, which is contained
in the older $Ng_1\sqrt{Ng_2}\le H$ region. The enlarged region uses a
strict subconvex saving.

## 5. Two feasible fourth-moment configurations with a strict gain

The following are scale comparisons for complete incidence collections.
They do not assert a lower bound for any individual character sum or for
the true signed sector. Fixed constants in the smooth factor support can
be inserted into each norm comparison. Distinct good prime ideals in
fixed relative intervals give realizations of the displayed scales; a
fixed congruence restriction on their norms can also ensure that the
residual characters are trivial on units. These are ordinary feasible
incidence patterns, not a claim that such patterns dominate the moment.

### 5.1. A gain without any prime-factor restriction

Use eight pairwise-coprime squarefree ideals and set

\[
(n_1,n_2;m_1,m_2)
=(c e a_1,\ c f_0 a_2;\ d e b_1,\ d f_0 b_2).
\tag{5.1}
\]

Here $f_0$ is a principal-mask label, distinct from the residual
conductor $f$. Take norm exponents

\[
Nc,Nd\asymp D^{7/10},\qquad
Ne,Nf_0\asymp D^{71/320},\qquad
Na_i,Nb_i\asymp D^{5/64}.
\tag{5.2}
\]

Every original factor has exponent
$7/10+71/320+5/64=1$. Moreover

\[
Ng_1\asymp D^{5/16},\quad Ng_2\asymp D^{7/5},\quad
Nq_0\asymp D^{71/160}.
\tag{5.3}
\]

At $h=101/100$, $H=D^h$, the old complexity has exponent

\[
5/16+(7/5)/2=81/80=h+1/400.
\]

Both one-sided gcds have exponent $7/10<499/700=(6-h)/7$, so these
tuples lie inside #919's small-gcd remainder. The two matched cross
separations have exponent $1-71/320=249/320$, and the unmatched pairs
are coprime. Thus none of the four cross separations is subpower.

For the whole incidence collection, the classical completion bound has
cost at most $HD^{2+1/400+\epsilon}$. The new branch (3.2) instead gives

\[
\boxed{
\mathcal Q^{\Phi}
\ll HD^{2-869/204800+\epsilon}.
}
\tag{5.4}
\]

Indeed

\[
\frac{359}{256}\frac5{16}
+\frac{103}{256}\frac75
=\frac{20511}{20480}
=\frac{101}{100}-\frac{869}{102400}.
\tag{5.5}
\]

Halving the strict difference gives the saving in (5.4). Thus this is a
diagonal-size signed sector which the previous two positive accounting
branches do not bound at that size.

### 5.2. A larger gain for a controlled prime factorization

Use (5.1), now with

\[
Nc,Nd\asymp D^{7/10},\quad
Ne,Nf_0\asymp D^{1/5},\quad
Na_i,Nb_i\asymp D^{1/10}.
\tag{5.6}
\]

Restrict the primes in the residual conductor $f=c d a_1a_2b_1b_2$
to norm at most a fixed multiple of $D^{1/10}$. For example, each of
$c,d$ can be a product of seven distinct primes at that scale. The
principal-mask primes in $e f_0$ need no such restriction.

At $h=21/20$, all original factors again have scale $D$, and

\[
Ng_1\asymp D^{2/5},\qquad Ng_2\asymp D^{7/5},\qquad
Ng_1\sqrt{Ng_2}\asymp D^{11/10}.
\tag{5.7}
\]

The old completion branch costs $HD^{2+1/20+\epsilon}$.
Both side gcds have exponent $7/10<99/140=(6-h)/7$; all matched cross
separations have exponent $4/5$. This again lies in the old hard,
far-separated small-gcd domain. Yet (3.6), with
$Y\asymp D^{1/10}$, proves

\[
\boxed{
\mathcal Q^{\Phi}
\ll HD^{2-1/120+\epsilon}.
}
\tag{5.8}
\]

The exact normalized exponent is

\[
-\frac12\frac{21}{20}
+\frac16\frac1{10}
+\frac23\frac25
+\frac16\frac75
=-\frac1{120}.
\tag{5.9}
\]

This example also lies outside (4.1): its subconvex-branch excess is
$19/512>0$. Thus the prime-factor branch supplies an additional gain
beyond the general subconvex branch. If the residual conductor has
eighteen primes all in the indicated fixed relative interval, any six
of them form a divisor comparable to $F^{1/3}$. The narrower
balanced-divisor collection then has the still stronger bound
$HD^{2-1/40+\epsilon}$ from (3.7).

## 6. Consequence for the literal signed remainder

Let $1<h\le11/10$, $H=D^h$, and $C=D^{(6-h)/7}$. Use exactly the
coefficient, row, and gcd conventions of #919. Let
$\mathcal U_C^{\Phi}(D,H)$ be its real signed sum with both side gcds
smaller than $C$, $g_1\ne1$, and $Ng_1\sqrt{Ng_2}>H$.

Let $\mathcal E_C^{\Phi}$ be its further portion where either (4.1) or
(4.3) holds, taking the union once. Equations (3.2) and (3.6), with the
dyadic summations in Section 4, prove the actual arithmetic inequality

\[
\boxed{|\mathcal E_C^{\Phi}(D,H)|\ll HD^{2+\epsilon}.}
\tag{6.1}
\]

The optional balanced-divisor region (4.4), with its fixed comparison
constant, can be added to the union with the same conclusion. These are
absolute bounds on the selected signed sums, deduced from positive
accounting of their complete character kernels.

Define the new residual sum

\[
\mathcal V_h(D)=\mathcal U_C^{\Phi}(D,D^h)
-\mathcal E_C^{\Phi}(D,D^h).
\tag{6.2}
\]

The exact norm split already proved in #919 and (6.1) give

\[
\boxed{
M_4(D,D^h)\le K_{\epsilon,h}D^{h+2+\epsilon}+2\mathcal V_h(D),
\qquad
\mathcal V_h(D)\ge-K_{\epsilon,h}D^{h+2+\epsilon}.
}
\tag{6.3}
\]

The new selection is invariant under exchanging the Hermitian sides, so
$\mathcal V_h$ is real. Deleting the controlled sector is justified by
(6.1); no monotonicity of a signed sum under restriction is presumed.

The same positive accounting can be imposed after any previously valid
norm split at higher orders. For the full smooth $2k$-moment itself,
the union of the old controlled regions and (4.1), (4.3) has total cost
$O(HD^{k+\epsilon})$; the complement is therefore another exact real
signed remainder at every fixed $k$. This all-order statement is a
proved component bound, not an induction closing the full moment.

If, for the source's fixed universal Mellin factor test and every positive
loss, one could additionally prove

\[
\int_X^{2X}\mathcal V_h(D)\,\frac{dD}{D}
\ll_{\epsilon,h}X^{h+2+e+\epsilon},\qquad e\ge0,
\tag{6.4}
\]

then #919's pinned averaged extraction would give the conditional strict
boundary $1/2+5h/24+e/4$. Equation (6.4) remains unproved. There is no
new zero-free claim here.

## 7. Why this does not close the generalized moment

For a tuple of $2k$ mutually coprime top-scale factors one has
$Ng_1\asymp D^{2k}$ and $g_2=1$. The new general subconvex branch
costs

\[
D^{k+\epsilon}H^{1/2}(D^{2k})^{359/512}
=H^{1/2}D^{(1+359/256)k+\epsilon}.
\tag{7.1}
\]

In the near-critical range $H=D^{1+\vartheta}$ with
$0<\vartheta\le1/10$ and $k\ge1$, this bound is not diagonal-size.
Even an available balanced conductor divisor would give
$H^{1/2}D^{7k/3+\epsilon}$, again too large in that range. In particular these
positive-accounting improvements do not convert a published subconvex
bound for $L$ into the required cancellation for powers of its
reciprocal.

The progress is an additional family of strict power savings in the
actual long-conductor region, including configurations outside the
previous subpower cross-separation sectors. The smallest still missing
arithmetic statement for the fourth-moment route is the signed averaged
bound (6.4), or a stronger estimate that implies it. At higher orders the
far-separated singleton covariance remains as well.

## 8. Validation scope

The norm exponents, the two exact gains, the original-factor balances,
and the displayed cutoff comparisons were checked with exact rational
arithmetic. The analytic argument is the written proof using (WU) and
(SO). Neither finite arithmetic nor an independent check of these
adapters would newly prove those published input theorems, certify a
global arithmetic moment, or constitute a proof-assistant formalization.
