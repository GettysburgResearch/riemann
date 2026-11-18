# Independent whole-work reconstruction of Lagarias’s right-half-line Morse model

**PAPER-LAG2009-MORSE.** The principal right-half-line spectral and Whittaker results in the pinned arXiv v6 survive reconstruction. The characteristic-zero multiplicities need an energy-derivative argument beyond spectral simplicity. The Weyl law gives a genuine zeta analogy, but even after matching both smooth coefficients the model cannot give the zeta counting measure. Section 5 has a specific printed shifted-structure-function mismatch, and the sign of the de Branges ratio in §6 must be tracked separately from the true Herglotz Weyl function in Appendix B. These are version-specific checks for director review. No canonical promotion or finding was made. [Reading ledger](analytic120_lagarias_morse_reading_coverage.md)

I read all 33 printed pages of Jeffrey C. Lagarias, *The Schrödinger Operator with Morse Potential on the Right Half Line*, arXiv:0712.3238v6, posted 18 August 2009, manuscript line “August 10, 2009-revision.” The file `sources/prefix_skeptic62_spectral/lagarias_morse.pdf` hashes to **307d253d70abc7d8ef3d24355e9ab7708010bda18c7b9060a4913033c6e224be**. Crossref identifies the journal manifestation as *Communications in Number Theory and Physics* **3**(2), 323–361, DOI **10.4310/CNTP.2009.v3.n2.a3**. The controlling proof read here is v6, so printed issues are not assigned to the separate journal bytes. [Pinned version](https://arxiv.org/pdf/0712.3238v6) · [Version history](https://arxiv.org/abs/0712.3238) · [Journal DOI](https://doi.org/10.4310/CNTP.2009.v3.n2.a3)

## §§1–2 | Operator and endpoint domain

Put \(x=e^u\), \(V_k(u)=e^{2u}/4+ke^u\), \(k,u_0\in\mathbb R\), on \(L^2([u_0,\infty),du)\). Substitute \(y(u)=e^{-u/2}f(e^u)\). Direct differentiation gives \(y''=e^{-u/2}(x^2 f''+f/4)\), so \((-\partial_u^2+V_k)y=Ey\) is equivalent to Whittaker’s equation with \(\kappa=-k\) and \(\mu^2=-E\). In particular the sign of the Whittaker index is opposite that of the linear potential coefficient. A recessive solution for every complex \(E\) is
\[
y(u,E)=e^{-u/2}W_{-k,\pm\sqrt{-E}}(e^u).
\]
The large-positive-argument normalization \(W_{\kappa,\mu}(x)\sim e^{-x/2}x^\kappa\) fixes a nonzero solution and is even in \(\mu\) by uniqueness. An independent solution on a sufficiently far interval is obtained by reduction of order, with growth \(\asymp e^{x/2} x^{-\kappa-1/2}\) in the \(u\)-variable. Thus the recessive line is the unique square-integrable line and the infinite endpoint is limit point. A recessive solution solves the differential expression, while an operator eigenfunction additionally satisfies the boundary condition at \(u_0\).

For \(\sin\alpha=0\) impose Dirichlet; otherwise write \(y'(u_0)=h y(u_0)\), \(h=-\cot\alpha\). The fixed Robin form is \(\int(|y'|^2+V_k|y|^2)du+h|y(u_0)|^2\), on \(H^1\) with \(\int V_{k,+}|y|^2<\infty\). Dirichlet restricts to trace zero. The trace estimate makes the boundary term relatively form bounded with arbitrarily small kinetic coefficient. After a constant shift the form is closed and bounded below for each fixed boundary parameter. Local Rellich compactness and coercivity of \(V_k\to+\infty\) give compact form embedding, hence compact resolvent. The associated operator is the regular-left, limit-point-right maximal differential domain with the specified boundary relation. More explicitly, it consists of square-integrable \(f\) with \(f,f'\in AC_{\mathrm{loc}}\), \(-f''+V_k f\in L^2\), and the left condition. For this smooth Morse potential one may also require \(f''\) and \(V_k f\) separately in \(L^2\). To see this, add a constant to make \(W=V_k+C\ge1\). On compactly supported domain vectors, the cross term in \(\|-f''+Wf\|_2^2\) gives \(2\int W|f'|^2-\int W''|f|^2\), with a fixed multiple of \(|f(u_0)|^2\) at the boundary. Since \(|W''|\ll W\), the negative terms can be absorbed by \(\|Wf\|_2^2+2\int W|f'|^2\) with a remaining \(O(\|f\|_2^2)\). Apply this to growing cutoffs of an operator-domain vector, using \(f'\in L^2\) from the form domain. This checks the stronger displayed domain for the Morse potential without using it as a blanket condition for arbitrary continuous potentials.

The eigenvalues are real, simple, bounded below, and exhaust a discrete sequence increasing to infinity. The one-dimensional recessive line proves geometric simplicity, and self-adjointness precludes generalized eigenvectors. Sturm oscillation gives exactly \(n\) interior nodes for the \(n\)th eigenfunction indexed from zero. For Dirichlet, \(V_k\ge e^{2u_0}/4\) when \(k\ge0\). For \(k<0\), \(V_k=(e^u/2+k)^2-k^2\), and the ground state's form identity gives strictly \(E_0>-k^2\), since equality would require vanishing derivative and zero Dirichlet trace. This proves the strict bound without needing uniform oscillator parameters in the printed comparison. The strict potential comparisons in Theorem 2.2 follow on translating to a fixed domain. Increasing \(k\) changes the potential by \(\Delta k\,e^u\), uniformly positive on the half-line. Moving a left endpoint to the right while keeping the same Robin parameter translates the potential by a positive distance. On the declared monotone ranges the difference is strictly positive everywhere, tends to infinity, and has a positive minimum. The min–max inequalities are strict. For Dirichlet alone the endpoint increase in fact holds even below the minimum of the well by Sturm endpoint differentiation or zero-extension plus uniqueness.

Two sharp boundary checks distinguish the quantifiers. The family is \(\pi\)-periodic in \(\alpha\). A sequence \(\alpha\to0^+\) modulo \(\pi\) gives \(h\to-\infty\). The normalized trial function proportional to \(e^{h(u-u_0)}\) has kinetic-plus-boundary expectation \(-h^2\), and bounded potential expectation as \(h\to-\infty\). Thus no uniform lower bound is possible over all Robin parameters, even at \(k=0\). The Dirichlet lower bounds do not apply to that family. Independently, if \(Q_k=\partial_u+e^u/2+k+1/2\), then on the Dirichlet form
\[
H_k=Q_k^*Q_k-(k+1/2)^2 .
\]
There is strict positivity for \(k=-1/2\) because the kernel solution of \(Q_k y=0\) has nonzero endpoint trace. Monotonicity gives positivity for \(k\ge-1/2\), and for \(k<-1/2\) the same argument gives \(E_0>-(k+1/2)^2\). For any fixed \(k<-1/2\), the full-line kernel \(e^{-e^u/2-(k+1/2)u}\) is square integrable and has negative energy. Truncating it by smooth cutoffs gives a negative Dirichlet test when \(u_0\) is sufficiently far left. Hence the stronger universal exception threshold is \(\kappa>1/2\), while a specified fixed \(u_0\) can still have no negative level. A central zero is possible: at fixed \(u_0\), \(E_0(0)>0\) and \(E_0(k)<0\) for sufficiently negative \(k\) by a fixed compactly supported trial function. The ground energy is continuous in \(k\), by the common form domain or finiteness and concavity of the variational infimum, and strictly increasing. At its unique crossing, the central Whittaker zero has order two as checked below.

Two local substitutions on pp. 8–9 require care. To normalize to \(e^{2u}/4\), use \(v=u-\tfrac12\log(4A)\), \(u_0=v_0+\tfrac12\log(4A)\), and \(k=B/(2\sqrt A)\). The printed paragraph instead uses \(A/4\) in the coordinate shift, \(2B/\sqrt A\) in the linear coefficient, and a different endpoint translation. Substitution into the specified potential confirms the corrected triple. The designation of \((W_{\kappa,\mu},M_{\kappa,\mu})\) as a basis except at nonpositive-integer \(\kappa\) is not a valid general criterion. For instance \(\kappa=1,\mu=1/2\) gives \(M=W=x e^{-x/2}\) by (7.5) and the recessive normalization. The theorem only needs an arbitrary independent solution, supplied by reduction of order on the tail.

## §3 | Weyl count and two independent checks

The convexity used in Theorem 3.1 is the eventual increasing-slope condition, in the source’s “convex downwards” terminology. Apply the cited Titchmarsh single-turning-point \(O(1)\) estimate on an eventual monotone convex tail. If the initial interval \([u_0,u_1]\) is not monotone, split there by Dirichlet–Neumann bracketing. On the fixed compact interval a bounded potential changes each eigenvalue by at most its sup norm, and the free one-dimensional count with the separated conditions is \((u_1-u_0)\sqrt T/\pi+O(1)\). This is also the contribution of the compact part of the phase integral to \(O(1)\). Dirichlet and Neumann cut endpoints thus give the same asymptotic precision. This reconstructs the eventual-tail extension without the printed substitution into the proof of the imported theorem. Take \(T_1\) strictly above the compact potential maximum as needed for turn uniqueness. The cited Titchmarsh monotone-tail theorem is a classical input here. The Morse case below has an independent count from the Whittaker connection formula.

For the phase integral let \(x=e^u/2\), \(x_0=e^{u_0}/2\), and \(X_k=\sqrt{T+k^2}-k\). Then
\[
 I_k(T)=\int_{x_0}^{X_k}\sqrt{T-x^2-2kx}\frac{dx}{x},\qquad
 \partial_k I_k(T)=-\int_{x_0}^{X_k}
       \frac{dx}{\sqrt{T+k^2-(x+k)^2}} .
\]
At large \(T\), the latter integral is bounded by \(\pi\) uniformly for \(k\) in a fixed compact interval. Differentiation is justified by the square-root behavior at the moving endpoint, or integrating the integrable interior derivative first by Fubini. Thus \(I_k=I_0+O_k(1)\). Substituting \(x=\sqrt T\,\operatorname{sech}v\), or integrating \(\sqrt{1-s^2}/s\), gives
\[
 I_0(T)=\sqrt T[\log(2\sqrt T/x_0)-1]+O(T^{-1/2}).
\]
This independently matches the source cancellation in (3.5)–(3.12), including the factor \(2\log 2\). The conclusion for every fixed separated real boundary condition is
\[
 N(T)=\frac{\sqrt T}{\pi}\log\sqrt T
 +\frac{2\log2-1-u_0}{\pi}\sqrt T+O(1).
\]
For the source substitution \(w=T^*/(e^u/2+k)\), the correct endpoint identity is \(T^*/w_0=e^{u_0}/2+k\), as subsequently used in (3.6). Choosing \(k,u_0,\alpha\) fixed avoids making a uniformity claim over moving operators.

For an independent verification and the later normalized spacing claim, now use \(x=e^{u_0}\), \(c=1/2-\kappa\), and write at \(t>0\)
\[
 W_{\kappa,it}(x)=2\Re A_x(t),\qquad
 A_x(t)=\frac{\Gamma(-2it)}{\Gamma(c-it)}
 e^{-x/2}x^{1/2+it}\,{}_1F_1(c+it,1+2it;x).
\]
For \(x\) in a compact positive interval the hypergeometric factor is \(e^{x/2}+O(t^{-1})\), with \(t\)-derivative \(O(t^{-2})\), also after one \(x\)-derivative. Indeed each factor \((c+j+it)/(1+j+2it)\) in its Pochhammer ratio is uniformly bounded, differs from \(1/2\) by \(O((j+1)/t)\), and has derivative \(O((j+1)/t^2)\). Telescoping the product yields summable bounds against \(x^j/j!\). Stirling's logarithmic derivative now yields
\[
 \partial_t\arg A_x(t)=-\log t-2\log2+\log x+O(t^{-2})
\]
on a continuous branch for all large \(t\). This gives the Dirichlet count through \(t=\sqrt{T}\) with \(O(1)\) error. For fixed Robin data the complex phase is multiplied by \(\cos\alpha+\sin\alpha(it+O(t^{-1}))\): the \(-1/2\) from \(y=x^{-1/2}W\) cancels the fixed half power. When \(\sin\alpha\ne0\) this multiplier has limiting argument and derivative \(O(t^{-2})\); when \(\sin\alpha=0\) the multiplier is a nonzero constant. Thus the same law follows for all the printed Morse boundary cases without the abstract Weyl theorem. Also consecutive positive Dirichlet \(t\)-zeros differ by \(\pi/(\log t+2\log2-\log x)(1+o(1))\). This supplies the local regularity in §5 independently. An \(O(1)\) counting remainder by itself does not imply normalized equispacing, for example alternating small fixed displacements from a uniform unfolded grid preserve its bounded count error.

## §4 and Appendix A | Entire function, location and multiplicity

Fix real \(\kappa\) and positive \(x=e^{u_0}\), and write \(Z(\mu)=W_{\kappa,\mu}(x)\). Evenness follows from the common equation and unique recessive normalization. Conjugation holds because the coefficients and normalization are real for real energy. Hence \(Z\) is real on the real and imaginary axes. The principal branch in \(x\) is the one used here. The power-series normalization of \({}_1\widetilde F_1(a,b;x)\) is entire in \((a,b,x)\), and the continuation of \(W\) at coinciding indicial exponents in (7.7)–(7.8) is analytic. One direct order bound avoids relying solely on the keyhole estimate (7.9). Set \(a=\mu-\kappa+1/2\), \(b=1+2\mu\) in the Euler integral for \(U(a,b,x)\). For fixed integer \(j\) with \(\Re(a+j)>0\) on \(\Re\mu\ge0\), integration by parts and continuation write
\[
 U(a,b,x)=\frac{(-1)^j}{\Gamma(a+j)}
   \int_0^\infty t^{a+j-1}\partial_t^j
      [e^{-xt}(1+t)^{b-a-1}]dt .
\]
This is holomorphic on a slightly enlarged right half-plane. It agrees there with the original integral where \(\Re a>0\), and the evenness of \(W=e^{-x/2}x^{\mu+1/2}U\) covers the other half-plane. The derivative contributes at most a fixed polynomial in \(|\mu|\); on \(t\ge1\) the integral is bounded by a gamma integral with parameter \(2\Re\mu+O(1)\), and on \(0<t\le1\) it has a fixed integrable majorant times \(e^{O(|\mu|)}\). Stirling for the prefactor gives \(\exp(O(|\mu|\log(|\mu|+2)))\), hence order at most one.

For multiplicity, define the entire energy characteristic \(F(E)=y(u_0,E)\), with \(E=-\mu^2\). At a real Dirichlet eigenvalue \(E_*\), \(y(u_0,E_*)=0\) and \(y'(u_0,E_*)\ne0\). Differentiation in \(E\) gives
\[
 (y\,\partial_Ey'-y'\,\partial_E y)'=-y^2 .
\]
The Wronskian term vanishes at infinity by the recessive expansion locally uniformly in the parameter, with Cauchy estimates for the energy derivative. Integration gives
\[
 y'(u_0,E_*)\,\partial_E y(u_0,E_*)
      =-\int_{u_0}^\infty y(u,E_*)^2du\ne0 .
\]
This proves a simple zero of \(F\). A simple eigenvalue alone does not prove the order of an arbitrary analytic characteristic, since squaring a characteristic leaves its spectral set unchanged. Composing \(F\) with \(E=-\mu^2\) proves a simple zero at each nonzero \(\mu\) and an exact double zero if \(E=\mu=0\).

The zeros correspond bijectively to the two roots of each real Dirichlet energy, counting the double central root. Positive energies give imaginary roots, negative energies real roots, and the latter and the possible central root are finite. The original bounds give no real zero for \(\kappa\le0\) and \(|\mu|<\kappa\) when \(\kappa>0\). The stronger check above excludes real zeros for \(\kappa\le1/2\) and gives \(|\mu|<\kappa-1/2\) for \(\kappa>1/2\). All these statements keep \(\kappa\) real and \(x>0\) fixed, and are about the **parameter** \(\mu\), not zeros as a function of the spatial variable \(x\). Counting both signs gives
\[
 \#\{\mu:Z(\mu)=0,|\Im\mu|\le t\}
 =2 N(t^2)+O(1)=\frac{2t}{\pi}\log t
  +\frac{2t}{\pi}(2\log2-1-u_0)+O(1).
\]
The factor two and the squared threshold are necessary in the intermediate equality on p. 17. The choice of strict versus inclusive endpoint changes at most two at high thresholds. The equivalent disk count differs by at most a bounded quantity since there are only finitely many real roots. Jensen now gives order one and infinite type. Shift by \(\mu=s-1/2\), so \(s=\mu+1/2\); the prose on p. 3 and the restatement on p. 15 reverse this translation, while the displayed \(Z_1(s)=W_{\kappa,s-1/2}(x)\) and the symmetry \(Z_1(s)=Z_1(1-s)\) use the correct relation. Appendix A’s printed mention of a possible \(M\)-pole at \(\mu=0\) is not borne out by (7.5), where \(b=1\). The standard unnormalized \(M\) can have lower-half-integer poles where \(1+2\mu\) is a nonpositive integer. The branch factor in (7.5) is \(x^{1/2+\mu}\). The exact checks here use that formula and its normalized series.

## §§5–6 | de Branges analogy and the actual zeta gap

There is a precise smooth-count comparison. Positive Morse ordinates have leading coefficient \(1/\pi\), whereas positive zeta ordinates have coefficient \(1/(2\pi)\). Scaling the Morse ordinates by two and choosing \(u_0=\log(4\pi)\) matches both smooth terms. Any other fixed scaling and endpoint must already match these two coefficients to give identical multisets. Even at the matching parameters the Morse remainder is bounded. The Riemann–von Mangoldt remainder \(S(t)\) is unbounded, for example by Selberg’s second-moment asymptotic cited in Titchmarsh §9.25, since \(T^{-1}\int_0^T|S(t)|^2dt\) grows like a positive multiple of \(\log\log T\). This excludes equality with the true zeta counting measure, even up to an added or removed finite set. It is independent of GUE predictions and RH. In the energy variable the Morse characteristic has order \(1/2\) and its canonical genus-zero product is over the actual Morse energies. A nowhere-zero normalization cannot change those roots into zeta ordinates. The paper supplies neither the prime-power oscillatory terms of an arithmetic trace formula nor an unconditional zeta determinant. Its comparisons with modular scattering, Connes, Meyer, Burnol and the cited physical models are context, and were checked as roles in the argument rather than whole audits of those works. [Titchmarsh reference copy](../../sources/equivalence_round2/titchmarsh1986.pdf)

Here are explicit checks on the auxiliary de Branges formulas. Write \(G(z)=\xi(1/2-iz)\), real entire and even. The source’s (5.5) defines \(E_0=G+iG'\). Under RH the paired real-zero product gives \(\Im(G'/G)<0\) in the upper half-plane, including positive multiplicities in the sum. Consequently \(E_0\) satisfies (5.1). Conversely at an upper-half-plane zero of \(G\), the two squared moduli of \(E_0\) and \(E_0^\#\) are equal, so (5.1) fails. This verifies the equivalence for the weak convention that permits real zeros of \(E\). If \(G\) has a real zero of multiplicity \(m\ge2\), \(G\) and \(G'\) have a common factor of order \(m-1\) there. The simple-spectrum multiplication construction after removal of such common factors cannot establish the simplicity of the zeta zeros or represent their multiplicities as simple eigenvalues. General de Branges multiplication statements also need their density and common-real-zero qualifications. For example, a linear Hermite–Biehler polynomial can give a one-dimensional space, where multiplication is only defined on zero, so blanket densely defined deficiency claims cannot be read without restrictions.

For real \(z\), \(\xi(1/2-h-iz)=\overline{\xi(1/2+h-iz)}\) by the functional equation and real symmetry. Thus the source’s printed **nonzero-\(h\)** formula on p. 20 is real on the entire real \(z\)-axis and cannot satisfy the strict (5.1). Its formal \(h\to0\) limit is \(\xi-i\xi'\), distinct from the separately printed and valid (5.5). A direct compatible replacement is the symmetric average of the two shifted \(\xi\) values plus \((\xi_+-\xi_-)/(2h)\), with no factor of \(-i\). For \(h>0\) this is a real linear combination of \(\xi_+\) and its reflected entire function with squared-coefficient difference \(1/h>0\). It inherits the strict HB inequality whenever the shifted function has it. This is a local formula comparison within v6, not a claim about the cited differenced-L publication. I visually checked the factor \(-i\) in the controlling PDF.

On the canonical-system side, parity can give a diagonal Hamiltonian under the relevant de Branges theorem. Pointwise invertibility and sufficient regularity are separate requirements for the coordinate and Liouville transformations. In determinant-one gauge diagonal entries are \(\alpha,\alpha^{-1}\); writing \(W=\alpha'/(2\alpha)\) and variables \(\sqrt\alpha A,B/\sqrt\alpha\) gives the first-order pair \(\psi'=W\psi-z\chi\), \(\chi'=z\psi-W\chi\). Eliminating gives the two formal potentials \(W^2\pm W'\) in (5.4). The actual transformed boundary domains must be checked. A parameter-dependent boundary equation by itself does not define one self-adjoint Schrödinger domain in the ordinary \(L^2\) space. For a Dirichlet sector and sufficiently regular endpoint, the standard partner is a fixed Robin sector, with the possible zero state accounted for by first-order factorization. The zeta case in the paper remains conditional, with invertibility and regularity not established. A Weyl count alone does not imply the printed speculative necessity of a particular pointwise potential shape for an unrestricted inverse problem.

For the Morse example (5.6), let \(x=e^u\), \(y_\pm=x^{-1/2}W_{\pm1/2,iz}(x)\) and \(Q=\partial_u+x/2\). Factorization and the normalized tail imply \(Qy_+=z^2 y_-\) and \(Q^*y_-=y_+\). This can be checked by intertwining and the leading coefficients at infinity; it also follows by the standard raising recurrence. The actual real-entire components in (5.6) are \(A=e^{x/2}y_+\) and \(B=z e^{-x/2}y_-\), so
\[
 A'=ze^xB,\qquad B'=-ze^{-x}A,qquad
 \partial_u\Im(B\overline A)=-\Im z\,(e^{-x}|A|^2+e^x|B|^2).
\]
The boundary term tends to zero at infinity. Thus \(\Im(B/A)>0\) in the upper half-plane, and \(A-iB\) indeed has the claimed strict HB property. The next printed display on p. 21 gives a different nonzero prefactor for \(A\), which does not change its zeros. The principal spectral sector is still Dirichlet for \(k=-1/2\) and has no zero level. In the convention \(E=A-iB\), (5.1) says \(\Im(B/A)>0\), so the ratio **\(-B/A\)** printed in (6.1) and evaluated in (6.2) is anti-Herglotz. The reconstruction formula on p. 19 also prints the reverse sign for \(B\) relative to \(E=A-iB\). One can use \(B/A\) in that convention or change the definition of \(B\) consistently. At small \(z=iy\), \(y>0\), the two positive-at-zero Whittaker factors in (6.2) give negative imaginary part directly, an independent check of the displayed sign. This sign issue is separate from the principal Weyl function in Appendix B, whose sign is correct.

## Appendix B | The Weyl function and norming data

The combination of the normalized fundamental solutions in (8.1) is a function of \(u\) required to lie in \(L^2\) at infinity. Its value at \(u_0\) alone does not express that condition. The actual construction gives \(m_0(E)=y'(u_0,E)/y(u_0,E)\). With initial pairs \((\cos\alpha,\sin\alpha)\) and \((-\sin\alpha,\cos\alpha)\), solving for the transformed slope gives exactly (8.3). A Green identity gives
\[
 \Im m_0(E)=\Im E\int_{u_0}^\infty |y(u,E)/y(u_0,E)|^2du,
\]
so the principal function is Herglotz in \(E\). Dirichlet eigenvalues are its simple poles, with residue \(-|y'(u_0,E_*)|^2/\|y(\cdot,E_*)\|_2^2<0\) by the Wronskian identity. Neumann eigenvalues are its zeros. Equation \(m'+m^2=V-E\) is immediate on taking the logarithmic derivative. The cited inverse spectral and non-tangential asymptotic results supply context, including the admissible sector \(0<\epsilon\le\arg z\le\pi/2-\epsilon\), \(E=z^2\), and \(m(z^2)\sim iz\). They are not needed to prove the explicit formula or infer unknown parameters from the zeta spectrum.

Inserting (8.6), \(xW'_{\kappa,\mu}=(x/2-\kappa)W_{\kappa,\mu}-W_{\kappa+1,\mu}\), into (8.5) gives
\[
 m(u_0,z^2)=\tfrac12e^{u_0}+k-\tfrac12-
 \frac{W_{1-k,iz}(e^{u_0})}{W_{-k,iz}(e^{u_0})}.
\]
This is the correct Theorem 8.1 display (8.4). Its intermediate line (8.7) prints a different numerator index, visibly \(W_{1-iz,\mu}\); the recurrence fixes the stated theorem. The expression is meromorphic and even in \(z\), as it must be a function of energy. Neither the zero-set comparison nor the Morse m-function identifies a Weyl function with the arithmetic one proposed in the introduction.

The page-by-page ledger names which upstream inputs were used and which historical assertions remain external. All scope decisions above are for the pinned arXiv v6 only. [Coverage ledger](analytic120_lagarias_morse_reading_coverage.md)
