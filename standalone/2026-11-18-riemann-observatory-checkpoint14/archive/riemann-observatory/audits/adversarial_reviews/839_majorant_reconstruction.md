# First-window majorant and close-pair reconstruction

17November2026. Proposer: analytic_frontier. Status: exact independent arithmetic passed; independent analytic review requested. Scope: the first-window majorant, separated-set Bessel bound and close-pair constants, not the full source theorem or a Lean build.

Source: Knausgård, arXiv2610.08965v1, §3 pp15–16; pinned repository0e961ea199b425010843bc8044676d4ad29fe031, Distinct839/Majorant/{Checker,Pointwise,Fourier,Separated}.lean. The source Pointwise file SHA256 is4426c7027430d7c82906e605a5cb65221fb5666c1ed5b5280b584bcb1241c9e2. The independent program compares its42 rational breakpoints with that exact source when the cache exists; offline the breakpoint list, coefficient array and source hash remain in the script/result.

Let theta=17/20, gamma0=607/1000 and

f(u)=[1+sum_(j=1..6)a_j cos(2pi j u)]1_{[-1/2,1/2]}(u),

a=(193305,−23105,29166,13952,−21009,41052)/10^6.

Let sinc(t)=sin(pi t)/(pi t), sinc(0)=1, and

S(u)=sinc(theta(u−1/2))+sinc(theta(u+1/2)), g(u)=gamma0 S(u)^2.

## Whole-interval exact check

On a source interval[l,r], take midpointm and halfwidthdelta. Machin's formula with100/40 alternating arctangent terms gives outward pi bounds at10^(-55). Evaluate trigonometric polynomials at the rational piQ=355/113 and retain the exact interval boundE>=|pi−piQ|.

For each cosine coefficient, reduce j*m by an integerk. Its true argument at u in[l,r] differs from2piQ(jm−k) by at most

2piUpper*j*delta+2E|jm−k|.

The global Lipschitz constant1 for cosine transports18-term lower/19-term upper alternating Taylor bounds, taking the coefficient sign into account. This gives f(u)<=fUp on the whole closed cell. All reduced evaluation arguments have absolute value at mostpiQ, and the omitted tails after18terms decrease; no first-term monotonicity assumption is needed.

For sinc_rad(x)=sin(x)/x=integral_0^1 cos(tx)dt, the derivative has absolute value at most1/2. At rational argumentpiQ*theta*(m+s), s=±1/2, the argument perturbation is at mostpiUpper*theta*delta+Etheta|m+s|. Its18-term even-power Taylor polynomial is a lower bound; the argument magnitude is below3 and the omitted alternating tail decreases. Subtract half the perturbation bound, sum the two sinc lower bounds to obtainS_low, then check S_low>0 andfUp<=gamma0*S_low^2.

All42 closed cells passed exact Fraction arithmetic, covering[0,1/2]. Evenness covers the negative half. f=0 andg>=0 outside the support. Thus f<=g on the whole real line. This is a different implementation with stronger Taylor orders and pi bounds than the source checker; the underlying elementary interval strategy is shared and must be judged mathematically.

## Fourier support and the separated-set estimate

With transform exp(−2pi iut),

S=Fourier(Psi), Psi(xi)=(2/theta)cos(pi xi)1_{[-theta/2,theta/2]}(xi).

Consequently ghat=gamma0(Psi*Psi), supported in[-theta,theta]. The convolution is continuous and zero at both support endpoints. Also

Lambda=ghat(0)=gamma0 integralPsi^2=(2gamma0/theta)(1+sinc(theta)).

The same exact Taylor/argument enclosure givesLambda<67/40=c/2 for c=67/20. If y_i are theta-separated, all off-diagonal ghat(y_i−y_j) vanish, including distance exactlytheta. Therefore for any finite complex vectorc,

integral f(u)|sum_i c_i exp(2pi i y_i u)|^2du
 <=integral g(u)|sum_i c_i exp(2pi i y_i u)|^2du
 =Lambda sum_i|c_i|^2.

This is the precise separated Gram operator bound used by the source; no informal spacing analogy is involved.

## Close pairs and scalar conditions

The already independently validated table has H=16384 and scaleV=2^28. Every t in[0,17/20] lies in one of cells0,...,13926. Their minimum integer entry is17657024, which is greater than the integer17648674 corresponding to beta=8824337/134217728. The whole-cell certificate therefore provesK(t)^2>=beta for |t|<=theta, including the final partial cell. No monotonicity of K is assumed.

The exact scalar checks are

c>2,4beta<(c−2)^2,

2beta>2x,4beta>x+y,8beta>2y,

with x=54350/10^6,y=69433/10^6. The first pair implies2+2sqrt(beta)<c. All passed. Exact output and input/source hashes are in experiments/results/839_majorant_check.json; replay with python experiments/code/839_majorant_check.py takes about0.2s.

The source's analytic operator in §3 is the finite continuous Hilbert-space construction also used by Lamzouri, with fixed smoothingepsilon beforeT tends to infinity, thenepsilon tends to0. It does not use the AF finite Gabor grid. Thus our separate AF no-buffer repair must not be presented as a missing step in this source. This majorant certificate is one of several distinct premises for Knausgård's theorem; original-search success, local-to-global transfer, clipped matrix inequalities and the externally established pair-correlation moment retain their own audit scopes.
