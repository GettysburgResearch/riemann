# Renewed direct attack on `CP(K)`: higher Euler closure and the balanced Möbius core

Agent: `gpt56-04-f`  
Date: 2026-08-07  
Branch: `agent/gpt56-04-f/151-finsler-target-completion`  
Input head: `75b8273e697247f3ce535da97e35929436912225`  
Imported terminal work: PR #165 at `13d32ea7a694acf64f5e55b4a41b9b632cd22dd0`  
Status: **PROPOSED PENDING INDEPENDENT REVIEW; `CP(K)` NOT PROVED; RH NOT PROVED**

## Executive conclusion

The direct continuation produced one real analytic strengthening:

```text
first Euler closure of terminal lattices
        ->
arbitrary-order Euler closure of every packet
with one complete unrestricted lattice carrying
any fixed positive logarithmic fraction.
```

This removes substantially more than the original terminal Type-I family.

It does not close the complete packet. After all such complete-lattice classes
are removed from the exact fixed-logarithm Heath--Brown slice, the residual
packet carries its macroscopic scale in truncated Möbius variables. The
residual retains exactly the rightmost-zero exponent of the Möbius safe signal.

Therefore the current chain is not a full proof packet. Its remaining theorem
is the balanced truncated-Möbius estimate `BTP(K)`, a genuine RH-bearing
arithmetic statement.

## 1. Imported terminal theorem

PR #165 `L-15449/L-15450` proves, subject to review, that a complete unrestricted
integer lattice

\[
 \sum_{n>=1}{P(\log n)\over\sqrt{An}}W(x-\log(An))
\]

has zero continuous main term under the half-pole moment conditions and a first
Euler remainder of size `e^(-x/2)` independent of the prefix `A`. Summing
prefixes `A<=e^(delta J)` closes every terminal family for `delta<1/2`.

The mechanism is valid only because the terminal variable retains its complete
active integer lattice.

## 2. Higher-order free-variable closure

`L-15160` smooths the safe window without adding an open-strip zero and applies
Euler summation to arbitrary order `R`. For one complete free variable it gives

\[
 |T_(A,P)(x)|
 \ll A^{R-1}e^{-(R-1/2)x}\operatorname{poly}_{K,R}(x,\log A).
\]

If the complementary product is at most `e^((1-eta)J)`, summing every prefix
costs `e^((1-eta+o(1))J)` and yields

\[
 \sup_{J<=x<=J+1}|T_J(x)|
 \le e^{(1/2-R eta+o(1))J}.
\]

Choosing `R>1/(2 eta)` gives exponential decay. Thus a free lattice need not be
the terminal variable; any complete unrestricted coordinate with fixed positive
logarithmic scale can be eliminated.

## 3. Why a cutoff must not be inserted in the Euler coordinate

The first draft of the sector argument selected tuples by the actual value of a
large unrestricted variable. That would truncate the lattice and create an
uncontrolled boundary term.

`R-15115` repairs this. It selects a coordinate through its **frozen
complementary product**. The selection condition is independent of the Euler
variable, and the common compact window then forces the entire active lattice
to lie in the macroscopic range. Every Euler application is therefore made to
a complete source-bound active lattice.

## 4. Exact residual core

Fix the final logarithmic variable at `q0=2`. `L-15159` identifies the complete
signed slice with a translated Möbius safe signal.

After every complete-lattice prefix class covered by `L-15160` is removed, all
remaining unrestricted variables have logarithmic size at most `eta J+O_K(1)`.
For `eta<1/(2K)`, at least half of the total scale is carried by the truncated
variables

\[
 d_i<=V=e^{J/K+O_K(1)}.
\]

Those variables carry Möbius weights and hard cutoff boundaries. Euler
summation does not apply to them.

The exact Gram-vector decomposition is

\[
 h_\mu=h_{\rm Euler}+h_{\rm bal},
\]

with `h_Euler` exponentially small. Hence `h_bal` retains the same upper
exponential energy exponent `Theta_zeta` as the full Möbius source. A finite
balanced destination partition cannot lower every component exponent because

\[
 \max_\tau E_\tau^{\rm bal}
 \ge ||h_{\rm bal}||^2/R_K^2.
\]

## 5. Attempts that do not close the balanced core

### Generic Cauchy/Schur/Young bounds

These replace the Möbius packet by total variation and pay the complete output
scale. They cannot produce a subexponential energy.

### Higher local moments alone

Hölder converts a balanced convolution to higher moments of its factors, but
the normalized exponential scales add back to one. Without an independent
Möbius moment saving, moment escalation merely repackages the same critical
estimate.

### Increasing Heath--Brown order

The exact packet reconstructs `mu` before its final logarithm. Increasing the
number of variables changes the factorization but not the arithmetic source.
At fixed order, at least one balanced packet retains the Möbius exponent.

### Varying the order with the physical block

A slowly growing order makes the hard variables arithmetically smooth and
suggests Rankin-counting bounds. However the signed tuple coefficient after a
cutoff partition is not the indicator or the Möbius weight of the smooth
numbers; recovering the exact coefficient requires precisely the
large-unrestricted-variable cancellations already removed. No source-bound
subexponential estimate was obtained. Moreover a varying safe filter requires a
separate quantitative pole lower bound.

### Selberg reflection

The critical-reflection identity linearizes the bulk prime-pair algebra, but its
contour-shift residue is exactly the rightmost-zero defect. It does not bound the
balanced Möbius core.

## 6. Correct status

```text
exact Heath--Brown/Mobius decoder             complete, proposed
terminal complete-lattice Euler closure       complete, proposed
higher-order free-lattice Euler closure       complete, proposed
complete-lattice sector partition             complete, proposed
balanced truncated-Mobius residual decoder    complete, proposed
balanced packet estimate BTP(K)                open / RH-bearing
CP(K)                                          not proved
Riemann Hypothesis                             not proved
```

## 7. Review recommendation

Do not submit this branch as a completed RH proof. The reviewable new theorem is
`L-15160`, together with the exact scope theorem `R-15115`.

A future full-proof submission must add a genuine subexponential bound for the
balanced truncated-Möbius normal Gram. Renaming that theorem or importing the
terminal Euler estimate does not close it.
