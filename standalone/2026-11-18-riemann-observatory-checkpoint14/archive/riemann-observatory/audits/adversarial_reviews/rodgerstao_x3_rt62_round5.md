# Independent check of the inverse-distance bound and Proposition 22 \(X_3\) comparison

Reviewer rt_repair_62. [Rodgers–Tao, arXiv:1801.05914v5](https://arxiv.org/pdf/1801.05914v5), PAPER-S004. Selected-source follow-up to the independent \(X_4\) note. Source inputs are (43)–(44), (50), (62)–(63), (66)–(67), the nearby relation on p. 42, and the \(X_3\), \(X'_3\) sums and comparison on pp. 49–52. All constants below can be chosen uniformly in the paper's time range. This checks the use of inverse-distance bounds in the \(X_3-X'_3\) comparison, without assessing the full proposition.

## Global and restricted unsigned bounds

Write \(L=\log T\), \(N=T L\), \(w_k=(1+|k|/N)^{-100}\), \(M=TL^3+\widetilde E_T\). Use the source's odd indexed points, assumed pairwise distinct, and put \(z_{jk}=|x_j-x_k|^{-1}\), \(z^0_{jk}=|\xi_j-\xi_k|^{-1}\). The pointwise inequality from the first rt62 audit yields \(S_2=\sum_{j\ne k} w_jw_k z_{jk}^2\ll M\), with the same bound for \(z^0\).

For \(h=|j-k|>A\log^2(2+|j|+|k|)\) with \(A\) sufficiently large, (44) and (50) give \(z_{jk}\ll\log(2+|j|+|k|)/h\). For fixed \(k\), summing this upper bound against \(w_j\) over \(|j|\le2|k|\) gives \(O(\log^2(2+|k|))\) by the harmonic sum. Over \(|j|>2|k|\) it gives at most \(\sum_{j\ne0} O(w_j\log(2+|j|)/|j|)=O(L^2)\), splitting at \(N\). Therefore the weighted total in this distance range is \(O(NL^2)\).

For the complementary range, \(h\le A\log^2(2+|j|+|k|)\) implies \(h=O_A(\log^2(2+|k|))\). Indeed, if \(|j|>2|k|\), then \(h\ge |j|/2\), forcing \(|j|=O_A(1)\). Also \(w_j\asymp_A w_k\) uniformly here, since \(|j|\asymp |k|\) outside a fixed interval. Thus the weight sum over this range is \(O_A(\sum_k w_k^2\log^2(2+|k|))=O_A(NL^2)\). By Cauchy–Schwarz its inverse-distance sum is \(O(\sqrt{MNL^2})=O(M)\). Combining the ranges gives
\[
 \sum_{j\ne k} w_jw_k (z_{jk}+z^0_{jk})\ll M.
\]
The bound has no exterior logarithm. The classical harmonic-block lower bound from the first audit explains why the extra logarithm cannot be inserted.

The split also gives restricted estimates. If both indices have \(|j|,|k|\le U=2T^{7/10}\), the large-distance part contributes \(O(UL^2)\) before any extra logarithm. For the small-distance part the pair weight is \(O(UL^2)\), giving at most \(O(\sqrt{MUL^2})\) by Cauchy–Schwarz. These bounds are still \(o(M)\) after any fixed power of \(L\). If both indices have \(|j|,|k|\ge B/2\) for \(B=T^{11/10}\), even with factors \(\log^C(2+T+|k|)\), the large-distance part is bounded by
\[
 O_C\left(\sum_{|k|\ge B/2} w_k(\log^2(2+|k|)+L^2)
            \log^C(2+T+|k|)\right).
\]
This is \(O_C(B(N/B)^{100}L^{C+2})\) by dyadic summation. For small distances, use Cauchy–Schwarz and the pair square-weight bound \(O_C(B(N/B)^{200}L^{2C+2})\). Both bounds are \(o(M)\). The argument also works for the thresholds \(T^{1-c}\) and \(T^{1+c}\) in Lemma 21(iii)–(iv), with constants depending on fixed \(c>0\). For the high threshold the first tail bound has factor \(T^{1-99c}\), and the weight in the second has factor \(T^{1-199c}\), before fixed logarithms. The restriction on both indices in (iii)–(iv) is respected below by passing from each anchor threshold to a comparable pair threshold.

## Exact mixed-domain comparison

Let \(i,j,k\) be pairwise distinct with \(j\sim_T k,\ i\sim_T k,\ i\not\sim_T j\), as in \(X_3\) and \(X'_3\). Write \(D_k=(T^2+|k|)^{1/10}\). The nearby distances are \(O(D_k)\), by \(|i-k|^{10}<T^2+2|k|+|i-k|\) and its \(j\) version. Write \(d_i=|i-k|\), \(d_j=|j-k|\), and \(R_{ab}=(T^2+|a|+|b|)^{1/10}\). The map \(a\mapsto R_{ab}\) is Lipschitz with constant \(\eta=\tfrac1{10}T^{-9/5}\). Therefore
\[
 D_k\le R_{kj}\le R_{ij}+\eta d_i\le d_j+(1+\eta)d_i.
\]
The last inequality allows equality \(R_{ij}=|i-j|\), covering the exact complement to the strict nearby relation. One of the two distances is at least \(D_k/3\) for large \(T\). Call it long, choosing either at ties. Every long reciprocal, actual or classical, is \(O(\log(2+T+|k|)/D_k)\), by (44), (50) and the uniform bound \(\log^2(T^2+|k|)/D_k=o_T(1)\). Nearby weights are comparable, since \(D_k=O(T^{1/5})=o(N)\) for \(|k|\le T^2\), and \(D_k=O(|k|^{1/10})=o(|k|)\) otherwise.

For \(|k|<T^{7/10}\) or \(|k|>T^{11/10}\), bound each product in the difference absolutely. At fixed \(k\) and fixed other index, there are \(O(D_k)\) possibilities for the long index, so its reciprocal sum costs at most \(O(\log(2+T+|k|))\). If the long index is \(j\), transfer its weight to \(i\) by comparability. In either case the remaining weighted sum is a sum of short-factor \(z\) or \(z^0\), multiplied by this logarithm. The remaining pair has both indices at most \(2T^{7/10}\) in the low range and both at least \(T^{11/10}/2\) in the high range. The restricted estimates above give \(o(M)\).

In the remaining bulk, first consider \(d_i,d_j\ge T^{1/10}\). The actual reciprocal of either signed gap equals its classical counterpart times \(1+O(L^2 T^{-1/10})\), by (44) and (50). The difference of products is bounded by \(O(L^2 T^{-1/10}z^0_{kj}z^0_{ki})\). The unweighted classical reciprocal sum over each nearby index is \(O(L^2)\) by harmonic summation. Retaining \(w_k\) and using \(\sum_k w_k=O(N)\) proves an error \(O(T^{-1/10}NL^6)=o(M)\).

Otherwise, the short distance \(h<T^{1/10}\) is unique since the other distance is at least \(D_k/3\). Fix \(k\) and the short index \(s\). For a possible long index \(\ell=k\pm r\), define
\[
 F_\pm(r)=r-(T^2+|k|+|k\pm r|)^{1/10}.
\]
It increases at least at rate \(1-\eta\) in the sense of all difference quotients. The conditions \(k\sim_T\ell\) and \(s\not\sim_T\ell\) imply
\[
 -(1+\eta)h\le F_\pm(r)<0.
\]
Indeed \(r+h\ge |s-\ell|\ge R_{s\ell}\ge R_{k\ell}-\eta h\). Each ray therefore permits \(O(h+1)\) integer distances. Since \(D_k\ge T^{1/5}\), the sum of long absolute reciprocals on these slots is \(O((h+1)L/T^{1/5})=O(LT^{-1/10})\) in bulk, for both actual and classical gaps. Transfer the long weight to the short index when needed. Bounding the two products absolutely gives \(O(LT^{-1/10}M)=o(M)\) by the corrected global inverse-distance estimate. This covers both (83) and (84), including boundary coincidences. It avoids the preliminary long-factor replacement on p. 52 entirely. If performed in this bulk short-distance regime, that replacement has relative error \(O(L^2T^{-1/5})\) by (44), (50), and the long lower bound. There is no need for that relative-error expression at arbitrary superpolynomial \(|k|\).

These bounds show \(X_3-X'_3=o(T\log^3T+\widetilde E_T)\) on the exact source domains. The positive lemma with its original exterior logarithm is unnecessary for this comparison. The separate \(X_4\) audit covers the other central use of that lemma. No whole-paper coverage is claimed.
