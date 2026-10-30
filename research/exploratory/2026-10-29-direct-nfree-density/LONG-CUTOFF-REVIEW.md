# Review of extending the fixed-field detector cutoff to 5/2

The gamma-convolution and buffered zero detector in [UNIFORM-DETECTOR-PROOF.md](UNIFORM-DETECTOR-PROOF.md) extend, with the same stated classical Hecke/FHL inputs, to any fixed bounded cutoff `1<t≤5/2`. This is a source-level review of the proof's quantifiers; it is not a claim that OpenAI's printed proposition states that wider interval.

The fixed-buffer Euler-log and functional-equation estimates are independent of t. The Mellin annular pointwise bounds allow every r,m in a fixed bounded range, including m>1; the reflected ordinary bound then has a potentially negative exponent, with its tails handled on the absolute line. Their contour losses are `O(e r)+O(e m)`, absorbed uniformly once e is chosen for the bounded range. In the gamma convolution the truncated inverse length is `D*=X^t`; its contribution to the left-line bound is only a fixed polynomial in X for t≤5/2. Choose the auxiliary exponential scale `X^B` with B larger in terms of 5/2 and the fixed strip-growth order. The dyadic lengths and number of blocks remain bounded and logarithmic, respectively. Choose the finite Sobolev derivative orders before τ and the external Fourier-tail order after τ. No use of t<3/2 occurs in the product-cutoff Fourier separation or the common frequency budget.

The same comparison of the gamma-convolution lower bound against the pointwise inverse and plain bounds gives `δ_a[m−min(m,1−m)]≪η`, hence `m≤1/2+O(η)` for the fixed positive floor, and gives both individual witness lower bounds after dividing by the opposite pointwise estimate. In particular `t−1/2−O(η)≤r≤t+O(η)` remains valid. The common-profile Sobolev and squarefree-kernel decomposition have the same fixed number of derivatives; larger bounded D only changes polynomial scale constants.

For the high-δ scalar application let `1−1/n<δ<1` and

    t=(5−n(1−δ))/2,        R=(1−δ)t.

Then `2<t<5/2`, and saturation confines r to `[t−1/2,t]` up to arbitrarily small losses. For the four exact Θ_n faces on this interval, f₃ dominates for r≤2, f_D dominates for r≥2, f₃ decreases and f_D increases. Their values at r=t−1/2 and r=t both equal R. Thus the inverse witness alone gives exponent R. No equality `m=t−r` or new mixed-moment assumption is used.

The ordinary Hecke continuation, fixed-strip growth, FHL conductor/masks and de Faveri's printed sieve remain external inputs. The stated argument is a fixed-field, fixed-parameter result; it makes no uniform claim as δ approaches an endpoint or as the field/order varies.
