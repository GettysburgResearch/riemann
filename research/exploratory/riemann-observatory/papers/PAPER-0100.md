# PAPER-0100 — On the average value of \(\pi (t)-\operatorname{li}(t)\)

| Field | Value |
|---|---|
| Authors | Johnston, Daniel R. |
| Year / stratum | 2023 / S6 |
| Venue | Can. Math. Bull. 66, No. 1, 185-195 (2023). |
| Identifiers | zbMATH [1525.11088](https://zbmath.org/?q=an:1525.11088) · DOI [10.4153/S0008439522000212](https://doi.org/10.4153/S0008439522000212) · arXiv [2201.06184](https://arxiv.org/abs/2201.06184) |
| MSC | 11M26, 11N05 |
| Families | C |
| Work type | original_paper |
| Evidence level of this record | **L1** |
| Full text | fulltext_read — https://arxiv.org/abs/2201.06184 |
| Selection | score 4.312, in-pool citations 5, seed lists 0, triage relevance 4 |

## Mathematical content (Level 1: full text read)

**Research question.** Is RH equivalent to negativity of the averaged error int_2^x (pi(t)-li(t))dt for ALL x>2 (Pintz 1991 claim made explicit)? Which unconditional weighted averages are negative, and how much extra weight is possible before zeros off the line force sign changes?

**Historical motivation.** Riemann 1859 remark pi(x)<li(x); Schmidt 1903; Littlewood 1914 sign changes; Pintz 1991 and others claimed average negativity (Ingham, Kaczorowski, Pintz) without explicit-range proof.

### Main results

- **THM-PAPER-0100-1** (Theorem 1.1, equivalence, scope: global; Sec.1; proof Sec.3). RH holds iff $\int_2^x(\pi(t)-\mathrm{li}(t))\,dt<0$ for all $x>2$.
- **THM-PAPER-0100-2** (Theorem 1.2, equivalence, scope: global; Sec.1; Sec.3). RH holds iff $\int_2^x(\theta(t)-t)\,dt<0$ for all $x>2$.
- **THM-PAPER-0100-3** (Theorem 1.3, unconditional theorem, scope: global; Sec.1; proof Sec.4). For all $x>2$: $\int_2^x\frac{\pi(t)-\mathrm{li}(t)}{t^2}dt<0$, $\int_2^x\frac{\theta(t)-t}{t^2}dt<0$, $\int_2^x\frac{\Pi(t)-\mathrm{li}(t)}{t^2}dt<0$, $\int_2^x\frac{\psi(t)-t}{t^2}dt<0$, with $\Pi(t)=\sum_{m\ge1}\pi(t^{1/m})/m$.
- **THM-PAPER-0100-4** (Theorem 1.4, Omega-result, scope: asymptotic; Sec.1; proof Sec.5). Let $\omega=\sup\{\Re s:\zeta(s)=0\}$. If $1/2<\omega\le1$ and $c<1+\omega\le2$, then each of $\int_2^x(\pi-\mathrm{li})t^{-c}dt$, $\int_2^x(\theta-t)t^{-c}dt$, $\int_2^x(\Pi-\mathrm{li})t^{-c}dt$, $\int_2^x(\psi-t)t^{-c}dt$ is $\Omega_+(1)$ (positive for arbitrarily large x). *Conditional on:* RH false (omega>1/2).
- **THM-PAPER-0100-5** (Lemma 2.8 (consequence), remark, scope: asymptotic; Sec.1 after Thm 1.3; Lemma 2.8). Since int_2^x (Pi-li) and int_2^x (psi-t) change sign infinitely often (Lemma 2.8, c=0, and Littlewood-type Omega_-), Theorems 1.1/1.2 fail for Pi and psi.

### Key definitions

- Pi(x)=sum_m pi(x^{1/m})/m
- omega=sup Re zeta zeros
- Omega_+(1): positive for arbitrarily large x

### Principal lemmas

- **THM-PAPER-0100-L1** (Lemma 2.1; Sec.2). For $2\le x\le10^{19}$, $\pi(x)<\mathrm{li}(x)$ and $\theta(x)<x$ (Buthe). — *Role:* Finite computational base; reduces RH case to x>10^19.
- **THM-PAPER-0100-L2** (Lemma 2.3; Sec.2). $\Pi(x)-1.9x^{1/2}<\pi(x)<\Pi(x)-x^{1/2}/\log x$ for $x\ge17$; $\psi(x)-1.5x^{1/2}<\theta(x)<\psi(x)-0.98x^{1/2}$ for $x\ge121$. — *Role:* Transfers between pi,theta and Pi,psi with explicit x^{1/2} gap that dominates in RH-true case.
- **THM-PAPER-0100-L3** (Lemma 2.6; Sec.2). Under RH, $\int_2^x(\psi(t)-t)dt\le0.08x^{3/2}$ for $x\ge3000$ (via explicit formula for psi_1 and sum_rho 1/|rho(rho+1)|=0.046209...). — *Role:* Controls the integrated psi error with explicit constant.
- **THM-PAPER-0100-L4** (Lemma 2.7; Sec.2). With $Q=\Pi-\mathrm{li}$, $R=\psi-x$, $R_1=\int_2^xR$: $Q(x)=R/\log x+R_1/(x\log^2x)+\int_{3000}^x(R_1/(t^2\log^2t)+2R_1/(t^2\log^3t))dt+C$, $C=-0.4351...$ — *Role:* Converts bounds on R_1 to bounds on Pi-li, then integrates again.
- **THM-PAPER-0100-L5** (Lemma 2.8; Sec.2). For $c<1+\omega\le2$ and $\delta>0$: $\int_2^x\Pi t^{-c}-\int_2^x \mathrm{li}\,t^{-c}=\Omega_\pm(x^{1+\omega-c-\delta})$, same for psi. — *Role:* Landau-type Omega argument via Mellin integral for log zeta(s) and -zeta'/zeta; drives the RH-false direction.

### Proof architecture

RH false: Lemma 2.8 (c=0) gives Pi integral > K x^kappa with kappa>3/2 infinitely often; Lemma 2.3 loses only O(x^{3/2}), so pi/theta integrals are positive. RH true: base x<=10^19 by Lemma 2.1; for x>10^19 use RH-conditional explicit bound R_1<=0.08 x^{3/2} (Lemma 2.6), Lemma 2.7 for Pi-li, and the -x^{1/2}/log x (resp. -0.98x^{1/2}) gap of Lemma 2.3 integrated to give a -0.57x^{3/2} (theta) or -0.58 x^{3/2}/log x (pi) term beating the positive error; small-range integrals computed in Mathematica (Lemma 2.5). Thm 1.3 via explicit Mertens (RS62 3.20, 3.23) and partial summation, no RH.

**Imported results.** Buthe 2018 Thm 2: pi<li, theta<x up to 10^19; Rosser-Schoenfeld 1962 explicit bounds (3.5),(3.6),(3.15),(3.16),(3.20),(3.23); Ingham Thm 27 (explicit formula); Brent-Platt-Trudgian 2021 Cor.1 (sum 1/(gamma(gamma+1)) bound); Benfatto et al Lemma 5.9 (li bound)

**Techniques.** explicit formula for integrated psi; Landau Omega-method / Mellin transform; explicit Rosser-Schoenfeld bounds; partial summation and integration by parts; finite computation (Buthe 10^19 verification)

## Context and interpretation

**Importance and obstacle overcome.** Removes the 'x>x0' ineffectiveness: gives a clean global equivalent of RH by combining computation to 10^19 with explicit RH-conditional estimates. Obstacle was making the claim fully explicit for all x. It is a restatement of RH, not progress toward proof.

**Relation to prior work.** Makes explicit Pintz 1991 (Acta Arith/Proc.) claim; extends Ingham-type average results; uses Buthe 2018 verification and Rosser-Schoenfeld bounds.

**Limitations and open questions.** Equivalence only; one direction depends on RH-conditional explicit bound with ad hoc constants and Mathematica integrals (not interval-certified). Weight 1/t^2 is not sharp; log t/t^2 left open (needs explicit zero-free region). Cannot go beyond c<1+omega without zero information.

## Research potential

- **Hypotheses that might be weakened.** The 10^19 base (Lemma 2.1) could be replaced by a larger verified range; the constants 0.08 and 0.046209 could be refined to test where margin is thinnest (x just above 10^19 is controlled by Lemma 2.1, so margin elsewhere is large: -0.57 x^{3/2}).
- **Generalizations.** Analogues for primes in arithmetic progressions (Chebyshev bias, Sec.6 suggests), number fields, and Dirichlet L GRH; weights f with explicit zero-free region such as log t/t^2.
- **Candidate connections.** Connects to Rubinstein-Sarnak logarithmic density bias: weight 1/t^2 (resp. 1/t^c) is a Cesaro-type smoothing; connects to Suzuki's screw-function positivity (CAND-01970) as another one-sided positivity equivalent.
- **Reusable lemmas.** Lemma 2.3 (pi vs Pi, theta vs psi explicit gaps), Lemma 2.7 (integrated representation of Pi-li), Lemma 2.8 (Omega result for weighted integrals).
- **Possible experiments.** Numerically compute min over x of -int_2^x(pi-li)dt / x^{3/2} up to 10^13 to see actual margin; test the 1/t^c weights near c=3/2 to see where sign changes first appear in the first Skewes-region zones.
- **Risks / barriers.** Equivalence adds no new constraint on zeros; any proof of the RH-true inequality would itself prove RH (circular). Dependence on a finite verification means any improvement is about computation, not method.

## Audit notes (Level 1 reader)

Minor: Sec.3 RH-true chain relies on Mathematica numeric values (Lemma 2.5, constants 370, 14000, 19000) without interval certification; (3.6) constant 0.9 and (3.3) 0.96 use monotonicity claims stated tersely. Statement of Thm 1.4 for c with 3/2<c<1+omega depends on delta choice; text of proof handles this. None else noticed in inspected portion.

*These notes are a reader's observations, not verified findings; see `audits/` for adjudicated findings.*

## Provenance

- Candidate `CAND-01969`; harvest queries: kw_RH_any, msc_11M26, msc_11N05, arxiv_rh_abs.
- Triage decision: include — New equivalent of RH via integral of pi(t)-li(t).
- Record generated by `tools/make_records.py`; search cutoff 2026-11-17.
