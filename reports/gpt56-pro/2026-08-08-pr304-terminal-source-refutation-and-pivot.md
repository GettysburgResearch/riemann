# PR #304 terminal source: completed refutation and corrected research frontier

## Frozen target

```text
repository  gfreund123/riemann
PR          #304
head        78b75fc17e27334a9950018528c1c6e083d74820
proposal    terminal adjacent-commutator closure of the eta boundary
```

This report gives completed proofs of the defects. It does not ask a reviewer to supply a missing argument.

## Verdict

```text
exact adjacent-tree load map                         VERIFIED
q-dependent shifted-fiber expression as a source    FALSE
literal zeroth Euler atomic-mass estimate            FALSE
correct complete-source polylog atomic norm          FALSE
absolute adjacent-terminal closure                   REJECTED
non-absolute coupled boundary estimate               OPEN
Cycle Debt / WSTS / RH                               UNPROVED
```

## 1. First exact defect: the emitted object is not a divisor source

The adjacent-tree map acts on a column-independent coefficient vector:

```text
sigma_m
-> Phi(sigma)=sum_m sigma_m E_(m-1)
-> load_q(Phi)=sum_(q|m) sigma_m.
```

PR #304 instead inserts coefficients `A_k(q,s),B_k(q,s)` which depend on the output column `q`. A single coefficient cannot simultaneously take different values when tested by different columns.

At

```text
N=18, q=5, k=2, s=1,
```

the actual boundary contribution is

```text
1/2(1/76-1/125)=49/19000,
```

while the declared divisor-source load is

```text
1/2(0-1/125)=-1/250.
```

They are unequal. This is a complete hypothesis-matching counterexample to the claimed source identity.

## 2. Second exact defect: the literal zeroth source is already too large

For every stopped endpoint `Y`, all columns

```text
floor((Y+1)/4)+1 <= q <= floor(Y/3)
```

have a common first omitted index `k=2`. The zeroth Euler jet at the odd node `5` has one sign and contributes at least

```text
ell_Y/(10 sqrt(q))
```

to the declared critical atomic norm. Summing the positive stopped-power weights through an output endpoint `X` gives at least a constant multiple of `sqrt(X)`, contradicting the claimed polylogarithmic ledger.

This already rejects the displayed calculation, but a proponent could still ask whether correct Möbius inversion creates additional cancellation. The next theorem closes that escape.

## 3. Strongest result: the correctly inverted complete source has linear mass

Let

```text
Q=floor((N+1)/2)
```

and let `h_N(q)` be the complete critical cutoff boundary on `2<=q<=Q`. Its unique genuine divisor source is

```text
sigma_m=sum_(d<=Q/m) mu(d)h_N(md).
```

On the linear cell

```text
I_N={floor((N+1)/4)+1,...,floor(N/3)},
```

one has `m>Q/2`, so the inversion has only the identity term:

```text
sigma_m=h_N(m).
```

Both omitted parity tails begin at `k=2`, and the complete paired boundary is

```text
h_N(m)=sum_(k>=2)
 [(2km-1)^(-1/2)-((2k+1)m)^(-1/2)]>0.
```

Keeping only `k=2` gives

```text
sqrt(m)sigma_m
 >1/2-1/sqrt(5)
 >1/20.
```

The cell contains at least `N/24` integers for `N>=30`. Therefore

```text
||sigma||_at>N/480.
```

This is the atomic norm of the **complete, correctly typed boundary source**.

For every exact decomposition

```text
sigma=sum_a sigma_a,
```

triangle inequality gives

```text
sum_a ||sigma_a||_at >= ||sigma||_at > N/480.
```

Thus no Euler order, Peano regrouping, stopped-power resolution, or corrected Möbius inversion can make an absolute terminal ledger polylogarithmic.

## 4. Consequence for the proposed RH proof

The frozen proof needs

```text
terminal source atomic cost = polylog(endpoint)
```

to obtain a contracting Cycle-Debt recurrence. The exact lower bound is linear. Therefore the terminal theorem and the proposed RH deduction do not follow.

The sparse adjacent-tree identity remains useful, but not after charging the complete source by absolute atomic variation.

## 5. Correct pivot

The only viable descendant of this route must preserve source cancellation through a quadratic or signed object. Its admissible shape is

```text
complete cutoff boundary
-> unique finite Möbius source
-> combine with the analytic bulk before positive parts
-> independent-frequency normal Gram or signed scale recurrence
-> only then estimate.
```

The following shapes are ruled out:

```text
boundary -> source components -> absolute atomic norms;
boundary -> separate Euler jets -> sum of terminal debts;
q-dependent coefficient fibers -> adjacent-tree source map.
```

The next source-specific target should therefore be an exact **bulk–boundary normal identity**, not another source-count theorem. It must display every cross term and must retain the fixed-ratio Möbius projection. No such identity is claimed proved in this report.

## 6. Exact replay

The standard-library experiment contains three independent mutations:

```text
literal zeroth-source accumulation;
minimal q-dependent source mismatch;
correct-source linear common-tail cell.
```

`verify_correct_source.py` checks the endpoint inequalities, the one-term Möbius inversion, the exact cell count, and the rational lower bound `N/480` at endpoints through `3072`. The written proof is cofinal; the finite replay is only an independent mutation check.

## Final status

```text
PR #304 as a proof of RH                    REJECTED
corrected terminal absolute strategy         FALSE
coupled bulk-boundary strategy               OPEN
Riemann Hypothesis                           UNPROVED
```
