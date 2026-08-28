# Wick subtraction belongs to an external-plus-diagonal Adams category

Status: **exact external-plus-diagonal closed-point extraction theorem, exact
normal-ordered external-product formula, and exact compatibility statement for
literal Wick diagonals; no complete native FFPS atom-space gluing, uniform
Betti estimate, RH, or GRH**.

Architecture: **Architecture B only**.

Bounded exact replay:
[`ffps_relative_external_diagonal_adams.py`](ffps_relative_external_diagonal_adams.py).
Canonical fixture:
[`ffps_relative_external_diagonal_adams.json`](ffps_relative_external_diagonal_adams.json).

Frozen inputs:

1. PR #760's relative-first and phase/coprimality externalization packets;
2. PR #757's exact closed-point Adams compression theorem;
3. the native Wick normal-ordering identity `L-106131` and conclusion-facing
   source ledger `T-106140` at PR #751 head
   `86cac1d64364015ec2cc0f8fbb6fc75dc041c12b`.

## 0. Outcome

The literal Wick diagonal is not an obstruction to closed-point Adams
extraction. It should not be forced into the bivariate partial-Frobenius
category. It belongs to a separate one-place diagonal channel, where ordinary
one-variable Adams--Möbius inversion applies exactly.

Let \(X/\mathbf F_q\) be a fixed closed-point space. Write

\[
 \mathscr E(X,X)
 =
 K_0^{\rm Weil}(X)_{\mathbf Q}
 \otimes
 K_0^{\rm Weil}(X)_{\mathbf Q}
\tag{0.1}
\]

for the separable two-place trace group and let

\[
 \Delta:X\longrightarrow X\times X
\]

be the diagonal. Define the **external-plus-diagonal trace category**

\[
\boxed{
 \mathscr E_\Delta(X)
 =
 \mathscr E(X,X)+\Delta_*K_0^{\rm Weil}(X)_{\mathbf Q}.
}
\tag{0.2}
\]

For

\[
 K=K_{\rm sep}+\Delta_*V
\tag{0.3}
\]

the ordered degree-\((a,b)\) closed-point trace is

\[
\boxed{
 P_{a,b}(K)
 =
 P_{a,b}(K_{\rm sep})
 +\mathbf1_{a=b}P_a(V).
}
\tag{0.4}
\]

The first term is extracted by the exact double Adams formula, and the second
by the exact one-place formula. No independent partial Frobenius is needed on
the diagonal object.

For one external product \(A\boxtimes B\), define its literal normal ordering

\[
\boxed{
 :A\boxtimes B:
 =
 A\boxtimes B-\Delta_*(A\otimes B).
}
\tag{0.5}
\]

Then

\[
\boxed{
 P_{a,b}(:A\boxtimes B:)
 =
 P_a(A)P_b(B)
 -\mathbf1_{a=b}P_a(A\otimes B).
}
\tag{0.6}
\]

Equivalently,

\[
\boxed{
\begin{aligned}
 ab\,P_{a,b}(:A\boxtimes B:)
={}&
 \sum_{e\mid a}\sum_{f\mid b}
 \mu(e)\mu(f)
 A_{a/e}(\psi^e A)
 A_{b/f}(\psi^f B)\\
&-\mathbf1_{a=b}\,
 a\sum_{e\mid a}\mu(e)
 A_{a/e}(\psi^e(A\otimes B)).
\end{aligned}
}
\tag{0.7}
\]

Only

\[
 2^{\omega(a)+\omega(b)}
 +\mathbf1_{a=b}2^{\omega(a)}
\tag{0.8}
\]

nonzero trace evaluations occur.

This is exactly the categorical shape of the native Wick subtraction

\[
 :\!\|Z\|^2\!:
 =\|Z\|^2-D
\tag{0.9}
\]

in `L-106131`: the complete square is a two-copy object, while \(D\) is the
literal same-atom diagonal. Once the off-atomic member has been realized in
the external/partial-Frobenius channel, its Wick subtraction is extracted by
(0.7). Therefore **Wick normal ordering itself is discharged from
`REMAINING-GLUE`**.

This does not construct the complete native atom space, prove that every
carrier/renewal/Boolean restriction is external-plus-diagonal, or estimate any
resulting trace.

## 1. One-place extractor

For a constructible Weil class \(V\) on \(X\), let

\[
 A_n(V)
 =
 \sum_{x\in X(\mathbf F_{q^n})}
 \operatorname{Tr}(F_{q^n,x}\mid V_{\bar x})
\]

and

\[
 P_d(V)
 =
 \sum_{\substack{x\in|X|\\\deg x=d}}
 \operatorname{Tr}(F_x\mid V_{\bar x}).
\]

The exact orbit formula is

\[
 A_n(V)
 =
 \sum_{d\mid n}d\,P_d(\psi^{n/d}V).
\tag{1.1}
\]

Möbius inversion gives

\[
\boxed{
 dP_d(V)
 =
 \sum_{e\mid d}\mu(e)A_{d/e}(\psi^eV).
}
\tag{1.2}
\]

No purity or RH assumption enters.

## 2. Separable two-place extractor

For

\[
 K_{\rm sep}
 =\sum_jc_jA_j\boxtimes B_j,
\]

put

\[
 A_{m,n}^{\rm sep}(K_{\rm sep})
 =\sum_jc_jA_m(A_j)A_n(B_j).
\]

Then

\[
\boxed{
 abP_{a,b}(K_{\rm sep})
 =
 \sum_{e\mid a}\sum_{f\mid b}
 \mu(e)\mu(f)
 A_{a/e,b/f}^{\rm sep}
 (\psi_1^e\psi_2^fK_{\rm sep}).
}
\tag{2.1}
\]

This is the frozen closed-point Adams theorem.

## 3. Diagonal channel

A degree-\(d\) closed point \(x\) contributes through \(\Delta_*V\) only to
the ordered pair \((x,x)\). Hence its two displayed degrees are equal, and

\[
 P_{a,b}(\Delta_*V)
 =\mathbf1_{a=b}P_a(V),
\tag{3.1}
\]

proving (0.4).

There is no need, and generally no way, to assign two independent Frobenius
powers to this diagonal term. It carries one Frobenius and is extracted before
or beside the bivariate object.

This distinction is load-bearing:

```text
off-diagonal/external channel:
  commuting partial Frobenii or a finite signed external-product presentation;

literal diagonal channel:
  one ordinary Frobenius and one-place Adams inversion.
```

Demanding partial Frobenii on their direct sum would create an artificial
obstruction.

## 4. Normal ordering

At a pair of closed points \(x,y\), the trace of \(A\boxtimes B\) is

\[
 t_A(x)t_B(y).
\]

The trace of \(\Delta_*(A\otimes B)\) is zero unless \(x=y\), when it is

\[
 t_A(x)t_B(x).
\]

Therefore (0.5) has the literal trace kernel

\[
 t_{:A\boxtimes B:}(x,y)
 =
 \begin{cases}
 t_A(x)t_B(y),&x\ne y,\\
 0,&x=y.
 \end{cases}
\tag{4.1}
\]

Equation (0.6) follows by summing degree pairs. Substituting (1.2) and (2.1)
proves (0.7).

For a finite rational sum of external products, normal ordering is applied
termwise and the same theorem holds by additivity.

## 5. Application to the native Wick ledger

`L-106131` defines, before conductor fibres are collapsed,

\[
 D_\iota(t)
 =
 \sum_\omega|z_{\iota,\omega}(t)|^2
\tag{5.1}
\]

and subtracts that same literal atomic diagonal from every additive or
character square. Thus its operation is exactly the trace-level restriction
(4.1), provided the native source atoms have been realized as closed points
of one fixed source space and the off-atomic member has been externalized.

The fixed-label phase and reduced-core coprimality layers are already
externalized in the predecessor packet. The present theorem adds:

```text
WICK-EXT:
  literal source normal ordering is an external-minus-diagonal object;
  the external part uses two-place Adams;
  the diagonal part uses one-place Adams.
```

Consequently the updated Architecture B ledger is

```text
PHASE-EXT       PROVED
COPRIME-EXT     PROVED
WICK-EXT        PROVED AS AN EXTERNAL-PLUS-DIAGONAL CATEGORY THEOREM

remaining:
  native atom-space realization;
  Boolean/carrier/renewal/equal-product/horizon gluing;
  relative projector transport through that common gluing;
  uniform signed trace/Betti estimate;
  exact principal binding.
```

The paid principal atomic diagonal in `T-106140` remains analytically useful,
but its prior subpower estimate is not needed to justify the categorical
extraction formula itself.

## 6. Distinct-place convention

For a general external-plus-diagonal object

\[
 K=K_{\rm sep}+\Delta_*V,
\]

the ordered distinct-place restriction is

\[
\boxed{
 P_{a,a}^{\ne}(K)
 =
 P_{a,a}(K_{\rm sep})-P_a(\delta K_{\rm sep}),
}
\tag{6.1}
\]

where \(\delta(A\boxtimes B)=A\otimes B\). The explicit diagonal class \(V\)
cancels: it appears in the raw degree-\((a,a)\) sum and is removed entirely by
the distinct-place restriction.

Thus the theorem is stable whether the diagonal is introduced as a Wick
subtraction, an already-present diagonal source class, or an equal-place
correction.

## 7. Scope firewall

- `WICK-EXT` is a categorical extraction theorem, not a trace estimate.
- A general coupled off-diagonal sheaf is not made separable by subtracting
  its diagonal.
- Equal **product** or carrier collisions need not be literal atom diagonals.
- The complete native owner/Boolean/carrier/renewal source is not constructed.
- The number of Adams evaluations is not a Betti bound.
- Architecture A is not used.

**No NATREL, RELPARTFROB, RELTRACE, principal binding, RH, or GRH theorem is
proved.**

## 8. Proof ledger

| statement | grade |
|---|---|
| external-plus-diagonal degree formula (0.4) | **PROVED EXACT** |
| normal-ordered degree formula (0.6)--(0.7) | **PROVED EXACT** |
| divisor-count evaluation ledger (0.8) | **PROVED EXACT** |
| literal Wick diagonal has this category | **PROVED CONDITIONALLY ON NATIVE ATOM-SPACE REALIZATION** |
| native phase/coprimality externalization | **IMPORTED FROM FROZEN SOURCE** |
| complete native source belongs to \(\mathscr E_\Delta\) | **NOT PROVED** |
| uniform trace estimate / RH / GRH | **NOT PROVED** |

## 9. Bounded replay

```text
python -B research/l-families/atlas/function_field/ffps_relative_external_diagonal_adams.py --check
python -B -O research/l-families/atlas/function_field/ffps_relative_external_diagonal_adams.py --check
python -B -m unittest tests.test_ffps_relative_external_diagonal_adams
python -B -O -m unittest tests.test_ffps_relative_external_diagonal_adams
```

The replay assigns exact rational Frobenius eigenvalue packets to finitely
many synthetic closed points, reconstructs extension-field sums, and verifies
the one-place, double, and normal-ordered extraction formulas. It enumerates
no finite field, curve, conductor family, \(L\)-function, or zero.
