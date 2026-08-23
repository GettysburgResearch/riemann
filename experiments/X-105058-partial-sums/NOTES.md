# Lane P PLAN (partial-sum equivalence)
1. Read T-105051, L-103101/103102, L-105052/105053, O-105054, X-105053 ANALYSIS.
2. (1) Redo Plancherel for TRUNCATED field Ht: exact identity + edge terms.
3. (2) Dictionary: gate theta <-> mean-square of Sigma_N(gamma) on fixed segment.
4. (3) VK lemma: M_{1/2}(x) << x exp(-c (log x)^{3/5-eps}) via Perron + branch cut on VK region.
5. Partial summation -> Sigma_N(gamma) << N^{1/2} exp(-c(log N)^{3/5-eps}) (g-series).
6. (4) RH-conditional: branch-cut Perron for M_{1/2} under RH; label rigor level.
7. Numerics: Sigma_N(gamma), gamma in {1,1.5,2}, N to 1e7, h_U + g; M_{1/2}(x) growth.
8. Draft L-105058 dictionary theorem + VK lemma in laneP dir.
9. Record failures honestly; RH never claimed.
10. Final: STATEMENTS PROVED first, <=1500 words.

## Derivations (pre-numerics)
- (1) Truncated Plancherel is EXACT, zero edge terms: field sum_{U<n<=N_X} h_U(n)n^{-1/2}A_-(Y/n)
  vanishes off (U, 4N_X] (A_- supp (1,4)); [U,4X/U] covers it. So Ht = (1/2pi) int w |P_{U,N_X}|^2.
- (3) ORCHESTRATOR SKETCH REFUTED: M_{1/2}(x) ~ -x/(2 sqrt(pi) (log x)^{3/2}) (Selberg-Delange,
  branch point of zeta^{-1/2} at s=1: VANISHING sqrt branch, NOT analytic; sigma_c(g)=1 exactly).
  Hence Sigma_N^(g)(gamma) ~ -N^{1/2-ig}/(sqrt(pi)(1-2ig)(log N)^{3/2}) DIVERGES. No VK subpower
  saving for g-sums; mollifier M_U zeta^{1/2} is what kills the w=1 branch: h-series = zeta^{1/2} R_U,
  R_U = Mobius tail, all Taylor data of R_U at 1 is VK-small.
- h-branch term: Sigma_N^(h)(gamma) = -2 m(U) N^{1/2-ig}/((1-2ig) sqrt(pi log N)) + contour,
  m(U)=sum_{d<=U} mu(d)/d. Energy branch mass ~ (2/pi^2) I_w m(U)^2 N/log N, I_w=int w/(1+4g^2).
  BUT: hatA_-(1/2)=0 kills the BULK Y^{1/2} mode; branch mass survives only via truncation edge
  Y ~ (N,4N]. Consistency vs L-105052 envelope and T-105051(III) RH-floor alpha=1/4 CHECKS.
- P4 (new, unconditional): limsup (1/log T) sum_{n<=T} m(n)^2 >= c0 = 2/((1/4+g1^2)|zeta'(rho1)|^2)
  via one-sided Mellin F(s)=1/(s zeta(s+1)) + Plancherel at Re s = -1/2+h vs pole-blowup at rho1.
- Refutation program: gate_theta for theta<1/4 contradicts branch mass io (needs extraction rigor).

## Numerics summary (num_results.json)
- sieve validated (g = mu*eta conv to n=300 exact).
- Sigma_g divergence: ratio to -N^{1/2-ig}/(sqrt(pi)(1-2ig)log^{3/2}N) at N=1e7:
  (1.15,0.09)@g=1, (1.06,0.21)@g=1.5, (0.84,0.10)@g=2. CONFIRMED incl. phase.
- M_half/pred -> 1.14 at 1e7 (1/log drift to 1). sigma_c(g)=1 confirmed shape.
- Sigma_h vs branch pred -2m(U)N^{1/2-ig}/((1-2ig)sqrt(pi log N)): ratios
  (1.1-1.7, |im|<=0.33) coupled and frozen-U modes; sqrt(N) growth, phase locked.
- Constants: gamma1=14.134725, |zeta'(rho1)|=0.793160, c0=0.0158924,
  I_w=0.49906, w_min[1,2]=0.380416 (matches deposit), min|zeta(1/2+ig)| on [1,2]=0.5396.
- Q(T)/log T = .303,.212,.166,.139,.120,.107 (T=1e2..1e7) > c0, decreasing.
- Branch mass vs measured H rows: pred 0.000-0.106 vs H 0.52-1.01: branch invisible
  below X~1e10 -> old flat scans do NOT test the mechanism. At X=UN=3.16e10 (this
  lane's direct P measurement) |Sigma_h(1)|^2=6.3 vs |b|^2=2.7: growth visible.
## Failures / refuted sketches recorded
- Orchestrator (3) premise FALSE: M_{1/2} has NO VK saving (branch point at 1);
  M_{1/2} ~ -x/(2 sqrt(pi) log^{3/2} x); g-series sigma_c = 1; critical partial
  sums diverge ~ N^{1/2}/log^{3/2}N. Dictionary item (2a) fixed-segment form FALSE
  as stated; corrected with |gamma|<=N uniform window + MV tail.
- Draft claim written: L-105058-partial-sum-dictionary-and-branch-mass.md
