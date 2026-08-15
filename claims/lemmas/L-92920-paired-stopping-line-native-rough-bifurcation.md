# L-92920 — Paired stopping-line orientation separates the native packet from its `P_61` rough lift

Claim ID: `L-92920`  
Status: **PROVED EXACT SOURCE/OBSERVATION NORMALIZATION COMPILER — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-15  
Primary inputs: `L-91362`, `L-91377`, `L-91379`, `L-91688`  
RH status: **unproved**

## 1. Paired source and signed observation

Let `V` be any additive typed observation space and work in the positive paired
cone

\[
 \mathbf V=V_+\oplus V_-.
\]

Define the signed observation and channel swap by

\[
 \Sigma(v_+,v_-)=v_+-v_-,
 \qquad
 S(v_+,v_-)=(v_-,v_+).
\]

Then

\[
 \boxed{\Sigma S=-\Sigma.}
\tag{L-92920.1}
\]

The relation holds simultaneously in the component row, literal score,
ordinary responses at `q` and `4q`, radix-four detail formed afterward, and
all additive boundary coordinates.

## 2. Full paired squarefree source is native

Attach a squarefree arithmetic source occurrence `n` to the `+` channel when
`mu(n)=1` and to the `-` channel when `mu(n)=-1`.  Applying `Sigma` to the full
paired source gives

\[
 \boxed{
 \Sigma\mathbf P_X
 =\sum_{n\le X/j}\frac{\mu(n)}{\sqrt n}Q_{X/n}(j)
 =c_X(j).
 }
\tag{L-92920.2}
\]

By `L-91377`, its ordinary, detail and literal-score observations are exactly

\[
 w_X,\qquad \Omega_X,\qquad J_\Lambda(X).
\tag{L-92920.3}
\]

Thus the paired source is a positive carrier of the signed native packet.

## 3. Finite forcing alone is the rough lift

The `P_61` finite forcing in `L-91362` carries channel factor
`S^(omega(d))` at the small-prime divisor `d`.  Therefore

\[
 \Sigma S^{\omega(d)}=(-1)^{\omega(d)}\Sigma=\mu(d)\Sigma.
\]

Its signed component-row observation is

\[
 \boxed{
 \Sigma\mathbf F_{61,X}
 =\sum_{d\mid P_{61}}\frac{\mu(d)}{\sqrt d}Q_{X/d}
 =D_{P_{61},X}.
 }
\tag{L-92920.4}
\]

By `L-91379`, this is exactly the native rough lift

\[
 \boxed{
 D_{P_{61},X}
 =\mathfrak D_X
 =N_X+\mathcal R_X,
 \qquad
 \mathcal R_X=
 \sum_{\substack{m\in\mathcal R_{67}\\m>1}}
 m^{-1/2}N_{X/m}.
 }
\tag{L-92920.5}
\]

The capacity observations of `mathcal R_X` are nonnegative, even though its
component row is signed.

## 4. Actual rough children remove the reservoir

The exact stopping-line identity is

\[
 \mathbf P_X
 =\mathbf F_{61,X}
 +\sum_{d\mid P_{61}}
  \sum_{p\ge67}(dp)^{-1/2}
  S^{\omega(d)+1}
  \mathbf P_{p+}(X/(dp)).
\tag{L-92920.6}
\]

The extra swap at the least rough prime is load bearing.  Applying `Sigma` and
using (L-92920.2)--(L-92920.5) gives

\[
\boxed{
 \Sigma\left[
  \sum_{d,p}(dp)^{-1/2}S^{\omega(d)+1}
  \mathbf P_{p+}(X/(dp))
 \right]
 =N_X-\mathfrak D_X
 =-\mathcal R_X.
}
\tag{L-92920.7}
\]

Consequently

\[
 \boxed{
 \Sigma\mathbf F_{61,X}
 +\Sigma\mathbf P_X^{\rm actual\ rough\ children}
 =N_X.
 }
\tag{L-92920.8}
\]

Actual paired children do not add their full native capacities to the finite
forcing.  Their oriented signed observation removes the rough reservoir.

## 5. Two forbidden substitutions

The following are different errors:

1. **Internalize first-owner slices of the rough lift.**  A stochastic split of
   `mathfrak D_X` followed by label erasure still equals `mathfrak D_X`; it does
   not become `N_X`.  `R-92920` then gives the exact `q=2` separator.
2. **Promote actual children to full native child capacities.**  Replacing the
   oriented child observation in (L-92920.7) by a positive copy of
   `mathcal R_X` changes the total from `N_X` to `N_X+2mathcal R_X`.

Neither substitution is a consequence of source ownership, target-mass
contraction, or same-index placement.

## 6. Correct acceptance contract

A one-shot physical compiler must retain, until after physical placement, the
complete label

```text
endpoint cell;
small-prime parity channel;
least rough prime;
rough-channel orientation bit;
current/child owner;
same-index physical placement.
```

For every actual child `b`, its positive physical realization `R_b` must obey

\[
 \boxed{
 \mathcal O(R_b)
 =\Sigma\bigl(S^{\varepsilon_b}\mathbf P_b\bigr),
 }
\tag{L-92920.9}
\]

in the declared typed observations.  It must not be replaced by
`Omega(P_b)` or by the unoriented marginal.

## 7. Boundary

```text
full paired source -> native packet                  exact
finite P61 forcing -> rough lift                     exact
extra rough-prime swap                               load bearing
actual rough-child signed sum                        minus rough reservoir
full-capacity child promotion                        forbidden
rough-lift label erasure                             does not yield native
paired-orientation compiler                          next lemma
Riemann Hypothesis                                   unproved
```
