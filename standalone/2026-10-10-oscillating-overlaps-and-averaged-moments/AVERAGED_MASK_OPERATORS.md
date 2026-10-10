# Averaged Euler removals: uniform coercivity, Mellin separation, and a sharp limitation

**Status:** new self-contained proofs, 2026-10-10; draft for independent review. The fixed-range coercivity theorem below is unconditional. The finite-mode application has an explicit additional asymptotic hypothesis. The synthetic model is an obstruction to deductions from removal identities alone, not a model of the actual Möbius coefficients.

**Scope:** ideals of the Eisenstein field \(K=\mathbb Q(\sqrt{-3})\), the exact sixth-power row masks in the October 5 Möbius/sextic family, and their action on arbitrary functions of the physical scale. Constants are uniform in the moving mask, scale, and fixed core. No new near-diagonal higher-moment upper bound, zero-free region, or proof of RH is claimed.

**Exact dependencies:** the original family and inverse-mask identity in PR 913, head \(6498d6cc2eded03159c7332b25fd224ad07f89c1\), files MOMENT_OBSTRUCTIONS.md, Sections 1 and 3, and GENERAL_MOMENT_ATTACK.md, Section 6. Their upstream source is OpenAI math commit \(adc7f1241b42e322a6451854ab7e4b4c146bf78a\), October 5 paper2.tex. All ideal counting, averaging, operator inversion, and separation arguments used here are proved below. No large sieve or imported zero-free theorem enters these proofs.

**What was actually done:** exact ideal-divisor manipulations, norm-convergent Euler products, bounded-operator estimates, and finite-dimensional linear algebra. No numerical zero test or computation is used to support an infinite assertion.

**Smallest remaining gap:** a cancellation estimate for the actual Möbius/sextic sums on the long balanced cores. The removal identities transmit such cancellation, but the final model shows that they do not supply a saving in the growth exponent by themselves.

## 1. Exact setting and the new conclusions

Write \(q=N\mathfrak p\) for the norm of a prime ideal, and let \(\operatorname{rad}d\) be the squarefree radical of an integral ideal \(d\). Every sum over an ideal below includes the unit ideal. Fix a completely multiplicative function \(\eta\) on integral ideals with

\[
\eta(1)=1,\qquad |\eta(d)|\le 1.
\tag{1.1}
\]

Zero values are allowed. For the actual family and a fixed nonzero core row \(r\), take

\[
\eta(d)=\nu(d)\chi_d(r),
\tag{1.2}
\]

including the original zero extensions at primes in the fixed bad set and at primes meeting \(r\).

For a function \(f\) on \((0,\infty)\), put

\[
S_df(x)=f(x/Nd),\qquad
T_vf(x)=\sum_{d\mid v^\infty}\eta(d)f(x/Nd).
\tag{1.3}
\]

The condition \(d\mid v^\infty\) means that every prime dividing \(d\) divides \(v\); its exponent in \(d\) is unrestricted. If \(f\) vanishes below a positive scale, the sum is finite at each \(x\). More general norm-convergent interpretations are supplied in Section 4.

In the arithmetic application the exact identity is

\[
A_{rv^6}(x;W)=T_vA_r(x;W).
\tag{1.4}
\]

There is no condition \((r,v)=1\). A prime at which \(\eta(\mathfrak p)=0\) contributes the identity operator, exactly as required by the nonunit zero extension. For a prime \(\mathfrak p\nmid v\),

\[
(I-\eta(\mathfrak p)S_{\mathfrak p})T_{v\mathfrak p}=T_v.
\tag{1.5}
\]

The new quantitative conclusions are:

1. Averaging the size of \(T_v\) over \(Nv\le Y\) costs a constant depending on the exponent, with no \(Y^\epsilon\) loss.
2. The mean of the exact removal operators converges in a causal dilation algebra to an explicitly invertible Euler product.
3. Consequently, for every fixed \(\sigma>0\) and \(1\le p<\infty\), there are constants \(c,C>0\) such that

\[
c\int_0^T |f(x)|^p x^{-p\sigma}\frac{dx}{x}
\le
\frac{1}{J(Y)}\sum_{Nv\le Y}
\int_0^T |T_vf(x)|^p x^{-p\sigma}\frac{dx}{x}
\le
C\int_0^T |f(x)|^p x^{-p\sigma}\frac{dx}{x}
\tag{1.6}
\]

for every \(Y\ge1\), every \(T>0\), and every function with finite norm on the right. Here

\[
J(Y)=\#\{v:Nv\le Y\}.
\tag{1.7}
\]

The same value of \(Y\) is used for every \(x\) in (1.6). A moving cutoff requires a separate argument, given in Section 7.

Thus the family of masks detects arbitrary weighted \(L^p\) mass, not only one Mellin mode or a large value at a record scale. This is a two-sided transfer theorem, not an upper cancellation estimate for the base function.

## 2. Ideal counts and their uniform divisibility error

### Lemma 2.1. Counting ideals and masks

There is a positive constant \(\kappa_K\) such that

\[
J(t)=\kappa_Kt+O_K(\sqrt t)\qquad(t>0).
\tag{2.1}
\]

There are constants \(c_K,C_K>0\) such that

\[
c_KY\le J(Y)\le C_KY\qquad(Y\ge1),
\tag{2.2}
\]

and \(J(t)\le C_Kt\) for all \(t>0\). For an ideal \(d\), write \(R_d=N\operatorname{rad}d\), and set

\[
w_Y(d)=\frac{J(Y/R_d)}{J(Y)}\qquad(Y\ge1).
\tag{2.3}
\]

This is exactly the proportion of bases \(v\) with \(Nv\le Y\) for which \(d\mid v^\infty\). Uniformly in \(Y\ge1\) and \(d\),

\[
\left|w_Y(d)-\frac1{R_d}\right|
\le C_K\min\left\{\frac1{R_d},
                  \frac{1}{Y^{1/2}R_d^{1/2}}\right\}.
\tag{2.4}
\]

Consequently, for \(0<\delta\le1/2\),

\[
\left|w_Y(d)-\frac1{R_d}\right|
\le C_K Y^{-\delta}R_d^{-1+\delta}.
\tag{2.5}
\]

**Proof.** Every ideal in the Eisenstein ring is principal and has six generators of a given norm. Counting nonzero points of its fixed planar lattice inside a disk of radius \(\sqrt t\), and dividing by six, gives

\[
J(t)=\kappa_Kt+O_K(\sqrt t+1)\qquad(t\ge1).
\]

For \(t\ge1\), the error is \(O_K(\sqrt t)\). For \(0<t<1\), \(J(t)=0\), and \(\kappa_Kt=O_K(\sqrt t)\). This proves (2.1) on its full stated domain. The upper bound follows at once, and the lower bound for large \(Y\), combined with \(J(Y)\ge1\) on the remaining bounded interval, proves (2.2).

The condition \(d\mid v^\infty\) is equivalent to \(\operatorname{rad}d\mid v\). Writing \(v=\operatorname{rad}d\,w\) proves (2.3). The estimate \(J(t)\ll_Kt\) and (2.2) give \(w_Y(d)\ll_KR_d^{-1}\), which gives the first bound in (2.4).

For the other bound, use (2.1) in the numerator and denominator:

\[
\begin{aligned}
J(Y/R_d)-R_d^{-1}J(Y)
&=O_K\left(\sqrt{Y/R_d}+R_d^{-1}\sqrt Y\right).
\end{aligned}
\]

After division by \(J(Y)\gg_KY\), and since \(R_d\ge1\), this is \(O_K(Y^{-1/2}R_d^{-1/2})\). This reasoning remains valid when \(R_d>Y\); (2.1) was stated for all positive arguments. Finally use

\[
\min(a,b)\le a^{1-2\delta}b^{2\delta}
\]

with \(a=R_d^{-1}\), \(b=Y^{-1/2}R_d^{-1/2}\). \(\square\)

All bases in this lemma are unrestricted integral ideals. This is the correct set for the row decomposition. Excluded coefficient primes have already been represented by \(\eta(\mathfrak p)=0\); they need not be excluded from the base count.

## 3. Averaging the Euler-factor norm without a power loss

For \(\sigma>0\), define

\[
E_\sigma(v)=
\sum_{d\mid v^\infty}(Nd)^{-\sigma}
=\prod_{\mathfrak p\mid v}(1-q^{-\sigma})^{-1}.
\tag{3.1}
\]

### Theorem 3.1. Bounded mean Euler norm

For every fixed \(\sigma>0\) and real \(p>0\),

\[
\sum_{Nv\le Y} E_\sigma(v)^p
\le C_{K,\sigma,p}Y\qquad(Y\ge1).
\tag{3.2}
\]

In particular, its average over \(Nv\le Y\) is bounded uniformly in \(Y\).

**Proof.** Put \(G_{\mathfrak p}=(1-q^{-\sigma})^{-p}\), and define the nonnegative multiplicative function \(h\), supported on squarefree ideals, by

\[
h(\mathfrak p)=G_{\mathfrak p}-1,\qquad
h(\mathfrak p^j)=0\quad(j\ge2).
\]

The exact finite divisor expansion is

\[
E_\sigma(v)^p=\sum_{d\mid v}h(d).
\]

Using Lemma 2.1 and nonnegativity,

\[
\begin{aligned}
\sum_{Nv\le Y}E_\sigma(v)^p
&=\sum_{Nd\le Y}h(d)J(Y/Nd)\\
&\le C_KY\sum_d\frac{h(d)}{Nd}\\
&=C_KY\prod_{\mathfrak p}
       \left(1+\frac{(1-q^{-\sigma})^{-p}-1}{q}\right).
\end{aligned}
\tag{3.3}
\]

The product is finite: outside finitely many primes, its nonconstant term is \(O_{\sigma,p}(q^{-1-\sigma})\), and
\(\sum_{\mathfrak p}q^{-1-\sigma}<\infty\). The latter follows, for example, by comparison with the sum over all ideals and the elementary count \(J(t)\ll_Kt\). Divide by \(J(Y)\gg_KY\) for the normalized version. \(\square\)

### Corollary 3.2. Fixed-core pointwise transfer without \(D^\epsilon\)

Fix \(p\ge1\), \(\sigma>0\), and \(D>0\). If

\[
C_f(D;\sigma)=\sup_{0<x\le D}x^{-\sigma}|f(x)|<\infty,
\]

then, for every \(Y\ge1\),

\[
\sum_{Nv\le Y}|T_vf(D)|^p
\ll_{K,\sigma,p}Y D^{p\sigma} C_f(D;\sigma)^p.
\tag{3.4}
\]

**Proof.** Formula (1.3) and \(|\eta|\le1\) give

\[
|T_vf(D)|\le C_f(D;\sigma)D^\sigma E_\sigma(v).
\]

Raise to the \(p\)-th power and apply Theorem 3.1. \(\square\)

For the actual family, the exact row factorization \(u=rv^6\), with the unit retained in the sixth-power-free core \(r\), gives the following fully summed form:

\[
\begin{aligned}
\sum_{0<Nu\le H}|A_u(D)|^p
\ll_{K,\sigma,p}D^{p\sigma}
\sum_{\substack{0<Nr\le H\\r\ {\rm sixth\text{-}power\text{-}free}}}
\left(\frac H{Nr}\right)^{1/6}
\sup_{0<x\le D}\frac{|A_r(x)|^p}{x^{p\sigma}}.
\end{aligned}
\tag{3.5}
\]

Indeed the base cutoff for that single core is \(Y_r=(H/Nr)^{1/6}\ge1\), and Corollary 3.2 applies with the same constant to every core. This removes the preliminary \((HD)^\epsilon\) in the individual-mask version of the transfer. It does not remove logarithms that may separately arise when a proposed core estimate is summed over many dyadic core ranges.

## 4. The causal dilation algebra and its invertible mean

For \(\sigma>0\), let \(\mathscr A_\sigma\) be the ideal Dirichlet-convolution algebra of coefficient sequences \(c=(c_d)\) with

\[
\|c\|_{\mathscr A_\sigma}
=\sum_d |c_d|(Nd)^{-\sigma}<\infty.
\tag{4.1}
\]

Its identity is the sequence supported at the unit ideal. Multiplicativity of the norm gives

\[
\|c*e\|_{\mathscr A_\sigma}
\le\|c\|_{\mathscr A_\sigma}\|e\|_{\mathscr A_\sigma}.
\tag{4.2}
\]

Completeness is the completeness of a weighted \(\ell^1\) space. The corresponding dilation operator is

\[
c(S)f=\sum_dc_dS_df.
\tag{4.3}
\]

Fix \(1\le p<\infty\) and \(T>0\), and equip \((0,T)\) with the norm

\[
\|f\|_{p,\sigma;T}
=\left(\int_0^T|f(x)|^px^{-p\sigma}\frac{dx}{x}\right)^{1/p}.
\tag{4.4}
\]

The substitution \(x=(Nd)y\) gives

\[
\|S_df\|_{p,\sigma;T}
^p
=(Nd)^{-p\sigma}
\int_0^{T/Nd}|f(y)|^py^{-p\sigma}\frac{dy}{y}
\le (Nd)^{-p\sigma}\|f\|_{p,\sigma;T}^p.
\tag{4.5}
\]

Therefore (4.3) converges in this space and

\[
\|c(S)f\|_{p,\sigma;T}
\le\|c\|_{\mathscr A_\sigma}\|f\|_{p,\sigma;T}.
\tag{4.6}
\]

Composition agrees with Dirichlet convolution, first for finite sequences and then by norm convergence. Every dilation is causal in the scale variable: the output at \(x\) uses only values at arguments at most \(x\). In particular, these are operator identities on the finite interval itself; no integrability beyond \(T\) is assumed.

The coefficients of \(T_v\) are in \(\mathscr A_\sigma\), with norm at most \(E_\sigma(v)\).

Define the mean operator

\[
M_Y=\frac1{J(Y)}\sum_{Nv\le Y}T_v.
\tag{4.7}
\]

Interchanging its finite outer sum with its absolutely summable coefficient sequences gives the exact algebra identity

\[
M_Y=\sum_d\eta(d)w_Y(d)S_d.
\tag{4.8}
\]

### Theorem 4.1. Quantitative mean limit and explicit inverse

For every \(\sigma>0\), the algebra element

\[
M=\sum_d\frac{\eta(d)}{N\operatorname{rad}d}S_d
\tag{4.9}
\]

belongs to \(\mathscr A_\sigma\) and is invertible there. For every

\[
0<\delta<\min(\sigma,1/2),
\tag{4.10}
\]

one has

\[
\|M_Y-M\|_{\mathscr A_\sigma}
\le C_{K,\sigma,\delta}Y^{-\delta}.
\tag{4.11}
\]

There are \(Y_0=Y_0(K,\sigma,\delta)\) and \(C_0=C_0(K,\sigma)>0\), independent of \(\eta\) subject to (1.1), such that

\[
M_Y^{-1}\in\mathscr A_\sigma,\qquad
\|M_Y^{-1}\|_{\mathscr A_\sigma}\le C_0
\quad(Y\ge Y_0).
\tag{4.12}
\]

**Proof.** The positive majorant for (4.9) has Euler product

\[
\sum_d\frac{(Nd)^{-\sigma}}{N\operatorname{rad}d}
=\prod_{\mathfrak p}
\left(1+\frac{q^{-\sigma}}{q(1-q^{-\sigma})}\right)<\infty.
\tag{4.13}
\]

The local nonconstant term is \(O_\sigma(q^{-1-\sigma})\).

For convergence, Lemma 2.1 gives

\[
\begin{aligned}
\|M_Y-M\|_{\mathscr A_\sigma}
&\le C_KY^{-\delta}
\sum_d (Nd)^{-\sigma}(N\operatorname{rad}d)^{-1+\delta}.
\end{aligned}
\tag{4.14}
\]

The last sum equals

\[
\prod_{\mathfrak p}
\left(1+
\frac{q^{-1+\delta-\sigma}}{1-q^{-\sigma}}\right),
\tag{4.15}
\]

and converges because \(\delta<\sigma\). This proves (4.11), with a constant uniform in \(\eta\).

To invert \(M\), use the local formal variable \(z=\eta(\mathfrak p)S_{\mathfrak p}\). The local factor of \(M\) is

\[
1+\frac1q\sum_{j\ge1}z^j
=\frac{1-(1-1/q)z}{1-z}.
\tag{4.16}
\]

Its inverse is

\[
\frac{1-z}{1-(1-1/q)z}
=1-\frac1q\sum_{j\ge1}(1-1/q)^{j-1}z^j.
\tag{4.17}
\]

Thus the inverse coefficients are multiplicative, and on prime powers they are

\[
a_{\mathfrak p^j}
=-\frac{\eta(\mathfrak p)^j}{q}(1-1/q)^{j-1}
\qquad(j\ge1).
\tag{4.18}
\]

Their norm has the uniform bound

\[
\|M^{-1}\|_{\mathscr A_\sigma}
\le
\prod_{\mathfrak p}
\left(1+
\frac{q^{-1-\sigma}}
     {1-(1-1/q)q^{-\sigma}}\right)
=:B_{K,\sigma}<\infty.
\tag{4.19}
\]

Finite-prime multiplication proves the inverse identity locally. Both products converge in the algebra, so the identity persists on taking their limits.

Finally choose \(Y_0\) so that

\[
\|M^{-1}(M_Y-M)\|_{\mathscr A_\sigma}\le\tfrac12
\quad(Y\ge Y_0).
\]

The Neumann series in the Banach algebra gives

\[
M_Y^{-1}
=\left(I+M^{-1}(M_Y-M)\right)^{-1}M^{-1},
\quad
\|M_Y^{-1}\|_{\mathscr A_\sigma}\le2B_{K,\sigma}.
\tag{4.20}
\]

All inverses constructed this way remain causal dilation operators. \(\square\)

For interpretation on the Mellin line, the multiplier of \(M\) is

\[
m(s)=
\prod_{\mathfrak p}
\frac{1-(1-1/q)\eta(\mathfrak p)q^{-s}}
     {1-\eta(\mathfrak p)q^{-s}},
\qquad \Re s>0.
\tag{4.21}
\]

The product and its reciprocal converge absolutely and locally uniformly in that half-plane. Neither numerator nor denominator local factor vanishes there, since the relevant moduli are less than one. Therefore \(m\) is holomorphic and nowhere zero on \(\Re s>0\). Equation (4.19) supplies a bound for the reciprocal that is uniform in the imaginary part on each fixed line \(\Re s=\sigma>0\).

This auxiliary nonvanishing statement concerns the mean mask multiplier. It is not a nonvanishing theorem for the original Hecke \(L\)-function.

## 5. Two-sided weighted \(L^p\) coercivity at finite scale

### Theorem 5.1. Uniform finite-range coercivity

Fix \(\sigma>0\) and \(1\le p<\infty\). There are \(c,C>0\), depending only on \(K,\sigma,p\), such that for every function \(\eta\) satisfying (1.1), every \(Y\ge1\), every \(T>0\), and every measurable \(f\) with \(\|f\|_{p,\sigma;T}<\infty\),

\[
c\|f\|_{p,\sigma;T}^p
\le \frac1{J(Y)}\sum_{Nv\le Y}
\|T_vf\|_{p,\sigma;T}^p
\le C\|f\|_{p,\sigma;T}^p.
\tag{5.1}
\]

The same assertions hold on the full interval \((0,\infty)\) when the indicated base norm is finite.

**Proof.** Equation (4.6) gives

\[
\|T_vf\|_{p,\sigma;T}\le E_\sigma(v)\|f\|_{p,\sigma;T}.
\]

The upper bound follows from Theorem 3.1 and \(J(Y)\asymp_KY\).

For \(Y\ge Y_0\), Theorem 4.1 and (4.6) give

\[
\|f\|_{p,\sigma;T}
=\|M_Y^{-1}M_Yf\|_{p,\sigma;T}
\le 2B_{K,\sigma}\|M_Yf\|_{p,\sigma;T}.
\tag{5.2}
\]

Pointwise convexity, followed by integration, gives

\[
\|M_Yf\|_{p,\sigma;T}^p
\le \frac1{J(Y)}
\sum_{Nv\le Y}\|T_vf\|_{p,\sigma;T}^p.
\tag{5.3}
\]

Combining (5.2) and (5.3) gives the lower constant \((2B_{K,\sigma})^{-p}\) on this range. For \(1\le Y<Y_0\), retain just the unit ideal \(v=1\), for which \(T_1f=f\). Then

\[
\frac1{J(Y)}\sum_{Nv\le Y}\|T_vf\|_{p,\sigma;T}^p
\ge\frac{\|f\|_{p,\sigma;T}^p}{J(Y)}
\ge\frac{\|f\|_{p,\sigma;T}^p}{J(Y_0)}.
\]

Thus one may take \(c=\min((2B_{K,\sigma})^{-p},J(Y_0)^{-1})>0\) for all \(Y\ge1\). The proof uses only the bounded operators on \((0,T)\), so the constants do not depend on \(T\). The full-interval assertion follows by the same operator proof or by monotone convergence in \(T\). \(\square\)

For the arithmetic application, \(A_r(x;W)=0\) below a positive constant depending only on the support of \(W\), and it is bounded on every compact scale interval. Its finite-\(T\) weighted norm is therefore finite for every \(\sigma>0\). Theorem 5.1 applies without a smoothness or derivative estimate, uniformly in the core \(r\), since \(|\nu(d)\chi_d(r)|\le1\).

If a fixed row budget \(H\) and a fixed core \(r\) are used, the matching cutoff is

\[
Y=(H/Nr)^{1/6}.
\tag{5.4}
\]

It is fixed throughout the integration in (5.1). The theorem applies for every \(Nr\le H\), including cores with only a bounded number of permitted masks.

### Corollary 5.2. Two-sided integrated transfer over all cores

For fixed \(H\ge1\), \(T>0\), \(\sigma>0\), and \(1\le p<\infty\), the actual family satisfies

\[
\begin{aligned}
&\int_0^T\mathcal M_p(x,H)x^{-p\sigma}\frac{dx}{x}\\
&\qquad\asymp_{K,\sigma,p}
\sum_{\substack{0<Nr\le H\\r\ {\rm sixth\text{-}power\text{-}free}}}
\left(\frac H{Nr}\right)^{1/6}
\int_0^T |A_r(x)|^px^{-p\sigma}\frac{dx}{x}.
\end{aligned}
\tag{5.5}
\]

**Proof.** Decompose every row uniquely as \(u=rv^6\). For each fixed core, apply Theorem 5.1 at the fixed range \(Y_r=(H/Nr)^{1/6}\), multiply by \(J(Y_r)\), and use \(J(Y_r)\asymp_KY_r\). Sum over the finitely many cores. The constants are uniform in their functions \(\eta_r\), since all satisfy (1.1). \(\square\)

Both \(H\) and every associated \(Y_r\) in (5.5) are fixed while \(x\) is integrated. There is no supremum over smaller scales and no \(H^\epsilon\) or \(T^\epsilon\) loss in this equivalence.

## 6. Strict separation of finitely many Mellin modes

This section identifies a stronger every-scale consequence when a finite dominant Mellin expansion is already available. Unlike Theorem 5.1, that arithmetic application has an extra hypothesis.

For \(\Re z>0\), put

\[
F_v(z)=\prod_{\mathfrak p\mid v}
(1-\eta(\mathfrak p)q^{-z})^{-1}.
\tag{6.1}
\]

It is the exact eigenvalue in \(T_v(x^z)=F_v(z)x^z\).

### Lemma 6.1. Multiplicative mean formula

Let \(g(v)=\prod_{\mathfrak p\mid v}G_{\mathfrak p}\), where

\[
G_{\mathfrak p}-1=O(q^{-b})
\tag{6.2}
\]

for a fixed \(b>0\). The \(G_{\mathfrak p}\) may be complex, and finitely many exceptional factors cause no difficulty. For every \(0<\delta<\min(b,1/2)\),

\[
\frac1{J(Y)}\sum_{Nv\le Y}g(v)
=
\prod_{\mathfrak p}
\left(1+\frac{G_{\mathfrak p}-1}{q}\right)
+O(Y^{-\delta}).
\tag{6.3}
\]

The product is absolutely convergent. The constant depends on the fixed local factors, \(K,b,\delta\).

**Proof.** Define \(h\) multiplicatively, supported on squarefree ideals, by \(h(\mathfrak p)=G_{\mathfrak p}-1\). The exact divisor expansion \(g(v)=\sum_{d\mid v}h(d)\) gives the normalized average

\[
\sum_{d\ {\rm squarefree}}h(d)w_Y(d),
\]

where terms with \(Nd>Y\) vanish. The proposed limit is
\(\sum_d h(d)/(Nd)\). By Lemma 2.1 their difference has modulus at most

\[
C_KY^{-\delta}
\sum_{d\ {\rm squarefree}}\frac{|h(d)|}{(Nd)^{1-\delta}}.
\]

The last sum has convergent product
\(\prod_{\mathfrak p}(1+|G_{\mathfrak p}-1|q^{-1+\delta})\)
because \(\delta<b\). This proves the claim. \(\square\)

Apply the lemma to \(F_v(z)\overline{F_v(w)}\). For \(\Re z,\Re w>0\), it gives

\[
\begin{aligned}
K_Y(z,w)
&:=\frac1{J(Y)}\sum_{Nv\le Y}
F_v(z)\overline{F_v(w)}
\longrightarrow K(z,w),\\
K(z,w)
&=\prod_{\mathfrak p}\left[
1-\frac1q+
\frac1{q(1-\eta(\mathfrak p)q^{-z})
          (1-\overline{\eta(\mathfrak p)}q^{-\bar w})}
\right].
\end{aligned}
\tag{6.4}
\]

The error is \(O(Y^{-\delta})\) for
\(0<\delta<\min(\Re z,\Re w,1/2)\).

### Theorem 6.2. Strict Mellin-mode coercivity

Suppose that \(\eta(\mathfrak p)\ne0\) at primes lying over infinitely many distinct rational primes. Fix pairwise distinct \(z_1,\ldots,z_m\) with \(\Re z_j>0\). Then the matrix

\[
(K(z_i,z_j))_{1\le i,j\le m}
\tag{6.5}
\]

is positive definite. Consequently, for every fixed integer \(k\ge1\), there are constants \(c,C>0\) and \(Y_0\) such that, for every \(Y\ge Y_0\) and every coefficient vector \(c_1,\ldots,c_m\),

\[
c\left(\sum_j|c_j|^2\right)^k
\le
\frac1{J(Y)}\sum_{Nv\le Y}
\left|\sum_jc_jF_v(z_j)\right|^{2k}
\le
C\left(\sum_j|c_j|^2\right)^k.
\tag{6.6}
\]

Here the constants may depend on \(\eta\), the fixed modes, and \(k\).

**Proof.** Write

\[
a_{\mathfrak p}(z)=(1-\eta(\mathfrak p)q^{-z})^{-1}.
\]

At a prime where \(\eta(\mathfrak p)\ne0\), equality
\(a_{\mathfrak p}(z_i)=a_{\mathfrak p}(z_j)\) is equivalent to

\[
q^{z_i-z_j}=1.
\tag{6.7}
\]

If the real parts differ, (6.7) is impossible. If
\(z_i-z_j=i\tau\), \(\tau\ne0\), and (6.7) held at norms \(q=\ell^a\) and \(q'=(\ell')^{a'}\) above two distinct rational primes, then

\[
\tau a\log\ell=2\pi n,\qquad
\tau a'\log\ell'=2\pi n'
\]

for nonzero integers \(n,n'\). This would make
\(\log\ell/\log\ell'\) rational, contradicting unique factorization of rational integers. Thus for each distinct pair, infinitely many available primes separate their responses.

For each ordered pair \(i\ne j\), select a distinct available prime \(\mathfrak p_{ij}\) with
\(a_{\mathfrak p_{ij}}(z_i)\ne a_{\mathfrak p_{ij}}(z_j)\).
Let \(P\) be the finite set of all selected primes. For a mode index \(\ell\), define

\[
R_i(\ell)=\prod_{j\ne i}
\left(a_{\mathfrak p_{ij}}(z_\ell)
      -a_{\mathfrak p_{ij}}(z_j)\right).
\tag{6.8}
\]

Then \(R_i(i)\ne0\) and \(R_i(\ell)=0\) for \(\ell\ne i\). Expanding the product in (6.8) expresses this coordinate vector as a linear combination of

\[
\left(\prod_{\mathfrak p\in E}a_{\mathfrak p}(z_\ell)\right)_{\ell=1}^m,
\qquad E\subseteq P.
\tag{6.9}
\]

Hence the response vectors (6.9) span \(\mathbb C^m\).

Let independent Bernoulli variables select each prime of \(P\) with probability \(1/q\). Every subset \(E\subseteq P\) has positive probability. Therefore its response Gram matrix \(K_P\), whose entries are the product in (6.4) restricted to \(P\), is positive definite.

The complementary-prime matrix \(K_{\rm rest}\) is positive semidefinite: it is the entrywise limit of finite-prime Bernoulli Gram matrices. Each of its diagonal entries is strictly positive. Indeed each local diagonal factor is positive, differs from one by \(O(q^{-1-\Re z_i})\), and has an absolutely convergent product.

The full matrix is the entrywise product
\(K=K_P\circ K_{\rm rest}\). If \(\lambda>0\) is the least eigenvalue of \(K_P\), the Schur product theorem gives

\[
K-\lambda\operatorname{diag}(K_{\rm rest})
=(K_P-\lambda I)\circ K_{\rm rest}\ \succeq\ 0.
\]

Since every diagonal entry of \(K_{\rm rest}\) is strictly positive, \(K\) is positive definite. The Schur product assertion can also be seen directly by taking tensor products of vectors realizing the two positive semidefinite matrices as Gram matrices.

Entrywise convergence (6.4) now gives uniform two-sided quadratic bounds for \(K_Y\) once \(Y\ge Y_0\). Thus (6.6) holds for \(k=1\). For higher \(k\), Jensen gives

\[
\frac1{J(Y)}\sum_{Nv\le Y}|Z_v|^{2k}
\ge
\left(\frac1{J(Y)}\sum_{Nv\le Y}|Z_v|^2\right)^k.
\]

For the upper bound let \(b=\min_j\Re z_j>0\). Then

\[
\left|\sum_jc_jF_v(z_j)\right|
\le \sqrt m\,\left(\sum_j|c_j|^2\right)^{1/2}E_b(v).
\]

Apply Theorem 3.1 with exponent \(2k\). \(\square\)

The nonvanishing hypothesis on \(\eta\) holds for a fixed actual Hecke core, because only finitely many primes are removed. It is needed for strict separation: if \(\eta\) were zero at every prime, then all \(F_v(z)\) would equal one and different modes would be indistinguishable by these masks.

### Corollary 6.3. No leading finite-mode cancellation across masks

Assume the hypothesis on \(\eta\) in Theorem 6.2. Suppose \(f\) vanishes below a positive scale, is locally bounded, and has an expansion

\[
f(x)=\sum_{j=1}^m c_jx^{\beta+it_j}
      +O(x^{\beta-\epsilon_0})
\qquad(x\ge1),
\tag{6.10}
\]

where \(\beta>0\), \(0<\epsilon_0<\beta\), the \(t_j\) are distinct, and at least one \(c_j\ne0\). For each fixed integer \(k\ge1\), there are \(D_0,Y_0,c,C>0\) such that for every \(D\ge D_0\) and every \(Y\ge Y_0\),

\[
cYD^{2k\beta}
\le \sum_{Nv\le Y}|T_vf(D)|^{2k}
\le CYD^{2k\beta}.
\tag{6.11}
\]

**Proof.** The residual \(g=f-\sum_jc_jx^{\beta+it_j}\) satisfies

\[
|g(x)|\le Cx^{\beta-\epsilon_0}\qquad(x>0).
\tag{6.12}
\]

For \(x\ge1\) this is assumed; below one it follows from local boundedness, the positive lower support threshold, and \(x^\beta\le x^{\beta-\epsilon_0}\). Applying \(T_v\) gives

\[
T_vf(D)=D^\beta\sum_j c_jD^{it_j}F_v(\beta+it_j)
+O(D^{\beta-\epsilon_0}E_{\beta-\epsilon_0}(v)).
\tag{6.13}
\]

The normalized \(\ell^{2k}\) norm over \(Nv\le Y\) of the error is
\(O(D^{\beta-\epsilon_0})\), uniformly in \(Y\ge1\), by Theorem 3.1. The coefficient vector \((c_jD^{it_j})_j\) has fixed nonzero Euclidean norm. Theorem 6.2 therefore bounds the normalized \(\ell^{2k}\) norm of the leading term above and below by positive multiples of \(D^\beta\), uniformly in \(D\) and \(Y\ge Y_0\). The triangle and reverse triangle inequalities, followed by a sufficiently large choice of \(D_0\), prove (6.11), using \(J(Y)\asymp_KY\). \(\square\)

For actual \(f=A_r\), this corollary applies only if expansion (6.10), including its power-saving remainder, has first been proved. The existence of an off-line zero alone does not imply that finite expansion: infinitely many zero contributions or an uncontrolled contour remainder may remain. The corollary supplies an every-scale rigidity statement under its stated hypothesis; it does not replace an unconditional record-scale argument.

## 7. A separate one-sided theorem for a moving mask range

This section records the precise perturbation statement that permits a scale-dependent range. It is not obtained by substituting a varying \(Y\) into Theorem 5.1.

### Proposition 7.1. Moving-average integrability detector

Fix \(1\le p<\infty\), \(\sigma>0\), \(\rho>0\), and \(c_*>0\). Suppose that the measurable cutoff \(Y(x)\) satisfies

\[
Y(x)\ge c_*x^\rho
\tag{7.1}
\]

for all sufficiently large \(x\). Let \(f\) be locally bounded and zero below a positive scale, and define

\[
Pf(x)=M_{Y(x)}f(x)
\tag{7.2}
\]

where \(Y(x)\ge1\). If

\[
\int_{X_1}^\infty
\left[
\frac1{J(Y(x))}\sum_{Nv\le Y(x)}|T_vf(x)|^p
\right]x^{-p\sigma}\frac{dx}{x}<\infty
\tag{7.3}
\]

for some sufficiently large \(X_1\), then

\[
\int_0^\infty|f(x)|^px^{-p\sigma}\frac{dx}{x}<\infty.
\tag{7.4}
\]

More precisely, on the space of functions zero below \(X_0\), the operator \(P\) has a bounded inverse on the weighted space of \([X_0,T]\), with a bound uniform in \(T\ge X_0\), provided \(X_0\) is sufficiently large depending on \(K,\sigma,\rho,c_*\).

**Proof.** Choose \(0<\delta<\min(\sigma,1/2)\). For \(x\ge X_0\) and a function \(g\) zero below \(X_0\), Lemma 2.1 gives the pointwise majorant

\[
\begin{aligned}
|(P-M)g(x)|
&\le C_K Y(x)^{-\delta}
\sum_d (N\operatorname{rad}d)^{-1+\delta}|g(x/Nd)|\\
&\le C_Kc_*^{-\delta}X_0^{-\rho\delta}
\sum_d (N\operatorname{rad}d)^{-1+\delta}|g(x/Nd)|.
\end{aligned}
\tag{7.5}
\]

The positive dilation operator in the last line has weighted \(L^p\) norm at most

\[
A_{K,\sigma,\delta}
=\sum_d(Nd)^{-\sigma}
       (N\operatorname{rad}d)^{-1+\delta}<\infty,
\tag{7.6}
\]

as already proved in (4.15). The constant operator \(M\) and its causal inverse preserve the subspace of functions zero below \(X_0\). On this subspace, choose \(X_0\) so large that

\[
\|M^{-1}\|\, C_Kc_*^{-\delta}
X_0^{-\rho\delta}A_{K,\sigma,\delta}<\tfrac12.
\tag{7.7}
\]

The Neumann argument now takes place in bounded operators on the weighted space, rather than in the constant-coefficient algebra. It proves the asserted inverse for \(P=M+(P-M)\), on every interval \([X_0,T]\). Every operator involved is causal, and all bounds are independent of \(T\).

For the general \(f\), decompose \(f=f_{\rm low}+g\), where

\[
f_{\rm low}=f\,1_{(0,X_0)},\qquad
g=f\,1_{[X_0,\infty)}.
\]

The low part has finite global weighted norm. Uniformly for \(Y\ge1\), Lemma 2.1 also gives \(w_Y(d)\ll_K(N\operatorname{rad}d)^{-1}\). Hence, for \(x\ge X_0\),

\[
|Pf_{\rm low}(x)|
\le C_K\sum_d\frac{|f_{\rm low}(x/Nd)|}
                         {N\operatorname{rad}d}.
\tag{7.8}
\]

The majorant has finite weighted operator norm by (4.13). Thus \(Pf_{\rm low}\) has finite weighted norm on the high-scale interval. Jensen and (7.3) give the same conclusion for \(Pf\), and therefore for \(Pg\).

Although global integrability of \(g\) is initially unknown, its norm on every finite interval is finite. Apply the uniform inverse estimate to \(g\) on \([X_0,T]\), then let \(T\) tend to infinity. This gives \(g\) finite global weighted norm, proving (7.4). \(\square\)

For a fixed arithmetic core \(r\), all its lifts satisfying

\[
Nv\le Y(x):=(x^h/Nr)^{1/6}
\tag{7.9}
\]

are included among the rows \(Nu\le x^h\). Here \(h>0\) is fixed and \(\rho=h/6\). Therefore, for sufficiently large \(x\),

\[
\frac1{J(Y(x))}\sum_{Nv\le Y(x)}
|A_{rv^6}(x)|^p
\ll_K (Nr)^{1/6}x^{-h/6}\mathcal M_p(x,x^h).
\tag{7.10}
\]

Thus the following genuinely weaker scale input is sufficient for weighted integrability of each fixed core:

\[
\int_{X_1}^\infty
\mathcal M_p(x,x^h)x^{-p\sigma-h/6}\frac{dx}{x}<\infty
\quad\Longrightarrow\quad
\int_0^\infty|A_r(x)|^px^{-p\sigma}\frac{dx}{x}<\infty.
\tag{7.11}
\]

In particular, if \(p=2k\) and the original moment obeys the dyadic integral bound

\[
\int_X^{2X}\mathcal M_{2k}(x,x^h)\frac{dx}{x}
\ll_{\epsilon}X^{k+h+\epsilon}
\qquad(X\ge2),
\tag{7.12}
\]

then (7.11) holds for every

\[
\sigma>\frac12+\frac{5h}{12k}.
\tag{7.13}
\]

Indeed choose \(0<\epsilon<2k\sigma-k-5h/6\) and sum (7.12), after multiplying by \(X^{-2k\sigma-h/6}\), over dyadic \(X\).

For such a \(\sigma\), Hölder's inequality makes the Mellin integral
\(\int_0^\infty A_r(x)x^{-s}\,dx/x\) absolutely convergent for \(\Re s>\sigma\); local uniform convergence makes it holomorphic there. This supplies the analytic continuation needed by a separate Mellin zero-extraction theorem, provided the chosen test has nonzero Mellin transform at the zero under consideration. The present proposition proves the transfer and integrability assertion, not the dyadic moment premise (7.12).

## 8. Exact-removal synthetic models at every growth exponent

The next construction enforces all local removal identities at all physical scales. It therefore addresses a stronger obstruction than an arbitrary array of row values.

Fix \(z=\beta+it\) with \(\beta>0\), and choose a smooth cutoff \(\chi\) on \((0,\infty)\) with

\[
\chi(x)=0\quad(x\le1/2),\qquad
\chi(x)=1\quad(x\ge1).
\tag{8.1}
\]

Set

\[
f_z(x)=x^z\chi(x),\qquad
B_v(x)=T_vf_z(x).
\tag{8.2}
\]

One may use in (8.2) the exact \(\eta\) of any fixed actual Hecke core. The base function is prescribed separately and is not asserted to equal a Möbius sum.

### Proposition 8.1. All exact identities with a persistent prescribed exponent

For every \(v\), \(B_v\) is smooth, vanishes below \(1/2\), and satisfies all exact removal identities (1.5). For every fixed integer \(k\ge1\),

\[
\frac1{J(Y)D^{2k\beta}}
\sum_{Nv\le Y}|B_v(D)|^{2k}
\longrightarrow C_{k,z,\eta}>0
\tag{8.3}
\]

as \(D,Y\) tend to infinity independently, where

\[
C_{k,z,\eta}
=\prod_{\mathfrak p}
\left(1-\frac1q+
\frac1q|1-\eta(\mathfrak p)q^{-z}|^{-2k}\right).
\tag{8.4}
\]

More precisely, for any \(0<\epsilon_0<\beta\) and
\(0<\delta<\min(\beta,1/2)\), the expression in (8.3) equals

\[
C_{k,z,\eta}+O(D^{-\epsilon_0}+Y^{-\delta}).
\tag{8.5}
\]

The implied constant depends on the fixed data, not on \(D,Y\).

**Proof.** On a compact interval of scales only finitely many ideals can satisfy \(D/Nd>1/2\). Thus the defining sums for \(B_v\), and all their derivatives, are locally finite. Formula (1.5) is the exact finite local geometric identity applied to this base function.

For all \(x>0\),

\[
|f_z(x)-x^z|\ll_{\chi,\beta,\epsilon_0}x^{\beta-\epsilon_0}.
\]

Therefore

\[
B_v(D)=D^zF_v(z)
+O(D^{\beta-\epsilon_0}E_{\beta-\epsilon_0}(v)).
\tag{8.6}
\]

After division by \(D^\beta\), Theorem 3.1 bounds the normalized \(\ell^{2k}\) norm of the error by \(O(D^{-\epsilon_0})\), uniformly in \(Y\ge1\). The normalized \(\ell^{2k}\) norm of \(F_v(z)\) is uniformly bounded, again by Theorem 3.1. The triangle inequality and the elementary estimate for the difference of fixed positive integer powers consequently show that

\[
\frac1{J(Y)D^{2k\beta}}\sum_{Nv\le Y}|B_v(D)|^{2k}
=\frac1{J(Y)}\sum_{Nv\le Y}|F_v(z)|^{2k}
+O(D^{-\epsilon_0}).
\tag{8.7}
\]

Apply Lemma 6.1 to
\(G_{\mathfrak p}=|1-\eta(\mathfrak p)q^{-z}|^{-2k}\).
Its nonconstant term is \(O_{k,z}(q^{-\beta})\), giving the stated limit and the \(O(Y^{-\delta})\) error. Each factor in (8.4) is positive; the deviations from one are absolutely summable. Hence their product is finite and strictly positive. \(\square\)

Taking \(Y=D^{h/6}\), for any fixed \(h>0\), gives

\[
\sum_{Nv\le D^{h/6}}|B_v(D)|^{2k}
\sim \kappa_K C_{k,z,\eta}D^{2k\beta+h/6}.
\tag{8.8}
\]

Thus exact removal identities, every-scale consistency, finite local conductor masks, and averaged coercivity all coexist with every prescribed \(\beta>1/2\). They do not force an improved upper exponent for the base. In particular, the identities alone cannot rule out a contribution of the same power size as an off-critical Mellin mode.

This is not a counterexample to the proposed moment for the actual family. The model does not enforce the expansion

\[
f(x)=\sum_n\mu_K(n)\eta(n)W(Nn/x)
\]

with one fixed smooth test. It need not obey any analytic identity that would follow specifically from those Möbius coefficients, an actual Hecke \(L\)-function, or the long-core bilinear structure. Those are precisely the constraints an upper-bound proof must still use.

## 9. What this advances, and what remains open

The unconditional advance is the quantitative and invertible mean-removal operator, and therefore uniform finite-scale weighted \(L^p\) coercivity for arbitrary base functions. It also gives a constant-loss fixed-core upper transfer and a valid route from dyadic scale-averaged moments to Mellin integrability. These conclusions eliminate artificial individual-mask power losses and isolate the role of integration over scale.

Finite leading Mellin modes satisfy a further rigidity statement: averaging over exact masks separates their phases and produces their expected moment power at every sufficiently large scale. Its finite-expansion hypothesis is substantive and has not been established here for the actual Möbius family.

The arithmetic missing input remains an upper moment estimate. The exact synthetic construction demonstrates why further manipulation of the removal identities, by itself, cannot supply the needed saving. A successful continuation must bring in a new constraint on the actual Möbius coefficients or on the unresolved long balanced core sums.
