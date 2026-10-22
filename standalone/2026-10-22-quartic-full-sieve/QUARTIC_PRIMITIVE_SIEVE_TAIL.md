# A full all-row tail bound for the quartic primitive sieve

**Status:** proposed native lemma, with a complete proof below. Internally reviewed by the separate agent `alternative_major`, including all prime-power cases, the CRT phases, the rowwise divisor count, and the complete all-row large-sieve scope. This is not an integrated result or an external review.

**Scope:** nonzero Gaussian integer rows, primitive column completion by the exact squarefree sieve, fixed ramified support and finite ray conditions. This is a tail bound, not a new zero-free theorem. No estimate for the low-divisor automorphic main term is included.

**Dependencies:** the local prime-power and CRT identities for quartic Gauss sums (DDHL, *Quartic Gauss sums over primes and metaplectic theta functions*, arXiv:2306.11875v2, §3); the elementary two-dimensional additive large sieve, whose use to give the required complete multiplicative large sieve is explained in §5. No quartic-specific squarefree-row large sieve is used.

**What was actually run:** symbolic local-exponent bookkeeping and the proof below. No numerical evidence is used.

**Smallest remaining gap for the proposed application:** an exact, uniformly controlled low-divisor spectral formula with its finite arithmetic diagonal retained. This note does not prove it.

## 1. Statement

Let $F=\mathbb Q(i)$, $\mathcal O=\mathbb Z[i]$, and omit the prime $1+i$ throughout. Use the unique primary generator for every odd ideal. Write $N(c)=|c|^2$ and

$$
g_4(k,c)=\sum_{x\bmod c}\left(\frac xc\right)_4
 e\!\left(\operatorname{Tr}_{F/\mathbb Q}(kx/c)\right).
$$

The additive character can equally be the fixed DDHL convention; changing the fixed dual lattice only changes constants and finitely many bad factors.

Fix a bounded function $W$ supported in $[a,b]\subset(0,\infty)$, with $a,b$ fixed. Let $\xi(c)$ be any function of modulus at most one; a fixed angular character and fixed ray condition are allowed. For $D\ge1$, $R\ge1$, define

$$
T_R(k,D)=\sum_{c\ {\rm primary}}
 \frac{\xi(c)g_4(k,c)}{N(c)}W\!\left(\frac{N(c)}D\right)
 \sum_{\substack{d\ {\rm primary}\\d^2\mid c\\N(d)>R}}\mu_F(d).
\tag{1}
$$

To use the proof as written, $\xi(c)$ must separate on the powerful/squarefree factorization: for each powerful $q$, the value $\xi(mq)$ is an arbitrary fixed column weight in $m$ of modulus at most one. This includes every bounded $\xi$; no multiplicativity is required. A congruence or coprimality restriction on $c$ can be included in that column weight.

Then, for every $\varepsilon>0$ and $K\ge1$,

$$
\boxed{
\sum_{\substack{k\in\mathcal O\\0<N(k)\le K}}
 |T_R(k,D)|^2
 \ll_{\varepsilon,W}
 (KD)^{\varepsilon}\left(\frac K R+\frac{D^2}{R^4}\right).
}
\tag{2}
$$

The row $k=0$ is excluded. Its constant Fourier term requires separate treatment in any automorphic application.

There are also exact empty-tail ranges. The left side of (2) is zero if
$R>\sqrt{bD}$, since $d^2\mid c$ and $N(c)\le bD$ imply
$N(d)\le\sqrt{bD}$. It is zero if $R>K$: a nonzero local Gauss sum
at every prime dividing $d^2$ forces that prime to divide $k$, so
$d\mid k$ and $N(d)\le N(k)\le K$. The same conclusions hold with
weak inequalities at these endpoints because the sieve uses $N(d)>R$.

For the inverse-Poisson scale $K=D^2/H$, (2) gives

$$
\sum_{0<N(k)\le K}|T_R(k,D)|^2
 \ll (KD)^{\varepsilon}\frac K R
 \qquad\text{when }R^3\ge H.
\tag{3}
$$

In particular the principal-scale case $H=1$ needs no additional lower bound on $R$.

## 2. Local row support and exact branch weights

Every odd $c$ has a unique factorization

$$
c=mq,
\quad m\text{ squarefree},\quad (m,q)=1,
\quad q\text{ powerful}.
\tag{4}
$$

Here every prime exponent in $q$ is at least two. The sieve coefficient in (1) becomes

$$
B_R(q)=\sum_{\substack{d\mid\operatorname{rad}(q)\\N(d)>R}}\mu_F(d).
\tag{5}
$$

Thus $B_R(q)=0$ unless $N(\operatorname{rad}(q))>R$, and $|B_R(q)|\le\tau(q)$.

Put $p=N(\pi)$ for an odd prime $\pi$. The elementary local Gauss-sum formula has the following two forms.

If $e\ge2$ and $4\nmid e$, then

$$
g_4(k,\pi^e)=0\quad\text{unless }v_\pi(k)=e-1,
\qquad
\left|\frac{g_4(k,\pi^e)}{p^e}\right|=p^{-1/2}
\text{ on its support}.
\tag{6}
$$

Indeed the local character is induced from the nontrivial character
$x\mapsto(x/\pi)_4^e$ modulo $\pi$. The additive conductor forces exactly $e-1$ powers of $\pi$ in $k$, and the remaining finite-field Gauss sum has modulus $\sqrt p$.

If $e\ge4$ and $4\mid e$, the character is principal on units, and its normalized Gauss sum is the exact Ramanujan identity

$$
\frac{g_4(k,\pi^e)}{p^e}
 =\mathbf 1_{\pi^e\mid k}
  -p^{-1}\mathbf 1_{\pi^{e-1}\mid k}.
\tag{7}
$$

Expand (7) into its two branches. Each local branch has a row divisor $\rho_\pi$ and an absolute coefficient $w_\pi$:

| Exponent/branch | $\rho_\pi$ | $w_\pi$ |
|---|---:|---:|
| $e\ge2$, $4\nmid e$ | $\pi^{e-1}$ | $p^{-1/2}$ |
| $e\ge4$, $4\mid e$, first branch | $\pi^e$ | $1$ |
| $e\ge4$, $4\mid e$, second branch | $\pi^{e-1}$ | $p^{-1}$ |

For a global branch $\mathfrak b$ of $q$, let

$$
\rho(q,\mathfrak b)=\prod_{\pi\mid q}\rho_\pi,
\qquad
w(q,\mathfrak b)=\prod_{\pi\mid q}w_\pi.
\tag{8}
$$

After setting $k=\rho(q,\mathfrak b)r$, the remaining local factor is a function of $r$ of absolute value at most one. Exact-valuation restrictions in (6) can be left in this factor.

## 3. The complete all-row large sieve for a single branch

For $(m,q)=1$, CRT gives

$$
g_4(k,mq)=
 \left(\frac m q\right)_4
 \left(\frac q m\right)_4
 g_4(k,m)g_4(k,q).
\tag{9}
$$

For squarefree $m$,

$$
g_4(k,m)=g_4(1,m)\overline{\chi_m(k)},
\qquad |g_4(1,m)|=\sqrt{N(m)},
\tag{10}
$$

with both sides zero when $(k,m)>1$. Thus the contribution of one fixed $(q,\mathfrak b)$, after writing $k=\rho r$, is a scalar of absolute value at most $w=w(q,\mathfrak b)$ times

$$
\sum_{m\ {\rm squarefree}} b_{q,\mathfrak b}(m)
 \overline{\chi_m(r)}.
\tag{11}
$$

The coefficients contain the fixed CRT phases, the twist $\overline{\chi_m(\rho)}$, $\xi(mq)$, all column restrictions, and
$g_4(1,m)N(m)^{-1}W(N(mq)/D)$. Consequently

$$
N(m)\le bD/N(q),
\qquad
\sum_m|b_{q,\mathfrak b}(m)|^2\ll_W1.
\tag{12}
$$

The latter bound is the elementary count of Gaussian ideals in a fixed dyadic annulus. It is also valid when that annulus meets $m=1$.

Use the ordinary complete multiplicative large sieve over $\mathbb Q(i)$, for primitive characters of conductor norm at most $M$ and all integer rows of norm at most $X$:

$$
\sum_{0<N(r)\le X}
 \left|\sum_{N(m)\le M}^{\rm sf} b_m\chi_m(r)\right|^2
 \ll (X+M^2)\sum_m|b_m|^2.
\tag{13}
$$

Fixed bad-prime conductor factors and primary-generator conventions change only the constant. Formula (13) is weaker than the quartic-specific squarefree-row large sieve, but it is sufficient here and retains all physical rows.

From (11)--(13), the branch norm is therefore

$$
\ll_W w(q,\mathfrak b)^2
 \left(\frac K{N(\rho(q,\mathfrak b))}
       +\frac{D^2}{N(q)^2}\right).
\tag{14}
$$

If $N(\rho)>K$, no nonzero row occurs, and the branch is empty.

## 4. Summing branches uses row support, not Minkowski

For any fixed nonzero $k$, every supported branch has
$\rho(q,\mathfrak b)\mid k$. In particular every prime dividing $q$ divides $k$, and its exponent $e$ satisfies $2\le e\le v_\pi(k)+1$. The total number of supported pairs $(q,\mathfrak b)$ is bounded by a fixed power of $\tau(k)$, hence is $\ll_\varepsilon N(k)^\varepsilon$. Also $|B_R(q)|\le\tau(q)\ll_\varepsilon D^\varepsilon$ on the support of $W$.

Applying Cauchy separately in each physical row, then summing (14), reduces (2) to

$$
\sum_{\substack{q\ {\rm powerful}\\N(\operatorname{rad}(q))>R}}
 \sum_{\mathfrak b}
 \frac{w(q,\mathfrak b)^2}{N(\rho(q,\mathfrak b))}
 \ll_\varepsilon R^{-1+\varepsilon},
\tag{15}
$$

and

$$
\sum_{\substack{q\ {\rm powerful}\\N(\operatorname{rad}(q))>R}}
 \sum_{\mathfrak b}
 \frac{w(q,\mathfrak b)^2}{N(q)^2}
 \ll_\varepsilon R^{-4+\varepsilon}.
\tag{16}
$$

These follow from absolutely convergent Euler factors. For (15) the local factor at a prime of norm $p$ that is required to occur is

$$
\sum_{\substack{e\ge2\\4\nmid e}}p^{-e}
 +\sum_{j\ge1}(p^{-4j}+p^{-(4j+1)})
 =p^{-2}(1+O(p^{-1})).
\tag{17}
$$

For (16) the local factor is

$$
\sum_{\substack{e\ge2\\4\nmid e}}p^{-(2e+1)}
 +\sum_{j\ge1}(p^{-8j}+p^{-(8j+2)})
 =p^{-5}(1+O(p^{-2})).
\tag{18}
$$

Fixing the squarefree radical $a$ therefore bounds the summands in (15) and (16) respectively by $N(a)^{-2+\varepsilon}$ and $N(a)^{-5+\varepsilon}$. Summation over $N(a)>R$ gives (15) and (16). This proves (2), after renaming $\varepsilon$.

## 5. Why the complete large sieve has the needed all-row scope

This paragraph records the standard reduction so that no squarefree-row theorem is silently substituted for (13). Gaussian fractions $a/c$ modulo $\mathbb Z[i]$, with $(a,c)=1$ and $N(c)\le M$, are separated by $\gg M^{-1}$ in the flat two-dimensional torus: a nonzero difference has numerator a nonzero Gaussian integer and denominator $cc'$, of modulus at most $M$. The two-dimensional additive large sieve for lattice rows $|r|\le\sqrt X$ therefore has constant $\ll X+M^2$.

For a primitive character $\chi\bmod c$, finite Gauss inversion expresses $\chi(r)$ as $N(c)^{-1/2}$ times a linear combination of the additive characters $e(\operatorname{Tr}(ar/c))$, with unit-modulus coefficients on $(a,c)=1$. Orthogonality over all characters modulo $c$ bounds the sum over primitive characters by the additive sum, with the standard factor $N(c)/\varphi(c)$. Applying the additive large sieve and then Hilbert-space duality gives the multiplicative large sieve for any selected primitive character at each conductor. Quartic characters modulo odd squarefree $m$ are primitive at every prime dividing $m$; the finitely ramified convention introduces only a fixed conductor factor.

The conductor $1$ character can be handled separately by the elementary row count $\ll X$, so it causes no exception. Every nonzero Gaussian row is included throughout.

## 6. Application boundary

The identity $\mu_F(c)^2=\sum_{d^2\mid c}\mu_F(d)$ is exact. Therefore (2) controls the actual omitted portion when this projector is truncated at $N(d)\le R$. If a low-divisor argument separately gives a full centered canonical norm with the correct arithmetic diagonal, (2) allows its tail to be reattached.

More precisely, suppose a separate theorem gives a relevant total vector
$S$ the bound $\|S\|_2^2\ll (KD)^\varepsilon K$. Then its cross term
with this tail satisfies

$$
|\langle S,T_R\rangle|
 \ll (KD)^\varepsilon
 \left(\frac K{\sqrt R}+\frac{D\sqrt K}{R^2}\right).
\tag{19}
$$

The exact norm difference
$\|S-T_R\|_2^2-\|S\|_2^2$
also contains the tail norm (2), in addition to twice this cross term.
When $K=D^2/H$ and $R^3\ge H$, (19) is
$O((KD)^\varepsilon K/\sqrt R)$, and (2) is smaller.
The inverse-Poisson prefactor $H/D$ then gives
$O((KD)^\varepsilon D/\sqrt R)$.

No claim about that total norm, its centering, its low-divisor level dependence, or a zero-free boundary follows from (2) alone.
