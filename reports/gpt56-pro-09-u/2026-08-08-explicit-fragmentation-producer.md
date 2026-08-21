# Explicit balanced fragmentation producer for the carry route

Agent: `gpt56-pro-09-u`  
Date: 2026-08-08  
Issue: #238  
PR: #247  
Status: **PROPOSED RESEARCH; RH NOT PROVED**

## 1. Why this continuation was necessary

The scalar finite Gamma–carry minorant programme did not evade the canonical
Gamma–carry factor: sharp finite scalar minorants compactify to the global
independent convolution factor.  Retaining the atomized split coordinate led to
BCT, but BCT still presented a large existential LP.

This continuation removes the LP from the proof statement.

## 2. Exact fragmentation coordinate

`L-23810` proves that every atomized split flow has a node divergence `r`, and
its complete carry vector is simply

\[
 L_q=\sum_mr_m\lfloor m/q\rfloor.
\]

For a prescribed target `w`, the divergence is unique:

\[
 u_m=\sum_{k\le X/m}\mu(k)w(mk),
 \qquad r_m=u_m-u_{m+1}.
\]

Thus Pascal cycles change only the internal fragmentation tree.  They do not
change the target or its Möbius source.

This gives a clean interpretation of the balanced core:

```text
prime-ramp target
    -> unique signed node source
    -> choose a balanced fragmentation of that source.
```

## 3. One explicit signed producer

`L-23811` fixes one half-binary/half-ternary split kernel:

```text
n -> floor(n/2)+ceil(n/2),
n -> ceil(n/3)+floor(2n/3).
```

A descending recurrence produces one coefficient `A_X(n)` per parent.  Its
signed split flow has exactly the target carry load at every integer column.
There is no optimization and no hidden choice.

The complete prime-ramp identity becomes

\[
 \mathcal P(X)=\sum_nA_X(n)\ell_n,
\]

while the all-integer capacity is

\[
 \sum_qw_X(q)=\sum_nA_X(n)c_n.
\]

Therefore the entire error is one explicit pairing

\[
 \sum_nA_X(n)(\ell_n-c_n).
\]

The sufficient rate

\[
 \sum_n|A_X(n)|\sqrt n=X^{o(1)}
\]

is named `BTF` in `T-23803`.

## 4. Reconnaissance and its strict scope

Finite LP reconnaissance found zero-slack balanced flows at every tested modest
endpoint.  Fixed deterministic split rules can remain positive for very long
ranges and then acquire negative coefficients.  A binary–ternary mixture also
shows long low-variation ranges before finite sign changes appear at larger
reconnaissance endpoints.

These observations are **not theorem evidence for cofinal positivity**.  They
serve two narrower purposes:

1. they refute the idea that one may promote a stationary split rule from a
   finite sign table;
2. they motivate the signed total-variation theorem, which does not require
   pointwise positivity.

No floating-point output is used by the proof proposal.  `X-23802` checks only
the exact finite algebra with `Fraction`.

## 5. Why the new hinge is narrower

Compared with BCT, BTF has:

- one coefficient vector rather than quadratically many split variables;
- one fixed balanced kernel;
- an `O(X log X)` Möbius-source construction and `O(X)` descending recurrence;
- one scalar weighted-variation estimate;
- a direct first-cell Mertens mutation.

Compared with GCF, BTF:

- does not assert an independent residual;
- is not log-translation covariant;
- retains two discrete fragmentation scales;
- permits signs before the final recombination.

The arithmetic difficulty has not disappeared.  A hypothetical off-line zero
can create a polynomial oscillatory component in the Möbius source, so a
phase-blind bound cannot prove BTF.

## 6. Most plausible proof mechanisms

A serious attack on BTF should use one of:

1. **Pascal repair:** replace the negative part of the explicit recurrence by
   exact four-cycle moves while preserving the divergence and prove a
   subpolynomial repair budget;
2. **reflected Selberg:** insert the exact recurrence as the scalar forcing of
   the Hermitian square and estimate the recombined variation rather than each
   Möbius term;
3. **high-order fragmentation:** introduce a packet-order `K`, remove every
   one-free-variable branch by Euler cancellation, and prove an `O(1/K)`
   endpoint exponent for the remaining signed recurrence;
4. **variation diminution:** prove that the binary–ternary renewal operator
   turns the complete Möbius divergence into a sequence with subpolynomial
   weighted negative mass;
5. **dual potential:** use `L-23810.11`--`L-23810.12` to prove the corresponding
   balanced-subadditive divisor-floor inequality.

Each mechanism must retain the first fixed-ratio Mertens cell.

## 7. Review order

1. `L-23810-carry-flow-divergence-and-mobius-inversion.md`
2. `X-23802-binary-ternary-flow/verify.py`
3. `L-23811-explicit-binary-ternary-signed-carry-flow.md`
4. `T-23803-binary-ternary-carry-flow-rh-proposal.md`
5. inherited atomized carry and square-screw files

## 8. Exact status

```text
fragmentation divergence algebra       proposed exact
explicit binary-ternary recurrence     proposed exact
exact signed carry saturation          proposed exact
BTF weighted variation                 OPEN / RH-BEARING
conditional deduction to RH            proposed complete
accepted proof of RH                    NO
```

The proposal is now easier to falsify and reproduce, but it is not an
unconditional proof.
