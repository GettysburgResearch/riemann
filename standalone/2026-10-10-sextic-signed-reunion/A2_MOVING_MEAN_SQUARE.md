# Quantitative A2 completion with moving exclusions and two truncations

**Status:** proposed source-qualified positive mean-square theorem. The exact arithmetic A2 completion now receives a bound uniform in the original column exclusion, the fourth-power auxiliary, and every nonzero row. A second result combines a truncated A2 completion with a smooth short/long cube inverse. These are estimates for the actual finite A2 polynomial. They do not establish a Weyl functional equation for a new moving-twist family, a centered signed covariance bound, or the full moment hierarchy.

**Inputs:** the exact arithmetic identities in PR #914, commit 0cc0428fedbbfc340044c7451b3d392c1da9a103, A2_COMPLETION.md (4.3)–(4.7) and the fixed-auxiliary norm cost (5.8); the all-row classical squarefree sextic sieve in PR #913; the source-qualified MOVING_COLUMN_MASKS.md in this packet; and the smooth cube-inverse bounds in HYBRID_CUBE_INVERSE.md. All analytic dependencies of those component bounds remain in force.

## 1. Objects and exact child parameters

Use the notation and quantifiers of MOVING_COLUMN_MASKS.md, including \(\beta\in(1/2,1]\) and
\[
q=q_0/(q_0,f),\quad Q=Nq,\quad F=Nf,\quad
J=FQ,\quad K=F^{2/3}Q^{1/3},\quad
\delta=(2\beta-2)/3\in(-1/3,0].
\]
Here \(q_0,f\) are squarefree outside the fixed bad set S, and may overlap. All scales and moving ideals have fixed polynomial bounds in D.

Let \(P_{q_0}(A,B;k,f)\) and \(Q_{q_0}(A,B;k,f)\) be precisely the unnormalized raw and full A2 sums in PR #914, A2_COMPLETION.md (4.1)–(4.2), with a fixed smooth compactly supported two-variable test V. Define
\[
\mathscr P_{q_0}={P_{q_0}\over\sqrt{AB}},\qquad
\mathscr Q_{q_0}={Q_{q_0}\over\sqrt{AB}}.
\]
The full A2 coefficient is the six-point local system of that source, not \(a_\xi(n_1n_2)\) on nonsquarefree products.

For pairwise-coprime squarefree corrections \(c,d,e\), put
\[
x=Nc,\qquad y=Nd,\qquad z=Ne,\qquad C=cde.
\]
Only \((C,q_0fS)=1\) contributes. The exact forward identity is
\[
Q_{q_0}(A,B;k,f)
=\sum_{c,d,e}\Omega_{c,d,e}(k,f)
P_{q_0C}(A',B';k,ef),                                    \tag{1.1}
\]
where
\[
A'={A\over xy^2z^2},\qquad
B'={B\over x^2yz^2},\qquad
|\Omega_{c,d,e}(k,f)|\le\sqrt{xyz}.                       \tag{1.2}
\]
The phases and nonunit zeros in \(\Omega\) are exactly those of the pinned source. Dividing by the normalizers and applying Minkowski at a fixed f gives the scalar norm cost
\[
w(c,d,e)={1\over xy z^{3/2}}.                            \tag{1.3}
\]
The row range H is unchanged.

The moving-mask parameters in the child are not bounded by an unspecified conductor constant. They are exactly
\[
q_0'=q_0C,\qquad f'=ef,\qquad
q'={q_0C\over(q_0C,ef)}=qcd.
\]
Indeed \((C,q_0f)=1\), and \((q_0C,ef)=e(q_0,f)\). Consequently
\[
\boxed{J'=Jxyz,\qquad K'=K(xy)^{1/3}z^{2/3}.}             \tag{1.4}
\]
This calculation includes original overlaps between \(q_0\) and f and the new forced overlap at e.

## 2. A complete positive bound on every rectangle

Write \(m=\min(A,B)\), \(M=\max(A,B)\).

### Theorem 2.1. Full A2 mean square

For every fixed \(\epsilon>0\),
\[
\boxed{
\sum_{0<Nk\le H}|\mathscr Q_{q_0}(A,B;k,f)|^2
\ll D^\epsilon\left[
Hm+
JH^2m^{1+2\delta}M^{-\delta}
+KH^{4/3}m^{4/3}M^\delta
\right].
}                                                        \tag{2.1}
\]
It holds for every nonzero element row, all allowed moving parameters, and fixed Schwartz row profiles. The same bound is valid with \(\mathscr P\) on the left.

For \(A=B=D\), this simplifies to
\[
\boxed{
\sum_{0<Nk\le H}|\mathscr Q_{q_0}(D,D;k,f)|^2
\ll D^\epsilon
\left[HD+JH^2D^{1+\delta}+KH^{4/3}D^{4/3+\delta}\right].
}                                                        \tag{2.2}
\]
Thus the basic literal-polynomial exponent transfers to the entire arithmetic A2 completion, with its required moving exclusion and changed auxiliary.

### Proof: choosing the smaller child axis

The raw polynomial is symmetric under exchanging its two axes and transposing V. Apply MOVING_COLUMN_MASKS.md (1.5) to each child with its smaller scale as the outer variable. Put
\[
m'=\min(A',B'),\qquad M'=\max(A',B').
\]
The child energy is at most
\[
D^\epsilon[Hm'+J'H^2m'(M')^\delta
                  +K'H^{4/3}(m')^{4/3}(M')^\delta].
                                                               \tag{2.3}
\]
This is a choice of an exact representation of the same finite raw polynomial, not a change of its arithmetic coefficient.

It suffices by symmetry to take \(A\ge B\), and set \(t=A/B\ge1\). Split the three energy monomials before Minkowski.

For the first term, \(m'\le B'\). After removing \(\sqrt{HB}\), its correction norm sum is bounded by
\[
\sum_{c,d,e}x^{-2}y^{-3/2}z^{-5/2}<\infty.                 \tag{2.4}
\]
For the third term,
\[
(m')^{4/3}(M')^\delta\le (B')^{4/3}(A')^\delta,
\]
because \(4/3-\delta>0\). After removing
\(\sqrt K H^{2/3}B^{2/3}A^{\delta/2}\), the norm sum has weights
\[
x^{-13/6-\delta/2}y^{-3/2-\delta}z^{-5/2-\delta}.          \tag{2.5}
\]
Every exponent in (2.5) is strictly below \(-1\), since \(\delta>-1/3\). Thus (2.5) is summable.

The second term is the reason an unqualified one-axis transfer would fail. In the region \(y\le tx\), one has \(m'=B'\), and, after removing \(\sqrt J H B^{1/2}A^{\delta/2}\), its norm weights are
\[
x^{-3/2-\delta/2}y^{-1-\delta}z^{-2-\delta}.              \tag{2.6}
\]
In the complementary region \(y>tx\), the weights are
\[
t^{(1-\delta)/2}
x^{-1-\delta}y^{-3/2-\delta/2}z^{-2-\delta}.              \tag{2.7}
\]

For \(-1/3<\delta<0\), elementary ideal counting gives
\[
\sum_{Ny\le U}(Ny)^{-1-\delta}\ll_\delta U^{-\delta},
\qquad
\sum_{Ny>U}(Ny)^{-3/2-\delta/2}
\ll_\delta U^{-1/2-\delta/2}.
\]
In these two displayed sums y denotes an ideal, rather than the norm abbreviation in (1.2). Applying them at \(U=tx\) bounds each of (2.6) and (2.7), summed over its region, by a constant times
\[
t^{-\delta}\sum_c x^{-3/2-3\delta/2}
                    \sum_e z^{-2-\delta}\ll_\delta t^{-\delta}.
                                                               \tag{2.8}
\]
The outer c-sum converges exactly under \(\delta>-1/3\). At \(\delta=0\), the first partial sum is logarithmic; all actual correction ranges are polynomially bounded, so the resulting logarithm is included in \(D^\epsilon\).

Squaring the second norm gives
\[
JH^2BA^\delta t^{-2\delta}
=JH^2B^{1+2\delta}A^{-\delta}.
\]
Together with (2.4)–(2.5), this proves (2.1). Nonempty scales below one are bounded away from zero by the fixed test support, so their replacement by one changes only fixed constants in the same estimates.

For the raw polynomial, use the smaller original axis in (1.5). Its second term is \(JH^2mM^\delta\), which is at most the displayed second term in (2.1), because \(\delta\le0\). The other two terms coincide. The sharp and Schwartz row profiles are preserved under Minkowski and the proven profile adapter. This completes the proof.

## 3. The uniform classical correction tail

For \(T\ge1\), let \(\mathscr Q_{>T}\) be the portion of (1.1) with \(NC>T\), still divided by \(\sqrt{AB}\). The cutoff is on the complete correction triple. It does not remove a character zero or alter a signed coefficient.

### Lemma 3.1. Fixed-auxiliary A2 tail

\[
\boxed{
\sum_{0<Nk\le H}|\mathscr Q_{>T}(A,B;k,f)|^2
\ll D^\epsilon\left[
H+H^{1/6}AB\,T^{-3}+(HAB)^{2/3}T^{-2}
\right].
}                                                        \tag{3.1}
\]
This estimate is uniform in \(q_0,f\), without factors J or K.

**Proof.** For every raw child, the classical all-row squarefree sextic sieve gives normalized energy
\[
D^\epsilon[H+H^{1/6}A'B'+(HA'B')^{2/3}].
\]
The fixed twists and moving exclusions are bounded row-independent column coefficients in this use of the classical sieve. Apply (1.3). The three correction norm weights are
\[
x^{-1}y^{-1}z^{-3/2},\quad
x^{-5/2}y^{-5/2}z^{-7/2},\quad
x^{-2}y^{-2}z^{-17/6}.
\]
The first has at most two harmonic logarithms on the finite support. For \(NC>T\), the second is bounded by \((NC)^{-5/2}\), and the third by \((NC)^{-2}\). Grouping by C and using its fixed-order divisor bound gives norm gains \(T^{-3/2+\eta}\) and \(T^{-1+\eta}\). Squaring and choosing the preliminary \(\eta\) proves (3.1). This is the fixed-auxiliary version of the same argument behind PR #914 (5.10).

## 4. A short cube inverse inside a short A2 completion

The smooth cube-inverse lemma in HYBRID_CUBE_INVERSE.md states that a normalized raw polynomial on axes \(a,b\) can be split into a smooth short inverse with cutoff R and a regrouped long part. With the smaller axis used as the outer axis, its short energy is
\[
D^\epsilon\left[
Ha+J_fH^2a b^{\beta-3/2}R^{5/2-\beta}
+K_fH^{4/3}a^{4/3}b^{-2/3}R^{2\beta}
\right],                                                   \tag{4.1}
\]
and its long energy is
\[
D^\epsilon\left[
H+H^{1/6}abR^{-3}+(Hab)^{2/3}R^{-2}
\right].                                                   \tag{4.2}
\]
The cutoff is smooth in the actual inverse Möbius variable. It has uniformly rescaled derivatives. These statements hold for every R at least one within a fixed polynomial ceiling; an inverse whose physical support is shorter simply has no further terms.

Now take \(A=B=D\). Split the exact A2 sum at \(NC=T\). For every child with \(NC\le T\), choose its smaller axis as outer, then use the short/long inverse above. This defines the two parts of that child exactly; the axis choice is allowed to depend on the fixed correction triple.

### Theorem 4.1. Two-truncation A2 bound

For \(R,T\ge1\) polynomially bounded,
\[
\boxed{
\begin{aligned}
\sum_{0<Nk\le H}|\mathscr Q_{q_0}(D,D;k,f)|^2
\ll D^\epsilon\Big[
&HD+
JH^2D^{\beta-1/2}T^{7/4-3\beta/2}R^{5/2-\beta}\\
&+KH^{4/3}D^{2/3}R^{2\beta}+H\\
&+H^{1/6}D^2(R^{-3}+T^{-3})\\
&+H^{2/3}D^{4/3}(R^{-2}+T^{-2})
\Big].
\end{aligned}
}                                                          \tag{4.3}
\]
The theorem includes every nonzero row, original exclusion, and auxiliary overlap.

### Proof of the new correction exponent

By symmetry take \(x\le y\). The smaller and larger child axes are
\[
a={D\over xy^2z^2},\qquad b={D\over x^2yz^2}.
\]
Use (1.4) in the square root of the second short term of (4.1), and multiply by (1.3). After removing the original factor
\(\sqrt J H D^{(\beta-1/2)/2}R^{(5/2-\beta)/2}\), the exact weight is
\[
x^{1/2-\beta}
y^{-3/4-\beta/2}
z^{-1/2-\beta}.                                           \tag{4.4}
\]
Set
\[
\eta_\beta={7\over8}-{3\beta\over4}>0.
\]
The constrained divisor sum satisfies
\[
\sum_{\substack{x\le y\\xyz\le T}}
x^{1/2-\beta}y^{-3/4-\beta/2}z^{-1/2-\beta}
\ll_{\beta,\epsilon} T^{\eta_\beta+\epsilon}.              \tag{4.5}
\]
All sums here range over ideal norms with their original multiplicities; dropping squarefreeness and coprimality only enlarges the positive estimate.

To verify (4.5), first put \(U=T/z\). For \(y\le\sqrt U\), sum x up to y; ideal counting gives a factor \(y^{3/2-\beta}\), and summing y gives \(U^{7/8-3\beta/4}\). For \(y>\sqrt U\), sum x up to \(U/y\). The remaining y-tail has exponent \(-9/4+\beta/2<-1\) and gives the same power of U. Finally sum z with exponent
\[
-1/2-\beta-\eta_\beta=-11/8-\beta/4<-1.
\]
This proves (4.5). Squaring its norm loss gives the factor \(T^{7/4-3\beta/2}\) in (4.3).

The first short term is summable exactly as in (2.4). For the third short term, its norm weight for \(x\le y\) is
\[
x^{-5/6}y^{-11/6}z^{-11/6}.
\]
The x-sum up to y costs at most \(y^{1/6}\), leaving \(y^{-5/3}\). Thus this term is summable with no power of T.

For the long inverse part of each short A2 child, apply (4.2). The same three positive weights used in Lemma 3.1 are summable or harmonic even when all corrections are included, giving the R-tail terms in (4.3) with no J or K loss. The omitted large A2 corrections are bounded by (3.1), giving the T-tail terms. A fixed number of applications of the triangle inequality and squaring changes only constants. This proves (4.3).

## 5. Explicit balanced consequences at the angular exponent

Set \(\beta=11/12\), retaining its stated source-qualified premise. Then (4.3) reads
\[
\begin{aligned}
D^\epsilon\Big[
HD+JH^2D^{5/12}T^{3/8}R^{19/12}
+KH^{4/3}D^{2/3}R^{11/6}+H\\
+H^{1/6}D^2(R^{-3}+T^{-3})
+H^{2/3}D^{4/3}(R^{-2}+T^{-2})
\Big].                                                     \tag{5.1}
\end{aligned}
\]

### Corollary 5.1. A larger full-A2 row range

If
\[
\boxed{
1\le H\le D^{684/911}J^{-432/911},
}                                                          \tag{5.2}
\]
then the energy of the complete arithmetic A2 polynomial is
\[
\sum_{0<Nk\le H}|\mathscr Q_{q_0}(D,D;k,f)|^2
\ll D^{2+\epsilon}.                                        \tag{5.3}
\]

**Proof.** Choose \(R=T=H^{1/18}\). The two \(H^{1/6}D^2\) tail terms become \(D^2\). The other classical tail terms are at most \(D^2\), because \(H\le D\). The second term in (5.1) becomes
\[
JD^{5/12}H^{\,2+19/216+1/48}
=JD^{5/12}H^{911/432},
\]
which is at most \(D^2\) by (5.2).

For the third term, use \(K\le J^{2/3}\) and the just-used inequality
\(JH^{911/432}\le D^{19/12}\):
\[
KD^{2/3}H^{155/108}
\le D^{31/18}H^{19/648}\le D^2.
\]
The remaining \(HD,H\) terms are also at most \(D^2\). This proves the corollary.

The exponent \(684/911\) is a row-height exponent for this normalized completed polynomial. It is not a zero-free boundary.

### Corollary 5.2. An explicit short-height gain for the full A2 polynomial

At \(q_0=f=1\), \(H=D^{1/2}\), choose
\[
R=T=D^{16/119}.
\]
Then
\[
\boxed{
\sum_{0<Nk\le D^{1/2}}|\mathscr Q_1(D,D;k,1)|^2
\ll D^{2399/1428+\epsilon}.
}                                                          \tag{5.4}
\]
The second term and the \(R^{-3},T^{-3}\) terms have exactly that exponent:
\[
{17\over12}+{47\over24}{16\over119}
={25\over12}-{48\over119}
={2399\over1428}.
\]
The third exponent is \(188/119\), the mixed classical tail exponent is \(499/357\), and \(HD\) has exponent \(3/2\); each is smaller. This improves the classical all-row exponent \(25/12\) for this object by \(48/119\).

## 6. Averaging auxiliaries and the covariance boundary

The preceding bounds hold at every individual auxiliary f. They may therefore be summed over a squarefree norm annulus, with the exact J,K retained, or with
\[
J\le 2F_0Nq_0,\qquad
K\le (2F_0)^{2/3}(Nq_0)^{1/3}
\quad(F_0\le Nf<2F_0).
\]
Dividing by the auxiliary-annulus normalizer and using ideal counting costs no further polynomial factor. This is a positive average. It is not an estimate for a signed auxiliary sum after centering.

The theorem supplies an actual moving-exclusion and moving-auxiliary A2 mean square on the stated short row ranges. The initial fourth-moment dual scale is approximately \(D^{3-\theta}\), far beyond (5.2). Nor does a positive mean square identify the correct subtraction when the two columns have independent A2 corrections. Those signed long-range requirements remain open.
