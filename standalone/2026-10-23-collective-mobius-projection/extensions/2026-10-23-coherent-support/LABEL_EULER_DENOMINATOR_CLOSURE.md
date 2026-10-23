# The label-supported Euler denominator preserves the coherent vector estimate

23 October 2026. This is a deduction for the full-series vector. It does not supply the selected-prime part of primitive inversion.

Use `COHERENT_FULL_REMAINDER_VECTOR.md`, SHA256 `f6058c80c4bde0f049f7f7a50740cfae4d4a158a88e1bc6c0cb8534be8f215a4`. Write its full raw contour vector as `R_R(U)`, where the good labels `R` are sixth-power-free, `NR<=K<=D^(1/7)`, and the free Möbius column has length `D`. Set

\[
 B(D,K)=D^{11/12}K^{1/12}+D^{5/6}K^{7/6}.
\]

For any phases `omega(R,k)` of modulus at most one, define

\[
 T_R(U)=\sum_{\operatorname{supp}k\subseteq\operatorname{supp}R}
       \frac{\omega(R,k)}{Nk}\,R_R(U/(Nk)^6).          \tag{E1}
\]

The phases are outside the defining free-column sum. There is no additional `k`-dependence in its arithmetic coefficients or smooth test. Then

\[
 \sum_{NR\le K}|T_R(U)|^2
   \ll (UDKNQ)^\epsilon B(D,K),\qquad U\ge\sqrt{DK}.   \tag{E2}
\]

All smooth profiles, fixed ray data and punctures are those of the input theorem. The same conclusion holds with a fixed finite sum of such profiles.

For each label,

\[
 \sum_{\operatorname{supp}k\subseteq R}(Nk)^{-1}
    =\prod_{p\mid R}(1-(Np)^{-1})^{-1}\ll_\epsilon K^\epsilon.
\]

Weighted Cauchy, followed by exchanging the positive sums, therefore gives

\[
 \sum_R|T_R(U)|^2\ll K^\epsilon
 \sum_k(Nk)^{-1}\sum_{\substack{NR\le K\\\operatorname{rad}k\mid R}}
                 |R_R(U/(Nk)^6)|^2.                  \tag{E3}
\]

The support condition can now be dropped from the inner nonnegative sum. This step is not an assertion that the character or the original Euler factors have lost their zero masks.

Put `A=U^(1/6)(DK)^(-1/12)>=1`. For `Nk<=A`, the input full-vector theorem applies at `Y=U/(Nk)^6>=sqrt(DK)`. The sum of `1/Nk` in this finite range is logarithmic. This proves E2 for the head.

For the tail use the exact original identity

\[
 R_R(Y)=S_R(Y)-c_wY^{1/6}P_R(D),                      \tag{E4}
\]

where `S_R` is the original raw finite sum. Its sixth-free label sieve implies the coarse bound

\[
 \sum_R|S_R(Y)|^2\ll(YDKNQ)^\epsilon
 [Y+D^{5/6}Y^{1/6}+K^2+D^{5/6}K^{7/6}].             \tag{E5}
\]

For clarity, E5 follows directly from `min(K,1+K^2/Y)(Y+D^(5/6)Y^(1/6))`: below `Y=K`, use the first alternative; above it use the second, whose additional nonvolume term is maximized at `Y=K`. The original annular sum is zero below a fixed positive support threshold. The full pole vector satisfies `sum_R|P_R(D)|^2<<D^(2/3+epsilon)`.

The volume and nonvolume tail sums in E3 are respectively

\[
 U\sum_{Nk>A}(Nk)^{-7}\ll U A^{-6}=(DK)^{1/2},
\]
\[
 D^{5/6}U^{1/6}\sum_{Nk>A}(Nk)^{-2}
       \ll D^{5/6}U^{1/6}A^{-1}=D^{11/12}K^{1/12}.
\]

The two plateau terms are summed only up to `Nk<<U^(1/6)`, by the exact support of `S_R`, so their `1/Nk` sum costs a logarithm. The pole has no such support cutoff; its entire infinite tail instead gives

\[
 D^{2/3}U^{1/3}\sum_{Nk>A}(Nk)^{-3}
       \ll D^{2/3}U^{1/3}A^{-2}=D^{5/6}K^{1/6}.
\]

All costs are absorbed by E2 in the stated range. Small epsilon losses in the input bounds are chosen first below the final epsilon; they are harmless in each strictly summable tail. This also justifies passage from finite partial sums in E1 to its limit.

In the original Mellin variable `u`, multiplying a full-series component by

\[
 \prod_{p\mid R}(1-\nu(p)^6(Np)^{5-6u})^{-1}
\]

has precisely the form E1, with `omega(R,k)=nu(k)^6`. Thus this denominator alone does not lose a factor `K` in the coherent vector theorem. Applying E2 after selected-prime transformations still requires proof that the transformed family has the same free coefficient, label norm and common profile. In particular, E2 does not justify reducing a full continuous numerator modulo sixth powers or discarding a moving puncture.
