# Fourth-moment attack: a structured two-Poisson extension and the remaining conductor barrier

Status: proposed research mathematics. Sections 2–5 give complete algebraic and analytic adapters conditional on the precisely named imported inputs. Section 8 proves weaker general moment bounds from the imported zero-free region and second moment. The desired diagonal-size fourth moment, the exponent 17/24, and the diagonal-size general 2k-th moments are **not proved** here.

Scope: the exact sextic Möbius family over K = Q(sqrt(-3)), with fixed finite-order character nu, fixed bad-prime set S, and fixed smooth compactly supported tests. The row range includes all nonzero rows, in particular sixth powers. No exceptional rows are removed.

Source: OpenAI, October 5 manuscript, `paper2.tex`, imported at commit `adc7f1241b42e322a6451854ab7e4b4c146bf78a`, locally at `riemann/standalone/2026-10-07-openai-quasi-riemann-import/upstream/preprints/The-Quasi-Riemann-Hypothesis-October-5-2026/build/paper2.tex`. Exact source interfaces: `eq:crt-a` (line 850), `eq:energy` (946), `lem:remove-exclusions` (965), `prop:poisson-reduction` (1000), `prop:canonical` (1261), `eq:T` (1289), `prop:R` (1316), `lem:cube-reduction` (1345), `prop:transfer` (1483), and the full two-Poisson proof (2230–2665). Source line numbers refer to that pinned file.

Validation boundary: the new adapters are mathematical deductions from the imported arithmetic identities, Poisson formula, smooth separation, and stated canonical theorem. They do not independently verify the upstream cubic-theta reflection theorem. No Lean build or numerical verification of zeros is involved.

## 1. The target and a useful change of emphasis

Write N for the ideal norm, and use the source's chosen primary generators when evaluating symbols. Put

\[
A_u(D)=\sum_{(n,S)=1}\mu_K(n)\nu(n)\chi_n(u)W(Nn/D).
\]

The desired fourth moment is

\[
\sum_{0<Nu\le D^{1+\theta}}|A_u(D)|^4
\ll_{W,\nu,S,\theta,\epsilon}D^{3+\theta+\epsilon},
\qquad\text{for every fixed small }\theta>0.                 \tag{1.1}
\]

The preceding packet's exact sixth-power prime recursion would then give the limiting exponent 17/24. It is essential that (1.1) include the sixth-power rows and hold for every test required by the Mellin continuation argument.

For a squarefree c, the earlier exact common-factor reduction uses

\[
B_{c,u}(X)=\sum_{\substack{ab\text{ squarefree}\\(ab,cS)=1}}
\mu_K(ab)\nu(ab)\chi_{ab}(u)W(Na/X)W(Nb/X).                \tag{1.2}
\]

A sufficient estimate is

\[
\sum_{0<Nu\le H}|B_{c,u}(X)|^2\ll D^\epsilon H X^2,
\quad H=D^{1+\theta},\quad 1\le X\le D,\quad Nc\ll D,       \tag{1.3}
\]

uniformly in c. It supplies (1.1) by the harmonic common-factor sum. The new work below improves the understanding of the analytic input (1.3): the *two-Poisson transfer* does extend to balanced squarefree divisor weights. The completed theta reflection and the unfavorable initial conductor ratio remain separate obstacles.

## 2. Uniform moving exclusions for the original second moment

This is a useful fully proved adapter; it does not give (1.3).

### Proposition 2.1

Assume the imported canonical theorem and its Poisson reduction. Fix theta > 0, C > 0, and fixed nu, S, W. Let H = D^(1+theta), D >= 2. Uniformly for 1 <= X <= D and integral q with Nq <= D^C,

\[
\sum_{0<Nu\le H}\left|
\sum_{(n,qS)=1}\mu_K(n)\nu(n)\chi_n(u)W(Nn/X)
\right|^2\ll D^\epsilon H X.                              \tag{2.1}
\]

The same estimate, with an adjusted fixed constant, holds for X in a fixed interval [c,1].

**Proof of the unexcluded estimate at these scales.** In `prop:poisson-reduction`, replace the source's column length D by X, but retain the present D as the polynomial reference parameter in `prop:canonical`. Its initial scales become

\[
Y=X/(BF),\quad\mathcal H\ll X^2/(HB^2),\quad\Sigma=YF=X/B.
\]

Consequently

\[
\mathcal H/\Sigma\ll X/(HB)\le D^{-\theta}.
\]

For sufficiently large D this satisfies the canonical hypothesis with kappa = theta/2, whenever the child ranges are nonempty and at least one. All scales are polynomially bounded in D. The proof of the reduction uses no other requirement that H be exactly a power of the particular smaller X: its arithmetic and smooth-kernel formulas remain identical. The initial diagonal is O(H), after normalization by X, and the same proof gives the unexcluded bound O(D^epsilon H X). The source's handling of bounded scales covers the remaining cases. This also follows by reading its displayed proof with the three scales left independent.

**Proof of uniform exclusion removal.** Set a_u(n) = mu_K(n) nu(n) chi_n(u), with its zero extension. The elementary Euler-factor identity gives, coefficient by coefficient,

\[
\sum_{(n,qS)=1}a_u(n)W(Nn/X)
=\sum_{d:\ p\mid d\Rightarrow p\mid q}
\nu(d)\chi_d(u) A_u(X/Nd).                                \tag{2.2}
\]

The right side is finite on the support of W. Its validity includes primes dividing the row: their character value is zero, so the associated local factors equal one on both sides. Minkowski and the just-proved unexcluded estimate yield

\[
\|A^{(q)}(X)\|_{\ell^2(u\le H)}
\ll D^{\epsilon/4}(HX)^{1/2}
\prod_{p\mid q}(1-(Np)^{-1/2})^{-1}.                        \tag{2.3}
\]

The finitely many scales X/Nd below one but meeting the support satisfy the same square-root bound with a fixed support-dependent constant, because they lie in a fixed compact subinterval of (0,1].

For every eta > 0,

\[
\prod_{p\mid q}(1-(Np)^{-1/2})^{-1}\ll_\eta (Nq)^\eta.
\]

Indeed for sufficiently large Np each local factor is at most (Np)^eta; the remaining fixed finite primes contribute a constant. Choose eta sufficiently small in terms of epsilon and C, then square (2.3). This proves (2.1). No implied constant is allowed to depend on the moving q. \(\square\)

### A proved but insufficient bound for B

Cauchy–Schwarz in a, followed by (2.1) with q = ac, gives

\[
\sum_{0<Nu\le H}|B_{c,u}(X)|^2\ll D^\epsilon H X^3.        \tag{2.4}
\]

Here Na is O(X), so N(ac) is polynomial in D as required. This is one full power of X short of (1.3). Combined with the common-factor decomposition of A_u(D)^2, its convergent sum of (Nc)^(-3/2) gives only the already available fourth-moment estimate O(D^(3+epsilon)H). Thus the exclusion adapter is useful, but the Cauchy step loses precisely the cancellation we need.

## 3. Exact residual-coefficient stability through two Poisson steps

Let a_xi(n) denote the source's normalized cubic Gauss-sum coefficient. For the moment, insert an arbitrary function v(n) into the inner sum of the source's `eq:smoothed-energy`; assume it is supported on a fixed compact norm interval times L. No claim of automorphy is made for these new coefficients.

### Lemma 3.1: the arithmetic identity

In the first transfer calculation, the source substitutions n_i = C u_i and u_i = t x_i change the residual factor into

\[
v(Ct x_1)\overline{v(Ct x_2)}.                             \tag{3.1}
\]

Thus its positive intermediate form is exactly the source's Q, with the summand P_(C,d,t)(y;U) replaced by

\[
\sum_n^*\mu(n)\xi_1(n)\mathbf1_{(n,t)=1}
\overline{\chi_n(y)}\chi_n(C)^4\chi_n(d)
v(Ctn)U(Nn/\ell).                                         \tag{3.2}
\]

In the second Poisson calculation, splitting its common divisor g and then the coprimality divisor w gives

\[
v(Ctgw n_1)\overline{v(Ctgw n_2)}.
\]

The source's output labels r = tg/e and f' = Cew satisfy the exact ideal identity

\[
Ctgw=rf'.
\]

Hence the residual output is

\[
\boxed{v(rf'n_1)\overline{v(rf'n_2)}}.                     \tag{3.3}
\]

It is identical for every preimage of the same (r,f',k'). Therefore the source's signed regrouping, performed **before absolute values**, is unchanged. At each p dividing f', its local coefficient is still

\[
(1+\mathbf1_{p\mid k'})-\mathbf1_{p\mid k'}
-\mathbf1_{p\nmid k'}=\mathbf1_{p\mid k'}.
\]

In particular the output still satisfies f' | k', and its exact outer coefficient is the source's

\[
\frac{c_I\Sigma}{L^2}N(r)\tau_{\rm div}(r).
\]

All character zero extensions and the exclusion (n,r)=1 remain present. This proves the identity, because all other factors are exactly those computed in `eq:paired-first-gauss`, `eq:common-poisson-output`, and the regrouping in `lem:second-transfer`. These are finite arithmetic sums, so inserting and carrying v introduces no exchange-of-limit issue. \(\square\)

**Important limitation for arbitrary v.** Formula (3.3) is not by itself a closed iterative theorem. The next first-Poisson map (f,h) -> hf^2 retains only hf^2; an arbitrary v(rfn) still depends on the lost f. The next section proves that the special balanced divisor weights can be separated without paying a polynomial number of f choices.

## 4. Balanced divisor weights form a closed transfer class

For A,B > 0 and a fixed smooth compactly supported bivariate test V, define

\[
v_{A,B,V}(n)=\sum_{ab=n}V(Na/A,Nb/B).
\]

Only squarefree n occur in the following family, so a,b are automatically squarefree and coprime. Put L = AB and define

\[
\mathcal E_2(\mathcal H,A,B,F;\xi,V)
=\frac1{LF}\sum_{F\le Nf<2F}^{*}\sum_{0<Nk\le\mathcal H}
\left|\sum_n^*a_\xi(n)\chi_n(k)\chi_n(f)^4
v_{A,B,V}(n)\right|^2.                                    \tag{4.1}
\]

The source bad-prime restrictions apply to every starred ideal. An added subscript (r) means the extra restriction (n,r)=1. Tests range over fixed compact rectangles in (0,infinity)^2; empty factor ranges may be discarded. Factor scales smaller than a fixed support-dependent constant give empty sums, so all nonempty scales considered below are polynomially bounded in the reference D.

### Lemma 4.1: exclusion removal in this class

For squarefree r with Nr <= D^C and all relevant polynomially bounded scales,

\[
\mathcal E_{2,(r)}(\mathcal H,A,B,F;\xi,V)
\ll D^\epsilon
\sum_{d\mid r}\sum_{d_1d_2=d}
\mathcal E_2(\mathcal H,A/Nd_1,B/Nd_2,FNd;\xi,V).           \tag{4.2}
\]

The implied constant depends only on epsilon, C and the fixed source data. This inequality deliberately retains the displayed finite divisor sums; they too have subpower cardinality and can subsequently be replaced by a supremum at a further subpower cost.

**Proof.** Insert sum_(d|r,d|n) mu(d), write n=dm, and use the source identity

\[
a_\xi(dm)=a_\xi(d)a_\xi(m)\chi_m(d)^4
\quad ((d,m)=1).
\]

The zero of chi_m(d)^4 enforces (m,d)=1 after extending the m sum. If (d,f) is nontrivial, the term vanishes. Otherwise the new auxiliary twist is df, still squarefree. On (m,d)=1, every factorization of dm is uniquely obtained by choosing d=d_1d_2 and m=m_1m_2. Hence

\[
v_{A,B,V}(dm)=\sum_{d_1d_2=d}
v_{A/Nd_1,B/Nd_2,V}(m).
\]

Each exterior coefficient has modulus at most one. Cauchy–Schwarz costs at most sum_(d|r) tau(d), which is D^epsilon after assigning a smaller local epsilon. For fixed d, the map f -> df is injective and its image can be enlarged by positivity to the new squarefree f range. The normalizer is **exactly preserved**:

\[
(A/Nd_1)(B/Nd_2)(FNd)=ABF.
\]

This proves (4.2), including the row zeros. \(\square\)

### Proposition 4.2: structured transfer theorem

Use the source's nonnegative smoothing Phi in the row k. Let A_2(V) be (4.1) with sum_k Phi(Nk/Hcal) in place of the sharp k range. Fix C_0 and suppose

\[
1\le\mathcal H,L,F,\Sigma\le D^{C_0},\qquad L=AB,
\qquad \max(\mathcal H,LF)\le\Sigma.                       \tag{4.3}
\]

For every integer m >= 0 and epsilon > 0 there is a finite integer J such that

\[
\boxed{\mathcal A_2(V)
\ll D^\epsilon\Sigma\|V\|_{C^J}^{2}
\left(1+\sup\frac{\mathcal E_2(\mathcal H',A',B',F';\xi',U)}{\Sigma'}\right)}.
                                                                    \tag{4.4}
\]

Here Sigma' = A'B'F', the tests U lie on a fixed enlarged compact rectangle, have C^m norm at most one, and the output scales satisfy exactly the source's geometric restrictions

\[
\mathcal H'\le\frac{\mathcal H L}{\Sigma F},\qquad
\frac{\mathcal H'}{\Sigma'}\le\frac{\mathcal H}{\Sigma},\qquad
\Sigma'\le L.                                             \tag{4.5}
\]

The child total column scale A'B' and F' are at least one. A factor axis may be shorter than one only within a fixed support-dependent compact range; equivalently one may rescale that axis and its test by a fixed constant. The derivative order and constants may depend on m, C_0, epsilon, the support rectangle, Phi, and the fixed source data. They do not depend on a moving ideal or row. Empty supremums are zero.

**Proof.** Choose once a scalar smooth cutoff supported on a compact total-norm interval and equal to one on products of the two support intervals of V. Insert it as the source's total-norm test W, and treat v_(A,B,V) as the residual arithmetic coefficient. Since |v(n)| <= tau(n)||V||_infinity, every source diagonal/zero-frequency bound is unchanged up to D^epsilon ||V||_infinity^2. For the off-diagonal terms apply Lemma 3.1. No factor allocation or absolute value is taken until its complete signed preimages have been regrouped.

Now fix a retained r and a dyadic block F_0 <= Nf' < 2F_0 from the source's regrouped output. The remaining column indices are coprime to rf', and r,f' are squarefree and coprime. Therefore

\[
v_{A,B,V}(rf'n)
=\sum_{r_1r_2=r}\sum_{f_1f_2=f'}\sum_{n_1n_2=n}
V\left(\frac{N(r_1f_1n_1)}A,
       \frac{N(r_2f_2n_2)}B\right).                       \tag{4.6}
\]

Every factorization is unique; no allocation is discarded. The coupled post-Poisson kernel need not be positive. Accordingly first perform the four-coordinate Mellin separation described below, so each term is a left/right bilinear product of column sums. Only then apply Cauchy–Schwarz in the row and over allocations of r and f'. This costs a fixed product of divisor functions, hence a subpower. Split each f_i norm into a dyadic block F_i <= Nf_i < 2F_i. There are only logarithmically many pairs. For fixed r_1,r_2,F_1,F_2, set

\[
\widetilde A=A/(Nr_1 F_1),\qquad
\widetilde B=B/(Nr_2 F_2),\qquad
\eta_i=Nf_i/F_i\in[1,2).
\]

The bivariate profile is V(eta_1 x,eta_2 y). Its derivatives on the resulting fixed compact rectangle are uniformly bounded by finitely many derivatives of V. Use Mellin/Fourier separation in the two positive coordinates x,y, taking a uniform bound over eta_1,eta_2. This turns the profiles into common bivariate tests, independent of the actual f_i, at a cost bounded by a finite Sobolev norm of V. In particular their Mellin coefficients satisfy, for every fixed even q,

\[
\sup_{\eta_1,\eta_2\in[1,2]}|b_{\eta_1,\eta_2}(s,t)|
\ll_q\|V\|_{C^q}(1+|s|+|t|)^{-q}.
\]

The coefficient functions of the Mellin integral may depend on f_i, but this uniform decaying majorant is used **before** integration and the row norm. Thus their row dependence does not invoke an arbitrary arithmetic-coefficient theorem. The square-sum inequality follows by Minkowski and then Cauchy–Schwarz in the row, exactly as in the source's `lem:smooth-mean-square`.

For each f', the number of its factorizations f'=f_1f_2 is at most tau(f'). After the separation, all these terms are bounded by the same common-test energy at that f'. Thus their sum is at most a subpower times the full f'-energy. Crucially this pays **tau(f')**, not the number F_0 of possible auxiliary ideals. No arbitrary divisor weight is left on the n column.

To make the source's normalizers exact, fix its r block R <= Nr < 2R and its X' = L/(RF_0), Sigma' = L/R. We have

\[
\widetilde A\widetilde B=L/(Nr F_1F_2).
\]

Replace the first factor scale by

\[
A'=\lambda\widetilde A,\quad B'=\widetilde B,
\qquad\lambda=\frac{Nr F_1F_2}{RF_0}.
\]

The dyadic support implies lambda lies in a fixed compact interval, for example [1/4,4]. This change is absorbed into the first coordinate of the smooth profile. It makes A'B'=X' and A'B'F_0=Sigma' exactly. The profile may depend on the frozen r and the dyadic labels; its smooth norms are still uniform, and the supremum in (4.4) is uniform in all factor scales.

The extra condition (n,r)=1 is removed by Lemma 4.1 **after** (4.6). For each divisor d and its allocation d_1d_2=d, the child total length becomes X'/Nd and the auxiliary scale becomes F_0 Nd. Hence Sigma' is unchanged. The source's consequence of f'|k', `eq:child-column-lower-bound`, gives X'/Nd >= 1 for every d|r. Thus every retained child satisfies the required total-column domain. The source's row scale is

\[
\mathcal H'=\frac{\mathcal H L}{\Sigma F R^2},\qquad
\frac{\mathcal H'}{\Sigma'}=\frac{\mathcal H}{\Sigma F R},
\]

which proves all of (4.5). Exclusion removal does not change these identities.

For completeness, the smooth separation remains valid for the kernels coupling the two product columns. Express each product column by its two factor coordinates, so the coupled kernel has four positive coordinates. Choose a Mellin decay order q > 2m+4, for instance q=2m+6. The relevant integral is bounded by

\[
\int_{\mathbb R^4}
\frac{(1+|s_1|+|s_2|)^m(1+|t_1|+|t_2|)^m}
{(1+|s_1|+|s_2|+|t_1|+|t_2|)^q}
\,d\boldsymbol s\,d\boldsymbol t<\infty.
\]

The dependence of the source Fourier kernel on the total product and its row parameter has the same uniform derivative bounds as before. Its four-coordinate Mellin coefficient has the same type of uniform majorant, now with exponent q in four frequency variables. For each separated left/right bilinear term, Cauchy–Schwarz in the full row index bounds the product by the common child-energy supremum. This is the justified order of operations even when the unsplit kernel has either sign. Enlarging J to cover these derivatives and the first source separation proves the asserted finite-norm dependence. No height or moving arithmetic label enters J.

It remains to sum the retained r block. Its coefficient is O(Sigma R/L^2), there are O(R) ideals r, and the corresponding unnormalized child energy is at most a subpower times (Sigma')^2 times the supremum. The factors cancel exactly:

\[
\frac{\Sigma R}{L^2}\,R\,(L/R)^2=\Sigma.
\]

All divisor allocations, exclusion divisors, and dyadic subdivisions have a fixed total number of subpower/logarithmic losses. Assign them smaller epsilons so their product is at most the requested D^epsilon. The zero-frequency term was already bounded by D^epsilon Sigma||V||^2. This proves (4.4). \(\square\)

This is a new extension of the *transfer* interface. It does not extend the source's completed theta transformation to these coefficients.

### Corollary 4.3: every fixed number of squarefree divisor factors

For a fixed j>=1 replace v_(A,B,V)(n) by

\[
v_{\boldsymbol A,V}(n)=\sum_{a_1\cdots a_j=n}
V(Na_1/A_1,\ldots,Na_j/A_j),\qquad L=\prod_{i=1}^j A_i.
\]

The same transfer statement holds with this j-factor family and Sigma'=F' product_i A_i'. Its constants and finite smoothness order may depend on j.

**Proof.** Lemma 3.1 is independent of j. Allocate each squarefree prime of r and f' among j factors after the signed regrouping; there are at most tau_j(r)tau_j(f') allocations. For exclusion removal allocate d among d_1,...,d_j and replace A_i by A_i/Nd_i and F by FNd, preserving the normalizer exactly. All fixed-order ideal divisor functions are subpower. The coupled kernel has 2j positive coordinates; choose an even Mellin decay order q>2m+2j, so its analogue of the displayed four-dimensional integral converges. A bounded rescaling of one factor axis again fixes the total child length exactly. The source r-block summation and all inequalities (4.5) are unchanged. These observations reproduce every step of Proposition 4.2 and prove the corollary. This concerns the squarefree product-column face; repeated-prime incidence components of a general moment must also be retained, as in Section 9 below. \(\square\)

## 5. Why the same extension is not yet a fourth-moment theorem

### 5.1 The completed input is missing

The source's completed sum `eq:T` may be formally defined for completely multiplicative Psi. Its reflection estimate `prop:R`, however, is proved only for the character twist

\[
\Psi_k(n)=\xi(n)\chi_n(k)\chi_n(f)^4.
\]

A divisor allocation weight is not such a twist. In the unsmoothed squarefree model its coefficient is 2^(omega(n)); inserting this into a theta coefficient changes the arithmetic sequence, not merely its smooth norm profile. The arbitrary complex coefficients allowed by the quadratic large sieve occur **after** a valid theta reflection; they do not authorize replacing the input theta coefficients.

Consequently Proposition 4.2 does not supply the balanced counterpart of the source's `lem:cube-reduction`. To obtain a canonical balanced theorem by the same induction, one would need a proved completed/cube-removal estimate of the form

\[
\mathcal E_2(\mathcal H,A,B,F)
\ll D^\epsilon\left[\Sigma+
\sup_{\substack{Nb>H_c\\L_b=AB/(Nb)^3>1}}
\mathcal E_2(\mathcal H,A_b,B_b,F)\right],
\quad A_bB_b=L_b,
\]

with the source's cutoff H_c^3=min(AB,(AB)^2/Hcal^2), fixed smooth-norm control, and the literal balanced coefficient family. This displayed estimate is **unproved**. If it held, Proposition 4.2 would close the source's finite induction in the positive-gap domain Hcal <= ABF D^(-kappa), with base case bounded by ideal divisor counting. It still would not cover the fourth-moment initialization below.

### 5.2 The initial conductor ratio is independently unfavorable

For c=1 and factor length X, the product column r=ab has total length Q=X^2. On the component where a,b,a',b' are pairwise coprime, the row character in |B|^2 is primitive with conductor

\[
aa'bb',\qquad N(aa'bb')\asymp X^4.
\]

This follows directly from the source's local sextic character primitivity and CRT, used in its `lem:poisson`. The nonzero row-Poisson frequencies therefore occupy norm scale

\[
\mathcal H\asymp X^4/H.
\]

At X=D and H=D^(1+theta),

\[
\mathcal H\asymp D^{3-\theta},\qquad
\Sigma=Q=D^2,\qquad
\mathcal H/\Sigma\asymp D^{1-\theta}.                      \tag{5.1}
\]

The canonical domain requires the opposite inequality, Hcal/Sigma <= D^(-kappa). Keeping the two axes visible does not change this literal primitive conductor. Any tensor argument must exploit an additional cancellation after Poisson or introduce a genuinely different transformation; merely renaming the axes does not reduce the dual range.

The same bookkeeping at a fixed 2k-th moment has total column length Q=D^k and initial dual range D^(2k)/H, hence ratio D^k/H. For H=D^(1+theta) this is D^(k-1-theta). The obstruction strengthens with k.

This is an obstruction to **this sufficient proof route**, not a counterexample to (1.1) or (1.3). In particular it does not justify claiming the desired moment is impossible.

### 5.3 Reflecting each factor separately after Cauchy does not solve it

The identity a_xi(ab)=a_xi(a)a_xi(b)chi_b(a)^4 holds for coprime squarefree a,b. Freeze a of norm about X. The completed b-factor has auxiliary twist f=a and column length X. Applying the source's completed estimate over rows k of norm at most Hcal costs

\[
\mathcal H+\mathcal H^2 Na/X\asymp\mathcal H+\mathcal H^2.
\]

If C_k denotes the sum over a of these completed b-factors, with coefficients of modulus at most one and a fixed smooth weight, Cauchy and the O(X) choices of a give the rigorous upper bound

\[
\sum_{Nk\le\mathcal H}|C_k|^2
\ll D^\epsilon X^2(\mathcal H+\mathcal H^2).               \tag{5.2}
\]

The uncompleted b factor has an additional normalization sqrt(X). Formula (5.2) is therefore far from a diagonal balanced estimate at the scales (5.1). A successful two-factor reflection would need to retain and estimate the coupling in a, not apply this Cauchy step. This calculation proves failure of the proposed factorwise bound, not a universal impossibility theorem for a coupled transformation.

## 6. What is and is not ruled out

There is no diagonal counterexample here to the fixed-nu moment (1.1). The preceding packet counted the full algebraic sextic diagonal at every fixed k and obtained O(D^(k+epsilon)), compatible with the target D^k H. A lower bound from just the diagonal cannot be asserted for a finite row average without controlling the off-diagonal terms.

There is, however, a simple counterexample to replacing the Möbius/divisor structure by *arbitrary bounded coefficients* in the short-row target. For a squarefree product-column interval of length Q, take positive coefficients on the squarefree ideals and the row u=1. The column sum has size comparable to Q, so its squared modulus is comparable to Q^2. A proposed bound H Q D^epsilon at H=Q^(1/2+o(1)) fails already on this single row. The equivalent arbitrary-residual version is obtained by taking v(n)=overline(a_xi(n)) on the fixed ray and squarefree support. Thus a proof of (1.3) must exploit the literal Möbius/divisor coefficient and cannot follow from an unrestricted short-row large sieve.

An entirely uniform extension of the dual conclusion E_2 << D^epsilon Sigma to arbitrary Hcal >> Sigma is also false: take A=B=F=1 and a fixed test isolating the unit ideal in both factor coordinates. Then the column is identically one at every row, and E_2 is comparable to Hcal while Sigma=1. This does **not** establish a lower bound for the large balanced family A=B=D at Hcal about D^3. For that literal family, no contradiction to an improved estimate is proved here.

Likewise sixth-power rows cannot be discarded and patched with the previous pointwise Möbius exponent beta: their contribution returns that same beta in principal-member extraction. They carry part of the very cancellation that (1.1) is meant to prove.

## 7. The next narrowly specified analytic tasks

The transfer-coefficient difficulty has been reduced to a proved adapter (Proposition 4.2). Two remaining tasks are distinct:

1. Construct and bound a coupled two-factor cubic-theta completion whose squarefree face is exactly the balanced coefficient in (4.1), keeping its cross-symbol chi_b(a)^4. Prove a cube-removal inequality with controlled factor scales. One-factor completion followed by Cauchy gives only (5.2).
2. Produce a cancellation estimate in the fourth-moment initial Poisson formula that reaches the long dual range Hcal about D^3 at product length D^2. This must avoid the current reduction to a positive dual energy requiring Hcal < Sigma. Merely extending the canonical coefficient class is insufficient.

An alternative is a direct bilinear row estimate for (1.2), retaining the balanced allocations through the entire signed four-column expansion. The exact conductor calculation in Section 5 applies to its pairwise-coprime component, so such a proof must name the additional cancellation it uses.

The strongest bound for B actually established here is (2.4), not (1.3). The new result with potential reuse is the complete structured transfer extension (4.4), together with uniform moving-exclusion removal. Section 8 also proves a weaker improved moment from the already imported zero-free region. No claim of 17/24 attainment is made.

## 8. A genuine weaker moment bound, and its exact saturation

The imported fixed zero-free half-plane does give a stronger moment than the trivial pointwise bound used in (2.4). The conductor uniformity needs proof: a fixed-character implied constant cannot simply be reused as u varies.

### Lemma 8.1: uniform subpower reciprocal bounds from a fixed half-plane

Fix beta in (1/2,1). Assume every finite-order Hecke L-function over the fixed field K has no zero in Re(s)>beta. For every delta>0 and epsilon>0,

\[
|L(\sigma+it,\chi)^{-1}|
\ll_{K,\beta,\delta,\epsilon}
[N\mathfrak q\,(2+|t|)]^\epsilon,
\qquad \sigma\ge\beta+\delta,                              \tag{8.1}
\]

uniformly in finite-order characters of modulus q. The reciprocal is interpreted analytically at the pole of a principal L-function, where it is zero. It suffices to consider delta with beta+delta<1, as the larger-real-part cases follow directly or by the same proof.

**Proof of a polynomial bound needed below.** First take a primitive nonprincipal character with conductor q. K has class number one. Its values on principal ideals define a periodic multiplicative function on the Eisenstein lattice modulo q, invariant under units, with zero sum on a complete residue cell. Each ideal is represented by six nonzero generators. A principal ideal q has a lattice fundamental cell with diameter O(sqrt(Nq)) and O(Nq) lattice points, since multiplication by a generator is a Euclidean similarity. Cover a disk of radius sqrt(x) by these cells. The complete cells cancel; the boundary cells contribute at most

\[
\left|\sum_{N\mathfrak a\le x}\chi(\mathfrak a)\right|
\ll_K\sqrt{xN\mathfrak q}+N\mathfrak q
\ll_K N\mathfrak q\sqrt x\qquad(x\ge1).                   \tag{8.2}
\]

The cell sum is zero because a nonprincipal character on the residue-unit group has zero total and its nonunit values vanish. Unit invariance ensures that nonprincipality as a Hecke character is exactly nonprincipality of this residue character here. For any fixed a>1/2, partial summation therefore continues the series to Re(s)>1/2 and gives

\[
|L(s,\chi)|\ll_{K,a}N\mathfrak q\,(1+|s|)
\quad(\Re s\ge a).
\]

For the primitive principal character, elementary disk counting gives the same polynomial bound after removing the pole at one. Specifically use

\[
\widetilde L(s)=\frac{s-1}{s+1}\zeta_K(s).
\]

It is holomorphic and nonzero in Re(s)>beta under the assumed zero-free statement, including s=1. Its growth in any fixed right strip is polynomial in 2+|t|. This follows directly from the ideal-count asymptotic with O(sqrt(x)) boundary error. For nonprincipal characters write Ltilde=L.

**Bound the analytic logarithm.** On Re(s)>beta choose the branch g(s)=log Ltilde(s) agreeing with the Euler branch at Re(s)>1; the rational pole-removal factor in the principal case has an equally bounded branch there. This exists since the half-plane is simply connected and Ltilde has no zeros. Choose fixed beta<a<sigma<b with b>1. The polynomial bound just proved, Borel–Caratheodory on disks centered at 2+it and extending to a slightly leftward line still to the right of beta, and the bounded value of g at the center imply

\[
|g(a+it)|\ll \log[N\mathfrak q(2+|t|)],
\qquad |g(b+it)|\ll_b1.                                  \tag{8.3}
\]

All disk radii are fixed in terms of beta and the desired margin. For example, choose the left edge of the outer disk between beta and a; the point a+it then lies in a strictly smaller concentric disk. The bound on Re g is the logarithm of the polynomial L-bound, so Borel–Caratheodory gives exactly (8.3), uniformly in q and t.

Fix t_0 and apply the three-lines theorem on [a,b] to g(s) exp((s-it_0)^2). This function decays vertically, and the boundary estimates in (8.3) imply boundary suprema O(log Q) and O(1), respectively, where Q=Nq(2+|t_0|). The logarithmic growth away from t_0 is absorbed by the Gaussian. Consequently

\[
|g(\sigma+it_0)|\ll (\log Q)^\omega,
\qquad \omega=\frac{b-\sigma}{b-a}<1.                     \tag{8.4}
\]

For beta+delta<=sigma<=b one can choose a and b uniformly so that omega is bounded away from one. For sigma>=b>1 the Euler product already bounds the reciprocal uniformly; no interpolation outside the strip is used. Exponentiating -Re g inside the strip gives

\[
|\widetilde L(s)^{-1}|\le\exp(C(\log Q)^\omega)
\ll_\epsilon Q^\epsilon.
\]

In the principal case L^(-1)=(s-1)/(s+1) times Ltilde^(-1), and the rational factor is bounded in the relevant half-plane. Finally, if chi is imprimitive, its reciprocal differs from its primitive reciprocal by

\[
\prod_{p\mid\mathfrak q,\ p\nmid\mathfrak q_0}
(1-\chi_0(p)(Np)^{-s})^{-1}.
\]

Its absolute value is at most product_(p|q)(1-(Np)^(-sigma))^(-1), which is O_epsilon((Nq)^epsilon) by the same fixed-small-prime argument used in Proposition 2.1. Redistribute epsilon to prove (8.1). \(\square\)

### Proposition 8.2: all fixed moments at a weaker exponent

Assume the zero-free hypothesis of Lemma 8.1 and the imported second moment. For each fixed integer k>=1, each fixed theta>0, H=D^(1+theta), and every epsilon>0,

\[
\boxed{\sum_{0<Nu\le H}|A_u(D)|^{2k}
\ll_{k,\theta,W,\nu,S,\beta,\epsilon}
H D^{1+2(k-1)\beta+\epsilon}.}                             \tag{8.5}
\]

**Proof.** Reciprocity, including the fixed ray-class factor in `eq:recip`, realizes n -> nu(n) chi_n(u) as a finite-order Hecke character whose modulus norm is O_(nu,S)(Nu), with its literal imprimitive zero extensions. There are only finitely many fixed ray corrections. The reciprocal Dirichlet series of the coefficients in A_u is therefore covered by Lemma 8.1; all excluded primes are included in its modulus or the fixed S.

Mellin inversion gives A_u(D) as the integral of the reciprocal L-function times MW(s)D^s. Shift from a line to the right of one to Re(s)=beta+delta. The reciprocal is holomorphic in the intervening half-plane, even for the principal character, and (8.1) together with rapid Mellin decay justifies the shift and absolute integral bounds. Uniformly for Nu<=H, this proves

\[
|A_u(D)|\ll D^{\beta+\delta}(1+H)^\eta.                   \tag{8.6}
\]

Choose delta and eta small in terms of the final epsilon, theta, and k. Multiply the imported second moment bound by max_u |A_u(D)|^(2k-2). This gives (8.5). It includes every row and has no moving-character implied constants. \(\square\)

Taking the previously derived conditional beta=139999/160000 yields the explicit fourth moment

\[
\sum_{0<Nu\le H}|A_u(D)|^4
\ll H D^{219999/80000+\epsilon},
\qquad\frac{219999}{80000}=2.7499875.                     \tag{8.7}
\]

The desired fourth moment would have exponent 2 in place of 2.7499875. Thus (8.7) is a real improvement over the trivial exponent 3, but remains far short of (1.1).

### Exact extraction saturation

For a moment bound H D^rho with 2k-th power, the previously proved prime recursion yields amplitude exponent

\[
\frac{\rho}{2k}+\frac{5h}{12k},\qquad H=D^h.
\]

Substituting rho=1+2(k-1)beta and letting h approach one gives

\[
\boxed{\beta+\frac{11/6-2\beta}{2k}.}                    \tag{8.8}
\]

When beta<11/12 this lies strictly above beta at every finite k and approaches beta from above. For k=2 and beta=139999/160000 it equals

\[
\frac{859997}{960000}=0.8958302083\ldots.
\]

Therefore this weaker general moment theorem cannot improve the already known boundary, even by letting k grow. It isolates the missing issue: interpolation between a second moment and a uniform pointwise estimate does not create the extra cancellation required for the diagonal-size moments.

## 9. A general incidence decomposition: repeated primes have only a harmonic summation cost

The earlier fourth-moment common-factor decomposition extends to every fixed moment without a new polynomial loss. This is a conditional reduction of the analytic target, not a proof of that target.

Fix k>=2. For q squarefree and positive factor scales X_i, define the squarefree-product family

\[
\mathcal B_{q,u}(\boldsymbol X)=
\sum_{\substack{a_1\cdots a_k\text{ squarefree}\\
 (a_1\cdots a_k,qS)=1}}
\mu_K(a_1\cdots a_k)\nu(a_1\cdots a_k)\chi_{a_1\cdots a_k}(u)
\prod_{i=1}^k W(Na_i/X_i).                                \tag{9.1}
\]

### Proposition 9.1

Let H=D^(1+theta), with theta fixed. Suppose, for every epsilon>0,

\[
\sum_{0<Nu\le H}|\mathcal B_{q,u}(\boldsymbol X)|^2
\ll D^\epsilon H\prod_i X_i,                             \tag{9.2}
\]

uniformly for 1/b<=X_i<=D and Nq<=(bD)^(k/2), with the fixed W supported on [a,b] and with harmless enlargement of b to at least one. Then

\[
\sum_{0<Nu\le H}|A_u(D)|^{2k}\ll D^{k+\epsilon}H.         \tag{9.3}
\]

The estimate must hold for unbalanced as well as balanced factor scales, and for the full row range H at every smaller factor scale. These are explicit hypotheses, not consequences of Proposition 4.2.

**Proof.** In an ordered k-tuple of squarefree ideals n_1,...,n_k, assign each prime p to its nonempty incidence set I={i:p|n_i}. Write c_I for the product of primes with that exact set. All c_I are squarefree and pairwise coprime. Fix the c_I for |I|>=2, write a_i=c_{ {i} }, and put

\[
d_i=\prod_{\substack{I\ni i\\|I|\ge2}}c_I,
\qquad q=\prod_{|I|\ge2}c_I,
\qquad X_i=D/Nd_i.
\]

Then n_i=d_i a_i, and the exact expansion is

\[
A_u(D)^k=
\sum_{\{c_I:\ |I|\ge2\}}^{\rm disjoint}
\left[\prod_{|I|\ge2}
\mu_K(c_I)^{|I|}\nu(c_I)^{|I|}\chi_{c_I}(u)^{|I|}\right]
\mathcal B_{q,u}(X_1,\ldots,X_k).                         \tag{9.4}
\]

All zero masks are exact. The exterior multiplier has modulus at most one, so Minkowski applies. A nonempty term has Nd_i<=bD, hence X_i>=1/b, and

\[
(Nq)^2\le\prod_{|I|\ge2}(Nc_I)^{|I|}
=\prod_i Nd_i\le(bD)^k.
\]

Thus (9.2) applies. Its square root bounds the summand by

\[
D^{\epsilon/2}H^{1/2}D^{k/2}
\prod_{|I|\ge2}(Nc_I)^{-|I|/2}.
\]

Discarding the pairwise-coprimality restriction in this nonnegative upper bound enlarges it. For every |I|>=3 the corresponding ideal sum converges, because |I|/2>1. For each of the binomial(k,2) sets with |I|=2, the ideal sum up to bD is O(log(2D)). Consequently

\[
\|A(D)^k\|_{\ell^2(u\le H)}
\ll D^{\epsilon/2}H^{1/2}D^{k/2}
\log(2D)^{\binom{k}{2}}.
\]

Square this and allocate a smaller epsilon in the hypothesis to absorb the logarithm. This proves (9.3). \(\square\)

The reduction makes two points precise. Higher moments do not fail merely because product columns contain repeated primes: at every fixed k their incidence components have only a harmonic/subpower recombination cost. The actual missing estimate is the squarefree k-factor mean square (9.2), with its exact masks, unbalanced scales, and uniform moving exclusion. Corollary 4.3 closes its two-Poisson coefficient bookkeeping, but Sections 5 and 8 explain why the existing analytic estimates do not supply its diagonal-size cancellation.
