# The growing closed-place supply tax

Status: **exact squarefree-polynomial large-deviation bound and a conditional
modewise-conductor firewall; no universal relative complex, signed family
estimate, RH, or GRH**

Bounded exponent replay:
[`function_field_closed_place_supply_tax.py`](function_field_closed_place_supply_tax.py).

## 0. Outcome

The scalable closed-place tower has enough eligible factors, but those
factors do not remain low-degree as the block rank grows.

Let `F` be uniformly distributed among monic squarefree degree-`n`
polynomials over `F_q`.  Let `E` be the eligible closed places:

\[
 \delta=
 \begin{cases}
 1,&q\equiv1\pmod4,\\
 1/2,&q\equiv3\pmod4.
 \end{cases}
\]

Write `Omega_E(F;D)` for the number of eligible irreducible factors of `F`
having degree at most `D`.  For

\[
 r=\lfloor\alpha\log n\rfloor,
 \qquad D=\lfloor n^\beta\rfloor,
 \qquad0<\beta<{\alpha\over\delta},
\]

there is the exact exponent bound

\[
 \boxed{
 \Pr(\Omega_E(F;D)\ge r)
 \le n^{-J_\delta(\alpha,\beta)+o(1)},}
\tag{0.1}
\]

where

\[
 \boxed{
 J_\delta(\alpha,\beta)
 =\alpha\log{\alpha\over\delta\beta}
  -\alpha+\delta\beta>0.}
\tag{0.2}

Consequently, in the logarithmic high-probability sense made precise in
Section 2, **every** selection of `r` eligible factors contains a place of
degree at least

\[
 \boxed{n^{\alpha/\delta-o(1)}.}
\tag{0.3}

The formal block leverage is only

\[
 n^{-\alpha\log(5/4)+o(1)}.
\]

Since

\[
 {\alpha/\delta\over\alpha\log(5/4)}
 ={1\over\delta\log(5/4)}
 =\begin{cases}
 4.4814\ldots,&\delta=1,\\
 8.9628\ldots,&\delta=1/2,
 \end{cases}
\tag{0.4}

the first obvious modewise conductor cost is vastly larger than the leverage
gain.

This is a serious firewall, not a death sentence.  It rules out importing the
fixed-equal-degree `O(r^2)` Betti story into the native growing-place tower.
It does **not** rule out a relative hard-minus-selected complex whose common
large-degree contributions cancel before a conductor bound is applied.

## 1. A direct moment bound

For `s>=1`, expand

\[
 s^{\Omega_E(F;D)}
 =\prod_{\substack{P\mid F\\P\in E,\ \deg P\le D}}
   (1+(s-1)).
\]

After expansion over squarefree products `A` of eligible short places,

\[
 \mathbb E[s^{\Omega_E(F;D)}]
 =\sum_A(s-1)^{\omega(A)}\Pr(A\mid F).
\tag{1.1}
\]

If `a=deg A<=n`, the number of squarefree degree-`n` multiples of `A` is at
most `q^(n-a)`, while the total squarefree family has
`q^n-q^(n-1)` members.  Thus

\[
 \Pr(A\mid F)\le {1\over1-q^{-1}}|A|^{-1}.
\tag{1.2}

The constant in (1.2) occurs once, not once per prime.  Positivity now gives

\[
\begin{aligned}
 \mathbb E[s^{\Omega_E(F;D)}]
 &\le {1\over1-q^{-1}}
 \prod_{\substack{P\in E\\\deg P\le D}}
 \left(1+{s-1\over|P|}\right)\\
 &\ll_{q,s}
 \exp\left((s-1)
   \sum_{\substack{P\in E\\\deg P\le D}}|P|^{-1}\right)\\
 &\ll_{q,s}D^{\delta(s-1)}.
\end{aligned}
\tag{1.3}
\]

The last step uses

\[
 \sum_{\substack{P\in E\\\deg P\le D}}|P|^{-1}
 =\delta\log D+O_q(1),
\tag{1.4}

which follows directly from the prime-polynomial theorem and the parity
description of eligible degrees.

Markov's inequality gives

\[
 \Pr(\Omega_E(F;D)\ge r)
 \le s^{-r}D^{\delta(s-1)+o(1)}.
\]

With `r=alpha log n`, `D=n^beta`, optimize at

\[
 s={\alpha\over\delta\beta}>1.
\]

This proves (0.1)--(0.2) without enumerating a polynomial or invoking a
central limit theorem.

## 2. The order-statistic consequence

Fix any `epsilon>0` and take

\[
 \beta={\alpha\over\delta}-\epsilon.
\]

Equation (0.1) says the probability of finding `r` eligible factors below
`n^beta` tends to zero by a power of `n`.  Therefore the `r`-th smallest
eligible factor degree exceeds `n^beta` with probability tending to one.
Equivalently,

\[
 {\log d_{(r)}(F)\over\log n}\ge {\alpha\over\delta}-o_{\Pr}(1).
\tag{2.1}
\]

This is the meaning of (0.3).  It is not a deterministic `o(1)` valid for
every polynomial, and the fixed-`epsilon` estimate alone is not being claimed
uniform as `epsilon` varies with `n`.

For two independently sampled cores, the union bound gives the same
conclusion on both sides.  The probability that two squarefree degree-`n`
cores are coprime is bounded below by a positive `q`-dependent constant
(equivalently, its local exclusion product converges to a nonzero Euler
product).  Dividing the union-bound failure probability by this constant
proves that conditioning on coprimality does not alter the power exponent.

This statement concerns random squarefree polynomial cores.  Transferring it
to the weighted Boolean FFPS source remains a separate source theorem.

## 3. Conditional conductor firewall

Suppose a modewise curve realization retains an eligible degree-`d` place as
a genuinely nontrivial tame Kummer branch.  After geometric base change that
place contributes `d` geometric branch points, so its arithmetic conductor
degree is at least linear in `d`; the corresponding separate rank-one curve
cohomology has the same linear scale.  This statement is not a lower bound
for a virtual or relative complex in which those local branches cancel.

If a rank-`r` block system uses a place of degree `D`, then half of its
`2^r-1` nonprincipal block characters contain that block:

\[
 {2^{r-1}\over2^r-1}>{1\over2}.
\]

Thus the normalized separate-mode conductor average is at least of order
`D`, unless an exact geometric cancellation removes that branch before the
individual mode is formed.  Combining with (0.3) gives the conditional lower
scale

\[
 n^{\alpha/\delta-o(1)}.
\tag{3.1}

This proves the comparison (0.4) for every architecture that:

1. estimates selected modes separately;
2. pays conductor at least linearly in each retained branch degree; and
3. does not cancel the large-degree branch in a common relative complex.

It is not a universal lower bound for arbitrary derived pushforwards.  A
relative projector can identify and cancel matching hard/selected
constituents before applying Deligne.  That possibility is now the main
reason to pursue relative sheafification rather than `CYSEL` mode by mode.

More generally, suppose the normalized trace theorem loses a power `D^theta`
of the largest selected place degree.  Equations (0.3) and the leverage scale
show that a net gain requires

\[
 \theta{\alpha\over\delta}
 <\alpha\log(5/4),
 \qquad\text{hence}\qquad
 \boxed{\theta<\delta\log(5/4).}
\tag{3.2}
\]

Numerically the admissible conductor exponent is below `0.223144` when
`q=1 mod 4`, and below `0.111572` when `q=3 mod 4`.  Even a hypothetical
square-root dependence `D^(1/2)` is too expensive.  A successful growing-rank
route therefore needs near-complete conductor cancellation, not merely a
routine improvement of a linear Betti estimate.

## 4. Architectural consequences

Three scales must now be tracked together:

\[
\begin{array}{c|c}
\text{quantity}&\text{scale at }r=\alpha\log n\\ \hline
\text{poor-core probability}&n^{-c_\delta(\alpha)+o(1)}\\
\text{formal leverage}&n^{-\alpha\log(5/4)+o(1)}\\
\text{typical r-th place degree}&n^{\alpha/\delta+o(1)}.
\end{array}
\tag{4.1}

The third scale dominates a separate Betti budget.  Therefore a useful
growing-rank theorem needs at least one new mechanism:

- a relative hard-minus-selected class cancelling the high-degree branches;
- a global trace estimate whose conductor dependence is sublinear in the
  largest selected degree;
- a source design using many quotient coordinates without requiring distinct
  large-degree factors;
- or a multiscale argument in which only bounded rank is used at each degree
  shell and gains accumulate coherently.

The last option is particularly interesting: it replaces one rank
`alpha log n` mask by a sequence of bounded-rank masks across logarithmic
degree bands.  Whether the principal source survives that iteration is open.

## 5. Proof ledger

Proved exactly from elementary counting and the prime-polynomial theorem:

- the truncated exponential-moment bound (1.3);
- the upper-tail rate (0.1)--(0.2);
- the high-probability factor-degree lower bound (0.3);
- the exponent comparison (0.4).

Conditional geometric consequence:

- the separate-mode conductor firewall (3.1), under the three stated
  modewise branch hypotheses.

Not proved:

- transfer of the random-core law to the weighted FFPS source;
- a universal conductor lower bound for relative complexes;
- a multiscale bounded-rank amplifier;
- the signed trace estimate, principal theorem, RH, or GRH.

## 6. Bounded replay

```text
python -B research/l-families/atlas/function_field/function_field_closed_place_supply_tax.py --check
python -B -O research/l-families/atlas/function_field/function_field_closed_place_supply_tax.py --check
python -B -m unittest tests.test_function_field_closed_place_supply_tax
python -B -O -m unittest tests.test_function_field_closed_place_supply_tax
```

The replay evaluates six scalar exponent panels.  It enumerates no
polynomial, closed place, curve, or point.
