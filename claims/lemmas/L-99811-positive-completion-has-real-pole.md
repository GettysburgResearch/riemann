# L-99811 — Every nontrivial coefficientwise-positive inverse-renewal completion has a real pole at the critical boundary

Claim ID: `L-99811`  
Status: **PROVED EXACT NO-GO THEOREM**  
Created: 2026-08-20  
Depends on: the positive inverse renewal of PR #653  
RH status: **not assumed**

Let

\[
 \beta(n)=\mu(n)-\mathbf1_{67\mid n}\mu(n/67),
 \qquad
 g(n)=v_{67}(n)+1.
\]

Then

\[
 \boxed{\beta*g=\delta_1,}
\tag{L-99811.1}
\]

and

\[
 G(z):=\sum_{n\ge1}\frac{g(n)}{n^z}
 =\frac{\zeta(z)}{1-67^{-z}}
 \qquad(\Re z>1).
\tag{L-99811.2}
\]

Suppose `w(n)>=0` and

\[
 a:=\beta*w
\]

is coefficientwise nonnegative and not identically zero. Convolving with `g`
gives

\[
 \boxed{w=g*a.}
\tag{L-99811.3}
\]

In the absolute-convergence half-plane,

\[
 W(z)=G(z)A(z).
\tag{L-99811.4}
\]

Choose `n_0` with `a(n_0)>0`.  For real `z>1`,

\[
 A(z)\ge a(n_0)n_0^{-z},
\]

so `A(z)` is bounded away from zero as `z downarrow 1`.  Since `G` has a
simple positive-real pole at `z=1`, `W` has a positive-real singularity there
(or diverges more strongly).

Now form the nonnegative SHARP completion

\[
 H_w(x)=\sum_{n\le x}\frac{w(n)}{\sqrt n}T(x/n).
\]

Its Mellin transform contains `W(s+1/2)` and therefore has a real singularity
at

\[
 \boxed{s=1/2.}
\tag{L-99811.5}
\]

Landau consequently stops at the critical real boundary and supplies no
holomorphy in `0<Re(s)<1/2`.  Such a completion cannot exclude an off-line zero
of zeta.

## Consequence

A proof cannot finish by applying any positive arithmetic convolution to the
inverse-renewal source and then invoking Landau.  The cancellation must be
retained before coefficientwise positivity—through a source-specific
cross-core estimate, a phase-adaptive owner theorem, or an equivalent signed
boundary argument.

This theorem includes the naive choice `w=g`, for which `a=delta_1`, as the
minimal example.  The obstruction is not a poor choice of positive inverse; it
is universal over all nontrivial coefficientwise-positive completions.
