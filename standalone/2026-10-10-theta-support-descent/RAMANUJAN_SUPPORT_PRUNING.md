# Regroup the Ramanujan terms before using the second reflection

**Status:** proposed component theorem, relative to the exact theta automorphy and cusp expansions named in [the opposite-derivative proof](OPPOSITE_DERIVATIVE_REFLECTION.md). This note gives an exact truncation of the completed standard infinity-cusp contribution, and Section 5 extends it to every source cusp using the proved adapter in [ALL_CUSP_REFLECTION.md](ALL_CUSP_REFLECTION.md). It does not prove a fourth or higher moment.

**Scope:** squarefree coprime primary ideals `a,k` outside the fixed bad set `S`; the full squarefree-index/cube-index sum on the good-primary standard face of PR #915; fixed smooth weights and fixed ray factors. The constants are uniform in the arithmetic labels and row norm. All local zeros, including primes dividing `k`, remain present.

**Sources:** PR #915, commit `9959364671f89b86f3992ec5ed5e19f804eb607b`, `COUPLED_THETA_COMPLETION.md`, Sections 1–3 and 6, and `NEGATIVE_BRANCH_DIRICHLET_SERIES.md`, equation (3.1). The new analytic input is Theorem 3.1 of the companion opposite-derivative proof in this packet. No zero-free assumption is needed for the truncation.

## 1. Use two local summands and keep the divisibility projection intact

For a good prime of norm `q`, the local Ramanujan polynomial is

\[
R_p(m)=-1+q\mathbf1_{p\mid m}.
\]

If `a` is squarefree, ordinary distributivity gives the exact identity

\[
\boxed{\quad
\prod_{p\mid a}R_p(m)
=\sum_{dg=a}\mu_K(g)N(d)\mathbf1_{d\mid m}.
\quad}                                                   \tag{1.1}
\]

Here `d,g` are squarefree and coprime. This is a signed identity, not a partition of the set of indices `m`.

On a theta coefficient `m=nb^3`, with `n` squarefree and `b` unrestricted, a prime divides `m` exactly when it divides `nb`. Thus

\[
\mathbf1_{d\mid nb}
=\sum_{ef=d}\mathbf1_{e\mid n}\mathbf1_{f\mid b}
                      \mathbf1_{(f,n)=1}.                \tag{1.2}
\]

The sum in (1.2) has exactly one nonzero summand whenever `d|nb`: assign every prime of `d` that divides `n` to `e`, and all remaining primes to `f`. It has no nonzero summands otherwise. The three-way allocation `a=efg` of PR #915 is therefore recovered by expanding the single projection in (1.1). Keeping that projection intact retains a finite periodic theta twist with a smaller modulus.

## 2. Define the literal completed projected component

Fix the ray character `rho` and the positive constant `c` from one fixed branch of PR #915's standard-face formula. Put

\[
\begin{aligned}
I_{k,a,d}(B)=\sum_n^*\sum_b
&\frac{\gamma_2(n)\rho(n)\vartheta(n)\alpha(n)\chi_k(n)^3
       \rho(b)^3\alpha(b)^3\chi_k(b)^3}
      {\sqrt{Nn}\,Nb}\;\mathbf1_{d\mid nb}\;
 V^\sharp\!\left(\frac{c\,Nn\,(Nb)^3 B}{(Na)^2(Nk)^2}\right),
\end{aligned}                                            \tag{2.1}
\]

where `n,b` are good primary indices, `n` is squarefree, `b` is unrestricted, and

\[
\vartheta(n)=\overline{\chi_n(\lambda)^2}.
\]

No condition involving `g=a/d` is imposed on `n` or `b`. Such a condition would change the negative Ramanujan term. The cube sum in (2.1) is complete. The transformed weight is the exact inherited transform of one fixed `V` with

\[
\operatorname{supp}V\subset[u,R]\subset(0,\infty).
\]

The standard-face part of the first reflected balanced completion is a fixed scalar times

\[
\frac1{\sqrt A}\sum_a^*
 \frac{\eta(a)\overline{\alpha(a)}^3\chi_k(a)^3}{\sqrt{Na}}
 W_1(Na/A)
 \sum_{dg=a}\mu_K(g)N(d) I_{k,a,d}(B).                  \tag{2.2}
\]

The scalar and `eta` have exactly the fixed-ray scope of the source; possible terms with `(a,k)>1` were already zero before reflection. The factor `(Na)^(-1/2)` in (2.2) comes from the product of the normalized Ramanujan factors and must not be removed.

## 3. Exact support theorem for every projected allocation

Choose a fixed `S`-supported modulus `M` large enough to encode the good-primary condition, `rho`, and all the fixed ray functions being considered. For each squarefree `d` coprime to `kS`, the function

\[
\phi_{k,d}(m)=\mathbf1_{m\text{ good primary}}\,
              \rho(m)\chi_k(m)^3\mathbf1_{d\mid m}       \tag{3.1}
\]

is periodic modulo `q=Mkd`. It preserves the nonunit zero at a prime of `k`; no primitivity convention is substituted. On `m=nb^3`, the last indicator is precisely the one in (2.1).

### Theorem 3.1. Uniform projected support cutoff

With `a=dg`, one has

\[
\boxed{\quad
(Ng)^2>81cR(NM)^2 B
\quad\Longrightarrow\quad
I_{k,a,d}(B)=0.
\quad}                                                   \tag{3.2}
\]

This is an exact identity for every permitted row `k`, not an average estimate. In particular (2.2) is unchanged when its divisor sum is restricted to

\[
Ng\le C_S\sqrt B,\qquad C_S=9\sqrt{cR}\,NM.             \tag{3.3}
\]

**Proof.** Use the opposite-derivative sum `S^+` of the companion note with

\[
X=\frac{(Na)^2(Nk)^2}{27cB},\qquad q=Mkd.
\]

Its exact standard-face coefficient identity, with the extra periodic projection (3.1), gives

\[
S^+_{\phi_{k,d}}(X;V^\sharp)=81i\,I_{k,a,d}(B).
\]

The companion support theorem makes this zero whenever `X>3R(Nq)^2`. Since `Nq=NM\,Nk\,Nd`, that inequality is exactly

\[
\frac{(Na)^2(Nk)^2}{27cB}
>3R(NM)^2(Nk)^2(Nd)^2,
\]

or (3.2). The factors involving the row `k` cancel. All fixed ray branches form a finite family, so a maximum of their constants gives one uniform cutoff if they are summed. No absolute-value estimate is taken over the additive translates: each individual second-reflection sum has empty compact support. This proves the claim. \(\square\)

### Consequences and the order of operations

If `supp(W_1)` is contained in `[u_1,v_1]` with `u_1>0`, the entire all-negative standard component (`d=1,g=a`) vanishes whenever

\[
u_1^2A^2>81cR(NM)^2B.                                    \tag{3.4}
\]

For balanced `A=B=D`, this holds for all sufficiently large `D`, uniformly in the dual row norm. More generally, every surviving projected component has

\[
Nd\ge\frac{Na}{C_S\sqrt B}.
\]

Thus at balanced factor lengths its positive-divisibility label has norm at least a fixed multiple of `D^(1/2)`.

The vanishing in (3.2) applies **after** all the `e,f` allocations in (1.2), all squarefree theta indices, and the full cube sum have been reunited for the fixed pair `(d,g)`. It does not assert that an individual `e,f` term or a separately truncated theta dyad vanishes. Apply this support theorem before the triangle inequality or a replacement of `V^sharp` by its decay majorant.

Any extra row-independent coefficient on the outer ideal `a` preserves this pointwise vanishing. In particular fixed-order divisor weights on that outer axis do not affect (3.2). This observation is about a component inside a completed higher-order construction; it does not construct or bound such a completion.

## 4. Why summing the components restores the large conductor

The support saving must not be promoted to a smaller conductor for the complete reflected polynomial. The local normalized additive Fourier transform, on a residue field of size `q`, gives

\[
\begin{array}{c|cc}
 &h=0&h\ne0\\\hline
-1&-1&0\\
q\mathbf1_{x=0}&1&1\\
-1+q\mathbf1_{x=0}&0&1
\end{array}                                             \tag{4.1}
\]

Indeed the transform of a constant is supported at zero, and the transform of `q` times the delta function at zero is one at every frequency. Hence

\[
\boxed{\widehat R_p(h)=\mathbf1_{h\ne0}.}                \tag{4.2}
\]

In the second reflection, call a good prime active when its additive frequency is nonzero. For the projected term `q\mathbf1_{x=0}`, inactive and active frequencies both occur. The negative term cancels its inactive frequency exactly. When the **whole** Ramanujan factor is reunited, every prime of the original `a` is again active. The local product therefore restores the good-prime denominator containing `ka`.

This conclusion is prior to any Gauss-sum evaluation. All cusp scalars and subsequent local transformations are linear in the finite Fourier coefficients, so the zero at the inactive frequency remains an exact zero. Fixed ray splitting and the original nonunit masks do not turn it into a positive contribution.

For one isolated negative or projected term the reduced second conductor is real and its compact-support cancellation is useful. For their complete sum, the second transform can simply reconstruct the original completion. A proof of the full fourth moment still needs cancellation or a mean-square estimate for the surviving full-conductor object. The identity (4.2) identifies precisely why the present support result alone does not close that proof.

## 5. The proved extension to all three cusps

Lemma 2.1 of [ALL_CUSP_REFLECTION.md](ALL_CUSP_REFLECTION.md) supplies the required geometric adapter for every original cusp `sigma`. For a translation `beta=lambda^3h/q`, reduce `beta=a_0/c_1`, with `c_1|q`. The lemma explicitly constructs `g` with the original first column `(a_0,c_1)` and factors `gamma_sigma g=g_1H`, with `g_1=I mod3`. The source's `SL_2(Z)` and `Z+3O` invariances reduce `theta(Hw)` to exactly one of the original three cusp functions. No additional cusp expansion is assumed. The coordinate Jacobian uses `c_1`, whose norm is at most `Nq`; it does not use the denominator of `gamma_sigma(beta)`.

All three frequency sequences lie in `lambda^(-4)O`, have minimum nonzero norm `1/81`, and have coefficient series absolutely convergent for `Re(s)>1`. Theorem 4.1 of that note therefore proves the exact reflected support identity at every source cusp.

In raw Fourier-norm coordinates the first reflection has scale

\[
X=\frac{(Nc_0)^2(Nk)^2(Na)^2}{B},\qquad q=Mkd,
\]

where `c_0` is one of the fixed bad factors from the first reflection, and `M` encodes its fixed periodic multiplier. Hence the complete grouped sum at that cusp is zero whenever

\[
\boxed{\quad
(Ng)^2>\frac{3R(NM)^2}{(Nc_0)^2}\,B.
\quad}                                                    \tag{5.1}
\]

There are finitely many `c_0` and fixed multipliers, so taking the largest constant gives one cutoff `Ng<=C_S sqrt(B)` for all of them. The explicit standard-face constant in (3.2) uses its reparametrization `Nell=Nn(Nb)^3/27`; (5.1) uses the raw Fourier norm and does not introduce that factor a second time. Thus the support conclusion is available before any restriction to a standard face, ramified valuation, or cube dyad.

## 6. Remaining arithmetic target

The fourth-moment initialization still contains product columns of length about `D^2` and dual rows of norm about `D^(3-theta)`. Removing a completed summand at every cusp does not estimate the strict signed covariance at those scales. Moreover, the original moment is an uncompleted Möbius polynomial; a support identity for its theta completion must be combined with a valid projection and covariance estimate before it can be used there.

The new conclusion is specific: the former large quadratic-sieve majorant for the completed all-negative term is avoidable at every source cusp because that term is exactly zero in the balanced large-scale regime. The full fourth moment, the limiting `17/24` boundary, and the generalized hierarchy remain open.
