# The extra-notched current has a bounded global anti-causal inverse

Status: **exact global one-sided inversion theorem; the later complete-beta
atomic firewall refutes its raw-complete Jordan application; moving-source
terminal compatibility and the parent native-source binding remain open; RH
unproved**

Bounded exact replay:
[`ffps_anticausal_outer_inversion_gate.py`](ffps_anticausal_outer_inversion_gate.py).

Frozen interfaces: PR #719 scientific head
`ec6635b4c7dcd08fe433b7ae7e1d9a8c9495dfcc`, specifically the zero-moment
`L-102880`, stable-image `L-102885`, and `T-102990`; and corrected source
commit `98af0db6ec7f77d6333a77a3dac53c4698852f43`, specifically `L-102500`,
`L-102701`, `L-102740`, `L-106134`, and `T-106150`.  The replay locks the
exact blobs because two different files carry the claim number `L-102880` at
the first commit.

## 0. Outcome

The naive causal inverse of the missing dyadic notch loses a square root, but
that is not the correct inverse geometry for a compact current.  From the
future endpoint, the inverse is a geometrically decaying anti-causal series.

There are in fact three kernels in the frozen chain.  With

\[
q(s)=1-\sqrt2\,2^{-s},
\qquad r(s)=1-2^{-s},
\]

their Mellin multipliers are

\[
\widehat K_{\rm nat}(s)
={4q(s)r(s)^2(s-1)\over s(s-1/2)},
\tag{0.1}
\]

from the explicit piecewise `K_L` in `L-102880`,

\[
\widehat K_{740}(s)
={q(s)r(s)^2(s-1)(5s+3/2)\over s(s-1/2)},
\tag{0.2}
\]

from differentiating the construction printed in `L-102740`, and

\[
\widehat K_{\rm ext}(s)
={q(s)^2r(s)^2(s-1)(5s+3/2)\over s(s-1/2)},
\tag{0.3}
\]

from the common-mother self-convolution.

Thus

\[
\boxed{
K_{\rm ext}=QTK_{\rm nat},
\qquad
Q=I-\sqrt2S_2,
\qquad
T={5D+3/2\over4}.}
\tag{0.4}
\]

For a fixed finite source, put `f=K_nat*sigma`, `h=Tf`, and `g=Qh`.  These
are the native, intermediate, and extra-notched currents.  Their total
logarithmic masses vanish, and both factors have one-sided bounded inverses:

\[
\boxed{
\|(K_{\rm nat}*\sigma)_-\|_{L^1}
\le {8\over3}(1+\sqrt2)
\|(K_{\rm ext}*\sigma)_-\|_{\rm TV}.}
\tag{0.5}
\]

The unresolved issue is not analytic inversion.  It is that the frozen FFPS
source and cutoff move with the horizon.  The anti-causal inverse reads a
future terminal shell.  One must prove that the same frozen source is
controlled on its entire constant-factor future support before replacing the
extra-notched premise by the native parent premise.

There is now also a decisive complete-source fence.  The later
`FFPS_COMPLETE_BETA_ATOMIC_VARIATION_FIREWALL.md` proves that the raw complete
duplicate-`67` beta current has Jordan negative variation
`Omega(sqrt(Y))`.  Thus (0.5) remains an exact fixed/live-source operator
theorem, but it is **not** a viable raw-complete beta route to RH.  A viable
complete-source use would have to mollify before taking the Jordan part; the
resulting negative-mass estimate is RH-equivalent and is not proved here.

There is a separate source-binding issue.  The multiplier identities prove a
same-source transfer to the explicit `K_nat` of the zero-moment `L-102880`.
Because the frozen `L-102885` instead calls the different common-mother object
`K_L`, a conclusion-facing use must still bind `BCI102990` to that explicit
native kernel and the same live source.  This packet calls that finite parent
audit `NATBIND106150` and does not declare it proved.

## 1. The three-way multiplier audit

The transform of the explicit piecewise kernel in `L-102880.2` is obtained by
integrating the constant and square-root pieces on `[1,2]`, `[2,4]`, and
`[4,8]`.  The constant terms combine to

\[
{8q(s)r(s)^2\over s},
\]

and the square-root terms combine to

\[
-{4q(s)r(s)^2\over s-1/2}.
\]

Their sum is (0.1).  On the other hand, the bracket in `L-102740` is

\[
5-{s+3/2\over s(s-1/2)}
={(s-1)(5s+3/2)\over s(s-1/2)}.
\]

After its final derivative this gives (0.2).  Finally `L-102500/L-102701`
contribute the second factor of `q`, giving (0.3).  In particular, the
common-mother multiplier assigned to the name `K_L` in the frozen `L-102885`
is (0.3), not the explicit piecewise multiplier (0.1).

Therefore the common-mother object is not merely one notch away from the
explicit native kernel: it also contains the stable first-order factor `T`.
The naming in `L-102740`, `L-102885`, and `L-106134` conflates these three
objects.

## 2. Bounded anti-causal inversion of the notch

In logarithmic coordinate `u`, write

\[
g=Qh,
\qquad
g(u)=h(u)-\sqrt2h(u-\log2).
\tag{2.1}
\]

Solving from the future gives

\[
\boxed{
h(u)=-\sum_{j\ge1}2^{-j/2}g(u+j\log2).}
\tag{2.2}
\]

For compact functions the sum is pointwise finite.  For finite signed
measures it converges absolutely in total variation.  Its coefficient mass is

\[
\sum_{j\ge1}2^{-j/2}=1+\sqrt2.
\tag{2.3}
\]

The minus sign means that `h_-` is controlled by `g_+`, not directly by
`g_-`.  Since `K_nat=D R_nat` with compact `R_nat`, `int f=0`.  Consequently
`int h=(3/8)int f=0`, and

\[
\int g=(1-\sqrt2)\int h=0,
\]

their positive and negative variations agree.  Hence

\[
\boxed{
\|h_-\|_{\rm TV}
\le(1+\sqrt2)\|g_+\|_{\rm TV}
=(1+\sqrt2)\|g_-\|_{\rm TV}.}
\tag{2.4}
\]

Here all three norms in (2.4) mean the masses of the corresponding Jordan
parts, equivalently their total-variation norms.  Thus the argument includes
the dyadic atoms of `K_ext`.

## 3. Positive inversion of the first-order factor

Write

\[
T={5\over4}(D+3/10).
\]

The zero-extended causal inverse is positive:

\[
f(u)={4\over5}
\int_{-\infty}^{u}e^{-3(u-v)/10}h(v)dv.
\tag{3.1}
\]

Its logarithmic `L1` norm is

\[
{4\over5}{10\over3}={8\over3}.
\tag{3.2}
\]

Thus

\[
\|f_-\|_{L^1}\le{8\over3}\|h_-\|_{\rm TV}.
\tag{3.3}
\]

Combining (2.4) and (3.3) proves (0.5).

## 4. The exact terminal gate

For a single globally compact fixed source, (0.5) solves the inversion
problem.  The FFPS theorem is indexed by a horizon `Y`, with cutoff
`U=floor(Y^(1/6))`.  Formula (2.2) may evaluate `g` at scales larger than the
observation point, while applying the stated theorem at a larger horizon may
change `U` and therefore change the source.

Define

```text
TERMFUT106150:
  for the source frozen at horizon Y and cutoff U(Y), the same live
  extra-notched current has its complete support in [1,CY] for one fixed C,
  and its Jordan negative variation on [1,CY] is Y^o(1).
```

Only a constant number of dyadic shells lie beyond the original horizon `Y`;
the full coefficient series remains bounded by (2.3).  Thus (0.5) gives the
same-source native live-current premise.  At the exact kernel level,

\[
\boxed{
\text{Jordan-WKSFSC}_{106150}
\ \text{and}\ \mathrm{TERMFUT}_{106150}
\Longrightarrow
\text{the explicit-}K_{\rm nat}\text{ live negative-mass premise}.}
\tag{4.1}
\]

The conclusion-facing arrow is conditional on the still-open parent binding:

\[
\boxed{
\text{Jordan-WKSFSC}_{106150}
\wedge\mathrm{TERMFUT}_{106150}
\wedge\mathrm{NATBIND}_{106150}
\Longrightarrow\mathrm{BCI}_{102990}
\Longrightarrow\mathrm{RH}.}
\tag{4.2}
\]

Equations (4.1)--(4.2) retain the historical frozen live-source implication.
They must not be read as asserting a raw complete-beta premise: that distinct
premise is refuted by the atomic firewall.  Nor does this packet prove that
the live `WKSFSC106150` source can be completed by `EXTSRC106150`; the two raw
premises cannot jointly yield a subpower complete current in view of the
square-root lower bound.

If the original `WKSFSC` quantifier already controls the complete support of
each fixed source, `TERMFUT106150` is bookkeeping and should be discharged by
an exact support lemma.  If its horizon quantifier changes the source before
the terminal shell is reached, the gate is real.

## 5. Relation to the direct extra-notched consumer

`FFPS_EXTRA_NOTCHED_MELLIN_LANDAU_CONSUMER.md` gives a second repair route
which never returns to `K_nat`.  It instead needs the complete-source adapter
`EXTSRC106150`.  Historically, the two proposed tasks were complementary:

```text
native route:  prove TERMFUT106150 and use bounded anti-causal inversion;
direct route:  prove EXTSRC106150 and use the extra-notched Landau consumer.
```

The direct **raw-Jordan** route is now retired.  `EXTSRC106150` remains a
source-accounting question, but only its fixed-mollified replacement can feed
a viable complete-current criterion, and `MEXTSRC106150/NATCOMP-MOLL106150`
are not proved.

The native route also needs the finite `NATBIND106150` source/kernel audit
before invoking `BCI102990`.  Neither route needs the power-lossy causal
inverse.

## 6. Proof ledger

Proved exactly:

- all three multipliers (0.1)--(0.3);
- the factorization (0.4);
- the anti-causal inverse and coefficient mass `1+sqrt(2)`;
- the zero-mass one-sided conversion;
- the positive stable inverse and constant `8/3`;
- the global bound (0.5).

Still open:

- terminal compatibility for the moving source/cutoff;
- whether the original horizon convention already implies `TERMFUT106150`;
- `NATBIND106150`, the exact parent binding to the explicit native kernel and
  same live source;
- `EXTSRC106150` and live-source `WKSFSC106150` as separate source gates;
- a fixed-mollified complete-source replacement (`MEXTSRC106150` and
  `NATCOMP-MOLL106150`), BCI, RH, and GRH.

Refuted by the later complete-source atomic firewall:

- raw complete-beta Jordan negative variation `Y^o(1)`; it grows at least
  like `sqrt(Y)`.  This does not by itself refute the differently scoped live
  source in (4.1), but it blocks promoting (4.1) through a raw-complete
  adapter.

## 7. Bounded replay

```text
python -B research/l-families/atlas/function_field/ffps_anticausal_outer_inversion_gate.py --check
python -B -O research/l-families/atlas/function_field/ffps_anticausal_outer_inversion_gate.py --check
python -B -m unittest tests.test_ffps_anticausal_outer_inversion_gate
python -B -O -m unittest tests.test_ffps_anticausal_outer_inversion_gate
```

The replay authenticates the eight frozen source blobs and uses exact
arithmetic in `Q(sqrt(2))` through dyadic depth `32`.  It enumerates no source
atom, conductor, curve, or point.
