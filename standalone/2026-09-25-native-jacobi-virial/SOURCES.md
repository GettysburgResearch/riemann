# Sources, prior work, and reading scope

## Existing mathematics imported or credited

1. NIST Digital Library of Mathematical Functions, Sections 18.25 and 18.26. Specifically 18.25.2 and 18.25.6--8 give continuous dual Hahn weights and norms; 18.26.2 gives the terminating hypergeometric polynomial. Checked on 25 September 2026. The parameters (1/2,1/2,3/2) used here are positive. The packet derives its own normalization and validates it with exact rational moments.
   https://dlmf.nist.gov/18.25
   https://dlmf.nist.gov/18.26

2. Ole Fredrik Brevig, Karl-Mikael Perfekt, Alexander Pushnitski, *The spectrum of some Hardy kernel matrices*, arXiv:2003.11346; Annales de l'Institut Fourier 74 (2024), 1061--1094, DOI 10.5802/aif.3589. The kernel 1/max(m,n) is the alpha=1/2 member of their family. This paper explicitly places its inverse in Jacobi/continuous dual Hahn theory. The native finite subtraction and the source-specific virial adapter are worked out in PROOF.md; the underlying spectral object is not claimed new. Read the abstract and pertinent introduction/Jacobi discussion in HTML, not an independent audit of the whole paper. The source's parameter/index conventions are not used to override our directly checked DLMF normalization.
   https://arxiv.org/abs/2003.11346
   https://arxiv.org/html/2003.11346v3
   https://aif.centre-mersenne.org/articles/10.5802/aif.3589/

3. Frantisek Stampach, *Asymptotic spectral properties of the Hilbert L-matrix*, arXiv:2202.04116, SIAM Journal on Matrix Analysis and Applications, DOI 10.1137/22M1476794. The studied finite matrix is 1/[max(i,j)+nu]. Checked abstract and publication page for prior-art attribution; this packet does not claim its norm asymptotics or an improvement on them. In particular, our generic 4||c||^2 bound is not a new Hardy inequality.
   https://arxiv.org/abs/2202.04116
   https://epubs.siam.org/doi/10.1137/22M1476794

4. Wlodek Bryc, *On the continuous dual Hahn process*, arXiv:2105.06969. Equations (2.4)--(2.5) in the HTML text supply an additional primary-source recurrence reference. The stochastic process is not imported into this research packet or claimed to solve the source problem.
   https://arxiv.org/html/2105.06969v3

The finite Dirichlet-convolution logarithmic derivative, finite summation by parts, Schur-complement identities, Fourier Plancherel, Bessel inequality, and beta/gamma identities are classical. Their source-specific application is proved explicitly. No external priority claim is made for the resulting elementary or composite identities. No infinite Euler product, unproved zeta property, random-prime model, or conjectured positivity is an input.

## Repository scope

The parent RAB33 packet was freshly replayed and published without changes at `12433ee0056756da006788a8b82e492aac9e6d1d` in PR #907. Live main was `f99d9e3908dde4865377c75d9ca051c1f545bf4f`. The original packet's reading scope and caveats remain in its SOURCES.md and PUBLISHER.md.

Main's agent/status instructions and recent PR metadata were read in the publication pass. Targeted default-branch searches for virial and Hahn did not find results; that is not a proof of novelty or an audit of unmerged branches. A broader reciprocal/variance search returned integrated review snippets but did not establish that this exact identity was or was not already present. No claim of repository-wide priority is made.

All additions are in a new standalone directory on the research branch. Main, other branches, canonical claim statuses, historical packets, and CI definitions are unchanged. The full Newton/Weil covariance has not been identified with the target W_N in this pass.
