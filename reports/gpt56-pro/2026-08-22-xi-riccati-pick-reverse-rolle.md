# Research report — Xi Riccati–Pick reverse-Rolle cascade

## Executive result

Levinson's reverse-Rolle intuition admits an exact mathematical formulation,
but the coefficient and the state variables differ from the original
one-point proposal.

The exact generic polynomial law is

\[
\boxed{
N_{\rm nr}(p)-N_{\rm nr}(p')=2E(p),
}
\]

not a coefficient-one inequality.  Here `E(p)` counts positive local minima
and negative local maxima.

On a finite complex domain the missing data are not an unspecified boundary
error.  They are the explicit argument-principle winding of `F/F'` and two
real endpoint defects.  The derivative ladder is governed by the exact
Riccati recursion

\[
h_{k+1}=h_k-h_k'/h_k,
\qquad
h_k=-F_{k+1}/F_k.
\]

Finally, the Ki / Gunns–Hughes cosine limit has a stronger zero-theoretic
consequence than is usually stated: every sufficiently high Xi derivative has
only simple real zeros on every fixed scaled complex box.  This follows from
Rouche plus conjugation symmetry.

Together these results turn the old intuition into an exact defect
conservation programme.  They do not prove RH.  The remaining work is now two
quantified gates rather than one vague converse to Rolle.

## 1. Why the original one-point count fails

At a critical point `c`,

\[
\mathcal L_f(c)=-f(c)f''(c).
\]

A negative value detects a positive minimum or negative maximum.  But one such
wrong extremum removes two potential real crossings, one on each side.

The polynomial

\[
x^4-2x^2+2
\]

has four nonreal zeros and two wrong extrema.  The even Cartwright entire
function

\[
2+\cos z
\]

has no real zeros, while every derivative zero is real and only half are wrong
extrema.  Thus coefficient one fails even under reality, parity, order one and
Cartwright growth.

## 2. Exact adjacent-edge theorem

If

\[
a<c_1<\cdots<c_m<b
\]

are the simple critical points of a real analytic `f`, then `f` is monotone on
every interval between consecutive entries of

\[
a,c_1,\ldots,c_m,b.
\]

Therefore

\[
N_\mathbb R(f;(a,b))
=
\sum_j
1_{f(c_j)f(c_{j+1})<0}.
\]

This is the correct primitive reverse-Rolle quantity: a two-critical-value
edge, not one isolated extremum.

After classifying the alternating maxima and minima, the count becomes

\[
N_\mathbb R(f;(a,b))
=m+1-2E-B_--B_+.
\]

The endpoint defects are explicit bits in `{0,1}`.  They disappear for a
polynomial on the whole real line.

## 3. Complex zero transport

For a real entire function on a conjugation-symmetric Jordan domain,

\[
W(F,F';\Omega)
={1\over2\pi i}
\int_{\partial\Omega}
\left(F'/F-F''/F'\right)dz
=N_\Omega(F)-N_\Omega(F').
\]

Combining this with the real count gives

\[
O_\Omega(F)
=
O_\Omega(F')+2E+B_-+B_++W-1.
\]

Iterating gives a complete derivative-ladder ledger.  No `O(1)` boundary term
is allowed to hide when the derivative order grows.

## 4. Riccati–Pick reformulation

Put

\[
h_k=-F_{k+1}/F_k.
\]

Then

\[
F_{k+1}^2-F_kF_{k+2}=F_k^2h_k',
\]

and

\[
h_{k+1}=h_k-h_k'/h_k.
\]

At a critical point, a wrong extremum is exactly a negative-slope zero of
`h_k`, equivalently a positive residue of `F_k/F_(k+1)`.  It is also a negative
diagonal node of the confluent Pick kernel

\[
K_k(z,w)
={h_k(z)-\overline{h_k(w)}\over z-\overline w}.
\]

This is the correct interface with Pick/Loewner methods.  The safe-line
actual-Xi order-three theorem is not automatically an all-order theorem for
these derivative-ratio kernels.

## 5. High-derivative entry is already an unconditional theorem

Ki proved the locally uniform convergence

\[
A_n\Xi^{(2n)}(C_nz)\to\cos z,
\qquad C_n\to0.
\]

Gunns and Hughes proved the corresponding Selberg-class result and explicit
scalings.

Fix a bounded conjugation-symmetric box whose boundary avoids cosine zeros.
Choose disjoint symmetric disks around the finitely many cosine zeros.  Rouche
gives exactly one high-derivative zero in each disk and no zeros elsewhere.
Because the approximating function is real entire, one nonreal zero would
force its conjugate into the same disk, contradicting the count one.  Hence the
zero is real and simple.

By differentiating the locally uniform convergence, the same is true for any
fixed finite band of subsequent derivatives.

This is a genuine unconditional finite-depth derivative cascade.

## 6. Why this still does not prove RH

The physical box is `C_n` times the fixed scaled box and therefore shrinks.
For a fixed original height `T`, one needs uniform cosine control on a scaled
box of width `T/C_n`, which grows with `n`.

Even after such a high-derivative base case, one must descend the complete
integer defect ledger.  The exact closure target is

\[
\mathfrak C_r(T)
=2\sum E_k+
 \sum(B_{k,-}+B_{k,+}+W_k-1)<2.
\]

If the top derivative has no off-real zero, this charge equals the off-real
zero count of Xi.  It is a nonnegative even integer, so a bound below two
forces it to vanish.

## 7. The redesigned programme

The original programme is replaced by two precise terminal theorems.

### GBOX104500

Prove a quantitative saddle-point/cosine approximation on the expanding scaled
rectangles corresponding to each fixed original height.  The estimate must be
Rouche-safe simultaneously around every cosine zero and on the zero-free
complement.

### RPCH104500

Control the cumulative derivative-ratio Pick defect and boundary winding so
that the exact charge is below two.  This may use:

```text
negative spectral mass of K_k;
adjacent critical-value signs;
argument variation of F_k/F_(k+1);
growing-order Levinson–Conrey estimates;
integer rigidity of the final count.
```

A proportion estimate is useful only after it is uniform enough that
exceptional proportion times total zero count is below two.

## 8. Relationship to the literature

- Levinson and Montgomery initiated the derivative-zero programme.
- Conrey proved explicit derivative-line proportions tending to one with the
  derivative order.
- Ki proved the Riemann-Xi cosine limit under repeated differentiation.
- Gunns and Hughes extended that limit to the Selberg class.
- The factor-two polynomial law is closely related to the real-critical-point
  and Hawaii-conjecture literature; this packet's new emphasis is the exact
  adjacent-edge, complex-winding and Riccati-Pick cascade needed for Xi.

The often-quoted numerical claim about more than 99 percent of the zeros of
`xi'''` is not frozen here because the exact table and counting convention were
not independently recovered in this pass.

## 9. Status

```text
exact real reverse-Rolle conservation         PROVED
complex winding transport                     PROVED
Riccati/Pick derivative dynamics              PROVED
fixed-scaled-box high derivative real zeros   PROVED
finite-depth scaled cascade                   PROVED
GBOX104500                                     OPEN
RPCH104500                                     OPEN / RH-BEARING
Riemann Hypothesis                             UNPROVEN
```
