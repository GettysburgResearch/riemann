# Independent check of the fixed-a near-line bridge

2026-11-17. Reviewer `/root/li_skeptic`. Scope: **THM-LC402**, §5 of `audits/littlewood_dependency_corpus_round4.md`. The proposed geometry and estimates were read and reconstructed independently. **No issue found under the two explicit classical inputs below.** This checks the local mathematical bridge, not the complete historical Littlewood/Titchmarsh ancestry.

The actual Titchmarsh1986 pp354–355 had already been independently visually read in the Riesz review; the existing image and primary source were reused. No new work or whole-book reading count is created. Riesz/Littlewood original-paper ancestry remains partially accessed as the corpus note states. No OCR-missing formula is promoted to a verified primary statement.

## Precise accepted inputs and branch

Let `f(s)=log zeta(s)` be the analytic continuation of the Euler logarithm from the right in the high half-plane `Re(s)>1/2, Im(s)>T_*`, under RH. It is not a separately selected principal logarithm at each point. The pole at1 is outside this high domain, and RH excludes zeros within it. A single holomorphic branch therefore exists and agrees with the absolutely convergent Euler logarithm on `Re(s)=2`.

Write `L(t)=log t/loglog t`. The accepted legible source input supplies fixed positive constants `A_0,C,C_0,T_*` with

\[
 \operatorname{Re}f(\sigma+it)\le C L(t)
 \qquad(\sigma>1/2,\ t\ge T_*),
 \tag{B1}
\]

and, on the one **fixed** equality curve,

\[
 |f(1/2+A_0/\log\log t+it)|\le C_0L(t).
 \tag{B2}
\]

These come from the upper-bound proof of14.14(A) and the same continued-log convention in14.14.3–4. It is enough to assume(B1) up to real part7/2; the Euler logarithm supplies any further right extension. The argument never treats the source's unspecified `A` as an arbitrary shrinking parameter. Only after fixing the source's `A_0` does it introduce a new `a>0` and track its Borel–Carathéodory loss.

## 1. The near-line disk has the claimed safe geometry

Fix `0<a<A_0` and put `mu=1/loglog t`. Center a disk at

`s_0=1/2+A_0 mu+it`.

Take outer radius `R=(A_0-a/2)mu` and inner radius `r=(A_0-a)mu`. Then

- `R>r>=0`, and `R-r=a mu/2`;
- the outer disk's leftmost real part is `1/2+(a/2)mu>1/2`;
- the inner disk's leftmost real part is `1/2+a mu`;
- at large `t` the disk's radius is less than one, so all imaginary parts stay large and `L(Im s)` is uniformly comparable to `L(t)`.

Thus the holomorphic branch is defined on a neighborhood of the outer closed disk, and the disk does not touch any possible critical-line zero. The real upper bound on that disk is at most `C' L(t)`, while(B2) gives its center value. The standard Borel–Carathéodory estimate yields

\[
 \sup_{|s-s_0|\le r}|f(s)|
 \le\frac{2r}{R-r}\sup_{|s-s_0|\le R}\operatorname{Re}f(s)
       +\frac{R+r}{R-r}|f(s_0)|
 \le C'(1+A_0/a)L(t).
\]

The formula is valid even if the center's real part is negative; its usual proof first estimates `f-f(s_0)` and then uses the absolute center value. This covers the whole real segment `1/2+a mu<=sigma<=1/2+A_0 mu`. The original proposition's constants may depend on the fixed `a`; there is no hidden fixed-epsilon estimate being substituted for a moving one.

## 2. A complete right-region argument without equality-line extrapolation

The source14.14.5 plus a fixed-strip Phragmén–Lindelöf bridge is one valid way to control the right region. The alternative curved-region maximum-principle argument in the corpus note can also be made fully explicit as follows.

Choose `T_0` large enough that the accepted source bounds hold in every disk below, that `T_0>4`, and that `delta_t=A_0/loglog t<1`. Consider

\[
 \Omega=\{s=\sigma+it:t>T_0,
        \theta(t)<\sigma<2\},
 \qquad \theta(t)=1/2+A_0/\log\log t.
\]

Define the holomorphic normalizer

\[
 D(s)=\frac{\operatorname{Log}(s+3)}
 {\operatorname{Log}(\operatorname{Log}(s+3))}.
\]

Both principal logarithms used in **this normalizer** are legitimate: for `Re(s)>1/2`, one has `Re Log(s+3)>log(7/2)>1`, so the inner logarithm lies in the right half-plane and its logarithm is analytic and nonzero. The normalizer is therefore analytic and zero-free. Uniformly for `1/2<=sigma<=2` at large height, `|D(s)|` is comparable to `L(t)`.

Set `G=f/D`. On the left boundary(B2) makes `G` bounded. On the right boundary the Euler logarithm is uniformly bounded, so `G` is bounded. On the fixed bottom segment `G` is continuous and bounded. These bounds depend on the fixed source data but not on the later damping parameter.

To justify the upper truncation, first prove only a crude growth estimate for `G` throughout `Omega`. At each height `t`, center another disk at `2+it`, take outer radius `R_t=3/2-delta_t/2` and inner radius `r_t=3/2-delta_t`. The outer left edge is `1/2+delta_t/2>1/2`, and every point of the horizontal segment `theta(t)<=sigma<=2` lies in the inner disk. The height changes by at most3/2, so(B1) applies with comparable `L(t)`. The center Euler logarithm is bounded. Borel–Carathéodory gives

\[
 |f(\sigma+it)|\le C\delta_t^{-1}(L(t)+1)
 =O(\log t),
\]

and hence `G(s)=O(loglog t)` uniformly in the entire curved strip. The use of an analytic branch, rather than a principal pointwise logarithm, is essential in this disk argument.

For fixed `eta>0`, apply the maximum principle on the finite curved domain `Omega intersect {t<H}` to `G(s)exp(eta s²)`. On its upper edge the preceding polylogarithmic bound is killed by `exp(-eta H²+4eta)`, so that edge tends uniformly to zero as `H` tends to infinity. On its other edges, `sigma<=2` and `t>=T_0>4` imply `|exp(eta s²)|<=1`. Their bounds are consequently uniform in `eta`. Letting `H` tend to infinity and then `eta` decrease to zero proves that `G` is bounded on all of `Omega`. Thus

\[
 |f(\sigma+it)|\le C L(t)
 \quad(\theta(t)\le\sigma\le2).
 \tag{B3}
\]

This supplies the whole right region without treating(B2), an equality-curve estimate, as if it already held in a half-plane. The truncation order is explicit; no growth bound at infinity is silently assumed.

## 3. The full fixed-a statement and its exact limit

Combine the near-line disk bound with(B3). For every fixed `a>0`, after raising the threshold if necessary,

\[
 |\log\zeta(\sigma+it)|\le K_a\frac{\log t}{\log\log t},
 \quad 1/2+a/\log\log t\le\sigma\le2.
\]

For `a>=A_0`, this is simply a subset of(B3). For `0<a<A_0`, the disk step gives the stated controlled loss `O(1+A_0/a)`. Real parts supply both zeta and reciprocal-zeta exponential bounds. Complex conjugation gives the analogous negative-height result with the compatible branch; only absolute values are needed for the reciprocal conclusion.

The finite-height conversion `t` to an independent bound `V`, and its low-height logarithm of `(s-1)zeta(s)` patch, are **separate** lemmas. This proof does not replace them by a formal `t=V` substitution. It also does not assert a new theorem for a parameter `a=a_N` tending to zero, effective constants or a usable numerical threshold. Those would need the remaining parameter dependencies and contour choices tracked separately.

No flaw was found in THM-LC402 within these precisely stated inputs. The classical source ancestry remains partial: the argument accepts the actually legible1986 source bounds(B1)–(B2), and does not certify every original1924/1927 proof passage.
