# rStation 48 v2 convergence and growing-degree audit

Independent targeted checks of §§2–6, equations (17)–(49), in *Adaptive zero clusters and optimal Nyman–Beurling approximation rates* by bramble_trace. I also checked the relevant use of (26) in §7.2 against the other reviewers' proposed repair. The inspected v2 manuscript has SHA-256 57a65d19bc9914db42dfc2869850cc02e959b87699099abeb40525085600681b. I found no further obstruction in these passages when the reciprocal bounds, zero alignment, and count are used as stated under RH. This is a scoped check, with the main theorem's status reserved for director adjudication. [Primary v2 manuscript](../../sources/witness62_rst048/v2.md) [Paper record](../../papers/PAPER-RST048.md)

## Normal convergence of the grouped expansion

Write \(F=1/\zeta\) and let \(R_C\) contain the full principal parts in the fixed-grid rectangle \(\Gamma_C\). Under RH the poles inside the critical strip all lie on its center line. Each contour has length \(O(D)\), \(F\) is bounded there by \(O(T_C^e)\), and centers are uniformly separated at a scale depending on fixed \(D\). For fixed compact \(K\) and remote cluster \(\Gamma_C\), \(|s-z|\asymp_K T_C\) uniformly for \(s\in K\). This gives
\[
 R_C'(s)=O_K(DT_C^{-2+e}),\qquad
 JR_C(s)=O_K(DT_C^{-3+e}).
\]
For the second bound, the regularization \(Jf(s)=f(s)-f(0)-s(f(0)-f(-1))\) changes the Cauchy kernel \(1/(s-z)\) into the exact expression \(s(s+1)/[z(z+1)(s-z)]\). Both bounds sum absolutely on \(K\) because \(e<1\). The individual sums of \(R_C(0)\) and \(R_C(-1)\) need no absolute estimate. Their differences do sum absolutely, by integrating the uniform bound on \(R_C'\) over \([-1,0]\). Accordingly one may split off the constant after differentiating the regularly convergent expansion.

In (17), first take the height to infinity along the good heights at fixed odd negative and fixed positive edges. The reciprocal bound on a fixed strip gives horizontal contribution \(O_{A,B,s}(T^{-3+e})\). The left and right limits follow only after that. On the right, \(|F(A+it)|\) is bounded uniformly for \(A\ge2\), and the cubic kernel gives \(O_s(A^{-2})\). On the left, \(B\) is a positive odd integer, and the functional equation yields the factors in (19). Explicitly, \(|\sin(\pi(-B+it)/2)|=\cosh(\pi t/2)\), while \(|\Gamma(1-it)|^2=\pi|t|/\sinh(\pi|t|)\). Their product is comparable to \(\sqrt{1+|t|}\). The gamma recurrence contributes \(\prod_{j=1}^B\sqrt{j^2+t^2}\), and \(\zeta(1+B-it)\) is uniformly bounded away from zero by absolute convergence of its reciprocal. These constants are uniform in \(B\). Thus the absolute integral on the negative edge is bounded by
\[
 \frac{C_s(2\pi)^{B+1}}{B!}
 \int_{\mathbb R}(B^2+t^2)^{-3/2}\,dt
 =O_s\!\left(\frac{(2\pi)^{B+1}}{B!B^2}\right).
\]
The bound uses \(|z|,|z+1|,|z-s|\gg_s\sqrt{B^2+t^2}\) for large \(B\). The factorial decay of trivial residues follows from the factor \(2(-1)^n(2\pi)^{2n}/((2n)!\zeta(2n+1))\) at \(-2n\). The residues at \(0,-1\) interpolate \(F(0)=-2\), \(F(-1)=-12\), producing \(10s-2\). The resulting formula extends meromorphically through \(0,-1\), away from the actual poles.

After differentiation the remaining constant is determined at real \(x\to+\infty\). Indeed \(|x-z|\gg x+T_C\) for \(x\ge2\) on every cluster contour, and separation gives
\[
 \sum_C\frac{D T_C^e}{(x+T_C)^2}
 \ll_D \int_1^\infty \frac{u^e}{(x+u)^2}\,du
 =O_{D,e}(x^{-1+e}).
\]
The trivial-pole derivative sum tends to zero by its summable residue bound, and \(F'(x)\to0\) by its absolutely convergent Möbius Dirichlet series on the right. This gives (21) with normal convergence off poles. The hypothesis of an all-height reciprocal bound on a negative strip does not enter. Only the specific odd-left-edge estimate is used for the second limit. [Equations (16)–(21)](../../sources/witness62_rst048/v2.md)

**Failure control.** Adding the entire term \(e^{-s}\) to a reciprocal model preserves its principal parts, fixed-strip subpower estimates and \(F'(x)\to0\) on the positive real ray, but changes the derivative in (21). The far-left edge estimate rules out precisely this kind of concealed entire term. When no such far-left estimate is known, a retained-left-edge identity with a separately bounded remainder is needed. The rStation reconstruction already verifies that variant for this application. [Retained-edge reconstruction](rstation48_adaptive_upper_rt62_rstation48.md)

## Growing profiles and multiple poles

The input \(|Q_k|_{\rm coef}\le3^{2k-2}\) follows from the binomial bound \(\sum_h\binom{2k-2}{h}2^{2k-2-h}\). Composing with \(v=(u-b)/(1-b)\) multiplies coefficient norms of monomials by at most \(A^{2k-2}\), \(A=(1+b)/(1-b)\). The factor \(1-u\) costs at most two. For a monomial \(p_\ell u^\ell\), the coefficient in \(u^{j-1}w_k^{(j)}(u)/(j-1)!\) has modulus \(|p_\ell|j\binom{\ell}{j}\). Since \(\ell\le2k-1\), this is bounded by \(|p_\ell|j2^{2k-1}\). Summing over \(\ell\), then using \(\sum_j\binom mj j=m2^{m-1}\) with \(m\le k\), gives exactly the required exponential base \(72A^2=200\) for \(b=1/4\). Bounding variation on the pieces by coefficient norms and charging their possible jump gives the stated allowance \(4k\). Thus no factorial is concealed in (27)–(28).

The beta polynomial satisfies \(Q_k(v)-1=O(v^k)\) at the left join and \(Q_k(v)=O((1-v)^{k-1})\) at the right. The extra factor \(1-u\) makes \(w_k\) vanish to order \(k\) at \(1\). A \(C^{k-1}\) taper at these joins suffices for \(m\le k\) derivatives without new delta terms. Near zero the extension \(1-u\) permits the usual distributional product rule. For each selected subset of \(j\) poles, the other \(D_x-i\theta\) factors cancel the corresponding convolution resolvents, leaving the \(j\)-fold sub-convolution. Its exact simplex normalization is \(x^{j-1}/(j-1)!\), so repeated labels cause no problem and supply the coefficient cancellation above. All phases have modulus one because all roots are aligned. The expectation in (31) reproduces Plancherel and the bounded-variation far estimate even at total collision.

In (35), the \(k!\) from Cauchy is canceled by the volume \(1/k!\) of the \(k\)-simplex in the divided difference. For \(t\in W_C\), the convex hull of the nodes and \(s\) stays on \(\Re z=1/2\). Circles of fixed radius \(D\) over that hull see zeta growth \(O_{D,e}(T_C^{D+e})\); the disk is away from the zeta pole. The removed product costs at most \((6D)^{k-m}\); combined with \((2D)^m D^{-k}\) this leaves at most \(6^k\). The only degree growth is thus exponential, and \(k_C\le D\log T_C\) converts it into the small exponents (37) and (40). A unit-interval estimate \(O(\log T_C)\) without the small fixed-window coefficient cannot be substituted here just by reducing \(D\). [Equations (22)–(41)](../../sources/witness62_rst048/v2.md)

## Pointwise identity and weighted convergence

For fixed \(N\) and \(\Re s\in(0,1)\) away from poles, the original Perron integral (42) is absolutely convergent. Its remote grouped terms after the shift are \(O_{N,s}(D T_C^{-2+e})\), as are the corresponding \(R_C'\). This yields pointwise absolute scalar convergence in (45) away from poles. For (44), directly integrate the first-order taper against \(e^{(z-s)x}\). The resulting kernel is
\[
 \frac{e^{L(z-s)}-1-L(z-s)}{L(z-s)^2}.
\]
It is entire at \(z=s\). Evaluating the finite cluster integral for \(s\) outside the contour and splitting its three terms gives \(R_C+(R_C'+B_C)/L\). Continuation and the residue at \(z=s\) then give the combined indicator and integral in (46). No separation of individual zeros is used.

The \(L^2\) argument does not follow from pointwise absolute convergence. For each fixed \(N\), retain the original rectangles including empties, telescope the finite contiguous exterior union, and then let the remote edges tend to infinity. At a fixed outer height the two vertical tails converge in weighted \(L^2\) by the squared convolution bound (47). The discarded horizontal edges vanish in weighted \(L^2\) by applying (48) at their own growing heights, and the indicator tail tends to zero in the same norm. Thus the pointwise sum equals the \(L^2\) limit of synchronized grid-height partial sums. For increasing \(N\), (49) at \(H=N^{1/20}\) supplies the needed small norm of the *unmodified* part. For the modified part, (41) instead proves an unconditional Hilbert-space sum over subsets by finite local overlap and square-summable far bounds. These are distinct estimates. A proof should avoid interchanging the order of contour tiling and absolute values, or asserting the absolute sum of the individual cluster \(L^2\) norms.

**Failure control.** Consider the model \(Z(s)=\sinh(\pi(s-1/2))/\pi\), \(F=1/Z\). Its poles are \(\rho_n=1/2+in\), \(n\in\mathbb Z\), with residues \((-1)^n\). Both \(Z\) and \(F\) have the required boundedness on the critical line or good fixed-strip edges, respectively; the same fixed-\(s\) scalar tail is absolutely convergent. For a fixed \(L>0\), its single-pole first-order defect at \(s=1/2+it\) is
\[
 E_n(s)=Z(s)\frac{(-1)^n(1-e^{-L(s-\rho_n)})}{L(s-\rho_n)^2}.
\]
On \(t=n+v\) with \(v\) in a sufficiently small fixed positive subinterval, \(|E_n|\) is bounded below independently of \(n\), since \(|\sin(\pi v)|\asymp |v|\) and \(|1-e^{-iLv}|\asymp_L |v|\). With weight \((1/4+t^2)^{-1}\), it follows that \(\|E_n\|_*\gg_L (1+|n|)^{-1}\). Thus \(\sum_n\|E_n\|_*=\infty\). This illustrates why absolute convergence of the individual norms is unavailable by the general estimates and unnecessary for the source's telescoped limit. It is a model test, not an assertion of divergence for zeta. [Equations (42)–(50)](../../sources/witness62_rst048/v2.md)

## Transfer limits and disposition

The proof segment requires a weighted norm comparable to \(dt/(1+t^2)\), subpower boundary growth, zero alignment on a fixed line, reciprocal bounds on both fixed vertical sides and selected horizontal edges, and a local count coefficient small enough relative to the fixed taper constants. It also needs either absolute factorial control of the true left and trivial poles or a retained left edge with a negligible contribution. A functional equation with different gamma factors may change the trivial-pole orders and the left-edge proof. A fixed-degree completed \(L\)-function with a proven analog of the small-window count might permit a smaller \(D\) depending on that degree. No uniform-conductor estimate follows from these fixed-parameter arguments. Off-line poles change the unit-modulus factors in (31), which is why a naive replacement of RH by a density statement does not suffice.

The known §7.2 localization issue remains real as a matter of using (26): being outside every small individual zero-neighborhood does not imply positive distance from the full hull of a cluster. For a fixed finite set of poles, regrouping into individual Laurent terms makes the required distance exactly the distance from each corresponding ordinate. This repair keeps constants dependent on the fixed set and is compatible with the order of limits. No claim about §§8.1 or 9, historical priority, quantitative uniformity, or unconditional approximation follows from this audit. [Independent localization repair](threshold62_rstation48_main_theorem_skeptic.md)
