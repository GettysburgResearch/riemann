# L-105434 — Real-rootedness is equivalent to the complete critical sign for every Xi derivative

Claim ID: `L-105434`  
Status: **PROVED CONDITIONAL EQUIVALENCE — REVERSE DIRECTION USES L-105432 AND REQUIRES HOSTILE REVIEW**  
Created: 2026-08-24  
Depends on: `L-105320`, `L-105432`; the real-zero Hadamard product  
RH status: **not assumed**

Fix `r>=0` and put

\[
F=\Xi^{(r)}.
\]

On the simple/noncommon stratum, the following are equivalent.

1. Every zero of `F` is real.
2. Every zero of `F'` is real and

   \[
   \boxed{
   {F(c)\over F''(c)}<0
   }
   \tag{L-105434.1}
   \]

   at every nonremovable critical point.
3. The complete critical Vandermonde/Hankel hierarchy `CRVH105330` holds for
   `F`.
4. `F/F'` is a meromorphic Pick function in the upper half-plane.

The nonstrict version includes removable common zeros through the confluent
ledger.

## 1. Real-rootedness implies the critical sign

If `F` has only real zeros, its order-one definite-parity Hadamard product is

\[
F(z)=Cz^\varepsilon
\prod_{x>0}\left(1-{z^2\over x^2}\right).
\tag{L-105434.2}
\]

Finite partial products have only real zeros. Their derivatives have only real
zeros by Rolle/Gauss--Lucas, and local uniform convergence plus Hurwitz gives
the same for `F'`.

At a noncommon critical point `c`,

\[
{F'(c)\over F(c)}=0.
\]

Differentiating the logarithmic derivative gives

\[
\boxed{
{F''(c)\over F(c)}
=
-\sum_{F(x)=0}{1\over(c-x)^2}<0,
}
\tag{L-105434.3}
\]

with multiplicities included and the paired series absolutely convergent.
Therefore `F(c)/F''(c)<0`.

The same formula is the electrostatic residue identity in `L-105320`.

## 2. The critical sign implies real-rootedness

If every critical point is real and every residue is nonpositive,
`L-105432` proves

\[
\operatorname{Im}{F(z)\over F'(z)}>0
\qquad(\operatorname{Im}z>0).
\]

The quotient cannot vanish in the upper half-plane. Since the denominator has
no nonreal zero, `F` has no upper-half-plane zero. Reflection pays the lower
half-plane. Thus `F` is real-rooted.

## 3. Vandermonde and Pick coordinates

`T-105330` identifies the complete strict critical Hankel hierarchy with
reality of the critical points and negativity of all residues. Hence items 2
and 3 are equivalent.

`L-105432--L-105433` show that item 2 makes `F/F'` Pick. Conversely, a
meromorphic Pick function has only real poles with nonpositive residues and
cannot vanish in the upper half-plane, so item 4 implies both items 1 and 2.

## 4. Xi and RH

At `r=0`, the equivalence becomes

\[
\boxed{
\mathrm{RH}
\Longleftrightarrow
\begin{cases}
\text{every zero of }\Xi'\text{ is real},\\
\Xi(c)/\Xi''(c)\le0\text{ at every critical point}
\end{cases}
\Longleftrightarrow
\mathrm{CRVH105330}(\Xi).
}
\tag{L-105434.4}

This does not solve RH. It identifies the complete critical-sign hierarchy as
an exact, source-specific reformulation rather than one half of a genuinely
independent two-gate problem.

## 5. Scope

The reverse implication is special to the Xi derivative class through the
safe-half-plane and subexponential-side theorems. Abstract entire functions
and finite-window packets retain the independent boundary block of
`L-105218`.
