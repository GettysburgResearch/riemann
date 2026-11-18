# Independent check of Hilbert–Schmidt certificate transfer

2026-11-17. Reviewer `/root/li_skeptic`. The clipping construction, sign directions and exact polynomial algebra were reconstructed from the statement before reading the completed advocate proof. The full proof `audits/adversarial_reviews/hilbert_schmidt_moment_transfer_round3.md` was subsequently read. Classification: **independently checked with no issue found in the inspected argument**. No arithmetic moment estimate, RH result, or priority claim is made.

For same-dimension Hermitian matrices `F,G` with sorted eigenvalues, Hoffman–Wielandt and Cauchy–Schwarz give

\[
 |d^{-1}\operatorname{Tr}h(F)-d^{-1}\operatorname{Tr}h(G)|
 \le \operatorname{Lip}(h)\|F-G\|_{HS}/\sqrt d.
\]

The supplied elementary rearrangement proof of Hoffman–Wielandt works for arbitrary signed real eigenvalues and does not assume commutativity. Thus a normalized Hilbert–Schmidt error tending to zero transfers bounded Lipschitz tests and hence weak spectral limits. It need not transfer unbounded polynomial moments; the supplied rank-one outlier example was checked algebraically.

If a fixed real polynomial `q` satisfies `q<=1_(0,infinity)` everywhere, set `h=max(q,-1)`. The maximum of these two minorants is still a minorant, and `h>=q`. A nonconstant polynomial bounded above on all of the real line has even degree and negative leading coefficient, so its set `{q>=-1}` is compact. Its derivative is bounded there; outside this set the clipped function is constant. This proves global Lipschitz continuity, including transitions, and `-1<=h<=1`. Therefore functional calculus gives exactly

\[
 n_+(G)/d\ge d^{-1}\operatorname{Tr}q(F)
       -\operatorname{Lip}(h)\|F-G\|_{HS}/\sqrt d.
\]

Both the clipping direction and the use of **F's** polynomial moments are correct. No moment transfer for `G` is needed. Keeping the polynomial fixed before the dimension limit is essential.

For `p=1-7x/4+2x^2/3`, `q=1-p^2` is a valid minorant because `p>=1` for `x<=0`. The exact identity

\[
 (p')^2=\tfrac83(p+19/128)
\]

gives on the active set `q>=-1`, where `|p|<=sqrt2`,

\[
 (q')^2=\tfrac{32}3p^2(p+19/128)
 \le\tfrac{64}3(\sqrt2+19/128)<211/6<36.
\]

Thus `Lip(h)<=6`. Expansion gives coefficients `(7/2,-211/48,7/3,-4/9)`. At moments `(1,4/3,2,13/4)` their sum is `31/36`; the stated conditional charge `2(31/36)-1` is `13/18`. These exact computations were independently replayed using rational arithmetic in `experiments/code/sine_gram_skeptic_exact_round4.py` and its results JSON.

With only the first two limiting moments and `D=84m3-16m4`, the polynomial value is `(D-85)/36+o(1)`. The proposed simple-zero charge consequently becomes `(D-103)/18+o(1)` after dimension normalization and a vanishing Hilbert–Schmidt error. The threshold to exceed `2/3` is `liminf D>115`, as stated. Its needed boundedness follows from this eventual lower bound together with `limsup D<=121`, the latter being the consequence of the universal inequality `q<=1` and the first two moments. Without a lower bound, `D` need not be bounded below, so the dimension-factor caveat in the proof is appropriate.

For the all-fixed-moments implication, even moments supply tightness and uniform integrability. The exponential-moment/Carleman sine law is Hamburger determinate, so no positivity of the approximating Hermitian matrices is needed. Weak transfer to `G` and the closed-set Portmanteau inequality for `(-infinity,0]` give `n_+(G)/d->1` because the limit is supported on the nonnegative line and has no atom at zero. Full model moment existence is now supplied by `THM-SG309`; prime-side matching, exact block geometry and the charge inequality remain distinct conditional arithmetic inputs.
