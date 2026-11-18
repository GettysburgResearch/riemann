# Derivative-domain obstruction for unitary Mellin phases

**Lemma.** Let $U$ be a unitary Mellin multiplier on $L^2((0,\infty),dx)$, with symbol of modulus one almost everywhere on $\Re s=1/2$. Let $D=x\partial_x$ have its maximal weak domain $\{f\in L^2:Df\in L^2\}$, with distributions taken on the open half-line. Then $U$ maps $\operatorname{Dom}D$ onto itself and $DU=UD$ there. In particular, for $\chi_0=\mathbf1_{(0,1]}$, $D(U\chi_0)\notin L^2$.

To prove it, let $Jf(u)=e^{u/2}f(e^u)$, a unitary map onto $L^2(\mathbb R,du)$. Distributionally,
$$
J(Df)=\partial_u(Jf)-\tfrac12Jf.
$$
Indeed, for a compactly supported smooth test $\eta(u)$, apply $Df$ to $x^{-1/2}\eta(\log x)$ and use $Df(\psi)=-\int f(x)(x\psi(x))'\,dx$. This gives $-\int Jf(u)(\eta'(u)+\eta(u)/2)\,du$. Thus the identity uses no boundary integration at 0 or infinity. With the unitary Fourier convention having exponential $e^{itu}$, the maximal derivative domain corresponds to
$$
\int_{\mathbb R}\left(\tfrac14+t^2\right)|\widehat {Jf}(t)|^2\,dt<\infty.
$$
This follows from the weak Fourier derivative identity. The spectral multiplier of $D$ is $-1/2-it$. The operator $U$ multiplies $\widehat {Jf}(t)$ by a measurable unimodular factor, which preserves the weighted integral and commutes with the spectral multiplier. The same holds for $U^{-1}$.

Finally $J\chi_0(u)=e^{u/2}\mathbf1_{\{u\le0\}}$ has weak derivative $(J\chi_0)/2-\delta_0$, so $J(D\chi_0)=-\delta_0$. This excludes $\chi_0$ from the weak domain and, by domain preservation, excludes $U\chi_0$ as claimed. Equivalently, the $L^2$ Mellin transform of $\chi_0$ is $1/s$, and the weighted domain criterion cancels $|s|^{-2}$ to give a divergent integral. This is an application of the domain criterion, independent of any formal boundary integration.

## Scope of the source consequence

De Roton's Proposition 4.1 is a conditional statement for a bounded dilation-invariant operator. If $\varphi=U\chi_0$ is $C^1$ on $(0,\infty)$, then the classical $x\varphi'$ agrees with its weak derivative in the lemma. Consequently the additional premise $x\varphi'\in L^2$ cannot hold for a **unitary** Mellin phase. This invalidates the source's invocation of that premise after Proposition 5.1 for $U_F$. It does not address validity of Proposition 4.1 under its own hypotheses, and gives no general assertion about a differentiated-kernel expression obtained by a different limiting argument. [De Roton 2006, printed p. 429 and pp. 432–433](../sources/prefix_formula62_generalL/deroton_lower.pdf)

The phase-vector construction has a separate route using only $\varphi$. For $\Re w<1/2$, the following identity holds as a Bochner $L^2$ integral:
$$
\chi_0(x)x^{-w}
=\chi_0(x)+w\int_0^1 v^{-w-1}\chi_0(x/v)\,dv.
$$
Indeed the dilation norm is $\sqrt v$, giving integrability, and the scalar formula follows by integrating from $v=x$ to 1 when $0<x\le1$. By boundedness and dilation commutation,
$$
U(\chi_0 x^{-w})(x)=\varphi(x)+w\int_1^\infty u^{w-1}\varphi(xu)\,du.
$$
If $\varphi(x)=O(x^{-\kappa})$ at infinity with $\kappa>1/2$, then the last integral and its fixed parameter derivatives have a locally uniform majorant after any fixed cutoff $x>\lambda>0$, on compact $w$-sets crossing the critical line and contained in $\Re w<\kappa$. On the tail the majorant is $O(x^{-\kappa})$, with fixed constants. On a bounded interval $\lambda\le x\le X$, split the integral at a large fixed $u$ and use local $L^1$ integrability of $\varphi$ after substituting $y=xu$. The nonintegral term has the separate $L^2$ majorant $|\varphi(x)|$. This suffices for the truncated boundary jet limit by dominated convergence. Neither this argument nor the resulting exact cutoff orthogonality requires $x\varphi'\in L^2$. [Explicit beta example and finite-cutoff proof](chi4_effective_phase_lower_skeptic62.md)
