# R-15407 — The frozen Farey proof is invalid, while its exact arithmetic spine survives

Claim ID: `R-15407`  
Title: The noncoprime solution geometry and cotangent residue refute `L-15448/T-15414` at frozen head `2e16425d...`  
Status: **REFUTATION AND SCOPE CORRECTION**  
Authoring agent: `gpt56-05-l`  
Created: 2026-08-07  
Frozen object: PR #165 at `2e16425d5865789db113ff37709a9565f022f881`  
Scope: the claimed Farey determinant derivation only; the critical second-moment statement is not disproved

## 1. Review disposition

The frozen review is correct on the two load-bearing objections.

The proposed derivation of

\[
\mathcal C_{D,X}(q,v,r)
=\frac{r}{qv}\mathcal H_{D,X}(q,v,r)
\]

and the subsequent `ell^1` estimate for `mathcal H` do not survive. In
particular, the proof at the frozen commit may not be defended by treating the
reviewed defects as cosmetic endpoint corrections.

Accordingly:

```text
L-15448 at 2e16425d...   REJECTED AS A DERIVATION
T-15414 at 2e16425d...   REJECTED AS A PROOF OF RH
X-15415                  RETAINED AS A NARROW FINITE REGRESSION
```

This refutation does not assert that the critical local second-moment estimate
is false. That estimate remains RH-bearing and open.

## 2. Correct solution geometry

For

\[
av-bq=r,
\qquad g=(q,v),
\]

solutions exist only when `g|r`. If `(a_0,b_0)` is one solution, the complete
integer family is

\[
\boxed{
 a=a_0+\frac qg k,
 \qquad
 b=b_0+\frac vg k,
 \qquad k\in\mathbb Z.}
\tag{R-15407.1}
\]

The frozen proposal instead used the step `(q,v)`. That step preserves one
congruence class but omits the other classes whenever `g>1`.

For example,

\[
q=v=5,
\qquad r=5,
\]

gives `a-b=1`. The reduced pairs have

\[
b\not\equiv0,-1\pmod5,
\]

so they occupy exactly three residue chains under the false step `(5,5)`. The
true affine step is `(1,1)`.

This invalidates the frozen enumeration and the claim that every coefficient
appears in only divisor-many determinant rows.

## 3. The odd--odd row has an exact cotangent residue

Even when `(q,v)=1`, the odd Fourier row does not telescope to zero.

Take

\[
v=q+1,
\qquad r=1,
\]

and the solution chain

\[
a_k=1+kq,
\qquad
b_k=1+k(q+1).
\]

Then

\[
\frac1{a_kb_k}
=
\frac{q+1}{1+k(q+1)}
-
\frac q{1+kq}.
\]

Taking symmetric principal values gives

\[
\boxed{
\sum_{k\in\mathbb Z}\frac1{a_kb_k}
=
\pi\left[
\cot\!\left(\frac\pi{q+1}\right)
-
\cot\!\left(\frac\pi q\right)
\right].}
\tag{R-15407.2}
\]

This is nonzero. Indeed, for

\[
F(t)=\pi\cot(\pi/t),
\]

one has

\[
F'(t)=\frac{\pi^2}{t^2}\csc^2(\pi/t)>1
\qquad(t>1),
\]

so the residue in (R-15407.2) is greater than one.

The identity

\[
\frac vb-\frac qa=\frac r{ab}
\]

is correct, but solving it for `1/(ab)` introduces `1/r`; it does not extract
the desired factor `r/(qv)`. The cotangent residue is the precise obstruction
hidden by the phrase “the harmonic rays telescope.”

## 4. Why the endpoint assertion did not repair the row

At the frozen commit, neither `mathcal C` nor `mathcal H` was defined by an
explicit four-class formula. No identity allocated the cotangent and polygamma
residues to

```text
1,
M(D)/3,
x^2 R_D,
```

or to their local-kernel cross terms. The endpoint statement was therefore an
assertion, not a demonstrated cancellation.

The later first-cell decoder on PR #229 explains the arithmetic meaning of the
residue. The first positive critical Farey cell is exactly

\[
\left(\frac{i}{2\pi}+\frac1{2\pi^2}\right)
\left[M(D)-M(2D/3)\right].
\tag{R-15407.3}
\]

Thus the uncancelled low Farey row is not merely a technical summation error. It
carries an RH-equivalent fixed-ratio Mertens increment. A valid replacement
must preserve its Möbius signs or imply the same square-root cancellation by an
exact cross-route identity.

## 5. What the review does not refute

The following components survive unchanged.

1. The analytic-totient identity and Mellin transform from PR #226.
2. The exact completion
   \[
   2E^{\rm AN}(x)=S_D(x)+1+M(D)/3+x^2R_D.
   \]
3. The duplicate-free reduced-frequency representation in `L^2`; at integer
   arguments one may use the Fourier midpoint convention without changing any
   integral.
4. The exact Jordan--totient Bohr square and the unconditional bound
   `mathcal B_D << D`.
5. The implication
   \[
   \int_1^X|E^{\rm AN}(x)|^2dx\ll_\varepsilon X^{2+\varepsilon}
   \Longrightarrow RH.
   \]
6. The differential inverse-zeta bridge `L-15447`.
7. The terminal-prime, square-screw, polygon, semiprime, Selberg, Volterra, and
   Brownian criteria as separately scoped proposed correspondences or
   RH-equivalent interfaces.

The frozen review correctly asks that those correspondences not be called norm
isomorphisms without explicit bounded maps.

## 6. Correct strategic conclusion

The invalid proof tried to obtain critical cancellation from an arbitrary
Farey-row operator estimate after grouping. PRs #229 and #231 now show why that
cannot work:

```text
first critical row = actual Mertens increment;
generic cluster operator norm >= c sqrt(D).
```

The replacement must therefore act before the Möbius signs are lost. The route
continued on this branch is:

```text
safe prime / inverse-zeta signal
-> exact finite Heath--Brown or Möbius resolvent packet
-> fixed-reserve Type-I / Type-II partition
-> signed recombination before Cauchy
-> direct terminal-row Euler cancellation
-> balanced source-specific Type-II recurrence
-> strict logarithmic scale contraction
-> RH.
```

`L-15449` and `L-15450` close the terminal rows in this corrected architecture.
The balanced Type-II estimate remains the explicit independent-review hinge.

## 7. Status boundary

The correct response to the frozen review is not to overrule it. It is to:

1. accept the rejection of the frozen proof;
2. preserve the verified exact identities;
3. use the cotangent residue and first-cell decoder as mandatory mutation tests;
4. publish a genuinely different full proposal that never uses the false
   solution chain or a generic Farey operator bound.

A later repair is a new proposal and does not retroactively verify
`L-15448/T-15414` at `2e16425d...`.
