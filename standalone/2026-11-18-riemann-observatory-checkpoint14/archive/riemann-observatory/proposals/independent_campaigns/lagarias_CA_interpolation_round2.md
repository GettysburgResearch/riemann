# A concrete finite-interval interpolation test for Lagarias's bound

Round2,parent reconstruction,2026-11-17. Independent review requested. No novelty claim. This concerns sparse finite verification, not a proof of RH and not the assertion that every counterexample itself is colossally abundant.

## Statement with explicit maximizer hypothesis

Let H(x)=psi(x+1)+gamma for realx>0, so H(n)=H_n. Put B(x)=H(x)+exp(H(x))logH(x). Then

g(t)=log(B(exp t)/exp t)

is strictly concave for exp t>=32768.

Consequently, suppose integers32768<=u<v are BOTH global maximizers of sigma(n)/n^(1+epsilon) for the SAME epsilon>0. If sigma(u)<=B(u) and sigma(v)<=B(v), then sigma(n)<=B(n) for every integeru<=n<=v. Strict endpoint inequalities imply strict inequalities throughout. This common-maximizer formulation includes all ties and does not rely on an unproved prime-ratio rule for consecutive colossally abundant numbers.

Ordinarily consecutive vertices in the complete colossally abundant upper hull share such a supporting parameter. The theorem is deliberately stated with the supporting-parameter hypothesis rather than silently relying on a particular enumeration convention or omitting simultaneous maximizers. Robin's original source and its exact tie conventions are recorded in PAPER-H001.

## Smooth harmonic derivative bounds

Write x=exp t>=1 and h(t)=H(x). The standard trigamma series and its Laplace integral give

h'=x sum_(n>=1)(x+n)^(-2)=integral_0^infinity a(v/x)exp(-v)dv,

a(y)=y/(exp y-1), with a(0)=1.

The integral test gives h'>=x/(x+1), while exp y-1>=y gives h'<=1. Also

-1/2<=a'(y)<=0 for y>=0.

Indeed a'<=0 follows from exp(y)(1-y)<=1; the derivative of its left side is-negative. The lower bound follows from

a'(y)+1/2=exp(y)(sinh(y)-y)/(exp(y)-1)^2>=0.

Differentiating the integrable Laplace expression yields

0<=h''=integral_0^infinity[-(v/x)a'(v/x)]exp(-v)dv<=1/(2x).

Differentiation is justified locally uniformly inx>0 by the displayed bounded derivative and exponential majorant. As H(1)=1, integrating h'<=1 and h'>=x/(x+1) gives

log x<h<=log x+1, x>=1,

where the lower bound uses1+log((x+1)/2)>=log x+1-log2>log x.

## Concavity calculation

Let z>=10, ell=log z, r=z exp(-z)/ell, and f(z)=log(z+exp(z)log z). Then

f(z)=z+logell+log(1+r).

Set A=(ell+1)/(z^2 ell^2). The logarithmic derivative ofr is

a_r=-1+1/z-1/(z ell).

For z>=10, -1<a_r<0 and a_r'=(-1+(ell+1)/ell^2)/z^2<=0. Thus r'<0 and r''=r(a_r^2+a_r')<=r. It follows that

0<f'<=1+1/(z ell)<=2,
f''=-A+r''/(1+r)-r'^2/(1+r)^2<=-A+r.

Moreover A>=1/(z^2 ell) and

A>r+4exp(1-z), z>=10.                               (*)

To prove(*), it suffices that exp z>z^3+4e z^2 ell. Since ell<=z ande<3, the right side is<13z^3. The function exp z/z^3 is increasing forz>3, and at10 we have exp10>(8/3)^10>13000, usinge>8/3 and the exact integer comparison8^10>13000*3^10. Hence(*) is strict.

Now x>=32768=2^15 gives log x>10 because log2>2/3 (strict Jensen inequality for1/u on[1,2]). Thus h>=10. Combining the derivative bounds, h'^2>=1/4,1/x<=exp(1-h), and the fact that-A+r<0 gives

g''=f''(h)h'^2+f'(h)h''
<=-(A-r)/4+1/x< -exp(1-h)+1/x<=0.

This proves strict concavity. All constants are coarse; no claim of the optimal threshold is made. Nonvalidated numerical inspection suggests a much larger range but is not used in the proof.

## Why the supporting chord certifies every intermediate integer

If u andv share a maximizingepsilon, write M=sigma(u)/u^(1+epsilon)=sigma(v)/v^(1+epsilon). For every integern,

log(sigma(n)/n)<=logM+epsilon logn.

The right side is the chord through the endpoint values log(sigma(u)/u) and log(sigma(v)/v). Endpoint inequalities put this chord below the chord throughg(logu),g(logv). Concavity puts the latter chord belowg(logn). Exponentiating gives the stated bound. Ties at other maximizing integers cause no problem; they lie on the same support line.

## Scope and continuation

A finite chain of such verified supports, plus endpoint inequalities, certifies precisely its covered intervals. It does not prove an infinite tail. Without a verified common-maximizer condition, an arbitrary pair of highly abundant integers is insufficient. Generating CA numbers by assuming consecutive ratios are always prime is not licensed.

A finite exact integer check extended to55440 is supplied separately, covering the initial range before the first CA endpoint above this conservative threshold in the source table. The global sparse criterion still requires ALL subsequent relevant support endpoints; no finite computation resolves RH.

Next independent tasks: check the full calculus proof, optimize the threshold if useful, and turn support parameters/tie choices into verifiable finite certificates with rational logarithm enclosures. The original broad globalCA equivalence is already in the literature; novelty of this explicit interpolation proof has not been established.
