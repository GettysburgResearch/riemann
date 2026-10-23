# The coherent full remainder bound at every physical scale

23 October 2026. This extends, without changing its frozen bytes,
COHERENT_FULL_REMAINDER_VECTOR.md, SHA256
f6058c80c4bde0f049f7f7a50740cfae4d4a158a88e1bc6c0cb8534be8f215a4.
Root identified the direct small-scale argument below.

Under exactly its hypotheses on coefficients, labels, profiles and
sources, the conclusion C1 holds for every \(U>0\):

\[
 \sum_{\substack{NR\le K\\R\ {\rm sixth\!-\!power\!-\!free}}}
       |\mathcal R_R(U)|^2
 \ll(DKNQ\max(1,U,U^{-1}))^\epsilon
       \{D^{11/12}K^{1/12}+D^{5/6}K^{7/6}\},
 \qquad 1\le K\le D^{1/7}.                              \tag{A1}
\]

For \(U\ge\sqrt{DK}\), this is C1. For \(1\le U<\sqrt{DK}\),
use the exact raw identity

\[
 \mathcal R_R(U)=S_R^{\rm phys}(U)
                 -\widehat w(2/3)U^{1/6}P_R(D).
\]

The finite-vector bound V4 and its sixth-free extension imply the
weaker uniform majorant

\[
 \sum_R|S_R^{\rm phys}(U)|^2
 \ll(UDKNQ)^\epsilon
       \{U+D^{5/6}U^{1/6}+K^2+D^{5/6}K^{7/6}\}.       \tag{A2}
\]

For completeness: below K use the K alternative in V4; between K
and K^2 use \(1+K^2/U\); above K^2 use its constant bound. These
three ranges prove A2. C2 bounds the squared pole contribution by
\(U^{1/3}D^{2/3}\).
At \(U\le\sqrt{DK}\), the first two terms of A2 are at most
\((DK)^{1/2}\) and \(D^{11/12}K^{1/12}\); the pole term is at most
\(D^{5/6}K^{1/6}\). The remaining dominations are those in C1.

Below the fixed physical support threshold the finite sum is exactly
zero and only the displayed negative pole remains. Any bounded
interval of positive U between that threshold and1 is covered by
the same support argument and a fixed enlargement of the unit ball.
Thus no inverse estimate on an empty subunit row ball is invoked.

The harmless U^(-epsilon) allowance in A1 is useful when summing
scaled terms. It does not assert growth of the raw remainder at0:
there the exact identity is a constant times U^(1/6) times its residue.

One consequence is that a denominator supported on a row label can
be treated after the analytic bound. If \(k\) is supported on R and
has outside coefficient \((Nk)^{-1}\), weighted Cauchy with any fixed
\(0<\delta<1\) gives

\[
 \left|\sum_{\operatorname{rad}(k)\mid R}
          (Nk)^{-1}F_{R,k}\right|^2
 \le
 \left(\sum_{\operatorname{rad}(k)\mid R}(Nk)^{-\delta}\right)
 \sum_{\operatorname{rad}(k)\mid R}(Nk)^{-2+\delta}|F_{R,k}|^2.
\]

The first factor is at most \((NR)^\epsilon\), with an
epsilon-dependent constant. If every fixed-k family has the same
A1 bound and profile seminorms, sum R and k, drop the remaining
label-support restriction only from the resulting nonnegative sum,
and use convergence of \(\sum_k(Nk)^{-2+\delta}\), allowing a smaller
internal epsilon for the scaled physical parameter.
This observation does not by itself prove that every simultaneously
inverted primitive family satisfies the fixed-k hypothesis.
