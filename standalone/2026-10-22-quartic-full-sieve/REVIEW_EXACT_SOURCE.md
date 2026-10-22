# Additional exact-source review: quartic sieve tail and coefficient correction

**Reviewer:** `spectral_route`, an internal research agent.
**Verdict:** no invalidating gap found in the tail lemma or corrected coefficient identity within the scopes below. The checked completion steps and README preserve those scopes. This report establishes neither a new zero-free boundary nor integration, human review, external peer review, or formal verification.

## 1. Frozen source and review scope

- Source commit: `193c3d79f0522f08f62afc5c24c29f139d889080`.
- Source tree: `1e71897b46a6b7b75fe8694c48b7d08911260276`.
- Parent: `e87c5f669f81fe6371af926917d1c5b21023bce8`.
- Packet: `standalone/2026-10-22-quartic-full-sieve/`.

Every source file was retrieved with `git show` at that commit. Hashes below are SHA256 of the exact Git blob bytes, without text or line-ending normalization.

| File | SHA256 |
|---|---|
| `QUARTIC_PRIMITIVE_SIEVE_TAIL.md` | `7500879e7fd62776ab4c06c55f3de2777fac9c8983e3acd62a6ef75943a8ee64` |
| `CORRECTED_QUARTIC_CODEC.md` | `cf82e4e81c15c16814d49d4415301207e30c4152829e03ad55280ad6148f1754` |
| `QUARTIC_ALL_ROW_COMPLETION.md` | `5e89202a6a9c72382ab01e38a6444a80c1c31199e030a01c92b19700d52620f4` |
| `README.md` | `d2d4db8df9309fd16cfeb3ff58fdaf5b1454a85417e9897264edd2b1756b3d44` |
| `DIRECT_PRINCIPAL_TARGET.md` | `5f87538ea5dbc9c858ae867969ee9170ccdc303e384fecaa1cee7aa8bf3a63cb` |
| `EXACT_COLUMN_MARKED_INVERSE.md` | `aa318fc58f8b8ba2a37d23eb69cf0e91e918a321192e28795ed1ffb2c2bc15fd` |
| `REFINED_POWERFUL_ROW_ENERGY.md` | `e1d0628a608a10412a43a0516aad7ca453f4bfbb5ccfb75ba1207ef664129ef7` |
| `QUARTIC_SPECTRAL_INTERFACE.md` | `c02d2f9cb36a0c2b76c6a24b5ab37d9efb3a85b19ddef573c34dae612075b63c` |

The main fresh reconstruction concerns the tail proof, particularly its complete multiplicative large sieve and its rowwise branch count. I had previously derived the quartic coefficient correction independently before reading the completed correction note. I authored the last three companion notes in the table; this report is not an independent review of those notes. The principal-target note was read to check the README's conditional wording, not to supply an additional complete review of its analytic continuation argument.

## 2. Complete-row large sieve and branch summation

The tail's use of the ordinary complete multiplicative large sieve has the required scope. Reduced Gaussian fractions with denominator norm at most \(M\) have separation \(\gg M^{-1}\) on the two-dimensional torus. Distinct primary denominators do not create duplicates. The fixed trace convention only changes the fixed dual-lattice normalization. The lattice additive large sieve therefore gives \(O(X+M^2)\) for **all** rows \(0<Nr\le X\).

More explicitly, primitive Gauss inversion and orthogonality of all characters at each modulus give the usual primal inequality

\[
 \sum_{Nc\le M}\frac{Nc}{\varphi(c)}
 \sum_{\chi\bmod c}^{*}
 \left|\sum_{0<Nr\le X}a_r\chi(r)\right|^2
 \ll (X+M^2)\sum_r|a_r|^2.
\]

Selecting the primitive quartic character at each squarefree conductor and applying Hilbert-space duality gives the tail's (13). The dual coefficient weight \(\varphi(c)/Nc\le1\) can be discarded. Odd squarefree quartic characters are primitive at every prime in their conductor. Conductor one is handled by the row count \(O(X)\). This step never restricts the physical rows to squarefree integers.

For a fixed powerful part \(q\) and Ramanujan branch, the CRT phases and \(\overline{\chi_m(\rho)}\) depend only on the column and the fixed branch. The remaining local factor depends on the row but has modulus at most the displayed branch weight. The annular support gives \(\sum_m|b_m|^2\ll_W1\), including the possible column \(m=1\). This justifies the branch bound (14).

For a fixed nonzero row \(k\), each supported pair \((q,\mathfrak b)\) has \(\rho(q,\mathfrak b)\mid k\). At a prime of valuation \(v\), the allowable exponents satisfy \(2\le e\le v+1\), with at most two local branches. Hence the number of supported pairs is at most

\[
 \prod_{\pi\mid k}(1+2v_\pi(k))
 \le \tau(k)^2
 \ll_\epsilon (Nk)^\epsilon.
\]

Cauchy is applied using this count **before** summing over physical rows. The factor \(B_R(q)\) costs only a divisor-bound power because \(Nq\le bD\). Thus no sum of square roots over all powerful parts is needed.

I checked both local types: the nonprincipal exponents force \(v_\pi(k)=e-1\) with normalized modulus \(p^{-1/2}\); exponents divisible by four retain the exact two-term Ramanujan identity. The resulting local squared weights start at \(p^{-2}\) and \(p^{-5}\), respectively, giving the radical tails \(R^{-1+\epsilon}\) and \(R^{-4+\epsilon}\). This proves the stated

\[
 (KD)^\epsilon\left(K/R+D^2/R^4\right)
\]

bound for arbitrary bounded **row-independent** column weights. At \(K=D^2/H\), the simplification to \(K/R\) requires \(R^3\ge H\). The zero row is excluded; the exact empty-tail ranges follow from \(d^2\mid c\) and \(d\mid k\).

The tail's dependency header names DDHL v2 whereas the packet README names v4. I checked the local identities actually used against [DDHL v4, (3.4)--(3.8)](https://arxiv.org/html/2306.11875v4). This version difference does not affect those steps; the tail does not use the earlier erroneous Gauss-square encoding.

## 3. Corrected quartic identity and completion checks

For split primes \(\pi=a+bi\), the self-symbol in DDHL v4 (3.11) equals
\[
 (\bar\pi/\pi)_4^{-2}=(2a/p)=(2/p)=(-1/\pi)_4.
\]
Here quadratic reciprocity and \(p=a^2+b^2\) give \((a/p)=1\). The finite signs cancel. For inert primary primes \(-p\), Frobenius preserves the trace character and conjugates the quartic character; since \(\chi(-1)=1\), the Gauss sum is real and its square is \(p^2\). Squared CRT phases are one, and nonsquarefree moduli have literal zero Gauss sum. These checks give
\[
 \widetilde g_4(c)^2=\mu_F(c)c/|c|
\]
for every odd primary \(c\), including both coefficient conversions. I also reconstructed the exact \(-1+2i\) counterexample to the old extra-ray formula.

For the completion note, I checked the new local fourth-power step: the \(j=4\) term is \(p^4-p^3\), while \(j\ge5\) lifts by \(p^4\). Fourth powers preserve the CRT and ray factors. This gives (2.1) with the stated sign and norm powers. Iteration is finite over primes, not over successive fourth-power quotients. Comparison with [CDFD v2, Corollary 6.2](https://arxiv.org/html/2604.01316v2) confirms the low-valuation coefficients used in (3.1). The row and Mellin scale substitutions (4.1)--(4.3) check algebraically. These checks concern nonzero Gaussian numerators, with the stated fixed ramified convention, and retain the external puncture.

## 4. Scope, omissions, and first remaining gap

The README accurately states that the full tail and exact completion do not prove a new boundary. Its \(0.85\) target is explicitly conditional; its marked refinement is described as source-dependent and inactive at the existing optimizer. It retains the zero-row exclusion, the condition \(R^3\ge H\), and the reciprocal-cusp warning.

The tail proves no bound for a row-dependent arbitrary column weight, no centered main term, and no total-vector norm used in a mixed Cauchy estimate. Completion and decreasing Mellin scales give identities, not summable automorphic norm estimates. The finite-cover evaluation cost and both reciprocal packet scales remain material.

I did not reprove the imported metaplectic continuation, the full spectral theory, the underlying cubic reflection, or the source-qualified inherited boundary. I did not verify a growing-level centered estimate, every cusp, or the missing cross-term/diagonal reconstruction. The first unresolved application step remains the uniform centered low-divisor quadratic estimate with its exact finite arithmetic diagonal and all mixed terms.

**What was run:** exact-commit Git reads, raw-byte SHA256 and control-byte checks for all eight source files, primary-source comparisons, and the mathematical reconstructions above. No numerical experiment, theorem prover, or executable proof checker was used; no source mathematics was changed.
