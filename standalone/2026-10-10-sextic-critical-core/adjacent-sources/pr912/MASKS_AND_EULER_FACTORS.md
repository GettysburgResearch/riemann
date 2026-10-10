# Rectangular singleton columns: uniform exclusion removal and Euler correction

Status: proved local algebra and conditional norm-transfer lemmas; the analytic rectangular mean square is not proved. No new zero-free region is asserted.

Scope: the inverse Möbius/sextic family in GettysburgResearch/riemann PR #910, head `670a76c1a3a8f325c43c1755b1cfc24d313a3e3c`. These lemmas are native arguments. The source audit uses OpenAI/math `adc7f1241b42e322a6451854ab7e4b4c146bf78a`, October 5 `paper2.tex`, particularly `eq:T`, `eq:completed-twist`, `prop:canonical`, `eq:initial-scales`, `eq:initial-positive-gap`, and `lem:quadratic`.

What was actually checked: complete local coefficient calculations, finite support, norm normalization, moving-prime constants, and the precise source coefficient/length interfaces. No computation of zeros and no independent revalidation of the full imported paper were performed.

Smallest remaining gap: a mean-square estimate for an unmasked rectangular product of inverse polynomials at one common row range near the largest factor scale. The two reductions below remove the separate moving-exclusion issue and show that the remaining singleton estimate is, up to harmless losses, equivalent to this correlated product estimate.

## 1. Definitions and uniformity conventions

Let `K = Q(sqrt(-3))`; the arguments below work in any fixed number field with its ideal norm. Fix an integer `r >= 1`, a finite set `S` of prime ideals, and tests `W_i` supported in fixed compact intervals `[a_i,b_i]` contained in `(0,infinity)`. Use ideals throughout. At each row `u`, put

\[
 \eta_u(n)=\nu(n)\chi_n(u).
\]

Only complete multiplicativity and `|eta_u(n)| <= 1` are used below, including the exact zero extensions. In particular `eta_u(1)=1`, and an identity with a prime dividing the row remains valid.

Define

\[
 A_u(X;W_i)=\sum_{(n,S)=1}\mu_K(n)\eta_u(n)W_i(Nn/X).
\tag{1.1}
\]

For a squarefree ideal `c` prime to `S`, define the singleton, pairwise-coprime rectangular column

\[
 B_{c,u}(\mathbf X)=
 \sum_{\substack{(n_i,n_j)=1\ (i\ne j)\\(n_1\cdots n_r,cS)=1}}
 \prod_{i=1}^r\mu_K(n_i)\eta_u(n_i)W_i(Nn_i/X_i).
\tag{1.2}
\]

Möbius factors force every `n_i` to be squarefree. Thus their product is squarefree. Write `B_1` for the unmasked family, retaining the fixed set `S`.

Take any finite row set `U`; the intended example is `0 < Nu <= H`, with row norm `l^2(U)`. Multiplication by `eta_u(d)` is a contraction on that norm. Every norm estimate in this note uses exactly the same row set at every smaller column scale.

The support floor is explicit: if `X_i < 1/b_i` for any `i`, then `B_c(X)=0` and also the corresponding product of `A` polynomials is zero. Whenever smaller scales occur, nonzero terms therefore have `X_i >= 1/b_i`. No estimate for a nonexistent fractional-norm ideal is used.

## 2. Exact removal of a moving exclusion

### Proposition 2.1: finite operator identity

For a tuple of ideals `d=(d_1,...,d_r)` supported on primes dividing `c`, write `e_{p,i}=v_p(d_i)` and define the nonnegative integer

\[
 \kappa_c(\mathbf d)=
 \prod_{p\mid c}
 \frac{(e_{p,1}+\cdots+e_{p,r})!}{e_{p,1}!\cdots e_{p,r}!}.
\tag{2.1}
\]

Then

\[
 B_{c,u}(\mathbf X)=
 \sum_{\substack{\mathbf d\\p\mid d_1\cdots d_r\Rightarrow p\mid c}}
 \kappa_c(\mathbf d)\eta_u(d_1\cdots d_r)
 B_{1,u}(X_1/Nd_1,\ldots,X_r/Nd_r).
\tag{2.2}
\]

The sum is finite: its nonzero terms satisfy `Nd_i <= b_i X_i` for every `i`.

**Proof.** This is an identity of multiplicative multivariable coefficients before inserting the smooth weights. At an unexcluded prime, the local series for a squarefree, pairwise-coprime tuple is

\[
 1-z_1-\cdots-z_r,
 \qquad z_i=\eta_u(p)(Np)^{-s_i}.
\]

Excluding the prime removes this local factor. Its formal reciprocal is

\[
 \frac1{1-z_1-\cdots-z_r}
 =\sum_{e_1,\ldots,e_r\ge0}
 \frac{(e_1+\cdots+e_r)!}{e_1!\cdots e_r!}
 z_1^{e_1}\cdots z_r^{e_r}.
\tag{2.3}
\]

Multiplying (2.3) over `p|c` gives (2.2) coefficient by coefficient. The substitution `n_i=d_i m_i` changes the test to `W_i(Nm_i/(X_i/Nd_i))`, with no derivative or normalization change. If `eta_u(p)=0`, all nonconstant local terms vanish and the same identity holds. Finally a nonzero inner term needs `Nm_i <= b_i X_i/Nd_i` and `Nm_i >= 1`, proving finiteness. `QED`.

### Proposition 2.2: no additional analytic theorem is needed for large moving primes

Assume the fixed set `S` contains every prime ideal of norm at most `4r^2`. Suppose an unmasked rectangular estimate

\[
 \|B_{1,\cdot}(\mathbf Y)\|_2
 \le C_{\epsilon_0}D^{\epsilon_0}H^{1/2}
       \prod_iY_i^{1/2}
\tag{2.4}
\]

holds for every nonvanishing smaller rectangle `1/b_i <= Y_i <= X_i`, using the same row set and the same fixed tests. Then

\[
 \|B_{c,\cdot}(\mathbf X)\|_2
 \le C_{\epsilon_0}D^{\epsilon_0}H^{1/2}
       \prod_iX_i^{1/2}
       \prod_{p\mid c}\left(1-\frac r{\sqrt{Np}}\right)^{-1}.
\tag{2.5}
\]

For every `delta>0`, the last product is `O_{K,r,delta}((Nc)^delta)`. Consequently, if `Nc <= D^C` for a fixed `C`, the moving exclusion costs only an arbitrarily small power of `D`.

**Proof.** Apply Minkowski to (2.2), use contraction of the exterior character, and insert (2.4). The remaining nonnegative sum is at most

\[
 \sum_{\mathbf d}\frac{\kappa_c(\mathbf d)}{\prod_i(Nd_i)^{1/2}}
 =\prod_{p\mid c}\sum_{m\ge0}
          \left(\frac r{\sqrt{Np}}\right)^m
 =\prod_{p\mid c}\left(1-\frac r{\sqrt{Np}}\right)^{-1}.
\]

All geometric series converge because `Np>4r^2`. For any `delta>0`, choose a fixed threshold `Q_delta` such that

\[
 -\log(1-r/\sqrt q)\le\delta\log q
 \quad(q\ge Q_\delta).
\]

The finitely many prime ideals of norm below this threshold contribute a constant, and the other factors contribute at most `(Nc)^delta`. Choosing `epsilon_0` and `delta` smaller than the desired final loss proves the last assertion. `QED`.

This statement is genuinely uniform in the moving ideal. It never treats `c` as part of an uncontrolled implied constant.

### 2.3 Restoring the original fixed bad-prime set

Let `S_0` be the original fixed set and put

\[
 S_r=S_0\cup\{p:Np\le4r^2\},\qquad P=S_r\setminus S_0.
\]

An unmasked theorem for this one fixed set `S_r`, followed by Proposition 2.2, suffices for every moving exclusion with the original set `S_0`.

Indeed, each prime of `P` occurs in at most one singleton factor. Assign each `p in P` either to no factor or to one of the `r` factors; if `p|c`, only the absent assignment is allowed. Let `q_i` be the product assigned to factor `i`, and let `c'` be the part of `c` outside `S_r`. Then the exact finite expansion is

\[
 B_{c,u}^{S_0}(\mathbf X)=
 \sum_{\text{permitted assignments}}
 \left(\prod_i\mu_K(q_i)\right)\eta_u(q_1\cdots q_r)
 B_{c',u}^{S_r}(X_1/Nq_1,\ldots,X_r/Nq_r).
\tag{2.6}
\]

There are at most `(r+1)^{|P|}` terms, a fixed number independent of `D,c,u`. After norm transfer, the scale multipliers sum to at most

\[
 \prod_{p\in P}\left(1+\frac r{\sqrt{Np}}\right),
\]

also a fixed constant. Scales below their support floor simply vanish. Thus no geometric series at a small prime is required. This uses an unmasked analytic hypothesis for a fixed enlarged set; it does not infer that hypothesis merely by discarding a mask from a signed polynomial.

## 3. The exact Euler correction for singleton factorization

For `Re(s_i)>1`, define the multivariable coefficient series

\[
 \mathcal F_u(\mathbf s)=
 \sum_{\substack{(n_i,n_j)=1\ (i\ne j)\\(n_1\cdots n_r,S)=1}}
 \prod_i\frac{\mu_K(n_i)\eta_u(n_i)}{(Nn_i)^{s_i}}
 =\prod_{p\notin S}(1-z_{p,1}-\cdots-z_{p,r}),
\tag{3.1}
\]

where `z_{p,i}=eta_u(p)(Np)^{-s_i}`. Also put

\[
 L_u^S(s)=\prod_{p\notin S}(1-\eta_u(p)(Np)^{-s})^{-1}.
\]

For the arithmetic family this is the finite-order Hecke Euler product specified by the row, with its original zero extensions. Only its Euler factors are used in the following algebra.

We have the exact factorization

\[
 \mathcal F_u(\mathbf s)=\mathcal C_u(\mathbf s)
            \prod_{i=1}^r L_u^S(s_i)^{-1},
\qquad
 \mathcal C_u(\mathbf s)=
 \prod_{p\notin S}
 \frac{1-\sum_i z_{p,i}}{\prod_i(1-z_{p,i})}.
\tag{3.2}
\]

### Proposition 3.1: analytic and coefficient control of the correction

The Euler product for `C_u` converges absolutely and locally uniformly on

\[
 \operatorname{Re}s_i>\tfrac12\quad(1\le i\le r),
\tag{3.3}
\]

uniformly in the row and in the imaginary parts on each closed subregion `Re(s_i)>=1/2+delta`. It is holomorphic there. If `S` contains all primes of norm at most `4r^2`, its reciprocal has the same properties. More strongly, the multivariable Dirichlet coefficients of both correction factors are absolutely summable when weighted by `prod_i(Nd_i)^{-1/2-delta}`, uniformly in `u`.

**Proof.** At one prime, write `z_i=z_{p,i}`. Expanding the denominator geometrically gives the particularly simple coefficient formula

\[
 \frac{1-\sum_i z_i}{\prod_i(1-z_i)}
 =1+\sum_{\mathbf e\ne0}
       \bigl(1-|\operatorname{supp}\mathbf e|\bigr)\mathbf z^{\mathbf e}.
\tag{3.4}
\]

Thus all terms supported in one coordinate vanish. Every nonconstant term involves at least two coordinates. Its absolute coefficient sum at `|z_i|<=q^{-1/2-delta}` is

\[
 1+\sum_{\substack{J\subseteq\{1,\ldots,r\}\\|J|\ge2}}
 (|J|-1)\prod_{i\in J}\frac{|z_i|}{1-|z_i|}
 =1+O_{r,\delta}(q^{-1-2\delta}).
\tag{3.5}
\]

The sum of `(Np)^{-1-2delta}` converges. This proves absolute Dirichlet-coefficient summability, uniformity and holomorphy for `C_u`. For the reciprocal, use

\[
 \frac{\prod_i(1-z_i)}{1-\sum_i z_i}
 =1+\frac{\displaystyle\sum_{j=2}^r(-1)^j e_j(\mathbf z)}
              {1-\sum_i z_i},
\tag{3.6}
\]

where `e_j` is the elementary symmetric polynomial. At the remaining primes, `sum_i|z_i|<1/2`. Expanding the denominator in (3.6) gives an absolute local coefficient sum `1+O_r(q^{-1-2delta})`, and the same argument applies. Neither the numerator nor the denominator in the local correction vanishes on (3.3) after the fixed small-prime removal. `QED`.

The cancellation of the one-coordinate terms explains why the correction starts at the summable prime weight `q^{-1-2delta}`. It contains the repeated-prime arithmetic; the reciprocal `L` factors retain the unsolved analytic content.

### 3.2 Exact positive coefficients for the inverse correction

The coefficient of `z^e` in `C_p^{-1}` is

\[
 h(\mathbf e)=
 \sum_{J\subseteq\operatorname{supp}\mathbf e}
 (-1)^{|J|}
 \frac{(|\mathbf e|-|J|)!}
      {\prod_i(e_i-\mathbf1_{i\in J})!}.
\tag{3.7}
\]

It is a nonnegative integer. To see this, consider words with `e_i` occurrences of letter `i`. For each active letter choose one distinct designated position. Such positions exist because the word length is at least the number of active letters. Inclusion-exclusion counts the words in which letter `i` does not occupy its designated position, giving exactly (3.7). For a single active letter the count is zero. When every active exponent is one, the count is the ordinary derangement number on the active letters. This interpretation is not needed for the norm theorem but checks the signs in the inverse identity.

## 4. Conditional equivalence with the actual mixed product moment

For fixed tests, put

\[
 P_u(\mathbf X)=\prod_{i=1}^r A_u(X_i;W_i).
\]

Assume all varying scales satisfy `X_i <= D^C` for a fixed `C`, with the exact support floors stated above, and assume `S` contains the fixed small-prime set. Then the following uniform families of assertions are equivalent, with arbitrary `D^epsilon` losses allowed:

\[
 \|B_{1,\cdot}(\mathbf X)\|_2
 \ll_\epsilon D^\epsilon H^{1/2}\prod_iX_i^{1/2};
\tag{4.1}
\]

\[
 \|P_{\cdot}(\mathbf X)\|_2
 \ll_\epsilon D^\epsilon H^{1/2}\prod_iX_i^{1/2}.
\tag{4.2}
\]

Each family must hold at every smaller nonvanishing rectangle while preserving the same row set. This is a conditional equivalence, not a proof of either estimate.

**Proof.** Factor `eta_u(d_1...d_r)` from the multivariable coefficients of `C_u` and its reciprocal; let the resulting row-independent coefficients be `c(d)` and `h(d)`. The coefficient identities (3.2) give exact finite smooth convolution identities

\[
 \begin{aligned}
 B_{1,u}(\mathbf X)
 &=\sum_{\mathbf d}c(\mathbf d)\eta_u(d_1\cdots d_r)
      P_u(X_1/Nd_1,\ldots,X_r/Nd_r),\\
 P_u(\mathbf X)
 &=\sum_{\mathbf d}h(\mathbf d)\eta_u(d_1\cdots d_r)
      B_{1,u}(X_1/Nd_1,\ldots,X_r/Nd_r).
 \end{aligned}
\tag{4.3}
\]

Both are finite because `Nd_i <= b_iX_i` on nonzero terms. Suppose (4.2) holds. Minkowski and contraction of the exterior row factors give

\[
 \|B_1(\mathbf X)\|_2
 \ll D^{\epsilon_0}H^{1/2}\prod_iX_i^{1/2}
 \sum_{Nd_i\le b_iX_i}
       |c(\mathbf d)|\prod_i(Nd_i)^{-1/2}.
\]

For any fixed `delta>0`, the last sum is at most

\[
 \left(\prod_i\max(1,b_iX_i)\right)^\delta
 \sum_{\mathbf d}|c(\mathbf d)|
       \prod_i(Nd_i)^{-1/2-\delta}
 \ll_{\delta,r,S,W_i}D^{Cr\delta}.
\]

Proposition 3.1 supplies the finite constant. Choose `epsilon_0` and `delta` smaller than the requested final loss. The second identity in (4.3) proves the reverse implication in exactly the same way, using the absolutely summable coefficients `h`. The estimates apply only to nonvanishing shifted rectangles; all other terms are zero. `QED`.

On the equal rectangle and with all tests equal, (4.2) is precisely

\[
 \sum_{u\in U}|A_u(D;W)|^{2r}\ll D^{r+\epsilon}H.
\]

Conversely, a `2r`-th moment uniform over all smaller factor scales at the same row range implies the mixed product bound (4.2) by Hölder. Thus the singleton formulation accurately isolates the local algebra but does not avoid the main higher-moment difficulty.

### Proposition 4.1: explicit logarithmic cost for the correction operators

The arbitrary small-power loss used in (4.3) can be replaced by

\[
 \bigl(\log(3+Z)\bigr)^{\binom r2},
 \qquad Z=\max\{1,b_1X_1,\ldots,b_rX_r\},
\tag{4.4}
\]

in each direction, at the level of the `l^2` norm. More precisely, for either `g=c` or `g=h`,

\[
 \sum_{Nd_i\le b_iX_i}|g(\mathbf d)|
                    \prod_i(Nd_i)^{-1/2}
 \ll_{K,r,S}\bigl(\log(3+Z)\bigr)^{\binom r2}.
\tag{4.5}
\]

Thus a squared norm loses at most the power `2 binom(r,2)` of this logarithm. The fixed small-prime removal is retained.

**Proof.** Every prime occurring in one of the permitted `d_i` has norm at most `Z`. Dropping the tuple-size restriction, while keeping this prime restriction, only enlarges the nonnegative coefficient sum. Put `t=q^{-1/2}` at a remaining prime. Formula (3.4) shows that all its nonconstant coefficients are nonpositive, so its absolute coefficient generating function is exactly

\[
 C_{\rm abs}(t)=2-\frac{1-rt}{(1-t)^r}
              =1+\binom r2t^2+O_r(t^3).
\tag{4.6}
\]

The inverse coefficients are nonnegative by (3.7), and hence their absolute generating function is

\[
 H_{\rm abs}(t)=\frac{(1-t)^r}{1-rt}
              =1+\binom r2t^2+O_r(t^3).
\tag{4.7}
\]

Both series converge because `rt<1/2`. Taking the logarithm of the product of either local majorant over `Np<=Z`, the sum of the cubic errors is bounded and the quadratic term is

\[
 \binom r2\sum_{Np\le Z}\frac1{Np}
 \le\binom r2\log\log(3+Z)+O_{K,r}(1).
\]

For completeness the required Mertens upper bound needs only the simple pole of the fixed Dedekind zeta function and Chebyshev's bound. Put `sigma=1+1/log Z` for `Z>=3`. The Euler product gives

\[
 \sum_{Np\le Z}\frac1{Np}
 \le\log\zeta_K(\sigma)
    +(\sigma-1)\sum_{Np\le Z}\frac{\log Np}{Np}.
\]

The simple pole gives `log zeta_K(sigma)=log log Z+O_K(1)`. The prime-ideal Chebyshev bound `sum_{Np<=x} log Np = O_K(x)`, obtained from the rational Chebyshev bound by splitting rational primes in the fixed field, gives `sum_{Np<=Z}(log Np)/Np=O_K(log Z)` by partial summation. This proves the displayed Mertens bound, including its unit coefficient of `log log Z`. Bounded `Z` is absorbed in the constant. Exponentiation proves (4.5). Applying it to the two finite identities (4.3) proves (4.4). `QED`.

The logarithm comes from prime collisions involving exactly two factors. Collisions involving three or more factors enter the convergent `q^{-3/2}` remainder. This agrees with the separate incidence-hypergraph decomposition of the full moment.

## 5. What the imported theta argument does and does not close

The October 5 source defines `T(X;Psi)` for a completely multiplicative `Psi`, but its reflection and mean-square theorem apply to the specific finite-order twists in `eq:completed-twist`, with fixed ray factors and prescribed moving sextic factors. The generic definition alone is not a reflection theorem for every completely multiplicative sequence.

The local coefficient for a singleton `r`-fold inverse column is `1-sum_i z_i`. After one row Poisson transform, the ordinary Möbius factor can still undergo the source's Gauss--Jacobi conversion. Its full divisor-allocation coefficient remains. Equations (3.2)--(4.3) show exactly what that coefficient represents: a correlated product of `r` reciprocal `L` functions, with an absolutely convergent correction. The source's ordinary cubic-theta coefficient is not this product. No theta reflection for this coefficient class has been derived here.

There is also a separate, quantitative scale obstruction. If one collapses the `r` factors, each of norm about `D`, to a single column of norm `X_0=D^r`, the source's initial row Poisson scale is

\[
 \mathcal H_{\rm dual}\asymp X_0^2/H.
\]

The source canonical descent requires a positive gap between that dual row length and the column-auxiliary product. In the unsplit leading range that product is `X_0`, so the ratio is

\[
 \frac{\mathcal H_{\rm dual}}{\Sigma}
 \asymp\frac{D^r}{H}.
\tag{5.1}
\]

At `H=D^{1+theta}` and `r>=2`, this is `D^{r-1-theta}`, not a small power. The initial positive-gap hypothesis fails even if one grants a formal extension of the coefficient class. A new coefficient adapter alone therefore cannot justify reusing the source induction at the desired row length.

Likewise, tensorizing the terminal quadratic sieve collapses a product of `r` columns of length `Y` to length `Y^r`. Its `(H+Y^r)` term incurs exactly the large-length cost that the desired theorem must avoid. The fact that the quadratic sieve accepts arbitrary complex coefficients does not remove this length term.

One cannot fix this by postulating an unrestricted bounded-coefficient higher-moment theorem. For a chosen row `u_0=1`, choose bounded coefficients `b(n)=overline{nu(n)}mu_K(n)` on the good squarefree ideals and take a fixed nonnegative smooth test. Then the modified inverse sum at that row is a positive squarefree count of order `D`. Its `2r`-th power alone is of order `D^{2r}`, larger than `D^rH` for `r>1+theta`. This counterexample concerns an arbitrary-coefficient extension, not the actual Möbius coefficient in the target family.

The productive missing estimate must retain arithmetic correlations between factors, the common row, and the signed terms generated by Poisson. The local algebra and moving exclusions are now explicit; no cancellation bound for those correlations is claimed.
