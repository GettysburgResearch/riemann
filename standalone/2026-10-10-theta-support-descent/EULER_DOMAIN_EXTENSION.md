# A larger analytic domain for the reunited Ramanujan factor

**Status:** proposed proved local factorization and fixed-index continuation theorem. The Hecke continuation and the optional convexity comparison use classical analytic inputs stated below. No generalized moment, new zero-free boundary, or legal contour shift for the full theta series is claimed.

**Scope:** the standard infinity-cusp face of the coupled two-factor completion, with its original finite ray factors, quadratic row phases, and all moving zero masks. The theta squarefree index is fixed throughout the continuation theorem. A separate section identifies the still-unproved passage to the complete theta sum.

**Frozen repository source:** PR #915, commit `9959364671f89b86f3992ec5ed5e19f804eb607b`, specifically `standalone/2026-10-10-sextic-critical-core/REUNITED_RAMANUJAN_EULER_PRODUCT.md`, Sections 1–4, and `NEGATIVE_BRANCH_DIRICHLET_SERIES.md`, Sections 2–3. Their definitions and original continuation domain are preserved. The new result extends their scalar arithmetic factor; it does not strengthen their theta-series conclusion by implication.

**External analytic input:** ordinary meromorphic continuation of Hecke L-functions, with entire finite L-function for a nonzero angular infinity type. See Bjorn Poonen, [Tate's thesis notes](https://math.mit.edu/~poonen/786/notes.pdf), Theorem 5.22 and the subsequent L-function formulation. The optional conductor comparison also uses the usual convexity estimate, derived from that functional equation and the Euler bound by the three-lines theorem. No new zero-free result is imported implicitly.

**What was checked:** the exact rational-function identities below; their initial Euler-product domain; normal convergence of the new remainder; the n-prime factors and their uniform norm bound; and the signs and exponents in two prospective contour paths. The local identity has an independent coefficient check recorded at the end. These checks are algebraic, not numerical evidence for a moment estimate.

## 1. The exact fixed-index object

Work over K=Q(omega), with the inherited primary-generator convention and fixed bad-prime set S. In this note k denotes the squarefree dual row, not the moment order. Let n be the squarefree theta index on the standard face, outside S. It need not be declared coprime to k: the character zeros keep the literal convention in that case too.

For fixed finite ray characters eta and rho, write

\[
\chi^-_k(a)=\eta(a)\overline{\alpha(a)}^3\chi_k(a)^3,
\qquad
\chi^+_k(b)=\rho(b)^3\alpha(b)^3\chi_k(b)^3,
\qquad \kappa=\eta\rho^3.
\tag{1.1}
\]

All three characters below have their Euler factors at S and at primes of k removed. In particular

\[
\kappa_k(p)=\kappa(p)\mathbf1_{p\nmid kS},
\qquad \chi^-_k(p)\chi^+_k(p)=\kappa_k(p).
\tag{1.2}
\]

The zero mask in this identity follows from the literal sixth power of the row character; it is not restored to one at a prime dividing k.

Set v=w+r-1. The fixed-index sum from the source is

\[
\mathcal F_{k,n}(w,r)=
\sum_{a\ \mathrm{squarefree}}\sum_b
\frac{\chi^-_k(a)}{(Na)^w}\frac{\chi^+_k(b)}{(Nb)^r}
\prod_{p\mid a}\bigl(-1+Np\,\mathbf1_{p\mid nb}\bigr).
\tag{1.3}
\]

It converges absolutely for Re(w)>1 and Re(r)>1. At a prime p, put q=Np and

\[
x=\chi^-_k(p)q^{-w},\qquad
y=\chi^+_k(p)q^{-r},\qquad
z=qxy=\kappa_k(p)q^{-v}.
\tag{1.4}
\]

Its local factor is (1-x+z)/(1-y) when p does not divide n and (1+(q-1)x)/(1-y) when p divides n. The previously established factorization is

\[
\mathcal F_{k,n}(w,r)
=\frac{L(r,\chi^+_k)L(v,\kappa_k)}{L(w,\chi^-_k)}
\mathcal E_{k,n}(w,v),
\tag{1.5}
\]

where the local factors of the old remainder are

\[
R_{p,n}(w,v)=
\begin{cases}
\displaystyle\frac{(1-x+z)(1-z)}{1-x},&p\nmid n,\\[5pt]
\displaystyle\frac{(1+(q-1)x)(1-z)}{1-x},&p\mid n.
\end{cases}
\tag{1.6}
\]

The old infinite product was proved holomorphic when

\[
\Re w>0,\qquad \Re v>\tfrac12,\qquad \Re(w+v)>1.
\tag{1.7}
\]

The two new extractions below identify which part of this restriction is only a restriction of that particular remainder product.

## 2. A quadratic extraction leaves only mixed cubic errors

Define

\[
\mathcal T_3=
\{(w,v):\Re w>0,\ \Re v>0,
\ 2\Re w+\Re v>1,\ \Re w+2\Re v>1\}.
\tag{2.1}
\]

### Theorem 2.1. Exact extraction and normal convergence

There is a holomorphic remainder \(\mathcal E^{(1)}_{k,n}\) on \(\mathcal T_3\) such that, initially in the absolute-convergence region and then meromorphically on \(\mathcal T_3\),

\[
\boxed{
\mathcal F_{k,n}(w,v+1-w)
=\frac{
L(v+1-w,\chi^+_k)L(v,\kappa_k)
L(w+v,\chi^-_k\kappa_k)}
{L(w,\chi^-_k)L(2v,\kappa_k^2)}
\mathcal E^{(1)}_{k,n}(w,v).}
\tag{2.2}
\]

For every delta>0 and epsilon>0, the remainder satisfies

\[
\boxed{
|\mathcal E^{(1)}_{k,n}(w,v)|
\ll_{S,\delta,\epsilon}
(Nn)^{\max(0,1-\Re w)+\epsilon}}
\tag{2.3}
\]

uniformly in k and both imaginary parts, on the closed region

\[
\Re w,\Re v\ge\delta,
\quad 2\Re w+\Re v\ge1+\delta,
\quad \Re w+2\Re v\ge1+\delta.
\tag{2.4}
\]

The remainder is not asserted to be nonvanishing.

**Proof.** At p not dividing n, the elementary identity

\[
\boxed{
\frac{(1-x+z)(1-z)}{1-x}
=\frac{1-z^2}{1-xz}
\left(1+\frac{xz(x-z)}{(1-x)(1+z)}\right)}
\tag{2.5}
\]

extracts both degree-two terms of the old remainder. In particular it extracts the positive mixed term xz and the negative pure term -z^2 with their actual signs. Define the new local factors by

\[
R^{(1)}_{p,n}=
\begin{cases}
\displaystyle1+\frac{x^2z-xz^2}{(1-x)(1+z)},&p\nmid n,\\[7pt]
\displaystyle\frac{(1+(q-1)x)(1-xz)}{(1-x)(1+z)},&p\mid n.
\end{cases}
\tag{2.6}
\]

The second line follows by multiplying the second line of (1.6) by (1-xz)/(1-z^2). We cancel the factor 1-z algebraically. Thus neither line divides by 1-x+z, which can vanish. The remaining denominators are nonzero when Re(w),Re(v)>0, because |x|<1 and |z|<1; at a deleted prime both are zero and the local factor is one.

At an n-free prime, on (2.4),

\[
|R^{(1)}_{p,n}-1|
\ll_\delta q^{-2\Re w-\Re v}+q^{-\Re w-2\Re v}.
\tag{2.7}
\]

Both prime sums converge normally on compact subsets of \(\mathcal T_3\). This proves holomorphy of the infinite part of the new product. Removing the primes of k or n from this uniform majorant does not enlarge its bound. The finitely many n-prime factors are holomorphic on the same domain.

At an n-prime, (2.6) gives

\[
|R^{(1)}_{p,n}|
\le
\frac{(1+q^{1-\Re w})(1+q^{-\Re w-\Re v})}
{(1-q^{-\Re w})(1-q^{-\Re v})}
\le C_\delta q^{\max(0,1-\Re w)}.
\tag{2.8}
\]

For fixed C_delta and every epsilon>0, the product of C_delta over the squarefree prime factors of n is O_delta,epsilon((Nn)^epsilon), by separating the finitely many small prime norms. Combining (2.7) and (2.8) proves (2.3), uniformly in the moving k and all vertical parameters.

Finally the extracted local quotient is

\[
\frac{1-\kappa_k(p)^2q^{-2v}}
{1-\chi^-_k(p)\kappa_k(p)q^{-w-v}},
\]

whose Euler product is exactly L(w+v,chi^-_k kappa_k)/L(2v,kappa_k^2). This proves (2.2) in the initial domain. Ordinary Hecke continuation supplies its meromorphic continuation to \(\mathcal T_3\). No zero-free half-plane is needed for this identity. QED.

### 2.1 The new inverse factor has finite order

The extracted numerator has infinity type -3:

\[
\chi^-_k\kappa_k
=\eta\kappa\,\overline\alpha^3\chi_k^3,
\tag{2.9}
\]

with the same literal zero mask. It is therefore nonprincipal, and its L-function is entire. The other angular numerator in (2.2) has infinity type +3 and is likewise entire.

The sole newly extracted reciprocal is finite order:

\[
L(2v,\kappa_k^2)^{-1}
=L_S(2v,\kappa^2)^{-1}
\prod_{p\mid k}(1-\kappa(p)^2q^{-2v})^{-1}.
\tag{2.10}
\]

Its primitive character is fixed, independently of k. Every moving factor on the right is nonzero for Re(v)>0. On a closed right half-plane it costs only (Nk)^epsilon, by the standard fixed-small-prime argument. This extraction introduces no new reciprocal of an angular L-function. The original reciprocal L(w,chi^-_k)^(-1) is still present and still requires its own estimate.

If a finite-order zero-free boundary beta is assumed for the fixed character kappa^2, (2.10) is holomorphic for Re(v)>beta/2, with the reciprocal understood analytically at the principal pole. Consequently the old remainder E has a holomorphic continuation on

\[
\mathcal T_3\cap\{\Re v>\beta/2\}.
\tag{2.11}
\]

The use of beta in this statement is expressly conditional. The new factorization and its meromorphic continuation are unconditional relative to ordinary Hecke continuation. In particular, an imported boundary beta<1 permits v below 1/2 in this scalar factor; it does not by itself authorize shifting the full theta integral there.

### 2.2 A fixed-index zero on the middle line

If kappa^2 is principal, L(2v,kappa_k^2) has a simple pole at v=1/2. Therefore, as a meromorphic identity in w and v,

\[
\boxed{
L(w,\chi^-_k)\mathcal F_{k,n}(w,v+1-w)
\quad\text{vanishes at }v=\tfrac12
\quad(\Re w>\tfrac14).}
\tag{2.12}
\]

Indeed, (w,1/2) belongs to \(\mathcal T_3\) for Re(w)>1/4. In (2.2), after multiplying by L(w,chi^-_k), all numerator factors and the remainder are holomorphic there. L(v,kappa_k) has no pole at v=1/2, whereas the reciprocal of L(2v,kappa_k^2) has a zero. This proves (2.12); the zero could have larger order. Multiplication by the original reciprocal's denominator is intentional, since a zero of L(w,chi^-_k) must not be silently ignored.

This is a fixed-theta-index identity. It is not a zero of the full completed polynomial: an analytically continued infinite n sum could supply a compensating singularity.

## 3. All linear mixed terms can also be extracted

The following additional result removes the old condition Re(w+v)>1 throughout the band Re(v)>1/2, with no zero-free input at all.

For an integer J>=0, define

\[
R^{[J]}_{p,n}=R_{p,n}\prod_{a=1}^{J}(1-x^a z).
\tag{3.1}
\]

At p not dividing n, the old factor has expansion

\[
R(x,z)=1+\frac{x}{1-x}z-\frac1{1-x}z^2.
\]

Multiplication by the product in (3.1) removes its first J terms linear in z. More exactly, its remaining coefficient of z is x^(J+1)/(1-x). Therefore, uniformly on Re(w),Re(v)>=delta,

\[
R^{[J]}_{p,n}
=1+O_{J,\delta}\!
\left(q^{-(J+1)\Re w-\Re v}+q^{-2\Re v}\right)
\quad(p\nmid n).
\tag{3.2}
\]

The higher powers of z have bounded coefficient sum because J is fixed and |x|<=2^(-delta)<1. The n-prime estimate is still (2.8) up to a constant depending on J and delta.

It follows that, on

\[
\Omega_J=\{\Re w>0,\ \Re v>1/2,
\ (J+1)\Re w+\Re v>1\},
\]

the old remainder has the holomorphic representation

\[
\boxed{
\mathcal E_{k,n}(w,v)
=\prod_{a=1}^{J}L(aw+v,(\chi^-_k)^a\kappa_k)
\mathcal E^{[J]}_{k,n}(w,v).}
\tag{3.3}
\]

The new remainder product converges normally there. Every displayed L-factor is a numerator with nonzero infinity type -3a, and hence entire. The regions Omega_J are nested, connected, and cover

\[
\boxed{\Re w>0,\qquad \Re v>\tfrac12.}
\tag{3.4}
\]

The expressions agree on overlaps by their Euler identity on a common open absolute-convergence domain and the identity theorem. Thus (3.3) proves the asserted holomorphic continuation throughout (3.4). Its remainder, rather than necessarily the full continued E, has the uniform bound (2.3).

There is a further arithmetic simplification: for even a, the row phase in (chi^-_k)^a is the principal coprimality mask, so its underlying primitive angular character is fixed independently of k. Only odd a retains the moving quadratic row twist. No row zero is deleted in either case.

## 4. What these facts do and do not permit in the theta integral

The literal Mellin coordinates in the frozen source are

\[
s=\tfrac12+t,\qquad
w=\tfrac12+z_M-2t,\qquad
v=\tfrac12+z_M+t,
\qquad r=v+1-w=3s-\tfrac12.
\tag{4.1}
\]

In particular

\[
t=(v-w)/3,\qquad z_M=(2v+w)/3-\tfrac12,
\]

and the complete scalar is exactly

\[
A^{v-1}\left(\frac{(Nk)^2}{cAB}\right)^{(v-w)/3}.
\tag{4.2}
\]

The positive constant c is fixed by the source cusp normalization.

The remainder bound (2.3) still grows with the theta index as (Nn)^(max(0,1-Re(w))+epsilon). Therefore bounding the normalized Gauss coefficient by one only proves absolute convergence of the n series when

\[
\Re s>1+\max(0,1-\Re w).
\tag{4.3}
\]

This is the same sufficient n-summability requirement as in the frozen packet. The new scalar factorization removes an Euler-product domain restriction, but it does not remove this distinct summation requirement. This component by itself proves no reciprocal estimate for the angular character chi^-_k. The separate [fixed-angular extension](HIGHER_ANGULAR_SECOND_MOMENT.md), Theorem 6.2, supplies a conductor-uniform reciprocal bound on Re(w)>11/12, conditional on its imported source inputs. It does not supply the much larger continuation needed at Re(w) near 1/2.

The separate [divisor-conditioning theorem](DEFORMED_GAUSS_CONTINUATION.md) continues the complete reunited series below this absolute n-series region, approaching Re(v)=1 from the right. It does so by conditioning on d, completing each Gauss series, and cancelling its cube factor exactly. That argument requires more than the scalar remainder bounds here and still does not reach the prospective critical paths below.

### 4.1 A prospective contour comparison, with both numerator costs

The following is only an algebraic/conductor comparison of possible contours. It is not a bound for the complete integral. Take A=B=D and denote Nk by Q for this paragraph. Work first with bounded imaginary parts, so that the fixed gamma and vertical factors do not obscure the Q powers. The standard degree-two Hecke convexity bound for a fixed angular type is

\[
|L(\sigma+i\tau,\psi_k)|
\ll_\epsilon Q^{(1-\sigma)/2+\epsilon},
\quad 0\le\sigma\le1,
\tag{4.4}
\]

with a polynomial vertical factor when tau varies. Its conductor is at most a fixed multiple of Q. Primitive convexity follows from the Hecke functional equation, the right Euler bound, and the three-lines theorem; restoring the moving Euler masks costs Q^epsilon on the fixed positive real-part ranges used here.

There are **two** angular numerators in (2.2). Both must be included. Relative to the central scalar D^(-1/2) at w=v=1/2, take 0<delta<1/4:

| Prospective path | Arguments of the two angular numerators | Exact scalar ratio | Product of convexity costs | Combined comparison |
| --- | --- | --- | --- | --- |
| w=1/2, v=1/2-delta | r=1-delta and w+v=1-delta | D^(-delta/3) Q^(-2delta/3) | Q^(delta+epsilon) | (Q/D)^(delta/3) Q^epsilon |
| w=1/2+delta, v=1/2-delta | r=1-2delta and w+v=1 | D^(delta/3) Q^(-4delta/3) | Q^(delta+epsilon) | (D/Q)^(delta/3) Q^epsilon |

Fixed powers of c are absorbed into the constant. The second path keeps the new mixed numerator on real part one, while moving the original angular numerator to 1-2delta. The first path would be adverse in the initial long dual range Q about D^3. Ignoring either numerator would misstate this comparison.

For both paths the newly extracted reciprocal is evaluated at 2v=1-2delta. A supplied finite-order boundary beta controls it only with a strict margin 1-2delta>beta. The possible improvement in the last column is consequently conditional on the indicated scalar estimates, and is **not yet a moment improvement**. In particular:

1. The original reciprocal L(w,chi^-_k)^(-1) needs a uniform bound on the chosen path. Its infinity type is -3. The separate fixed-angular Theorem 6.2 proves the bound only on Re(w)>11/12; neither displayed prospective path lies in that range.
2. The full deformed Gauss/theta series must be continued with adequate bounds along the path. For example, on the second path s=1/2-2delta/3 and s+w=1+delta/3, far outside the sufficient absolute-convergence condition (4.3). This path is also outside the domain of the separate divisor-conditioning theorem, which remains on Re(v)>1.
3. Every fixed-ray component, pole crossed by the full series, and transformed-weight seminorm must be included before a norm inequality can be stated.

These are existing analytic obligations, not hidden in the finite-index factorization. The value of the comparison is that it specifies a coupled contour direction whose elementary conductor arithmetic is favorable, whereas holding w fixed is not.

## 5. Exact local checks and result of this component

The main rational identity can be checked without any analytic or floating-point input by clearing denominators:

\[
(1-x+z)(1-xz)
-(1-x)(1+z)
=x^2z-xz^2.
\tag{5.1}
\]

The n-prime formula is checked by

\[
\frac{(1+(q-1)x)(1-z)}{1-x}
\frac{1-xz}{1-z^2}
=\frac{(1+(q-1)x)(1-xz)}{(1-x)(1+z)}.
\tag{5.2}
\]

The literal zero-mask case x=z=0 gives one in all local factors. The executable [exact checker](checks/check_euler_factors.py) verifies the polynomial identities, rational examples, zero masks, linear-extraction coefficients, both numerator contour exponents, and the exact cube cancellation in the companion continuation theorem. Its acceptance checks remain active under Python optimization. The output in [euler_factor_checks.json](results/euler_factor_checks.json) records these finite checks; the proofs, rather than the examples, establish the infinite analytic statements.

The completed result is an explicit factorization with a normally convergent cubic remainder, a larger fixed-index continuation domain, and an exact identification of the new reciprocal as finite order. The optional linear extraction also gives holomorphic continuation throughout Re(w)>0, Re(v)>1/2. These statements preserve the Ramanujan interference and all moving zeros. The full generalized 2k-th moment remains dependent on a sufficiently strong estimate for the correlated theta family and its original angular reciprocal on the required contour.
