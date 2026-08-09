# T-90001 — The theta bridge: WSTS <=> RH as a short resident proof spine

Claim ID: `T-90001` (provisional range 90001+; allocate at registry before integration)  
Status: **PROPOSED COMPLETE EQUIVALENCE SPINE — independent review required; WSTS and RH remain unproved**  
Original authoring: `claude-fable-5` session `riemann-proof-review-8nz34i`  
Audit/extension: `gpt56-sol`, 2026-08-09  
Resident companions: `L-90006` (WSTS => RH), `L-90007` (RH => WSTS), `L-90005` (even-endpoint deterministic z-collapse)  
Scope: full equivalence `WSTS <=> RH` in standard analytic number theory. The theorem is a reduction/criterion, not a proof of RH.

## 0. Objects

For integer `X>=4`, put
\[
b_X(m)=2\sqrt m\left(\log(X/m)-2(1-\sqrt{m/X})\right)
\]
on `[2,X]` and zero outside. By construction
\[
b_X(X)=b_X'(X)=0.
\]
For every integer `q>=2`, define
\[
v_q=\sum_{k\le X/q}[b_X(kq)-b_X(kq+1)],
\]
\[
r_X(q)=v_q-q^{-1/2}\log(X/q).
\]
Let
\[
Y=\lfloor X/2\rfloor,
\qquad
s_X(p)=r_X(p)-\mathbf1_{p\le Y}r_Y(p),
\]
\[
T_X^s(z)=\sum_{z\le p\le X}(\log p)s_X(p),
\qquad
B_X=\max_{2\le z\le X}[T_X^s(z)]_+.
\]
The Weighted Shell-Tail Stability statement is
\[
\boxed{
\forall\varepsilon>0,
\qquad B_X=O_\varepsilon(X^\varepsilon).
}
\tag{WSTS}
\]

For the continuum bridge put
\[
g(u)=\frac{\log u+4}{\sqrt u}-4,
\qquad
F(\theta)=\sum_{k\le1/\theta}g(k\theta),
\]
\[
E(\theta)=F(\theta)-\theta^{-1/2}\log(1/\theta).
\]
On
\[
\frac1{N+1}<\theta\le\frac1N,
\]
let
\[
S_N=\sum_{k\le N}k^{-1/2},
\qquad
A_N=\sum_{k\le N}k^{-1/2}\log k.
\]
Then exactly
\[
\boxed{
E(\theta)=\theta^{-1/2}
[A_N+(S_N+1)\log\theta+4S_N]-4N.
}
\tag{T-90001.1}
\]
Finally put
\[
H(\theta)=\int_\theta^1E(u)\,du,
\]
\[
E_c(\theta)=E(\theta)-c^{-1/2}E(\theta/c)\mathbf1_{\theta\le c},
\qquad
H_c(\theta)=\int_\theta^1E_c(u)\,du.
\]

## 1. Unconditional bridge with explicit floor error

Let
\[
c=Y/X\in[1/3,1/2].
\]
For every `2<=z<=X`,
\[
\boxed{
T_X^s(z)
=\sqrt X\,H_c(z/X)
+\mathcal E_{X,Y}(z)
+\mathrm{fl}_{X,Y}(z),
}
\tag{T-90001.2}
\]
where, with
\[
R(t)=\vartheta(t)-t,
\]
\[
\boxed{
\mathcal E_{X,Y}(z)
=X^{-1/2}\int_{[z,X]}E_c(t/X)\,dR(t),
}
\tag{T-90001.3}
\]
and
\[
\boxed{
|\mathrm{fl}_{X,Y}(z)|
\le
\zeta(3/2)(-\zeta'(3/2))(2+\log X).
}
\tag{T-90001.4}
\]

The per-modulus estimate behind (T-90001.2) is
\[
\boxed{
\left|r_X(q)-X^{-1/2}E(q/X)\right|
\le
\frac{\zeta(3/2)}2q^{-3/2}
\left(2+\log\frac Xq\right).
}
\tag{T-90001.5}
\]

Two post-verification repairs are load bearing in this derivation.

First, the top cell `kq<=X<kq+1` is handled by extending the analytic formula for
`b_X` through `[X,X+1]`; the discrepancy from the declared zero extension is
quadratic because `b_X(X)=b_X'(X)=0`, and is absorbed by the displayed floor
slack.

Second,
\[
|g'(u)|={u^{-3/2}\over2}|\log u+2|
\]
is **not** monotone on `(0,1]`.  The correct cell-sup argument uses the decreasing
majorant
\[
M(u)={u^{-3/2}\over2}(2-\log u),
\qquad 0<u\le1.
\]
This is the repaired E2/E3-type issue from the source session; no false
monotonicity is used here.

## 2. Moat Lemma

For every `0<theta<=1`,
\[
\boxed{H(\theta)\le0.}
\tag{T-90001.6}
\]
More generally, for every `c in (0,1)`,
\[
\boxed{H_c(\theta)\le0.}
\tag{T-90001.7}
\]

### Proof

Let
\[
J(\theta)=H(\theta)/\sqrt\theta.
\]
On one reciprocal cell, direct differentiation of the exact antiderivative gives
\[
\boxed{
J'(\theta)
=2\theta^{-3/2}
[N\theta+1-(S_N+1)\sqrt\theta].
}
\tag{T-90001.8}
\]
The elementary induction
\[
S_N\le2\sqrt N-1
\tag{T-90001.9}
\]
follows because
\[
2\sqrt N-2\sqrt{N-1}
={2\over\sqrt N+\sqrt{N-1}}
\ge N^{-1/2}.
\]
Therefore
\[
J'(\theta)
\ge
2\theta^{-3/2}(\sqrt{N\theta}-1)^2
\ge0.
\tag{T-90001.10}
\]

No integration constant is hidden.  On the `N`th cell,
\[
\boxed{
H(\theta)
=-2\sqrt\theta
[A_N+(S_N+1)\log\theta+2S_N-2]
+4N\theta-4.
}
\tag{T-90001.11}
\]
One checks `H'=-E`, `H(1)=0`, and exact continuity at every knot using
\[
A_N=A_{N-1}+N^{-1/2}\log N,
\qquad
S_N=S_{N-1}+N^{-1/2}.
\]
Thus `J` is continuous and nondecreasing, with `J(1)=0`; hence `J<=0` to the
left of one and (T-90001.6) follows.

For `theta<=c`,
\[
H_c(\theta)
=\sqrt\theta[J(\theta)-J(\theta/c)]\le0,
\]
while for `theta>c`, `H_c=H`.  This proves (T-90001.7).  In particular the
finite ratio `floor(X/2)/X` is covered exactly; no idealized `c=1/2` replacement
is needed for the Moat.

## 3. RH implies WSTS

`L-90007` supplies a resident proof with no numerical profile constant.  From
(T-90001.1), elementary sum-integral comparison gives
\[
|E(\theta)|
\ll\theta^{-1/2}[1+\log(1/\theta)],
\tag{T-90001.12}
\]
\[
|E'(\theta)|
\ll\theta^{-3/2}[1+\log(1/\theta)]
\tag{T-90001.13}
\]
on reciprocal-cell interiors, with continuity at the knots.  The same bounds
hold uniformly for `E_c`, `1/3<=c<=1/2`.

Under RH, the classical von Koch estimate gives
\[
R(t)=O(\sqrt t\log^2(2t)).
\]
Stieltjes integration by parts in (T-90001.3) therefore yields uniformly in `z`
\[
\boxed{
\mathcal E_{X,Y}(z)\ll\log^4(2X).
}
\tag{T-90001.14}
\]
The Moat makes the continuum term in (T-90001.2) nonpositive, and the floor
error is only logarithmic. Hence
\[
\boxed{
\mathrm{RH}\Longrightarrow B_X\ll\log^4(2X)
\Longrightarrow\mathrm{WSTS}.
}
\tag{T-90001.15}
\]

The source session reports an additional dyadic-difference cancellation giving
`O(log^3 X)`.  That sharper exponent is **not load bearing** and is not promoted
here without its complete resident bookkeeping.  The conservative `log^4`
bound already proves the implication.

## 4. WSTS implies RH

`L-90006` supplies a resident consumer that avoids both the historical
square-screw stack and the session-only `hat E` derivation.

Put
\[
A_X=\sum_{p\le X}(\log p)r_X(p).
\]
At `z=2`, the shell identity is exactly
\[
\boxed{T_X^s(2)=A_X-A_{\lfloor X/2\rfloor}.}
\tag{T-90001.16}
\]
Thus WSTS and dyadic iteration give, one-sidedly,
\[
\boxed{A_X\ll_\varepsilon X^\varepsilon.}
\tag{T-90001.17}
\]

Let
\[
P(X)=\sum_{p\le X}{\log p\over\sqrt p}\log{X\over p}.
\tag{T-90001.18}
\]
The complete prime-power seed objective satisfies the exact divisor-switched
identity
\[
\sum_{q\le X}\Lambda(q)v_q(b_X)
=\sum_{n=2}^{X}b_X(n)\log{n\over n-1}.
\tag{T-90001.19}
\]
Comparison with its elementary integral gives
\[
\sum_{q\le X}\Lambda(q)v_q(b_X)
=4\sqrt X+O(\log(2X)).
\]
Using (T-90001.5) and (T-90001.12), the contribution of prime powers `p^k`,
`k>=2`, is `O(log^3(2X))`.  Hence
\[
\boxed{
\sum_{p\le X}(\log p)v_p(b_X)
=4\sqrt X+O(\log^3(2X)).
}
\tag{T-90001.20}
\]
Since `A_X` is this seed objective minus `P(X)`, WSTS implies the sharp one-sided
ramp
\[
\boxed{
4\sqrt X-P(X)\ll_\varepsilon X^\varepsilon.
}
\tag{T-90001.21}
\]
for integer `X`.  On `N<=X<N+1`,
\[
P(X)-P(N)
=\log(X/N)\sum_{p\le N}{\log p\over\sqrt p}
\ll{\log(2N)\over\sqrt N},
\]
so the same bound holds for real `X`.

Now put
\[
F(X)=4\sqrt X-P(X).
\]
For `Re z>1/2`, direct Fubini gives
\[
\int_1^\infty P(X)X^{-z-1}dX
={1\over z^2}\sum_p{\log p\over p^{z+1/2}}.
\]
Writing
\[
Q(s)=\sum_p\sum_{k\ge2}{\log p\over p^{ks}},
\]
which is holomorphic for `Re s>1/2`, the Euler product yields
\[
\boxed{
\widehat F(z)
={4\over z-1/2}
+{1\over z^2}{\zeta'\over\zeta}\left(z+{1\over2}\right)
+{1\over z^2}Q\left(z+{1\over2}\right).
}
\tag{T-90001.22}
\]
The zeta pole at `s=1` cancels the explicit pole at `z=1/2`.  If `rho` is a
nontrivial zero with `Re rho>1/2`, then (T-90001.22) has the uncancelled pole
\[
z_\rho=\rho-1/2,
\qquad
\operatorname*{Res}_{z=z_\rho}\widehat F(z)
={m_\rho\over(\rho-1/2)^2}\ne0.
\tag{T-90001.23}
\]
There is no singularity on the positive real axis: `zeta(s)<0` on `(0,1)` by
the alternating eta identity, `zeta(s)>0` for `s>1`, and the sole pole at one
was just cancelled.

Given a hypothetical zero with
\[
\delta=\Re\rho-1/2>0,
\]
choose `0<epsilon<delta`.  By (T-90001.21), for a sufficiently large constant
`C`,
\[
G_\varepsilon(X)=CX^\varepsilon-F(X)\ge0
\qquad(X\ge1).
\]
Its Mellin transform is
\[
{C\over z-\varepsilon}-\widehat F(z).
\]
Landau's one-sign theorem forces the real abscissa of convergence to be the
only positive-real singularity, namely `z=epsilon`.  But then the defining
nonnegative transform is holomorphic throughout `Re z>epsilon`, contradicting
the genuine pole (T-90001.23), whose real part is `delta>epsilon`.
Therefore no zero lies to the right of the critical line.  Functional-equation
symmetry gives
\[
\boxed{\mathrm{WSTS}\Longrightarrow\mathrm{RH}.}
\tag{T-90001.24}
\]

No `1/zeta` factor appears in this consumer; no zeta zero can be hidden by a
finite shell blind spot.

## 5. Deterministic z-collapse: a new structural simplification

`L-90005` proves more of the formerly numerical Lemma S.  For exact dyadic/even
endpoints there is one continuum sign crossing
\[
\boxed{
c_*=0.1408520350138399254409579889\ldots
}
\tag{T-90001.25}
\]
and the exact finite shell obeys
\[
q\le c_*X-1\Longrightarrow s_X(q)>0,
\]
\[
q\ge c_*X+158\Longrightarrow s_X(q)<0.
\tag{T-90001.26}
\]
Consequently, for even `X`,
\[
\boxed{
B_X=[T_X^s(2)]_+ +O(X^{-3/2}\log(2X)).
}
\tag{T-90001.27}
\]
The previous `0.1408512...` value was only a coarse numerical approximation.
This result removes the `z`-maximum geometry on even endpoints, but it does not
bound the surviving RH-bearing scalar `T_X^s(2)`.

## 6. Audit disposition of the source-session flags

The source branch arrived with four named presentation/review flags.  Their
current disposition on this branch is:

- **Former Flag 0 (full converse consumers absent): CLOSED for the proof spine.**
  `L-90006` is a complete resident prime-ramp/Landau consumer.
- **Former Flag 1 (specific numerical profile constants): REMOVED FROM THE
  LOAD-BEARING CLAIM.** `L-90007` proves the needed absolute-constant profile
  bounds directly; no claimed constant `1`, `0.244`, or `0.410` is required.
- **Former Flag 2 (real-X interpolation of `A_X`): NOT NEEDED.** The resident
  consumer interpolates the prime ramp directly by (T-90001.21), with an
  `O(log X/sqrt X)` error.
- **Former Flag 3 (finite-height literature constants): NON-LOAD-BEARING AND
  EXCLUDED FROM THIS THEOREM.** Any finite verified window belongs in a separate
  calibration note after source checking.

The post-verification notation repair distinguishing the prime ramp from
`R(t)=vartheta(t)-t`, the top-cell tangency repair, the nonmonotone-`g'` repair,
and the global Moat antiderivative are all retained.

## 7. Exact theorem boundary

Proposed complete, subject to independent review:

```text
unconditional finite theta bridge              T-90001 §1
Moat H_c <= 0 for every c in (0,1)             T-90001 §2
RH => WSTS with O(log^4 X)                     L-90007 / §3
WSTS => one-sided prime ramp                    L-90006 / §4
prime-ramp Mellin/Landau consumer => RH         L-90006 / §4
WSTS <=> RH                                     T-90001
exact dyadic continuum one-crossing             L-90005
finite even-endpoint bounded transition         L-90005
```

Still open:

```text
WSTS unconditionally                            OPEN / RH-EQUIVALENT
surviving endpoint prime-ramp scalar            OPEN / RH-BEARING
odd-endpoint version of the sharp z-collapse    OPEN / deterministic
Riemann Hypothesis                              UNPROVEN
```

The practical review surface is now `T-90001 + L-90006 + L-90007`; `L-90005` is
a structural simplification, not an additional RH assumption.