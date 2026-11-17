# PAPER-0069 — The eighth moment of the Riemann zeta function

| Field | Value |
|---|---|
| Authors | Ng, Nathan; Shen, Quanli; Wong, Peng-Jie |
| Year / stratum | 2026 / S7 |
| Venue | J. Eur. Math. Soc. (JEMS) 28, No. 10, 4175-4237 (2026) |
| Identifiers | DOI [10.4171/jems/1568](https://doi.org/10.4171/jems/1568) · arXiv [2204.13891](https://arxiv.org/abs/2204.13891) |
| MSC | 11M06, 11M41, 11M50 |
| Families | A, B |
| Work type | original_paper |
| Evidence level of this record | **L1-partial** |
| Full text | partial_fulltext — arxiv.org/abs/2204.13891 |
| Selection | score 4.4981, in-pool citations 2, seed lists 0, triage relevance 4 |

## Mathematical content (Level 1: full text read)

**Research question.** Prove an asymptotic formula for the eighth moment I_4(T)=int_0^T |zeta(1/2+it)|^8 dt, conditional on RH and a quaternary additive divisor conjecture, extending Ng's sixth moment method.

**Historical motivation.** Keating-Snaith random-matrix conjecture for moments; Conrey-Gonek heuristic for k=3,4; Ng's conditional sixth moment; Ivic's work that the averaged quaternary additive divisor conjecture implies I_4(T)<<T^{1+eps}.

### Main results

- **THM-PAPER-0069-1** (Theorem 1.1, theorem, scope: conditional; Sec. 1, eq. (1.13)). Assume RH and Conjecture 1. Then $I_4(T)\sim\frac{24024\,a_4}{16!}\,T(\log T)^{16}$ as $T\to\infty$, with $a_4=\prod_p(1-1/p)^{16}\sum_{m\ge0}\binom{m+3}{m}^2p^{-m}$ (k=4 case of (1.5)). *Conditional on:* RH, Conjecture 1 (quaternary additive divisor conjecture).
- **THM-PAPER-0069-2** (Conjecture 1, conjecture, scope: conditional; Sec. 1, eq. (1.12); derived heuristically in Appendix 1 (Sec. 9)). There is C>0 such that for any eps_0,eps'>0, P>1, X,Y>1/2 with Y≍X, f smooth with supp in [X,2X]x[Y,2Y] and $x^my^nf^{(m,n)}\ll_{m,n}P^{m+n}$, for X sufficiently large and $1\le|r|\ll X^{1-\epsilon'}$: $D_{f;4,4}(r)=\frac1{(2\pi i)^2}\iint_{B_1\times B_2}\zeta^4(z_1)\zeta^4(z_2)\sum_{q\ge1}\frac{c_q(r)G_4(z_1,q)G_4(z_2,q)}{q^{z_1+z_2}}\int_0^\infty f(x,x-r)x^{z_1-1}(x-r)^{z_2-1}dx\,dz_2dz_1+O(P^CX^{1/2+\epsilon_0})$, where $D_{f;4,4}(r)=\sum_{m-n=r}\tau_4(m)\tau_4(n)f(m,n)$. *Conditional on:* is a conjecture (no numerical confirmation exists per authors).
- **THM-PAPER-0069-3** (Theorem 1.2 (from companion article [26]), theorem (imported), scope: conditional; Sec. 1, (1.14); proved in Ng-Shen-Wong [26] (not here)). Assume RH, k>=12, T large, $|t_0|\le0.5T$. Then $\int_0^T|\zeta(\tfrac12+it+it_0)|^k|\zeta(\tfrac12+it-it_0)|^k\,dt\ll_kT(\log T)^{k^2/2}G(T,t_0)^{k^2/2}$ with $G=\min\{1,\log T/|2t_0|\}$ for $|t_0|\le1/200$ and $\log(2+|2t_0|)$-type for larger (as printed in the paper). *Conditional on:* RH.
- **THM-PAPER-0069-4** (Prop 3.1, proposition, scope: asymptotic; Sec. 3). Under RH, for any eps>0 and T>=T_eps, $I_\omega-\tilde I_\omega=O(\epsilon T(\log T)^{16})$ with implied constant independent of eps, where $\tilde I_\omega$ uses the truncated Vt~ with U=T^{1-eps}. *Conditional on:* RH.
- **THM-PAPER-0069-5** (Prop 3.2, proposition, scope: asymptotic; Sec. 3). Unconditionally $I_D=\frac{4a_4(\log U)^{16}}{638512875}\int\omega(t)dt+O(T(\log T)^{15})$ (diagonal terms).
- **THM-PAPER-0069-6** (Prop 3.3, proposition, scope: conditional; Sec. 3, eq. (3.9)). Assuming Conjecture 1, $I_O=-\frac{13381a_4}{2615348736000}\int\omega(t)(\log T)^{16}dt+O(\epsilon T(\log T)^{16})+O(T(T/T_0)^{1+C})$ (off-diagonal). Together: $I_\omega=a_4\frac{24024}{16!}\int\omega(t)(\log T)^{16}dt+O(\epsilon T(\log T)^{16})+O(T(T/T_0)^{1+C})$ (3.9). *Conditional on:* Conjecture 1.
- **THM-PAPER-0069-7** (Prop 2.1, proposition, scope: asymptotic; Sec. 2, (2.2)). Approximate functional equation: for G entire with |G(s)|<<exp(-c|t|), $|\zeta(\tfrac12+it)|^8=2\sum_{m,n}\frac{\tau_4(m)\tau_4(n)}{(mn)^{1/2}}(m/n)^{-it}V_t(\pi^4mn)+O((1+|t|)^{-B})$.

### Key definitions

- I_k(T)=int_0^T|zeta(1/2+it)|^{2k}dt
- D_{f;k,l}(r)=sum_{m-n=r} tau_k(m)tau_l(n) f(m,n)
- G_k(s,n) (1.11), g_k(s,n) Definition 1
- U=T^{1-eps}, I_omega smoothed moment

### Principal lemmas

- **THM-PAPER-0069-L1** (Prop 6.1; Sec. 6). For M,N >> T_0^{1-eps_1}, M≍N, MN<<U^{4+eps_2}: $I_{M,N}=\frac{2T}{\sqrt{?}}\sum_{r\neq0}D_{f_r}(r)+O(T^{-B})$ with f_r given by (6.6) a smooth weight built from W(x/M)W(y/N), G(s), g(s,t), (1+r/y)^{-it}, (U/t)^{4s}. — *Role:* Reduces the off-diagonal to quaternary additive divisor sums D_{f;4,4}(r) so that Conjecture 1 can be applied.
- **THM-PAPER-0069-L2** (Lemma 2.2; Sec. 2). (i) $g(s,t)=(t/2)^{4s}(1+O((|s|^2+1)/t))$; (ii) derivative bounds $\ll |s|^iT^{4\epsilon_0-i}$; (iii) $\tilde V_t(x)=O((U^4/x)^A)$ for $x>U^4$. — *Role:* Truncation lemma allowing mn<<U^{4+eps} with U=T^{1-eps}.
- **THM-PAPER-0069-L3** (Lemma 6.3 / Prop 6.4; Secs. 6.3-6.9, 7). Evaluation of the main-term integrals after applying Conjecture 1, for |u_i|<delta'; moving contours to Re(s)=eps_3, 0<delta<eps_3<0.15. — *Role:* Executes the contour shifts and bounds the secondary terms of the off-diagonal.
- **THM-PAPER-0069-L4** (Lemma 8.1; Sec. 8). For z in C: $G_k(s,p^j)\approx\tau_k(p^j)-p^{s-1}\tau_k(p^{j-1})$ near s=1 (precise statement in Lemma 8.1). — *Role:* Arithmetic factor in the off-diagonal main term.
- **THM-PAPER-0069-L5** (Lemma 8.2-8.4; Sec. 8). Bounds for G_{s,t}(1,1) and H_s(1,1) arising in the singular-series residue computations; conditions |a_i|,|b_i|<=delta. — *Role:* Residue bookkeeping giving the explicit constant 13381/2615348736000.

### Proof architecture

Smoothed eighth moment I_omega=int omega(t)|zeta|^8 dt. Use the approximate functional equation (Prop 2.1) with two Dirichlet polynomials of length ~T^2 each, then reduce the length by T^eps (truncate to mn<<U^{4+eps2}, U=T^{1-eps}) at a cost O(eps T (log T)^16) which is controlled via RH using the shifted-moment bound of Theorem 1.2 (Prop 3.1). Split I into diagonal I_D (Prop 3.2, unconditional) and off-diagonal I_O. For I_O use Prop 6.1 to express via D_{f;4,4}(r); insert Conjecture 1 (contour integrals of zeta^4(z1)zeta^4(z2) with Ramanujan sums c_q(r) and G_4), shift contours and compute residues (Secs. 6-8) giving Prop 3.3. Add D and O to get (3.9) with polynomial main term of leading size a_4 24024/16! (log T)^16 and error eps T (log T)^16 (only wins by eps, no lower-order terms). Remove smoothing omega by sandwiching with omega^+/omega^- (parameter eta, eta_0) to get Theorem 1.1.

Dependency edges: CAND-02382 → Ng-Shen-Wong shifted moments [26] (imports); CAND-02382 → Harper 2013 RH upper bound (uses); CAND-02382 → Ng 2008 sixth moment (extends)

**Imported results.** Harper 2013: I_k(T)<<T(log T)^{k^2} under RH; Theorem 1.2 (Ng-Shen-Wong companion [26]) shifted moments under RH, Chandee's conjecture for two shifts; Conrey-Gonek heuristic for D_k and conjectural asymptotics; Conrey-Farmer-Keating-Rubinstein-Snaith Lemma 2.5.1 [5] (cancellation of polar terms) mentioned for the shifted version; Ng 2008 sixth moment method [25]

**Techniques.** approximate functional equation for |zeta|^8; smoothed truncation to length T^{2-eps} (Soundararajan-Young, Chandee-Li, Shen); Duke-Friedlander-Iwaniec delta method heuristics (Appendix 1); Mellin-Barnes contour shifts and residue computation; shifted moment upper bound under RH (Harper's method with shifts); sandwich between smooth weights to remove smoothing

## Context and interpretation

**Importance and obstacle overcome.** Shows that RH + a quaternary additive divisor conjecture pins down the Keating-Snaith/CFKRS leading constant for k=4 (eighth moment), upgrading Harper's upper bound to an asymptotic. The obstacle: the Dirichlet polynomials have length T^2, beyond what additive divisor error terms can control; overcome by shaving T^eps off the length using a sharp RH-conditional bound on shifted moments (Theorem 1.2).

**Relation to prior work.** Extends Ng (sixth moment, ternary additive divisor conjecture) and makes Conrey-Gonek rigorous modulo the conjecture; uses Harper's RH upper bound and its shifted variant [26].

**Limitations and open questions.** Doubly conditional: RH plus an unproved, numerically unconfirmed Conjecture 1. 'Win by an epsilon' only: no lower-order terms or power-saving error term (unlike the sixth moment in [25]). Not proved: lower bound without RH (the authors indicate it is likely under Conjecture 1 alone, Remark 3). The no-shifts treatment sidesteps the |I|=|J|=4 shifted case (multiple residues).

**Ideas in remarks/appendices/abandoned paths.** Remark 6: the no-shift approach has main terms from multiple poles (multiple residues) versus the shifted approach where polar terms cancel by CFKRS Lemma 2.5.1 (Sec. 1, Remarks). Remark 3: the method likely gives the correct lower bound without RH (cf. Soundararajan-Young, Shen).

## Research potential

- **Hypotheses that might be weakened.** Conjecture 1's range |r|<<X^{1-eps'} and error O(P^C X^{1/2+eps_0}): the proof only needs a power saving below T^{1-0.5 eps}; an averaged-in-r form (Ivic's averaged conjecture) would plausibly suffice and is weaker. The k>=12 restriction in Theorem 1.2 should be checked for k=8 usage (the paper uses shifted moment of power 8 with the larger exponent; verify which k is used).
- **Generalizations.** Same method conditional on ternary/quaternary conjectures for 2k=10, 12 would need (k+? )-ary divisor conjectures; analogue for Dirichlet L-functions (Chandee-Li) and for the lower bound without RH.
- **Candidate connections.** Moments-RH linkage: fits into the programme relating moment asymptotics to zero statistics (Montgomery pair correlation, Conrey-Snaith ratios conjecture); a numerical test of Conjecture 1 via computing D_{4,4}(r) with smooth weights is a bridge to computational families.
- **Reusable lemmas.** Prop 3.1 (RH-based T^eps length reduction) is reusable for any 2k-th moment; Lemma 8.1 arithmetic factor G_k(s,p^j).
- **Possible experiments.** Numerically test Conjecture 1: compute D_{f;4,4}(r) for tau_4 with a smooth f at X~10^6-10^8 against the contour-integral main term; compare I_4(T) numerics with 24024 a_4/16! T(log T)^16 and lower-order polynomial P_16 (CFKRS).
- **Risks / barriers.** Cannot be made unconditional: it would imply I_4(T)<<T^{1+eps}, itself currently open. Conjecture 1 is a major open problem in additive divisor sums (k=ell=4).

## Audit notes (Level 1 reader)

Observed (not an error): abstract/Remark 6 notes Theorem 1.2 requires k>=12 while the eighth moment uses exponent 4 on each side (k=8 total power of |zeta|^8 shifted): hypothesis match not verified by me; check [26] and the use in Prop 3.1. Prop 6.1 text extraction garbled the prefactor 2T/sqrt(?) so it is not quoted exactly. Also the text and some displayed fractions were garbled by extraction; no definite inconsistency found.

*These notes are a reader's observations, not verified findings; see `audits/` for adjudicated findings.*

## Provenance

- Candidate `CAND-02382`; harvest queries: kw_RH_any, kw_moments_zeta, msc_11M06, msc_11M50, arxiv_moments_zeta, arxiv_rh_abs.
- Triage decision: include — Eighth moment of zeta conditional.
- Record generated by `tools/make_records.py`; search cutoff 2026-11-17.
