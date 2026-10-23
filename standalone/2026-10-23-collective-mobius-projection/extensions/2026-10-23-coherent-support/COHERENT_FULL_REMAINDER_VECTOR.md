# Coherent reflection improves the full remainder vector

23 October 2026. Proposed analytic deduction; independent review pending.
This is a full-series vector theorem. The analogous moving-coprimality
primitive vector requires a separate argument and is not asserted here.

Use the actual Möbius coefficient and all fixed ray, puncture, smooth
profile and literal-zero conventions of LABEL_UNIFORM_MOBIUS_RESIDUES.md.
Let \(\mathcal R_R(U)\) be its raw full-series contour scalar L19.
For all good sixth-power-free labels \(NR\le K\), assume

\[
 1\le K\le D^{1/7},\qquad U\ge\sqrt{DK}.
\]

Then the proposed strengthening of S5 is

\[
 \boxed{\quad
 \sum_{NR\le K}|\mathcal R_R(U)|^2
 \ll(UDKNQ)^\epsilon
 \{D^{11/12}K^{1/12}+D^{5/6}K^{7/6}\}.
 \quad}                                                     \tag{C1}
\]

The second term retains the completion plateau. No cancellation in
the reflected completion ideals is assumed.

## 1. Three input vector bounds

The frozen sixth-free extension is
SIXTH_FREE_LABEL_EXTENSION.md, SHA256
3e4a3d902aa937d7a498ab1201a269e6891265a9b1c8a34945524c330797b507.
Its S1 gives the whole full-residue vector bound

\[
 \sum_{NR\le K}|P_R(D)|^2\ll(DKNQ)^\epsilon D^{2/3}.     \tag{C2}
\]

Its inherited original completed finite vector satisfies

\[
 \sum_{NR\le K}|B_R(Y)|^2
 \ll(YDKNQ)^\epsilon
 [Y+D^{5/6}Y^{1/6}+K^2+D^{5/6}K^{7/6}].              \tag{C3}
\]

Here \(B_R(Y)=\sum_b(Nb)^{-1}S_R(Y/(Nb)^6)\) is exactly zero
below a fixed positive physical support threshold, because its
original test is annular.

For the completed contour vector \(F_R(Y)\), apply finite V4 after
reflection before summing labels. The numerator and Gauss orientation
are unchanged. On a label dyad \(NR\asymp H\), its effective dual
scale is \(C=DH/Y\). The full reflected completion calculation in
REFLECTED_VECTOR_COMPLETION_SCOPE.md, SHA256
39850353a97e596a8e0ebabfecaf41b954cceed2026612a91ae0716eb62cb040,
retains every integral completion ideal and implies

\[
 \sum_{NR\asymp H}|F_R(Y)|^2
 \ll(YDHNQ)^\epsilon
 [DH/Y+D^{5/6}(DH/Y)^{1/6}+H^2+D^{5/6}H^{7/6}].
                                                               \tag{C4}
\]

The displayed weaker envelope is valid also below the transition
scales in R2, including subunit dual scales using rapid kernel decay.
Summing dyads gives the same expression with H replaced by K.
The common norm profile is separated before either n or R is fixed.
The reflected bad-prime classes remain a fixed finite family.

## 2. Exact reciprocal completion and the balanced split

The exact identity, on the original absolutely convergent line, is

\[
 \mathcal R_R(U)=\sum_a{\mu(a)\over Na}F_R(U/(Na)^6).     \tag{C5}
\]

Split at

\[
 A=U^{1/6}(DK)^{-1/12}\ge1.                            \tag{C6}
\]

For \(Na\le A\), use C4. For \(Na>A\), use the exact original
identity \(F_R(Y)=B_R(Y)-c_wY^{1/6}P_R(D)\), with its fixed
normalizing constant retained. Apply Minkowski in the label Hilbert
space. This uses absolute a weights; no Mertens premise is needed.

The reflected volume head has amplitude

\[
 (DK/U)^{1/2}\sum_{Na\le A}(Na)^2
 \ll(DK/U)^{1/2}A^3=(DK)^{1/4}.
\]

The original volume tail has amplitude
\(U^{1/2}\sum_{Na>A}(Na)^{-4}\ll U^{1/2}A^{-3}
=(DK)^{1/4}\). Their squared cost is \((DK)^{1/2}\).

The reflected nonvolume head has amplitude

\[
 D^{5/12}(DK/U)^{1/12}
       \sum_{Na\le A}(Na)^{-1/2}
 \ll D^{5/12}(DK/U)^{1/12}A^{1/2}
 =D^{11/24}K^{1/24}.
\]

The original nonvolume tail has amplitude
\(D^{5/12}U^{1/12}\sum_{Na>A}(Na)^{-3/2}\), giving the
same result. Their squared cost is \(D^{11/12}K^{1/12}\).

The two plateau amplitudes are bounded by
\(K+D^{5/12}K^{7/12}\) times harmonic ideal sums. The reflected
head is finite. On the original tail, B_R is exactly zero once
\(Na\) exceeds a fixed multiple of \(U^{1/6}\). Thus these sums
cost logarithms only, and their squared contribution is
\(K^2+D^{5/6}K^{7/6}\), up to a subpower.
There is no divergent infinite a^(-1) plateau.

Finally C2 bounds the entire pole tail, including every subunit
scale, by the amplitude

\[
 U^{1/6}D^{1/3}\sum_{Na>A}(Na)^{-2}
 \ll U^{1/6}D^{1/3}A^{-1}=D^{5/12}K^{1/12}.
\]

Its squared cost is \(D^{5/6}K^{1/6}\). Since K<=D,
the volume and pole costs are bounded by the first term in C1,
and \(K^2\) is bounded by the second. This proves C1.

## 3. Quantitative scope

At \(U=D^h\), the old inverse nonvolume exponent is
\(5/6+h/6\). Both C1 terms are strictly smaller, with fixed
epsilon slack, when

\[
 k<\min\{2h-1,\ h/7,\ 1/7\},\qquad K=D^k,\quad
 h\ge(1+k)/2.                                         \tag{C7}
\]

For the binding scale \(h\) near .859, the restrictive comparison
is \(k<h/7\), about .123. The earlier S5 had the smaller range
\(k<(2h-1)/7\), about .103.

This is a coherent full-contour improvement. Passing it through the
whole primitive inversion, or controlling the orthogonal complement
of the actual inverse row vector, remains a separate task. No smaller
B_flat is inferred from C1.
