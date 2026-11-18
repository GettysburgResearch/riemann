# Independent review: harmonic Lagarias interpolation is eventually log-concave

Reviewer: li_advocate. Date:2026-11-17. Reconstructed from the parent's proposed chain of estimates before reading its proof. Result: the concavity claim and the support-chord transfer are valid with the explicit endpoint hypothesis below. No novelty claim is made and no unverified CA endpoint list is certified by this review.

## Exact statement

For real x>0 put H(x)=ψ(x+1)+γ, so H(n)=H_n at positive integers. For x≥32768 define B(x)=H(x)+exp(H(x))log(H(x)), and

g(t)=log(B(exp(t))/exp(t)).

Then g''(t)<0 whenever exp(t)≥32768. All logarithms here have positive real arguments.

## Derivative bounds with domains checked

Set x=exp(t), h=H(x), and a(u)=u/(exp(u)−1), with a(0)=1. The trigamma integral gives

H'(x)=∫_0^∞a(u)exp(−xu)du,
h'=xH'(x)=∫_0^∞a(v/x)exp(−v)dv.

For u>0, a'(u)≤0 follows from exp(u)(1−u)≤1. Also

a'(u)+1/2=exp(u)[sinh(u)−u]/(exp(u)−1)²≥0.

Thus −1/2≤a'≤0. Differentiation of the h' integral is justified by an integrable multiple of v exp(−v) on every x≥1 range, and gives

0<h''=∫_0^∞−(v/x)a'(v/x)exp(−v)dv≤1/(2x),
0<h'≤1.

The trigamma series and monotone integral comparison also give

H'(x)=∑_(n≥1)(x+n)^(−2)≥∫_1^∞(x+u)^(−2)du=1/(x+1),

so h'≥x/(x+1). Integrating that lower bound from0, using H(0)=0, yields H(x)≥log(x+1)>log x. The upper bound H'≤1/x implies H(x)−log x is decreasing; since H(1)=1, H(x)≤log x+1 for x≥1. Therefore

t≤h≤t+1, x≥1.

Finally log2>2/3, for example from log2=2atanh(1/3) and its positive series. Hence for x≥32768=2^15, t≥15log2>10 and h>10. The asserted threshold is therefore rigorously within the range used below.

## Bounds for the outer function

Let y=h≥10 and ℓ=log y. Write

f(y)=log(y+exp(y)log y)=y+log(log y)+log(1+r(y)),
r(y)=y exp(−y)/log y,
a_0(y)=(ℓ+1)/(y²ℓ²).

Put b=1/y−1/(yℓ). Since ℓ>2, one has0<b<1 and

(log r)'=−1+b∈(−1,0),
(log r)''=−1/y²+a_0<0

(the last inequality uses ℓ²>ℓ+1). Therefore r'≤0 and r''/r=((log r)')²+(log r)''≤1. It follows directly that

f'≤1+1/(yℓ)<2,
f''=−a_0+r''/(1+r)−(r')²/(1+r)²≤−a_0+r.

The r'' term is harmless if negative; if positive it is at most r/(1+r)≤r. No positivity of r'' has been assumed.

For all y≥10, exp(y)>13y³. Indeed exp(y)/y³ increases for y>3, while at10 the lower bound e>8/3 gives

exp(10)>(8/3)^10>13000.

The last inequality is a strict integer comparison, checked independently in the accompanying script. Using log y≤y and e<3, one obtains

exp(y)a_0−exp(y)r
>13y(ℓ+1)/ℓ²−y/ℓ
=12y/ℓ+13y/ℓ²>12>4e.

Thus

a_0>r+4exp(1−y).

## Concavity

Because g(t)=f(h(t))−t,

g''=f''(h)(h')²+f'(h)h''
≤−(a_0−r)/4+1/x
<−exp(1−h)+1/x≤0.

Here h'≥x/(x+1)≥1/2, a_0−r>0, f'≤2 and h''≤1/(2x) justify the first inequality. The last inequality uses h≤log x+1. The preceding strict inequality proves g''<0, even if the final non-strict bound happened to be equality. No RH assumption is used.

## Exact support-line endpoint transfer

Let integers32768≤a<b share an explicit ε>0 such that both maximize σ(n)/n^(1+ε) over positive integers n. More generally, it suffices to have a certified affine line dominating log(σ(n)/n) for every integer n∈[a,b], with equality at a and b. Then the arithmetic function on these integer log-coordinates lies below the chord through

(log a, log(σ(a)/a)), (log b, log(σ(b)/b)).

If σ(a)<B(a) and σ(b)<B(b), the arithmetic chord is strictly below the chord through (log a,g(log a)) and (log b,g(log b)). Concavity of g places that latter chord below g throughout the interval. Consequently σ(n)<B(n) for every integer a≤n≤b.

The orientation is important: the arithmetic support line is an upper bound for the discrete values, while concavity supplies a lower bound on g by its endpoint chord. Endpoint verification and a shared support line therefore suffice to cover all intermediate integers.

Calling two numbers 'consecutive colossally abundant' does not by itself constitute a certificate of this hypothesis: one must establish that they share the same supporting ε and account for every tie/face in the chosen CA enumeration, or verify the interval support line directly. Under a fully certified upper-envelope definition the standard CA correspondence may supply this fact, but that extra theorem or computation has not been silently assumed here. This review does not provide an endpoint list or prove the inequality globally beyond a finite range.

## Reproducibility and scope

`experiments/code/lagarias_concavity_skeptic.py` verifies the exact integer base inequality8^10>13000·3^10 and records180-digit sample evaluations of g'' and its proved upper bound at x=32768,10^6,10^12,10^50,10^100. The numerical evaluations are explicitly nonvalidated and serve only as stress tests; all-x concavity follows from the analytic inequalities above. Large x requires extra precision because h''=xψ_1(x+1)+x²ψ_2(x+1) involves cancellation.

Classification: independently checked with no issue in the eventual strict concavity theorem. The CA chord corollary is valid under the explicit shared-maximizer/support-line hypothesis; that hypothesis must remain visible in any finite certificate.

## Independent threshold improvement: x≥2048

A subsequent proposal by li_skeptic lowers the threshold to2048. I independently checked it before reading that agent's proof. The original argument remains valid with h≥7, with these replacements:

1. Since e<3, exp(5)<243<343=7³, hence log7>5/3. Therefore for h≥7, ℓ=logh satisfies ℓ²>ℓ+1. This is the condition actually used to make (logr)''<0 and r''≤r. Also h>e ensures0<1/h−1/(hℓ)<1, so the derivative signs remain correct and f'≤2 still holds.
2. The exact positive exponential partial sum is

∑_(k=0)^12 7^k/k!=14603038643/13685760>1029=3·7³.

Since exp(h)/h³ increases for h>3, this proves exp(h)>3h³ for every h≥7.
3. Accordingly,

exp(h)a_0−exp(h)r>2h/ℓ+3h/ℓ².

The function h/logh increases for h>e. Since e>8/3 gives e²>7 and therefore log7<2, the first term is strictly greater than7. The function h/log²h, on h>1, has its global minimum e²/4 at h=e²; thus the second term exceeds3·7/4=21/4. Their sum exceeds49/4>12>4e. Therefore a_0−r>4exp(1−h), exactly the domination needed in the existing g'' proof.
4. For x≥2048=2^11, h≥logx≥11log2>22/3>7, so every condition above holds.

Thus **g''(logx)<0 for every x≥2048**, and the same certified support-chord endpoint transfer applies for endpoints at least2048. This improvement uses exact inequalities throughout; it does not rely on floating-point concavity samples.

For a possible all-x≥1 extension, the coarse sufficient inequality −f''(h)/f'(h)>2exp(1−h) does not hold throughout the small h range (it already fails near h=2). That does not refute concavity itself; it shows this particular shortcut cannot justify a global extension. A separate sharper analytic argument or a fully validated compact-interval derivative certificate is required before lowering the remaining threshold. No all-x claim is made in this review.
