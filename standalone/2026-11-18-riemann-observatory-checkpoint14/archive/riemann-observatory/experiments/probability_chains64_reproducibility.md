# Two probability laws from zeta zeros

## Caption

**Two probability laws from zeta zeros.** (A) The arithmetic Nakamura–Suzuki exponent gives an equivalence between RH and the statement that its exponential is an infinitely divisible real-line characteristic function. Under RH this characteristic function belongs to a compound Poisson sum whose jumps carry multiplicity weights on all signed zero ordinates. The conditional tail, iid Cauchy limit and dense atom set belong to that law. Its zero atom satisfies \(0.95487677454644730<\Pr(X=0)<0.95490529007639706\). (B) Under RH, sample one signed ordinate beyond height \(Y\) in absolute value with normalized derivative weights and map it to the countable prime torus. Heap–Li–Zhao (HLZ) supplies the source input for the Poisson-circle product limit. The scalar CLT for the actual arithmetic draw at \(P=(\log Y)^D\) uses the refined uniform character bound to match every fixed moment to the product model. The product is the fixed-character weak limit, while the CLT uses quantitative control of characters with growing indices.

## Stable claim identifiers

- Panel A uses THM-NAKAMURA-ZETA-ID, THM-NAKAMURA-PROBABILITY-TAIL, THM-NAKAMURA-CAUCHY-SCALING, THM-NAKAMURA-DENSE-ATOMS and CERT-NAKAMURA-ZERO-ATOM. [Director review](../audits/adversarial_reviews/director_probability_tail_round10.md)
- Panel B uses THM-PRIME-POISSON-TORUS, THM-HLZ-UNIFORM-POLYLOG-PHASE and THM-ARITHMETIC-PRIME-PHASE-CLT. [Torus limit review](../audits/adversarial_reviews/director_hlz_prime_torus_round9.md) · [CLT review](../audits/adversarial_reviews/director_prime_phase_clt_round10.md)

## Regenerate

Run from the repository root with Python and Matplotlib. The original export uses Matplotlib 3.10.8, its Agg backend and bundled DejaVu and mathematical font assets.

    python experiments/code/probability_chains64.py

The script produces a 2700 × 2000 PNG and vector PDF and SVG. PDF fonts are embedded and SVG glyphs are paths. [PNG](results/probability_chains64.png) · [PDF](results/probability_chains64.pdf) · [SVG](results/probability_chains64.svg)
