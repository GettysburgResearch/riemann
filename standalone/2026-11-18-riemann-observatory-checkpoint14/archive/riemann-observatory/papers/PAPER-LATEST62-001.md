# The sixth moment of the Riemann zeta function

Alexandre de Faveri and Mayank Pandey. arXiv:2610.01035v1, 1 October 2026, 19 pages. The archived arXiv landing page shows one version and gives a repository DOI. [Version history](https://arxiv.org/abs/2610.01035v1) · [Primary PDF](https://arxiv.org/pdf/2610.01035v1)

## Reading and verification

Read all 19 pages of the primary PDF through its layout-preserving text, including the introduction, proof sketch, §§3–10 and references. The reading follows the passage from additive energy to large values of perturbed square-root sums, then through short zeta moments back to large zeta values and moment integration. Level 1 denotes complete substantive reading. The cited input proofs and full exponent bookkeeping have not been independently audited. The private PDF is `sources/recent_corpus_round5/2610.01035.pdf`.

- Theorem 1.1, p. 1 and proof p. 19. Unconditionally, for $T\ge1$ and $\varepsilon>0$, $\int_0^T|\zeta(1/2+it)|^6dt\ll_\varepsilon T^{37/30+\varepsilon}$.
- Theorem 1.3, p. 2, and Theorem 9.1, pp. 15–18. If $T^{7/60}\le V\le T^{5/38}$, the maximum size $N(T,V)$ of a 1-spaced subset of the $[T,2T]$ level set $|\zeta|\ge V$ satisfies $N(T,V)\ll_\varepsilon T^{24/17+\varepsilon}V^{-128/17}$.
- Corollary 1.4, p. 2 and proof p. 9. Let $D_\eta(w)=\sum_{N<n\le2N}a_ne(w(\sqrt{n/N}+\eta(n/N)^{3/2}))$, with $|a_n|\le1$, $N\le W\le N^{4/3}$, $|\eta|\le cW/N^2$ for sufficiently small $c>0$, and $\Upsilon=1+|\eta|W$. A 1-spaced set in $[0,W]$ on which $|D_\eta|\ge V$ has size $\ll_\varepsilon N^\varepsilon(N^2/V^2+N^2W^{3/4}\Upsilon^{1/8}/V^3+N^{5/2}W^{3/2}\Upsilon^{1/4}/V^5)$.
- Theorem 10.1, p. 18. The unconditional twelfth-moment bound is $T^{2-520/445121+\varepsilon}$. Its proof uses Theorem 9.1 with auxiliary integer $k=6$, the Trudgian–Yang 2025 exponent-pair consequence, and Bourgain subconvexity. Theorem 1.2 then uses fourth-to-twelfth moment interpolation to save a power for each fixed exponent in $(4,12]$.

## Checkable consequences and next question

At $V=T^{1/8}$, Theorem 1.3 gives the exponent $8/17$, a saving of $1/34$ over the classical exponent $1/2$ at that threshold. In the sixth-moment decomposition the upper endpoint contributes exponent $2-6(5/38)=23/19<37/30$, while both low-range and middle-range contributions attain $37/30$ at the lower endpoint. The Iwaniec density application reported in §1.1 requires a sixth-moment exponent strictly below $6/5$. The present exponent is $1/30$ above $6/5$.

A scoped follow-up is to keep the short-second-moment reduction fixed and test which of the competing terms in (30), p. 18, would have to improve to extend the low end of the useful large-value estimate below $V=T^{7/60}$. For a sixth-moment exponent below $6/5$, the classical fourth-moment contribution $T V^2$ already forces the crossover to occur below $V=T^{1/10}$. Extending only the existing line $24/17-(128/17)\sigma$ toward lower $\sigma$ would not suffice because the line, after adding $6\sigma$, grows towards the left.
