# Independent adversarial check of the effective cluster bound

I checked the proposed bound (A), its fixed-window and quadrature estimates, and its stated input requirements against rStation 48 v2 §§4–8 and the fixed-Laurent localization repair. The quantitative conclusion survives these checks, conditional on the listed certified inputs and the director's decision. No numerical constants for zeta, new zero certificates, or two-sided rate are produced by this review. [Proposed proof](effective_cluster62_proof.md) [Claim records](../../theorems/effective_cluster62_claims.jsonl) [rStation 48 v2](../../sources/witness62_rst048/v2.md)

## Scaled finite-window asymptotics

For \(p(u)=u^{j-1}w(u)/(j-1)!\), its first nonvanishing left jet is \(p^{(j-1)}(0)=1\), and its right jets through order \(j-1\) vanish. The internal joins needed for repeated-node orders have matching jets. Hence integration by parts yields
\[
 1-(iv)^j\int_0^1p(u)e^{-ivu}\,du
       =-\int_0^1p^{(j)}(u)e^{-ivu}\,du .
\]
The piecewise derivative is of bounded variation, including its possible jumps. Its \(L^1\) norm controls \(|e_{j,w}|\) while the endpoint magnitudes and variation control \(|v e_{j,w}|\). The proposed \(M_{j,w}\) is a safe majorant of their sum. The off-window Laurent estimate follows after division by \(|t-\gamma|^j\) and one further factor from \(1+L|t-\gamma|\ge L|t-\gamma|\).

For the top coefficient, change variables \(v=L(t-\gamma)\). The variation of the smooth weight is bounded by \(D_\rho |v|/L\) on \(|v|\le Lr_\rho\), and
\[
 \int_0^X\frac{v}{(1+v)^2}\,dv
       =\log(1+X)+\frac1{1+X}-1\le\log(1+X).
\]
The omitted symmetric Fourier tail contributes at most \(2M_{m,w}^2/(1+Lr_\rho)\). Division by \(2\pi\) gives the exact \(M_{m,w}^2/\pi\) factor in (C). Plancherel at the constant weight gives \(m^2/|\rho|^2\). For lower Laurent orders \(j<m\), the factor \(|t-\gamma|^{m-j}\) made by the zero cancels the singular bound \(1/(L|t-\gamma|)\), including by continuity at the zero. All other fixed terms are \(O_Y(1/L)\) on the selected window since their distances are positive. The cross integrals against the top profiles are controlled by the \(L^1\) bound \(2M_{m,w}\log(1+Lr_\rho)/L\). Outside the selected windows the entire fixed sum has norm \(O_Y(1/L)\) by (B). This verifies the absolute \(O_Y((1+\log L)/L)\) error for the scaled squared norm of the fixed sum.

## Why the tail contributes its squared bound

For \(Y<|\tau_C|\le H\), the source subset estimate (41) gives \(\|T_{Y,H}\|_*^2\le B Y^{-99/100}/L\). The constant is uniform in \(Y,N\) once the fixed contour/growth constants and finite exceptions have been included. The fixed minimum separation of centers bounds the sum of \(T_C^{-2+1/100}\) by an integral plus an endpoint term. Even the mesh constant can be fixed independently of \(Y\).

On each \(J_\rho\), the finite nearby exterior cells have ordinate hulls disjoint from the window at a certified positive distance. In fact the window lies strictly inside its own grid cell while the other cells stay on the other side of at least one of its two edges. Their terms can be bounded by the Newton contour coefficients and (26), using this distance and finite multiplicity bounds. There is no need to resolve their individual roots. For the other cells, (38) gives an absolutely summable bound there of size \(1/L\): after splitting at \(2(1+|\gamma|+r_\rho)\), the far majorant behaves like \(T_C^{-2+\beta}\) with \(\beta<1\). The local zeta bound is uniform on the fixed window. This proves \(\sup_{J_\rho}|T_{Y,H}|\le A''_\rho/L\) uniformly in \(H,N\) at fixed \(Y\).

It follows that the scaled fixed/tail cross integral over all selected windows is \(O_Y((1+\log L)/L)\) from the profile \(L^1\) bounds. Off them, Cauchy–Schwarz gives
\[
 L\left|\int_{\rm exterior}2\Re(P_Y\overline{T_{Y,H}})\,
                  \frac{dt}{2\pi(1/4+t^2)}\right|
   \le 2A'_Y\sqrt{B}\,Y^{-99/200} L^{-1/2}.
\]
Thus the only nondecaying tail term at fixed \(Y\) is its own scaled squared cost \(B Y^{-99/100}\). A direct triangle bound before using the spatial localization would add a larger fixed cross term and does not justify (A). The proof makes the needed distinction.

## Euler bounds and outer arithmetic errors

In the differentiated cumulative Euler identity, the derivative of the fractional-part endpoint contributes at most \((\log X)^h/X\) on \(\Re z=0\). The contribution from \((1+z)\) times the differentiated integral costs at most
\[
 (1+|z|)X^{-1}(1+\log X)^h
                   \sum_{k=0}^h\binom hk k!,
\]
by \(y=Xe^v\). The derivative falling on \(1+z\) gives the stated \(h\)-multiple of the corresponding sum of degree \(h-1\), with an empty sum at \(h=0\). This verifies the displayed \(E_h\). The first piece has \(p\ge1\) because \(q(0)=0\), so each \(h=m-1+p\ge1\); the derivative of the cumulative discrepancy at \(X=1\) is zero. For each later piece, subtracting the cumulative values at its two endpoints cancels the regular-zeta term for that piece even if its coefficients differ from those of adjoining pieces. Continuity of \(q\) resolves integer breakpoints. The factor \(L^{-p}(1+\log X)^h\le 2^h L^{m-1}\) holds for \(1\le X\le N\), \(L\ge1\). The two endpoints of each piece give the factor two in \(M_q\).

For the inner ordinate range, the rational norm weight cancels \((1+|s-\rho|)^2\) up to a known fixed \(\gamma\)-constant, and \(\int_{|t|\le N^{a/2}}(1+|t|)^{2e}dt\) costs \(N^{a(1+2e)/2}\). This verifies the squared remainder \(O(L^{2m-2}N^{-a(3/2-e)})\). On the outer range the entire difference of the sum and integral is bounded by \(O((1+L)^m)\), yielding \(O(L^{2m}N^{-a(1/2-e)})\) after the weighted growth integral. Taking square roots gives the exact powers used in the proof. The regular-zeta contribution on the inner range is bounded by its integrable full-line logarithmic majorant, so no regular term is counted twice. The fixed anchor uses the convergent \(n^{-3/2}(\log n)^m\) series and the Lipschitz bound on \(q\).

The source exponents for high-strip/growing quadrature errors and the growing anchor independently check as \(-0.049978\), \(-0.1499595\), \(-0.049958\), and \(-0.07499475\). The slowest among the required squared estimates is \(-0.049958\), so the unscaled norm exponent is exactly \(-0.024979\). Multiplication by \(\sqrt L\) then gives the proposed last term of (A). At the baseline anchor, the retained-left Perron line estimate is valid at \(s=1\); the pole at \(w=0\) is simple for the full integrand because \(F(1)=0\), though the kernel has a double pole. Its residue is \(F'(1)/L=1/L\).

## Quantifiers, computability and suggested edits

The proof gives all sufficiently large integer \(N\) with \(N\ge Y^{20}\) for fixed selected \(Y\). The formulation for all integers \(N\ge Y^{20}\) is supported if the stated certified inputs furnish all-height contour/exception envelopes, with low cases absorbed into fixed constants. If only eventual estimates are supplied, state an additional certified starting height or absorb the finite initial cutoff range explicitly. Neither formulation permits \(Y\) to move with \(N\) without controlling \(K_Y,Q_Y\).

The one-sided tolerance algorithm is relative to the stated certified inputs. With numerical global constants \(B,U\), one can choose a fixed \(Y\) then request its exact multiplicity/isolation data, and use an upper bound for \(C_\zeta\) in the squared cross terms of (A). This does not give an unconditional procedure for finding the missing input certificates from RH alone. The finite selected cells and outside tail are located by center modulus, so when using a unit-window zero count for \(C_\zeta-S_Y\), start at \(Y-2D/3\) or use a coarser safe smaller threshold. The reported \(BY^{-99/100}\) uses center counting and needs no such change. The monotone-distance abstraction correctly shows that qualitative convergence cannot yield a universal effective rate. Burnol's liminf alone cannot certify an explicit lower tolerance at a specified \(N\).

Change the Perron phrase “double pole at zero” to “simple pole at zero after cancellation,” and fix the malformed \(O(L^{-1})\) notation in the Euler paragraph. Explicitly say integer \(N\) and retain candidate status until adjudication. I found no counterexample to (A) under its stated geometry and certified envelopes. The main vulnerabilities are dropping the positive cell-edge distance, mistaking fixed-\(Y\) constants for uniform ones, or claiming computability of exact multiplicities without the supplied certificates.
