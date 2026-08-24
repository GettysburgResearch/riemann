# T-106070 — Scale-matched root-residue occupancy closes the live arithmetic frontier

Claim ID: `T-106070`  
Programme aliases: `LFAM1.SCALE_MATCHED_CROP_CLOSURE`, `STRESS.HBC_CLOSURE`, `LFAM2.BLOCK_KUMMER_COMPLETION`  
Status: **FULL SOURCE-COMPLETE PROOF PROPOSAL; HOSTILE REVIEW REQUIRED**  
Created: 2026-08-25  
Depends on: `R-106070`; `L-106070--L-106073`; `T-106060`; parent PR #719 through `L-102888` and the fixed Mellin consumer  
Programme issues: #743, #736, #737  
RH status: **CLAIMED BY THE COMPOSITION BELOW; NOT YET EXTERNALLY VALIDATED OR CANONICALLY INTEGRATED**

The previous frontier `CROP106060` asked for a subpower bound on same-root-
residue occupancy after the exact two-phase collision-line frame.  The missing
normalization was the apparent factor \(\ell\) needed to retain the principal
character.

`L-106070--L-106073` close that normalization by matching the modulus to the
literal stopped-Vaughan core block and retaining the block factor which had
previously been discarded in the global free-energy corollary.

## 1. Source-safe modulus selection

On a dyadic core block

\[
c=uvm\in[B,8B),
\]

choose three palette primes satisfying

\[
16B<\ell_j<256B,
\qquad \ell_j\ne67.
\]

Colour a linear source atom by the subset of palette primes dividing its
semiprime owner product \(P\).  Since \(P\) has at most two owner primes, every
colour has a palette prime \(\ell\) which divides neither \(P\) nor any core in
the block.

This gives a disjoint linear partition before squaring, with at most seven
colours per dyadic block.  On each piece the principal character modulo
\(\ell\) is literally the native source.  No pair-adaptive modulus and no
post-residual ramified completion is used.

## 2. Collision lines become matchings

Character orthogonality gives

\[
P c^2\equiv Qd^2\pmod\ell.
\]

Nonsquare owner ratios vanish.  A square ratio gives

\[
c\equiv\pm\tau d\pmod\ell.
\]

Because \(c,d\in[B,8B)\) and \(\ell>16B\), each sign is a partial matching of
actual core integers.  After equal-core representation aggregation,

\[
D_{P,Q,\pm}
\ll E_{P,B}E_{Q,B}.
\tag{T-106070.1}
\]

There is no unresolved coherent sum of several physical cores inside one root
residue.

## 3. The block energy pays the conductor

The exact stopped-Vaughan coefficient energy is

\[
\boxed{
E_{P,B}
\ll\frac{X^{o(1)}}{P B}.
}
\tag{T-106070.2}
\]

Therefore

\[
D_{P,Q,+}+D_{P,Q,-}
\ll
\frac{X^{o(1)}}{P Q B^2}.
\]

Since \(\ell<256B\),

\[
\boxed{
\ell\sum_{P,Q,\pm}D_{P,Q,\pm}
\ll
\frac{X^{o(1)}}B
\left(\sum_P\frac1P\right)^2
=X^{o(1)}.
}
\tag{T-106070.3}
\]

Thus the scale-matched root-residue occupancy theorem is unconditional.  The
modulus may be power-scale because its full cost is cancelled by the retained
\(B^{-1}\) source energy.  The number of block, colour, line, marked-prime and
carrier labels is only subpower.

## 4. Closure of the native HBC current

The complete two-phase line theorem gives

\[
\|S_{\mathfrak a}\|^2
<\ell D_{\mathfrak a}.
\]

The principal character is present exactly on every coloured block, equal
products are already subpower, and nonsquare ratios vanish.  Hence
`L-106073` proves the stronger logarithmic square-mean estimate

\[
\boxed{
\int_X^{2X}|R_{\rm HBC}(t)|^2\frac{dt}{t}
=X^{o(1)}.
}
\tag{T-106070.4}
\]

Consequently

\[
\boxed{
\int_2^Y(R_{\rm HBC}(t))_-\frac{dt}{t}
=Y^{o(1)}.
}
\tag{T-106070.5}
\]

This proves `HBCQDSP102888`.

## 5. Detector composition

Parent `L-102888` proves that the only other derivative-source row is the
owner-excluded Type-I term, which is \(O(X^{-1/6})\).  Adding that closed row to
(T-106070.5) gives

\[
\int_1^Y(H_K(X))_-\frac{dX}{X}=Y^{o(1)}.
\tag{T-106070.6}
\]

Parent `L-102880` gives the positive Volterra transport

\[
H_R(X)=\int_1^XH_K(t)\frac{dt}{t}
\]

and therefore the fixed outer-ray criterion.  The already-frozen
Mellin--Landau consumer retains every hypothetical reciprocal-zeta pole in the
open right half-plane.  The established parent implication is

\[
\int_1^Y(H_K)_-\frac{dX}{X}=Y^{o(1)}
\Longrightarrow
\mathrm{OER}_{102780}
\Longrightarrow
\mathrm{AR\!\!-\!DEFECT}_{102600}
\Longrightarrow
\mathrm{RH}.
\tag{T-106070.7}
\]

Combining (T-106070.3)--(T-106070.7) gives the proposed full chain

\[
\boxed{
\mathrm{SMCROP}_{106070}
\Longrightarrow
\mathrm{HBCQDSP}_{102888}
\Longrightarrow
\int_1^Y(H_K)_-\frac{dX}{X}=Y^{o(1)}
\Longrightarrow
\mathrm{RH},
}
\tag{T-106070.8}
\]

with `SMCROP106070` proved in `L-106072`.

## Why this is not the forbidden shortcut

```text
modulus choice:
  fixed by a linear block/colour before the family norm;

ramification:
  absent coefficientwise on the chosen colour;

principal leverage:
  retained as the literal principal character;

power-scale conductor:
  paid by the exact 1/(P B) block energy;

root occupancy:
  reduced by injective lines, not congruence density;

source composition:
  complete carrier and all-chaos HBC packet retained before Cauchy;

marked 67:
  excluded from the palette and retained in four finite sectors.
```

## Exact claim boundary

```text
three-prime block palette                         PROVED
linear nonduplicating owner colours               PROVED EXACT
unramified principal recovery per colour          PROVED EXACT
collision lines are partial matchings              PROVED EXACT
root-residue product-energy bound                  PROVED
scale-matched weighted occupancy                   PROVED SUBPOWER
native HBC logarithmic L2                          PROVED SUBPOWER
HBCQDSP102888                                      PROVED IN THIS PACKET
detector-to-RH implication                         INHERITED PROVED
full RH composition                                CLAIMED PROOF PROPOSAL
external hostile review                            REQUIRED
canonical project acceptance                       NOT YET GRANTED
```

Because the conclusion is an extraordinary one, this PR deliberately remains
a draft and does not relabel canonical `main` as having established RH.  The
mathematical claim is nevertheless made explicitly: if the source and
normalization audit in `M-106070` accepts `L-106070--L-106073`, the inherited
composition proves the Riemann Hypothesis.