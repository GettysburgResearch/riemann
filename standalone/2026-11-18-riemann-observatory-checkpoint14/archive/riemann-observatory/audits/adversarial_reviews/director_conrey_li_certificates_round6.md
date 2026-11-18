# Reproduced Conrey–Li negative shift forms

Source arXivmath/9812166v1, full preprint10pages, SHA256 `bdb68ede69e41939be0c2b740cbe1955da8b24940e30eb8c8f4554878dfb4568`. Conrey and Li established these negative examples and credited Sarnak with a separate nonnumerical argument. The program supplies scoped interval reproductions, not a new obstruction or a criticism of that paper.

The director inspected the actual kernel action(2.3), Theorems1–2 and all four source examples, read both independent audits and their code, and reran the256-bit FLINT program using its pinned private interpreter. The output matched the retained JSON exactly. The gamma/zeta/Hurwitz balls rely onpython-flint0.9.0. A separate75-decimal interval implementation using only explicit Euler–Maclaurin and log-gamma Stirling remainders independently encloses one interior zeta witness.

ForE(z)=X(1−iz), whereX is exactly the source completion, the actual zero kernel is in the positive-i-shift domain by(2.3). At a critical zeroρ=1/2+it,w=−t−i/2, its real form is−Re[X′(ρ)X(ρ+1)]/(2π). Opposite strict real endpoint signs on rational brackets of half-width10^-20 around the two source heights give actual zeros by continuity and functional-equation realness. A derivative/product ball on each whole bracket certifies a strictly negative form. Root enumeration, simplicity and RH are unnecessary. The zeta bracket center is111.029535543169674524656, with sign numerator in(−5.390,−5.388)×10^-69; theχ4 center is67.6369208635460683980549, with sign in(−2.311,−2.309)×10^-45. The factor2π is positive. The source uses its stated completion normalization, so a change by a nonzero real constant preserves signs but rescales these numbers.

ForW(z)=1/X(1−iz), the prescribed kernel actionT K_W(w,·)=K_W(w+i,·) has, at every strictly upper-half-plane w,

    Re< K_W(w,·),T K_W(w,·) >
      =|W(w+i)|²/[2π(2Imw+1)] Re[W(w)/W(w+i)].

Take w=−282+i10^-6 forζ. The independent interval calculation gives

    −0.004750153564007396
      < Re[X(2+10^-6+282i)/X(1+10^-6+282i)]
      < −0.004750153564007395.

It verifies both denominators exclude0. This single interior kernel disproves the stated numerical-range positivity without invoking extension across the original boundary. The correspondingχ4 witness usesw=−8714.2+i10^-6. FLINT also reproduces the two boundary ratios printed in the source. The source's numerical quotient is the reciprocal of the kernel ratio, with the same real sign because Re(1/q)=Re(q)/|q|²; that normalization must not be silently reversed.

In the independent implementation, the periodic Bernoulli remainders are explicitly added to both interval components before division. The gamma logarithm is analytic on the right half-plane and real on the positive axis. The bound|z+t|≥(|z|+t)/sqrt2 controls its remainder; no special-function point evaluations are used there. The director checked those remainder bounds as well as the reproducing and derivative signs.

Scope: two specified entire-space shift forms and two specified reciprocal-space kernel actions. A different domain, shift or operator is not excluded. Tests distinguish a root's existence from the sign of its form throughout the root enclosure. Mathematical kernel identities plus validated signs establish these finite counterexamples; floating agreement alone would not.

Evidence: witness62_conrey_li_deep.md; prefix_formula62_conrey_li_independent.md; experiments/code/witness62_conrey_li_deep.py and prefix_formula62_conrey_li_independent.py; exact retained results. Reproduce after installingpython-flint==0.9.0 in a virtual environment; experiments/reproducibility.md gives commands. No source-author error finding arises from reproducing these correct negative results.
