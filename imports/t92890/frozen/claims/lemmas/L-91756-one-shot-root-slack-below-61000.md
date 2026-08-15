# L-91756 — The one-shot root slack has absolute native cost below 61000

Claim ID: `L-91756`  
Status: **PROPOSED COMPLETE DIRECT NATIVE-COST THEOREM — REVIEW REQUIRED**  
Created: 2026-08-15  
Depends on: `L-91378`, `L-91755`, `L-91733`, `L-19885`, `L-19887`, `L-91115`  
Does not depend on: `J_Lambda(X)-4sqrt(X)=O(log X)`  
RH status: **unproved at this claim**

Let

\[
\delta_X=\sum_qY_4(q)r_X(q)
 =J_\Lambda(X)-\mathcal H(d_X).
\]

## 1. Exact cost decomposition

Before thinning, the native-detail difference is the sum of:

```text
bottom and top omitted positive endpoint rows;
retained-cell finite/continuum comparison;
intrinsic martingale collar;
terminal comparison vector.
```

All Hall, first-owner, causal-current, and internal-child operations are exact
in the total component row and create no additional native deficit.

After thinning,

\[
\begin{aligned}
\delta_X\le{}&(1-\tau_K)J_\Lambda(X)\\
&+\mathcal H(o_X^{\rm bot})+\mathcal H(o_X^{\rm top})\\
&+\sum_qY_4(q)
 (|e_X^{\rm mis}(q)|+|e_X^{\rm col}(q)|+|e_X^{\rm term}(q)|).
\end{aligned}
\]

Every term is named before estimation; no unspecified `O(1)` base or port is
imported.

## 2. Square-root thinning

The elementary Chebyshev theorem `L-19887` gives

\[
J_\Lambda(X)<16(\log2)\sqrt X.
\]

Hence

\[
\boxed{(1-\tau_K)J_\Lambda(X)<12012.}
\]

## 3. Nonterminal comparison

For `L=log(2X)`,

\[
\sum_{q\le X}\frac{Y_4(q)}q\le3+2L+2L^2.
\]

The all-column mismatch plus intrinsic collar therefore costs at most

\[
\frac{971}{4\sqrt K}(3+2L+2L^2)=o(1),
\]

which is less than `4` for `X>=10^12`.

## 4. Terminal comparison

The terminal vector is bounded by `4452X^{-3/2}`. Since

\[
\sum_{q\ge2}\frac{Y_4(q)}{q^{3/2}}<11,
\]

its complete native cost is less than

\[
4452\cdot11=48972.
\]

## 5. Omissions

The endpoint score derivative obeys

\[
\dot H(s)<\frac8{\sqrt s},
\]

and the equality density is below two. The only bottom omission is the width-two
transition strip beginning at `K`; all deeper inner source is present as an
internal causal-child colour. The top omission has fixed width `W+2`.

Thus for `X>=10^12` the combined omission score is less than one. The positive
martingale quantizer is score-favourable.

There is no auxiliary port and no large-endpoint finite base correction.

## 6. Uniform bound and strict NRCT debt

Combining the previous sections,

\[
\boxed{0\le\delta_X<12012+4+48972+1<61000.}
\]

For `X>=10^12`,

\[
61000<2(4\sqrt X-3).
\]

Hence the original current-debt clause and the equivalent bounded
weighted-slack clause of NRCT both hold.

```text
circular benchmark bridge                 absent
square-root thinning cost                 <12012
nonterminal comparison                    <4 at X>=1e12
terminal comparison                       <48972
omissions                                 <1
auxiliary port/base                       zero in large-X theorem
root native slack                         <61000
NRCT current debt                         strict
```
