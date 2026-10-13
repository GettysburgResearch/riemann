# Sources, overlap, and external-input boundary

## Repository sources actually inspected

1. PR #937, head `9f3250198a9b0551f42eb73dfd74a265c2a66854`:
   `standalone/2026-10-13-prime-freezing-and-noise/PRIME_FREEZING.md`.
   https://github.com/GettysburgResearch/riemann/pull/937
   Supplies the model, log-square starting theorem, and exact signed flux.
   Its Section 3 lower example changes the coefficient array. Its Section 4
   terminal lower bound is explicitly open. This packet preserves that status.
   The local mounted proof was read and the live PR source identity checked.

2. PR #936, head `eb8d23decc003d36ded287dc98868308192cc889`:
   `standalone/2026-10-13-rough-conductor-localization/PROOF.md`.
   https://github.com/GettysburgResearch/riemann/pull/936
   Sections 1--4 were read at the pinned source through the connected GitHub
   tool. They already prove the positive Rankin upper tradeoff
   2k max(1/2,1-1/A), and sharpness using retained local phases realized by
   CRT without controlled row height. Our sign version of the upper tradeoff
   is not presented as a new general method. The principal-row lower envelope
   and its controlled-height amplification are the additional conclusions.

The recent PR descriptions #930--#935 were checked for overlap; except for
previously supplied context they were not fully proof-audited or imported as
analytic inputs. No exhaustive historical or global novelty audit is claimed.

## Classical literature and what is used

3. R. de la Breteche and G. Tenenbaum,
   *Friable averages of oscillating multiplicative functions*,
   arXiv:2207.04777v14, revised 20 July 2024.
   https://arxiv.org/abs/2207.04777v14
   https://arxiv.org/pdf/2207.04777
   The abstract, introduction, Theorem 1.2 and reference list were inspected,
   including the page-3 theorem screenshot. The PDF heading uses
   "oscillating arithmetic functions". This paper treats negative zeta powers
   and asymptotic expansions of smooth-number restricted sums. Its introduction
   explicitly discusses extension to products of Dedekind-zeta powers.
   We credit this existing theory; we do not import its full uniform theorem
   without a field/test adapter. MATHEMATICS.md Section 4 instead provides
   a self-contained reduction, at fixed 1/2<theta<1, from the classical
   prime ideal and Mobius estimates explicitly stated in (1.2).

4. Earlier works credited by that paper include:
   K. Alladi, *Asymptotic estimates for sums involving the Mobius function II*,
   Trans. Amer. Math. Soc. 272 (1982), 87--105;
   A. Hildebrand, *On a problem of Erdos and Alladi*, Monatsh. Math. 97
   (1984), 119--124; and G. Tenenbaum, *Sur un probleme d'Erdos et Alladi*,
   Seminaire de theorie des nombres, Paris 1988--89, Progr. Math. 91
   (1990), 221--239. These original papers were not independently re-read
   in full during this pass. Bibliographic credit is not a proof audit.

5. The classical prime ideal theorem goes back to E. Landau,
   *Neuer Beweis des Primzahlsatzes und Beweis des Primidealsatzes*,
   Math. Ann. 56 (1903), 645--670. Bibliographic record:
   https://eudml.org/doc/158079
   The fixed-field zero-free-region consequences in (1.2) are separately
   stated standard analytic-number-theory inputs. We do not claim that a
   bibliographic record alone proves the displayed all-log-power Mobius bound.
   No growing conductor, GRH, imported 7/8 theorem, or numerical zero computation
   is used. The exact field and finite exclusions remain fixed throughout.

6. Rankin majorants, the finite Mellin transform identity, Khintchine's fixed
   even-moment inequality, and partial summation are classical tools.
   The needed finite-sign inequality and all applications are reconstructed
   in the proof. Standard unique ideal factorization, the norm-Euclidean
   property of the Eisenstein integers, and six units supply the actual
   prime-generator replicas.

## What is not claimed

The sharp envelope does not prove a lower bound at one prescribed logarithmic
cutoff curve. The forced flux blocks concern an explicit physical replica
measure, not a signed lower bound over the whole row ball. The positive centered
hierarchy does not control the conditional mean or original endpoint.
This packet proves no new full native moment or zero-free exponent.
