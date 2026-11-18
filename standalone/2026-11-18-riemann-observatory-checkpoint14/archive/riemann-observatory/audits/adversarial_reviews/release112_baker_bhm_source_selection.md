# Independent selection review of Baker and Blomer–Harcos–Michel

18 November 2026. Recommend both published papers as targeted Level 0 proof dependencies. I matched the publisher metadata and the controlling passages against the retained PDFs. The full journal articles are accessible. The inspected evidence is limited to the passages below.

I compared normalized titles, author combinations, DOI strings and the Numdam item identifier against 1,002 canonical bibliography rows, 1,133 records across 89 contributor shards, 13,617 records across 14 top-level corpus and provider JSONL ledgers, the alias register and the existing Round 14 pending record. No matching work or provider candidate was found. The two proposed work IDs are distinct from each other and from the separate Ghosh, Ren and Korolev dependencies.

## Baker's averaged inverse-prime sum

Roger C. Baker, *Kloosterman sums with prime variable*, Acta Arithmetica 156(4), 351–372 (2012), DOI `10.4064/aa156-4-4`. The 22-page publisher PDF hashes to `2b1b0690e08489b077bb632fef2d6ea777ebe6684dc02efe5d6af9e67127cbda`. On p. 351 the sum has primes (x<p\le2x) with ((p,q)=1), and phase (e(a\bar p/q)). On p. 352 Baker defines (q\sim Q) as (Q<q\le2Q) and Theorem 2 bounds the sum over this modulus block of the maximum over unit numerators by ((Q^{11/10}x^{4/5}+Qx^{11/12})Q^\epsilon), for (Q^{1/2}\le x\le2Q).

This is the direct source of the inverse-prime cancellation used after divisor Voronoi. The local proof uses a common prime endpoint in each application of the modulus average and controls its distinct taper weights by Abel summation. The result does not directly bound inverse-square phases, arbitrary dual numerators sharing factors with the modulus, or the whole signed (C_*) sum.

[Publisher issue metadata](https://www.impan.pl/pl/wydawnictwa/czasopisma-i-serie-wydawnicze/acta-arithmetica/all/156/4) · [Publisher PDF](https://www.impan.pl/shop/en/publication/transaction/download/product/82065) · [Local arithmetic application](prime107_inverse_prime_voronoi.md)

## The exact smooth divisor transform

Valentin Blomer, Gergely Harcos and Philippe Michel, *Bounds for modular L-functions in the level aspect*, Annales scientifiques de l’École Normale Supérieure, Série 4, 40(5), 697–740 (2007), DOI `10.1016/j.ansens.2007.05.003). The 44-page Numdam journal PDF hashes to `7a07387f1f9da1dcd20d9dda329d0ee02d6d8df5aa3af885227545cbc4149fb5`. In §2.3, (2.25)–(2.27), pp. 708–709, the smooth divisor Voronoi formula takes a positive integer modulus (c), ((d,c)=1), and (F\in C_c^\infty((0,\infty))). It has a numerator-independent logarithmic main term and dual phases (e(\pm\bar d m/c)), with kernels (J^-=-2\pi Y_0(4\pi\,\cdot)\) and (J^+=4K_0(4\pi\,\cdot)\). This is a checked formula within the paper, distinct from its level-aspect subconvexity theorem.

With the prime factor frozen and coprime to the modulus, the unit-numerator subtraction cancels the main term and converts the dual unit average to a Ramanujan factor. Both remaining inverse-prime phase signs fit Baker for unit dual indices. The numerical cutoff bounds and saving for the transition band belong to the separately reviewed application.

[Numdam journal record](https://www.numdam.org/item/ASENS_2007_4_40_5_697_0/) · [Numdam journal PDF](https://www.numdam.org/item/10.1016/j.ansens.2007.05.003.pdf#page=12) · [Independent transfer review](uniform108_baker_bridge_qa.md)

Both records remain pending director primary-passage reading and admission. The raw PDFs remain in private source storage.
