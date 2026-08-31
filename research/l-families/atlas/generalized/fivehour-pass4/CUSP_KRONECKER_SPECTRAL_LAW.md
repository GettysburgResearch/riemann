# A native cusp operator and its growing-index spectrum

Status: PROPOSED ANALYTIC THEOREM; independent frozen-source review required.
Scope: level one, even weight tending to infinity; growing indices below
linear weight. This is not an RH theorem or a scalar-quotient zero census.
Authoring base: #766 `17c7624a0bd56c5356d00278b2a846d2efdbdccc`.
No numerical calculation is used as proof of an infinite assertion.

## 1. Native operator and normalization

Use the standard fundamental domain \(\mathcal F\), with
\(a_0=\sqrt3/2\le y\), and the conjugate-linear-first Petersson form

\[
 G_k(f,g)=\int_{\mathcal F}y^{k-2}\overline{f(z)}g(z)\,dx\,dy,
 \qquad V_k=S_k(SL_2(\mathbb Z)).
\]

The sign-identified Eisenstein completion is the same as the accepted parent:

\[
 E^*(z,s)=\Lambda(2s)y^s+\Lambda(2s-1)y^{1-s}+R_s(z),
 \qquad \Lambda(v)=\pi^{-v/2}\Gamma(v/2)\zeta(v).
\]

Its residue at one is \(1/2\). Define the real invariant symbol and its
finite-dimensional Petersson compression by

\[
 E_0(z)=\lim_{s\to1}\left(E^*(z,s)-\frac1{2(s-1)}\right),
 \qquad G_k(f,\mathcal T_kg)=\int_{\mathcal F}E_0y^{k-2}\bar f g.
 \tag{K1}
\]

Cusp decay makes every entry finite. This defines a genuine self-adjoint
operator on \(V_k\); multiplication by \(E_0\) is not asserted to preserve
holomorphic forms. Write its eigenvalues in decreasing order as
\(\lambda_1(k)\ge\cdots\ge\lambda_{d_k}(k)\).

Expanding the preceding Fourier formula at one gives exactly

\[
 E_0(z)=\frac{\pi y}{6}-\frac12\log y+c_0+r_0(z),
 \quad c_0=\frac{\gamma-\log(4\pi)}2,
 \quad r_0(z)=2\sum_{n\ge1}\sigma_{-1}(n)e^{-2\pi ny}\cos(2\pi nx).
 \tag{K2}
\]

Indeed \(\Lambda(2s-1)=1/[2(s-1)]+c_0+O(s-1)\),
\(\Lambda(2)=\pi/6\), and the coefficient \(4\sqrt y\) in the nonconstant
Fourier expansion combines with \(K_{1/2}(2\pi ny)=e^{-2\pi ny}/(2\sqrt{ny})\).
Thus, with

\[
 q_0=e^{-2\pi a_0},\qquad R_0=\frac{2q_0}{(1-q_0)^2},
 \qquad U_0=c_0+R_0-\tfrac12\log a_0,
\]

we have \(|r_0|\le R_0\) throughout \(\mathcal F\), because
\(\sigma_{-1}(n)\le n\). In particular
\(E_0(z)\le\pi y/6+U_0\).

The Eisenstein Fourier normalization is also printed in Section 3 of
[Barquero-Sanchez et al., Faltings heights of CM elliptic curves and special
Gamma values (2017)](https://link.springer.com/article/10.1007/s40993-017-0077-7).
The finite-part constant in (K2) is derived here in the present completion.

## 2. The theorem, including explicit finite bounds

Put \(\nu=k-1\), and for a positive integer \(J\) define

\[
 \delta_{k,J}=4\pi J\frac{(2\pi J)^{k-1}}{(k-1)!}
                 \exp(4\pi^2J^2/k),
\]
\[
 Q(b,x)=\frac{\Gamma(b,x)}{\Gamma(b)},\qquad
 L_{k,J}=\frac{k-1}{4\pi J}Q(k,4\pi J)(1-\delta_{k,J}),
 \qquad g(v)=\frac{\pi v}{6}-\frac12\log v+c_0-R_0.
 \tag{K3}
\]

**Theorem K.** For every even \(k\ge4\) and \(1\le J\le d_k\),

\[
 \lambda_J(k)\le\frac{k-1}{24J}+\frac\pi6+U_0. \tag{K4}
\]

If also \(\delta_{k,J}<1\) and \(L_{k,J}\ge3/\pi\), then

\[
 \lambda_J(k)\ge g(L_{k,J}). \tag{K5}
\]

Consequently, for EVERY sequence of even weights \(k\to\infty\) and integers
\(1\le J_k=o(k)\),

\[
 \boxed{\lambda_{J_k}(k)\sim\frac{k}{24J_k}.} \tag{K6}
\]

For every real sequence \(t_k\to\infty\) with \(t_k=o(k)\),

\[
 \boxed{\#\{j:\lambda_j(k)>t_k\}\sim\frac{k}{24t_k}.} \tag{K7}
\]

Strict versus non-strict counting at a threshold does not change (K7).
All sequences refer to the actual operators (K1), not fitted matrices.

## 3. Upper bound from the complete coefficient flag

Let \(W_J=\{f:a_f(1)=\cdots=a_f(J-1)=0\}\). Its codimension is at most
\(J-1\); no coefficient-independence assertion is needed for this upper bound.
For \(f\in W_J\), Parseval on the whole width-one cusp \(y\ge1\) gives sums
over ALL \(n\ge J\). If \(a=4\pi n\), integration by parts gives

\[
 \frac{\int_1^\infty y^{k-1}e^{-ay}dy}
      {\int_1^\infty y^{k-2}e^{-ay}dy}
 =\frac{k-1}{a}+
   \frac{e^{-a}}{a\int_1^\infty y^{k-2}e^{-ay}dy}
 \le\frac{k-1}{a}+1. \tag{K8}
\]

The last denominator is at least \(e^{-a}/a\), since \(k\ge2\).
Below height one, multiplication by \(y\) is at most the identity.
Consequently, in the FULL normalized Petersson measure,

\[
 \mathbb E_f[y]\le1+\frac{k-1}{4\pi J}. \tag{K9}
\]

Applying the upper bound after (K2), followed by the finite-dimensional
min--max principle on \(W_J\), proves (K4). The portion below height one
and the infinite Fourier tail have not been discarded.

## 4. Lower bound from the full Poincare block

Write \(A_n=\Gamma(k-1)/(4\pi n)^{k-1}\). Let \(P_n\) be the ordinary
holomorphic Poincare series with \(G_k(P_n,f)=A_na_f(n)\), and put
\(v_n=P_n/\sqrt{A_n}\), \(1\le n\le J\). The parent
[uniform-depth packet](../PROPER_THETA_SOURCE_UNIFORM_DEPTH_ZEROS.md), U1--U3,
translates the full Petersson formula to the present convention:

\[
 K_{mn}=G_k(v_m,v_n)
 =\delta_{mn}+2\pi i^k\sum_{c\ge1}\frac{S(m,n;c)}c
     J_{k-1}(4\pi\sqrt{mn}/c),\qquad \|K-I\|\le\delta_{k,J}.
 \tag{K10}
\]

This follows from \(|S(m,n;c)|\le c\), \(\sum c^{-(k-1)}\le2\), and
the defining Bessel-series bound. It is an infinite-tail estimate and a
full block operator bound, not a sampled Gram calculation.

For \(f=\sum_{n=1}^Jv_nc_n\), coefficient reproduction says
\(\sqrt{A_n}a_f(n)=(Kc)_n\), while \(G_k(f,f)=c^*Kc\). Keeping just the
first \(J\) nonnegative Parseval terms in the \(y\)-moment gives

\[
 \int_{y\ge1}y^{k-1}|f|^2dxdy
 \ge\frac{k-1}{4\pi J}Q(k,4\pi J)\|Kc\|^2.
 \tag{K11}
\]

When \(\delta_{k,J}<1\), \(K\) is positive definite and
\(\|Kc\|^2/(c^*Kc)\ge1-\delta_{k,J}\). The span therefore has dimension
\(J\), and every nonzero vector in it has \(\mathbb E_f[y]\ge L_{k,J}\).

Jensen's inequality for the logarithm, in the same probability measure,
now yields

\[
 \frac{G_k(f,\mathcal T_kf)}{G_k(f,f)}
 \ge \frac\pi6\mathbb E_f[y]-\frac12\log\mathbb E_f[y]+c_0-R_0
 =g(\mathbb E_f[y]). \tag{K12}
\]

The function \(g\) is increasing for \(v\ge3/\pi\). Thus (K12) is at
least \(g(L_{k,J})\) under the stated hypothesis. Min--max on this
\(J\)-dimensional native subspace proves (K5).

## 5. Uniform growing-index asymptotics

Suppose \(J/k\to0\). The elementary factorial lower bound
\((k-1)!\ge((k-1)/e)^{k-1}\) gives

\[
 \log\delta_{k,J}
 \le\log(4\pi J)+(k-1)\log\frac{2\pi eJ}{k-1}
                         +\frac{4\pi^2J^2}{k}\longrightarrow-\infty.
 \tag{K13}
\]

Indeed the second term divided by \(k\) tends to minus infinity, whereas
the last term divided by \(k\) tends to zero and \(\log J/k\to0\).
Also a Gamma variable of shape \(k\) satisfies

\[
 1-Q(k,4\pi J)\le e^{4\pi J}2^{-k}\longrightarrow0, \tag{K14}
\]

by applying Markov to its negative exponential. Hence
\(L_{k,J}\sim k/(4\pi J)\to\infty\). The logarithmic term in (K5) is
negligible relative to \(k/J\); (K4)--(K5) prove (K6).
The usual dimension formula \(d_k=k/12+O(1)\) ensures \(J\le d_k\)
eventually; equivalently, positivity of (K10) already supplies independence.

For (K7), fix \(0<\eta<1\) and take indices immediately below and above
\((1\mp\eta)k/(24t_k)\). They tend to infinity and are \(o(k)\).
Equation (K6) puts the first corresponding eigenvalue strictly above
\(t_k\), and the second strictly below it, for large weights. Sandwiching
the counting function and then letting \(\eta\downarrow0\) proves (K7).

## 6. Relation to the period pencil and exact nonclaims

For each FIXED weight, the Petersson-normalized period matrix satisfies

\[
 \mathcal M_k(1-\varepsilon)
 =-\frac1{2\varepsilon}I+\mathcal T_k+O_k(\varepsilon).
 \tag{K15}
\]

The coefficient \(k/(24J)\) explains why balancing these two displayed
terms suggests \(\varepsilon\sim12J/k\). But (K15) alone is not a uniform
growing-weight approximation. This packet does NOT use it to infer growing
period zeros, simple crossings, monotone spectral flow, or noncancellation
in a chosen scalar flag quotient. Direct estimates for the exact
\(s\)-dependent symbol are a separate target.

The theorem concerns a source-defined automorphic compression. It neither
constructs a new automorphic representation nor supplies a positivity
mechanism for the Riemann Xi function. Classical Fourier/Petersson formulas,
Jensen, and min--max are imported tools; external novelty is not asserted.
