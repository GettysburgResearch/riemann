# Quasi-RH research wave (10 October 2026)

```text
Status: EXPLORATORY / IMPORTED (external theorems) / PROPOSED (new statements)
Scope: global for the imported zero-free half-planes; conditional/proposed for everything derived here
Exact sources or dependencies: see "Sources" below (frozen copies of the four external manuscripts were read in full extract; nothing in this directory is a repository-reviewed theorem)
What was actually run: reading of the primary manuscripts; a Python reconstruction of the Part II exponent system (scripts/); literature search; repo hypothesis audit
Smallest remaining gap: a single new moment or large-sieve input that moves the 11/12 - ell/4 comparison below Liu's 0.874957 (see FINDINGS.md)
```

**RH remains open.** Nothing in this directory proves or disproves RH, and nothing here is integrated. This is a three-hour reconnaissance wave on the October 2026 external development: a *uniform zero-free half-plane* for all Dirichlet $L$-functions and all finite-order Hecke $L$-functions over $\mathbb Q(\sqrt{-3})$.

## Sources (external, not reviewed here)

| Source | Statement | Status as read |
|---|---|---|
| OpenAI, *The Quasi-Riemann Hypothesis: a zero-free half-plane $\Re s>7/8$*, 30 Sept 2026 (`github.com/openai/math`, `preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/paper.pdf`, 199 pp.) | Theorem 1.1: every finite-order Hecke $L$-function over $F=\mathbb Q(\sqrt{-3})$ and every Dirichlet $L$-function (including $\zeta$) has no zero in $\Re s>7/8$; principal pole allowed. Corollary 1.2: least quadratic nonresidue $n(p)\le C(\log p)^A$ and deterministic polynomial-time square roots mod $p$. | Main 7/8 statements for $\zeta$, Dirichlet and Hecke carry Lean comparator files (poles excluded in the formal statements). Not peer reviewed. |
| OpenAI, *The Quasi-Riemann Hypothesis*, 5 Oct 2026 (`.../October-5-2026/paper2.pdf`, 49 pp.) | Theorem 1.1: $\Re s>11/12$ zero-free, same families, by a different recursive mean-square (Möbius-sum power-saving) argument. Corollary 1.2: $\sup_{q\le x}|\pi(x;q,a)-\mathrm{li}(x)/\varphi(q)|\ll x^{11/12}\log x$. | Human-edited for readability. |
| OpenAI, *Uniform exclusion of Landau–Siegel zeros*, 1 Oct 2026 (9 pp.) | Theorem 1: absolute $c>0$ with $(1-\beta)\log q\ge c$ for every real zero $\beta$ of a primitive nonprincipal real Dirichlet $L$-function. | **Independent algebraic argument** (interpolation determinants on a biquadratic field; Laurent/Bost-type), not a corollary of 7/8. Lean comparator exists; no explicit $c$. |
| B. Liu, *Slightly improved zero-free half-planes for the quasi-Riemann hypothesis*, arXiv:2610.12234 (8 Oct 2026) | Re-optimizes the two length parameters $(b,\ell)=(1/8,1/6)$ of the 7/8 proof: $B_r=34999/40000$ and $B_{\rm new}=(1507-2\sqrt{921})/1653\approx0.874957$. Expected optimal for that estimate system with $\kappa\in[3/4,1]$. | Lean formalizations claimed in the author's repository. |
| S. Kintali, *A short proof of the quasi-Riemann hypothesis*, 7 Oct 2026 (personal site) | $\Re s>47/48$ via cubic theta reflection + quadratic large sieve + a general Hecke zero-density estimate (row count $U^{5(1-a)}$). | Weaker bound; useful as the simplest instance of the architecture. |

## The architecture in one paragraph

Fix a primitive finite-order Hecke character $\eta$ over $F$ and let $\beta_*$ be the supremum of real parts of zeros over the **whole** primitive family. A completed cubic-theta sum (coefficients: cubic Gauss sums; Kubota–Patterson theta via Dunn–Radziwiłł's unconditional expansions) is averaged against sextic residue characters and $\eta$. Two exact representations: (i) cubic reflection + quadratic Hecke large sieve gives the *low* bound $|J_\eta(Z)|\ll Z^{l_x/2+b/12+\epsilon}$; (ii) Poisson summation gives a *principal* row equal to a Mellin integral of $Z^{C(s)}e^{(s-5/6)^2}H_\eta(s)/L_F^S(s,\eta)$ with $C_b(s)=s-(4+b)/6$, plus nonprincipal rows $u\ne1$ carrying twists $\eta\chi_\bullet(u)$ that are controlled by a zero detector (a truncated-inverse polynomial and a plain polynomial are simultaneously large when a twist has a zero of real part $a$), the sextic large sieve, and two moment estimates (Lemma 17.1 inverse second moment, Lemma 18.1 fourth moment, the latter for $\kappa=2\beta_*-1\in[3/4,1]$). A power saving in both comparisons continues $1/L$ across the rightmost zero, contradicting the definition of $\beta_*$ (Proposition 2.1). With balanced scales $X=Z^{l_x},Y=Z^{l_y}$, $l_x=(1-b-\ell)/2$, $l_y=(1+b-\ell)/2$ and total selected-prime length $\ell$, matching the low exponent with the principal exponent gives

$$B(\ell)=\frac{11}{12}-\frac{\ell}{4},$$

so $\ell=0$ is Part I (11/12), $\ell=1/6$ is Part II (7/8), and $\ell\to2/3$ would be $3/4$. The constraint on $\ell$ is the nonprincipal exponent $E(d)<\Delta$ (eq. (20.4)) whose row-count input $R_*$ comes from the moments; this is where the real obstruction lives.

## Contents of this directory

- `README.md` — this hub.
- `FINDINGS.md` — synthesized findings of the wave (bottleneck model, bootstrap barrier, alternative architectures, repository consequences), with exact statements and the smallest remaining gaps.
- `notes/` — working notes: A (full exponent model and sensitivity), B (bootstrap/κ barrier), C (mechanism, alternative families, literature), D (unconditional consequences for this repository), E (lead reconstruction of the endpoint exponent), H (what a generalized 2k-th moment buys), and later wave-2 notes (F quartic feasibility, G 2k-moment lemma attack, I mixed-moment attack, J direct-side Gram loss) as produced.
- `scripts/` — the exponent-system reconstruction and any experiments (ordinary floating point; not certificates).

Nothing here changes `RESULTS.md`, `STATUS.md` or the integrated record. Any statement below marked PROPOSED needs its own exact-SHA review before it can be cited.
