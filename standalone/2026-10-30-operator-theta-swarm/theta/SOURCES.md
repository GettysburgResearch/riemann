# Sources, repository context, and originality scope

## Primary mathematical references

- Dan Romik, *Orthogonal polynomial expansions for the Riemann xi function*, arXiv:1902.06330v3 (5 May 2019), equations (1.6)–(1.11) for the exact theta/Fourier normalization; Section 1.1.2 for the Pólya universal-factor background. [Abstract](https://arxiv.org/abs/1902.06330) · [PDF](https://arxiv.org/pdf/1902.06330). The full PDF was retrieved and the normalization inspected. Romik's orthogonal-polynomial Poisson flows are related background; the sampling construction here has not been identified with one of those flows.
- NIST Digital Library of Mathematical Functions, [10.25.2](https://dlmf.nist.gov/10.25.E2): the positive series for `I_n(a)`. [10.32.9](https://dlmf.nist.gov/10.32.E9): the integral defining `K_nu(a)`. The respective documentation pages were inspected.
- Classical Gaussian Poisson summation gives equation (9) directly. The exact exponential-tilting and Skellam identities are derived from the two Poisson power series in the proof, rather than taken as a black-box probabilistic result.

## Repository comparison

The inspected current integrated guide was the `AGENTS.md`, `README.md`, `STATUS.md`, `PROGRAMMES.md`, and relevant xi/operator entries in `research/integrated/CURRENT_RESULTS.md` at the available checkout `/workspace/scratch/12ccfafb9db9/riemann` (observed head `c77671d71dcf22a08833a6d7f86a6f15a2eba84f`). That is a historical checkout, not a claim about the current live main head.

The theta20 packet's `README.md` and relevant searches of `PROOF20.md` were also inspected in a separate existing local snapshot. It realizes the actual theta moments through degree 20 by a connected finite ferromagnet, and explicitly leaves cofinal feasibility open. Searches also inspected neighboring theta and finite-model material. This lane does not extend that finite certificate or inherit an unperformed replay.

The current parent task separately inspected the live GitHub PR state. No claim is made that every historical research branch has been searched exhaustively.

## What is asserted as this contribution

The supplied proofs establish the particular derivative obstruction, the fixed-envelope analyticity obstruction with a quantitative bandwidth consequence, the explicit Skellam source approximation and diffusion expansion, and the coefficient obstruction to its elementary multiplier shortcut. These are proposed new contributions to this research packet, not claims of global priority. Pólya approximants, Lee–Yang phenomena, Skellam laws, Bessel-function expansions, positivity tests, and source approximation as general methods are classical.

In particular, the proof does not use or improve an imported quasi-RH boundary. It is not a universal closure theorem for arbitrary positive kernels. The open Bessel-sum zero statement is a new precise research target here, not an established theorem.
