# Coherent volume for squarefree-label primitive continuation

23 October2026. Proposed extension, final independent review requested.
The frozen all-sixth-free CP theorem remains unchanged at SHA256
bb321aae05c906187371ea7cd7a01062b19f0c0a2d889b3106c4d6e48eaaeca4.
This additional theorem is restricted to SQUAREFREE labels. It does
not claim the new volume treatment for fifth-power label branches.

With the same actual Möbius coefficient, fixed profiles, ray sectors,
punctures, natural zeros and upstream inputs, the proposed improvement is
\[
 \sum_{\substack{NR\le K\\R\ {\rm squarefree}}}
 |\mathcal P_R(U)|^2
 \ll ((2+U)DKNQ)^\epsilon
 [U+D^{11/12}K^{1/12}+D^{5/6}K^{7/6}],
 \quad K\le D^{1/7},\ U\ge1.                         \tag{CV1}
\]
The partial-pole term is deliberately left at its already reviewed
scalar cost. No improvement of the complementary operator follows.

## 1. Common-row support estimate and low-divisor volume

Use root's retained-support finite bound
LOCAL_SUPPORT_VECTOR_REFINEMENT.md, SHA256
499e1333611699c91a6c3b2cf5376f5b702bca74254b222bab47fdc93043f1dc.
In CP's notation, a fixed common inverse-row multiplier q0 prime to
the remaining label changes the physical column length to L/q0.
The same local-support proof gives the positive bound
\[
 \lambda^2(1+B\sqrt{q_0/L})I(L,X),\qquad B=K/A_R.
                                                               \tag{CV2}
\]
The volume part is lambda²[L+B sqrt(q0 L)].
Here the remaining label's full-modulus shared factors retain their
actual physical support; no arbitrary row-dependent phase is allowed.

First aggregate e into r=e²c0 as in V8, on an e-dyad.
The free column length depends on that dyad and is separated smoothly.
The scalar changes from lambda to e*lambda and q0 loses e².
The main and mixed volume weights are consequently E^0 per dyad;
the nonvolume weights still decay. This is not a sum of E separate
amplitude bounds.

Use CP5 and put
\[
 B_*=U^{1/3}(DK)^{-1/6}P^{-1}.
\]
The range with nonempty reflected head has d0<=B_*/(fk²).
Its main volume sums to amplitude
sqrt(U) P^-1/2 G^-1/2 S^-1/2 times convergent ordinary factors.
The squared selected weights sum with subpower cost.

Its mixed volume before summing d0 has amplitude
\[
 D^{1/8}K^{5/8}P^{1/4}G^{-1/2}A_R^{-1/2}t_{\rm out}^{1/4}S
 k^{-1}f^{-9/4}d_0^{1/4}v_0^{-1/2}.
\]
After the d0 cutoff it is at most
\[
 D^{-1/12}K^{5/12}U^{5/12}
 P^{-1}G^{-1/2}A_R^{-1/2}t_{\rm out}^{1/4}S
 k^{-7/2}f^{-7/2}v_0^{-1/2}.                          \tag{CV3}
\]
The selected outside-modulus amplitude exponent is at most-1;
the inside-modulus exponent is at most-1/2. Their squares are
summable or logarithmic after divisor Cauchy per original label.
Thus the squared mixed cost is D^-1/6 K5/6 U5/6, which is at most U
because K5<=D<=DU in the stated range.

## 2. The empty-head range: a second, exact aggregation

The preceding cutoff calculation alone is insufficient. Above it,
the original-only mixed amplitude summed separately in d0 would
restore KU. Instead aggregate BOTH e and d0 into
\[
 w=e d_0,\qquad r=w^2c_0.
\]
This is legitimate specifically on the original-only branch:
\[
 d^2c=(fd_0)^2(e^2f^4c_0)=f^6r.                     \tag{CV4}
\]
Hence its physical test depends on r and fixed f,k,a, not on the
partition of w into e and d0. The free Möbius length is
D/(G w f v0), depending only on the w-dyad. The partitions of w
are divisor-many column coefficients, and the empty-head condition
is retained as a column restriction on those partitions.
The two free characters use the same row r*t_out*S6.
Their zeros enforce every d0/R0 and d0/free-column coprimality
condition. No new free-column arithmetic coefficient is introduced.

The scalar changes by e*d0, while q0 becomes t_out*S6.
The main original volume is O(U) after the convergent fixed-factor
sums and the selected-label divisor Cauchy. The mixed original volume
has squared base K sqrt(U). Selected outside-modulus squared weights
are at most p^-1; inside-modulus squared weights are at most1.
Their positive sum costs at most K times a subpower. Therefore this
entire mixed tail costs
\[
                         K^2\sqrt U\le U,           \tag{CV5}
\]
since U>=sqrt(DK) and K<=D1/7 imply U>=K4.

The nonvolume part of this SAME aggregated bound must also be
controlled. Its amplitude before the k and w-dyad sums is
\[
 D^{5/12}U^{1/12}P^{-1/2}G^{-11/12}S^{-1/2}
 k^{-3/2}f^{-29/12}w^{-5/12}v_0^{-11/12}.             \tag{CV6}
\]
The empty-head condition forces w>=B_*/(fk²).
Summing the w-dyads gives
min(1,(B_*/(fk²))^-5/12). The elementary ideal sum
\[
 \sum_k k^{-3/2}\min(1,(B_*/k^2)^{-5/12})
 \ll B_*^{-1/4}                                    \tag{CV7}
\]
follows by splitting at sqrt(B_*); for B_*<1 use the full convergent
k-sum and 1<=B_*^-1/4. Retaining f changes its exponent to-13/6,
still summable, and dropping v0^-11/12 only enlarges the bound.
Substitution into CV6 gives exactly
D11/24 K1/24 P^-1/4 G^-11/12 S^-1/2, with summable factors.
Selected outside-modulus factors are aggregated by the restricted
inverse-row procedure of CP4; inside-modulus squared weights cost
at least S^-3/2. Thus the nonvolume part is bounded by CP's middle
term, rather than importing it from an incompatible estimate.

The original and reflected completion ideals retain their weights.
The mixed volume b-weight is b^-5/2, so that completion sum converges.
The high-tail plateau has w^-5/12 per w-dyad and a k^-1 weight.
The original finite support restricts k to O(U1/6), so this costs
only a subpower; no infinite k^-1 convergence is asserted.
The exact subunit pole tails are still those of the frozen CP proof.

## 3. Conclusion and example

For U>=sqrt(DK), CV3--CV7 replace CP's KU by U. All other CP
nonvolume and partial-pole bounds remain valid. For smaller U,
CP's direct primitive finite-minus-pole argument already bounds
the whole expression by D11/12K1/12+D5/6K7/6.
This proves CV1.

With the same Gram hypotheses as CP8, the actual squarefree-label
projection is consequently bounded by
\[
 U+D^{11/12}K^{1/12}+D^{5/6}K^{7/6}+U^{1/3}D^{2/3}.  \tag{CV8}
\]
For U=D6/7 and K=D1/10, its four exponents are
6/7,37/40,19/20,20/21. The maximum is20/21, still a saving1/42
relative to the inherited inverse nonvolume exponent41/42.
The labels grow asD1/10. The complementary inverse vector remains
uncontrolled, and neither a smaller B_flat nor RH is concluded.

