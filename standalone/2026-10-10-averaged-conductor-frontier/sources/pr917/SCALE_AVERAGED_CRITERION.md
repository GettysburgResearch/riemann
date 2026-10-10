# A scale-averaged generalized moment criterion

Status: proposed proved reduction, with a complete causal-operator argument. The arithmetic moment hypothesis in Section 4 remains open. No new zero-free half-plane is asserted.

Scope: the exact zero-extended Möbius/sextic family over K = Q(sqrt(-3)); all fixed moment orders; a moving row height H = D^h; and a single compactly supported smooth test. The moment upper bound is needed only after averaging over a dyadic interval of the column scale D.

Dependencies: the elementary ideal count in this field, exact Euler-factor removal, and the universal Mellin test proved in PR #912 at head `6afd64e042ce7b59d550c3d76e9e2cca8b2c7379`, `MELLIN_AND_SPIKES.md`, Proposition 1.1. The fixed-cutoff operator developed in the accompanying `AVERAGED_MASK_OPERATORS.md` motivated the proof. The moving-cutoff argument below is given explicitly, because a cutoff cannot be moved inside an integral by a change of notation.

## 1. Exact replicas and their averaged operator

For a fixed finite-order Hecke character \(\nu\), a fixed excluded-prime set \(S\), and the literal sextic symbol, write

\[
A_u(D;W)=\sum_{(n,S)=1}\mu_K(n)\nu(n)\chi_n(u)W(Nn/D),
\qquad \chi_n(u)=(u/n)_6.
\tag{1.1}
\]

Fix a nonzero element \(r\). Set \(\eta_r(n)=\nu(n)\chi_n(r)\) on ideals outside \(S\), and extend it by zero at \(S\). This is completely multiplicative, with \(|\eta_r(n)|\le1\). In this section any completely multiplicative \(\eta\) with this bound is allowed.

For an ideal \(v\), choose one generator and define the causal dilation operator

\[
(T_v f)(x)=\sum_{\operatorname{rad}(d)\mid v}\eta(d)f(x/Nd).
\tag{1.2}
\]

Here \(\operatorname{rad}(d)\) is the squarefree radical ideal. When \(f\) vanishes below a positive scale, this sum is finite for each \(x\). For the arithmetic function \(f(x)=A_r(x;W)\), the exact identity is

\[
\boxed{T_v f(x)=A_{r v^6}(x;W).}
\tag{1.3}
\]

Indeed, at a prime of \(v\), multiplying the inverse Euler series \(1-\eta(p)(Np)^{-s}\) by its geometric inverse removes precisely the terms divisible by that prime. This is the same as the original zero-extended factor \(\chi_n(v^6)={\bf1}_{(n,v)=1}\). The coefficient identity is finite at each ideal, so (1.3) does not require an analytic continuation or an exchange of divergent series. Replacing the chosen generator of \(v\) by a unit does not change \(v^6\).

Let \(J(Y)\) count integral ideals of norm at most \(Y\). Define \(J(Y)=0\) for \(Y<1\). Elementary lattice counting, using class number one, gives

\[
J(Y)=\kappa_KY+O_K(Y^{1/2}),\qquad J(Y)\asymp_KY\quad(Y\ge1).
\tag{1.4}
\]

For \(Y\ge1\), average over every ideal base:

\[
(M_Y f)(x)=\frac1{J(Y)}\sum_{Nv\le Y}T_v f(x)
=\sum_d\eta(d)w_Y(d)f(x/Nd),
\qquad
w_Y(d)=\frac{J(Y/N\operatorname{rad}(d))}{J(Y)}.
\tag{1.5}
\]

The density is exact: \(\operatorname{rad}(d)\mid v\) if and only if \(v=\operatorname{rad}(d)b\), and norms multiply. No coprimality restriction between the base and the fixed row is imposed.

## 2. Uniform approximation and a causal inverse

For \(\sigma>0\), put

\[
\|f\|_{p,\sigma;(a,b)}=
\left(\int_a^b|f(x)|^p x^{-p\sigma}\frac{dx}{x}\right)^{1/p},
\qquad 1\le p<\infty.
\tag{2.1}
\]

The dilation \(f(x)\mapsto f(x/Nd)\) has norm at most \((Nd)^{-\sigma}\) on a finite interval \((0,T)\). On \((X_0,T)\), the same statement holds for functions extended by zero below \(X_0\). Therefore a series of dilations with coefficient majorant \(c_d\ge0\) has norm at most \(\sum_dc_d(Nd)^{-\sigma}\). This remains true if each actual coefficient depends on \(x\), provided the majorant is uniform in \(x\).

Write \(R=N\operatorname{rad}(d)\). From (1.4), uniformly for \(Y\ge1\),

\[
w_Y(d)\ll_KR^{-1},\qquad
|w_Y(d)-R^{-1}|
\ll_K\min\{R^{-1},Y^{-1/2}R^{-1/2}\}.
\tag{2.2}
\]

For \(R\le Y\), insert (1.4) into the ratio in (1.5); its error is \(O(Y^{-1/2}R^{-1/2})\), and the first bound in (2.2) gives the other estimate. For \(R>Y\), the ratio is zero and the difference is exactly \(R^{-1}\). Thus both cases are included.

Fix

\[
0<\delta<\min(\sigma,1/2).
\]

The geometric interpolation of the two quantities in (2.2) gives

\[
|w_Y(d)-R^{-1}|\ll_K Y^{-\delta}R^{-1+\delta}.
\tag{2.3}
\]

The required weighted sums converge:

\[
\sum_d R^{-1+\delta}(Nd)^{-\sigma}
=\prod_p\left(1+\frac{(Np)^{-1+\delta-\sigma}}
 {1-(Np)^{-\sigma}}\right)<\infty.
\tag{2.4}
\]

Convergence follows from \(\delta<\sigma\) and convergence of the ideal zeta series to the right of one. In particular, the limiting operator

\[
(Mf)(x)=\sum_d\frac{\eta(d)}{N\operatorname{rad}(d)}f(x/Nd)
\tag{2.5}
\]

is bounded on every space (2.1), uniformly in \(\eta\). Its Euler factor, with \(S_p f(x)=f(x/Np)\) and \(q=Np\), is

\[
M_p=\frac{1-(1-q^{-1})\eta(p)S_p}{1-\eta(p)S_p}.
\tag{2.6}
\]

It has the explicit inverse

\[
M_p^{-1}
=1-q^{-1}\sum_{j\ge1}(1-q^{-1})^{j-1}\eta(p)^jS_p^j.
\tag{2.7}
\]

Both Euler products converge in the algebra with coefficient norm \(\sum_d|c_d|(Nd)^{-\sigma}\): the nonconstant local norm is \(O_\sigma(q^{-1-\sigma})\). Hence \(M^{-1}\) is a bounded causal operator, with a bound depending on \(K,\sigma\), uniform in \(\eta\) and in a finite endpoint \(T\). Equations (2.2)–(2.4) also give

\[
\|M_Y-M\|_{p,\sigma}\ll_{K,\sigma,\delta}Y^{-\delta}.
\tag{2.8}
\]

These are norm-convergent dilation identities. They make no assertion about the reciprocal of a Hecke \(L\)-function near a zero.

## 3. The moving-cutoff lemma

### Theorem 3.1

Let \(Y(x)\ge c x^\rho\) for all sufficiently large \(x\), where \(c,\rho>0\), and let \(f\) be measurable, locally bounded, and zero below a positive scale. Set

\[
P f(x)=M_{Y(x)}f(x)
\]

where \(Y(x)\ge1\). If

\[
\int_{X_1}^{\infty}|P f(x)|^p x^{-p\sigma}\frac{dx}{x}<\infty,
\tag{3.1}
\]

then

\[
\int_0^\infty|f(x)|^p x^{-p\sigma}\frac{dx}{x}<\infty.
\tag{3.2}
\]

Here \(1\le p<\infty\), \(\sigma>0\), and \(X_1\) can be any fixed sufficiently large number. There is no regularity requirement on \(Y(x)\) beyond measurability and the displayed lower bound.

### Proof

Choose \(\delta\) as in Section 2 and then \(X_0\ge X_1\) sufficiently large. On functions \(g\) extended by zero below \(X_0\), equations (2.3)–(2.4) give, for \(X_0\le x\le T\),

\[
|(P-M)g(x)|
\ll c^{-\delta}X_0^{-\rho\delta}
\sum_d (N\operatorname{rad}(d))^{-1+\delta}|g(x/Nd)|.
\tag{3.3}
\]

Thus the norm of \(E=P-M\) on this space is \(O(c^{-\delta}X_0^{-\rho\delta})\), uniformly in \(T\). Since \(M^{-1}\) is causal and bounded, it preserves the zero-below-\(X_0\) subspace. Increase \(X_0\) until \(\|M^{-1}E\|\le1/2\). The Neumann series then gives a uniformly bounded inverse for \(P=M(I+M^{-1}E)\) on \((X_0,T)\).

Split \(f=f_0+f_1\), with \(f_0\) supported below \(X_0\) and \(f_1\) zero there. By local boundedness and the positive lower support, \(\|f_0\|_{p,\sigma;(0,\infty)}<\infty\). The first bound in (2.2) majorizes \(P f_0\) by

\[
C_K\sum_d (N\operatorname{rad}(d))^{-1}|f_0(x/Nd)|.
\]

This is a bounded operator in the same norm, by (2.4) with \(\delta=0\). Consequently \(P f_0\) has finite weighted norm even on the infinite upper interval. Applying the finite-\(T\) inverse to \(P f_1=P f-P f_0\) gives

\[
\|f_1\|_{p,\sigma;(X_0,T)}
\ll \|P f\|_{p,\sigma;(X_0,\infty)}
  +\|f_0\|_{p,\sigma;(0,\infty)},
\tag{3.4}
\]

uniformly in \(T\). Letting \(T\to\infty\) proves (3.2). All uses of an inverse were on a finite interval with a causal operator; no integrability of the unknown \(f_1\) at infinity was assumed. \(\square\)

## 4. A dyadic-scale moment hypothesis suffices

Use the single nonnegative test \(W_*\in C_c^\infty((1,2))\) from PR #912, whose Mellin transform is nonzero for \(\Re s>0\). Define

\[
M_{2k}(D,H)=\sum_{0<Nu\le H}|A_u(D;W_*)|^{2k},
\qquad
Q_{2k,h}(X)=\int_X^{2X} M_{2k}(D,D^h)\frac{dD}{D}.
\tag{4.1}
\]

### Theorem 4.1. Scale-averaged extraction

Fix an integer \(k\ge1\), \(h>0\), and \(e_k\ge0\). Suppose that, for every \(\epsilon>0\) and every \(X\ge2\),

\[
\boxed{Q_{2k,h}(X)\ll_{k,h,\epsilon,\nu,S}X^{h+k+e_k+\epsilon}.}
\tag{4.2}
\]

Then every primitive Hecke \(L\)-function induced by \(n\mapsto\nu(n)\chi_n(r)\), for a fixed nonzero element \(r\), is zero-free in the strict half-plane

\[
\boxed{\Re s>\beta_{k,h,e}
=\frac12+\frac{5h}{12k}+\frac{e_k}{2k}.}
\tag{4.3}
\]

This is an implication from (4.2). The hypothesis is not proved here. Constants in the conclusion may depend on the fixed row \(r\); no uniform bound in its conductor is needed for this direction.

### Proof

Fix \(r\), set \(p=2k\), and choose \(\sigma>\beta_{k,h,e}\). For sufficiently large \(D\), let

\[
Y_r(D)=\left(\frac{D^h}{Nr}\right)^{1/6}.
\tag{4.4}
\]

The ideals \(v\) with \(Nv\le Y_r(D)\) give distinct element rows \(r v^6\) with norm at most \(D^h\). Jensen's inequality, the exact identity (1.3), and (1.4) give

\[
\begin{split}
|M_{Y_r(D)} A_r(D)|^{2k}
&\le\frac1{J(Y_r(D))}\sum_{Nv\le Y_r(D)}|A_{rv^6}(D)|^{2k}\\
&\ll_{K,r} D^{-h/6} M_{2k}(D,D^h).
\end{split}
\tag{4.5}
\]

Using (4.2) on \([X,2X]\), the integral of the right side times \(D^{-2k\sigma}\) is at most a constant times

\[
X^{k+5h/6+e_k-2k\sigma+\epsilon}.
\tag{4.6}
\]

Choose \(\epsilon>0\) smaller than \(2k\sigma-k-5h/6-e_k\). Summing (4.6) over dyadic \(X\) converges. The moving-cutoff theorem, with \(\rho=h/6\) and \(c=(Nr)^{-1/6}\), therefore proves

\[
\int_0^\infty |A_r(D;W_*)|^{2k}D^{-2k\sigma}\frac{dD}{D}<\infty.
\tag{4.7}
\]

The arithmetic function is locally bounded and is zero for \(D\) below a positive constant, so all the other hypotheses of Theorem 3.1 hold.

Hölder's inequality now makes

\[
F_r(s)=\int_0^\infty A_r(D;W_*)D^{-s}\frac{dD}{D}
\tag{4.8}
\]

absolutely convergent and holomorphic in \(\Re s>\sigma\). Logarithmic derivatives are dominated on each smaller closed half-plane by the same inequality. For \(\Re s>1\), direct Mellin inversion of the finite-scale sums gives

\[
F_r(s)=\widehat W_*(s)\frac{E_r(s)}{L_K(s,\psi_r)},
\tag{4.9}
\]

where \(\psi_r\) is the primitive inducing character and \(E_r\) is the finite product restoring the deleted Euler factors. Every factor of \(E_r\) is nonzero and holomorphic in \(\Re s>0\). The same is true of \(\widehat W_*\) there. By the identity theorem for meromorphic functions, a zero of \(L_K(s,\psi_r)\) in \(\Re s>\sigma\) would produce a pole of the holomorphic function \(F_r\), which is impossible. The principal pole of an \(L\)-function produces a zero of its reciprocal and causes no exception.

Finally let \(\sigma\) decrease to (4.3). Every point in the strict half-plane is covered by some intermediate \(\sigma\). \(\square\)

### Corollary 4.2. Cofinal orders approach the full hypothesis

Suppose (4.2) holds along an unbounded sequence of fixed integer orders \(k\), with \(h=h_k>0\),

\[
h_k=o(k),\qquad e_k=o(k).
\tag{4.10}
\]

Then the twist family in Theorem 4.1 has no zero with real part greater than \(1/2\). If the hypotheses hold for every fixed finite-order \(\nu\), this gives the GRH conclusion for the finite-order Hecke family over \(K\), by the functional equation and complex conjugation. The usual factorization over this quadratic field then gives the corresponding Dirichlet-family conclusion. These remain conditional consequences of the unproved cofinal arithmetic hypotheses.

For the intended fixed \(h=1+\theta\), \(0<\theta\le1/10\), and diagonal moments \(e_k=0\), the extraction exponent is unchanged:

\[
\beta_k=\frac12+\frac{5(1+\theta)}{12k}.
\tag{4.11}
\]

The difference is in the input: (4.2) permits exceptional individual scales and asks only for the dyadic integral. A pointwise bound of the desired size immediately implies (4.2). The proof does not infer such a pointwise bound from its averaged version.

## 5. What this contributes to the current attack

The exact removal identities provide a quantitative and invertible mean operator on every positive weighted scale space. This allows a weaker, scale-averaged version of the original generalized moment estimate to drive the same zero-free extraction. No finite expansion into dominant Mellin modes, selection of record scales, pointwise bound on the Möbius sum, or derivative estimate is required.

The averaging theorem supplies the implication after an arithmetic upper bound is available. It does not supply that upper bound. In particular, the new cubic common-gcd estimate in `OSCILLATING_OVERLAPS.md` still leaves the nearly coprime balanced contribution open, both pointwise and in the dyadic integral (4.2). A proof of that remaining averaged estimate would be sufficient progress for this route; a proof at every individual column scale is no longer required.
