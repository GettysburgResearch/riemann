# Independent check and repair of BGSTB arXiv v1 §6

The unit-window estimate cited in (6.4) does not imply the claimed unit-size bound on the microscopic vertical sum. The needed conclusion \(S(T)=o(T\log T)\) nevertheless follows under the paper's uniform strong-density premise and its stated Bourgain input by retaining the horizontal term of the kernel denominator. This repairs the route to the two simple-zero results in §§6–7 of arXiv v1. Journal treatment of §6 remains unverified. [Primary PDF](../../sources/analytic/2306.04799.pdf) [Journal DOI](https://doi.org/10.4064/aa230612-20-3)

## Source and exact local defect

The staged primary PDF is arXiv:2306.04799v1, SHA-256 133071c4d85c875fe9b1a7d4001f22d7174270ab8f1fa8e6cee6178d20276ee9. I checked the hypotheses on p. 2, (2.5), Lemmas 6–7, §6 on pp. 9–10, and the use of (6.3) in §7. Theorem 2 assumes all zeros with \(T^{3/8}<\gamma\le T\) lie in the strict box \(|\beta-1/2|<1/(2\log T)\). Theorem 3 assumes \(N(\sigma,T)=o(T^{2(1-\sigma)})\) on \([1/2+1/(2\log T),25/32+\eta]\) for fixed positive \(\eta\), with an inclusive real-part count and multiplicities. The argument uses little-o uniform in \(\sigma\) over that interval. Equation (6.5) supplies an upper-range extension. [Primary PDF](../../sources/analytic/2306.04799.pdf)

Set \(L=\log T\). Equation (6.4) asserts \(\sum_{0<\gamma'\le T}(1+L^2(\gamma-\gamma')^2)^{-1}\ll1\) by bounding it by a smooth-density integral using (2.5). The cited unit count yields \(O(L)\), by bounding the shell of radius \(1\) by \(O(L)\) and each two-sided shell \(j\le|\gamma-\gamma'|<j+1\), \(j\ge1\), by \(O(L/(jL)^2)\). An ordinate sequence satisfying even the full Riemann–von Mangoldt formula with \(O(\log t)\) error can attain order \(L\). Take the inverse images of successive integers under its smooth main term at large heights. In an infinite sequence of disjoint unit intervals, move the ordinates inside each interval to distinct points of a subinterval of length \(1/\log t\). At any height the count changes by only \(O(\log t)\). Each modified interval still has order \(\log t\) points, and at an ordinate of its cluster the claimed microscopic sum is of order \(\log t\) if \(T\) is at the upper endpoint of the unit interval. The example addresses the inference from counting information.

The subsequent partial summation display on p. 10 also has incorrect signs/exponents. For \(a=1/2+1/(2L)\), inclusion of the atom at \(a\) gives exactly
$$
 \sum_{\beta\ge a,\ 0<\gamma\le T} T^{2\beta-1}
 = eN(a,T)+2L\int_a^1 T^{2u-1}N(u,T)\,du.
$$
This follows by writing each summand as its value at \(a\) plus the integral of its derivative from \(a\) to the individual \(\beta\). It gives \(o(TL)\) with the uniform premises, and the \(O(L)\) vertical estimate alone then gives only \(o(TL^2)\) for the bound formed in the preprint. [Primary PDF, §§2 and 6](../../sources/analytic/2306.04799.pdf)

## Retaining the horizontal denominator

In the first inequality of §6, bound the absolute magnitude of \(S(T)\) by the nonnegative sum, absorbing the bounded \(w\) and \(2\pi\). For each ordered far pair, charge its term to a zero with the larger \(|\beta-1/2|\). This costs at most a factor of two when later summing over all outer zeros and all partner zeros. For the charged zero \(\rho=\beta+i\gamma\), write
$$
 m=L|\beta-1/2|,\qquad d=L|\beta-\beta'|,\qquad v=L(\gamma-\gamma').
$$
The far cutoff and triangle inequality give \(1\le d\le2m\le L\). Thus \(m\ge1/2\). The kernel term is bounded by a constant times \(e^d/(d^2+v^2)\). Put \(q=2m-d\ge0\). From \(m=(d+q)/2\) and \(d\ge1\),
$$
 \frac{1+m^2+v^2}{d^2+v^2}
 \le 1+\frac{1+m^2}{d^2}\ll(1+q)^2.
$$
The function \(e^{-q}(1+q)^2\) is bounded. Therefore each term is at most a constant times \(e^{2m}/(1+m^2+v^2)\).

Apply (2.5) in unit shells. The shell \(|\gamma-\gamma'|<1\) contributes \(O(L/(1+m^2))\) to the kernel without its \(e^{2m}\) factor. The other shells contribute \(O(L\sum_{j\ge1}(jL)^{-2})=O(1/L)\). This is \(O(L/(1+m^2))\) since \(m\le L/2\). Reflection in the critical line preserves \(\gamma\), \(m\), and multiplicity. Consequently
$$
 |S(T)|\ll L\sum_{\substack{0<\gamma\le T\\\beta\ge 1/2+1/(2L)}}
            G(L(\beta-1/2)),\qquad
 G(y)=\frac{e^{2y}}{1+y^2}.
$$

Writing \(D(y)=N(1/2+y/L,T)\), layer integration gives the right-side sum without the outer \(L\) as
$$
 G(1/2)D(1/2)+\int_{1/2}^{L/2}G'(y)D(y)\,dy.
$$
The derivative is positive and \(G'(y)e^{-2y}=O((1+y^2)^{-1})\). For fixed small \(\eta>0\), put \(y_*=(25/32+\eta-1/2)L\). The strong-density premise gives \(D(y)\le \epsilon(T)Te^{-2y}\) for \(1/2\le y\le y_*\), with \(\epsilon(T)\to0\). It follows that the initial term and the integral below \(y_*\) give \(O(\epsilon(T)T)\). Above \(y_*\), it suffices to use the weaker uniform \(O(Te^{-2y})\) consequence of the source's stated (6.5). That part is \(O(T\int_{y_*}^\infty(1+y^2)^{-1}dy)=O(T/L)\). Together they give \(S(T)=o(TL)\) with the same kernel, so Lemma 7 and §7 can be applied as before. This replacement uses the upper-range estimate as stated in the preprint. It does not reprove every estimate in Bourgain's original argument. [Primary PDF, Lemma 6 and §§6–7](../../sources/analytic/2306.04799.pdf) [Bourgain bibliographic record](https://doi.org/10.1155/S107379280000009X)

Theorem 2 also follows by the printed thin-box-to-density reduction. At \(\sigma\ge1/2+1/(2L)\), the strict box forces all counted ordinates to be at most \(Y=T^{3/8}\). Thus \(N(\sigma,T)\ll T^{3/8}L=o(T^{2(1-\sigma)})\) uniformly for \(\sigma\le25/32+\eta\) if \(0<\eta<1/32\). The upper-range Bourgain bound and the preceding calculation suffice with this one fixed \(\eta\).

One can also verify the earlier direct thin-box repair with the coarser vertical bound. At height \(Y\) the contribution to \(\sum T^{2\beta-1}\) from \(\beta\le4/5\) is \(O(T^{39/40}L)\). Above \(4/5\), use the uniform \(N(u,Y)\ll Y^{2(1-u)}\) bound and the paper's Vinogradov–Korobov bound \(u\le U=1-\eta(Y)\) for zero real parts at height at most \(Y\). The endpoint at \(4/5\) is \(O(T^{3/4})\), since \(T^{2u-1}Y^{2(1-u)}=T\exp[-(5/4)L(1-u)]\). The derivative integral is \(O(LT\exp[-(5/4)L\eta(Y)])=o(T)\), since \(L\eta(Y)\gg L^{1/3}(\log L)^{-1/3}\). Thus the outer sum is \(o(T)\), and even the coarse \(O(L)\) vertical bound gives \(S(T)=o(TL)\).

## Version scope

The publisher record shows Acta Arithmetica 214 (2024), pp. 357–376. Its PDF endpoint redirects to the publication page, which labels PDF access subscriber-restricted. Crossref returns no update relationships on the article record. The authors' follow-up arXiv:2501.14545v1 §§2–3 explicitly identifies and repairs a different error in the remainder of the published BGSTB24 Theorem 1, and says applications such as Lemmas 5 and 7 remain correct. The follow-up quotes a different remainder from formula (1.4) of arXiv:2306.04799v1. The corrected (3.3) of the follow-up provides the remainder strength used in the v1 applications. The follow-up does not establish how the journal version handled (6.4). [Publisher record](https://doi.org/10.4064/aa230612-20-3) [Crossref record](https://api.crossref.org/works/10.4064/aa230612-20-3) [Authors' follow-up §§2–3](https://arxiv.org/html/2501.14545v1#S2)
