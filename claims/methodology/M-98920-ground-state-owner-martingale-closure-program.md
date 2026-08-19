# M-98920 — Ground-state / owner-martingale closure program

## Single proposed mechanism

The positive renewal kernel of `L-98920` is too large for any source-blind
subpower Doob transform: for odd primes `g_diamond(p^k)=1`, so the tilted mass
contains

\[
\sum_{p,k}p^{-k(1/2+\varepsilon)},
\]

which converges only for `epsilon>1/2`. Thus no one-channel positive norm can
contract at RH scale.

The exact escape is to retain the logarithmic owner martingale of `L-97102`
before collapsing to a prefix. For each source integer `n`, the weights

\[
P_n(d)=\frac{\Lambda_\diamond(d)g_\diamond(n/d)}
{g_\diamond(n)\log n}
\]

form a probability distribution, and `(-1)^t f(N_t)` is a bounded martingale.
The coefficient energy is only logarithmic:

\[
\sum_{n\le X}\frac{b_\diamond(n)^2}{g_\diamond(n)n}\ll\log X.
\]

`L-98921` is the exact prefix Volterra projection of this martingale.

## Desired final theorem: OMCE98920

Prove a multiplicative Carleson/Doob embedding only after the native
square-root normalization and factor-four boundary extraction. In schematic
form, for the exact normalized annular observable `A_X/sqrt(X)`, prove

\[
\int_1^T \bigl[(A_X/\sqrt X)_-\bigr]\,\frac{dX}{X}
\le (\log T)^C
 + o(1)\,\mathcal E(T),
\]

where `mathcal E(T)` is the owner-martingale quadratic variation already
controlled by `L-97102`.

A valid proof must eliminate cross terms by conditional martingale
orthogonality before the source index is summed. Plain Cauchy--Schwarz on the
prefix or annulus is forbidden: it loses a power of `X` through the positive
trace mass.

If OMCE98920 holds with any polylogarithmic right side, then the native scalar
has subpower logarithmic negative mass. The negative-mass Mellin theorem of PR
#615 then implies RH.

## Exact firewalls established in this pass

1. source-blind positive renewal Doob contraction at subpower tilt: impossible;
2. direct prefix Cauchy--Schwarz with `g/n`: loses a factor of `X`;
3. annularizing before ordinary Cauchy--Schwarz still loses local counting mass;
4. logarithmic owner probabilities exist exactly and retain only logarithmic
   coefficient energy.

Thus the only surviving version of this idea is a source-level martingale
Carleson embedding through the already-normalized native boundary.

RH remains unproved; OMCE98920 is the single open closure theorem proposed here.
