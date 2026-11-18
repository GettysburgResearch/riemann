# Zeta moments, critical zeros, and automorphic central values, 1984–2014

The [source records](classical63_lfunctions_records.jsonl) add 25 works to the Observatory's historical bibliography through the moment conjectures, mollified zero counts, and automorphic averages around the turn of the century. The sources cover continuous zeta moments, discrete moments at zeros, random-matrix determinants, and families of primitive Dirichlet characters and cusp forms. Their averaging measures and hypotheses determine how the results can be compared.

## Complete reading of Conrey–Ghosh–Gonek's 1984 gap note

Read the published paper on pp. 421–424, including its November 1983 addition in proof. For consecutive ordinates $\gamma\le\gamma'$ of zeta zeros, let $\lambda$ and $\mu$ denote the limit superior and inferior of $(\gamma'-\gamma)\log\gamma/(2\pi)$ as $\gamma\to\infty$. The theorem on p. 421 assumes RH and gives the strict inequalities $\lambda>2.337$ and $\mu<0.5172$. The proof takes a Dirichlet polynomial of length $K=T^{1-\delta}$ for fixed sufficiently small $\delta>0$. Its mean square on $[T,2T]$ is $M_1$. Its mean square at translates of each ordinate in $(T,2T]$, integrated over shifts from $-\pi c/\log T$ to $\pi c/\log T$, is $M_2(c)$. The criterion follows by comparing the area covered by the translated intervals with the integral over $[T,2T]$. Page 423 evaluates $M_2(c)/M_1=h(c)+O(1/\log T)$ using a logarithmic-derivative contour for the discrete mean. [Original scan, pp. 421–424](../sources/classical63_lfunctions/gonek1984gaps.pdf)

Page 422 takes $a_k=d_r(k)k^{-1/2}$ for large gaps and $a_k=(-1)^{\Omega(k)}d_r(k)k^{-1/2}$ for small gaps. Here $d_r(p^m)=\Gamma(m+r)/(\Gamma(r)m!)$ and $\Omega$ counts prime factors with multiplicity. The prime number theorem and the partial sum of $d_r(k)^2/k$ give
$$
h_\pm(c)=c\pm2r\int_0^1
\frac{\sin(\pi c\theta(1-\delta))}{\pi\theta}(1-\theta)^{r^2}\,d\theta
+O(1/\log T),
$$
with the minus sign for large gaps. At $\delta=10^{-5}$, Simpson quadrature gives approximately $0.99966039$ for $(c,r)=(2.337,2.2)$ with the minus sign and $1.00011862$ for $(c,r)=(0.5172,1.1)$ with the plus sign. These numerical checks reproduce the directions of the paper's inequalities. The proof uses the cited Montgomery–Odlyzko criterion and also gives its own shorter contour explanation. [Original scan, pp. 421–423](../sources/classical63_lfunctions/gonek1984gaps.pdf)

The printed addition in proof lowers the method's coefficient-independent cutoff from $6.2$ to $3.74$ and announces $\lambda>2.68$ from a more complicated argument. The two on-page estimates with the explicit weights remain $2.337$ and $0.5172$. The proof addition contains the improved constants and no derivation of the announced $2.68$ bound. [Original scan, p. 424](../sources/classical63_lfunctions/gonek1984gaps.pdf#page=4)

## Complete reading of Conrey–Ghosh's 1998 sixth-moment note

Read pp. 1–5 of the authors' arXiv v1, corresponding to the article published in IMRN 1998(15), 775–780. Write
$$
a_3=\prod_p(1-p^{-1})^4(1+4p^{-1}+p^{-2}),\qquad
D_N(s)=\sum_{n\le N}d(n)n^{-s}.
$$
The first short-polynomial theorem on arXiv p. 3 is a special case of Theorem 2 of the authors' earlier work. With weight polynomial $P=1$, $N=T^\theta$ and a fixed $0<\theta<1/2$, it gives
$$
\int_1^T |\zeta(1/2+it)|^2\zeta(1/2+it)^2D_N(1/2-it)\,dt
\sim \frac{\theta^6a_3}{720}
\left(\frac16-\frac{\theta}{7}+\frac{\theta^2}{56}\right)T\log^9T .
$$
There is no RH hypothesis on the stated short-polynomial formula. The factor in parentheses results from integrating $\alpha^5(1-\alpha\theta+(\alpha\theta)^2/7)$ on $[0,1]$. The analogous theorem on p. 4 concerns $\int_1^T |\zeta(1/2+it)|^2|D_N(1/2+it)|^2\,dt$ for the same strict length range. For $P=1$, its integral uses $h(\alpha)=(1-\alpha)^3/3$. The article cites its earlier theorems for both short-polynomial formulas. [Author's v1, pp. 2–4](../sources/classical63_lfunctions/cg1998.pdf)

The sixth-moment statement itself is conjectural:
$$
\int_1^T|\zeta(1/2+it)|^6\,dt
\sim \frac{42a_3}{9!}T\log^9T .
$$
The first sketch splits an approximate functional equation for $\zeta(s)^2$ and uses functional-equation symmetry to combine two integrals. For the leading term, it extrapolates the short-polynomial formula to $\theta=1$ and leaves the contribution of the approximate-functional-equation error outside the calculation. The algebra gives $2a_3/(720\cdot24)=42a_3/9!$. The second sketch gives the same coefficient from predicted diagonal and mixed terms, $28a_3/9!$ and $14a_3/9!$, with another length extrapolation and oscillatory cancellation. Its final remarks point to an additive-divisor approach for long Dirichlet polynomials, developed in Conrey–Gonek 2001. The arXiv record lists only v1. The journal record confirms the separate printed manifestation. [Author's v1](https://arxiv.org/abs/math/9807187v1) · [Original journal listing](https://doi.org/10.1155/S1073792898000476)

## Corrections and changes of hypotheses

- Conrey–Ghosh–Gonek 1998, p. 498, states that an earlier version omitted GLH and that the referee identified the omission. Theorem 1 in print assumes RH and the generalized Lindelöf hypothesis, giving $C_s\ge19/27$ and $C_d\ge5/6+1/81$. The argument uses a sixth-moment bound for Dirichlet $L$-functions implied by GLH, and the same correction applies to the authors' cited companion paper [5]. Bui–Heath-Brown 2013, p. 1 and §3, obtains the simple-zero bound $19/27$ under RH using Heath-Brown's generalized Vaughan identity. Its distinct-zero corollary gives $0.84665$ under RH. The 2013 result improves the hypothesis with a different proof. [1998 journal scan](../sources/classical63_lfunctions/cgg1998.pdf#page=2) · [2013 author version](../sources/classical63_lfunctions/buihb2013.pdf)
- The earlier Milinovich–Ng draft places Theorem 1 under RH. The revised author manuscript and the 2014 journal abstract require GRH for Dirichlet $L$-functions. The revised Theorem 1.1 gives $N(T)^{-1}\sum_{0<\gamma\le T}|\zeta'(\rho)|^{2k}\gg_k(\log T)^{k(k+2)}$ for fixed positive integers $k$ and sufficiently large $T$. The cited main result uses the revised hypotheses. [2007 author draft](../sources/classical63_lfunctions/mn2014.pdf) · [Revised manuscript](../sources/classical63_lfunctions/mn2014final.pdf) · [2014 journal](https://doi.org/10.1093/imrn/rnt028)
- Bui–Conrey–Young's arXiv v2 reports minor corrections and adds a discussion of Feng's mollifier length. A comparison of §2.1 shows that v2 adds $Q(x)+Q(1-x)=\mathrm{constant}$ to the earlier requirement $Q(0)=1$. The published paper retains the symmetry condition. Both arXiv versions give the $0.4105$ and $0.4058$ lower bounds. The final journal introduction goes further in its description of how an admissible-length variant of Feng's mollifier might be combined with the authors' approach. [v1](../sources/classical63_lfunctions/bcy2011v1.pdf) · [v2](../sources/classical63_lfunctions/bcy2011.pdf) · [Journal text](../sources/classical63_lfunctions/bcy2011print.pdf)

## Scope of the related results

| Original source | Primary-text passage and use |
|---|---|
| Gonek 1984 | The theorem on pp. 123–124 evaluates a discrete mixed derivative sum with reflected arguments. Corollary 1 uses RH to turn it into a critical-line mean value at shifted zero ordinates. |
| Conrey–Ghosh–Goldston–Gonek–Heath-Brown 1985 | The theorem on p. 43 assumes RH and gives positive lower limiting distribution at thresholds $\alpha>0.77$ and upper limiting distribution below one at $\alpha<1.33$. The five-author QJM article studies positive proportions of gaps. |
| Gonek 1989 | The publisher identifies the 18-page original on negative moments. The catalogue establishes its bibliographic identity and the full scan was unavailable in this pass. |
| Soundararajan 2000 | Theorem 1 on p. 448 proves at least $7/8$ nonvanishing at $1/2$ in the family $\chi_{8d}$ for positive odd square-free $d$. Its mollified moment controls nonvanishing at one point in each family member. |
| Hughes–Keating–O'Connell 2000 | Theorem 1.2, p. 2613, proves the CUE eigenangle derivative moment for bounded $k$ with $\Re k>-3/2$. Conjecture 1.3 proposes a zeta derivative moment at zeros, with Barnes factor $G(k+2)^2/G(2k+3)$ and a prime factor. |
| Iwaniec–Luo–Sarnak 2000 | The introduction and Theorems 1.1–1.5 specify the families, analytic conductor and Fourier support. Theorem 1.1 has support $(-2,2)$ for the square-free level limit and includes sign-separated orthogonal densities. Page 56 assumes RH for the family and all Dirichlet $L$-functions unless otherwise stated. Appendix C treats Hypothesis S separately. |
| Conrey–Iwaniec 2000 | Theorem 1.1 bounds the cubic sum of $L_f(1/2,\chi)$ over primitive forms of weight $k\ge12$ and level dividing the odd square-free conductor $q$, with even $k$ and matched parity. Waldspurger positivity gives Corollary 1.2's $q^{1/3+\varepsilon}$ individual bound. |
| Iwaniec–Sarnak 2000 | The journal entry identifies the original nonvanishing and Landau–Siegel-zero paper. The Iwaniec–Luo–Sarnak introduction describes its unconditional central-value setting. This pass did not obtain the full 2000 Israel Journal article. |
| Conrey–Gonek 2001 | Introduction and Conjecture 1 give long Dirichlet-polynomial evidence for the sixth moment and predict the eighth-moment coefficient with factor $24024/16!$. The additive-divisor hypotheses belong to the evidence for the conjecture. |
| Conrey–Iwaniec 2002 | Theorems 1.1–1.2 in the author manuscript turn a sufficiently frequent small-gap condition for on-line zeros into an effective lower bound for $L(1,\chi)$. The comparison permits off-line zeros and the required gap frequency is an explicit hypothesis. |
| Kowalski–Michel–VanderKam 2002 | Theorem 1.1 in the author manuscript obtains a $q^{1/2-1/80+\varepsilon}$ level-aspect bound for derivatives on the critical line, with a fixed primitive $g$ and specified level and spectral conditions. The Rankin–Selberg structure gives a moment method for a varying cusp form. |
| Watson, 2002 dissertation, 2008 revision | Abstract and Theorem 3 link squared triple integrals of automorphic eigenforms to central Rankin triple-product values normalized by adjoint factors and local terms. The abstract explains why a quantitative Lindelöf estimate for the associated family gives an equidistribution consequence. |
| Hughes 2003 | Theorems 3–4 prove a shifted characteristic-polynomial moment at CUE eigenangles. Section 3 transfers the formula to a zeta conjecture at an offset from zero ordinates. |
| Conrey–Farmer–Keating–Rubinstein–Snaith 2005 | Published §1.5 and §2.5 give the moments recipe and conjectural moment polynomials, retaining lower-order terms and the arithmetic Euler product. The recipe uses the shifted factors in both halves of approximate functional equations. |
| Conrey–Rubinstein–Snaith 2006 | Theorems 1–3 prove random-matrix derivative moment results. Conjecture 1 identifies the predicted zeta derivative analogue. The author archive titles the preprint differently from the final CMP article. |
| Gonek–Hughes–Keating 2007 | Theorem 1 gives the unconditional smoothed Euler–Hadamard product approximation. The Splitting Conjecture treats the average of the product via its factors and supplies the heuristic bridge to the Keating–Snaith moment. |
| Young 2011 | Theorem 1.1 in the published Annals article averages fourth powers at $1/2$ over primitive characters of prime modulus $q\ne2$. It yields a polynomial of degree four in $\log q$ and an error $O(q^{-5/512+\varepsilon})$. |
| Bui–Conrey–Young 2011 | Theorem 1.1 and §2.2 obtain $\kappa\ge0.4105$ and the simple critical-line proportion $\kappa^*\ge0.4058$ unconditionally from a two-piece mollifier. |
| Conrey–Iwaniec–Soundararajan 2012 | Corollary 1 and Theorem 1 evaluate a sixth moment over even primitive Dirichlet characters with an additional height integral and averaging over conductors. This gives a proved result for the specified completed family. |
| Conrey–Iwaniec–Soundararajan 2013 | Theorem 1 in the author's v1 gives $14/25$ simple critical-line zeros in the weighted primitive-character count with $(\log Q)^6\le T\le(\log Q)^A$, $A\ge6$ fixed and $Q$ sufficiently large. Its weights are $\Psi(q/Q)/\varphi(q)$ for smooth compactly supported nonnegative $\Psi$. |

Keating–Snaith's 2000 zeta-moment paper, Rudnick–Sarnak's 1996 correlation paper, Conrey's 1989 critical-line paper and Harper's 2013 conditional moment paper already have Observatory records. The mathematical statements above use historical sources and their own normalizations. The journal year and preserved manifestation date are separately identified where they differ. A primary-text passage counts as a partial reading, and the two complete readings specify the scope of their proof checks. [Prior records](../corpus/bibliography.jsonl)
