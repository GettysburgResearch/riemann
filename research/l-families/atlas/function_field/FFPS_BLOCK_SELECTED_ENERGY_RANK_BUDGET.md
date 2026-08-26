# The block selected-energy rank budget is quadratic, not linear

Status: **exact cohomological dimension ledger for the path model; no native
FFPS moment estimate, RH, or GRH claim**

Exact replay:
[`ffps_block_selected_energy_rank_budget.py`](ffps_block_selected_energy_rank_budget.py).

## 0. Outcome

The endpoint-disjoint path construction gives a linear average first Betti
number across its `2^r-1` selected modes.  The block interferometer, however,
contains the **energies** `|H_chi|^2`.  Their natural tensor rank is the square
of the first Betti number.

For a mode indexed by a nonempty subset `S subset {1,...,r}`, with all
endpoint places of degree `e`, the maximally extended Kummer line has

\[
 b_S=\dim H_c^1=2e|S|-2.
\tag{0.1}
\]

The exact averages are

\[
 \boxed{
 {1\over2^r-1}\sum_{S\ne\varnothing}b_S
 ={2er2^{r-1}-2(2^r-1)\over2^r-1},}
\tag{0.2}
\]

and

\[
 \boxed{
 {1\over2^r-1}\sum_{S\ne\varnothing}b_S^2
 ={2^r\big(e^2r(r+1)-4er+4\big)-4\over2^r-1}.}
\tag{0.3}
\]

Thus

\[
 \overline b\sim er-2,
 \qquad
 \overline{b^2}
 =e^2r^2+(e^2-4e)r+4+O(2^{-r}).
\tag{0.4}
\]

The good news is that normalization removes the exponential mode count.  The
bad news is that the relevant second-moment complexity is quadratic in the
number of blocks, not linear.

## 1. Why the square is the relevant rank

Suppose a selected trace has the cohomological form

\[
 H_\chi=-\operatorname{Tr}(F_q\mid V_\chi),
 \qquad \dim V_\chi=b_\chi,
\]

with `V_chi` pure of weight one after the usual compact-support conventions.
Then `|H_chi|^2` is represented, after choosing the matching dual/conjugate
realization, on

\[
 V_\chi\otimes\overline{V_\chi},
\]

whose dimension is `b_chi^2` and whose weight is two.  Equivalently, the
elementary Deligne bound already shows the same budget:

\[
 |H_\chi|\le b_\chi q^{1/2}
 \quad\Longrightarrow\quad
 |H_\chi|^2\le b_\chi^2q.
\tag{1.1}
\]

Therefore the selected average in the interferometer has the separate-bound
scale

\[
 {1\over2^r-1}\sum_{\chi\ne1}|H_\chi|^2
 \le q\,\overline{b^2},
\tag{1.2}
\]

not `q^(1/2)*overline b`.  The exact Artin--Schreier/Kummer weight-barrier
packet shows that this weight-two scale can be attained even when every
selected line is nonconstant and the off-coset kernel is atom-free.

## 2. Exact derivation

Use the binomial identities

\[
 \sum_{k=1}^r k{r\choose k}=r2^{r-1},
 \qquad
 \sum_{k=1}^r k^2{r\choose k}=r(r+1)2^{r-2}.
\]

Then

\[
 \begin{aligned}
 \sum_{S\ne\varnothing}b_S^2
 &=\sum_{k=1}^r{r\choose k}(2ek-2)^2\\
 &=2^r\big(e^2r(r+1)-4er+4\big)-4,
 \end{aligned}
\]

which proves (0.3).  The subtraction of four is the omitted empty subset,
whose formal value `(2e*0-2)^2` would be four.

## 3. What remains genuinely promising

Quadratic rather than exponential growth still leaves room for a useful
architecture.  The exact hierarchy is now:

\[
 \begin{array}{c|c}
 \text{number of selected modes} & 2^r-1\\
 \text{normalized first-moment rank} & \asymp er\\
 \text{normalized selected-energy rank} & \asymp e^2r^2\\
 \text{cohomological weight of selected energy} & 2
 \end{array}
\tag{3.1}
\]

To beat this separate energy bound, one must preserve the signed cancellation
between the off-coset interferometer and selected average.  The positivity
firewall proves that no atom-free PSD quadratic replacement can do so.  A
higher-order collision-free moment is another possible route, but it requires
delocalization.

## 4. Maximal-extension firewall remains

Formula (0.3) uses each mode's maximal lisse open.  The block packet proves
that the common source open has additional removable-puncture cost.  Squaring
the ranks does not legalize mode-dependent extension.  Before applying (1.2)
to a native source, one still needs either:

- exact boundary corrections allowing each selected mode to use its maximal
  extension; or
- a recomputation with the common-open Betti number for every mode.

This note corrects the rank scale; it does not cross the source-extension
gate.

## 5. Proof ledger

Proved exactly:

- the total and average first-rank formula (0.2);
- the total and average tensor-rank formula (0.3);
- quadratic growth (0.4).

Imported with explicit scope:

- the path-mode Betti formula (0.1);
- purity/Deligne as the interpretation of the separate-bound scale.

Not proved:

- that every `|H_chi|^2` is realized on one common native FFPS sheaf;
- a signed joint estimate better than (1.2);
- boundary-extension legality, principal individualization, RH, or GRH.

## 6. Bounded replay

Run:

```text
python -B research/l-families/atlas/function_field/ffps_block_selected_energy_rank_budget.py --check
python -B -O research/l-families/atlas/function_field/ffps_block_selected_energy_rank_budget.py --check
python -B -m unittest tests.test_ffps_block_selected_energy_rank_budget
python -B -O -m unittest tests.test_ffps_block_selected_energy_rank_budget
```

The replay evaluates closed binomial sums for at most twelve blocks and place
degree five.  It enumerates no subsets, conductors, curves, or points.
