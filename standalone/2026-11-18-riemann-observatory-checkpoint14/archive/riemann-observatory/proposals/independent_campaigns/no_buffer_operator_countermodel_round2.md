# Why relative Hilbert–Schmidt control does not give a small operator tail

Status: proposed elementary countermodel, independent review requested. Scope: abstract sampling/localization hypotheses; these points are not asserted to be zeta zeros. This does not challenge the director-accepted no-buffer transfer, which needs only a tail small relative to sqrt(N).

Fix any smooth nondecreasing cutoff chi with chi(s)=0 for s<=0 and chi(s)=1 for s>=1. For L>2 put

T=2pi exp(L), h=2pi/L, d=floor(T/h),

phi_L(u)=chi(L/2+u)chi(L/2−u).

This is an original-type fixed-taper indicator window: real, even, smooth, bounded by1, supported in[-L/2,L/2], with uniformly bounded first and second derivative L1 norms. Its normalization a_L=||phi_L||²/L tends to1. Thus the uniform Fourier decay and Parseval hypotheses of the localization lemma hold.

Let eta=1/4 and r=T−h. Put a conjugate pair of gamma-points r+i eta and r−i eta outsideI=[T,2T), with multiplicity1 each. Add the d real points alpha_k+h/2,0<=k<d, insideI. This finite conjugation-invariant family has N(I)=d asymptotic to TL/(2pi) and a uniform global unit-interval count O(log(|t|+3)). Every gamma-point has |Im gamma|<=1/4; it even satisfies the named Vinogradov–Korobov strip for all large T, because its delta(T) tends to0. It need not satisfy the explicit formula or the prime-side moment, which are outside the geometric localization hypotheses.

Let F_L(w)=integral phi_L(u) exp(iwu)du and J(s)=integral_0^1 chi'(u) exp(su)du. Since chi' is nonnegative with integral1, J(-eta)>0. The endpoint transitions do not overlap when L>2. Integration by parts gives the exact formula

F_L(w)=[exp(iwL/2)J(-iw)−exp(-iwL/2)J(iw)]/(iw), w!=0.

At w=-h+i eta one has

exp(-iwL/2)=-exp(eta L/2),

exp(iwL/2)=-exp(-eta L/2).

Continuity of J and h->0 therefore imply

exp(-eta L/2) F_L(-h+i eta) -> -J(-eta)/eta.

The limit is nonzero and real. Evenness/reality gives F_L(conjugate w)=conjugate(F_L(w)). Consequently the excluded pair's normalized matrix has its0,0 entry

(E_0)_(0,0)=2 Re(F_L(-h+i eta)^2)/(a_L L²)

asymptotic to [2J(-eta)^2/eta²] exp(eta L)/L²,

which tends to positive infinity. Hence ||E_0||_op>=|(E_0)_(0,0)| does not tend to0. Adding the real bulk changes G_0 but not E_0.

There is no conflict with the relative-norm estimate: absolute Parseval at the smaller strip width eta gives ||E_0||_1=O(exp(eta L)/L), and sqrt(N) has size exp(L/2)sqrt(L). Their ratio tends to0. The sharper VK upper bound also allows this family: exp(L/4)/L is much smaller than exp(L/2−cL^(1/3)/(logL)^(1/3)).

This explicitly prevents reusing the no-buffer argument in a statement that requires ||E||_op=o(1), such as a direct vanishing-threshold Weyl transfer. The original growing buffer can supply stronger operator control; our accepted simplification only removes it from the specific trace/Hilbert–Schmidt chain in AF section6. The countermodel is about sufficiency of abstract assumptions, not an assertion that the actual zeta tail has diverging operator norm.

## Independent fixed-multiset strengthening

The independent reviewer checked all signs and supplied a stronger quantifier form in audits/adversarial_reviews/AF_no_buffer_operator_countermodel.md. Define a single real critical background by inverse values ofQ(t)=t/(2pi)[log(t/(2pi))−1], and add sparse off-line quartets at±(2pi exp(n²)−2pi/n²)±i/4. AlongT_n=2pi exp(n²), the near pair gives the same divergent diagonal; all other quartets have Fourier-square contributionO(exp(n²/4)n/T_n^4), before the common normalization. Real background contributes nonnegatively to the diagonal.

This one fixed multiset has the Riemann–von Mangoldt main term withO(logT) error, global unit countsO(log(|t|+3)), conjugation and negation symmetry, and eventual compatibility with the classical zero-free strip. Its operator error diverges alongT_n, while the relative Hilbert–Schmidt error tends to0. The proposer independently checked the sparse-distance bounds and inverse-count normalization. Director adjudication accepted the scoped negative control; no actual-zeta or explicit-formula model is claimed.
