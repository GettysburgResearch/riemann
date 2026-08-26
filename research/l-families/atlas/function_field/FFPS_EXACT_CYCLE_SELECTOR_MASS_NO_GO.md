# Exact cycle selectors have forced exponential mass

Status: **exact characteristic-zero representation-theoretic no-go for the
full `S_d` cycle selector; no native FFPS source adapter, trace estimate,
individualization, RH, or GRH claim**

Bounded exact replay:
[`ffps_exact_cycle_selector_mass_no_go.py`](ffps_exact_cycle_selector_mass_no_go.py).
Canonical summary:
[`ffps_exact_cycle_selector_mass_no_go.json`](ffps_exact_cycle_selector_mass_no_go.json).

This packet starts from the universal root-incidence cancellation in
`FFPS_RELATIVE_BOUNDARY_TRACE_TOWER_GATE.md`.  That packet left open whether
the exterior-power presentation of the exact irreducibility selector could be
replaced by a lower-complexity characteristic-zero realization.  In the full
`S_d` character category, it cannot.

## 0. Outcome

Let `C_d` be the conjugacy class of `d`-cycles in `S_d`, and let

\[
 q_d=1_{C_d}
\]

be its indicator as a class function.  For `0<=k<=d-1`, write

\[
 H_k=(d-k,1^k).
\]

Then character orthogonality and the Murnaghan--Nakayama rule give the
**unique** irreducible-character expansion

\[
 \boxed{
 q_d={1\over d}\sum_{k=0}^{d-1}(-1)^k\chi_{H_k}.}
\tag{0.1}
\]

Since

\[
 \dim H_k={d-1\choose k},
\tag{0.2}
\]

the absolute rank mass of every class in the rationalized representation
ring `R(S_d) tensor Q` with trace exactly `q_d` is forced to be

\[
 \boxed{
 \|q_d\|_{\rm rank}
 ={1\over d}\sum_{k=0}^{d-1}{d-1\choose k}
 ={2^{d-1}\over d}.}
\tag{0.3}
\]

For `d>1`, its positive and negative rank masses are separately forced:

\[
 \boxed{
 \|q_d\|_+=\|q_d\|_-={2^{d-2}\over d}.}
\tag{0.4}
\]

Equivalently, the integral numerator `d q_d` has minimal positive and
negative ranks `2^(d-2)` and minimal total cohomology rank `2^(d-1)`.
Placing the even hooks in even degree and the odd hooks in odd degree attains
the bound.  Any bounded complex of characteristic-zero semisimple
`S_d`-representations with Euler trace `d q_d` has at least those ranks in
the two parities.

Thus the exterior presentation was not merely an expensive first attempt.
It is rank-optimal, and its exponential cost is intrinsic to an **exact
full-monodromy selector**.

## 1. Why the expansion is forced

Irreducible characters form an orthonormal basis of class functions on
`S_d`.  If

\[
 q_d=\sum_{\lambda\vdash d}a_\lambda\chi_\lambda,
\]

then

\[
 a_\lambda
 =\langle q_d,\chi_\lambda\rangle
 ={|C_d|\over|S_d|}\chi_\lambda((d))
 ={1\over d}\chi_\lambda((d)).
\tag{1.1}
\]

The Murnaghan--Nakayama rule removes a rim hook of length `d`.  A Young
diagram of size `d` is itself such a border strip exactly when it is a hook
`H_k`; the sign is `(-1)^k`.  Therefore

\[
 \chi_\lambda((d))=
 \begin{cases}
  (-1)^k,&\lambda=H_k,\\
  0,&\text{otherwise},
 \end{cases}
\tag{1.2}
\]

which proves (0.1).  The hook-length formula gives (0.2).

All irreducible `S_d` characters are realizable over the rationals, so there
is no rational-versus-complex descent saving.  More importantly, changing
generators cannot change (1.1): after decomposing any proposed virtual
representation into irreducibles, the same hook coefficients reappear.
The triangle inequality then makes (0.3) a lower bound for every signed
presentation, with equality for (0.1).

For the integral numerator, let `e_lambda` and `o_lambda` be the even- and
odd-degree multiplicities of an irreducible in a semisimple complex.  Its
Euler coefficient is `e_lambda-o_lambda`.  Equation (0.1), multiplied by
`d`, forces this difference to be `(-1)^k` on `H_k` and zero elsewhere.
Hence

\[
 e_{H_k}+o_{H_k}\ge1.
\]

Summing dimensions over even and odd `k`, respectively, gives

\[
 \sum_{k\text{ even}}{d-1\choose k}
 =\sum_{k\text{ odd}}{d-1\choose k}=2^{d-2},
\]

proving (0.4) and the complex lower bound.

## 2. Product selectors are multiplicatively expensive

For independent universal place coordinates of degrees
`d_1,...,d_r`, the monodromy group is the product

\[
 S_{d_1}\times\cdots\times S_{d_r}.
\]

The exact simultaneous irreducibility indicator is the external tensor
product `q_(d_1) tensor ... tensor q_(d_r)`.  Product irreducible characters
are again an orthonormal basis, so uniqueness tensorizes and

\[
 \boxed{
 \left\|\bigotimes_{i=1}^r q_{d_i}\right\|_{\rm rank}
 =\prod_{i=1}^r{2^{d_i-1}\over d_i}.}
\tag{2.1}
\]

No termwise decomposition of that exact product selector in the full product
character category can have smaller absolute rank mass.

This sharpens the entropy--conductor warning.  In the scalable closed-place
model, the `r`-th eligible degree has typical size

\[
 d_{(r)}=\exp((1/\delta+o(1))r).
\]

Paying even one exact selector termwise at that degree has logarithmic rank
cost asymptotic to `(log 2)d_(r)`, which is exponential in `r`; the formal
hard-mask leverage gains only `r log(5/4)`.  Therefore the raw exact
irreducibility selector cannot be expanded into constituents and bounded
separately in a growing-place proof.  It must cancel as an assembled virtual
class before complexity is measured, or be replaced by a weaker or
source-specific mechanism.

## 3. What this does and does not rule out

The theorem closes one precise escape:

```text
exact d-cycle indicator on every conjugacy class
  + characteristic-zero finite monodromy through S_d
  + complexity paid as absolute semisimple rank
  -> forced mass 2^(d-1)/d.
```

It does **not** rule out:

- a source-specific trace function required only on a strict subset of
  conjugacy classes;
- an approximate, averaged, or one-sided selector;
- cancellation after tensoring the selector with the full FFPS complex;
- a geometric complex whose relevant pushed-forward cohomology is much
  smaller than the absolute rank of a termwise presentation;
- modular or non-semisimple constructions where ordinary characteristic-zero
  character decomposition is not the complexity ledger;
- selecting descended closed-orbit atoms rather than universal geometric
  roots.

In particular, the universal incidence identity

\[
 [\mathcal P_d\otimes\mathcal Q_d]=0
\]

remains valuable: if it is assembled before taking absolute complexity, the
boundary vanishes exactly.  The no-go says that expanding `Q_d` first and
hoping for a cheaper exact `S_d` character presentation cannot work.

## 4. Consequence for the next experiment

The affordable-selector question should no longer be posed as a search over
alternative exact `S_d` virtual representations.  The live experiments are:

1. tensor the selector with the **entire** owner/core/Wick relative complex
   and simplify in `K_0` before any termwise estimate;
2. identify the smallest quotient of the factorization-type algebra actually
   observed by the native source and solve the selector problem there;
3. replace exact irreducibility by a low-complexity signed filter that kills
   only the boundary constituents occurring in the pushforward;
4. test whether a descended closed-orbit description avoids the universal
   root permutation module altogether.

These are changes of geometry or of the information requested from the
selector.  Within the exact full-`S_d` category, the optimization problem is
finished.

## 5. Proof and scope ledger

| statement | grade |
|---|---|
| unique hook expansion (0.1) | **PROVED EXACT** by orthogonality and Murnaghan--Nakayama |
| forced absolute/positive/negative masses | **PROVED EXACT** |
| semisimple complex lower bound and parity realization | **PROVED EXACT** |
| product-selector mass (2.1) | **PROVED EXACT** |
| determinant replay of the cycle indicator through `d=10` | **BOUNDED EXACT CHECK** |
| cheaper exact full-`S_d` semisimple selector | **RULED OUT IN THE STATED CATEGORY** |
| cheaper source-specific or jointly cancelled geometric selector | **OPEN / NOT RULED OUT** |
| native FFPS adapter, uniform trace estimate, individualization | **OPEN** |
| `CYSEL`, `WCADD`, `WCKUM`, RH, or GRH | **NOT PROVED** |

The character theory is classical and no external novelty is claimed for
(0.1)--(0.4).  The project contribution is the obstruction ledger: it closes
the explicitly open rank-optimization loophole in the previous boundary
packet and redirects the scalable amplifier towards joint cancellation.

## 6. Bounded replay

```text
python -B research/l-families/atlas/function_field/ffps_exact_cycle_selector_mass_no_go.py --check
python -B -O research/l-families/atlas/function_field/ffps_exact_cycle_selector_mass_no_go.py --check
python -B -m unittest tests.test_ffps_exact_cycle_selector_mass_no_go
python -B -O -m unittest tests.test_ffps_exact_cycle_selector_mass_no_go
```

The replay checks every cycle type through degree ten, the exact hook ranks
and parity masses through degree twelve, three product panels, the canonical
JSON, and every frozen source blob.  It enumerates no finite-field point,
polynomial, closed place, curve, sheaf, source atom, `L`-function, or zero.
