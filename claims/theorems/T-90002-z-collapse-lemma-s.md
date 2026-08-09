# T-90002 — Lemma S promoted: single sign change of s_X and the z-collapse of WSTS

Claim ID: `T-90002` (provisional range; allocate at registry)
Status: **PROVED (Theorems P, Q, S and Corollary C below), modulo two named imported dependencies (both stated PROVED in their home files): T-90001 §1 per-modulus floor bound, and O-90004 Prop A (used only in Corollary C). Finite-cell inequalities certified by high-precision monotone-envelope evaluation with margins ≥ 4·10⁻³ (script in X-90003); no other numerics are load-bearing.**
Authoring: `claude-fable-5` session `riemann-proof-review-8nz34i`, Strike B prong B3
Date: 2026-08-09
Dependencies: T-90001 §0 objects, §1 per-modulus floor bound; O-90004 §1 Prop A (Corollary C only)
Scope: deterministic sign structure of \(s_X(q)\); no prime input except in Corollary C's prime-indexed sums; no RH claim.

## 0. Objects and statement

Notation of T-90001 §0: \(b_X, v_q, r_X(q)=v_q-q^{-1/2}\log(X/q)\), \(Y=\lfloor X/2\rfloor\), \(s_X(q)=r_X(q)-\mathbf 1_{q\le Y}r_Y(q)\), profile \(g(u)=(\log u+4)/\sqrt u-4\), \(E(\theta)\) with cell formula \(E=\theta^{-1/2}[A_N+(S_N+1)\log\theta+4S_N]-4N\) on \(1/(N{+}1)<\theta\le1/N\), \(S_N=\sum_{k\le N}k^{-1/2}\), \(A_N=\sum_{k\le N}k^{-1/2}\log k\); \(E_c(\theta)=E(\theta)-c^{-1/2}E(\theta/c)\mathbf 1_{\theta\le c}\). \(E\) is continuous on \((0,1]\) (knot jumps vanish via \(S_N=S_{N-1}+N^{-1/2}\), \(A_N=A_{N-1}+N^{-1/2}\log N\); equivalently \(g(1)=0\)). Write \(\psi(\theta)=\sqrt\theta\,E(\theta)\), \(\varphi(\theta)=\psi(\theta)-\psi(2\theta)=\sqrt\theta\,E_{1/2}(\theta)\) for \(\theta\in(0,1/2]\), and \(B(u)=2\sqrt u(\log(1/u)-2(1-\sqrt u))\) (so \(b_X(uX)=\sqrt X\,B(u)\), \(B'=-g\)).

**Theorem S.** Let \(c^*=0.140852035013839925440958\ldots\) be the unique root in \((1/8,1/7)\) of
\[\alpha_7+\beta_7\log\theta-\gamma_7\sqrt\theta=0,\qquad \alpha_7=A_7-A_3+4(S_7-S_3)-(S_3+1)\log2,\ \beta_7=S_7-S_3,\ \gamma_7=4(7-3\sqrt2)\]
(the N=7/N′=3 cell equation of O-90004). Then for every integer \(X\ge10^5\):
\[s_X(q)>0\ \text{ for all integers } 2\le q\le c^*X-52,\qquad s_X(q)<0\ \text{ for all integers } c^*X+52\le q\le Y .\]
At most 104 integers near \(c^*X\) are left undetermined (observed: at most 1 at every tested \(X\)).

**Corollary C (z-collapse).** For \(X\ge10^5\), unconditionally,
\[B_X=[T^s(2)]_+ +O^*\!\bigl(5.7\cdot10^4\,X^{-3/2}\log X\bigr),\]
so WSTS \(\iff [T^s(2)]_+=O_\varepsilon(X^\varepsilon)\): the z-max is redundant and WSTS is one scalar per \(X\). (Sharper than the \(O(X^{-1}\log^2X)\) conjectured in O-90004 §1.)

## 1. Theorem P (profile single crossing) — the analytic core

**P1 (per-cell closed form).** For \(\theta\) in cell \(N\) (\(N\ge2\)), \(2\theta\) lies in cell \(N'=\lfloor N/2\rfloor\) for the *entire* cell (even \(N=2M\): \(2\theta\in(2/(2M{+}1),1/M]\subset(1/(M{+}1),1/M]\); odd \(N=2M{+}1\): \(2\theta\in(1/(M{+}1),2/(2M{+}1)]\subset(1/(M{+}1),1/M]\)). Hence on cell \(N\),
\[\varphi(\theta)=\alpha_N+\beta_N\log\theta-\gamma_N\sqrt\theta,\quad \alpha_N=A_N-A_{N'}+4(S_N-S_{N'})-(S_{N'}+1)\log2,\ \beta_N=S_N-S_{N'}>0,\ \gamma_N=4(N-\sqrt2N')>0.\]
\(\varphi_N'(\theta)=\theta^{-1}(\beta_N-\tfrac{\gamma_N}2\sqrt\theta)\): each \(\varphi_N\) is increasing then decreasing (**unimodal**), so its infimum on the closed cell is at an endpoint, and its supremum is at an endpoint or at \(\theta_{\rm crit}=(2\beta_N/\gamma_N)^2\).

**P2 (effective Euler–Maclaurin).** Define \(\sigma_N=S_N-2\sqrt N-\zeta(\tfrac12)\), \(\rho_N=A_N-(2\sqrt N\log N-4\sqrt N)+\zeta'(\tfrac12)\). By the trapezoid rule with second-derivative remainder (\(|{\int_{k-1}^k}f-\tfrac{f(k-1)+f(k)}2|\le\tfrac1{12}\sup|f''|\)) applied to \(f=x^{-1/2}\) (convex, so the error has one sign) and \(f=x^{-1/2}\log x\) (\(|f''|\le x^{-5/2}(2+\tfrac34\log x)\)), summing tails by monotone comparison:
\[\tfrac1{2\sqrt N}-R_S(N)\le\sigma_N\le\tfrac1{2\sqrt N},\qquad \bigl|\rho_N-\tfrac{\log N}{2\sqrt N}\bigr|\le R_A(N),\]
\[R_S(N)=\tfrac1{16}N^{-5/2}+\tfrac1{24}N^{-3/2},\qquad R_A(N)=\tfrac1{12}\bigl[(2.75+0.75\log N)N^{-5/2}+(2.1667+0.5\log N)N^{-3/2}\bigr]\ (N\ge8).\]
(The constants \(\zeta(\tfrac12),\zeta'(\tfrac12)\) are *defined* here as the limits, which exist by these tail bounds; only \(a:=1+\zeta(\tfrac12)\) is ever needed numerically, and the \(\sigma\)-bracket at \(N=10^6\) certifies \(-(1+\zeta(\tfrac12))\log2\in[0.319093429839,\,0.319093429868]\).) On cell \(N\ge8\), writing \(u=N\theta\in(N/(N{+}1),1]\) and \(\tilde\varphi(u)=2\sqrt u-2-\log u\in[0,\,0.335(1-u)^2]\) (Taylor at \(u=1\); \(\tilde\varphi''\le0.669\) on \([8/9,1]\)):
\[\psi(\theta)=a\log\theta+\kappa+\tfrac2{\sqrt N}+\delta_N(\theta),\quad \kappa=4\zeta(\tfrac12)-\zeta'(\tfrac12),\]
\[|\delta_N(\theta)|\le D(N):=0.67N^{-3/2}+R_A(N)+R_S(N)(\log N+4)+0.5N^{-3/2}+R_S(N)/N,\]
by collecting \(-2\sqrt N\tilde\varphi(u)\) (\(\le0.67N^{-3/2}\)), \(\rho_N-\sigma_N\log N\), \(\sigma_N\log(N\theta)\) (\(|\log u|\le1/N\)), and \(4\sigma_N-2/\sqrt N\). Both \(a\log\theta\) and \(\kappa\) **cancel in \(\varphi\)**:
\[\varphi(\theta)=-a\log2+\tfrac2{\sqrt N}-\tfrac2{\sqrt{N'}}+O^*\!\bigl(D(N)+D(N')\bigr)\ \ge\ 0.319093-\Bigl(\tfrac2{\sqrt{N'}}-\tfrac2{\sqrt N}\Bigr)-D(N)-D(N').\]

**P3 (verified finite cells; margins from `X-90003/profile_cells.py`, 30-digit monotone envelopes).**
- Tail \(N\ge18\): \(\Xi(N)=2/\sqrt{N'}-2/\sqrt N+D(N)+D(N')\le0.319093-0.0231\) for all \(18\le N\le400\) (checked term by term), and for \(N>400\), \(\Xi(N)\le2\sqrt2/\sqrt{N-1}-2/\sqrt N+2D(200)<0.043\). Hence \(\varphi\ge0.0231\) on \((0,1/18]\).
- Cells \(8\le N\le17\): endpoint minima (P1 unimodality) give \(\varphi\ge0.0329\) on \((1/18,1/8]\).
- Cell \(7\): \(2\beta_7/\gamma_7=0.31433<\sqrt{1/8}\), so \(\varphi_7\) is **strictly decreasing** on \((1/8,1/7]\) with \(-\varphi_7'\in[1.7305,2.4566]\); \(\varphi(1/8)=+0.032917\), \(\varphi(1/7)=-0.0048568\): unique simple zero \(c^*\), and \(|\varphi(\theta)|\ge1.7305\,|\theta-c^*|\) on the cell.
- Cells \(2\le N\le6\): suprema (endpoints and \(\theta_{\rm crit}\) where interior) are \(-0.196018,-0.076261,-0.068472,-0.008790,-0.004311\): \(-\varphi\ge0.00431\) on \((1/7,1/2]\).

**P4 (uniformity in \(c=Y/X\)).** For \(\theta\le c\), \(\partial_c[\sqrt\theta E_c(\theta)]=c^{-1}[(S_{N'}+1)-2N'\sqrt{\theta/c}]\) (cell \(N'\ni\theta/c\)); the bracket lies in \((-0.4604,\,0.586+0.0396]\) by P2's \(\sigma\)-bracket and \(2\sqrt{N'}(1-\sqrt{N'/(N'{+}1)})\le0.586\), so \(|\partial_c|\le0.626/0.49\le1.28\) for \(c\in[0.49,\tfrac12]\); \(c\mapsto\sqrt\theta E_c(\theta)\) is continuous (continuity of \(E\)). Since \(\tfrac12-c\le\tfrac1{2X}\): \(\bigl|\sqrt\theta E_c(\theta)-\varphi(\theta)\bigr|\le0.65/X\). ∎(P)

## 2. Theorem Q (small q, exact two-scale identity; log-free)

For integers \(2\le q\le Y/2\), with \(K_Y=\lfloor Y/q\rfloor\), \(K_X=\lfloor X/q\rfloor\), \(L=\log(X/Y)\):
\[\boxed{\;s_X(q)=-2L\!\!\sum_{k\le K_Y}\!(\sqrt{kq+1}-\sqrt{kq})\;+\;4K_Y(Y^{-1/2}-X^{-1/2})\;+\!\!\sum_{K_Y<k\le K_X}\!\!\bigl[b_X(kq)-b_X(kq{+}1)\bigr]\;-\;\frac L{\sqrt q}\;-\;\mathbf 1_{q\mid Y}\,\beta_Y\;}\]
with \(0<\beta_Y=2\sqrt{Y{+}1}\,[\,2(\sqrt{1+1/Y}-1)-\log(1+1/Y)\,]\le0.52\,Y^{-3/2}\). *Proof.* \(v_q(b_X)-v_q(b_Y)=\sum_{k\le K_Y}[h_X-h_Y](kq)+\sum_{K_Y<k\le K_X}h_X(kq)\), \(h_Z(m)=b_Z(m)-b_Z(m{+}1)\); and for \(m+1\le Y\) the integrand identity \(Z^{-1/2}g(t/Z)\big|_{Z=X}-\big|_{Z=Y}=-L\,t^{-1/2}+4(Y^{-1/2}-X^{-1/2})\) integrates to \([h_X-h_Y](m)=-2L(\sqrt{m+1}-\sqrt m)+4(Y^{-1/2}-X^{-1/2})\). The only extension case is \(k=K_Y\), \(q\mid Y\) (then \(m{+}1=Y{+}1\)), producing exactly \(-\beta_Y\); \(\beta_Y>0\) and \(\le0.52Y^{-3/2}\) since \(0<2(\sqrt{1+h}-1)-\log(1+h)\le h^2/4\). At scale \(X\) no extension occurs (integers: \(kq\le X<kq+1\Rightarrow kq=X\), a zero term). Identity machine-verified to 1e-13, and to ratio \(1+2\cdot10^{-9}\) of \(\beta_Y\) in the \(q\mid Y\) case. ∎

**Theorem Q.** For integers \(X\ge10^5\) and \(2\le q\le X/110\): \(s_X(q)\ \ge\ 0.319093/\sqrt q-3.22/\sqrt X\ >\ 0.\)
*Proof.* Bound the identity's terms. (i) \(\sqrt{kq+1}-\sqrt{kq}\le\tfrac12(kq)^{-1/2}\), so term 1 \(\ge-(L/\sqrt q)S_{K_Y}\ge-(L/\sqrt q)[2\sqrt{K_Y}+\zeta(\tfrac12)+\tfrac1{2\sqrt{K_Y}}]\) (P2, \(\sigma\le\tfrac1{2\sqrt N}\)). (ii) \(K_Y\ge Y/q-1\). (iii) \(b_X\) is convex on \([Y,X{+}1]\) (\(b_X''(m)=m^{-3/2}(1-\tfrac12\log(X/m))>0\)), so \(h_X(m)\ge-b_X'(m{+}1)=X^{-1/2}g((m{+}1)/X)\), and \(g\) decreases on \([0.49,1.01]\), so \(\sum_{K_Y<k\le K_X}\ge(X/q)\int_{u_1}^{u_2}g=(X/q)[B(u_1)-B(u_2)]\), \(u_1\in(c,c+(q{+}1)/X]\), \(u_2\in(1,1+(q{+}1)/X]\). The \(\sqrt X/q\) growth terms carry total coefficient \(-2\sqrt c\log(1/c)+4(\sqrt c-c)+B(c)\equiv0\) **identically in \(c\)**, and \(-L(1+\zeta(\tfrac12))/\sqrt q\ge0.319093/\sqrt q\) survives (\(L\ge\log2\)). The error budget (all for \(c\ge0.4995\), \(q\le X/110\)): \(\tfrac L2(Y-q)^{-1/2}\le0.50X^{-1/2}\); \(4(Y^{-1/2}-X^{-1/2})\le1.67X^{-1/2}\); slope of \(B\) at \(u_1\): \(0.68(q{+}1)/(q\sqrt X)\le1.02X^{-1/2}\); \(B(u_2)\le1.01((q{+}1)/X)^2\) giving \(\le0.016X^{-1/2}\); \(\beta_Y\le0.005X^{-1/2}\) (at \(X\ge10^5\)). Total \(3.22X^{-1/2}\). Positivity at \(q=X/110\): \(0.319093\sqrt{110}=3.3466>3.22\). ∎
(Machine check: \(\min_{q\le X/150}[s_X(q)-\text{bound}]=+0.0056\) at \(X=2\cdot10^5\).)

## 3. Proof of Theorem S

Let \(\theta=q/X\le c\). Import (T-90001 §1, applied at scales \(X\) and \(Y\); \(X^{-1/2}c^{-1/2}=Y^{-1/2}\)):
\[\bigl|\sqrt q\,s_X(q)-\sqrt\theta E_c(\theta)\bigr|\le\zeta(\tfrac32)\,q^{-1}\bigl(2+\log(X/q)\bigr)=:\mathrm{FL},\]
and by P4, \(\sqrt\theta E_c(\theta)\ge\varphi(\theta)-0.65/X\) (resp. \(\le\varphi(\theta)+0.65/X\)). Then for \(X\ge10^5\):
- \(2\le q\le X/110\): Theorem Q gives \(s_X(q)>0\).
- \(X/110\le q\), \(\theta\le1/8\): \(\varphi\ge0.0231\) (P3), while \(\mathrm{FL}+0.65/X\le2.6124\cdot110(2+\log110)/X+0.65/X\le1926/X\le0.0193<0.0231\). Positive.
- \(1/8<\theta\le c^*-52/X\): ramp \(\varphi\ge1.7305\cdot52/X=89.9/X\), while \(\mathrm{FL}+0.65/X\le2.6124\cdot8(2+\log8)/X+0.65/X\le85.9/X\). Positive.
- \(c^*+52/X\le\theta\le1/7\): \(-\varphi\ge89.9/X>73.5/X+0.65/X\ge\mathrm{FL}+0.65/X\) (here \(q\ge c^*X\)). Negative.
- \(1/7<\theta\le c\): \(-\varphi\ge0.00431>74.1/X\). Negative. ∎

## 4. Proof of Corollary C

\(T^s(z)=T^s(2)-\sum_{p<z}(\log p)s_X(p)\). For \(z\le c^*X-52\) the removed terms are \(\ge0\) (Theorem S), so \(T^s(z)\le T^s(2)\). For \(z\ge c^*X+52\), \(T^s(z)=\sum_{p\ge z}(\log p)s_X(p)\le0\), because \(s_X(p)<0\) on \([z,Y]\) (Theorem S) and on \((Y,X)\) (O-90004 Prop A; \(s_X(X)=0\)). For \(z\) in the window, \(T^s(z)\le T^s(2)+\sum_{|p-c^*X|<52}(\log p)|s_X(p)|\); on the window \(|\varphi|\le2.4566\cdot53/X+0.65/X\) so \(|s_X(p)|\le X^{-1/2}|E_c|+\text{floor}\le(350+198)X^{-3/2}\), and the sum is \(\le104\cdot548\,X^{-3/2}\log X\le5.7\cdot10^4X^{-3/2}\log X\). Since \(B_X\ge[T^s(2)]_+\) always, C follows. ∎

## 5. Discipline notes

- **What is imported.** T-90001 §1's per-modulus floor bound (PROVED there; re-verified here, worst observed ratio 0.072 of the bound) and O-90004 Prop A (PROVED there; Corollary C only). Everything else is self-contained: P2's constants are elementary trapezoid tails; the only transcendental input is the certified bracket for \((1+\zeta(\tfrac12))\log2\), produced by P2's own \(\sigma\)-inequality at \(N=10^6\).
- **Finite-cell certification.** All P3 inequalities are finitely many evaluations of \(\alpha_N+\beta_N\log\theta-\gamma_N\sqrt\theta\) at cell endpoints/critical points, computed at 30 digits; smallest margin 0.00431. This is interval-arithmetic-grade (margins exceed evaluation error by >25 orders); a formal interval check is a mechanical upgrade.
- **The 52-window and \(X\ge10^5\)** are artifacts of the error budget, not of the phenomenon (observed window \(\le1\) integer at all tested \(X\); observed signs correct for all \(X\) tested down to \(10^4\)). For \(X<10^5\) the statement is NUMERICAL_ONLY.
- **What C changes.** WSTS is now officially the one-scalar statement \([T^s(2)]_+=O_\varepsilon(X^\varepsilon)\), equal by the Stirling bridge to minus the ramp deficit; every future producer proposal should attack that scalar directly. Margin data: \(-T^s(2)\approx0.17\log X+0.4\) (O-90004).
- **Numerics locations.** `experiments/X-90003-z-collapse-verification/`: `profile_cells.py` (P1–P4 checks incl. \(\Xi\)-scan and Lipschitz), `discrete_check.py` (exact \(s_X\) for \(X\in\{10^5{+}1,\,2\cdot10^5{-}1,\,2\cdot10^5\}\): one sign flip each, at \(\lfloor c^*X\rfloor\); identity to 1e-13; floor-ratio and Theorem-Q slack checks).
