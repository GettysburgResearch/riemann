# T100200 — Exact critical-activation compression of FEAG99980

**Scientific status:** unconditional structural advance; `PATG100200`, `FEAG99980`, and RH remain unproved.

## 1. Finite labelled packet

Let `B` be a finite labelled multiset with labels `q>=2`; repeated labels are allowed. For `A subset B`, put

\[
P_A=\prod_{q\in A}q,\qquad \epsilon_A=(-1)^{|A|}.
\]

Define

\[
\Delta_B=\prod_{q\in B}(1-q^{-3/2})
\]

and

\[
f(y)=\begin{cases}16,&0<y<1,\\24y^{-1/2}-9y^{-1},&y\ge1.\end{cases}
\]

The quadratic-envelope packet is

\[
\mathcal E_B(y)=\sum_{A\subseteq B}\epsilon_AP_A^{-3/2}f(y/P_A).
\tag{1}
\]

For `x>=1`, define the active moments

\[
S_\sigma(x)=\sum_{P_A\le x}\epsilon_AP_A^{-\sigma},\qquad
\sigma\in\{1/2,1,3/2\},
\]

and the inactive tail

\[
\overline S_{3/2}(x)=\Delta_B-S_{3/2}(x).
\]

## 2. Exact cell formula

Between consecutive labelled subset products the active set is fixed. On such a cell,

\[
\boxed{
\mathcal E_B(y)=16\overline S_{3/2}+24y^{-1/2}S_1-9y^{-1}S_{1/2}.
}
\tag{2}
\]

No subset expansion remains after these three moments are known.

Put

\[
\mathcal H_B(y)=4\sqrt y\,S_1-3S_{1/2}.
\]

Then on the open cell,

\[
\boxed{
\mathcal E_B'(y)=-3y^{-2}\mathcal H_B(y),\qquad
\mathcal H_B'(y)=2y^{-1/2}S_1.
}
\tag{3}
\]

Thus the quadratic envelope and the critical linear SHARP state form one exact stop-loss pair.

## 3. Complete classification of cell minima

If `S_1>0`, then `H_B` is increasing; any interior zero changes `E_B'` from positive to negative and is a local maximum.

If `S_1=0`, the envelope is monotone or constant.

If `S_1<0` but `S_{1/2}>=0`, then `H_B<0`, hence the envelope is increasing.

Therefore an interior minimum can occur only when

\[
S_1<0,\qquad S_{1/2}<0.
\tag{4}
\]

In that sector the unique candidate is

\[
\boxed{y_*=\left(\frac{3S_{1/2}}{4S_1}\right)^2.}
\tag{5}
\]

It matters only when it lies inside the current activation cell. Substitution gives

\[
\boxed{
\mathcal E_B(y_*)=16\left(\overline S_{3/2}+\frac{S_1^2}{S_{1/2}}\right).
}
\tag{6}
\]

Since `S_{1/2}<0`, positivity at the critical point is equivalent to the Turán inequality

\[
\boxed{S_1^2+\overline S_{3/2}S_{1/2}\le0.}
\tag{7}
\]

## 4. Exact activation-jump ledger

Let

\[
b_B(d)=\sum_{A:P_A=d}\epsilon_A.
\]

The kernel jump is `f(1)-f(1-)=-1`, hence at an activation product `d`,

\[
\boxed{
\mathcal E_B(d)-\mathcal E_B(d^-)=-b_B(d)d^{-3/2}.
}
\tag{8}
\]

Only `b_B(d)>0` can create a new downward endpoint minimum.

Consequently, for a finite labelled source, global nonnegativity is equivalent to two finite witness classes:

1. nonnegativity immediately after every activation with `b_B(d)>0`;
2. nonnegativity at every double-negative critical point (5) lying in its cell.

All other points are dominated by one of these witnesses.

## 5. Infinite prime source and PATG100200

For one label for every prime and a second label `67`, the exponent-`3/2` product is absolutely convergent:

\[
\Delta_\infty=\frac{1-67^{-3/2}}{\zeta(3/2)}.
\]

At each finite `y`, the active moments are finite and the inactive tail is the absolutely convergent complement. Thus the same witness classes are exactly the all-scale content of `FEAG99980`.

Define `PATG100200` as:

1. every positive-parity prime activation leaves `E(d)>=0`;
2. every actual-prime double-negative cell whose `y_*` lies inside the cell satisfies (7).

Then

\[
\boxed{PATG100200\Longleftrightarrow FEAG99980\Longrightarrow RH.}
\tag{9}
\]

The first equivalence is exact, not asymptotic.

## 6. Generic total positivity is false

Take the rational labels

\[
B=\left\{2,\frac{21}{10},\frac{11}{5},\frac{23}{10},\frac{12}{5},\frac52,3,27\right\}.
\]

As `y->2-`, every nonempty shifted argument is below activation, so

\[
\mathcal E_B(2^-)=12\sqrt2-\frac92+16\left[\prod_{q\in B}(1-q^{-3/2})-1\right].
\]

Outward 100-decimal evaluation yields

\[
-2.02518<\mathcal E_B(2^-)<-2.02516.
\]

Therefore the envelope kernel is not a completely monotone multiplicative spline. One- and two-prime positivity plus fully coactive positivity do not imply all mixed-activation positivity for arbitrary shifts. The actual proof must visibly use prime spacing and the exact inactive prime tail.

## 7. Exact frontier

```text
quadratic SHARP positivity                 inherited proved
one-/two-prime activation                  inherited proved
fully coactive blocks                      inherited proved
three-moment cell formula                  proved exact
complete cell-minimum classification       proved exact
activation-jump ledger                     proved exact
generic mixed-shift positivity             refuted
PATG100200 actual-prime activation gate     open
FEAG99980                                  open
Riemann Hypothesis                         unproved
```
