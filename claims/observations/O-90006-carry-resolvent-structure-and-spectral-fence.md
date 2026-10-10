# O-90006 — The carry inverse is exactly Möbius × elementary; no spectral/PSD realization exists

Claim ID: `O-90006` (provisional range; allocate at registry)
Status: **STRUCTURE THEOREM PROVED (exact-rational-verified); SPECTRAL LANE CLOSED with exact witness — session-author review (compact strike; no separate verifier agent, disclosure below)**
Authoring: `claude-fable-5` session `riemann-proof-review-8nz34i`, Strike C (2 prongs) + session-author adversarial read
Date: 2026-08-09
Extends/subsumes: `L-32701` rows 2–3 (PR #337) — closed-form symbols now for ALL rows
Scope: exact algebra + located-failure certificates; no RH claim

## 1. Structure theorem (proved; verified in exact rationals for the full inverse at T=60)

On indices \(\{2..T\}\) (virtual rows 0,1 zero-padded), the carry matrix factors **exactly**:
\[
B_T=N^{-1}S^2D_-\Delta Z,\qquad
\boxed{\,B_T^{-1}=M\,S\,D_-^{-1}\Delta^2N\,}
\]
(\(N=\mathrm{diag}(q+1)\), \(S\)=cumulative-sum, \(D_-=\mathrm{diag}(q-1)\), \(\Delta=I-\)shift, \(Z\)=divisibility, \(M\)=Möbius matrix \(\mu(q/n)[n|q]\)) — **the inverse carry matrix is the Möbius operator times elementary factors, with no truncation error at any finite T**. Key identity (session-author re-verified by hand at n=2): \(\Delta_q^2[(q+1)\beta_{q,n}]=(q-1)([n|q]-[n|(q-1)])\). Explicit inverse rows: \(c_j(n)=\sum_{e|n}A_{j,e}\,\mu(n/e)\) with \(A_{j,j}=\frac{j+1}{j-1}\), \(A_{j,j+1}=\frac{(j+1)(2-j)}{j(j-1)}\), \(A_{j,e}=\frac2{j(j-1)}\) for \(e\ge j+2\) (constant tail — matching O-90001's positive hinge envelope); Dirichlet symbols reproduce `L-32701`'s \(E_2,E_3\) exactly and extend to all \(j\): \(E_j(s)=-2\sum_{d<j}d^{-s}+(j+2)(j-1)j^{-s}-j(j-1)(j+1)^{-s}\).

## 2. The spectrum is provably arithmetic-free

\(\mathrm{spec}(B_T^{-1})=\{\frac{n+1}{n-1}\}\) (triangularity); \(\det=T(T+1)/2\) exactly — in sharp contrast to Redheffer (det = Mertens), **the arithmetic is pushed entirely off the spectrum into non-normality**: no diagonal symmetrizer exists (one line: diagonal similarity preserves triangularity), and the true symmetrizer's condition number is \(1.6\cdot10^{73}\) at T=50, \(9.4\cdot10^{179}\) at T=100. Singular values follow smooth power laws (\(\sigma_{\max}\sim T^{0.50}\), cond \(\sim T^{1.51}\)) and do **not** approach Hilbert–Pólya constants \(1/(\frac14+\gamma_k^2)\). The zeros live where the symbol says: Dirichlet-transform functionals \(t\mapsto|\sum_nc_j(n)n^{-1/2-it}|\) peak at the first six zeta zeros to grid resolution (T=2000).

## 3. The autopsy (the located-failure certificate)

**Congruence Lemma (proved, one line):** \(\mathrm{sym}((B_T^{\mathsf T})^{-1})\) PSD ⟺ \(\mathrm{sym}(B_T)\) PSD (\(x=B_T^{\mathsf T}y\); Sylvester kills all diagonal-rescaling escapes). **The zero-responsiveness pre-check passes** — unlike the CvS candidate (R-16001): for Dirichlet test vectors the Hermitian form converges to \(\Phi(s)=G(\bar s,s)/\zeta(s)+\)elementary, and the pole residues at the first zeros are \(|G/\zeta'|\approx6.34,4.67,4.01\ne0\) — this gate would have *meant* something. **And it is false, violently:** first failure at exactly \(T=10\) with an **exact rational witness** (\(r^{\mathsf T}B_{10}r=-427605197/13860000000<0\), Fraction arithmetic); min eig \(\sim-0.0232\,T\) (linear); a single frozen profile transfers across scales (Rayleigh \(-0.023T\) at every T tested to 3072). **Cause: ζ-blind and structural** — the pure carry sawtooth \(g(u)=\lfloor u\rfloor(1-\{u\})/u\), with no Möbius/prime input whatsoever, reproduces the minimal eigenvalue to 0.6%, the same eigenvector peak and mass profile, the same \(-0.023T\) law.

**Fence.** Carry positivity is a **cone statement** (the single hinge direction \(h_T\), rows \(c_T\ge0\) — the L-32701/O-90001 lane), not a spectral statement: the same sawtooth that accumulates one-sidedly along the hinge direction is two-sidedly indefinite. No PSD/spectral realization of the carry family exists. Recorded so no future wave attempts a "carry operator" Hilbert–Pólya reading.

## 4. What survives and where it points

The structure theorem is a genuine asset: an exact, boundary-error-free finite model of \(1/\zeta\), reducing every hinge-row question (SHARP, O-90001) to the explicit band-plus-constant-tail matrix \(A\) acting through Möbius convolution — the recommended follow-up is a positivity analysis at the level of \(A\) (where the constant tail matches the observed positive envelope) rather than of any symmetrization. RH-content extraction from this family is norm growth against oscillatory vectors — i.e. Mertens-type partial-sum functionals — reconnecting to the O-90004 §4 calibration rather than to a new operator.

## 5. Review disclosure

Compact strike: no separate verifier agent was budgeted. Session-author review performed: the \(\Delta^2\) identity hand-checked (n=2, q=4,5,6), Möbius inversion on indices ≥2 validated, the Congruence Lemma's change of variables re-derived, the T=10 witness is exact-rational (no float trust), and all statuses preserve the prong agents' own labels. Scripts: `scratchpad/struct_check.py`, `spec.py`, `spec2.py`, and the C2 witness/profile scripts; full prong reports in the session workflow journal (`wf_e914df48-132`).
