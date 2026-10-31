# The absolute anchor budget cannot reach the complete regime

Status: proposed source-specific obstruction theorem and an exact positive-model control. This supersedes the suggestion in the previous packet that bounding its positive-part transport integral might by itself be a viable cofinal target. The transport identity remains valid. No RH proof or new zero-free boundary is asserted.

The definitions and the safe-half-plane remainder estimate are those of `spectral/ANCHOR_FLOW.md` and `spectral/MOVING_ANCHOR_THEOREM.md` in PR #1026, frozen commit `11b4f6612275955a1fddb5c53f67dc21124783f8`.

## 1. An unconditional impossibility for the actual xi source

Write `G_N(a)=T_N(a)/(2a)`, `g_0(a)=f(1/2+a)`, and retain the real skew matrix K and the rank-two boundary matrix B from the preceding packet. For `a_0>a_1>=1`, set `tau_j=log a_j`, `U(v)=exp((v-tau_0)K)`, and

\[
 X_+(a_0,a_1)=\int_{\tau_1}^{\tau_0}U(v)B(e^v)_+U(v)^*\,dv.
\]

The previous sufficient condition was `||X_+||<lambda_min G_N(a_0)`.

**Theorem 1.** Let `N>=1`, `a_0>=100(N+1)`, and `1<=a_1<a_0`. For the actual xi source,

\[
 \|X_+(a_0,a_1)\|-\lambda_{\min}G_N(a_0)
 >\frac12\log\frac{N+1}{a_1}-\frac{29}{12}.
\tag{1}
\]

In particular, if `(N+1)/a_1>=128`, the proposed sufficient condition fails. For every cofinal family `N/a_1 -> infinity`, it therefore fails eventually, regardless of the choice of safe starting anchors `a_0>=100(N+1)`.

### Trace loss

Since `B_+>=B` and trace is invariant under U,

\[
 \|X_+\|\ge\frac{\operatorname{tr}X_+}{N+1}
 \ge g_0(a_0)-g_0(a_1).
\tag{2}
\]

This uses the exact identity `tr B=(N+1)g_1` and `d g_0/d log a=g_1`. Even when the right side were negative, the inequality remains valid.

### An alternating Fejer test vector

Put `a=a_0`, `sigma=a+1/2`, `q=(a-1/2)/(a+1/2)`, and

\[
 v_j=\frac{(-1)^j}{\sqrt{N+1}},\qquad 0\le j\le N.
\]

Separate the actual source as `f(s)=1/2 log(s/(2*pi))+R(s)`. The preceding proof gives `||R(s_a(S))||<3/19` and `|R(sigma)|<1/19` in this safe regime. The main-source off-diagonal coefficients in G are

\[
 g_n^0=\frac{1+(-1)^{n+1}q^n}{4n}.
\]

Consequently

\[
\begin{aligned}
 v^*G_N(a)v
 &\le g_0(a)+\frac12\sum_{n=1}^N
  \left(1-\frac n{N+1}\right)\frac{(-1)^n-q^n}{n}
  +\frac4{19}\\
 &\le g_0(a)-\frac12H_N+
 \frac{N}{2(N+1)}+\frac{(1-q)N}{4}+\frac4{19}\\
 &<g_0(a)-\frac12\log(N+1)+\frac34.
\end{aligned}
\tag{3}
\]

The alternating weighted sum is nonpositive because its positive magnitudes decrease. Bernoulli's inequality `q^n>=(1-n(1-q))` supplies the second line. Finally `H_N>=log(N+1)`, `(1-q)N/4<1/400`, and `1/2+1/400+4/19<3/4`. This proves the required uniform upper bound on the smallest starting eigenvalue. In particular the large diagonal `g_0(a)` is not itself the available minimum-eigenvalue margin.

### The endpoint diagonal

For real `s>1`, the digamma Binet formula and the negative Mangoldt sum give

\[
 f(s)<\frac12\log\frac{s}{2\pi}+\frac1{2s}+\frac1{s-1}.
\]

For `s=a_1+1/2`, `a_1>=1`, the rational terms are at most `7/3`, and `s/(2*pi*a_1)<1/4`. Since `log 2>2/3`,

\[
 g_0(a_1)<\frac12\log a_1+\frac53.
\tag{4}
\]

Combining (2)--(4) gives (1). The threshold 128 follows from
`(7/2)log 2>29/12`; a rational lower bound obtained from the first three positive terms of `log 2=2 atanh(1/3)` already proves that strict inequality.

This obstruction is unconditional and uses the whole actual source. It does not imply that the endpoint matrix is indefinite. It proves that this particular sufficient estimate overpays for transport.

## 2. A fixed relative metric does not repair positive-part overpayment in general

It is tempting to replace the scalar margin by

\[
 \|G_0^{-1/2}X_+G_0^{-1/2}\|<1.
\tag{5}
\]

This is a valid sufficient condition whenever `G_0>0`. It still discards signed cancellation, and can fail badly even for an elementary positive-real source.

**Proposition 2.** Take `f_*(s)=1+(s-1/2)`, `N=1`, `a_0=200`, and `a_1=200 exp(-1/4)`. Every covariance matrix of this source is positive semidefinite, and the two-dimensional matrices are strictly positive. Nevertheless both the original condition and (5) fail, with the relative left side greater than 2.

**Proof.** In this dimension,

\[
 G(a)=I+a\begin{pmatrix}1&1\\1&1\end{pmatrix},
 \quad K=\frac12\begin{pmatrix}0&-1\\1&0\end{pmatrix},
 \quad B(a)=a\begin{pmatrix}0&1\\1&2\end{pmatrix}.
\]

The minimum eigenvalue of G is exactly 1 for every a. Put
`v=(1,-1)/sqrt(2)`, so `G(a_0)v=v`. The positive eigenvalue of the displayed B/a is `1+sqrt(2)`; a corresponding unit eigenvector has angle `3*pi/8`. With `t=v_log-tau_0` in `[-1/4,0]`, U rotates by angle `t/2`. Hence

\[
 v^*X_+v
 =200(1+\sqrt2)\int_{-1/4}^0
 e^t\sin^2(\pi/8+t/2)\,dt.
\]

Throughout that interval, the sine argument is greater than `1/4`. The elementary chord bound on `[0,pi/2]` and `pi<22/7` give `sin(pi/8+t/2)>7/44`. Also `1+sqrt(2)>2` and `1-exp(-1/4)>1/5`. Thus

\[
 v^*X_+v>200\frac{49}{4840}=\frac{245}{121}>2.
\]

This is larger than the exact minimum eigenvalue 1. Because `G_0^{-1/2}v=v`, it also lower-bounds the left side of (5). Yet the endpoint G is strictly positive. The failure is therefore caused by taking the positive part before integration, not by negative source geometry.

An ordinary floating diagnostic with the logarithmically growing positive source `f_*(s)=1/2 log(1+(s-1/2)/(2*pi))` finds the same phenomenon, but no numerical example is needed for the proposition.

## 3. What the repair must retain

The exact signed identity

\[
 U(\tau_1)G(a_1)U(\tau_1)^*
 =G(a_0)-\int_{\tau_1}^{\tau_0}U(v)B(e^v)U(v)^*\,dv
\]

remains correct. A useful continuation theorem must preserve directional cancellation, compare to a source-matched reference, or use a different limiting geometry. Merely shrinking constants in the old absolute budget cannot work, and replacing its scalar denominator by a fixed initial matrix is not a source-independent cure.

The companion `LAGUERRE_WINDOW_BRIDGE.md` develops a constructive alternative: the proportional degree/anchor regime has an exact compact-support limit, including the complete prime operator and a transfer theorem for the actual spectral floor. It can consume a proven compact-window positivity bound without the impossible positive-part transport budget. Extending those window bounds to unbounded support is still the RH-bearing gap.
