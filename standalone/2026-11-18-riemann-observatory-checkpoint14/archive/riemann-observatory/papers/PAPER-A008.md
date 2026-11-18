# PAPER-A008 — Lee–Leong: quantitative Mertens and reciprocal-zeta bounds

Ethan Simpson Lee and Nicol Leong, [*New explicit bounds for Mertens function and the reciprocal of the Riemann zeta-function*, arXiv2208.06141v5](https://arxiv.org/abs/2208.06141v5),9September2026; first submission12August2022.25pages. Preprint; no journal reference was observed. The visible PDF title omits the hyphen in zeta-function; both variants are recorded. Accessed17November2026.

**Scope:** PDF accessed; introduction and Theorem1.1 inspected, with PDFp2 rendered to verify the exponent. Whole-work reading/audit is not claimed. The current source states, for every realx>=exp(4589.20),

|M(x)|<33.56x(logx)exp(−sqrt(logx/5.56)).

This is Theorem1.1,eq(9),p2, stated unconditionally. It supplies faster-than-any-logarithmic-power cancellation. The proof and its explicit computational constants remain an external cited input. A separate elementary Abel argument converts it tosum_(n<=N)mu(n)/n=O_K((logN)^(-K)) andsum_(n<=N)mu(n)logn/n=−1+O_K((logN)^(-K)), for every fixedK>0. Exact hypotheses/derivation are in audits/mobius_quantitative_source_analytic_round4.md.

Version history matters: v3(31May2023) was withdrawn; its actual notice says cited technical ingredients contained errors seriously affecting those results. v4(26July2024) and the inspectedv5 are later replacements, and the current landing describes substantial revisions. This archive has not audited the repair or compared the proofs. It makes no error allegation aboutv5 and does not substitute an earlier abstract for the current theorem.
