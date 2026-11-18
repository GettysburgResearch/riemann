# ABR cutoff and short-interval normalization check

I checked arXiv:2604.25579v1 §§1–3 and both appendices against the primary PDF, and followed the cited Arguin–Bailey short-interval arguments in arXiv:2202.06799v2 §§3.2–3.3. This is a scoped re-audit of PAPER-LATEST62-002. It adds no unique-work full-read count. The checks give a repair of the cutoff path to Theorem 1.1 conditional on the Gaussian comparison estimates used in the paper, and verify normalized formulations of Corollaries 3.1–3.2. The archived arXiv history lists only v1, submitted 28 April 2026. [Version snapshot](../../sources/witness62_abr/arxiv_2604.25579_history.html) [ABR primary PDF](../../sources/recent_corpus_round5/2604.25579.pdf) [AB23 primary PDF](../../sources/witness62_abr/2202.06799.pdf)

## Where the stated cutoff is unavailable

In (1.7)–(1.8), the checkpoints and abscissae are defined only up to \(L=1+\max\{\ell:\beta_\ell\le e^{-10^4 k}\}\), for \(\beta_\ell=e^{\ell-1}/\sqrt{\log T}\). The event \(G_\ell\), the increment constraints, and Lemma 2.3 concern \(1\le\ell\le L\). In the proof of Lemma 2.3, (2.4) takes the least \(m\) with \(\beta_m>\beta_\ell^\gamma\), \(\gamma=1/25\). Since \(0<\beta_L<1\) and \(\gamma<1\), at \(\ell=L\) this requires \(m>L\). The same issue arises for any \(\ell\) with \(\beta_\ell^\gamma\ge\beta_L\), including some \(\ell<L\). Merely excluding the last index does not resolve it. The proof does not specify a separate treatment for this band. Extending the geometric sequence alone does not enlarge the domain of the abscissae, the good events used for \(S_\ell^{(m)}\), or Lemma B.1. The endpoint paragraph near (1.13) announces a bound on \(H\cap G_L\). This is a different event from the barrier exits at indices where (2.4) is out of range.

For an in-range \(m\), the printed argument below (2.6) checks a length less than \(T^{1/2}\). Lemmas A.1 and B.1 state \(T^{2q\beta_m}\le T^{1/4}\). The weaker criterion is insufficient to invoke either lemma as stated. Both changes are addressed below. [ABR pp. 4–9 and 11–12](../../sources/recent_corpus_round5/2604.25579.pdf)

## Stop at the last usable checkpoint

Keep all the original cutoff definitions, the good and increment events, and the barrier widths. Put \(t=\log\log T\), \(t_\ell=t+\log\beta_\ell\), \(h_\ell=-\log\beta_\ell\), and \(c_\ell=e^{h_\ell/25}\). For fixed \(k\ge2\) and large \(T\) let
$$
 J=\max\{\ell\le L:\beta_\ell^\gamma<\beta_L\}.
$$
Then \(1\le J<L\), \(h_L/\gamma<h_J\le h_L/\gamma+1\), and \(10^4k-1<h_L\le10^4k\). In particular \(t_J=t-O(k)\), \(c_J=\exp(O(k))\), and \(\beta_J^{-1}=\exp(O(k))\). At every \(\ell\le J\), (2.4) has a well-defined \(m\le L\) and \(\beta_m\le e\,\beta_\ell^\gamma=e/c_\ell\), by minimality and the geometric ratio. All the event restrictions in (2.2) then cover the abscissa at \(m\). Keep the original unions over \(j\le L\). Telescope only up to \(J\):
$$
 \mathbb P(H)=\sum_{\ell=1}^{J}\mathbb P(H\cap(G_{\ell-1}\setminus G_\ell))
                  +\mathbb P(H\cap G_J).
$$

For the lower barrier, the parameter calculation can use \(q=\lceil W/10\rceil\), \(W=(V-u)/10\), and \(\kappa=V/t\le1.1k\) for sufficiently large \(T\). With \(u\in[L'_\ell,L_\ell]\) and \(h=h_\ell,\ c=c_\ell\),
$$
 c\le V-u\le \kappa h+4c,\qquad
 2q\beta_m\le \frac{2e}{100}(\kappa h/c+4)+\frac{2e}{c}<\frac14.
$$
For the last inequality \(h\ge 10^4k-1\ge19999\), so \(c=e^{h/25}\) and \(\kappa h/c\le1.1(h+1)h e^{-h/25}/10^4\). The correction keeps a fixed margin below the stated polynomial length bound.

For \(D=t_m-t_\ell\le h+1\), Lemma A.1 and \((2q)!/(2^q q!)\le(2q)^q\) give the moment ratio in (2.6) at most a constant from the lemma times \((qD/W^2)^q\). Here \(W\ge c/10\), and \(q\le W/9\). The logarithm \(\log(9W/D)\) is at least
$$
 \frac h{25}-\log\!\left(\frac{10(h+1)}9\right)\ \ge\ \frac{0.9h}{25}.
$$
This bounds the moment ratio by \(\exp[-0.9h(V-u)/2500]\), up to the lemma's implicit factor. In particular its exponential saving is at least \(3.5k(V-u)\) for these \(h\). The one-point factor \(e^{-u^2/t_\ell}\), with \(\bar u=u-\kappa t_\ell\), loses at most \(\exp(\kappa^2h+2\kappa|\bar u|)\) relative to \(e^{-V^2/t}\). As \(V-u\ge|\bar u|\ge c\), the moment saving absorbs that loss, the \(O(c)\) bins, and the \(O(h+1)\) abscissae. The resulting bound has the factor \(e^{-c}e^{-V^2/t}/\sqrt t\). Rounding bin endpoints by bounded constants is harmless with this margin. For the two-abscissa branch, (2.2) places both bins within \(O(c)\) of \(\kappa t_\ell\), while their separation is at least \((V-u)/10-O(1)\). Lemma B.2 then supplies a Gaussian saving \(\exp(-\Omega(c^2))\). Expanding the square in \((u+w)^2/(4t_\ell)\) costs at most \(\kappa^2h+8\kappa c+O(\kappa)\) in the exponent relative to \(e^{-V^2/t}\), enough even for the first level where lower endpoints can be negative. The number of bin pairs and abscissae is absorbed as above. The other two barrier estimates are used only in their original index range.

For the surviving event, apply Soundararajan (1.5) with \(x=T_J\) and \(\lambda=1/2\). Prime powers \(p^r\) with \(r\ge3\) cost \(O(1)\), since \(\sum_p\sum_{r\ge3}p^{-r/2}/r\) converges. Thus \(H\cap G_J\) forces \(S_J^{(J)}>V-\frac34\beta_J^{-1}-O(1)\). On \(G_J\) this sum also lies in a band of length \(2c_J\). Apply the untwisted one-point bound on each of its \(O(c_J+1)\) unit bins. This is the \(Q=1\) version of (B.1), obtained by omitting the twist in (B.9)–(B.13). Each used bin has \(u\ge V-\exp(O(k))\) and \(t_J=t-O(k)\), so
$$
 \mathbb P(H\cap G_J)\ll
   \exp(\exp(O(k)))\,\frac{e^{-V^2/t}}{\sqrt t}.
$$
This is the constant scale of Theorem 1.1. Early-exit estimates sum because \(c_{\ell-1}=e^{1/25}c_\ell\). This verifies the replacement index and length choices, and the needed terminal estimate, assuming the comparison input. It does not prove Proposition 1.4 for its original late indices or constitute an independent verification of Appendix B. [ABR §§1.2–2.3 and Appendix B](../../sources/recent_corpus_round5/2604.25579.pdf)

## Corollaries 3.1–3.2 use probability in the center

By ABR §1.2, \(\mathbb P(\tau\in E)=\operatorname{meas}(E)/T\) for \(\tau\) uniform on \([T,2T]\). The §3 applications describe the exceptional bounds as Lebesgue measure. Their cited AB23 source uses the same wording in Corollaries 1.3–1.4 but its proofs explicitly bound \(\mathbb P\), starting with its discretization inequality (63), then (66), and ending with \(\mathbb P(G^c)\ll1/A\). In AB23 §3.3, a different division by \(2(\log T)^\gamma\) normalizes the **within-window** high-point measure, leaving the independent normalization \(1/T\) for the random window center.

There is a direct counterexample to the literal raw-measure formulation of (3.2). Take its allowed \(\beta=0\) and \(A=3/2\). The integrand is one almost everywhere in \(h\), regardless of how the power at zeros is defined, so the integral is identically \(2(\log T)^\gamma\). Every \(t\in[T,2T]\) is exceptional, and its exceptional Lebesgue measure is \(T\), not \(O(1/A)\). With normalized measure the implicit constant can cover this case. This example concerns (3.2) as worded and is independent of RH. [ABR p. 10 render](../../sources/witness62_abr/abr_v1_p10-10.png) [ABR pp. 9–10](../../sources/recent_corpus_round5/2604.25579.pdf) [AB23 §§3.2–3.3](../../sources/witness62_abr/2202.06799.pdf)

For the positive normalized bounds, let \(s=\log\log T\), \(k_\gamma=\sqrt{1+\gamma}\), \(M=k_\gamma s-(\log s)/(4k_\gamma)\), and \(X(\tau,h)=\log|\zeta(1/2+i(\tau+h))|\). The discretization bound (63) multiplies the one-point probability at \(V=M+y-O(1)\) by \(O(e^{(1+\gamma)s})\). Theorem 1.1 then gives normalized probability \(O_\gamma(e^{-2k_\gamma y-y^2/s})\) for \(y=o(s/\log s)\), since the \(\log s\) term cancels the \(s^{-1/2}\) and its cross term with \(y\) is \(o(1)\). Shifted center distributions can be bounded by integrating over the original interval plus a fringe of relative length \(O((\log T)^\gamma/T)\) per mesh point. This is negligible even after multiplication by the mesh size. For (3.2) with \(\beta>0\), Fubini with the global \(\beta\)-moment bounds gives an expected short moment \(O_{\beta,\gamma}((\log T)^{\gamma+\beta^2/4})\). Adjacent dyadic intervals cover all shifts. Markov gives \(O_{\beta,\gamma}(1/A)\) in normalized measure.

For (3.3), fix \(\beta>2k_\gamma\), take \(B>0\) depending on \(A,\gamma\) to make the normalized exceptional probability for the maximum above \(M+B\) be \(O_\gamma(1/A)\), and restrict to its complement \(E\). For any fixed \(a\in(0,k_\gamma-k_\gamma^2/\beta)\), the layer integral for the expected short moment times \(1_E\) is bounded by a constant times
$$
 e^{\gamma s}\left(e^{\beta as}
      +\int_{as}^{M+B}\frac{e^{\beta v-v^2/s}}{\sqrt{s}}\,dv\right).
$$
Here the one-point tail estimate is uniform over the compact interval of positive slopes in the integration range. This follows from Theorem 1.1 for every convergent slope sequence by a compactness argument and the given bound for \(C_k\). The negligible shift fringe contributes \(o(1)\) before comparison to the displayed bound. Because \(\beta-2v/s\) stays bounded below by a positive constant, the integral is at most a constant times its integrand at \(M+B\). Expanding that endpoint, the expectation is \(O_{B,\beta,\gamma}\big(e^{(\beta k_\gamma-1)s}s^{-\beta/(4k_\gamma)}\big)\). Markov with factor \(A\) gives the claimed stochastic order for each fixed \(\beta,\gamma\), with a constant depending on the fixed parameters. Raw exceptional measures multiply all these probabilities by \(T\). These derivations confirm the normalization independently of treating the wording as an implicit convention. [ABR Theorem 1.1 and §3](../../sources/recent_corpus_round5/2604.25579.pdf) [AB23 §3.2](../../sources/witness62_abr/2202.06799.pdf)
