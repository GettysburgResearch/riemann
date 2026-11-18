# PAPER-H001 — Robin,1984: original source and sparse extremal reduction

**Identity.** Guy Robin, *Grandes valeurs de la fonction somme des diviseurs et hypothèse de Riemann*, Journal de Mathématiques Pures et Appliquées, neuvième série63(2)(1984),187–213. Manuscript received April1983 (p213). DOI not established here; MR0774171, ISSN0021-7824. Source read: original journal scan,29 PDF pages comprising two cover/contents pages and all27 numbered article pages. Current Jagy host failed; archived copy succeeded: https://web.archive.org/web/20180205020128id_/http://zakuski.utsa.edu/~jagy/Robin_1984.pdf . Access2026-11-17. Archived host is a source copy, not a publisher correction service.

**Scope.** Level0 verified from original page headers/title and accessible scan. Whole French article pp187–213 read substantively, including appendix table/references; equations underlying the requested results were checked visually rather than accepted from OCR. Level1 complete. Scoped Level2 reconstruction of §3Proposition1 and §4 oscillation transfer and comparison to Lagarias; not a complete technical audit of the27-page proof. The finite computation of2347 extremal numbers, every explicit numerical constant and Nicolas's underlying Landau theorem were not independently certified. No paper-wide Level3 claim. See `audits/robin_round2.md` for a small formula-fidelity issue and limits.

## Exact main results

All logarithms natural. Let σ(n)=∑_(d|n)d, γ Euler's constant, and f(n)=σ(n)/(n loglogn), n≥3.

**Theorem1,p188:** RH is equivalent to

    σ(n)<e^γ n loglogn for every integer n≥5041.

The inequality is strict and the boundary is n>5040. The source's §3Proposition3,p204, supplies the RH⇒inequality direction; §4Proposition1,pp204–205, supplies a stronger oscillatory converse.

**Theorem2,p188:** For every integer n≥3,

    σ(n)/n ≤ e^γ loglogn + K/loglogn,

where the displayed constant is0.6482… and equality occurs atn=12. Consequently its exact value is K=(7/3−e^γ loglog12)loglog12. The abstract uses the rounded upper constant0.6483 with a strict inequality. Do not silently describe the sharp constant as exactly0.6483. Theorem2 is unconditional, although its proof draws on finite computations also used in§3.

**Theorem3,pp188–189:** Under RH the paper sharpens bounds for ∑_(p≤x)1/p−loglogx−B_1 and e^γ logx∏_(p≤x)(1−1/p)−1, with error logx/(8πsqrtx) and stated small-x thresholds. Its proof is in§5; this record does not certify all threshold constants. The relevant conceptual improvement is integration of the explicit formula before bounding it, rather than pointwise estimation of ψ(x)−x inside the tail integral.

## Colossally abundant numbers: exact tie convention

**Definition,p189:** N≥1 is colossally abundant(CA) if there exists ε>0 such that

    σ(m)/m^(1+ε) ≤ σ(N)/N^(1+ε) for every integer m≥1.

The non-strict inequality matters. CA includes every tied global maximizer, not only the smallest or largest integer at a threshold. With F(x,a)=log(1+1/(x+x²+⋯+x^a))/logx, a≥1, define E_p={F(p,a):a≥1} and E=∪_pE_p. Away from E, the unique maximizing exponent is

    a_p(ε)=floor(log((p^(1+ε)−1)/(p^ε−1))/logp)−1.

At ε∈E_p two adjacent exponents atp tie. Independent choices at distinct tied primes give additional global maxima. The proposition onp190, citing Erdős–Nicolas and the six-exponentials theorem, describes the possible two-prime coincidence by four maximizers N,qN,rN,qrN. Its transcendence dependency was not re-proved here. An enumeration that simply assumes all threshold sets E_p disjoint has an unproved extra assumption. For the endpoint reduction one can instead include all tied CA values; adjacent values share a supporting ε.

## §3Proposition1,p192: endpoint reduction

For consecutive CA integers N,N′ with3≤N≤n≤N′,

    f(n) ≤ max(f(N),f(N′)).

Although placed in a section whose standing assumption isRH, its proof uses only the extremal definition and elementary convexity. This dependence was independently reconstructed; RH is unnecessary for this local proposition.

Choose the common supporting ε and c=σ(N)/N^(1+ε)=σ(N′)/N′^(1+ε). Then σ(n)/n≤c n^ε, so

    f(n)≤c exp(h(logn)), h(t)=εt−loglogt, t>1.

Since h″(t)=(logt+1)/(t²log²t)>0, its maximum on[logN,logN′] is at an endpoint. Equality of the supporting values supplies f(N)=c exp(h(logN)) and likewise forN′. This proves the result including ties.

For a *finite* verification interval, this certificate requires both bracketing endpoints, possibly including the first CA beyond the advertised cutoff. It also has a startup issue:5040 itself violates Robin's inequality, so a valid right endpoint55440 does not by itself certify5041≤n<55440 using the maximum inequality. Robin's proof explicitly checks ordinary integers through55440 after checking CA values from55440 upward(p204). The source reports2347 CA values for its finite prime-factor cutoff; that computation has not been reproduced here.

## §4Proposition1,pp204–205: exact oscillation and converse

Let Θ=sup{Reρ:ζ(ρ)=0,0<Reρ<1}. Assuming¬RH, soΘ>1/2, for **every** b with

    1−Θ<b<1/2,

Robin states, along CA integers n,

    f(n)=e^γ[1+Ω_±((logn)^(−b))].

The Ω_± means there are positive constants c_+,c_- and arbitrarily large CA integers with f(n)/e^γ−1≥c_+/(logn)^b, and arbitrarily large CA integers with f(n)/e^γ−1≤−c_-/(logn)^b. It does not say every CA number violates the inequality, does not give an effective first violation, and does not require a zero attainingΘ.

The input onp204 is Nicolas's1983 Theorem3, obtained using Landau's oscillation method:

    log[e^γ logθ(x)∏_(p≤x)(1−1/p)]=Ω_±(x^(−b)).

This is an explicit external dependency, not proved from scratch in Robin's article or this audit. His CA factorization yields(p205)

    f(n)=exp[−2sqrt2/(sqrtx logx)+O(1/(sqrtx log²x))]
          × (∏_(p≤x)(1−1/p)^(−1))/logθ(x),

where x is the largest-prime cutoff attached to ε and logn~x. The deterministic logarithmic correction is o(x^(−b)) becauseb<1/2. Taking reciprocal/exponentials preserves both signs of the larger oscillation (with their roles interchanged), and comparability logn~x transfers its scale. This reconstructs the converse architecture and explains the exponent restriction. Any argument usingb=1/2 needs additional control and does not follow from this dominance comparison.

## Reconciliation with Lagarias(PAPER-R001)

Lagarias's all-integer criterion is σ(n)≤H_n+e^(H_n)logH_n, n≥1, equality only at1. Its Lemma3.2 bounds the excess over Robin's right side by7n/logn forn≥20. Robin's positive CA oscillation has excess at least c e^γ n loglogn/(logn)^b. Their ratio tends∞ for b<1/2 (indeed forb<1). Thus¬RH forces infinitely many CA violations of **Lagarias's** inequality as well.

Consequently, for any fixed finite cutoffB, RH is equivalent to Lagarias's inequality holding on **all CA integers n≥B**. This is a global logical consequence of Robin's oscillation theorem plus Lagarias's comparison and RH⇒all-integer Lagarias. It is not the same as a finite-interval endpoint reduction for Lagarias's right side, and it supplies no finite stopping criterion. Checking just the *Robin inequality* on all CA integers>5040 also suffices globally. Testing Lagarias only on primorials or an arbitrary CA subsequence has not been justified by this argument: the positive oscillation subsequence need not meet the chosen subset.

## Proof architecture and frontier

RH branch: CA supporting-line reduction → explicit formula integrated against weighted kernels → prime-square tail and loglogN corrections → negative leading margin2+c−2sqrt2, c=γ+2−log(4π), plus explicit bounds → finite CA and integer verification → threshold5041.

Converse branch: off-line zero/Θ>1/2 → Nicolas–Landau oscillation in normalized prime product → CA profile correction of smaller order → two-sided CA oscillation → infinitely many Robin violations → domination of Lagarias slack.

The mathematically useful next step is an interval-arithmetic CA generator that includes ties and certifies every supporting interval, together with independently reproducible versions of the finite checks and a dependency audit of Nicolas's precise oscillation theorem. Improving finite ranges cannot replace the unbounded oscillation/tail theorem. A second project is to prove an actual endpoint domination theorem for a chosen elementary replacement of loglogn; the transfer throughRH above does not supply one.
