# Source-complete factor-67 proof of the two-row annular producer

**Status:** candidate complete unconditional RH proof proposal; hostile independent reconstruction required.  
**Base:** PR #547 at `d60f93b0e207a83a283fb229eb988aa4c404765d`.  
**Compared:** PR #552 at `81df9c3f507aba0e5f21187044583a0d6fb90db9`; PR #555 at `341697b4694ba7f44f2ba2be73cb3fc982939412`.  
**Riemann Hypothesis:** not treated as established by publication.

## 1. Firewalls

This proof does not use the reservoir mechanisms refuted in PR #552. A fixed-product divisor cube may cancel equal-knot atoms but may not manufacture a three-knot convex packet. An all-integer interval is not an available rough reservoir. A signed color `d|P_61` is never promoted to a positive leaf. Every terminal theorem is applied only after the complete `P_61` color family has been summed. No oriented rough child is physically observed; no full child capacity, port, endpoint deficit, `J_Lambda/P_Lambda/F_Lambda` bridge, NEDB, or Target–Lorenz tail is used.

## 2. Scale-four source and fixed-row notation

Put

\[
 H_x(n)=\min\!\left(\log4,\log\frac xn\right)_+,
 \qquad
 A_x(j)=Q_x(j)-Q_{x/4}(j).
\]

Let

\[
 P=P_{61}=\prod_{p\le61}p,
 \qquad
 E_j(x)=\sum_{d\mid P}\frac{\mu(d)}{\sqrt d}A_{x/d}(j),
 \quad j=2,3.
\tag{2.1}
\]

The complete two-row annular Riesz state is

\[
 a_X(j)=c_X(j)-c_{X/4}(j)
 =\sum_{n\le X}\frac{r_j(n)}{\sqrt n}H_X(n),
\tag{2.2}
\]

with

\[
 r_2(n)=\mathbf1_{n=1}-\mu(n)+2\mathbf1_{2\mid n}\mu(n/2)-\mathbf1_{3\mid n}\mu(n/3),
\tag{2.3}
\]

and

\[
 r_3(n)=\frac13\mathbf1_{n=1}-\frac13\mu(n)-\frac13\mathbf1_{2\mid n}\mu(n/2)+\frac53\mathbf1_{3\mid n}\mu(n/3)-\mathbf1_{4\mid n}\mu(n/4).
\tag{2.4}
\]

## 3. Scale-four harmonic quadrature

Define

\[
 K(x)=\sum_{n\ge1}\frac{H_x(n)}{\sqrt n}.
\]

For every real `x>=1`,

\[
 \boxed{
 K(x)=2\sqrt x+\kappa_4+e_4(x),
 \qquad
 \kappa_4=\zeta(1/2)\log4,
 \qquad
 |e_4(x)|\le\frac1{6\sqrt x}.}
\tag{3.1}
\]

To prove this, write `K(x)=G(x)-G(x/4)` with

\[
 G(x)=\sum_{n\le x}n^{-1/2}\log(x/n).
\]

On each unit cell, both terms are affine in `log x`. Two-term Euler summation for the generalized harmonic sum and its exponent derivative gives

\[
 G(x)=4\sqrt x+\zeta(1/2)\log x-\zeta'(1/2)+R(x).
\]

One integration by parts of the periodic Bernoulli remainder, using `|B_2({t})|<=1/6`, gives

\[
 |R(x)-R(x/4)|\le(6\sqrt x)^{-1}.
\]

The finitely many initial cells are checked by the same exact cell formula. Subtraction cancels `zeta'(1/2)` and proves (3.1). No zero-free information enters.

## 4. Complete P61 annular reserve

Write `q_j=C_j*1+h_j`. For row two,

\[
 C_2=1,
 \quad h_2(1)=-1,
 \quad h_2(2)=2,
 \quad h_2(3)=-1.
\]

For row three,

\[
 C_3=1/3,
 \quad h_3(1)=h_3(2)=-1/3,
 \quad h_3(3)=5/3,
 \quad h_3(4)=-1.
\]

Define

\[
 \Phi(x)=\sum_{d\mid P}\frac{\mu(d)}{\sqrt d}H_x(d),
\]

\[
 A_P(x)=\sum_{\substack{d\mid P\\d\le x}}\frac{\mu(d)}d,
 \quad
 B_P(x)=\sum_{\substack{d\mid P\\d\le x}}\frac{\mu(d)}{\sqrt d},
 \quad
 N_P(x)=\#\{d\mid P:d\le x\}.
\]

Finite rearrangement gives

\[
 E_j(x)=C_j\sum_{d\mid P}\frac{\mu(d)}{\sqrt d}K(x/d)
 +\sum_a\frac{h_j(a)}{\sqrt a}\Phi(x/a).
\tag{4.1}
\]

The exact activation sweep over `d` and `4d`, for all `262144` divisors `d|P`, proves

\[
 \boxed{|\Phi(x)|<3/2\qquad(x>0).}
\tag{4.2}
\]

Combining (3.1) and (4.1),

\[
\begin{aligned}
 E_j(x)\ge{}&2C_j\sqrt x\,A_P(x)
 +C_j\kappa_4B_P(x)
 -\frac{C_jN_P(x)}{6\sqrt x}\\
 &-\frac32\sum_a\frac{|h_j(a)|}{\sqrt a}.
\end{aligned}
\tag{4.3}
\]

A second exact divisor-event sweep proves `A_P(x)>1/100` for `x>=67`. At every divisor event `x>=2000`, the right side of (4.3) is larger than `6` in row two and larger than `3/5` in row three. Between divisor events it is increasing, so the event check covers the full real tail.

The compact original-row replay on `1<=x<=2000`, together with affine-in-`log x` cell reduction, proves

\[
\boxed{
\begin{array}{ll}
0\le E_2(x)<5/2,&0\le E_3(x)<1,\qquad 1\le x<67,\\[2mm]
E_2(x)>7/5,&E_3(x)>1/2,\qquad x\ge67.
\end{array}}
\tag{4.4}
\]

The compact minima occur near `x=104` and `x=102`; the analytic splice is not the limiting case.

## 5. Kernel-independent least-owner tree

The positive annular source coefficient is

\[
 h_X(n)=n^{-1/2}H_X(n).
\]

It has exact scale covariance. If `n=pm`, then

\[
 p^{-1/2}h_{X/p}(m)=h_X(pm).
\tag{5.1}
\]

Therefore

\[
 h_X-p^{-1/2}A_ph_{X/p}
\]

is literally `h_X` restricted to indices not divisible by `p`; it is positive.

For ordered active rough primes `p_i>=67`, put

\[
 r_i=p_i^{-1/2},
 \quad s_i=\prod_{\nu\le i}(1-r_\nu),
 \quad \lambda_i=r_is_{i-1},
 \quad \alpha_i=r_i\lambda_i.
\]

The exact causal identity is

\[
P_X=s_kP_X+
\sum_i\lambda_i(P_X-r_iA_{p_i}P_{X/p_i})+
\sum_i\alpha_iA_{p_i}P_{X/p_i}.
\tag{5.2}
\]

It is polynomial algebra:

\[
s_k+\sum_i\lambda_i=1,
\qquad
-\lambda_ir_i+\alpha_i=0.
\]

Only positivity and (5.1) are used, so the identity applies to the annular packet. Recursive children have scale at most `X/67`; the tree terminates after finitely many generations.

Crucially, the finite colors `d|P_61` are passive labels throughout the rough tree. They are never split or observed. At a terminal current edge with owner `p`, the complete color family is summed first, and the row is exactly

\[
 E_{j,Pp}(Z)=E_j(Z)-p^{-1/2}E_j(Z/p).
\tag{5.3}
\]

This is the complete-color repair of the ambiguous individual-leaf wording in PR #555.

## 6. Terminal leaves and root positivity

A terminal rough current has `Z=py`, with `p>=67` and `1<=y<67`. By (4.4) and (5.3),

\[
\begin{aligned}
 E_{2,Pp}(py)
 &>\frac75-\frac{5/2}{\sqrt{67}}
 >\frac{87}{80}>0,\\
 E_{3,Pp}(py)
 &>\frac12-\frac1{\sqrt{67}}
 >\frac38>0.
\end{aligned}
\tag{6.1}
\]

The rational inequalities use only `sqrt(67)>8`. A terminal outer packet with no rough owner has scale below `67` and is nonnegative by the compact line of (4.4).

Apply the finite tree to the positive parity-labelled annular root. Every coefficient `s_k`, `lambda_i`, and `alpha_i` is nonnegative; every current leaf satisfies (6.1); every child is treated recursively; and the process terminates. The root signed observations are therefore

\[
 \boxed{a_X(2)\ge0,\qquad a_X(3)\ge0\qquad(X\ge1).}
\tag{6.2}
\]

The observation is exactly (2.2), not a rough lift, a promoted capacity, or a branchwise child row.

## 7. Direct Mellin–Landau conclusion

PR #547 proves, for `j=2,3`,

\[
\int_1^\infty a_X(j)X^{-s-1}\,dX
=(1-4^{-s})
\left[
 \frac{C_j}{s^2}
 +\frac{P_j(s+1/2)}{s^2\zeta(s+1/2)}
\right].
\tag{7.1}
\]

The factor `1-4^{-s}` has no zero in `Re s>0`. The two finite numerators have no common zero in the open critical strip: with `x=2^{-z}`, simultaneous vanishing gives

\[
 -3(x-1)(x-2)=0,
\]

forcing `Re z=0` or `Re z=-1`.

The two nonnegative kernels (6.2), Landau's real-abscissa theorem, and the functional equation therefore give the proposed conclusion

\[
 \boxed{\mathrm{RH}.}
\]

## 8. Review boundary

Publication is not acceptance. Immediate falsifiers are: a failure of the scale-four quadrature bound; an omitted `P_61` activation event; a duplicated or separated finite color; a negative grouped terminal row; a mismatch between the root observation and (2.2); or a failure of the fixed-row Mellin transform or Landau hypotheses.

The deterministic proof object records

```text
PASS_SOURCE_COMPLETE_ANNULAR_FACTOR67_CANDIDATE
6b4b29f0ee4d6500df59693f109723c58bcc1ddaa2998df718ae5f1e5e59e9d1
```

RH remains classified as unestablished pending hostile independent reconstruction.
