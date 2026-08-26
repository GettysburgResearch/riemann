# FFPS cyclic closure budget: what WCADD/WCKUM do and do not control

Status: **exact conditional closure theorem and exact coefficient-cone no-go**.
The WCADD106140 and WCKUM106140 estimates remain open.

## Start here

There are two different questions hiding behind “does WCADD/WCKUM control the
cyclic centered identity?”

1. **The identity as a whole:** yes, conditionally and with sharp scalar
   constants. The left side is the principal Wick-centered trace. If the open
   WCADD and WCKUM estimates are proved, their difference controls it.
2. **The two cyclic mechanisms separately:** no. The hard conditioned-current
   average and the selected Kummer trace share one uncontrolled positive-growth
   direction. No linear, triangle, or generic Cauchy recombination of the
   declared bounds sees that direction.

The exact bookkeeping is three-dimensional. On an eligible cyclic collection
of live bilateral fibres, define

\[
\begin{aligned}
 C&=\text{principal-weighted average of the \(k\) rotated hard currents},\\
 S&=\text{principal-weighted selected cyclic Kummer trace},\\
 R&=\text{the residual complete nonprincipal Kummer trace}.
\end{aligned}
\]

Then the committed cyclic identity and live L-106131 decomposition give

\[
 \boxed{
 P=C-S,\qquad K=S+R,\qquad A=C+R,\qquad P=A-K.}
\tag{0.1}
\]

Here \(A,K,P\) are the additive, complete nonprincipal, and principal
Wick-centered traces. The coefficient matrix for \((A,K)\) on
\((C,S,R)\) is

\[
 \begin{pmatrix}1&0&1\\0&1&1\end{pmatrix},
\]

whose kernel is

\[
 \boxed{(C,S,R)\longmapsto(C+T,S+T,R-T).}
\tag{0.2}
\]

Thus \(A,K,P\) are unchanged while the hard and selected traces grow together.
The cyclic construction does not turn the two open live gates into estimates
for its constituents.

More generally, this gives an exact coefficient-budget closure criterion. A
target

\[
 L_{u,v,w}=uC+vS+wR
\]

is controlled by linear recombination of the two declared scalar gates if and
only if

\[
 \boxed{w=u+v.}
\tag{0.2a}
\]

Indeed this is precisely the condition that \((u,v,w)\) annihilate the kernel
in (0.2), or equivalently lie in the row span of the measurement matrix. In
that case

\[
 L_{u,v,w}=uA+vK,
 \qquad
 |L_{u,v,w}|\le |u|\varepsilon_A+|v|\varepsilon_K.
\tag{0.2b}
\]

The principal target \((u,v,w)=(1,-1,0)\) passes this test. The individual
hard and selected targets do not.

There is, however, a clean one-inequality closure. For a fixed mask,

\[
 C\ge-{k\over t}D_E,\qquad
 S\ge-\left({k\over t}-1\right)D_E,
\tag{0.3}
\]

where \(D_E\) is the paid principal atomic diagonal on the eligible fibres.
Consequently the single one-sided estimate

\[
 \boxed{
 \mathrm{CYSEL}(k,S):\qquad S(Y)\le Y^{o(1)}
 }
\tag{0.4}
\]

would give \(|S(Y)|=Y^{o(1)}\), and then \(C=P+S\) is subpower as well.
Given the whole-identity bound, the one-sided alternative
\(C(Y)\le Y^{o(1)}\) is equivalent up to the paid atomic terms.

This is the smallest missing analytic inequality exposed by the cyclic route:
an upper bound for only the selected \(k-1\) Kummer modes, globally recombined
before taking an absolute value.

The machine-readable entry point is `exact_theorems` in
`ffps_cyclic_closure_budget.json`.

## 1. Frozen source contract and a premise correction

This packet consumes the committed all-\(k\) identity at

`1242951f9529435fd9100d8be6f0d4d4d6f24eae`

and payload

`fa2aa7082d4e6e38f79690ec5295f3ffa238e7be17d9c6a7bfd146f3c9eb7a9f`.

It locks the following live PR #751 claims at head
`98af0db6ec7f77d6333a77a3dac53c4698852f43`:

| claim | role |
|---|---|
| L-106120 | bilateral even-character and root-character channels |
| L-106121 | positive principal moment and paid principal diagonal |
| R-106122 | corrected physical Kummer coordinates |
| R-106123 | global signed conductor-recombination firewall |
| R-106131 | complete atomic cardinality and principal-only payment |
| L-106131 | exact \(A^\circ=P^\circ+K^\circ\) decomposition |
| T-106140 | exact principal inequality and open WCADD/WCKUM gates |

One premise needs saying precisely.
WCADD106140 and WCKUM106140 are not currently proved inequalities. They are
explicitly declared **open
RH-bearing estimates** in T-106140. What is proved is:

- the exact decomposition \(A=P+K\);
- the paid principal atomic diagonal;
- the conditional inequality
  \[
  M_{\rm PP}\le D_{\rm PP}+|A|+|K|.
  \]

The results below are exact coefficient consequences of those proved facts,
and exact statements of what would follow if both open estimates were proved.

## 2. Matching the cyclic coefficients to the live Kummer weights

Fix one eligible fibre with primes \(\ell,\rho\), common exact character order
\(k\), and a retained set \(\mathscr S\) of \(t\) quotient values. Write

\[
 c_q={q+1\over q-1},\qquad
 c=c_\ell c_\rho,\qquad
 w_{\rm NN}={2\ell\over\ell-1}{2\rho\over\rho-1}.
\]

If

\[
 \gamma_r={1\over t}\sum_{s\in\mathscr S}s^{-r},
\]

then the committed Fourier calculation gives

\[
 \sum_{r=1}^{k-1}|\gamma_r|^2={k\over t}-1,
\qquad |\gamma_r|\le1.
\tag{2.1}
\]

The cyclic selected trace occurs with coefficient \(c|\gamma_r|^2\), whereas
the corresponding live L-106120 summand inside \(K\) has coefficient
\(w_{\rm NN}\). Therefore its fraction of that weighted summand is

\[
 \boxed{
 \lambda_r={c\over w_{\rm NN}}|\gamma_r|^2
 ={(\ell+1)(\rho+1)\over4\ell\rho}|\gamma_r|^2.}
\tag{2.2}
\]

Every \(\lambda_r\) lies in \([0,1)\). Define \(S\) by taking these fractions
of the selected double-nonprincipal summands, and define \(R=K-S\). The
residual keeps coefficient \(1-\lambda_r>0\) on each selected channel and
coefficient one on every other mixed or double-nonprincipal channel.

This proves the middle relation \(K=S+R\) in (0.1). Combining it with
\(P=C-S\) and \(A=P+K\) gives \(A=C+R\) exactly.

For the ternary control

\[
 (\ell,\rho,k,t)=(7,13,3,2),
\]

\[
 {c\over w_{\rm NN}}={4\over13},
\qquad |\gamma_1|^2=|\gamma_2|^2={1\over4}.
\]

Hence

\[
 \lambda_1=\lambda_2={1\over13},
\qquad
 \lambda_1+\lambda_2={2\over13}.
\tag{2.3}
\]

The residual retains \(12/13\) of each of those two weighted channels, plus
every other nonprincipal channel.

## 3. The exact atomic budget

Put

\[
 D_0=(\ell-1)(\rho-1).
\]

For one literal atomic diagonal \(D\), the four relevant subtraction
coefficients are

\[
 \boxed{
\begin{aligned}
 B_C&={k\over t}c,\\
 B_S&=\left({k\over t}-1\right)c,\\
 B_K&=D_0-c,\\
 B_R&=D_0-{k\over t}c.
\end{aligned}}
\tag{3.1}
\]

They obey

\[
 \boxed{B_C+B_R=D_0,\qquad B_S+B_R=B_K.}
\tag{3.2}
\]

The first identity is the atomic version of \(A=C+R\); the second is the
atomic version of \(K=S+R\).

The automatic lower bounds (0.3) follow because the uncentered hard squares
and selected character squares have nonnegative coefficients. After global
recombination,

\[
 D_C={k\over t}D_E,\qquad
 D_S=\left({k\over t}-1\right)D_E.
\tag{3.3}
\]

For fixed \(k/t\), both are paid whenever the principal diagonal \(D_E\) is
paid.

The residual is completely different. Relative to the principal atomic
coefficient,

\[
 \boxed{
 {B_R\over c}
 ={D_0\over c}-{k\over t}
 ={(\ell-1)^2(\rho-1)^2\over(\ell+1)(\rho+1)}
 -{k\over t}.}
\tag{3.4}
\]

This grows on the scale \(\ell\rho\). Generic positivity gives only

\[
 R\ge-B_RD.
\tag{3.5}
\]

That lower budget is conductor-dimensional and is exactly the normalization
obstruction isolated by R-106131. Cauchy has not supplied a subpower lower
bound for \(R\).

At the ternary control,

\[
\begin{aligned}
 B_C&={7\over3},&
 B_S&={7\over9},\\
 B_K&={634\over9},&
 B_R&={209\over3}.
\end{aligned}
\tag{3.6}
\]

The finite scalar point

\[
 (C,S,R)=(50,50,-50)
\]

lies inside those declared lower budgets for \(D=1\), while

\[
 A=K=P=0.
\tag{3.7}
\]

This is a coefficient-cone witness, not a claim that one arithmetic source
realizes those exact numbers. It proves that the declared scalar identities,
positivity lower bounds, triangle inequality, and generic Cauchy constants do
not logically exclude a large common hard/selected direction.

## 4. What the two global gates control

Suppose the two open estimates were available with explicit budgets

\[
 |A(Y)|\le\varepsilon_A(Y),\qquad
 |K(Y)|\le\varepsilon_K(Y).
\]

Then, exactly,

\[
 \boxed{
 |P(Y)|=|A(Y)-K(Y)|
 \le\varepsilon_A(Y)+\varepsilon_K(Y).}
\tag{4.1}
\]

The coefficients one and one are sharp if only the two scalar absolute-value
budgets are known: opposite signs attain their sum. No cyclic coefficient
improves (4.1), because the residual \(R\) cancels identically.

There is a localization subtlety, but principal positivity resolves it. Let
\(E\) be any collection of fibres eligible for the chosen cyclic mask. Its
uncentered principal moment is

\[
 M_E=D_E+P_E\ge0
\]

and is a positive sub-sum of the complete principal moment. Hence

\[
\boxed{
 -D_E\le P_E
 \le D_{\rm total}+|A|+|K|-D_E,
}
\tag{4.2}
\]

and in particular

\[
 \boxed{|P_E|\le D_{\rm total}+|A|+|K|.}
\tag{4.3}
\]

Therefore the complete WCADD/WCKUM gates, if proved, already control the
**whole centered cyclic identity** on every eligible subset. There is no
additional localization gate for \(C-S\).

What they do not control is \(C\) or \(S\). The measurement matrix has rank
two and the kernel (0.2). Even localized estimates for \(A_E,K_E\) would leave
the same kernel unless the dimension-bearing negative residual direction were
controlled.

## 5. The exact single-gate closure criterion

Assume the two open gates and use the paid principal diagonal
\(D_E\le D_{\rm total}=Y^{o(1)}\). Then (4.3) says that the hard and selected
traces differ by a subpower quantity:

\[
 C_E-S_E=P_E=Y^{o(1)}.
\tag{5.1}
\]

Their lower bounds are already paid:

\[
 C_E\ge-{k\over t}D_E,\qquad
 S_E\ge-\left({k\over t}-1\right)D_E.
\tag{5.2}
\]

Thus only their common positive direction remains. Any one of the following
one-sided estimates kills it:

\[
\begin{aligned}
 \mathrm{CYSEL}(k,S):&\quad S_E(Y)\le Y^{o(1)},\\
 \mathrm{CYHARD}(k,S):&\quad C_E(Y)\le Y^{o(1)}.
\end{aligned}
\tag{5.3}
\]

For fixed \(k/t\), (5.1)--(5.2) make these two conditions equivalent up to
subpower errors, and either implies

\[
 |C_E(Y)|+|S_E(Y)|=Y^{o(1)}.
\tag{5.4}
\]

CYSEL is the more targeted L-function statement: it asks for an upper bound
on only the \(k-1\) explicit double-nonprincipal modes
\((\eta^r,\theta^r)\), with coefficients \(c|\gamma_r|^2\), after coherent
global conductor recombination.

Equivalently, if separately localized \(K_E\) were available, CYSEL would be
the lower residual estimate

\[
 R_E(Y)\ge-Y^{o(1)}.
\]

But the complete WCKUM scalar does not localize \(K\) to \(E\), so CYSEL is
the honest source-facing formulation.

## 6. Why triangle and Cauchy stop here

Three tempting shortcuts fail exactly:

1. **Take the selected part of WCKUM.**

   The centered summands \(|W_{\eta,\theta}|^2-D\) are signed. A bound on
   their complete weighted sum does not bound a selected sub-sum.

2. **Return to the uncentered positive family.**

   Positivity then introduces the atomic coefficient \(B_R\), whose ratio to
   the paid principal diagonal is (3.4). This reinstates the
   conductor-dimensional trace corrected by R-106131.

3. **Apply Cauchy fibre by fibre.**

   This takes absolute values before the signed varying-conductor
   recombination and is forbidden by R-106123 and T-106140.

So the no-go is not “the cyclic identity is useless.” Its whole principal
combination is exactly the RH-facing quantity. The no-go says that the hard
gain cannot be promoted into a proof by merely pointing to the selected modes
inside WCKUM. One new analytic estimate must control their common positive
growth.

## 7. Exact boundary

Proved exactly here:

- the coefficient matching (2.2) between the cyclic selected modes and live
  L-106120 weights;
- the three-variable relations (0.1) and the kernel (0.2);
- the exact atomic coefficients (3.1)--(3.4);
- the sharp conditional whole-identity budget (4.1);
- localization of that principal budget to any eligible subset by positivity;
- the one-sided single-gate criterion CYSEL/CYHARD;
- a finite ternary coefficient-cone witness.

Not proved:

- WCADD106140 or WCKUM106140;
- CYSEL or CYHARD;
- a selected Kummer trace formula, varying-conductor large sieve, or
  function-field estimate;
- BCI102990, RH, or GRH;
- an external novelty claim.

The main conclusion is therefore precise:

\[
\boxed{
\begin{gathered}
\text{WCADD + WCKUM control the cyclic identity as a whole;}\\
\text{one additional one-sided selected-mode estimate controls its pieces.}
\end{gathered}}
\]

## 8. Reproduction

The producer performs exact rational coefficient algebra only. Its two tiny
numeric controls are \((5,13,2,1)\) and \((7,13,3,2)\). It enumerates no
residue field, prime family, conductor, character family, L-function, curve,
or zero. Source bytes, git objects, exact operations, packet sizes, and wall
time are capped and fail closed.

~~~powershell
python research/l-families/atlas/function_field/ffps_cyclic_closure_budget.py --check
python -O research/l-families/atlas/function_field/ffps_cyclic_closure_budget.py --check
python -m pytest -q tests/test_ffps_cyclic_closure_budget.py
python -O -m pytest -q tests/test_ffps_cyclic_closure_budget.py
python -m ruff check research/l-families/atlas/function_field/ffps_cyclic_closure_budget.py tests/test_ffps_cyclic_closure_budget.py
python -m ruff format --check research/l-families/atlas/function_field/ffps_cyclic_closure_budget.py tests/test_ffps_cyclic_closure_budget.py
~~~

Regenerate the canonical JSON only by omitting `--check` from the first
command.
