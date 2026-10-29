# The moving-prime error in the Gauss Gram formula

**Status.** This is a source-qualified bookkeeping observation, not an improvement of the full error bound. It traces the D-loss in Xu–Sang [arXiv:2610.17675v2](https://arxiv.org/abs/2610.17675v2), §§2.3 and 3.2, for the twist d=p, e_p=5, with p good and P=Np. The source's moments and their stated uniformity are imported.

The nonexceptional term in Proposition 3.1 is bounded by Lemma 3.2 as O_ε(D Z^ε), Z=2qLD. For one frozen C,b,g and branch, its two column characters have moving support at most D R_C,g, and the two applications of the plain second moment (2.6), combined by Cauchy–Schwarz, give

    w_C,g √(N₁N₂) (Krow/Ng) D R_C,g Z^ε
      ≤ N R X D Z^ε.                                                (1)

Here R denotes the source's outer-frequency shell parameter, not a conductor, and the last step is (3.7). After summing the frozen labels and the q/L³ prefactor, this yields O_ε(D Z^ε). Thus the D factor is inherited from the **moving-support factor in the nonprincipal plain moment**; it is not a pointwise bound on the Gauss local factor that can simply be averaged away.

For d=p and e_p=5 the columns are coprime to p, so p divides neither C nor b nor g. Split the nonexceptional frequencies into p|k and p∤k. On the first part write k=pℓ. The local symbol satisfies, including its zeros,

    χ_n(p⁵k) = χ_n(p⁶ℓ) = 1_(n,p)=1 χ_n(ℓ).                       (2)

The p puncture was already present in the column and is fixed independently of ℓ; it is an admissible fixed puncture in (2.6), and remains in the unit-ideal factor. The p symbol can therefore be removed from the moving support while the frequency length shrinks by P. All other frozen factors, masks, ray partitions and branch scalars are unchanged. Repeating the source proof on this subfamily gives O_ε(P^(−1) Z^ε) for its nonexceptional contribution. If the rescaled row ball is subunit it is empty; dyadic shell and Fourier-seminorm estimates remain those of Lemma 3.2. The implicit power losses and source parameter conventions are as there.

For p∤k, however, the frequency family still contains a nontrivial fixed twist χ_n(p⁵), and its moving support still contains p. The stated second moment supplies only the original O_ε(P Z^ε) contribution. A saving from this dominant subfamily would require a new estimate exploiting the *fixed prime twist* and its interaction with the varying frequency, or a direct cancellation in the signed Gram expansion. Neither follows from (2) or the source moment. In particular this split alone does not extend the P≤Y^(1/7−δ) regime in the [growing-rank calculation](README.md).

**Independent review.** A second researcher checked the frozen-variable coprimality, cancellation and preserved puncture, the shorter ℓ range, and the surviving p-coprime support loss against the source, conditional on its uniform fixed-puncture moment.
