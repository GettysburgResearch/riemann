# Bounded real-zero variance: a signed finite-selector theorem

Status: proposed analytic component, with proof below; not independently reviewed.
Scope: exact complete finite trigonometric compressions of the Weil form. The all-scale variance-selection hypothesis remains OPEN. No new zero-free region is claimed.
Exact sources: the full source and finite real-zero theorem of PR #1017 at `450dd8abecf58dfe60b3bc39bda0f792ea82ce95`; the theta density and its complete-source annihilation identity in PR #1021 at `742e952be4ef7843de86ea12678c0bdd3d3579c3`; the even spectral consumer at `0f07049ff1e8cc7765f6de01b4e176ad627bba4b`.
Native contribution proposed here: Gaussian smoothing converts bounded real-zero variance into the overlap and residual control needed by a signed finite-resolvent argument. An explicit, compatible quadratic Fourier schedule and a Gaussian zero detector close its analytic steps.
Smallest remaining gap: construct exact legal full-matrix resolvents with the uniform variance bound in Theorem 1. Neither the example in Section 2 nor the residual estimates construct such resolvents.

## 1. Exact statement and legality

Use the Fourier convention

\[
\widehat f(z)=\int_{\mathbb R}f(x)e^{-izx}\,dx.
\]

Let \(K_W\) be the complete real, even Weil convolution distribution, with quadratic form

\[
\begin{aligned}
q_a[f]={}&\frac1{2\pi}\int_{\mathbb R}
 \bigl(\Re\psi(1/4+it/2)-\log\pi\bigr)|\widehat f(t)|^2\,dt\\
&+2\Re\bigl(\widehat f(i/2)\overline{\widehat f(-i/2)}\bigr)\\
&-\sum_{2\le n\le e^{2a}}\frac{\Lambda(n)}{\sqrt n}
 \bigl(C_f(\log n)+C_f(-\log n)\bigr),
\end{aligned}
\tag{1}
\]

where \(f\) is extended by zero from \([-a,a]\), and
\(C_f(t)=\int\overline{f(x)}f(x+t)\,dx\). Every prime power is retained. The domain is the logarithmic Fourier form domain, as in the pinned source.

Let \(\phi\) be the positive even theta probability density, with

\[
\widehat\phi(t)=X(t)=\Xi(t)/\Xi(0),\qquad
K_W*\phi=0,\qquad
V_X=\int x^2\phi(x)\,dx<\infty.
\tag{2}
\]

The source gives, for every fixed derivative order, a bound of the form
\(\exp(C|x|-c e^{2|x|})\). In particular \(\phi\) and its derivatives have all Gaussian moments. Only these unconditional facts about the actual theta source are used.

Fix a constant

\[
M\ge\max(1,V_X),\qquad
N_a=\left\lceil\frac{11a^2}{50M}\right\rceil,
\qquad a\in\mathbb N.
\tag{3}
\]

Let \(T_a\) be the exact compression of (1), with its \(L^2[-a,a]\) inner product, to the **full** trigonometric space

\[
\mathcal T_a=\operatorname{span}\{e^{in\pi x/a}:|n|\le N_a\},
\tag{4}
\]

and let \(E_a\) be its real even subspace. Put
\(\lambda_a=\min\operatorname{spec}(T_a)\), including both parity blocks.
For each sufficiently large integer \(a\), choose a real number
\(\kappa_a<\lambda_a\) and define

\[
u_a=(T_a-\kappa_a)^{-1}1,\qquad
f_a=\frac{u_a}{\int_{-a}^a u_a(x)\,dx},\qquad
F_a=\widehat f_a.
\tag{5}
\]

The denominator is strictly positive by coercivity. Reflection and conjugation make \(f_a\) real and even. The finite real-zero result imported in PR #1017 from Connes--van Suijlekom, Theorem 5.6, says that \(F_a\) has only real zeros. This use requires legality below the **full** finite minimum. A shift below the even-block minimum alone is not asserted to supply that conclusion.

**Theorem 1.** Suppose that the exact resolvents (5) satisfy

\[
V_a:=-F_a''(0)=\int_{-a}^a x^2 f_a(x)\,dx\le M
\tag{6}
\]

for every sufficiently large integer \(a\). No physical nonnegativity assumption on \(f_a\) is made. Then \(\kappa_a\to0\), and RH follows.

The quantity in (6) is a signed physical second moment. It is nonnegative here because the entire transform is normalized, even, and real-rooted; it is not being interpreted as the variance of a positive measure. The conclusion is conditional on an all-scale assertion about the **actual source resolvents**.

## 2. The chosen schedule passes a necessary compatibility test

Every normalized finite trigonometric transform in (4) has compulsory real zeros

\[
F(m\pi/a)=0\qquad(|m|>N_a).
\tag{7}
\]

For an even entire function of exponential type, real on the real axis, with \(F(0)=1\) and only real zeros, the paired Hadamard product is

\[
F(z)=\prod_j(1-z^2/t_j^2),\qquad
-F''(0)=2\sum_j t_j^{-2}.
\tag{8}
\]

Indeed the function has order at most one, its zeros occur in opposite pairs, and the possible exponential factor is constant by evenness. The paired product converges locally uniformly. It follows from (7) that

\[
V\ge \frac{2a^2}{\pi^2}\sum_{m>N_a}m^{-2}
\sim\frac{100M}{11\pi^2}<M.
\tag{9}
\]

A much smaller coefficient in \(N_a\asymp a^2/M\) would make (6) impossible. This is a necessary dimensional constraint, not a numerical subtlety.

There is an exact witness that the transform and variance requirements are compatible with (3): normalize

\[
h_{a,N}(x)=c_{a,N}\cos^{2N}(\pi x/(2a)),\qquad |x|\le a,
\tag{10}
\]

to have integral one. This belongs to \(E_a\) when \(N=N_a\), and

\[
\widehat h_{a,N}(z)
=\frac{\Gamma(N+1)^2}
 {\Gamma(N+1+az/\pi)\Gamma(N+1-az/\pi)}
=\prod_{m>N}\left(1-\frac{a^2z^2}{\pi^2m^2}\right).
\tag{11}
\]

The Fourier integral follows from the beta integral, or from integrating the finite cosine expansion; the second equality follows from the sine product and the gamma recurrence. Consequently its only zeros are precisely the compulsory zeros, and

\[
V(h_{a,N_a})
=\frac{2a^2}{\pi^2}\sum_{m>N_a}m^{-2}
\le\frac{2a^2}{\pi^2N_a}
\le\frac{100M}{11\pi^2}<M.
\tag{12}
\]

This checks **function-space compatibility**. It does not show that (10) is the resolvent of the Weil matrix, or that any legal source resolvent satisfies (6).

## 3. Two consequences of bounded real-zero variance

Apply (8) to \(F_a\). For every complex \(z\),

\[
|F_a(z)|\le\prod_j(1+|z|^2/t_j^2)
\le e^{M|z|^2/2},
\tag{13}
\]

and, by expanding finite products and passing to the limit,

\[
|F_a(t)-1|\le e^{Mt^2/2}-1\qquad(t\in\mathbb R).
\tag{14}
\]

The exact Fourier coefficients of \(f_a\) on \([-a,a]\) are
\(F_a(n\pi/a)/(2a)\). Therefore

\[
\begin{aligned}
\|f_a\|_1
&\le\sum_{|n|\le N_a}|F_a(n\pi/a)|\\
&\le(2N_a+1)
 \exp\left(\frac{M\pi^2N_a^2}{2a^2}\right)\\
&\le C_M(1+a)^2
 \exp\left(\frac{121\pi^2}{5000M}a^2\right).
\end{aligned}
\tag{15}
\]

The last step absorbs the ceiling in (3) into a constant depending on fixed \(M\). This bound is large, but Gaussian source approximants below have a strictly faster decay rate.

Define the heat Gaussian and the smoothed theta source by

\[
G_M(x)=(4\pi M)^{-1/2}e^{-x^2/(4M)},\qquad
v=\phi*G_M.
\tag{16}
\]

Then \(v\) is positive, even, of mass one, and
\(\widehat v(t)=X(t)e^{-Mt^2}\). The complete-source identity (2), or the Gaussian-tested explicit formula, gives \(K_W*v=0\).

Since \(\phi\) is a probability density,

\[
|X(t)|\le1,\qquad X(t)\ge1-\tfrac12V_Xt^2.
\tag{17}
\]

Equations (14) and (17) imply

\[
F_a(t)X(t)
\ge X(t)-|F_a(t)-1|\,|X(t)|
\ge2-\tfrac12V_Xt^2-e^{Mt^2/2}.
\tag{18}
\]

All functions in the following Parseval integral are integrable by (13):

\[
\begin{aligned}
\langle f_a,v\rangle
&=\frac1{2\pi}\int_{\mathbb R}F_a(t)X(t)e^{-Mt^2}\,dt\\
&\ge\frac{2-\sqrt2-V_X/(4M)}{2\sqrt{\pi M}}
=:m_M>0.
\end{aligned}
\tag{19}
\]

The inequality is strict because \(M\ge V_X\) and \(2-\sqrt2-1/4>0\). Thus a positive source overlap is obtained without assigning a sign to \(f_a\).

## 4. An elementary complete-source residual estimate

For a real or complex \(C^1\) function \(r\) with

\[
|r(x)|+|r'(x)|\le B e^{-2|x|},
\tag{20}
\]

the full physical source is

\[
\begin{aligned}
(K_W*r)(x)={}&2\int_{\mathbb R}\cosh((x-y)/2)r(y)\,dy-c_0r(x)\\
&-\int_0^\infty\frac{e^{-t/2}}{1-e^{-2t}}
 \{r(x+t)+r(x-t)-2e^{-t/2}r(x)\}\,dt\\
&-\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
 \{r(x+\log n)+r(x-\log n)\},
\end{aligned}
\tag{21}
\]

where \(c_0=\log(4\pi)+\gamma\). This is the unchanged source convention, including both pole terms and every prime power.

**Residual lemma.** There is an absolute constant \(C\) such that

\[
|(K_W*r)(x)|\le C B e^{2|x|}.
\tag{22}
\]

**Proof.** The pole integral is at most \(CB e^{|x|/2}\). For \(0<t\le1\), the bracket in the archimedean integral is \(O(Bt)\), by (20) and the mean-value theorem; its kernel is \(O(1/t)\). For \(t\ge1\), the bracket is \(O(B)\) and the kernel is integrable. Thus the archimedean part is \(O(B)\). Finally,

\[
e^{-2|x\pm\log n|}\le e^{2|x|}n^{-2},
\]

and the prime sum is bounded by
\(2B e^{2|x|}\sum_{n\ge2}(\log n)n^{-5/2}\). This proves (22), using only \(\Lambda(n)\le\log n\). The integrals and sums used here converge absolutely after the displayed archimedean cancellation. QED.

The functions constructed below are \(C^1\) after extension by zero. Their compact restrictions belong to the operator domain of \(A_a\): their Fourier transforms decay as \(O((1+|t|)^{-1})\), which suffices for the logarithmic multiplier to belong to \(L^2\); the other fixed-interval terms are bounded operators. Thus the identity \(q_a(f,p)=\langle f,A_ap\rangle\) used below is a genuine operator/form identity.

## 5. Finite approximants to the smoothed theta source

Put

\[
d=\frac{49}{200M}.
\tag{23}
\]

For fixed \(M\), the Gaussian convolution in (16) satisfies

\[
|v(x)|+|v'(x)|\le C_M e^{-dx^2}.
\tag{24}
\]

To see this without an asymptotic assertion, choose \(d<d'<1/(4M)\). Completing the square gives
\(G_M(x-y)\le C e^{-d'x^2+C_My^2}\). The derivative of the Gaussian contributes a linear factor, absorbed by the gap \(d'-d\). Integrating against \(\phi\), whose Gaussian moments are finite by (2), proves (24).

Periodize \(v\) with period \(2a\), and truncate to modes \(|n|\le N_a\):

\[
S_av(x)=\frac1{2a}\sum_{|n|\le N_a}
 X(n\pi/a)e^{-M(n\pi/a)^2}e^{in\pi x/a}.
\tag{25}
\]

The periodization copies other than the central one, and their first derivatives, are bounded on \([-a,a]\) by \(C_Me^{-da^2}\). Since \(|X(t)|\le1\), the omitted Fourier series, including its first derivative, is bounded by

\[
C_M(1+a)^C\exp\left(-\frac{M\pi^2N_a^2}{a^2}\right).
\tag{26}
\]

This follows by comparing each Gaussian tail sum with its integral; differentiation adds the factor \(|n|\pi/a\). The use of \(N_a\), rather than \(N_a+1\), weakens the bound harmlessly. The exponent in (26) is at least
\(121\pi^2 a^2/(2500M)\), which is greater than \(da^2\).

Set

\[
p_a(x)=S_av(x)-(S_av)(a),\qquad
v_a=p_a/\int_{-a}^a p_a(x)\,dx
\quad (|x|\le a),
\tag{27}
\]

and extend by zero. For large \(a\), the normalizing integral is
\(1+O_M((1+a)^C e^{-da^2})\), hence nonzero. The polynomial and its derivative vanish at both endpoints: the value was subtracted, and every even trigonometric polynomial has derivative zero there. Thus the extension is \(C^1\).

Equations (24)--(27), both inside and outside the interval, give

\[
|v_a(x)-v(x)|+|(v_a-v)'(x)|
\le B_a e^{-2|x|},\qquad
B_a\le C_M(1+a)^C e^{-da^2+2a}.
\tag{28}
\]

Outside \([-a,a]\), use that \(-dx^2+2|x|\) decreases once \(|x|\) is sufficiently large. Inside, multiply the uniform approximation bound by \(e^{2a}\). The mass normalization introduces an error of the same order because \(v\) and \(v'\) are bounded.

Since \(K_W*v=0\), (22) implies

\[
\|A_av_a\|_\infty
\le C_M(1+a)^C e^{-da^2+4a}.
\tag{29}
\]

The strict exponent margin that matters is

\[
d-\frac{121\pi^2}{5000M}
=\frac{1225-121\pi^2}{5000M}
>\frac{15}{5000M}>0,
\tag{30}
\]

where the deliberately loose inequality \(\pi^2<10\) is enough. Hence (15), (28), and (29) yield

\[
\|f_a\|_1\|A_av_a\|_\infty\longrightarrow0,
\qquad
|\langle f_a,v_a-v\rangle|\longrightarrow0.
\tag{31}
\]

Together with (19), this proves

\[
\langle f_a,v_a\rangle\ge m_M/2
\quad\text{for all sufficiently large }a.
\tag{32}
\]

## 6. A broad finite comparator

Choose a fixed, real, nonnegative, even smooth function \(\eta\), supported in \((-1,1)\), of mass one. Put

\[
\eta_{a/2}(x)=\frac2a\eta(2x/a),\qquad
w^{(a)}=v*\eta_{a/2}.
\tag{33}
\]

It is again a complete-source null function. Young's inequality gives

\[
\|w^{(a)}\|_2^2\le\|\eta_{a/2}\|_2^2=C/a,
\qquad \|w^{(a)}\|_1=1.
\tag{34}
\]

Its Fourier transform is
\(X(t)e^{-Mt^2}\widehat\eta((a/2)t)\), and
\(|\widehat\eta((a/2)t)|\le1\) on the real axis. Thus it has the same Fourier truncation bound (26). Its physical tails and first derivatives at \(|x|\ge a\) have the bound

\[
C_M\exp\bigl(-d(|x|-a/2)^2\bigr),
\tag{35}
\]

by (24) and the support of \(\eta_{a/2}\).

Periodize, truncate at the same \(N_a\), subtract the endpoint value, and normalize mass exactly as in (27). Call the resulting element of \(E_a\) \(w_a\). The preceding proof, with the boundary distance \(a/2\), gives

\[
\begin{gathered}
\|w_a\|_1\le C_M,\qquad
\|w_a\|_2^2\le C_M/a,\\
\|A_aw_a\|_\infty\le
 C_M(1+a)^C\exp(-da^2/4+4a)=:\varepsilon_a,\\
|q_a[w_a]|\le C_M\varepsilon_a,
\qquad a\varepsilon_a\longrightarrow0.
\end{gathered}
\tag{36}
\]

For the \(L^2\) estimate, the finite approximation error is at most
\(C_M(1+a)^C e^{-da^2/4}\) pointwise on the interval, so its squared integral and the cross term are negligible compared with \(1/a\). The mass normalization tends to one. No sign assertion about \(w_a\) is required.

The Gaussian convolution in (33) is necessary for this proof at the chosen cutoff: the unsmoothed theta Fourier tail alone has only exponential decay in \(N_a/a\), which need not beat the complete prime operator growth.

## 7. The legal shifts tend to zero

Write

\[
c_a=\left(\int u_a\right)^{-1}>0.
\]

The exact finite variational equation is

\[
(T_a-\kappa_a)f_a=c_a1.
\tag{37}
\]

The normalized vector uniquely minimizes
\(q_a[f]-\kappa_a\|f\|_2^2\) among vectors of mass one in \(\mathcal T_a\), and its minimum is \(c_a\). This follows by expanding around \(f_a\); the cross term is zero for mass-zero perturbations, and \(T_a-\kappa_a\) is positive definite.

Pair (37) with \(v_a\), using (31), its mass one, and the actual operator-domain identity from Section 4:

\[
c_a=-\kappa_a\langle f_a,v_a\rangle+r_a,
\qquad |r_a|\le\|f_a\|_1\|A_av_a\|_\infty\longrightarrow0.
\tag{38}
\]

For \(\kappa_a<0\), comparison with the mass-one vector \(w_a\) gives

\[
c_a\le C_M\varepsilon_a+C_M|\kappa_a|/a.
\tag{39}
\]

Combining (32), (38), and (39),

\[
|\kappa_a|\left(m_M/2-C_M/a\right)
\le |r_a|+C_M\varepsilon_a\longrightarrow0.
\tag{40}
\]

Thus the negative shifts tend to zero. If \(\kappa_a\ge0\), full legality and the Rayleigh quotient of \(w_a\) yield

\[
0\le\kappa_a<\lambda_a
\le\frac{q_a[w_a]}{\|w_a\|_2^2}
\le 2a C_M\varepsilon_a\longrightarrow0,
\tag{41}
\]

where \(\|w_a\|_2^2\ge1/(2a)\) follows from mass one and its support. Consequently \(\kappa_a\to0\) in all cases. The exact even-block minimum is therefore bounded below by a sequence tending to zero.

## 8. A Gaussian zero detector for the quadratic Fourier schedule

The older compact Gevrey projection argument at a cubic mode cutoff does not apply unchanged to \(N_a\asymp a^2\). The following direct argument supplies the required consumer.

**Theorem 2.** Fix \(\eta\ge0\) and \(c>0\), put \(N_a=\lceil ca^2\rceil\), and let \(\lambda_a^{\mathrm{even}}\) be the minimum of the exact even compression of (1). If, for every \(\epsilon>0\),

\[
\lambda_a^{\mathrm{even}}
\ge-C_\epsilon e^{(2\eta+\epsilon)a}
\quad\text{for every sufficiently large integer }a,
\tag{42}
\]

then zeta has no zero with \(\Re\rho>1/2+\eta\). In particular an eventual uniform finite lower bound suffices for RH.

**Proof.** Fix \(s>0\), let \(g=G_s\), and write
\(G(z)=\widehat g(z)=e^{-sz^2}\). For \(t\ge0\), define the even real test

\[
h_t(x)=g(x-t/2)+g(x+t/2).
\tag{43}
\]

Its \(L^1\) norm is two and its \(L^2\) norm is uniformly bounded in \(t\). The Gaussian-tested explicit formula converges absolutely, and, with
\(z_\rho=(\rho-1/2)/i\), gives

\[
q[h_t]=2q[g]+2C_g(t),\qquad
C_g(t)=\sum_\rho e^{-2s z_\rho^2}e^{iz_\rho t}.
\tag{44}
\]

The series is real by the zero symmetries. Its coefficient absolute values are at most \(e^{s/2}e^{-2s\gamma^2}\), since \(|\Im z_\rho|<1/2\), so the unconditional count \(N(T)=O(T\log(2+T))\) justifies absolute convergence, including differentiation and Laplace transformation where used below. The source side also converges absolutely, because its Gaussian autocorrelations beat the exponential growth of the prime measure and the pole terms. The standard compact explicit formula extends to these tests by smooth cutoffs and these same bounds.

Choose any fixed \(0<\delta<1\), and for this \(t\) set

\[
a=\left\lceil\frac{t}{2(1-\delta)}\right\rceil.
\tag{45}
\]

Both Gaussian centers have distance at least \(\delta a\) from the boundary, up to an immaterial bounded change from the ceiling. Periodize \(h_t\) with period \(2a\), truncate at \(N_a\), and subtract the value at \(a\). Denote the zero-extended even polynomial by \(p_{a,t}\). Its derivative is zero at both endpoints, so the extension is \(C^1\).

The physical and Fourier Gaussian tails, including one derivative, are bounded respectively by

\[
C(1+a)^C e^{-\delta^2a^2/(4s)+O(a)},\qquad
C(1+a)^C e^{-s\pi^2c^2a^2+O(1)}.
\tag{46}
\]

Translation multiplies Fourier samples by phases of modulus one. The physical estimate follows from the boundary clearance; copies in the periodization are farther away. Consequently, for some fixed \(d_{s,c,\delta}>0\),

\[
|p_{a,t}(x)-h_t(x)|+|(p_{a,t}-h_t)'(x)|
\le B_{a,t}e^{-2|x|},\qquad
B_{a,t}\le C(1+a)^C e^{-d_{s,c,\delta}a^2+O(a)}.
\tag{47}
\]

For example, any constant strictly smaller than the minimum of the two quadratic exponents in (46) works for all large \(a\). The weighted estimate outside the interval follows by maximizing
\(-(|x|-t/2)^2/(4s)+2|x|\) there; the maximum lies at its boundary for sufficiently large \(a\).

Apply (22) to \(r=p_{a,t}-h_t\). The polarized source pairings are well-defined and symmetric; Fubini is justified by their Gaussian or exponential tails and the cancellation in (21). Thus

\[
\begin{aligned}
|q[p_{a,t}]-q[h_t]|
&=|q(p_{a,t},r)+q(r,h_t)|\\
&\le C B_{a,t}\int (|p_{a,t}(x)|+|h_t(x)|)e^{2|x|}\,dx\\
&\le C(1+a)^C e^{-d_{s,c,\delta}a^2+O(a)}=o(1).
\end{aligned}
\tag{48}
\]

Here \(\|p_{a,t}\|_1\) is bounded, its support is \([-a,a]\), and
\(\int |h_t(x)|e^{2|x|}dx\le C_s e^t\). Equation (47) also preserves the uniformly bounded \(L^2\) norm. This verifies the finite approximation against the complete operator, without an unproved continuum lower bound.

Apply (42) to \(p_{a,t}\), use (44)--(48), and absorb bounded \(t\):

\[
C_g(t)\ge-C_{\epsilon,s,c,\delta}
 \exp\left(\frac{\eta+\epsilon/2}{1-\delta}\,t\right)
\quad(t\ge0).
\tag{49}
\]

Set \(\alpha=(\eta+\epsilon/2)/(1-\delta)\), and choose \(C\) so that
\(D(t)=C_g(t)+Ce^{\alpha t}\ge0\) on \([0,\infty)\). For \(\Re w>\max(1/2,\alpha)\),

\[
\int_0^\infty D(t)e^{-wt}\,dt
=\sum_\rho\frac{e^{-2s z_\rho^2}}{w-iz_\rho}
 +\frac{C}{w-\alpha}.
\tag{50}
\]

The right side is meromorphic on the whole plane, with normal convergence away from its discrete poles. It has no real pole above \(\alpha\): zeta has no real nontrivial zero. One direct check for \(0<u<1\) is that the alternating eta series is positive by adjacent-term pairing, while \(1-2^{1-u}<0\), so \(\zeta(u)<0\).

For completeness, the Landau fact used here is: the finite convergence abscissa of the Laplace transform of a nonnegative function is a singularity at that real abscissa. If it were regular there, expand the transform around a real point \(w_1\) just to the right in a disk reaching a real \(w_2\) to the left. Its Taylor series at \(w_2\) has nonnegative terms
\(\int t^nD(t)e^{-w_1t}dt\,(w_1-w_2)^n/n!\). Tonelli identifies their finite sum with convergence at \(w_2\), a contradiction. The positive gap to the abscissa justifies differentiation.

It follows that the convergence abscissa in (50) is at most \(\alpha\) (or is \(-\infty\)). The right side is therefore holomorphic in \(\Re w>\alpha\). Any zero \(\rho\) with \(\beta-1/2>\alpha\) would give a pole there with residue
\(m_\rho e^{-2s z_\rho^2}\ne0\), a contradiction. The Gaussian coefficient never vanishes, so no auxiliary choice of a test avoiding a proposed zero is needed. Finally choose \(\epsilon\) and then \(\delta\) arbitrarily small to exclude every zero with \(\beta-1/2>\eta\). This proves Theorem 2. QED.

With \(c=11/(50M)\), (40)--(41) provide the eventual uniform lower bound needed in (42) with \(\eta=0\). Theorem 2 completes the proof of Theorem 1.

## 9. What remains arithmetic

The theorem removes the physical-sign condition from the earlier bounded-variance route at the explicitly chosen compatible schedule. It does not establish bounded variance for any cofinal family of actual legal resolvents. Full finite legality must also be verified for the shifts; an even-only comparison cannot be silently substituted in the imported real-zero step.

The witness (10) proves that the structural premises fit in these finite spaces. It does not solve the source equation (37). Neither finite numerical variance matching nor an observed monotone branch proves the required all-scale existence assertion. No monotonicity of the selector variance in the shift is used or established here.

The mathematical alternatives remain an actual lower bound on the complete even matrices, or a source-dependent argument constructing the legal bounded-variance family. The Gaussian mechanism isolates that latter question without an additional physical positivity or Xi-identification hypothesis.

## Primary mathematical references

- A. Connes, C. Consani, H. Moscovici, *Zeta Spectral Triples*, arXiv:2511.22755v1, <https://arxiv.org/html/2511.22755v1>. Imported full source, domain, and theta framework; no completed RH proof is attributed to this work.
- A. Connes, W. D. van Suijlekom, *Quadratic Forms, Real Zeros and Echoes of the Spectral Action*, arXiv:2511.23257v1, <https://arxiv.org/html/2511.23257v1>, especially Theorem 5.6. Imported finite real-zero theorem, with its complete source-class and full-legality hypotheses as authenticated by pinned PR #1017.
- M. Suzuki, *Weil's quadratic form via the screw function*, arXiv:2606.09096v1, <https://arxiv.org/html/2606.09096v1>. Its introduction records Yoshida's earlier even-test positivity implication; no novelty claim is made here for the classical even-sector Weil criterion. The explicit Gaussian approximation and quantitative finite schedule are the component proved above.
