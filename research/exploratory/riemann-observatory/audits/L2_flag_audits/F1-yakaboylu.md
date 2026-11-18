# Level-2 audit F1-yakaboylu

```text
Status: AUDIT (Level 2; adjudicated where flagged)
Scope: the specific issue named below, not the whole paper
Exact sources or dependencies: see 'Sources checked'
What was actually run: independent reading and recomputation by an auditor agent; independent two-sided adjudication where the auditor flagged an issue
Smallest remaining gap: see adjudication
```

**Target.** F1-yakaboylu: E. Yakaboylu, "Hamiltonian for the Hilbert-Pólya Conjecture", arXiv:2309.00405 (v1 Sep 2023 to v6 21 Jun 2024); J. Phys. A: Math. Theor. 57, 235204 (2024), DOI 10.1088/1751-8121/ad4c2d. Context also checked: precursor arXiv:2211.01899 and the follow-up arXiv:2408.15135 (v1 to v17, Aug 2024 to Aug 2026).

**Auditor classification.** `verified_error`

**Final classification.** `verified_error`; public characterization allowed: **True**

**Summary.** The paper does not claim to prove RH. Its v6/J. Phys. A text says the argument is formal and that "the second stage requires further rigorous treatment". It does claim to "establish the existence of a similarity transformation" that is self-adjoint on a domain fixed by a boundary condition satisfied through the zeta zeros, so that eigenvalues are real (Sec. II, Eqs. 12-18). That Stage-II claim fails, with explicit witnesses.

(a) The weight (18) defines an indefinite quadratic form. An explicit vector has <U|U> = -0.0231, so (18) is not the Gram kernel of any S'^dagger S'. Being symmetric for an indefinite (Krein) form does not imply a real spectrum.

(b) For eigenfunctions, condition (17) is equivalent to F(s)+F(1-s)=0 with F = Gamma*eta. This is not the Dirichlet condition. There are spurious solutions with zeta(s) nonzero (for example s = 1/2 + 3.70362i), and the eta-prefactor zeros satisfy Dirichlet but not (17).

(c) In Sec. I, the Dirichlet condition Psi_s(0)=0 also holds at s_k = 1+2*pi*i*k/log2, where zeta is nonzero. Psi_{s_k} is in L^2, so the "Hamiltonian with Dirichlet BC" has the non-real eigenvalues 2*pi*k/log2 - i/2 whatever the truth of RH. The paper excludes these points only by a convention in its introduction. With its natural domain S(Dom D), H has no eigenvalues at all.

(d) Davenport-Heilbronn control: the Sec. II argument carries over word for word to W_DH, which is positive and analytic. At the off-line zero rho_DH = 0.808517+85.699348i both the Dirichlet condition and (17) hold, so the argument would force Re rho_DH = 1/2, which is false.

Also found: the normalization in Appendix B assumes Re rho = 1/2 (circular), and the component series in Eq. (9) diverges factorially for the claimed eigenvectors. The author's later arXiv:2408.15135 v17 reduces the claim to an operator positivity that is equivalent to RH, and its point spectrum explicitly includes the prefactor zeros.

**Witness / evidence.** W1 (indefinite metric, Eqs. 14/18). Writing z=e^a and y=e^b, the form <U|U> = ∫∫ω'(z,y) u'*(y) u'(z) becomes a convolution form with spectral density 2Re F(1/2+iτ), where F(s) = Γ(s)η(s). This density is negative for τ in (3.7036, 6.1241), for example -0.00468 at τ=4. Test vector: u'(z) = z^{-1/2+4.8i} exp(-(ln z)^2/18). Direct 2-D quadrature of the paper's kernel gives <U|U> = -0.02313; with L=6 it gives -0.04703, against an asymptotic prediction of -0.02362/-0.04723. The matching vector U0 = Σ (u_n/n!)|n> is in ℓ^2, with ||U0||^2 ≈ 2.94e-5.

W2 (condition (17) is not the Dirichlet condition). For u'=z^{s-1}, (1/u')∫ω'u' dy = F(s)+F(1-s) exactly. This was checked by quadrature at s=0.3+2i, z=0.5 and z=3, agreeing to 1e-11. On the critical line this equals 2Re F(1/2+iτ). Its roots in (0,30) are 3.70362, 6.12407, 8.54643, 9.24104, 9.33466, 11.6687, 13.4473, 14.1347, 15.1575, 16.8919, 19.6791, 21.0220, 21.2802, 22.8090, 24.3160, 25.0109, 25.8556, 28.3633, 29.8664. Only 14.1347, 21.0220 and 25.0109 are zeta zeros. At s*=1/2+3.70362373148i: |ζ(s*)| = 0.5855 and F(s*) = 0.01012i, which is nonzero, while quadrature of (17) gives about 1e-18.

W3 (non-real Dirichlet eigenvalue in Sec. I). Take s1 = 1+9.064720284i, with ζ(s1) = 1.3466+0.1099i. Then ∫ z^{s1-1}/(1+e^z) dz = Γ(s1)η(s1) = 0 (quadrature about 1e-35). For t=(1-√5)/2, which is the paper's β=1 choice with α=0.1180, the Hille-Hardy closed form gives |Ψ_s(x)| ≤ C e^{-αx}; this was checked numerically. So Ψ_{s1} is in L^2 with Ψ_{s1}(0)=0, and its eigenvalue is E = 9.0647 - 0.5i.

W4 (Davenport-Heilbronn). W_DH(x) = Σ a_n e^{-nx} with a = (1, ξ, -ξ, -1, 0) mod 5 and ξ = 0.284079043840412. It equals q(1-q)(1+(1+ξ)q+q^2)/(1-q^5) with q=e^{-x}, so it is positive and analytic on [0,∞), with W(0) = 0.65682. Its Mellin transform is Γ(s)f_DH(s) (checked by quadrature), and the functional equation Λ(s)=Λ(1-s) was checked numerically. Kernel ω'(z,y) = W(y/z)/z + W(z/y)/y is symmetric and homogeneous of degree -1, so (14) and (15) hold. The zero ρ = 0.808517182456637+85.6993484853776i has |f(ρ)| = 5e-41 and |f(1-ρ)| = 3e-39. So the Dirichlet condition M[W](ρ)=0 holds and (17) holds (G_W(ρ)/|Γ(1-ρ)| = 3e-39), yet E = i(1/2-ρ) = 85.699 - 0.3085i.

W5 (Eq. 9 divergence). With c_m = B_m(2^m-1)/m! (confirmed with sympy) and g_m = Γ(m+ρ1)(1-η(m+ρ1)), |c_m g_m| = 2.1e-9 at m=2, 4.5e-3 at m=16, 2.4e2 at m=24 and 3.7e32 at m=60. The series is factorially divergent.

Analytic: H = S D S^{-1} on S(Dom D) has empty point spectrum. S is bounded and injective, and D is unitarily equivalent to -i d/du on L^2(R), which has purely absolutely continuous spectrum.

**Sources checked.**
- arXiv:2309.00405v6 full text (pdftotext; = J. Phys. A version era, dated 24 Jun 2024)
- arXiv:2309.00405v1 full text (abstract/claims)
- arXiv:2309.00405v3 full text (abstract: 'It is shown that the Hamiltonian is self-adjoint ... thereby ensuring that its every eigenvalue is real')
- arXiv abs page 2309.00405 (version history v1-v6; journal ref)
- Crossref metadata DOI 10.1088/1751-8121/ad4c2d (published 2024-06-04; transparent peer-review DOIs v1/v2/v3 reviews; content not accessible via WoS gateway)
- arXiv:2408.15135v17 full text (Nontrivial Riemann Zeros as Spectrum, 18 Aug 2026): Theorem 3.3 point spectrum includes Z_p; Theorem 4.5 W>0 iff RH
- arXiv:2408.15135 abstracts v1, v4, v7, v8, v10, v12, v14, v16, v17 (claim trajectory)
- arXiv API author search (Yakaboylu) incl. 2211.01899
- Zenodo 10.5281/zenodo.19353727 (N. Feldmann, 'Obstructions to the Spectral Proof of the Riemann Hypothesis via the Yakaboylu Hamiltonian', Mar 2026, unrefereed; addresses 2408.15135 v14)
- WebSearch for comments/critiques (none peer-reviewed found)
- Independent numerics: mpmath/sympy/numpy/scipy scripts in /tmp/claude-0/-home-user-riemann/e62aa4cb-6226-5e37-8f52-ea0fa055746f/scratchpad/l2/yakaboylu_scripts/check1.py ... check6.py

## Auditor report

# L2 audit: F1-yakaboylu, "Hamiltonian for the Hilbert-Pólya Conjecture"

## 0. Identification and versions
- **Target:** E. Yakaboylu, arXiv:2309.00405.
  - v1: 1 Sep 2023, "A Hamiltonian for the Hilbert–Pólya Conjecture".
  - v2: 16 Nov 2023. v3: 31 Jan 2024. v4: 22 Feb 2024. v5: 14 May 2024.
  - v6: 21 Jun 2024.
- **Published:** J. Phys. A: Math. Theor. **57**, 235204 (2024), DOI 10.1088/1751-8121/ad4c2d, published 4 Jun 2024.
  - Crossref lists transparent peer-review records: 2 referees and 3 rounds. Their text could not be retrieved because the Web of Science gateway needs JavaScript.
  - The audited text is arXiv v6 (published-version era). The IOP typeset version was **not** compared.
- **Precursor:** arXiv:2211.01899 (2022), "Formally Self-Adjoint Hamiltonian…".
- **Follow-up:** arXiv:2408.15135, v1–v17, 27 Aug 2024 – 18 Aug 2026. It is built explicitly on the J. Phys. A paper.
- **Third-party critique:** N. Feldmann, Zenodo 10.5281/zenodo.19353727 (Mar 2026). It is unrefereed and addresses 2408.15135 v14, not the J. Phys. A paper itself.
  - Its main points: the transformed Dirichlet domain is not dense; the bounded intertwiner gives conjugate pairing rather than reality; closing the gap is equivalent to the Nyman–Beurling criterion.
- No erratum or published comment to the J. Phys. A article was found.

## 1. What exactly is claimed (v6)
**Setup**
- The operator is H = S·D·S^{-1}, with:
  - D = (xp+px)/2 (Berry–Keating);
  - S = t^N e^{αx}/(1+e^x), where N = ½(xp²+p²x+x) is the Laguerre "number operator";
  - α = (1+t)/(2−2t), with Re t < 1;
  - all on L²[0,∞).

**Stage I (Sec. I)**
- The functions Ψ_s = S φ_s, with φ_s = x^{s−1}/√(2π), satisfy Ψ_s(0) ∝ (1−2^{1−s})Γ(s)ζ(s) (Eq. 3).
- The paper states: "The Dirichlet boundary condition can only be satisfied by the vanishing of the Riemann zeta function". Hence E_s = i(1/2−ρ).

**Stage II (Sec. II)**
- After a dilation and a choice of t (β=1, i.e. t = (1−√5)/2), the problem moves to "Mellin space".
- A weight ω′ is posited with ω′(z,y) = ω′*(y,z) (Eq. 14) and z∂_zω′ = −∂_y(yω′*) (Eq. 15).
- Integration by parts gives <V|H′U> = BT + <U|H′V>*.
- The boundary term is said to vanish under the ratio condition (17). From this the paper concludes "Dom H′ = Dom H′*", so that H′ "becomes self-adjoint … and hence admits only real eigenvalues".
- With ω′ = (1/z)/(1+e^{y/z}) + (1/y)/(1+e^{z/y}) (Eq. 18), the paper says (17) "corresponds to" Ψ_s(0)=0.
- Conclusion as stated: "Thus, there exist a similarity transformation … self-adjoint on the domain specified by the condition (17)". The abstract says "we establish the existence of a similarity transformation … that is self-adjoint".

**Hedge (Discussion)**
- "If the formal argument presented in this manuscript can be rigorously established, our approach holds the potential to imply the validity of the RH. It is important to note that the second stage requires further rigorous treatment."
- So **RH is not claimed as proved** in v6/J. Phys. A. v3's abstract was stronger: "It is shown that the Hamiltonian is self-adjoint … thereby ensuring that its every eigenvalue is real."

**W-generalization (Discussion)**
- Replacing (1+e^x)^{-1} by W gives the Dirichlet condition M[W](s) = 0.
- The paper says: "if there exists a similarity transformation … self-adjoint … then M[W] can have zeros only on the critical line". The abstract says: "Our result can be extended to a broader class of functions whose zeros lie on the critical line."
- **Precision note on the Level-1 reading:** the Discussion sentence is literally a *conditional*, so it is not false as written. What fails is the Sec. II construction, which is W-agnostic (finding F5).

**Follow-up trajectory (author's own)**
- 2408.15135 v1/v4 (2024): "the eigenvalues are real"; "well-defined similarity transformation that renders this Hamiltonian self-adjoint".
- v8/v10 (2025): "all such [simple] zeros lie on the critical line".
- v12 (Oct 2025): claims simplicity of the zeros and a positive semidefinite W that "enforces Re(ρ)=1/2". The spectrum now explicitly includes the "periodic Dirichlet zeros" 1+2πik/log 2.
- **v17 (Aug 2026):** retreats to "a symmetric operator W … whose positivity is *equivalent* to the Riemann Hypothesis". It states that "the self-adjointness of ĥ rests on the positivity W>0; yet this condition already entails Re(ρ)=1/2".
- Reported here as the author's own revision, not as an Observatory finding.

## 2. Findings (each with witness)
All numerics are independent of the Level-1 reader (mpmath 1.3, 25–40 digits; numpy/scipy). The scripts are in `/tmp/claude-0/-home-user-riemann/e62aa4cb-6226-5e37-8f52-ea0fa055746f/scratchpad/l2/yakaboylu_scripts/check1.py` through `check6.py`.

### F1. With its natural domain, H has no eigenvalues at all (analytic; precise)
- S is bounded and injective:
  - t^N is diagonal in the Laguerre basis with nonzero entries t^{n+1/2}, and is a contraction for 0<|t|<1;
  - e^{αx}/(1+e^x) is positive and bounded for α ≤ 1, which includes the paper's t=(1−√5)/2, where α=0.1180.
- D is self-adjoint and unitarily equivalent (via x=e^u) to −i d/du on L²(ℝ), which has purely absolutely continuous spectrum.
- Suppose HΨ = EΨ with Ψ = Sφ and φ ∈ Dom D. Then S(D−E)φ = 0, so (D−E)φ = 0, so φ = 0.
- Hence σ_p(H) = ∅ on Dom H = S(Dom D). The paper's "eigenstates" Ψ_s = Sφ_s come from φ_s = x^{s−1}, which is not in L² for any s. So they lie outside this domain.
- The eigenvalue statement therefore needs an extended operator and domain, which the paper never specifies.

### F2. On the extended "Dirichlet" operator: non-real eigenvalues exist regardless of RH. Stage I's "only ζ(s)=0" is false
**The functions Ψ_s**
- By the Hille–Hardy formula, Σ tⁿχ_n(x)χ_n(z) = (1−t)^{-1}e^{−α(x+z)}I₀(2√(txz)/(1−t)). This was checked numerically: 0.38872666319 from both sides.
- Hence Ψ_s(x) ∝ e^{−αx}∫z^{s−1}(1+e^z)^{-1}I₀(…)dz.
- For t=(1−√5)/2 this gives |Ψ_s(x)| ≤ C e^{−0.118x}. So Ψ_s ∈ L² for **every** Re s>0. The same holds for 0<t<√2−1.

**The Dirichlet condition**
- Ψ_s(0) ∝ Γ(s)η(s), and η also vanishes at s_k = 1+2πik/log 2 (k≠0), where ζ(s_k) ≠ 0.
- Witness s₁ = 1+9.064720284i:
  - ζ(s₁) = 1.3466+0.1099i;
  - the quadrature of ∫z^{s₁−1}/(1+e^z)dz is about 1e−35;
  - computed Ψ_{s₁}(0) ≈ 2e−35, against values of order 3e−5 for x>0;
  - Ψ_{s₁} decays and has finite L² norm.
- The eigenvalue is E = i(1/2−s₁) = 9.0647 − 0.5i.

**Consequence**
- Any domain containing the Dirichlet-selected eigenfunctions contains non-real eigenvalues. So "self-adjoint or admits only real eigenvalues ⇒ RH" is vacuous for this operator.
- The paper excludes s_k only through the introduction's phrase "except for the points where (1−2^{1−s}) is zero (which we consider hereafter)". That restricts a parameter; it does not specify a domain.
- The author's later 2408.15135 (v12–v17, Theorem 3.3) lists these points in σ_p.
- Classification for the Stage-I sentence: verified error, with a missing-hypothesis character.

### F3. The Sec. II "inner product" with weight (18) is indefinite. No similarity transformation realizes it
**Reduction**
- Write z=e^a, y=e^b, u′ = z^{−1/2}φ(ln z).
- Then (14) becomes ∫∫k(b−a)φ*(b)φ(a), with k(c) = e^{c/2}W(e^c) + e^{−c/2}W(e^{−c}).
- Its Fourier transform is k̂(τ) = M[W](1/2+iτ) + M[W](1/2−iτ) = 2Re F(1/2+iτ), with F = Γη.

**Sign changes**
- 2Re F(1/2+iτ) = 2.144 at τ=0, −0.00468 at τ=4, −0.00342 at τ=5, and changes sign infinitely often.

**Explicit negative vector**
- u′(z) = z^{−1/2+4.8i}exp(−(ln z)²/(2·3²)).
- Direct 2-D quadrature of the paper's kernel gives <U|U> = **−0.02313**. With L=6 it gives −0.04703; the predictions are −0.0236 and −0.0472.
- The matching state U₀ = Σ(u_n/n!)|n⟩ is in ℓ², with ||U₀||² ≈ 2.94e−5. It is therefore a legitimate vector in the paper's own representation (Eqs. 12, 21–22).

**Consequences**
- (18) cannot equal ⟨·|S′†S′|·⟩ for any S′ on a domain containing such vectors. So "there exist a similarity transformation" with this weight is false as stated.
- More basically, symmetry with respect to an indefinite (Krein) form does not imply a real spectrum. Eigenvectors with non-real eigenvalues are simply neutral.
- The same indefiniteness holds for the Davenport–Heilbronn analogue: 2Re M[W_DH](1/2+8i) = −3.7e−6.

### F4. Condition (17) is not equivalent to the Dirichlet condition
- For the eigenfunction u′ = z^{s−1} with weight (18), (1/u′)∫ω′u′dy = F(s)+F(1−s) exactly, independent of z.
  - Quadrature at s=0.3+2i, for z=0.5 and z=3, matches the closed form to 1e−11.
- So (17) holds iff F(s)+F(1−s) = 0, not iff F(s) = 0.
- Roots of 2Re F(1/2+iτ) in (0,30): 3.70362, 6.12407, 8.54643, 9.24104, 9.33466, 11.6687, 13.4473, **14.1347**, 15.1575, 16.8919, 19.6791, **21.0220**, 21.2802, 22.8090, 24.3160, **25.0109**, 25.8556, 28.3633, 29.8664. Only the three bold values are zeta ordinates.
- Witness s* = 1/2+3.70362373148i:
  - |ζ(s*)| = 0.5855 and F(s*) = 0.01012i, which is nonzero, so the Dirichlet condition fails;
  - the (17) quadrature is about 1e−18 at z=1 and z=7, so (17) holds.
- Conversely, at s_k (Re s = 1) the y-integral in (17) diverges logarithmically. The continued value F(1−s₁) = 5.70e−7 − 6.77e−7i is nonzero.
- So the paper's claim that "(17) corresponds to the boundary condition Ψ_s(0)=0" fails in both directions.
- Further structural defects:
  - (17) is a ratio condition, nonlinear in u′, so it does not define a linear subspace.
  - No adjoint domain is ever computed. "Dom H′ = Dom H′*" is asserted, not derived.

### F5. Davenport–Heilbronn control: the Sec. II argument proves a falsehood
**Why the argument transfers**
- The steps (13)→(17) use only (14) and (15).
- Any real kernel that is symmetric and homogeneous of degree −1 satisfies (15), by Euler's relation. In particular ω′_W(z,y) = W(y/z)/z + W(z/y)/y does, for any real W.

**The function W_DH**
- W_DH(x) = Σa_n e^{−nx}, with a = (1, ξ, −ξ, −1, 0) periodic mod 5 and ξ = 0.284079043840412.
- In closed form, W_DH = q(1−q)(1+(1+ξ)q+q²)/(1−q⁵) with q = e^{−x}. It is positive on (0,∞) and analytic at 0, with W(0) = (3+ξ)/5 = 0.65682.
- So S = t^N e^{αx}W is admissible, and xW′/W has a convergent Taylor series at 0, as in Eq. (5).
- Its Mellin transform is M[W](s) = Γ(s)f_DH(s); quadrature matches to 15 digits.
- The completed Λ(s) = (π/5)^{−(s+1)/2}Γ((s+1)/2)f(s) satisfies Λ(s) = Λ(1−s); checked numerically.
- The identity (1/u′)∫ω′_W u′ = M[W](s)+M[W](1−s) was checked by quadrature for W_DH as well.

**The zero**
- ρ_DH = 0.808517182456637 + 85.6993484853776i, with |f(ρ)| = 5e−41 and |f(1−ρ)| = 3e−39. The control value is |f(1.3+85.7i)| = 0.49.
- So:
  - the Dirichlet condition M[W](ρ) = 0 holds;
  - (17) holds, since |G_W(ρ)|/|Γ(1−ρ)| = 3e−39.

**Conclusion**
- The paper's argument, applied word for word, would make E = i(1/2−ρ_DH) = 85.699 − 0.3085i real. That is false.
- So the Stage-II inference is invalid; it is not merely non-rigorous.
- This is the requested Davenport–Heilbronn-type control. It also exposes the "broader class" remark: the method distinguishes nothing about 1/(1+e^x) except through the functional equation it shares with DH.

### F6. Appendix B normalization assumes RH (circular)
- The appendix rewrites ∫dz z^{ρ*+ρ′−2} as ∫dz z^{2ε−1} (with ρ = ρ′). That requires 2Re ρ − 2 = −1, i.e. Re ρ = 1/2.
- For Re ρ ≠ 1/2 the integral ∫z^{2σ−2}dz diverges at 0 or at ∞.
- The "δ_{ρρ′}" is really a Dirac delta in Im ρ, so the eigenfunctions are not normalizable for any ρ.
- The textbook argument "symmetric ⇒ real eigenvalue" needs 0 < <u|u> < ∞, which is unavailable here.

### F7. Bernoulli/Borel step (Level-1 point; suspected gap)
- c_m = B_m(2^m−1)/m! with B₁ = +½ is confirmed: sympy series of x/(1+e^{−x}).
- In Eq. (9) the k-th component is the series Σ_m c_m g_{k+m}/k!, with g_n = Γ(n+s)(1−η(n+s)). This was checked by quadrature.
- For s = ρ₁ = 1/2+14.1347i, |c_m g_m| is 2.1e−9 (m=2), 4.5e−3 (m=16), 2.4e2 (m=24), 9.1e7 (m=32) and 3.7e32 (m=60). The series is factorially divergent.
- So the claimed eigenvectors are not in the (maximal) domain of the number-basis operator (8). Eq. (9) holds only after an unstated Borel resummation, and the swap of Σ_m with ∫_0^∞dz is not justified.
- Minor point: the Borel polygon for these series is the strip |Im x| < π (resp. 2π), not the stated "Re x>0, Im x<π" region.
- This is not independently fatal, since the resummed object is multiplication by x/(1+e^{−x}). But it means the operator in Sec. II is never defined on a stated domain.

## 3. Charitable readings considered
- **v6 is explicitly hedged** on RH. The audit therefore does **not** say the paper claims a proof of RH. The verified error concerns the asserted Stage-II statement: a self-adjoint similarity transform exists on a domain defined by (17) and matched to Ψ_s(0)=0, with only real eigenvalues as a consequence.
- **Different ω′ for other W.** One might say the weight (18) was chosen specifically for ζ, and a different weight could be chosen for W_DH. This does not rescue the argument. The self-adjointness steps do not use any property of the specific weight beyond (14)–(15). Moreover F3 shows that, for ζ itself, (18) is not a Hilbert-space Gram kernel.
- **Prefactor zeros.** Excluding the prefactor zeros could be read as the paper focusing on ζ zeros. But an operator's spectrum cannot be pruned by fiat; doing so requires restricting to an invariant subspace (a compression). The author's own 2026 version does exactly that, and then finds that self-adjointness on that subspace is *equivalent* to RH.
- **Dirichlet-domain density.** Feldmann's (unrefereed) density obstruction for the follow-up applies in spirit here too. Ψ(0) = ⟨S†δ₀, φ⟩ becomes a continuous functional after the transform, because t^N is smoothing. This was not independently re-derived in this audit and is listed as context only.

## 4. Verdict
- **Classification: verified_error.** The claim is that a self-adjoint similarity transform exists on the domain (17), which is said to match the Dirichlet condition, and that its eigenvalues are therefore real.
- **Explicit witnesses:**
  - (i) the negative-norm vector, <U|U> = −0.0231, against weight (18);
  - (ii) the spurious (17)-solution s* = 1/2+3.70362i with ζ(s*) ≠ 0;
  - (iii) the non-real Dirichlet eigenvalue 9.0647−0.5i at s₁ = 1+2πi/log 2, with Ψ_{s₁} ∈ L²;
  - (iv) the Davenport–Heilbronn reductio at ρ_DH = 0.808517+85.699348i.
- **Stage I** is correct only formally. Its sentence "can only be satisfied by ζ(s)=0" needs the excluded prefactor zeros. The operator-theoretic meaning of "eigenvalue" is missing (F1).
- **RH status:** not proved by this paper. The author's latest follow-up (2408.15135 v17) is an RH-equivalent reformulation, a Weil–Bombieri-type positivity, not a proof.
- **Adjudication:** recommended (Level 3) before any public wording, per methodology §6(i)/(iv). The witnesses are reproducible from the listed scripts.

## 5. Not done / limits
- The IOP typeset version and the referee reports were not read.
- Eqs. (6)–(8), the su(1,1) algebra, were not re-derived; no witness depends on them.
- The Feldmann note was read only at abstract and grep level.
- Every DH/ζ value was computed at 25–40 digits with mpmath. These are not certified interval computations. The off-line DH zero itself is classical (Spira; Bombieri–Ghosh).


## Independent adjudication

**Rationale.** The paper does not claim to prove RH. Its v6/J. Phys. A Discussion says the argument is formal and that "the second stage requires further rigorous treatment". It does, however, assert the following unconditionally:
- Abstract: "we establish the existence of a similarity transformation ... that is self-adjoint on the domain specified by an appropriate boundary condition".
- Sec. II: "Thus, there exist a similarity transformation ... self-adjoint on the domain specified by the condition (17)", which "hence admits only real eigenvalues".
- Sec. II: condition (17) "corresponds to" Psi_s(0)=0.

I wrote my own code, independent of the auditor's scripts, and checked each assertion. All four auditor witnesses reproduce, and I found a fifth that stays inside the paper's own zeta setting.

(1) **Condition (17) fails inside the zeta setting itself.** For the paper's eigenfunctions u'=z^{s-1} with weight (18), substitution gives (1/u')∫ω'u'dy = G(s) := F(s)+F(1-s), where F = Γη, exactly, for 0<Re s<1. G has a zero off the critical line at s0 = 0.88106174137852 + 63.45282508476655i, certified with Arb ball arithmetic and Rouché's theorem on |s-s0| = 1e-10. At s0, ζ(s0) = 2.5645-0.7873i ≠ 0. So z^{s0-1} satisfies (17) identically, with the non-real eigenvalue E = 63.45282508 - 0.38106174i.

(2) **The weight (18) is indefinite.** The test vector u'(z) = z^{-1/2+4.8i}exp(-(ln z)^2/18) gives <U|U> = -0.0231346. A direct 2-D quadrature and the spectral formula agree to 8 digits. The matching ℓ² vector has norm² 2.937e-5. So (18) cannot be S'†S' for any S' whose domain contains U, for example any bounded S'. The paper's own Appendix-B normalisation Re F'(ρ) is also sign-indefinite: -3.35e-10 at ρ1 and +2.31e-14 at ρ2.

(3) **(17) is not the Dirichlet condition.** At s* = 1/2+3.70362373148i, (17) holds but ζ(s*) ≠ 0.

(4) **Davenport-Heilbronn control.** The same argument, with a positive analytic W_DH, would force the known off-line zero 0.808517182456637+85.699348485378i onto the critical line, which is false.

The argument therefore fails, not merely lacks rigour. It treats z^{s0-1} (or a hypothetical off-line zeta zero) exactly as it treats on-line zeros. If its domain contains them, a self-adjoint operator would have non-real eigenvalues, which is impossible. If its domain excludes them, the argument says nothing about RH.

**Charitable defenses I considered.**
- The hedge, the "we assume" wording at the start of Sec. II, and the fact that the paper is a physics paper: none of these removes the unconditional "Thus, there exist" and "establish". The published abstract, checked on the IOP landing page, matches v6. No erratum exists.
- The paper explicitly excludes the prefactor zeros s_k = 1+2πik/log 2. So the auditor's Stage-I finding (F2) is downgraded to missing_hypothesis. Under the paper's own construction those points do give L² Dirichlet eigenfunctions with non-real eigenvalues.
- The divergent Eq. (9) series is a suspected gap.
- The empty point spectrum on S(Dom D) is an unresolved ambiguity about which extended operator is meant.

**Author's own revisions.** These are reported separately from the Observatory findings. 2408.15135 v17 lists the prefactor zeros in the point spectrum. It reduces the claim to an operator positivity that is equivalent to RH.

**Public wording.** Public characterization is allowed under methodology §6, because the witnesses are explicit and were verified independently. It must be scoped to the Stage-II self-adjointness/real-eigenvalue assertion. It must not say the paper claimed a proof of RH.

# L3 adjudication: F1-yakaboylu, "Hamiltonian for the Hilbert–Pólya Conjecture"

## 0. Identification and versions (re-checked)
- **Paper:** arXiv:2309.00405, v1 (1 Sep 2023) to v6 (21 Jun 2024). The arXiv API reports v6 as current, with journal_ref *J. Phys. A: Math. Theor.* **57** 235204 (2024), DOI 10.1088/1751-8121/ad4c2d.
- **IOP landing page:**
  - received 18 Feb 2024, accepted 15 May 2024, published 4 Jun 2024;
  - single-anonymous review, 2 revisions;
  - the published abstract is word-for-word the v6 abstract;
  - the full typeset text is paywalled and was not read.
- **Abstract evolution (fetched from arXiv abs pages):**
  - v1 was "heuristic" in tone.
  - v3 was stronger: "It is shown that the Hamiltonian is self-adjoint on the domain of a weighted Hilbert space ... thereby ensuring that its every eigenvalue is real."
  - v6/J. Phys. A: "we establish the existence of a similarity transformation ... that is self-adjoint on the domain specified by an appropriate boundary condition".
- **Follow-up:** arXiv:2408.15135 v17 (18 Aug 2026). From its API abstract:
  - the point spectrum explicitly includes the prefactor zeros Z_p;
  - after compressing to the zeta spectral subspace, an intertwiner W is obtained "whose positivity is equivalent to the Riemann Hypothesis".
  - This is the **author's own revision**, reported separately from Observatory findings.
- No erratum or published comment on the J. Phys. A article was found.

## 1. What is claimed (v6 text, re-read)
- **Stage I (Sec. I).**
  - H = S D S^{-1}, with D = (xp+px)/2 and S = t^N e^{αx}/(1+e^x).
  - Ψ_s = Sφ_s, with φ_s = x^{s-1}/√(2π).
  - Ψ_s(0) ∝ (1-2^{1-s})Γ(s)ζ(s) (Eq. 3).
  - "The Dirichlet boundary condition can only be satisfied by the vanishing of the Riemann zeta function". The introduction has already excluded the zeros of (1-2^{1-s}).
- **Stage II (Sec. II).**
  - The section opens with "Now, we **assume** the existence of a similarity transformation ...".
  - A Mellin-space weight ω' is introduced, with (14) symmetry and (15) homogeneity.
  - Integration by parts gives <V|H'U> = BT + <U|H'V>*.
  - Under the ratio condition (17), "Dom H' = Dom H'*" and H' "becomes self-adjoint on the domain specified by the condition (17), and hence admits only real eigenvalues".
  - With ω' = (1/z)/(1+e^{y/z}) + (1/y)/(1+e^{z/y}) (Eq. 18), "(17) corresponds to the boundary condition Ψ_s(0)=0 for the eigenfunctions g'_s(z) = g0(s) z^{s-1}".
  - Conclusion: "**Thus, there exist a similarity transformation** ... self-adjoint on the domain specified by the condition (17)".
- **Hedge (Discussion).** "If the formal argument presented in this manuscript can be rigorously established, our approach holds the potential to imply the validity of the RH. It is important to note that the second stage requires further rigorous treatment."
- **What this adds up to:**
  - RH is **not** claimed as proved.
  - The existence of the self-adjoint similarity transform, and the reality of the eigenvalues on the (17)-domain, **are** asserted.
  - The W-generalisation sentence in the Discussion is literally conditional ("if there exists ...").

## 2. Strongest defense of the paper
1. **Formal framing.** The author flags Stage II as formal and needing rigour. Sec. II opens with "we assume". A physicist's reading takes ω' as an ansatz for a metric, as in pseudo-Hermitian quantum mechanics.
   - *Assessment:* this explains the tone, but not the unconditional "Thus, there exist" and "establish". More importantly, a pseudo-Hermitian metric gives a real spectrum only if it is **positive**. With an indefinite metric (a Krein space), non-real eigenvalues are allowed. So the hedge "can be rigorously established" cannot be met by the argument as written (see §3).
2. **Prefactor zeros.** The introduction explicitly sets aside the points where 1-2^{1-s}=0. Read this way, the Stage-I sentence is correct.
   - *Assessment:* accepted. The auditor's F2 is downgraded from verified_error to **missing_hypothesis**. Excluding them by convention does not restrict the operator's domain. Under the paper's own construction those points give L² Dirichlet eigenfunctions with non-real eigenvalues (§3.6). The author's 2026 follow-up puts them in σ_p.
3. **Generalised eigenfunctions.** Physics papers routinely use non-L² eigenfunctions such as x^{s-1}.
   - *Assessment:* fair for D. But then "eigenvalue selected by a boundary condition" needs an operator and domain specified, and the paper gives none. On the natural domain S(Dom D), H has empty point spectrum, because S is bounded and injective and D has purely absolutely continuous spectrum. This is an **unresolved_ambiguity**, not by itself an error.
4. **Short repair.** Could a different, positive weight satisfying (14)–(15) be chosen so that (17) holds exactly at zeta zeros?
   - *Assessment:* no repair is available within the paper's argument. The reality step needs 0 < <u|u> < ∞ for the eigenvector. Every eigenfunction z^{s-1} has ω'-"norm" of the form 0·∞ or ∞. Appendix B obtains a finite value only by writing z^{ρ*+ρ-2} = z^{2ε-1}, which assumes Re ρ = 1/2, so it is circular. A positivity that does the job is RH-equivalent, which the author's own v17 states.

## 3. Independent verification of the witnesses
All code is my own, written in a separate directory and not taken from the auditor's scripts. Tools: mpmath 1.3 (25–40 digits, non-rigorous high precision), numpy/scipy, and python-flint 0.9 (Arb ball arithmetic, used for the certified witness in §3.1).

Scripts are in `/tmp/claude-0/-home-user-riemann/e62aa4cb-6226-5e37-8f52-ea0fa055746f/scratchpad/l3_yakaboylu/`:
- `a_kernel_sign.py`
- `b_negative_vector.py`
- `c_condition17.py`
- `c2_offline.py`
- `c4_bisect.py`
- `d_dh_and_stage1.py`
- `e_certify.py`
- `f_misc.py`

### 3.0 The key identity (derived analytically, then checked numerically)
- For u'(z) = z^{s-1} and ω'_W(z,y) = W(y/z)/z + W(z/y)/y, with 0 < Re s < 1:
  - substituting y = zx in the first term gives z^{s-1}M[W](s);
  - substituting y = z/x in the second term gives z^{s-1}M[W](1-s).
- Hence (1/u')∫ω'_W u' dy = M[W](s) + M[W](1-s) =: G_W(s), independent of z.
- For W = 1/(1+e^x), M[W] = F = Γη, which is the paper's F in Appendix B.
- Quadrature checks:
  - s = 0.3+2i and s = 0.7+5.5i, at z = 0.5 and z = 3, agree to about 1e-11;
  - the Davenport–Heilbronn analogue at s = 0.4+2.5i agrees to 12 digits.

### 3.1 New witness (adjudicator): an off-critical-line solution of (17) in the paper's own zeta setting
- **Argument-principle counts of zeros of G = F(s)+F(1-s)** in 0.02 < σ < 0.98:

  | t range | zeros of G (argument principle) | sign changes of Re F on the line |
  |---|---|---|
  | [1, 30] | 19 | 19 |
  | [30, 60] | 30 | 30 |
  | [60, 90] | **37** | 35 |

- **Locating the extra zeros.**
  - Bisecting rectangles in σ ∈ [0.51, 0.98] isolates one zero.
  - Newton refinement gives **s0 = 0.88106174137852107 + 63.45282508476655i**.
  - Its mirror 1 - s̄0 is the second zero.
- **Certification (`e_certify.py`).** Arb ball arithmetic at 256 bits covers the circle |s-s0| = 1e-10 with 4000 balls. The Rouché comparison with c·(s-s0) passes, with worst ratio |G-L|/|L| ≤ 0.047. So there is **exactly one zero of G with |s-s0| < 1e-10**, and therefore Re s ≈ 0.8811 ≠ 1/2.
- At s0, ζ(s0) = 2.5645 − 0.7873i (Arb), which is nonzero. The zero lies near the prefactor point 1 + 2π·7i/log 2 = 1 + 63.4530i, where F is small.
- **Consequence.** The paper's Mellin-space eigenfunction g'_{s0}(z) = z^{s0-1} satisfies condition (17) identically, since the ratio is G(s0) = 0 for every z. Its eigenvalue is E = i(1/2 − s0) = **63.45282508 − 0.38106174 i**, which is non-real. This contradicts "self-adjoint on the domain specified by the condition (17), and hence admits only real eigenvalues".
- **The dilemma.** z^{s0-1} has exactly the same type as z^{ρ-1} for any hypothetical off-line zeta zero ρ: a power function with Re ≠ 1/2, satisfying (17), with ω'-norm of the form 0·∞.
  - If the (17)-domain contains such functions, it contains a non-real eigenvalue.
  - If some extra requirement excludes them, it also excludes hypothetical off-line zeta zeros, and the argument says nothing about RH.
  - Either way, the Stage-II inference is invalid. This is a zeta-internal analogue of the Davenport–Heilbronn reductio.

### 3.2 Indefinite weight (auditor W1, reproduced)
- **Reduction.** With z = e^a and y = e^b, the quadratic form becomes ∫∫k(b−a)φ*(b)φ(a), whose Fourier symbol is 2Re F(1/2+iτ).
- **Sign changes.** 2Re F(1/2+iτ) is 2.1443 at τ=0, **−0.004682** at τ=4, −0.003424 at τ=5 and +1.40e−4 at τ=7.
- **Test vector:** u'(z) = z^{−1/2+4.8i}exp(−(ln z)²/18).

  | Case | Direct 2-D quadrature | Spectral formula |
  |---|---|---|
  | L = 3 | **−0.02313457** | −0.023134574 |
  | L = 6 | −0.04702794 | −0.047027944 |
  | Positive control (τ0 = 2) | +0.99665066 | +0.99665066 |

- **Legitimate state.** The paper's ℓ² state U0 = Σ(u_n/n!)|n> has ||U0||² = 2.937e−5 (finite).
- **Fubini.** For bounded S', the Fubini/interchange step behind (22) is justified for this U0: |u(y)|/y is integrable and Σ_k y^{k−1}/k! ≤ e^y/y. So <U0|S'†S'|U0> ≥ 0 would equal the negative form. Hence **no bounded S'** has (18) as its weight, and "there exist a similarity transformation" with weight (18) is false.
- **Inside the paper's own Appendix B.** The normalisation <Ψ'_ρ|Ψ'_ρ> = |g0|²Re F'(ρ) changes sign across zeros. Re F'(ρ) is −3.348e−10 at ρ1, +2.307e−14 at ρ2, −6.46e−18 at ρ3 and −4.24e−21 at ρ4. These values are from mpmath, cross-checked against F'(ρ) = Γ(ρ)(1−2^{1−ρ})ζ'(ρ) in Arb; this check is not certified. So whatever sign convention is chosen, some eigenstates get a negative "norm".

### 3.3 (17) is not equivalent to Dirichlet (auditor W2, reproduced)
- **Roots of 2Re F(1/2+iτ) in (0,30):** 3.70362373, 6.12406997, 8.54642622, 9.24104065, 9.33466431, 11.668675, 13.4473021, **14.1347251**, 15.157541, 16.891941, 19.6791279, **21.0220396**, 21.2802071, 22.8090222, 24.3160156, **25.0108576**, 25.8556447, 28.3633255, 29.8664018.
- Only the bold values are zeta ordinates.
- **Witness s* = 1/2 + 3.70362373148154i:**
  - |ζ(s*)| = 0.585484 and F(s*) = 0.0101206i, so the Dirichlet condition fails;
  - direct quadrature of (17) gives about 1e−18 at z = 1 and z = 7, so (17) holds.
- **Direction of the equivalence.** Dirichlet ⇒ (17) holds at genuine zeta zeros, by the functional equation. The converse fails on the line (§3.3) and off it (§3.1).

### 3.4 Davenport–Heilbronn control (auditor W4, reproduced)
- **The function.**
  - ξ = 0.2840790438404123.
  - W_DH = q(1−q)(1+(1+ξ)q+q²)/(1−q⁵) with q = e^{−x}; it matches the Dirichlet series.
  - It is positive and analytic, with W(0+) = (3+ξ)/5 = 0.6568158088.
  - Its Mellin transform equals Γ(s)f(s) to 15 digits.
  - Λ(s) = (π/5)^{−(s+1)/2}Γ((s+1)/2)f(s) satisfies Λ(s) = Λ(1−s) to 12 digits at two test points.
- **The zero.**
  - ρ_DH = 0.808517182456637386 + 85.6993484853775922i;
  - |f(ρ)| = 5.2e−41 and |f(1−ρ)| = 2.6e−39;
  - control value |f(1.3+85.7i)| = 0.49;
  - G_W(ρ)/|Γ(ρ)| = 2.1e−40.
- **Conclusion.** Both the Dirichlet condition and (17) hold, but E = 85.69934849 − 0.30851718i. The Sec. II steps use only (14), (15) and (17). These hold for ω'_W because it is real, symmetric and homogeneous of degree −1. So the argument would "prove" a falsehood.

### 3.5 Bernoulli/Borel step (Level-1/auditor F7, reproduced)
- c_m = B_m(2^m−1)/m! with B1 = +½ matches the series of x/(1+e^{−x}) (sympy, m ≤ 11).
- g_n = Γ(n+ρ)(1−η(n+ρ)) was checked by quadrature.
- |c_m g_m| at ρ1 is 2.05e−9 (m=2), 4.54e−3 (m=16), 2.40e2 (m=24), 9.12e7 (m=32) and 3.75e32 (m=60). The Eq. (9) component series diverges factorially.
- The paper's stated Borel region "Re x > 0, Im x < π" is not the Borel polygon, which is the strip |Im x| < π. This is minor.
- Classification: **suspected_gap**. The step is formal, and the resummed object is just multiplication by x/(1+e^{−x}).

### 3.6 Stage I prefactor points (auditor W3, reproduced, but reclassified)
- s1 = 1 + 9.06472028365i, with ζ(s1) = 1.3465802 + 0.1098834i.
- Γη(s1) is about 5e−36 in mpmath, and direct quadrature of ∫z^{s1−1}/(1+e^z) gives about 3e−35.
- For t = (1−√5)/2 (the paper's β=1 choice, so α = 0.1180340):
  - the Hille–Hardy closed form is verified against the Laguerre series to 14 digits;
  - it gives |Ψ_s(x)| ≤ e^{−αx}Γ(σ)η(σ)/(1−t), so Ψ_{s1} ∈ L²;
  - numerically, Ψ_{s1}(0) is about 2e−35, while Ψ_{s1}(x) is of order 1e−6 to 1e−5 for x > 0.
- So the Dirichlet eigenvalue 9.0647 − 0.5i is non-real.
- Because the paper explicitly excludes these points, I classify this as **missing_hypothesis**. The exclusion is a convention, not a domain restriction. The author's own follow-up later includes these points in σ_p.

## 4. Component verdicts

| Component | Classification |
|---|---|
| Stage II: self-adjoint similarity transform on the (17)-domain, hence real eigenvalues; "(17) corresponds to Ψ_s(0)=0"; weight (18) as an inner product | **verified_error** (witnesses §3.1–§3.4) |
| Stage I: "only by ζ(s)=0" | missing_hypothesis (prefactor zeros excluded only by convention; L² non-real Dirichlet eigenvalues exist) |
| Operator and domain for "eigenvalues" of non-L² φ_s; empty σ_p on S(Dom D) | unresolved_ambiguity |
| Eq. (9) / Borel step | suspected_gap |
| Appendix B normalisation | assumes Re ρ = 1/2 (circular); sign-indefinite even in the paper's own regularisation |
| Discussion "broader class" sentence | literally conditional; the Davenport–Heilbronn control shows the method cannot tell such a class apart |
| RH status | not proved; the paper does not claim it; the author's v17 follow-up is an RH-equivalent positivity reformulation |

## 5. Final decision
- **Classification:** `verified_error`. The Stage-II existence and reality claim of the published paper is incorrect as stated.
- **Witnesses:** explicit and independently re-derived. The strongest is the certified off-line zero s0 = 0.8810617414 + 63.4528250848i of F(s)+F(1−s) in §3.1. Through the paper's own eigenfunction z^{s0−1}, it satisfies condition (17) with the non-real eigenvalue 63.45282508 − 0.38106174i.
- **Public characterization:** allowed, with this scope. Suggested wording:

> "The paper's Stage-II argument (Sec. II, Eqs. 13–18) does not establish a self-adjoint similarity transform with real spectrum. The proposed weight (18) is indefinite, and the boundary condition (17) admits eigenfunctions with non-real eigenvalues (for example s ≈ 0.8811+63.4528i, where ζ ≠ 0). The identical argument would also place an off-line Davenport–Heilbronn zero on the critical line. The paper does not claim a proof of RH, and the author's later work (arXiv:2408.15135 v17) reformulates the remaining step as a positivity condition equivalent to RH."

- **Wording to avoid:** do not say the paper "claimed to prove RH". The prefactor-zero issue must not be presented as an error of the Stage-I sentence.

## 6. Limits
- The IOP typeset text and the referee reports were not read. The abstract matches v6.
- The su(1,1) reduction (Eqs. 6–8) was not re-derived; no witness depends on it.
- All values except the Arb/Rouché certificate in §3.1 are non-rigorous high precision. The Davenport–Heilbronn off-line zero is also classical (Spira; Balanzario–Sánchez-Ortiz).
- The identity in §3.0 is proved by an elementary substitution, valid for 0 < Re s < 1, so it covers s0.
- The Feldmann Zenodo note on the follow-up was not re-examined.
