# Lagarias's right-half-line Morse operator | Whole-work advocate

PAPER-LAG2009-MORSE. I read all 33 pages of the pinned Jeffrey C. Lagarias arXiv:0712.3238v6, including §§1–6, both appendices, and bibliography entries [1]–[74]. The body is dated 10 August 2009 and arXiv posted v6 on 18 August 2009. The pinned PDF SHA-256 is 307d253d70abc7d8ef3d24355e9ab7708010bda18c7b9060a4913033c6e224be. I compared the earlier version metadata and principal statements, and checked the core passages and both appendices in the published manifestation, *Communications in Number Theory and Physics* 3(2), 323–361 (2009). The complete reading applies to the pinned v6. I propose Level 1 for that reading. The local reconstructions and source qualifications below are additional review evidence. [Pinned v6](../../sources/prefix_skeptic62_spectral/lagarias_morse.pdf) · [Version history](https://arxiv.org/abs/0712.3238) · [Journal identity](https://doi.org/10.4310/CNTP.2009.v3.n2.a3) · [Publisher PDF](https://intlpress.com/api/bgcloud-front/resource/pdf/volume/1805800182296035329-1805800182296035329-c120f85c336773853a96543363875a8c.pdf)

## Theorem map and dependencies

| v6 printed pages | Main contribution | Input and scope |
|---|---|---|
| 1–7, §1 | Introduces the confining right-half-line problem, contrasts line and left-half-line scattering spectra, and states the Whittaker and zeta analogy. | Morse's original potential, Whittaker/Bessel antecedents, and the two-sign zeta count. The toy model distinction is explicit. |
| 7–11, §2 | Theorem 2.1 gives the Whittaker substitution, subordinate solution, self-adjoint separated domains and simple discrete spectrum. Theorem 2.2 gives endpoint and \(k\)-monotonicity. | Whittaker asymptotics, singular endpoint classification, Sturm theory and minimax, citing Whittaker–Watson [74], Reed–Simon [55–56], Levitan–Sargsjan [45], and Coddington–Levinson [17]. |
| 11–15, §3 | Theorem 3.1 gives an \(O(1)\) Weyl remainder for an eventually increasing convex potential. Theorem 3.2 evaluates both leading Morse terms. | Titchmarsh [67, Theorem 7.4] and a finite left-end correction. The first two coefficients are independent of \(k\) and the fixed boundary condition \(\alpha\). |
| 15–18, §4 | Theorem 4.1 gives entire growth, reflection, zero axes and multiplicity, the finite exceptional set, and its two-sign count. | Theorems 2.1 and 3.2, Appendix A, and the energy substitution \(E=-\mu^2\). The printed multiplicity argument needs the transversality step below. |
| 18–23, §§5–6 | Compares scattering and spectral interpretations, gives the canonical-system interface and a Morse de Branges example, and distinguishes two \(m\)-functions. | The arithmetic de Branges construction cites [40–42]. Invertibility and regularity of its canonical coefficient remain open here. The exact Morse canonical-system example cites [43], listed as in preparation. |
| 23–25, Appendix A | Normalized Kummer function, Whittaker branches, parameter symmetry and growth. | [8], [64], [70], and [74]. The fixed positive \(x\) setting is crucial to the spectral application. |
| 25–28, Appendix B | Theorem 8.1 gives the principal Weyl–Titchmarsh \(m\)-function, with boundary rotation and Riccati identity. | Theorem 2.1 and the differentiation recurrence [1, (13.4.33)]. Sectorial asymptotics and inverse reconstruction are cited inputs. |
| 28–33 | References [1]–[74]. | Bibliography read and main dependencies mapped. Reading the reference list does not constitute reading each cited work. |

## Boundary problem and exact spectral identification

Fix \(k,u_0\in\mathbb R\). Work on \(L^2([u_0,\infty),du)\) with
\[
 \tau_k=-\frac{d^2}{du^2}+\frac14e^{2u}+ke^u,\qquad
 \cos\alpha\,f(u_0)+\sin\alpha\,f'(u_0)=0 .
\]
The standard maximal-domain formulation requires \(f,f'\) locally absolutely continuous up to the regular endpoint and \(f,\tau_k f\in L^2\), then imposes the displayed boundary condition. This specifies the local regularity behind the notation on p. 9, where a stronger global absolute-continuity notation is used. At the singular endpoint there is no additional boundary condition. With \(x=e^u\) and \(f=x^{-1/2}F(x)\), the equation becomes \(F''+[-1/4-k/x+(1/4+E)/x^2]F=0\). Thus \(\kappa=-k\), \(\mu^2=-E\), and the normalized square-integrable solution at \(+\infty\) is
\[
 y(u,E)=e^{-u/2}W_{-k,\sqrt{-E}}(e^u).
\]
The sign of the square root is immaterial by evenness. The \(x\to+\infty\) asymptotic \(W_{\kappa,\mu}(x)\sim e^{-x/2}x^\kappa\) gives double-exponential decay in \(u\). A second solution via reduction of order \(y(u)\int^u y(v)^{-2}\,dv\), taken sufficiently far to the right where \(y\) has no zeros, grows and is outside \(L^2\). This gives the limit-point assertion for the entire energy plane without relying on the printed characterization of when \(M_{\kappa,\mu}\) and \(W_{\kappa,\mu}\) are independent. For example at \((\kappa,\mu)=(1/2,0)\) the Kummer parameter is zero and the two standard functions coincide, despite \(\kappa\) being positive.

Weyl endpoint theory gives self-adjointness after the one left condition. Independently, the shifted quadratic form is bounded below because for Robin data its endpoint contribution is \(-\cot\alpha\,|f(u_0)|^2\), controlled by the trace inequality against the derivative and \(L^2\) terms. The potential tends to infinity, giving compact form embedding by local compactness and control of the tails. Every eigenspace is one dimensional because the subordinate space at the right is one dimensional. For Dirichlet data \(E_0>0\) when \(k\ge0\). For \(k<0\), \(V_k(u)+k^2=(e^u/2+k)^2\ge0\) and the Dirichlet form on an eigenfunction has strictly positive derivative contribution, so \(E_0>-k^2\). This also avoids a quantifier gap in the harmonic-oscillator comparison on p. 10, where the comparison scale may depend on \(\epsilon\). A uniform lower bound over all Robin parameters would fail. The boundary condition is periodic in \(\alpha\) modulo \(\pi\).

For Theorem 2.2, translation to \(v=u-u_0\) fixes both the form domain and boundary condition. The potential strictly increases under the stated changes of \(k\), or of \(u_0\) when \(k\ge0\) or \(u_0\ge\log(2|k|)\). Strictness in minimax follows by using the finite eigenspace span of the larger-potential operator and the positive minimum of the form difference on that finite unit sphere.

## Weyl law and the phase integral

For fixed separated data write \(N_\alpha(T)=\#\{E_n<T\}\). Theorem 3.1 gives \(N_\alpha(T)=I_k(T)/\pi+O(1)\) with \(I_k(T)=\int_{u_0}^{u_T}\sqrt{T-V_k(u)}\,du\). The source adapts Titchmarsh's oscillation estimate by absorbing the compact non-monotone part. Another direct way to see the extension is to cut at a sufficiently large \(u_1\), imposing a Dirichlet point there. The restriction is codimension one in the form domain, so the count changes by at most one. The finite left interval has count \((u_1-u_0)\sqrt T/\pi+O(1)\) by bounded-potential comparison with the separated kinetic operator. The right interval is in Titchmarsh's increasing convex regime. The compact left action differs from \((u_1-u_0)\sqrt T\) by \(O(T^{-1/2})\). A turning point is unique for \(T\) strictly above the maximum in the possibly non-monotone part, and the high-energy threshold may be enlarged.

The source expands the transformed integral by (3.4)–(3.11). At \(R=\sqrt T\) the result is
\[
 N_\alpha(T)=\frac{R}{\pi}\log R+
      \frac{2\log2-1-u_0}{\pi}R+O(1).
\]
A short independent calculation uses \(x=e^u/2\) and \(x_0=e^{u_0}/2\). For large \(T\), \(I_k=\int_{x_0}^{-k+\sqrt{T+k^2}}\sqrt{T-x^2-2kx}\,dx/x\), and the integrable differentiated endpoint is
\[
 \frac{\partial I_k}{\partial k}
 =-\int_{x_0}^{-k+\sqrt{T+k^2}}\frac{dx}{\sqrt{T-x^2-2kx}}
 =-\frac{\pi}{2}+\arcsin\frac{x_0+k}{\sqrt{T+k^2}} .
\]
There is no boundary term because the numerator vanishes at the turning point. Differentiation can be justified by cutting just below that point and using the uniform integrable square-root singularity for \(k\) in a compact interval. Thus \(I_k=I_0-\pi k/2+O_{k,u_0}(T^{-1/2})\). For \(k=0\), \(x/R=\sin t\) evaluates \(I_0=R(\log(2R/x_0)-1)+O_{u_0}(R^{-1})\). This sharpened *action difference* does not identify a new constant for the staircase error. The strict and inclusive eigenvalue conventions differ by at most one.

## Entire zeros and the multiplicity repair

Set \(Z(\mu)=W_{\kappa,\mu}(e^{u_0})\), \(k=-\kappa\). Appendix A gives a single-valued entire function in \(\mu\) for fixed \(\kappa\) and positive \(x\); in the \(x\)-variable the source instead fixes the principal branch on the cut plane. The two-branch Kummer expression has apparent singularities when \(2\mu\) is integral, so directly using the two terms at those points is unsafe. Their entire continuation is the \(W\) solution. Evenness follows from the differential equation and the shared normalization at \(+\infty\). Real \(\kappa\) plus conjugation implies reality on both axes. The growth bound \(e^{O(|\mu|\log(|\mu|+2))}\) from Appendix A gives order at most one. One way to substantiate this estimate is to use \(W=e^{-x/2}x^{\mu+1/2}U(a,c,x)\), \(a=\mu-\kappa+1/2\), \(c=1+2\mu\), with the Kummer integral. In the evenness-reduced region \(\Re\mu\ge0\), integrate its \(t^{a-1}\) factor by parts a fixed number of times so that \(\Re(a+N)>0\), and divide by \(\Gamma(a+N)\). The remaining \(N\)-th derivative of \(e^{-xt}(1+t)^{\mu+\kappa-1/2}\) contributes a fixed polynomial in \(|\mu|\) times an integrable gamma-type majorant. Stirling's bound for the reciprocal gamma factor and this majorant give the stated growth. The zero count rules out finite type at order one by Jensen's formula.

A zero gives an \(L^2\) Dirichlet eigenfunction at \(E=-\mu^2\). Self-adjointness forces \(E\in\mathbb R\), and hence \(\mu\) is real or imaginary. Real zeros come only from nonpositive Dirichlet energies, are finite, and satisfy \(|\mu|<\kappa\) when \(\kappa>0\). There are none for \(\kappa\le0\). The source's spectral simplicity alone does not establish the order of a characteristic zero. Put \(\dot y=\partial_E y\) and take a real Dirichlet energy \(E_*\). Then
\[
 \frac{d}{du}\big(y\dot y'-y'\dot y\big)=-y^2,\qquad
 -y'(u_0,E_*)\dot y(u_0,E_*)=\int_{u_0}^{\infty} y(u,E_*)^2\,du>0 .
\]
The term at infinity vanishes by the locally uniform Whittaker asymptotic and its derivative, with Cauchy estimates in energy for the parameter derivative. The nonzero \(y'\) at \(u_0\) follows by uniqueness for the ODE. Thus the Dirichlet characteristic \(y(u_0,E)\) has simple zeros in \(E\). Substitution \(E=-\mu^2\) gives simple zeros for \(\mu\ne0\), and exactly double at zero if there is a zero-energy eigenvalue. This repairs the one-sentence justification in Theorem 4.1.

For large \(T>0\), the number of all \(Z\) zeros with \(|\Im\mu|\le T\), counted with analytic multiplicity, is exactly twice the inclusive Dirichlet count at \(T^2\). Positive energies give \(\pm i\sqrt E\), negative energies give two real zeros, and zero counts twice at the origin. The printed proof drops the factor two and square in a displayed intermediate count, while the stated final expression is correct:
\[
  N_Z(T)=\frac2\pi T\log T+
           \frac2\pi(2\log2-1-u_0)T+O(1).
\]
For \(Z_1(s)=W_{\kappa,s-1/2}(e^{u_0})\), the substitution is \(s=\frac12+\mu\). The opposite translation in introductory prose and the corresponding §4 line are slips. Passing from height to \(|s|<T\) on the line moves the large cutoff by \(O(1/T)\), affecting the asymptotic count by \(O(1)\) from the Weyl formula. Real exceptions affect a bounded range. The \(k=0\) K-Bessel identification (4.7) is a distinct classical check.

## The Weyl function and a separate spectral zeta consequence

With the principal boundary normalization of (8.1)–(8.3), \(m(u_0,E)=y'(u_0,E)/y(u_0,E)\), and Green's identity gives
\[
 \Im m(u_0,E)=\Im E\,
    \frac{\int_{u_0}^{\infty}|y(u,E)|^2\,du}{|y(u_0,E)|^2}>0
 \quad (\Im E>0).
\]
Changing the separated boundary angle gives the Möbius expression (8.3). Differentiating in the base point gives \(m'+m^2=V_k-E\). The recurrence in (8.6) gives Theorem 8.1,
\[
 m(u_0,z^2)=\tfrac12e^{u_0}+k-\tfrac12
   -\frac{W_{1-k,iz}(e^{u_0})}{W_{-k,iz}(e^{u_0})}.
\]
The numerator should be \(W_{1-k,iz}\) in the proof's (8.7) as well. The journal labels these as Theorem B.1 and (B.4)–(B.7), and retains the numerator slip in (B.7). A simple Dirichlet pole \(E_*\) has residue \(-y'(u_0,E_*)^2/\int y(u,E_*)^2\,du\) by the transversality identity. The poles, zeros and their norming information are strictly more data than a Weyl count. Section 6's de Branges quotient \(-B/A\) is a first-order canonical-system object associated to \(z\); it is not itself this second-order quotient in \(E=z^2\).

The paper gives an entire characteristic and a counting law, rather than a Dirichlet series called an operator spectral zeta function. One consequence of Theorem 3.2 can be recorded explicitly. Choose a fixed \(c\) so that all \(E_n+c>0\). The auxiliary operator series \(\zeta_{H,c}(s)=\sum_n(E_n+c)^{-s}\) has absolute convergence abscissa \(1/2\). A fixed shift changes the displayed smooth count by \(O(1)\). Writing the count as \(A\sqrt t\log t+B\sqrt t+O(1)\) with \(A=1/(2\pi)\), \(B=(2\log2-1-u_0)/\pi\), partial integration above \(t=1\) gives meromorphic continuation to \(\Re s>0\). The bounded remainder contributes a holomorphic integral there, and the polar part at \(s=1/2\) is
\[
 \frac{1}{4\pi(s-\tfrac12)^2}
       +\frac{2\log2-u_0}{2\pi(s-\tfrac12)}.
\]
This is a spectral counting consequence, with neither an Euler product nor a prime trace deduced. Independently the characteristic in energy is entire of order \(1/2\), by evenness and the growth/count in \(\mu\); its nonzero zeros admit a genus-zero product because \(\sum_{E_n\ne0}|E_n|^{-1}<\infty\). Include a factor \(E\) if zero is an eigenvalue. This product is over the Morse spectrum. The Weyl quotient supplies the additional norming data.

## What the Riemann-shaped count does and does not match

A precise obstruction follows even after allowing a positive constant rescaling of the positive Morse ordinates. The positive model count at \(t=T/2\) has leading \(T\log T/(2\pi)\), and \(u_0=\log(4\pi)\) matches the zeta linear term. This is the unique positive rescaling and endpoint that match both coefficients. The model then has bounded remainder, for every fixed \(k,\alpha\). The zeta count away from zero ordinates has remainder \(S(T)+O(1)\) relative to the same two terms, and the unconditional Selberg oscillation quoted in Titchmarsh §9.9, (9.9.7), makes \(S(T)\) unbounded. Hence this constant-rescaling comparison cannot give equality of spectra even after changing finitely many entries. Adding a fixed shift of the ordinate could add a term of order \(\log T\), so the stated obstruction is for the specified multiplicative rescaling of energies/ordinates. [Titchmarsh, §§9.4 and 9.9](../../sources/selberg_round2/titchmarsh_zeta.pdf)

The source's §5 statement about clock spacing does not follow from an \(O(1)\) count error alone. At unfolded positions \(x_n=n+(-1)^n c\), \(0<c<1/2\), one has \(N(x)=x+O(1)\) while consecutive gaps alternate between \(1-2c\) and \(1+2c\). A separate Whittaker phase estimate would be required to prove the asserted clock behavior of the actual model from asymptotics of individual zeros. Likewise, no prime trace identity follows from the level count, from the existence of a positive self-adjoint domain, or from a genus-zero product.

The literal nonzero-shifted arithmetic function in §5 fails the printed strict Hermite–Biehler inequality, and the convention for the de Branges quotient in §6 has the opposite sign from its explicit Herglotz claim. Both also occur in the journal. The rendered countertests and precise algebraic repairs are recorded separately. [Rendered convention check](geometry120_lagarias_morse_rendered_conventions.md)\n\nThe concrete arithmetic gap in §5 is earlier than identifying a candidate potential. The cited de Branges construction for \(E_0(z)=\xi(1/2-iz)+\xi'(1/2-iz)\) is tied to RH. An arithmetic diagonal canonical coefficient is not shown here to be invertible almost everywhere or smooth enough for determinant-one reparameterization and (5.4). Even for a smooth transform, eigenparameter-dependent boundary data on one partner require a separate fixed-domain realization before invoking ordinary scalar self-adjointness. The fixed separated Morse domain in Theorem 2.1 verifies none of those additional arithmetic hypotheses. The toy example with \(k=-1/2\) explains the map in a solvable case.

## Version and review boundary

The arXiv record lists v1 (19 Dec 2007), v2 (11 Nov 2008), v3 (16 Dec 2008), v4 (18 Dec 2008), v5 (26 Jun 2009), and v6 (18 Aug 2009). I retrieved v1–v5 and compared the core theorem statements and the changed text around the principal proofs. The initial version already contains the three main Morse/Whittaker statements. Earlier versions have 26, 29, 30, 29, and 33 PDF pages respectively. In the v5-to-v6 comparison, the abstract's exceptional interval is corrected, the Dirichlet oscillator comparison value changes from \(1/2\) to \(3\), and the strict lower energy bound is stated in place of the earlier weak one. The direct form proof above makes this strictness transparent. The publisher PDF retrieved for cross-check has SHA-256 268dff410dae549b457c45375007922e91cc8b9b7e23530814044d42bb54b280 and adds a provider page to the 39 journal pages. It typesets the appendices as A and B and retains the short multiplicity justification in §4. The scoped comparisons of the other manifestations do not upgrade their reading status.

The complete v6 reading, the proof map, and the explicit repairs support the main Morse model, spectral count, Whittaker zero theorem and Weyl quotient. They leave the full proof ancestry of Titchmarsh's oscillation theorem, the external de Branges claims, the inverse uniqueness theorem, and any independent clock-spacing theorem outside this advocate report. No canonical record was changed. [Proposed reading update](../../quality/pending_round15/geometry120_lagarias_morse_source_update.jsonl)
