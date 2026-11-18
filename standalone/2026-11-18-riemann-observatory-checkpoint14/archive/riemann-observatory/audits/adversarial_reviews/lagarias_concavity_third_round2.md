# Independent third review: logarithmic concavity of the Lagarias envelope

Date:2026-11-17. This reviewer did not read the parent or advocate proof before reconstructing the proposal from the stated lemma and definitions. Status: **independently checked with no issue found in the stated calculus lemma or conditional endpoint implication**. No literature novelty assessment, RH proof, or independent validation of the separate integer base certificate is claimed.

## Statement checked

For realx≥1 define

H(x)=ψ(x+1)+γ,   B(x)=H(x)+exp(H(x))log H(x),

where ψ is the digamma function and γ is Euler's constant. Put

g(t)=log[B(exp t)/exp t].

Then g″(t)<0 whenever exp t≥32768. All logarithms in the proof are natural. On this domain H>10, so every auxiliary log H and log log H below is well-defined.

## 1. Integral identities and differentiation conditions

The harmonic continuation has the convergent representation

H(x)=∫_0^1 (1−u^x)/(1−u)du
    =Σ_{k≥1}(1/k−1/(x+k)), x>0.

It equals the harmonic number at every integer. The series and its differentiated series converge uniformly on compact positive x-intervals. Equivalently, differentiation of the integral is justified by domination near0 and1. Thus ψ′(x+1)=Σ_{k≥1}(x+k)^(−2).

Let h(t)=H(exp t), x=exp t, and a(u)=u/(exp u−1), with a(0)=1 by continuation. The trigamma integral and the substitution v=xy give

h′(t)=xψ′(x+1)=∫_0^∞ a(v/x)e^(−v)dv.             (L1)

For u>0,

a′(u)=[(1−u)e^u−1]/(e^u−1)².

The numerator is negative because its derivative is−ue^u and its value at0 is0. Moreover a′(u)≥−1/2 is equivalent to

e^(2u)−2ue^u−1=2e^u(sinh u−u)≥0.

Therefore −1/2≤a′≤0, with strict negativity for u>0. Also e^(−u)≤a(u)≤1: the upper bound uses e^u≥1+u; the lower bound is equivalent to1−e^(−u)≤u.

These bounds imply

x/(x+1)≤h′≤1,

and differentiation under(L1) gives

h″(t)=−∫_0^∞(v/x)a′(v/x)e^(−v)dv,

hence0<h″≤1/(2x). The bound |a′|≤1/2 supplies the required integrable derivative majorant on each compact positive x-interval. No informal interchange of a nonuniform limit is needed.

## 2. Harmonic-continuation bounds and the threshold

Since h′≤1, H(x)−log x is nonincreasing for x≥1. Its value at1 is1. At each integern, H_n−log n≥0 by the elementary harmonic-sum integral comparison. For any realx≥1, monotonicity compared with an integern≥x therefore gives

log x≤H(x)≤log x+1.                              (L2)

Also log2>2/3: integrate the strict tangent-line lower bound for1/u at u=3/2 over[1,2]. Thus log32768=15log2>10. For x≥32768, h=H(x)>10. Equation(L2) also gives

1/x≤e^(1−h).                                    (L3)

## 3. Independent derivatives of the outer function

Define f(h)=log[h+e^h log h]. For h≥10, put

r=h e^(−h)/log h,
A=(log h+1)/(h² log²h),
b=1−1/h+1/(h log h).

Since log h>2, one has0<b<1 and

b′=1/h²−A=[1−1/log h−1/log²h]/h²>0.

The decomposition

f(h)=h+log log h+log(1+r)

gives r′=−br and r″=r(b²−b′)≤r. Therefore

0<f′=1+1/(h log h)−br/(1+r)<2,

f″=−A+r″/(1+r)−(r′)²/(1+r)²≤−A+r.              (L4)

In the last inequality, r″≤r suffices even if r″ is negative: its divided contribution is then nonpositive. Thus no sign was silently assumed for r″.

## 4. The exponential dominance inequality

For all h≥10,

e^h>13h³.

Indeed e^h/h³ is increasing for h>3, and e>8/3 gives e^10>(8/3)^10>13000 by an exact integer comparison. Using this inequality,

e^h A>13h(log h+1)/log²h.

Subtract h/log h from the right side. The remainder is

12h/log h+13h/log²h>12>4e,

because log h<h and e<3. Since e^h r=h/log h, this proves

A>r+4e^(1−h).                                   (L5)

In particular A−r>0, so the bound on f″ is strictly negative.

## 5. Chain rule and strict concavity

Since g(t)=f(h(t))−t,

g″=f″(h)(h′)²+f′(h)h″.

For x≥32768 one has h′≥x/(x+1)≥1/2,0<h″≤1/(2x),0<f′<2, and f″≤−(A−r)<0. Care is needed with the negative sign: using the lower bound on(h′)² gives an upper bound on this negative term. Thus

g″≤−(A−r)/4+1/x
   ≤−(A−r)/4+e^(1−h)<0

by(L3) and(L5). This proves the claimed threshold lemma for all realx in the domain, rather than only at sampled integers.

## 6. Shared-parameter maximizer endpoints

Let integers u<v both maximize σ(n)/n^(1+ε) over all positive integers n for the **same** real ε. Write

C=log[σ(u)/u^(1+ε)]=log[σ(v)/v^(1+ε)].

Then every positive integern satisfies

log[σ(n)/n]≤C+εlog n.                            (L6)

Assume u,v≥32768 and σ(u)≤B(u), σ(v)≤B(v). At t_u=log u and t_v=log v, the affine line C+εt is therefore below both g-values. Strict concavity puts g above its endpoint chord, and that chord is above the affine line throughout[t_u,t_v]. Combining with(L6) yields

σ(n)≤B(n), for every integer u≤n≤v.

Interior inequalities are strict when u<v. This argument handles multiple maximizer ties: only common ε and equality of the maximizing value matter. It does not require that the two endpoints be consecutive in an ordered list of maximizers.

The direction of concavity is correct here: the arithmetic support line is below both endpoint values, so a concave envelope lies above it between the endpoints. Concavity alone would not justify interpolating arbitrary unrelated upper bounds without(L6).

## Scope checks and failure conditions

* Both endpoints must be in the proven real-concavity domain. An interval crossing32768 is not covered merely because one endpoint exceeds it.
* The same ε must support both endpoints. Being maximizers for two unrelated parameters does not supply(L6) with a common affine line.
* Maximization is global over the integers under consideration. A finite-search maximizer does not automatically give(L6) beyond that finite search domain. A restricted-domain version of the implication holds only within that verified domain.
* Endpoint Lagarias inequalities and maximizer status remain separate arithmetic inputs. This audit does not verify the independent base certificate through55440 or any infinite list of endpoints.
* The result certifies finite intervals once their inputs are known. It proves neither RH nor all remaining endpoint inequalities.
* The proof uses no floating-point constants: e>8/3,e<3,log2>2/3 and the integer comparison for(8/3)^10 suffice.

## Optional strengthening noticed during review

The threshold can likely be reduced without changing the argument. An explicit variant for h≥7 replaces e^h>13h³ by e^h>3h³; the latter follows from monotonicity and the rational lower bound Σ_(k=0)^12 7^k/k!>1029. Then

3h(log h+1)/log²h−h/log h=2h/log h+3h/log²h>4e

for h≥7: h/log h is increasing there, log7<2, and h/log²h≥e²/4, while e²>7 and e<3. Also log7>5/3 ensures b′>0. With log2048=11log2>7, these inequalities would prove the same concavity for x≥2048. This strengthening is supplied as a complete elementary candidate for separate independent review; the adjudicated claim in this report remains the requested32768 threshold.

Exploratory direct numerical differentiation also found negative g″ at sample points between1 and32768, but that observation is not a proof of global concavity below the stated threshold.
