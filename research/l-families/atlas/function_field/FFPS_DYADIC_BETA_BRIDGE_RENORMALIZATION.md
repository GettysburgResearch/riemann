# The dyadic beta bridge is a constant-condition Möbius bridge and needs no separate endpoint gate

Status: **exact dyadic-to-ratio-two bridge geometry, exact duplicate-\(67\)
bridge renormalization, exact rough-source bridge transport, and a
rough-support sparse-query no-go; no Möbius bridge estimate, RH, or GRH
result**

Bounded exact replay:
[ffps_dyadic_beta_bridge_renormalization.py](ffps_dyadic_beta_bridge_renormalization.py).
Canonical summary:
[ffps_dyadic_beta_bridge_renormalization.json](ffps_dyadic_beta_bridge_renormalization.json).

Frozen inputs:

* endpoint-sampling frontier, commit
  `fad8ce2c4ce8633c5bb67356e6765800eac3d440`;
* sharp prefix-truncated rough frontier, commit
  `d1af013130ae4004c629b916950e34545b0a65f1`.

The replay pins both complete quartets at those commits.  The only external
asymptotic input used below is the prime number theorem in the form

\[
 \pi(X)-\pi(y)=(1+o(1)){X\over\log X}
 \qquad(y=X^{o(1)}).
\tag{0.1}
\]

It is used only for the support-aware sampling no-go, not for any exact
scale identity.

## 0. Outcome

For a prefix sequence \(F_x=F_{\lfloor x\rfloor}\), with \(F_x=0\) for
\(x<1\), define its augmented dyadic bridge

\[
 \mathcal B_F(X)=\max\left\{
 |F_1|,
 \max_{\substack{j\ge0\\2^j<X}}
 \max_{2^j<Y\le\min(2^{j+1},X)}
 |F_Y-F_{2^j}|
 \right\}.
\tag{0.2}
\]

The atom \(|F_1|\) removes an irrelevant first-block exception and makes
every statement exact for finite \(X\ge2\).

The first observation is that the separate dyadic endpoint gate in the
predecessor is redundant.  If

\[
 \mathcal M_F(X)=\max_{1\le Y\le X}|F_Y|,
\tag{0.3}
\]

then

\[
\boxed{
 \mathcal B_F(X)\le2\mathcal M_F(X),
 \qquad
 \mathcal M_F(X)\le
 (2+\lfloor\log_2X\rfloor)\mathcal B_F(X).}
\tag{0.4}
\]

Thus one signed dyadic bridge reconstructs every completed dyadic endpoint
and the current partial block at only logarithmic cost.  No arithmetic
input enters (0.4).

Now put \(q=67\), \(s=1/2+it\),

\[
 \omega=q^{-s},\qquad a=|\omega|=q^{-1/2},
\tag{0.5}
\]

and define

\[
 M_x(t)=\sum_{n\le x}{\mu(n)\over n^s},
 \qquad
 D_x(t)=\sum_{n\le x}{\beta(n)\over n^s},
 \qquad
 \beta(n)=\mu(n)-\mathbf1_{q\mid n}\mu(n/q).
\tag{0.6}
\]

Their bridges satisfy the uniform two-sided comparison

\[
\boxed{
 {1-a\over1+2a}\,\mathcal B_M(X,t)
 \le \mathcal B_D(X,t)
 \le(1+3a)\mathcal B_M(X,t).}
\tag{0.7}
\]

This is the requested exact renormalization: the literal beta bridge is a
bounded coordinate change of the standard weighted Möbius bridge.  The
constants are independent of \(X\), \(t\), the kernel, and the endpoint.
The duplicate-\(67\) orientation creates no bridge contraction.

For one fixed coefficient sequence \(c_n\), write
\(F_x(t)=\sum_{n\le x}c_nn^{-it}\), and let
\(\mathcal B_F(X,t)\) denote its augmented bridge. For each fixed integer
\(h\ne0\), at the guarded harmonic \(t_{h,X}\), local Abel transport gives

\[
 (1+|t_{h,X}|\log2)^{-1}\mathcal B_F(X,0)
 \le\mathcal B_F(X,t_{h,X})
 \le(1+|t_{h,X}|\log2)\mathcal B_F(X,0).
\tag{0.8}
\]

Combining (0.4), (0.7), (0.8), and the frozen maximal-prefix theorem gives

\[
\boxed{
 \mathrm{RH}
 \Longleftrightarrow
 \mathcal B_D(X,t_{h,X})^2=X^{o(1)}
 \Longleftrightarrow
 \mathcal B_M(X,0)^2=X^{o(1)}.}
\tag{0.9}
\]

Equation (0.9) proves no estimate.  It says exactly what survived the
endpoint-compression attempt: not an endpoint-plus-bridge pair, but one
ordinary signed Möbius block gate.

Rough preconditioning also transports through the bridge. Freeze \(y=y_X\)
at the outer horizon, put \(P_y=\prod_{p\le y}p\), and define

\[
 A_{y,x}(t)=
 \sum_{\substack{n\le x\\(n,P_y)=1}}{\mu(n)\over n^s}.
\tag{0.10}
\]

With the frozen masses

\[
\begin{aligned}
 C_{\rm sf}(X,y)&=
 \sum_{\substack{d\le X\\d\mid P_y}}d^{-1/2},\\
C_{\rm sm}(X,y)&=
 \sum_{\substack{d\le X\\P^+(d)\le y}}d^{-1/2},
\end{aligned}
\tag{0.11}
\]

Here and below \(P^+(1)=1\).

With these conventions, one has

\[
\boxed{
 \mathcal B_M
 \le(3C_{\rm sf}-2)\mathcal B_A,
 \qquad
 \mathcal B_A
 \le(3C_{\rm sm}-2)\mathcal B_M.}
\tag{0.12}
\]

Consequently, throughout the sharp positive-mass range
\(y_X\le(\log X)^{2+o(1)}\), the rough Möbius bridge is another
subpower-conditioned RH normal form.  This removes small-prime Euler
states exactly, but does not estimate the remaining bridge.

Finally, rough support alone does not permit a smaller endpoint exponent.
Even after every prime at most \(y=X^{o(1)}\) is removed, all primes in
\((y,X]\) remain admissible rough positions. A deterministic source-blind
sampler with
\(m\) value queries can hide, inside one dyadic block, an admissible
zero-total excursion of height at least

\[
\boxed{
 \mathcal B_F(X)\ge
 {N_y^\square(X)\over
  2\bigl(m+2+\lfloor\log_2X\rfloor\bigr)\sqrt X}
 -{1\over2\sqrt X},}
\tag{0.13}
\]

where

\[
 N_y^\square(X)
 =\#\{n\le X:\mu(n)^2=1,\ (n,P_y)=1\}.
\tag{0.13a}
\]

Every prime in \((y,X]\) belongs to this support, so

\[
 N_y^\square(X)\ge\pi(X)-\pi(y)=X^{1-o(1)},
\tag{0.14}
\]

any source-blind interpolation error that is subpower still requires
\(m\ge X^{1/2-o(1)}\). Rough sparsity can save logarithms, not the
square-root sampling exponent.  This is not a counterexample for the
literal Möbius signs. The zero-answer adversary covers deterministic
adaptive value queries; randomized guarantees are not analyzed.

## 1. Dyadic bridges cover every ratio-two increment

Define the real-endpoint ratio-two gate

\[
 \mathcal C_F(X)=\max\left\{
 |F_1|,
 \sup_{\substack{1\le u<v\le X\\v\le2u}}
 |F_v-F_u|
 \right\}.
\tag{1.1}
\]

Then

\[
\boxed{
 \mathcal B_F(X)\le\mathcal C_F(X)\le3\mathcal B_F(X).}
\tag{1.2}
\]

The first inequality is immediate. For the second, choose \(j\) with
\(2^j\le u<2^{j+1}\). If \(v\le2^{j+1}\), subtract two partial bridges
from the same dyadic left endpoint, at cost at most \(2\mathcal B_F\).
If \(v>2^{j+1}\), split at \(2^{j+1}\). The tail of the first block costs
at most \(2\mathcal B_F\), and the partial second block costs at most
\(\mathcal B_F\). Since \(v\le2u<2^{j+2}\), no third block occurs.

The factor three is sharp for arbitrary coefficient sequences.  Take a
prefix path with

\[
 F_4=0,\qquad F_5=1,\qquad F_8=-1,\qquad F_{10}=-2,
\tag{1.3}
\]

and keep every other relevant within-block excursion inside the unit
disk. Then \(\mathcal B_F=1\), while

\[
 |F_{10}-F_5|=3,
 \qquad10=2\cdot5.
\tag{1.4}
\]

When real scaled endpoints are replaced by floors, one may enlarge (1.1)
to integer pairs \(r<s\le2r+1\). The same two-block proof and the same
factor three remain valid. The sole zero-endpoint case \(r=0,s=1\) is
covered by the atom \(|F_1|\). This is the form replayed exactly.

## 2. Exact duplicate-(67) bridge inversion

The literal scale identity is

\[
 D_x=M_x-\omega M_{x/q}.
\tag{2.1}
\]

For a dyadic pair \(2^j<Y\le2^{j+1}\), subtract (2.1) at \(Y\) and
\(2^j\):

\[
 D_Y-D_{2^j}
 =(M_Y-M_{2^j})
 -\omega(M_{Y/q}-M_{2^j/q}).
\tag{2.2}
\]

The first increment costs \(\mathcal B_M\); the scaled increment has ratio
at most two and costs \(3\mathcal B_M\) by (1.2). This proves

\[
 \mathcal B_D\le(1+3a)\mathcal B_M.
\tag{2.3}
\]

The terminating inverse is

\[
 M_x=\sum_{k\ge0}\omega^kD_{x/q^k}.
\tag{2.4}
\]

In a dyadic increment, the \(k=0\) term costs \(\mathcal B_D\); every
\(k\ge1\) term costs \(3\mathcal B_D\). Hence

\[
\begin{aligned}
 \mathcal B_M
 &\le\left(1+3\sum_{k\ge1}a^k\right)\mathcal B_D\\
 &={1+2a\over1-a}\mathcal B_D.
\end{aligned}
\tag{2.5}
\]

Equations (2.3)--(2.5) prove (0.7).  They preserve all signs inside every
block.  Absolute values enter only after the exact scale identities have
been assembled.

## 3. Why no separate endpoint gate remains

The lower comparison in (0.4) follows from

\[
 |F_Y-F_{2^j}|\le|F_Y|+|F_{2^j}|.
\tag{3.1}
\]

For the reverse comparison, if \(2^J\le Y\le2^{J+1}\), telescope

\[
 F_Y=F_1+
 \sum_{j=0}^{J-1}(F_{2^{j+1}}-F_{2^j})
 +(F_Y-F_{2^J}).
\tag{3.2}
\]

There are at most \(2+\lfloor\log_2X\rfloor\) terms, each bounded by the
augmented bridge.  This proves (0.4).

The logarithm is harmless for every \(X^{o(1)}\) target. Thus the
predecessor's endpoint-plus-bridge decomposition can be sharpened to a
bridge-only decomposition.  This is an assembly theorem, not a new
cancellation estimate.

## 4. Rough scale transport

With the cutoff \(y_X\) frozen across all prefixes, the exact finite
identities are

\[
\begin{aligned}
 M_x(t)
 &=\sum_{\substack{d\mid P_y\\d\le x}}
 {\mu(d)\over d^s}A_{y,x/d}(t),\\
 A_{y,x}(t)
 &=\sum_{\substack{d\le x\\P^+(d)\le y}}
 {1\over d^s}M_{x/d}(t).
\end{aligned}
\tag{4.1}
\]

For a dyadic increment, the \(d=1\) summand is a literal dyadic bridge and
costs one copy of the target bridge. Every \(d>1\) summand is a scaled
ratio-two increment and costs three copies.  Taking coefficient masses
gives

\[
 1+3(C_{\rm sf}-1)=3C_{\rm sf}-2,
 \qquad
 1+3(C_{\rm sm}-1)=3C_{\rm sm}-2,
\tag{4.2}
\]

which proves (0.12).  Composing with (0.7) gives the fully source-faithful
comparison

\[
\boxed{
 {1-a\over(1+2a)(3C_{\rm sm}-2)}\mathcal B_A
 \le\mathcal B_D
 \le(1+3a)(3C_{\rm sf}-2)\mathcal B_A.}
\tag{4.3}
\]

The frozen sharp frontier proves

\[
 C_{\rm sf}(X,y_X),C_{\rm sm}(X,y_X)=X^{o(1)}
 \Longleftrightarrow
 \limsup_{X\to\infty}{\log y_X\over\log\log X}\le2.
\tag{4.4}
\]

Therefore rough preconditioning is a subpower bridge isomorphism
throughout exactly that positive-mass range.  Beyond it, (4.3) is still
true, but its absolute constants may lose a power; signed scale
cancellation is not refuted.

## 5. Rough support does not compress endpoint sampling exponent

Let a deterministic value-query sampler choose at most \(m\) prefix
endpoints. For an adaptive sampler, answer zero to each query before
placing the final excursion. Adjoin
\(0,X\) and every dyadic boundary. These points form at most

\[
 m+2+\lfloor\log_2X\rfloor
\tag{5.1}
\]

cells, each contained in one dyadic block. The squarefree rough-support
positions are partitioned among them, so one cell contains at least

\[
 K\ge{N_y^\square(X)\over m+2+\lfloor\log_2X\rfloor}
\tag{5.2}
\]

such positions.

Put \(r=\lfloor K/2\rfloor\). On the first \(r\) selected rough positions
in that cell set

\[
 a_n=X^{-1/2}\overline{z_n},
\tag{5.3}
\]

and on the next \(r\) set

\[
 a_n=-X^{-1/2}\overline{z_n},
\tag{5.4}
\]

where \(|z_n|=1\) is any prescribed phase sequence. Set every other
coefficient to zero.  Then

\[
 |a_n|=X^{-1/2}\le n^{-1/2},
\tag{5.5}
\]

all queried prefixes and every dyadic boundary are zero, while the bridge
at the midpoint is \(r/\sqrt X\). Equations (5.2) and
\(r\ge(K-1)/2\) prove (0.13).

The adversary is supported only on squarefree \(y\)-rough positions, so it
preserves every source zero forced by nonsquarefreeness or a small prime.
By (0.14), for the entire subfrontier range
\(y_X\le(\log X)^{2+o(1)}\) and every fixed
\(0<\delta<1/2\), a sampler with \(m=X^{1/2-\delta}\) can still hide a
bridge of size \(X^{\delta-o(1)}\).

This is a source-blind information theorem.  It does not replace the
literal coefficients by an adversary inside (0.9), and it does not rule
out a Möbius-specific Volterra identity or cancellation theorem. Randomized
query guarantees lie outside the result.

## 6. Claim ledger

| statement | grade |
|---|---|
| dyadic-to-ratio bridge cover (1.2) | **PROVED EXACT; FACTOR THREE SHARP SOURCE-BLINDLY** |
| bridge/maximal comparison (0.4) | **PROVED EXACT FOR EVERY PREFIX SEQUENCE** |
| duplicate-(67) bridge renormalization (0.7) | **PROVED EXACT** |
| endpoint gate redundancy | **PROVED AT LOGARITHMIC COST** |
| bridge-only beta and Möbius RH criteria (0.9) | **PROVED FROM FROZEN MAXIMAL RH EQUIVALENCE** |
| rough bridge comparison (0.12), (4.3) | **PROVED EXACT** |
| subfrontier rough bridge RH criterion | **PROVED FROM THE FROZEN MASS FRONTIER** |
| PNT rough-support size | **IMPORTED CLASSICAL PNT** |
| rough-support sparse-query no-go | **PROVED SOURCE-BLINDLY** |
| Möbius, beta, or rough bridge estimate | **OPEN / NOT CLAIMED** |
| RH or GRH | **NOT PROVED** |

## 7. Bounded replay

The replay checks the sharp factor-three ratio example, a terminating
rational scale inverse over 243 prefixes, both dyadic bridge constants,
maximal reconstruction, and a 256-term hidden excursion supported only on
integers coprime to \(30\). It uses no floating-point operation, zeta-zero
enumeration, prime search, or matrix calculation.

~~~text
python -B research/l-families/atlas/function_field/ffps_dyadic_beta_bridge_renormalization.py --check
python -B -O research/l-families/atlas/function_field/ffps_dyadic_beta_bridge_renormalization.py --check
python -B -m unittest tests.test_ffps_dyadic_beta_bridge_renormalization
python -B -O -m unittest tests.test_ffps_dyadic_beta_bridge_renormalization
python -B -m ruff check research/l-families/atlas/function_field/ffps_dyadic_beta_bridge_renormalization.py tests/test_ffps_dyadic_beta_bridge_renormalization.py
python -B -m ruff format --check research/l-families/atlas/function_field/ffps_dyadic_beta_bridge_renormalization.py tests/test_ffps_dyadic_beta_bridge_renormalization.py
~~~
