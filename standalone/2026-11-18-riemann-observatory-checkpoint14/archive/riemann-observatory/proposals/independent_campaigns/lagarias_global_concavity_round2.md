# A reproducible global concavity lemma for the Lagarias envelope

Campaign checkpoint:2026-11-17. Status: a computer-assisted elementary calculus proof, with the compact certificate independently audited and replayed in two interval implementations. Novelty is **unassessed**. This proves no instance of RH beyond separately supplied arithmetic inputs.

## Exact statement

For realx≥1, let

H(x)=ψ(x+1)+γ=Σ_{k≥1}x/[k(x+k)],
B(x)=H(x)+e^(H(x))log H(x),
g(t)=log[B(e^t)/e^t].

Then **g″(t)<0 for every t≥0**. At the left endpoint the derivatives are those of the smooth continuation aroundx=1, whereB(1)=1>0.

The proof has two parts: an analytic argument for x≥2048 and a finite rigorous interval certificate on1≤x≤2048. The latter has170 rational cells and a standard-library-only replay using integer arithmetic. No numerical sample is used as proof.

## Analytic preliminaries

Put x=e^t and h(t)=H(x). The integral representation

h′(t)=∫_0^∞ a(v/x)e^(−v)dv, a(u)=u/(e^u−1),

with a(0)=1, gives

x/(x+1)≤h′≤1, 0<h″≤1/(2x).                    (G1)

For completeness, e^(−u)≤a(u)≤1; also−1/2≤a′(u)<0 foru>0. The lower derivative bound is equivalent to sinh u≥u, and differentiation under the integral is dominated by(v/(2x))e^(−v) on compact positive x-intervals. Thus h″=−∫(v/x)a′(v/x)e^(−v)dv.

The function H(x)−logx is nonincreasing, equals1 atx=1 and is nonnegative at each integer by harmonic-sum integral comparison. Therefore

logx≤H(x)≤logx+1, x≥1.                       (G2)

In particular1/x≤e^(1−h).

Write f(h)=log[h+e^h logh], so g=f(h(t))−t. Let

B=h+e^h logh,
B₁=1+e^h(logh+1/h),
N=−e^(2h)(logh+1)/h²+e^h[(h−2)logh+2−3/h]−1.

Direct differentiation gives

f′=B₁/B, f″=N/B².                            (G3)

The expansion N=BB″−B₁² was independently checked by the reviewer and advocate.

## Analytic tail: x≥2048

For h≥7 put L=logh,r=he^(−h)/L,A=(L+1)/(h²L²), and b=1−1/h+1/(hL). Then

0<b<1, b′=[1−1/L−1/L²]/h²>0.

Indeed log7>5/3, since e<3 gives e^5<243<343=7³; hence1/L+1/L²<24/25. The decomposition f=h+loglogh+log(1+r), together with r′=−br and r″=r(b²−b′)≤r, gives

0<f′<2, f″≤−A+r.                            (G4)

The following exact inequalities establish the required dominance.

* e^h/h³ increases forh>3. At7, Σ_{j=0}^{12}7^j/j!=14603038643/13685760>1029=3·7³. Thus e^h>3h³ forh≥7.
* The function h/logh increases forh>e. Since e²>7 and log7<2, one has2h/logh>7 forh≥7.
* Onh>1, h/log²h has global minimum e²/4; hence3h/log²h>21/4.

It follows that

e^h A−h/logh
>2h/logh+3h/log²h
>49/4>12>4e.

Since e^h r=h/logh,

A−r>4e^(1−h).                               (G5)

Now use(G1), the negative sign in(G4), h′≥1/2 and(G2):

g″=f″(h)(h′)²+f′(h)h″
≤−(A−r)/4+1/x
≤−(A−r)/4+e^(1−h)<0.

Finally log2>2/3, obtained by integrating the tangent-line lower bound for1/u on[1,2]. Therefore x≥2048 implies h≥logx≥11log2>7. This proves the tail.

The tail was independently checked by the parent, skeptic and advocate tracks. See `audits/adversarial_reviews/lagarias_concavity_third_round2.md` and the advocate's separate review for the initially supplied32768 threshold and this strengthening.

## Compact certificate: a sufficient inequality

On each cell we certify B>0,B₁>0,N<0 and

P(x,h)=N[x/(x+1)]²+B B₁/(2x)<0.              (G6)

These four strict inequalities imply g″<0 by(G1)–(G3): the negative f″ term uses the lower bound onh′, and the positive f′ term uses the upper bound onh″. Explicitly,

g″≤P(x,H(x))/B(H(x))²<0.

The full dependence ofH onx is enclosed by a rectangle in(x,h); interval evaluation ofP over that rectangle is conservative. No assumption of independent actual variables is needed.

## A finite rational enclosure for H

For integerM≥1 set

S_M(x)=Σ_{k=1}^M x/[k(x+k)].

For fixedx>0 the summand x/[u(x+u)] is positive and decreasing in realu. The integral test therefore gives

S_M(x)+log(1+x/(M+1)) ≤ H(x)
≤ S_M(x)+log(1+x/M).                          (G7)

For a rational cell[a,b], monotonicity ofH gives a valid interval from the lower expression atato the upper expression atb. The certificate usesM=32. Every operation in the enclosure and in(G6) is performed with rigorous outward rounding.

Thus no special-function implementation of digamma, polygamma or Euler's constant is required to check the compact proof.

## Certificate and two independent arithmetic backends

The adaptive Arb construction generated339 trial cells and accepted170 leaves covering exactly[1,2048]. Their endpoints are rational dyadic numbers. The coverage check uses exact rational comparisons: the first left endpoint is1, each next left endpoint equals the previous right endpoint, every width is positive, and the final right endpoint is2048.

1. `experiments/code/lagarias_compact_arb.py` constructs and replays the certificate with python-flint0.9.0/FLINT3.6.0 at160-bit precision. It uses only validated log/exp ball functions and elementary arithmetic. Artifact: `experiments/results/lagarias_compact_arb.json`.
2. `experiments/code/lagarias_compact_integer.py` independently replays the same rational cells using **only Python's standard library**. Artifact: `experiments/results/lagarias_compact_integer.json`. It does not import FLINT, Arb, mpmath, Decimal or any floating-point numerical package. Acceptance decisions use only integer comparisons.

The advocate independently inspected the code, checked240 signed reciprocal intervals against exact Fractions, and replayed every cell with both backends. All strict comparisons passed. The parent has been notified for integration/adjudication. Neither implementation is a proof-assistant kernel; the finite algorithm and its interval lemmas remain part of the inspectable proof.

## Standard-library interval arithmetic and transcendental remainders

The integer backend represents an interval as[l,u]/S with integerl,u and S=2^192. Input rationals are enclosed by floor and ceiling. Addition is exact; multiplication takes the minimum and maximum of the four integer endpoint products and rounds after division byS. Reciprocal uses decreasing monotonicity and outward floor/ceiling ofS² divided by endpoints. Intervals containing0 are rejected before division.

The logarithm uses exact binary range reduction z=2^k y,1≤y≤2. Set r=(y−1)/(y+1). The program checks0≤r≤1/2 and evaluates

logy=2Σ_{j=0}^{127}r^(2j+1)/(2j+1)+R,
0≤R≤3·2^(−256).

The bound follows from the geometric tail2r^257/[257(1−r²)]≤3·2^(−256). The same expansion computes log2. For negativek, interval multiplication automatically reverses endpoint order. Monotonic endpoint evaluation handles an interval argumentz.

The exponential reduces a nonnegative argument to0≤y≤1 by dividing by a power of2. It evaluates the degree-80 Taylor polynomial and adds the Lagrange remainder bound

0≤e^y−Σ_{j=0}^{80}y^j/j!≤3/81!,

usinge<3. Repeated interval squaring restores the original argument. Negative arguments are handled by reciprocal. Again monotonic endpoint evaluation encloses an interval argument. All Taylor and geometric remainder bounds are themselves rounded outward as rational integers overS.

Rounding errors from every intermediate operation are retained; small terms that fall below one scaled unit are enclosed rather than silently discarded. The compact strict margins do not depend on a tolerance or a sampled sign.

## Portable replay

From an ordinary Python3 installation, with the archive paths intact:

```sh
python experiments/code/lagarias_compact_integer.py --cells experiments/results/lagarias_compact_integer.json
```

Expected output reports170 certified cells, domain[1,2048],192-bit precision and no external packages. The command recomputes the inequalities on every cell; it does not merely inspect the signs stored in JSON. It also checks exact coverage.

An optional independent Arb replay is:

```sh
python -m pip install python-flint==0.9.0
python experiments/code/lagarias_compact_arb.py --verify experiments/results/lagarias_compact_arb.json
```

A separate exploratory script, `lagarias_concavity_third.py`, contains arbitrary-precision sampled differentiation checks. Those samples are not used anywhere in the proof above.

## What the global lemma enables—and what remains arithmetic

If integeru<v maximize σ(n)/n^(1+ε) for a commonε over the relevant integer domain, their common maximum supplies the affine support line

log[σ(n)/n]≤C+εlogn.

If both endpoints satisfy σ(u)≤B(u) and σ(v)≤B(v), global concavity putsg above this line throughout[logu,logv]. Hence every intervening integer satisfies the Lagarias inequality. With the global result there is no lower endpoint threshold beyond1.

This is a **conditional interval certificate**. It does not establish endpoint inequalities, prove global maximizer status from finite-search evidence, or certify an infinite sequence of intervals. A finite initial verification still proves only a finite statement.

The same global concavity also implies continuous monotonicity ofB(x)/x: by(G1),h′→1, and(G4)'s decomposition givesf′→1, so g′→0 at infinity. Sinceg″<0, g′ decreases strictly toward0 and must be positive at every finite point. This is stronger than merely knowing the sampled sequenceB(n)/n increases, but priority has not been determined.

## Prior-source comparison and limits

The actual arXiv:2602.15905v2 source, Andrew MacArevey, was read in full. Proposition2.1 proves (B(x)/x)′>0 forx≥e^4; Corollary2.1 supplies integer monotonicity for alln using finite checks below55; Theorem3.1 reduces least counterexamples to superabundant numbers. No log-concavity theorem was identified there.

The Lagarias sections of arXiv:2606.15096v1 were inspected. They report formal finite checking through10000 and leave a global tail/extremal-integer reduction unresolved. The associated formal artifacts were not obtained or replayed in this track. No smooth-profile log-concavity or common-parameter support-line interpolation theorem was identified in the inspected material.

These comparisons do not constitute a complete priority search. The mathematical output should be described as an independently established, reproducible calculus lemma of unassessed novelty, not as a new RH theorem or a claim of historical priority.
