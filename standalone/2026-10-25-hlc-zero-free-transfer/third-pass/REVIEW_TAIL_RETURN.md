# Independent review of the coherent tail return

Reviewer: `fractional_native`, independently of the author.

**Verdict: PASS for the exact local algebra, natural-factor identification,
and explicitly limited contour-resource comparison.** The note does not
prove a new tail moment, a global contour deformation, or a lower bound
for the actual signed moment. Its conclusions remain correctly scoped to
those distinctions.

I applied only the authorized wording correction:
“one full L function divided by two inverse factors” was changed to
“one full L function multiplied by two reciprocal factors.”
No displayed formula or mathematical argument was changed.

## Exact reviewed bytes

| File | Bytes | SHA-256 | Git blob |
|---|---:|---|---|
| `TAIL_RETURN.md` | 11,575 | `857916fd4dc98b89749e172ccab4f13005594e0a9e38cd41d31ec784c3484da4` | `6f23b05dcde927022ed690898cd93767b61b0583` |
| `check_tail_return.py` | 7,046 | `b3a380994c7c27aa1b4afda5f8a218a73edececeb12a7a48c5d7078863c1aed8` | `dd0390dcea00cb2048b4249cc9df2d3068ccf556` |

These are hashes of the complete local files actually reviewed after the
permitted wording repair. They do not by themselves authenticate a
remote mathematical commit. The note's status line still says that
independent review was requested; the present file supplies that review.

## 1. The local identity retains the gcd and both signs

At a good prime, the original two-inverse coefficient has local values
$1,-(r+t),rt$ at exponents zero, one and two. Summing the residual
gcd with its harmonic weight gives exactly

\[
 1-\frac{r+t}{q}+\frac{rt}{q^2}=\Delta,\qquad
 -(r+t)+\frac{rt}{q},\qquad rt.
\]

In particular the $rt/q$ term in the exponent-one coefficient is a
genuine repeated-prime term, not an optional correction.

The variables $X,Y$ satisfy $XY=u$ only on the unit support.
The reduced coprimality condition allows the geometric $b$-series only
when the exponent of the numerator $a$ is zero. Consequently the
complete local factor is

\[
 \frac{\Delta}{1-Y}-(r+t-rt/q)X+rtX^2.
\]

Multiplying by $1-Y$ and replacing $XY$ by $u$ gives

\[
 \mathcal N_p
  =(1-rX)(1-tX)
    +(u-1/q)(r+t-rt/q-rtX),
\]

with exactly the signs stated in equation (2). At $h=0$,
$u=1/q$, and the remainder cancels identically.
I independently expanded both sides; the supplied checker also proves
this generic polynomial equality by coefficient comparison.

The note does not apply $XY=u$ at a primitive ramified prime. It also
does not impose a new $Q_s$ zero on the primitive dual denominator.
These two restrictions are necessary.

## 2. The primitive return gives the exact natural L factors

I checked the finite-factor issue directly, in addition to the note's
primal check. At a redundant natural puncture $p$, the original
numerator and gcd variables have zero character value if divisible
by $p$, whereas the primitive dual variable need not.
After Mellin inversion of the reflected kernel, its $e$-divisor
factor at that prime is

\[
              1-\psi^*(p)(Np)^{v-1}
                =1-\psi^*(p)(Np)^{-w}.
\]

The primitive denominator still has its full local factor
$(1-\overline{\psi^*(p)}(Np)^{-v})^{-1}$.
Applying the primitive functional equation to the full denominator
and retaining the outside $e$ factors therefore gives

\[
 L(w,\psi^*)\prod_{p\mid Q_s}
                      (1-\psi^*(p)(Np)^{-w})
                         =L_\psi(w).
\]

At a primitive conductor prime the character value is zero, and the
corresponding local factors are one. The two reciprocal good-prime
products omit precisely the natural punctures, so they are
$L_\psi(w+s)^{-1}$ and $L_\psi(w+z)^{-1}$, not reciprocals for
a differently masked primitive family. All fixed ray presentations
are treated separately before the original finite outer combination
is summed.

The conductor, gamma, and root-number factors belong to the ordinary
functional equation and the transformed common profile, as in the
already reviewed native reflection. The note's independent primal
formula (5) confirms the final common factor without inferring a
contour shift from this local calculation.

In that primal formula one may take $\operatorname{Re}w>1$ and
positive real parts for $s,z$. Then $L_\psi(w)$ and both
reciprocal Euler series are absolutely convergent, and the three
Mellin densities have sufficient decay. The smooth truncated sums
are finite. Thus the triple integral is genuinely the original
smooth convolution on its annulus.

There is no common region where both ordinary Euler series at $w$
and $v=1-w$ converge absolutely; such a region is not needed or
claimed. The reflected calculation uses the ordinary functional
equation as a global meromorphic identity, while the independent
primal formula has its own valid absolute-convergence region.
Neither fact licenses moving an integration contour through a
reciprocal pole.

The full smooth outer support through $8D$ is preserved. Terms that
vanish only after summing their complete primal or reflected
expression cannot be removed before the coefficient is regrouped.

## 3. No reciprocal of the dangerous local polynomial is used

The only scalar normalization of the gcd polynomial is division by
$\Delta$. On the harmonic contours of the companion theorem,
$\operatorname{Re}(1+s),\operatorname{Re}(1+z)>0$, so the two
factors of $\Delta$ are nonzero. This is different from dividing
by the quadratic $\mathcal D_p(X)$ in equation (6).

I independently checked the counterexample:

\[
 q=7,\quad r=t=5/4,\quad \Delta=529/784,
\]

\[
 \mathcal D_p(2/5)=11/529>0,\qquad
 \mathcal D_p(1/2)=-229/2116<0.
\]

Hence it has a real zero inside that interval, while both ordinary
factors $1-rX,1-tX$ are at least $3/8$ throughout the interval.
Moreover $(5/4)^8<7$ gives the stated $\beta>7/8$, and

\[
 X<1/2<16/25=7^{-(2-2\beta)}
\]

places the example to the right of the claimed correction-product
boundary in its real Dirichlet exponent.

This disproves a blanket justification for inverting that quadratic
using only the nonvanishing of the ordinary local factors.
It does not assert that this zero lies on a valid buffered reciprocal
contour, nor that it creates an actual adverse family moment.
The note's argument never takes the forbidden
$\mathcal D_p(X)^{-1}$: it retains the complete coprimality sum
instead.

## 4. The contour comparison is exact but intentionally limited

At $B\asymp D$, the reduced-numerator cutoff supplies $U^{rh_0}$.
Set $m=\min(s_0,z_0)$. The two stipulated reciprocal conditions imply
$\operatorname{Re}w+h_0\ge a-m$, so the complete scale power obeys

\[
\begin{split}
 &r(\operatorname{Re}w-1/2)+rh_0+
                         \alpha s_0+(r-\alpha)z_0\\
 &\quad\ge r(a-1/2)+
       \alpha(s_0-m)+(r-\alpha)(z_0-m).
\end{split}
\]

Both additional terms are nonnegative for $0<\alpha<r$.
Equality requires $s_0=z_0$ and equality in the active reciprocal
line constraint. The scale contribution of the reduced-numerator
contour cannot simply be discarded. In the balanced equal-shift
case the apparent $D^{-\theta}$ cutoff saving is canceled exactly
by the required $D^\theta$ displacement.

This is a generic affine identity and inequality. It remains valid
for the unequal cutoffs in the note, with the fixed support constants
absorbed in the exponent convention. It concerns an optimistic
pointwise estimate in which the numerator and correction factors
are granted subpower cost. It proves neither a global continuation
of those correction products nor an admissible shift for every
displayed contour.

The comparison with the existing density resource is also correctly
limited. At $a=4/5$ the density exponent is $9/19$, and the
difference between that proposed resource and the desired target is

\[
 \frac9{19}+\frac35r-\left(\frac{1+5r}{6}-\frac1{1000}\right)
      =\frac{35}{114}-\frac7{30}r+\frac1{1000}.
\]

This affine function is decreasing in $r$. Its minimum on
$[29/25,117/100]$ is the exact positive number
$499/14250$. Thus the interval claim follows from the endpoint
calculation, not from interpolation between sampled grid points.

An admissible upper-bound bin is not a proof that the bin is
populated, and the outside scale is not a lower bound for the
actual signed integral. The note explicitly preserves both
qualifications. Its conclusion is that this particular direct
contour estimate does not close the target. Coherent cancellation,
a new joint moment, or exclusion of the relevant class remain
possible additional inputs.

## 5. Checker replay and review limits

I independently ran the unchanged checker under `python -O`.
It passed:

- two generic polynomial coefficient identities, with twelve nonzero
  monomials in the coherent numerator;
- six exact local-root predicates;
- 8,100 rational scale predicates;
- 23 density-resource predicates.

The negative controls detect removal of the repeated-prime term,
removal of reduced coprimality, and omission of the required contour
displacement; the last mutation fails in 1,224 tested cases.
Every predicate is an explicit runtime check and survives optimized
Python execution.

The arithmetic scope is inherited from the exact pinned source
and reviewed native identities cited in
`SIGNED_NATIVE.md` and `GCD_NATIVE_COEFFICIENT.md`.
I did not independently certify the entire external zero-free
framework. The checker certifies finite algebra and rational
arithmetic; it cannot certify an analytic moment or global contour
deformation.

This note concerns the reduced gcd-ratio decomposition. Its
large-$B$ comparison must not be confused with the distinct proved
far-tail estimate for the unequal original-product decomposition
in `ASYMMETRIC_HB_TAIL.md`. The latter uses the original shorter
inverse second moment in addition to capped pointwise bounds,
and is not contradicted by the contour-scale audit here.
No overlap of those decompositions is estimated by the present
review.
