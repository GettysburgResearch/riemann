# Reuniting the Ramanujan allocations before taking norms

Status: exact Euler factorization and a proved enlarged domain of absolute convergence for its remainder. This addendum retains the interference between the negative and divisibility terms. It does not supply a new contour estimate or the full balanced moment.

Dependencies: `COUPLED_THETA_COMPLETION.md` and `NEGATIVE_BRANCH_DIRICHLET_SERIES.md`, whose frozen versions are unchanged. The only analytic input beyond their exact arithmetic is the classical meromorphic continuation of Hecke L-functions (Hecke–Tate; for a precise statement see [Poonen, Tate's thesis notes, Theorem 5.22, p. 38](https://math.mit.edu/~poonen/786/notes.pdf)); no zero-free assertion is assumed. All indices in this addendum lie on the explicitly restricted standard infinity-cusp face, outside the fixed set S. k is squarefree outside S, and the theta squarefree index n is held fixed before any reindexing. The sum reunites the entire Ramanujan allocation over a,b on this face, including primes assigned to the squarefree theta index; it is not a restriction to e=1.

The initial identity concerns two complex variables w,r with Re(w)>1 and Re(r)>1. The notation s used below is related by r=3s-1/2; it is not an independent third variable.

## 1. Exact local factors with the actual character types

Let eta,rho be fixed ray characters from the finite bad-ray decomposition. For a good prime p, put q=Np and

\[
\chi^-(p)=\eta(p)\overline{\alpha(p)}^3\chi_k(p)^3,
\qquad
\chi^+(p)=\rho(p)^3\alpha(p)^3\chi_k(p)^3,
\]

\[
x_p=\chi^-(p)q^{-w},\qquad
 y_p=\chi^+(p)q^{-r}.
\tag{1.1}
\]

Both characters retain their zeros at S and at primes dividing k. Set

\[
\kappa=\eta\rho^3,
\qquad
\kappa_k(p)=\kappa(p)\mathbf1_{p\nmid kS},
\qquad
v=w+r-1,
\qquad z_p=q x_p y_p=\kappa_k(p)q^{-v}.
\tag{1.2}
\]

The last identity is exact: the infinity types -3 and +3 cancel, and chi_k(p)^6 is one or zero according as p does or does not avoid k. In particular the finite-order factor still has the moving k zero mask. It is not the fully primitive kappa character with those Euler factors restored.

For fixed n squarefree, define the two-variable sum

\[
\mathcal F_{k,n}(w,r)
 =\sum_{a\ \mathrm{squarefree}}\sum_b
 \frac{\eta(a)\overline{\alpha(a)}^3\chi_k(a)^3}{(Na)^w}
 \frac{\rho(b)^3\alpha(b)^3\chi_k(b)^3}{(Nb)^r}
 \prod_{p\mid a}\left(-1+Np\,\mathbf1_{p\mid nb}\right).
\tag{1.3}
\]

The power q^(-1/2) of the normalized Ramanujan factor has already been included in w, exactly as in the double-Mellin variables of the companion note. Thus no further q^(-1/2) belongs in the product in (1.3). The sum is absolutely convergent for Re(w),Re(r)>1: the potentially largest mixed contribution is q|x_p y_p|, and Re(w)+Re(r)>2 makes its prime sum convergent.

If p does not divide n, the a-prime can be absent or present and the b-prime exponent can be any j>=0. Its complete local sum is

\[
\begin{aligned}
\sum_{j\ge0} y_p^j+
 x_p\left[-1+(q-1)\sum_{j\ge1}y_p^j\right]
 &=\boxed{\frac{1-x_p+q x_p y_p}{1-y_p}}.
\end{aligned}
\tag{1.4}
\]

If p divides n, its Ramanujan factor is always q-1 when p divides a, so the local factor is

\[
\boxed{\frac{1+(q-1)x_p}{1-y_p}}.
\tag{1.5}
\]

These retain all a,b,n overlaps. Formula (1.4) reunites the negative and cube-divisibility terms; (1.5) also retains the squarefree-index divisibility contribution. No triangle inequality has been taken.

## 2. Factorization with an absolutely convergent remainder

### Theorem 2.1

Let

\[
\Omega=\{(w,v):\Re w>0,\ \Re v>1/2,\ \Re(w+v)>1\}.
\]

Define local remainder factors

\[
R_{p,n}(w,v)=
\begin{cases}
\displaystyle\frac{(1-x_p+z_p)(1-z_p)}{1-x_p}
 =1+\frac{x_pz_p-z_p^2}{1-x_p},&p\nmid n,\\[8pt]
\displaystyle\frac{(1+(q-1)x_p)(1-z_p)}{1-x_p},&p\mid n.
\end{cases}
\tag{2.1}
\]

Then the product mathcal E_(k,n)(w,v)=product_p R_(p,n)(w,v) is holomorphic on Omega. Its infinite part converges normally on compact subsets there. Initially for Re(w),Re(r)>1, and then by meromorphic continuation to Omega with r=v+1-w,

\[
\boxed{\mathcal F_{k,n}(w,r)
 =\frac{L_S(r,\chi^+)\,L_S(v,\kappa_k)}
        {L_S(w,\chi^-)}\,
   \mathcal E_{k,n}(w,v).}
\tag{2.2}
\]

For every delta>0 and epsilon>0, uniformly on

\[
\Re w\ge\delta,\quad
\Re v\ge\tfrac12+\delta,\quad
\Re(w+v)\ge1+\delta,
\]

one has

\[
\boxed{|\mathcal E_{k,n}(w,v)|
 \ll_{S,\delta,\epsilon}
 (Nn)^{\max(0,\,1-\Re w)+\epsilon}.}
\tag{2.3}
\]

The bound is uniform in k and in the imaginary parts. The product is not asserted to be everywhere nonzero.

**Proof.** At p not dividing n, divide (1.4) by the local factor of L(r,chi+)L(v,kappa_k)/L(w,chi-). The result is exactly the first line of (2.1). At p dividing n the same calculation gives the second line. Crucially, neither divides by 1-x_p+z_p, which can vanish. The only displayed denominator in the remainder is 1-x_p, and it is nonzero because Re(w)>0 and |chi^-(p)| is zero or one.

Away from the finitely many prime factors of n,

\[
|R_{p,n}-1|
\ll_\delta q^{-\Re(w+v)}+q^{-2\Re v}.
\]

Both prime sums converge locally uniformly on Omega, even when summed over all ideals instead of primes. This proves normal convergence and holomorphy of the infinite part. Removing factors at primes of k can only remove terms from the uniform majorant. The finitely many n-prime factors are holomorphic on the same domain.

For their size use

\[
|R_{p,n}|
\le \frac{(1+q^{1-\Re w})(1+q^{-\Re v})}
           {1-q^{-\Re w}}
\le C_\delta q^{\max(0,1-\Re w)}
\]

with C_delta independent of p and the imaginary parts. The factors beyond q^max(0,1-Re w) are at most a fixed constant per prime, and hence their product is O_(delta,epsilon)((Nn)^epsilon), by the standard fixed-small-prime argument. Combining this with the uniform bound on the infinite part gives (2.3).

The Euler identity is proved in the initial absolute-convergence region. The classical meromorphic continuations of the three displayed Hecke L-functions then give the stated meromorphic continuation of that same function to Omega. This does not invoke a zero-free half-plane: poles of the reciprocal L-factor are allowed. \(\square\)

The new factor L(v,kappa_k) is finite order, even though the numerator and denominator at r,w have nonzero infinity type. Explicitly,

\[
L_S(v,\kappa_k)
 =L_S(v,\kappa)\prod_{p\mid k}(1-\kappa(p)(Np)^{-v}).
\tag{2.4}
\]

Every moving Euler factor in (2.4) must remain.

## 3. The newly visible divisor in the literal Mellin coordinates

The companion negative-branch identity has

\[
s=\tfrac12+t,\qquad
w=\tfrac12+z_M-2t,\qquad
r=3s-\tfrac12=1+3t.
\]

Here z_M denotes the outer smooth Mellin variable, to distinguish it from the local z_p. Therefore

\[
\boxed{v=w+r-1=\tfrac12+z_M+t.}                         \tag{3.1}
\]

If eta rho^3 is principal, L_S(v,kappa_k) has its usual simple pole at v=1. Its possible polar divisor in these Mellin variables is

\[
\boxed{z_M+t=\tfrac12.}                                \tag{3.2}
\]

Changing the two independent Mellin variables from z_M,t to v,t also gives the exact identities

\[
w=v-3t,\qquad s=\tfrac12+t,
\]

\[
\boxed{A^{z_M-1/2}\left(\frac{cB}{(Nk)^2}\right)^{-t}
 =A^{v-1}\left(\frac{(Nk)^2}{cAB}\right)^t.}               \tag{3.3}
\]

The new scalar divisor is therefore at v=1, while the independent transformed norm ratio remains (Nk)^2/(cAB). Identifying the scalar divisor does not remove that adverse ratio or bound the remaining t integral.

This is different from the conditional numerator/denominator matching line z_M+t=-1/2 obtained by applying a Hecke functional equation to the isolated negative term. Reuniting the Ramanujan terms exposes an additional finite-order L-factor rather than silently eliminating the angular quotient.

The pole need not be merely an artifact at every fixed theta index. For example, take n=1 and eta=rho=1. On v=1 with Re(w)>1, z_p=1/q at primes outside kS and |x_p|<1/q. Hence each good local remainder is nonzero, and the normally convergent remainder product is nonzero. Also L(w,chi-) is nonzero by its Euler product. The nonprincipal angular L(r,chi+) is not identically zero, so away from its discrete zero set as r=2-w varies, the fixed-n function in (2.2) has a genuine simple pole at v=1. This is a statement about that fixed-index meromorphic function. It does not prove an uncancelled pole after summing theta indices or fixed-ray components, and it is not a lower bound for the smoothed balanced polynomial.

## 4. What the remainder bound permits before any further theorem

Reintroducing the squarefree theta series gives a deformation of its coefficients by mathcal E_(k,n)(w,v). Since |gamma_2(n)|=1, (2.3) proves absolute convergence of that n series only in the explicit sufficient region

\[
\Re s>1+\max(0,1-\Re w).
\tag{4.1}
\]

For 0<Re(w)<1 this is Re(s+w)>2. In either case, together with v=w+3s-3/2 and Re(w)>0, this sufficient absolute-convergence region implies Re(v)>5/2: if Re(w)>=1 use Re(s)>1; if Re(w)<1 use Re(s)>2-Re(w). It therefore does not approach the new v=1 divisor. In the case 0<Re(w)<1, the n-convergence condition becomes Re(z_M-t)>1 in the literal Mellin variables. The elementary Euler-product continuation therefore does not itself justify shifting both smooth contours to a useful critical region. The numerator pole at (3.2), the reciprocal angular L-factor, the deformed Gauss series, and all moving k Euler factors would have to be controlled together.

This is a concrete improvement in the analytic description: a product preserving the Ramanujan interference has a holomorphic remainder beyond the initial Euler-product domain and exposes its finite-order divisor exactly. It neither establishes the required higher moment nor supplies a legal contour shift across the newly identified divisor.
