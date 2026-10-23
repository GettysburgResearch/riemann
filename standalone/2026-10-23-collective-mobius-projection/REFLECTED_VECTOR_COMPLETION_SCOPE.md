# Reflected label vectors: the completion plateau

23 October 2026. This derives the exact scope of a possible strengthening
of the label-vector proof. It does not claim a new zero-free boundary.

Use the completed reflection identity (9) of PR1015
COMPLETED_FE_KERNEL.md at commit
e87c5f669f81fe6371af926917d1c5b21023bce8. For a label dyad \(NR\asymp K\)
and column length \(D\), set \(C=DK/Y\). The finite reflected modulus
dyad \(Nc\asymp L\) has the same numerator \(nR\), Gauss orientation,
and finite bad-place vector as before reflection. Separating the
common smooth coordinates \(n/D,R/K,c/L\) is legitimate. Norm twists
in \(R\) are outside each row; the free Möbius coefficient is unchanged.

The finite vector estimate is

\[
 M(L,K)\ll(DLK)^\epsilon
 \min(K,1+K^2/L)\{L+D^{5/6}L^{1/6}\}.
\]

The kernel on \(L\le C\) has size
\((L/C)^{1/6-\epsilon}\), and decays rapidly above \(C\).
Taking its squared envelope and summing dyadically gives, before
the reflected completion-ideal sum,

\[
 G(C,K)\ll(DCK)^\epsilon
 \begin{cases}
 KC+KD^{5/6}C^{1/6},&1\le C\le K,\\
 K^2+D^{5/6}K^{3/2}C^{-1/3},&K\le C\le K^2,\\
 C+D^{5/6}C^{1/6}+D^{5/6}K^{3/2}C^{-1/3},&C\ge K^2.
 \end{cases}                                                \tag{R1}
\]

The extra nonvolume term is the modulus dyad \(L\asymp K\).
For \(K<L<K^2\), the squared weighted nonvolume envelope is
\(D^{5/6}K^2C^{-1/3}L^{-1/2}\); it decreases toward that dyad.
For \(L<K\) it increases toward that dyad. Rapid kernel decay
handles \(L>C\), including every subunit effective scale.

The completed reflected identity also contains every integral ideal
\(b\), with coefficient \(1/Nb\) and scale \(C/(Nb)^6\). This is
not restricted to finitely many bad-prime ideals. For
\[
 (C/K^2)^{1/6}\le Nb\le(C/K)^{1/6},
\]
the square root of the extra term in R1, multiplied by \(1/Nb\), is

\[
 D^{5/12}K^{3/4}C^{-1/6},
\]

independent of \(Nb\). The ideal count up to \((C/K)^{1/6}\) therefore
produces the squared cost \(D^{5/6}K^{7/6}\). Retaining all other
ranges gives the safe completed envelope

\[
 \sum_{NR\asymp K}|F_R(Y)|^2\ll(DYK)^\epsilon
 \begin{cases}
 KC+KD^{5/6}C^{1/6},&1\le C\le K,\\
 K^2+D^{5/6}K^{7/6},&K\le C\le K^2,\\
 C+D^{5/6}C^{1/6}+D^{5/6}K^{7/6},&C\ge K^2.
 \end{cases}                                                \tag{R2}
\]

At \(C<1\), the reflected series is rapidly small, with constants
depending on the chosen fixed decay order. In deriving R2 one may
retain a harmless logarithm in the middle volume range; it is
absorbed by the displayed arbitrary subpower.

Consequently applying the finite label sieve after reflection is
legitimate, but it does not preserve the decaying peak in R1 after
positive completion. Dropping this completion cost would be an
incorrect strengthening.

There is an exact analytic relation at the central point: the
completed vector is regular at \(u=1\), whereas the isolated
completion zeta factor has a pole. Thus the raw full vector vanishes
there in the appropriate regularized sense. This relation does not
justify subtracting a constant from every finite kernel term while
discarding the large-modulus tail. The completed kernel obtained by
summing \(b\) has a nonzero constant contribution at small argument
unless that global relation is used coherently. Establishing such
coherent cancellation with quantitative tails is a new analytic
input, not a consequence of the finite dyad norm estimate above.
