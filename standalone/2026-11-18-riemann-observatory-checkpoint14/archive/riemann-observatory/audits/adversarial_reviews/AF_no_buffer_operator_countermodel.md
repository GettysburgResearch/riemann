# Synthetic countermodel: unbuffered operator error need not vanish

Reviewer: semantic_skeptic. Date: 17 November 2026. Independently reconstructed from the proposed claim by direct Fourier integration and norm estimates. No build or numerical computation is used. This is a countermodel for an inference from the **abstract window/strip/local-count hypotheses**, not an assertion about actual zeta zeros or a counterexample to any proportion theorem.

## Exact family

Fix any smooth nondecreasing real chi with chi(s)=0 for s<=0 and chi(s)=1 for s>=1. For L>2 let

phi_L(u)=chi(L/2+u)chi(L/2-u),

F_L(w)=integral_R phi_L(u) exp(iwu)du,

a_L=L^(-1) integral_R phi_L(u)^2du.

Then phi_L is real, even, smooth, supported in[-L/2,L/2], lies in[0,1], and equals1 on[-L/2+1,L/2-1]. Therefore1-2/L<=a_L<=1 and a_L tends to1. Its first and second derivative L1 norms are bounded uniformly in L: the two transition regions are disjoint and are translates/reflections of the fixed chi derivatives. Thus the ordinary critical-sampling and uniform C2 Fourier-decay hypotheses used by the localization argument hold.

Take

L=log(T/(2pi)), h=2pi/L, d=floor(T/h),

alpha_k=T+kh, 0<=k<d, I=[T,2T), eta=1/4.

Place a multiplicity-one conjugate pair of synthetic gamma points

z_plus=T-h+i eta, z_minus=T-h-i eta.

Both real parts lie just outside I. Add d real points alpha_0,...,alpha_(d-1) inside I if a normalization N(I)~TL is desired. The number of points in any unit ordinate interval is O(L), uniformly in T, and every window is finite. The set is invariant under gamma conjugation. These are synthetic points; no zeta functional equation or explicit formula is asserted for this family.

Define v(z)_k=F_L(z-alpha_k), A_L=a_L L^2, and let the discarded pair matrix be

E_L=A_L^(-1)[v(z_plus)v(z_plus)^T+v(z_minus)v(z_minus)^T].

Since phi_L is real and even, F_L(conjugate(w))=conjugate(F_L(w)). Hence E_L is real symmetric. The added real points lie inside I and do not alter E_L.

## Independent check of the Fourier identity and sign

Put

J(s)=integral_0^1 chi'(u)exp(su)du.

For real s, J(s)>0: chi'>=0 and integral chi'=chi(1)-chi(0)=1. J is entire. On the left endpoint transition phi_L'=chi'(L/2+u); on the right it is minus the reflected derivative. Integration by parts, with zero endpoint boundary values, gives exactly

F_L(w)=[exp(iwL/2)J(-iw)-exp(-iwL/2)J(iw)]/(iw), w!=0.

Indeed integral phi_L'(u)exp(iwu)du equals

exp(-iwL/2)J(iw)-exp(iwL/2)J(-iw),

and also equals -iw F_L(w). This independently fixes the signs.

At w_L=z_plus-alpha_0=-h+i eta one has iw_L=-eta-ih and hL/2=pi. Therefore

exp(iw_LL/2)=-exp(-eta L/2),

exp(-iw_LL/2)=-exp(eta L/2),

so

exp(-eta L/2)F_L(w_L)
 =[J(-eta-ih)-exp(-eta L)J(eta+ih)]/(-eta-ih)
 tends to -J(-eta)/eta.

The limit is a strictly negative real number. Thus, writing c_eta=J(-eta)/eta>0,

Re(F_L(w_L)^2)~c_eta^2 exp(eta L).

In particular it is positive for all sufficiently large L; the argument does not replace the real part of a complex square by its absolute square without justification.

## Divergent operator norm

The00 entry of the real symmetric pair matrix is

(E_L)_00=2 Re(F_L(w_L)^2)/(a_L L^2)
 ~2 c_eta^2 exp(eta L)/L^2.

For eta=1/4, exp(eta L)=(T/(2pi))^(1/4). Consequently

||E_L||_op >= |(E_L)_00| tends to infinity.

The inequality follows by evaluating the Rayleigh quotient on the first standard basis vector. It does not require E_L to be positive semidefinite. This is an explicit obstruction to deducing ||E_0||_op=o(1) solely from the assumptions used in the unbuffered localization lemma.

## Relative Hilbert–Schmidt smallness still holds

A complex rank-one matrix vv^T has nuclear norm||v||_2^2. Parseval gives

sum_{k in Z}|F_L(z_plus-alpha_k)|^2
 =L integral phi_L(u)^2 exp(-2 eta u)du
 <=(L/eta)sinh(eta L).

Therefore

||E_L||_HS<=||E_L||_1
 <=2 sinh(eta L)/(a_L eta L)
 =O(exp(eta L)/L).

With N(I)=d~TL/(2pi),

||E_L||_HS/sqrt(N(I))
 =O(T^(eta-1/2)/L^(3/2)) tends to0.

Thus the same family simultaneously has a divergent operator error and a vanishing relative Hilbert–Schmidt error. A transfer argument requiring only the latter can remain valid; a Weyl step requiring an operator perturbation tending to0 cannot be imported from it.

## Scope of symmetries and zero-free strips

In rho coordinates, rho=1/2+i gamma, the pair has real parts1/4 and3/4. These lie inside any Vinogradov–Korobov strip[delta(t),1-delta(t)] for all sufficiently large T because delta(t) tends to0. Thus adding that strip hypothesis alone does not force this abstract operator error to vanish. This observation does not claim actual zeta zeros with those real parts exist.

If both usual gamma symmetries are wanted, add the negative-ordinate mirrors of all points. The negative pair and negative real points are a distance comparable to T from the retained grid. Uniform Fourier decay bounds their contribution to the00 entry by O(exp(eta L)/(L^2 T^4))+O(1/(L T^3)), negligible beside exp(eta L)/L^2. Their total nuclear contribution is also negligible. Hence the operator divergence survives that extension. No full zeta explicit-formula or prime-moment model is constructed or claimed.

## One fixed multiset, rather than a varying family

The preceding construction already disproves a bound uniform over all admissible models at each height. To exclude a quantifier mistake, the operator-norm failure can also be realized by **one fixed infinite synthetic multiset**, along a sequence of heights.

For t>2pi*e set

Q(t)=t/(2pi)[log(t/(2pi))-1].

It is strictly increasing from0 to infinity. Let b_j be its unique inverse value at the positive integer j. Put real gamma points at every b_j and -b_j, all with multiplicity1. This critical background has positive-ordinate count floor(Q(t)) and unit-interval count O(log(|t|+3)). Its dyadic count is

Q(2T)-Q(T)+O(1)
 =T/(2pi)[log(T/(2pi))+2log2-1]+O(1),

the usual Riemann–von Mangoldt main term.

Now fix, once and for all,

T_n=2pi*exp(n^2), L_n=n^2, h_n=2pi/n^2,

r_n=T_n-h_n,

and add the four points r_n+i eta, r_n-i eta, -r_n+i eta, -r_n-i eta for every sufficiently large integer n. The entire multiset is fixed independently of the height T used in the window construction. It is invariant under conjugation and negation, lies in the fixed strip |Im gamma|<=eta=1/4, and has finite windows. The sparse off-line pairs add at most O(1) points to each sufficiently large unit interval and dyadic interval. Cumulatively they add O(sqrt(logT)), so the usual cumulative main term still has error O(logT). In particular N([T,2T))~TL/(2pi).

At T=T_n the positive pair with index n gives the positive00 asymptotic already derived. All other off-line points lie a distance comparable to T_n or more from the first sample alpha_0=T_n: earlier positive points and all earlier negative points are at distance at least T_n/2, while later pairs are much farther. Uniform C2 Fourier decay yields

sum_{other off-line z}|F_{L_n}(z-T_n)|^2
 <=C exp(eta L_n)[n/T_n^4 + sum_{m>n}r_m^(-4)]
 =O(exp(eta L_n)n/T_n^4).

After normalization by a_L L_n^2, this is negligible compared with the near-pair scale exp(eta L_n)/L_n^2. The contribution of every excluded **real** background point to the00 entry is nonnegative, since F_L is real on the real axis. Therefore the full discarded matrix for this fixed multiset still satisfies

(E_0(T_n))_00 >=(2 c_eta^2+o(1))exp(eta L_n)/L_n^2,

and its operator norm diverges along T_n. Absolute nuclear convergence follows from the same global local-count/decay estimates used by the localization lemma.

For completeness, applying the localization argument with the fixed narrower strip |Im gamma|<=eta gives ||E_0(T)||_1=O(exp(eta L))=O(T^(1/4)): near endpoint strips have O(L) points and normalized Parseval mass O(exp(eta L)/L); distant strips have the summable D^(-3) bound. Consequently

||E_0(T)||_HS/sqrt(N([T,2T)))=O(T^(-1/4)/sqrt(L)) tends to0.

All off-line rho real parts are1/4 or3/4, so this fixed multiset also satisfies the eventual Vinogradov–Korobov strip condition. It is not constructed to satisfy the zeta explicit formula or prime-side moment. The countermodel shows that **even these strip, symmetry, local-count and Riemann–von Mangoldt counting properties do not imply an unbuffered operator error tending to0**. Additional analytic information could still force that property for actual zeta zeros; no conclusion about their existence or operator error is asserted here.

Classification: **explicit counterexample to an altered inference**, not a verified error in a source theorem. The permissible conclusion remains relative-Hilbert–Schmidt control; obtaining an o(1) operator error requires an additional argument or stronger truncation.
