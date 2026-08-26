# Source-exact native reflection and half-divisor geodesic criteria for RH

Status: **exact native reflection/geodesic decompositions and exact analytic
equivalences; the one-sided estimates and RH remain unproved**

Bounded replay:
[`ffps_mollified_geodesic_rh_criterion.py`](ffps_mollified_geodesic_rh_criterion.py).

This packet gives a route around the open Boolean completion bridge in
`FFPS_MOLLIFIED_COMPLETE_SOURCE_ADAPTER.md`.  It does not prove that bridge.
Instead it retains the frozen continuous half-divisor homotopy all the way
from the native beta source to the analytic detector.

Read first:

1. frozen `L-102602`, `L-102700--L-102701`, and `L-102707--L-102708` at
   `ec6635b4`;
2. `FFPS_EXTRA_NOTCHED_MELLIN_LANDAU_CONSUMER.md`;
3. `FFPS_MOLLIFIED_BETA_RH_EQUIVALENCE.md`.

The replay pins these lemma blobs at the full commit
`ec6635b4c7dcd08fe433b7ae7e1d9a8c9495dfcc`, the extra-notched consumer at
`3f10a6be2009f8e499b1bd421fd97b2095a82b06`, and all four files of the
committed equivalence packet at
`9f29bdb6ea7375df84de550d62f9d0984634a8dd`.  It also pins the elementary
reflection convention of `L-106135` at
`356fbf29e958e2ea067bfe5ef912b1f68d0334c6`; the causal truncation needed for
the complete native field is proved below rather than imported from that
finite-source `L2` setting.

## 0. Outcome

Let `A` be the positive ratio-four spline, `B=A*_M A`, and

\[
 \Phi_*=(2D-1)B.
\tag{0.1}
\]

Write

\[
 P(D)={1\over2}D(D-1)(5D+3/2),
 \qquad
 \mathcal D_{\rm out}=P(D)(2D-1).
\tag{0.2}
\]

Thus the extra-notched kernel is exactly

\[
 K_{\rm ext}=P(D)\Phi_*=\mathcal D_{\rm out}B,
\tag{0.3}
\]

where, on expansion,

\[
 \mathcal D_{\rm out}
 =5D^4-6D^3+{1\over4}D^2+{3\over4}D.
\tag{0.4}
\]

Let `lambda` be the complete labelled half-divisor source of frozen
`L-102700`, so `lambda*lambda=beta`, and define its endpoint field

\[
 F_1(X)=\sum_{n\ge1}{\lambda(n)\over\sqrt n}A(X/n),
 \qquad I_1=F_1*_M F_1.
\tag{0.5}
\]

Fix `epsilon>0` and the positive log box `eta_epsilon`.  Pulling fields back
by `X=e^t`, the complete mollified beta density is exactly

\[
\boxed{
 h_\varepsilon
 =\eta_\varepsilon*P(D)H_{\rm nat}
 =\eta_\varepsilon*\mathcal D_{\rm out}I_1.}
\tag{0.6}
\]

This has a source-exact reflection form, but a finite-horizon fence is
essential because the complete `F_1` need not lie in global `L2`.  For an
observation horizon `T`, choose any `R>T` and put

\[
 f_{1,R}(u)=1_{[0,R]}(u)F_1(e^u),
 \qquad
 \mathcal O_{1,R}(x)
 =\left\|{f_{1,R}-f_{1,R}(x-\,\cdot)\over2}\right\|_2^2.
\tag{0.7}
\]

Then, as distributions before mollification and as ordinary densities after
it,

\[
\boxed{
 h_\varepsilon(t)
 =-2\eta_\varepsilon*\mathcal D_{\rm out}
       \mathcal O_{1,R}(t)
 \quad(0\le t\le T).}
\tag{0.8}
\]

The right side is independent of the choice of `R>T` on `[0,T]`.  Therefore,
for every one fixed `epsilon>0` and any choice such as `R(T)=T+1`,

\[
\boxed{
 \mathrm{RH}
 \Longleftrightarrow
 \int_0^T
 \left(\eta_\varepsilon*\mathcal D_{\rm out}
             \mathcal O_{1,R(T)}(t)\right)_+dt
 =e^{o(T)}.}
\tag{0.9}
\]

The continuous half-divisor path retains a useful root-free relative form.
Put `I_tau=G_tau*_M G_tau`.  Its endpoints are the squared and native
sources, and

\[
 I_1-I_0=\int_0^1 2(\dot G_\tau*_M G_\tau)\,d\tau.
\tag{0.10}
\]

The exact decomposition is

\[
\boxed{
 h_\varepsilon=\mathcal C_\varepsilon+\mathcal Q_\varepsilon,}
\qquad
\begin{aligned}
 \mathcal C_\varepsilon
 &=\eta_\varepsilon*\mathcal D_{\rm out}(I_1-I_0),\\
 \mathcal Q_\varepsilon
 &=\eta_\varepsilon*\mathcal D_{\rm out}I_0.
\end{aligned}
\tag{0.11}
\]

Here

\[
 \mathcal Q_\varepsilon(t)
 =\sum_{m\ge1}{\beta(m)\over m}
   \kappa_\varepsilon(t-2\log m),
 \qquad
 \kappa_\varepsilon=\eta_\varepsilon*K_{\rm ext},
\tag{0.12}
\]

and unconditionally

\[
 \int_0^T|\mathcal Q_\varepsilon(t)|\,dt
 \le2\|\kappa_\varepsilon\|_1
       \sum_{m\le e^{T/2}}{1\over m}
 =O_\varepsilon(1+T).
\tag{0.13}
\]

Consequently

\[
\boxed{
 \mathrm{RH}
 \Longleftrightarrow
 \int_0^T(\mathcal C_\varepsilon(t))_-\,dt=e^{o(T)}.}
\tag{0.14}
\]

With the same causal truncation at both endpoints, this is exactly the
relative reflection gate

\[
 \mathcal C_\varepsilon
 =-2\eta_\varepsilon*\mathcal D_{\rm out}
      (\mathcal O_{1,R}-\mathcal O_{0,R})
 \quad\hbox{on }[0,T].
\tag{0.15}
\]

Equations (0.9) and (0.14)--(0.15) are source-faithful RH criteria.  They
bypass the unproved Boolean adapter `NATCOMP-MOLL106150`, but not the
arithmetic cancellation problem.  The native reflection form is the shortest
exact endpoint criterion; the geodesic form keeps a root-free tangent and its
full companion attached for possible estimates.

## 1. Frozen source identity

The duplicate-`67` native and squared Dirichlet multipliers are

\[
 B_{\rm nat}(z)={1-67^{-z}\over\zeta(z)},
 \qquad
 B_{\rm sq}(z)={1-67^{-2z}\over\zeta(2z)}.
\tag{1.1}
\]

Frozen `L-102602` writes

\[
 H_{\rm nat}=H_{\rm def}+H_{\rm sq}
\tag{1.2}
\]

at the common mother `Phi_*`.  Frozen `L-102707` defines

\[
 \ell_\tau(x)
 =\tau\sqrt{1-x}+(1-\tau)\sqrt{1-x^2},
\tag{1.3}
\]

forms the complete labelled sources `Lambda_tau`, and proves

\[
 \Lambda_0=\lambda^\square,
 \qquad \Lambda_1=\lambda,
 \qquad
 {d\over d\tau}(\Lambda_\tau*\Lambda_\tau)
 =2\dot\Lambda_\tau*\Lambda_\tau.
\tag{1.4}
\]

Frozen `L-102700` supplies the endpoint normalization

\[
 \lambda*\lambda=\beta,
 \qquad
 \lambda^\square*\lambda^\square=\beta^\square.
\tag{1.5}
\]

Since every `G_tau` uses the same kernel `A`, finite-horizon Mellin Fubini
gives

\[
 (2D-1)I_1=H_{\rm nat},
 \qquad
 (2D-1)I_0=H_{\rm sq},
\tag{1.6}
\]

and hence

\[
 H_{\rm def}
 =(2D-1)(I_1-I_0)
 =(2D-1)\int_0^1
   2(\dot G_\tau*_M G_\tau)\,d\tau.
\tag{1.7}
\]

Thus (0.6) is the direct native endpoint identity, while (0.10)--(0.11) are
the same identity split into its squared endpoint and root-free geodesic
difference.  The endpoint order is load-bearing: `tau=0` is squared and
`tau=1` is native, so the difference has the displayed positive sign.  The
tangent has no root coordinate, while the companion `G_tau` carries the unit
coordinate.

Applying constant-coefficient differentials is legitimate distributionally.
The compact kernel identity (0.3), local finiteness of every shifted source,
and the final positive log-box convolution then make (0.6) and (0.11)
equalities of ordinary locally integrable log densities.

No moving Vaughan cutoff, owner reselection, regional absolute value, or
Boolean half-source is introduced.  In particular, the multiplicative gauge
issue isolated by `NATCOMP-MOLL106150` is absent from this path.

## 2. Exact squared-source coefficient and absolute bound

Expanding the second multiplier in (1.1) gives

\[
 {1-67^{-2z}\over\zeta(2z)}
 =\sum_{m\ge1}{\beta(m)\over m^{2z}}.
\tag{2.1}
\]

Since `z=s+1/2`, its term is

\[
 {\beta(m)\over m^{2(s+1/2)}}
 ={\beta(m)\over m}(m^2)^{-s}.
\tag{2.2}
\]

Thus after the extra-notched kernel and mollification, the term at the
physical square `m^2` has coefficient `beta(m)/m`, proving (0.12).

Because `|beta(m)|<=2`, Tonelli and translation invariance of logarithmic
`L1` give, on a finite horizon,

\[
\begin{aligned}
 \|\mathcal Q_\varepsilon\|_{L^1([0,T])}
 &\le
 \sum_{m\le e^{T/2}}{|\beta(m)|\over m}
 \int_0^T|\kappa_\varepsilon(t-2\log m)|\,dt\\
 &\le2\|\kappa_\varepsilon\|_1
       \sum_{m\le e^{T/2}}{1\over m}.
\end{aligned}
\tag{2.3}
\]

The support of `kappa_epsilon` is nonnegative in log coordinate, so no future
source point enters `[0,T]`.  Even without that convention, enlarging the
upper limit by the fixed support ratio changes only the constant.
The elementary bound `H_N<=1+log N` makes (2.3)
`<=2||kappa_epsilon||_1(1+T/2)`.

This direct harmonic estimate is stronger and more portable than invoking a
derivative bound for the old common mother.

## 3. Causal reflection fence and proof of the equivalences

Put `f_tau(u)=G_tau(e^u)`.  The support of `A` in `[1,4]` and the fact that
all source indices are at least one imply that every `f_tau` is causal
(`f_tau(u)=0` for `u<0`) and locally square-integrable.  It need not be in
global `L2`, so no infinite norm is used.

For finite `R`, put `f_(tau,R)=1_[0,R]f_tau`.  If `x<R`, causality confines
the convolution to `0<=u<=x`, and therefore

\[
 i_\tau(x):=I_\tau(e^x)
 =\int_{\mathbb R}f_{\tau,R}(u)f_{\tau,R}(x-u)\,du.
\tag{3.1}
\]

Let `R_x f(u)=f(x-u)` and let `E_x=(I+R_x)/2` and `O_x=(I-R_x)/2`.
For

\[
 \mathcal E_{\tau,R}(x)=\|E_xf_{\tau,R}\|_2^2,
 \quad
 \mathcal O_{\tau,R}(x)=\|O_xf_{\tau,R}\|_2^2,
 \quad
 \mathcal N_{\tau,R}=\|f_{\tau,R}\|_2^2,
\]

the elementary reflection identity gives, on `x<R`,

\[
 i_\tau
 =\mathcal E_{\tau,R}-\mathcal O_{\tau,R}
 =\mathcal N_{\tau,R}-2\mathcal O_{\tau,R}
 =2\mathcal E_{\tau,R}-\mathcal N_{\tau,R}.
\tag{3.2}
\]

The norm term is finite and independent of `x`.  Because
`mathcal D_out` has the factor `D`, (3.2) yields the distributional identity

\[
 \mathcal D_{\rm out}i_\tau
 =-2\mathcal D_{\rm out}\mathcal O_{\tau,R}
 =2\mathcal D_{\rm out}\mathcal E_{\tau,R}
 \qquad(x<R).
\tag{3.3}
\]

The log box is one-sided:
`(eta_epsilon*g)(t)` uses only `g(t-v)` with `0<=v<=epsilon`.  Hence, for
`R>T`, (3.3) proves (0.8) throughout `[0,T]` without seeing the truncation
boundary.  It also proves (0.15), after subtracting the `tau=0` identity from
the `tau=1` identity.  In particular,

\[
\begin{aligned}
 (h_\varepsilon)_-
 &=2\left(\eta_\varepsilon*\mathcal D_{\rm out}
              \mathcal O_{1,R}\right)_+,\\
 (\mathcal C_\varepsilon)_-
 &=2\left(\eta_\varepsilon*\mathcal D_{\rm out}
       (\mathcal O_{1,R}-\mathcal O_{0,R})\right)_+
\end{aligned}
\quad\hbox{a.e. on }[0,T].
\tag{3.4}
\]

The mollified-beta equivalence packet proves

\[
 \mathrm{RH}
 \Longleftrightarrow
 \int_0^T(h_\varepsilon)_-dt=e^{o(T)}.
\tag{3.5}
\]

Equations (3.4)--(3.5) prove the native reflection equivalence (0.9)
directly.  For the geodesic criterion, use the elementary inequality

\[
 |(u+v)_--u_-|\le|v|.
\tag{3.6}
\]

Integrating (3.6), using (0.11) and (0.13), gives

\[
 \left|
  \int_0^T(h_\varepsilon)_-dt
  -\int_0^T(\mathcal C_\varepsilon)_-dt
 \right|
 =O_\varepsilon(1+T).
\tag{3.7}
\]

Since `1+T=e^{o(T)}`, equations (3.5)--(3.7) prove (0.14) in both
directions.  Together with the second line of (3.4), they also show that
`GEO-WKSFSC106150` is exactly a positive-mass bound for the relative
native-versus-squared reflection energy, not merely a sufficient surrogate.

All these logical equivalences are unconditional; none of their equivalent
one-sided estimates, and hence neither RH, is asserted to hold.

## 4. Two exact half-divisor research coordinates

The Boolean half-source programme seeks a finite-depth equal-pair square
`J_U^diamond` with owner allocation and a frozen block cutoff.  Its advantage
is discrete combinatorial structure; its present cost is the missing
native-to-completed additive adapter and terminal semantics.

The shortest native route keeps

```text
native beta source
  -> exact complete labelled half-divisor square lambda*lambda
  -> ordinary Mellin self-convolution of the positive-spline field F_1
  -> causally truncated reflection-odd energy
  -> extra-notched differential
  -> fixed positive mollification.
```

This is the same reflection-signature algebra used by `L-106135` and
`T-106150`, but it is applied directly to the complete native endpoint.  It
imports no Boolean/Wick completion, owner allocation, or Vaughan cutoff.  The
causal cutoff `R>T` is only a finite-`L2` fence: after the factor `D` it has no
effect on the observed horizon.

Its unresolved core is the exact gate

```text
NATREF-MOLL106150:
  for one fixed epsilon>0 and R(T)=T+1,
  the positive logarithmic mass on [0,T] of
  eta_epsilon*D_out O_(1,R(T)) is exp(o(T)).
```

By (0.9), this gate is equivalent to RH.

The geodesic coordinate retains more source structure:

```text
native beta minus squared beta
  -> exact squared/native completion homotopy
  -> root-free tangent x full companion
  -> polarized multiplicative Hankel current
  -> relative native-minus-squared reflection energy
  -> extra-notched differential and fixed positive mollification.
```

Its unresolved core is likewise exact:

```text
GEO-WKSFSC106150:
  for one fixed epsilon>0, the positive logarithmic mass on [0,T] of
  eta_epsilon*D_out(O_(1,R(T))-O_(0,R(T))) is exp(o(T)).
```

By (3.4), this is precisely the negative-mass gate for `C_epsilon`; by
(0.13), the squared endpoint changes logarithmic absolute mass by only
`O_epsilon(1+T)`.  Thus the native and relative reflection gates are
equivalent at subpower scale.

Frozen `L-102708` already proves polylogarithmic labelled source/tangent
energies and a subpower same-product convolution energy, uniformly in `tau`.
It does **not** control the distinct-product physical overlap or orient the
polarized current.  Those are the two load-bearing targets for a future proof
of `GEO-WKSFSC106150`.

## 5. Proof ledger

Proved exactly:

- `K_ext=P(D)Phi_*`;
- `h_epsilon=eta_epsilon*D_out(F_1*_M F_1)` from `lambda*lambda=beta`;
- the causal finite-`L2` reflection identity (0.8) and its cutoff
  independence on the observed horizon;
- the source-exact geodesic/squared decomposition (0.10)--(0.12);
- the unconditional `O_epsilon(T)` squared-source `L1` bound;
- the exact relative reflection identity (0.15);
- equivalence of the native reflection, geodesic, and complete mollified
  one-sided gates;
- the unconditional logical equivalences (0.9) and (0.14), while no
  equivalent one-sided estimate is asserted true here.

Imported frozen theorem:

- the complete half-divisor square, continuous geodesic identities
  (1.4)--(1.7), and uniform labelled/same-product energy bounds.

Not proved:

- `NATREF-MOLL106150`;
- `GEO-WKSFSC106150`;
- distinct-product cross-owner cancellation or a sign orientation;
- `NATCOMP-MOLL106150`, the Boolean completed-source adapter;
- RH or GRH.

## 6. Bounded replay

```text
python -B research/l-families/atlas/function_field/ffps_mollified_geodesic_rh_criterion.py --check
python -B -O research/l-families/atlas/function_field/ffps_mollified_geodesic_rh_criterion.py --check
python -B -m unittest tests.test_ffps_mollified_geodesic_rh_criterion
python -B -O -m unittest tests.test_ffps_mollified_geodesic_rh_criterion
```

The replay authenticates the frozen source identities and checks only exact
coefficient, differential, harmonic, and implication ledgers.  It enumerates
no conductor, prime interval, curve, point, or zeta zero.
