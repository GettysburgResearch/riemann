# Full-theorem continuation: parity firewall and adjacent-dyadic Mertens flux

Date: 2026-08-10  
Branch: `research/gpt56-pro/90102-liouville-bernstein-extremality`  
PR: #356  
Status: exact theorem/refutation packet; RH unproved

## 1. Attack undertaken

The session attacked the final critical-neutral sign in three forms:

1. the positive divisor-forcing/Möbius boundary;
2. the compact odd squarefree annulus;
3. the three multiples states `U_X(1),U_X(2),U_X(4)`.

The aim was a literal max-flow or injection paying the negative annular sector.
The attempt did not stop at numerical positivity: the active divisor graph and
the exact Mertens state were both derived to their terminal algebraic forms.

## 2. Boundary repair

`L-90215` correctly proves the elementary forcing

\[
6J(x)-15/2+9/\sqrt2
\]

for `x>=4`, but the same formula cannot be inserted at descendants `x/d<4`.
The corrected all-scale forcing is the piecewise nonnegative function
`widetilde Phi` of `R-90226`.

The repair is substantive but not fatal:

```text
positive forcing             retained;
exact Möbius inversion       retained;
sub-four boundary state      restored;
claimed global large-cell formula rejected.
```

The mutation at `x=2` rejects the uncorrected inversion exactly.

## 3. Divisor-flow route reaches a parity firewall

The odd-annulus representation has support on odd squarefree

\[
X/8<m\le X
\]

and kernel zero

\[
y_0=3/2+\sqrt2.
\]

Every active divisibility edge has ratio `3`, `5`, or `7`. Across such an edge:

- the Möbius sign reverses;
- the kernel sign also reverses;
- the signed contribution color is unchanged.

Hence every connected component of the active divisor graph is monochromatic.
The negative components form a zero-capacity cut for every flow using only
comparability/divisibility edges.

This proves that the most literal exact-flow completion is impossible. Any
valid injection must cross incomparable components, import an external unit
reservoir, or retain signed channels before positivity.

## 4. Exact adjacent-dyadic flux

The three-source coordinate collapses to

\[
\boxed{
K_\star(X)=1-X^{-1/2}
+\frac1{2\sqrt2}
\int_{X/4}^{X/2}[M(t)-M(2t)]t^{-3/2}dt.
}
\]

Thus the final sign is exactly the one-sided adjacent-shell estimate

\[
\boxed{
\int_{X/4}^{X/2}[M(t)-M(2t)]t^{-3/2}dt
\ge-2\sqrt2(1-X^{-1/2}).
}
\]

Equivalently, the weighted Möbius mass of every dyadic shell `[t,2t]`, averaged
over one adjacent octave, must stay below one fixed constant.

This identity includes the exceptional unit correction. Omitting it produces a
false formula.

## 5. Why this is the honest terminal obstruction

The three existing front doors are now literally the same scalar:

```text
three-source Pascal boundary;
compact odd squarefree annulus;
adjacent-dyadic Mertens flux.
```

The natural divisor graph cannot mix signs because it preserves parity color.
The remaining theorem is therefore not another finite filter optimization or a
local transport estimate. It is a parity-breaking bound on incomparable
Möbius components.

That bound would prove RH by the already resident Landau consumer. It is not
proved in this packet.

## 6. Verification

`X-90209-critical-neutral-parity-flux` independently replays:

- the direct arithmetic source;
- the three-source identity;
- the odd-annulus identity;
- the piecewise-exact Mertens integral;
- every active `3/5/7` edge and its color equality;
- the sub-four forcing repair and the `x=2` mutation.

The retained verdict is

```text
PASS_X_90209_CRITICAL_NEUTRAL_PARITY_FLUX
```

at 90 decimal digits.

## 7. Exact frontier

```text
positive forcing above four             PROVED
all-scale piecewise positive forcing     REPAIRED / PROVED
literal divisor max-flow                 REFUTED BY COLOR-PRESERVING CUT
three-source reduction                   PROVED EXACT
odd-annulus reduction                    PROVED EXACT
adjacent-dyadic Mertens-flux reduction   PROVED EXACT
constant one-sided flux bound            OPEN / RH-BEARING
Riemann Hypothesis                       UNPROVEN
```
