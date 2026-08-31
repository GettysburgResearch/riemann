# All-inner width bounds and the source dual-jet interface

Status: CLASSICAL ANALYTIC INGREDIENTS; NEW SOURCE-INTERFACE CORRECTION AND
BOUNDED EXACT CONTROLS. Independent frozen-SHA review required.

Scope: every genuinely inner upper-half-plane numerator, including infinite
Blaschke and singular inner factors; finite denominator with arbitrary complex
nodes and multiplicities. No native cofinal count, total-charge, free-energy,
descent, percentage, or RH conclusion. RH remains unsolved.

Exact dependencies: eight Git/blob/LF-SHA-256 bindings in the manifest. The
historical claims are preserved, not silently repaired. In particular, the
raw-value convention in L-106671 is incompatible with the explicit Fourier
Gram below; its covariance algebra and the independent band bounds survive.

What was run: Gaussian-rational Gram, value/dual-jet, partial-fraction,
orthogonality, source covariance and positivity controls, with strict type,
resource and complete-source/fixture tests. No numerical Fourier integration,
transcendental evaluation, numerical Xi samples or formal analytic verification.

Smallest remaining gap: the bounds below localize a finite packet's physical
band; they do not bound its total physical charge. A native cofinal
denominator/count/source-charge ledger and the free-energy comparison remain.

## 1. Width-sensitive theorem for every inner numerator

Use the unitary Fourier map
\[
 F(x)=(2\pi)^{-1/2}\int_0^\infty f(t)e^{ixt}dt,
 \qquad \langle F,H\rangle=\int_{\mathbb R}\overline F H\,dx.
\]
Let \(B_-\) be a finite Blaschke product with zeros
\(b_j=a_j+iy_j\), \(y_j>0\), listed with multiplicity, and degree \(n\ge1\).
Let \(B_+\) be ANY inner function on the upper half-plane. Let \(E\) synthesize
any basis of \(K_{B_-}=H^2\ominus B_-H^2\), \(G=E^*E\), and, for any measurable
frequency set \(I\) of finite Lebesgue measure \(\Delta\), put
\[
 H_I=E^*M_{B_+}^*\Pi_I M_{B_+}E,\quad
 S=\sum_j y_j,\quad
 \beta=\frac{16}{\pi^{3/2}}\sqrt\Delta\sum_j\sqrt{y_j}.
\]
The band projector acts in the Fourier realization; it is never commuted
through an inner or outer multiplier. Then
\[
 \boxed{\operatorname{tr}(G^{-1}H_I)
 \le\sum_j\min\{1,\tfrac{16}{\pi^{3/2}}\sqrt{\Delta y_j}\}
 \le\min\{n,\beta\},\qquad
 H_I\le\min\{1,\beta\}G.}                         \tag{IW1}
\]
Also \(\beta\le(16/\pi^{3/2})\sqrt{\Delta nS}<4\sqrt{\Delta nS}\)
when \(\Delta>0\); the non-strict version covers \(\Delta=0\).

Proof. Write \(b_b(z)=(z-b)/(z-\bar b)\). Iterating the elementary orthogonal
decomposition \(K_{uv}=K_u\oplus uK_v\) gives the Takenaka--Malmquist basis
\[
 \phi_j(x)=\left(\prod_{\ell<j}b_{b_\ell}(x)\right)
             \sqrt{y_j/\pi}\,(x-\bar b_j)^{-1}.
\]
Unimodular constants do not matter. The decomposition proves orthonormality
and spanning, also for repeated zeros, without a separation assumption.
Boundary modulus one gives, almost everywhere,
\[
 |B_+(x)\phi_j(x)|^2
   =\frac{y_j}{\pi((x-a_j)^2+y_j^2)}=:P_{y_j}(x-a_j).
\]
These functions belong to \(L^{4/3}\cap L^2\). The usual Hausdorff--Young
inequality in this normalization is
\(\|\mathcal F^{-1}F\|_4\le(2\pi)^{-1/4}\|F\|_{4/3}\).
The nonsharp constant follows by Riesz--Thorin interpolation between the
\(L^1\to L^\infty\) norm \((2\pi)^{-1/2}\) and Plancherel norm one.
Band Holder therefore gives
\[
 \int_I|\mathcal F^{-1}(B_+\phi_j)|^2
 \le\sqrt{\Delta/(2\pi)}
       \left(\int_{\mathbb R}P_{y_j}^{2/3}\right)^{3/2}.
\]
After scaling, this last integral is
\(\pi^{-2/3}y_j^{1/3}J\), where
\[
 J=\int_{\mathbb R}(1+u^2)^{-2/3}du
 \le 2+2\int_1^\infty u^{-4/3}du=8.
\]
Thus each band mass is at most \((16/\pi^{3/2})\sqrt{\Delta y_j}\), and also
at most one by Plancherel. Sum over this orthonormal basis. Positivity then
bounds the largest eigenvalue of \(G^{-1/2}H_IG^{-1/2}\) by its trace, while
\(H_I\le G\) gives the unit cap. Cauchy--Schwarz proves the height-sum bound.
Finally \(\pi>3\) implies \(16/\pi^{3/2}<4\). No approximation, derivative,
phase moment or degree of \(B_+\) occurs in this proof.

For comparison, Hilbert-valued Hausdorff--Young is also dimension-free:
apply scalar Hausdorff--Young between
\(\|\widehat{\boldsymbol F}\|_{L^4(\ell^2)}
\le(\sum\|\widehat F_j\|_4^2)^{1/2}\) and
\((\sum\|F_j\|_{4/3}^2)^{1/2}\le\|\boldsymbol F\|_{L^{4/3}(\ell^2)}\).
Both outside inequalities are Minkowski. Concavity applied to the model
kernel diagonal would instead yield
\((16/\pi^{3/2})\sqrt\Delta(\sum y_j^{1/3})^{3/2}\).
Summing the separate basis bounds is stronger and yields (IW1).

## 2. Values are not kernel coefficients: an explicit correction

For simple nodes use the column kernels
\[
 E_j(x)=\frac{i}{\sqrt{2\pi}(x-\bar b_j)},\qquad
 G_{ij}=\frac{i}{b_i-\bar b_j}.
\]
They satisfy \(E^*F=\sqrt{2\pi}(F(b_j))_j\). If
\(V=\operatorname{diag}(B_+(b_j))\), the reproducing identity gives
\[
 E^*M_{B_+}=VE^*,\qquad M_{B_+}^*E=E A,\quad A=V^*.
\]
Consequently the PHYSICAL adverse compression is
\[
 \boxed{E^*P_{B_+H^2}E=A^*GA=VGV^*\le G,}
                                                        \tag{IW2}
\]
not \(V^*GV\) with this Gram. Switching an inner-product convention requires
switching all coefficient/synthesis conventions together; it does not justify
inserting raw values in the displayed column-matrix formulas.

Exact falsifier: take \(b=(i,1+i,2+i)\) and
\(B_+(z)=(z-2i)/(z+2i)\). Its raw values are
\((-1/3,-1/5-2i/5,1/13-8i/13)\). Then
\[
 \operatorname{rank}(G-VGV^*)=1,\quad
 \operatorname{tr}(G^{-1}VGV^*)=235/117<3,
\]
whereas
\[
 \det(G-V^*GV)=-64/14625,\quad
 \operatorname{tr}(G^{-1}V^*GV)=1943/585>3.                 \tag{IW3}
\]
Thus the literal raw-value L-106671 formula cannot be a positive physical
Pick compression with the stated Gram. The coarse packet's real confluent
controls explicitly used adjoint-kernel jets, masking the mismatch in its
simple-node prose. This packet records the correction separately; it does
not rewrite those sources or assert their unrepaired physical determinant.
HT10/CB4--CB5 remain valid algebraic congruences for commuting matrices;
HT11/CB16 remain valid relative inequalities for their defined quadratic forms.
Their physical identification requires the consistent dual convention here.

For confluence let \(r=0,\ldots,q_b-1\),
\[
 E_{b,r}(x)=\frac{i}{\sqrt{2\pi}(x-\bar b)^{r+1}},\quad
 (J_F)_{r,s}=\begin{cases}F^{(r-s)}(b)/(r-s)!,&r\ge s,\\0,&r<s.
 \end{cases}
\]
The normalized value jets obey \(E^*M_F=J_FE^*\), so the coefficient matrix
is \(A_F=J_F^*\), an upper triangular matrix. This is just the Leibniz rule
followed by the Riesz adjoint. The Gram entries are
\[
 G_{(b,r),(c,s)}=
 \frac{i(-1)^r{r+s\choose r}}{(b-\bar c)^{r+s+1}}.
\]
HT4 uses \(t^re^{-(y+ia)t}/r!\), whose Fourier transform is
\(i^{r+1}/[\sqrt{2\pi}(x-\bar b)^{r+1}]\). Thus, with
\(S_0=\operatorname{diag}(i^r)\),
\[
 E_{HT}=E S_0,\quad G_{HT}=S_0^*GS_0,\quad
 A_{F,HT}=S_0^{-1}J_F^*S_0.                              \tag{IW4}
\]
The phase change is essential in nonreal/confluent examples; raw lower
value jets must not be substituted into the HT4 coefficient formula.

## 3. The corrected literal source, outer covariance and physical band

Retain \(N=OB_+,D=OB_-,R=N-D\), with \(O\) holomorphic and nonzero at the
retained denominator nodes, and each retained multiplicity at most its
multiplicity in \(B_-\). Local multiplication then gives
\(J_R=J_OJ_{B_+}=J_{B_+}J_O\). In the Riesz coefficient convention put
\[
 A=J_{B_+}^*,\quad C=J_O^*,\quad R_c=J_R^*=CA=AC,\quad
 G_O=C^*GC.
\]
These are the actual source jets, not freely chosen substitutes. In the HT4
basis conjugate all three coefficient matrices by \(S_0\) as in (IW4).
The outer matrix is invertible. It is retained in the exact metric; we do
not multiply the Fourier waveform physically by the outer factor or commute
it with \(\Pi_I\). For any positive Hermitian weight \(H\), cyclicity gives
\[
 \operatorname{tr}(G_O^{-1}R_c^*HR_c)
 =\operatorname{tr}(G^{-1}A^*HA)=\operatorname{tr}(PH),
 \quad P=AG^{-1}A^*.                                    \tag{IW5}
\]
Also \(G_O-\tau R_c^*GR_c=C^*(G-\tau A^*GA)C\), so their normalized
determinants agree. This is the corrected physical determinant, not an
authentication of the historical raw-value determinant.

By (IW2), \(A^*GA\le G\). The matrix \(T=G^{1/2}AG^{-1/2}\) satisfies
\(T^*T\le1\), hence \(TT^*\le1\), proving \(P\le G^{-1}\).
No matrix is assumed to commute with \(G\) or \(H\). Put
\[
 Q=\operatorname{tr}(PG)\le n,\qquad
 S_I=\operatorname{tr}(PH_I).
\]
The actual projected kernel frame is
\(P_{B_+H^2}E=M_{B_+}EA\); its band Gram is \(A^*H_IA\).
Thus (IW5) with \(H=H_I\) is its canonical physical band trace. From (IW1),
\[
 \boxed{S_I\le\min\{Q,\beta,\min(1,\beta)Q\}.}           \tag{IW6}
\]
The absolute \(\beta\) bound uses the CORRECT dual contraction. For arbitrary
historical raw-value matrices, only the relative inequality from
\(H_I\le\min(1,\beta)G\) is unconditional. If \(Q=0\), then \(S_I=0\);
no ratio by zero is formed. One cannot divide the relative factor by \(n\).

## 4. What the height budget does and does not buy

The unweighted denominator-rank normalized trace satisfies
\[
 n^{-1}\operatorname{tr}(G^{-1}H_I)
 \le\min\{1,(16/\pi^{3/2})\sqrt{\Delta S/n}\}.            \tag{IW7}
\]
For a shallow packet \(y_j\le\eta\), this is at most
\((16/\pi^{3/2})\sqrt{\Delta\eta}\), uniformly in rank and numerator.
For an independently supplied global normalizer \(N_0>0\),
\[
 \frac{\operatorname{tr}(G^{-1}H_I)}{N_0}
 \le\frac{16}{\pi^{3/2}}
       \sqrt{\Delta\,(n/N_0)(S/N_0)}.                   \tag{IW8}
\]
Hence bounded \(n/N_0,S/N_0\) and \(\Delta\to0\) imply a vanishing normalized
band trace (and the corrected physical source band). For several finite
windows replace \(\Delta\) by their maximum, and \(n,S\) by totals;
Cauchy--Schwarz proves the same statement. This needs an independent count
ledger: a height sum does not bound arbitrarily shallow node counts.

The frozen actual-Xi envelope, fixed odd \(K\) and fixed \(M>0\), has
ABSOLUTE width
\[
 \Delta_X=(KM/\pi+o(1))e^{-X}/X,\qquad X\longrightarrow\infty. \tag{IW9}
\]
The relative width is instead of order \(e^{-X}/X^2\). For arbitrary
source-relative suppression it is sufficient that
\(\sqrt{\Delta_X}\sum\sqrt{y_j}\to0\), for example
\(nS=o(Xe^X)\). A charge lower bound comparable with \(n\) is another
possible route from (IW7), but is not supplied here. No native companion
count or substitution \(X\sim\log T\) is inferred. None of (IW7)--(IW9)
bounds total \(Q\), deletes forced topological charge, or closes free energy.

This genuinely removes the FINITE NUMERATOR restriction of HT8 at finite
denominator level, at the price of an absolute-width/height bound. The delay
counterexample in HT14 remains consistent: shifting a fixed-width band to
large frequency does not shrink its absolute width. Unbounded denominator
rank still requires accounting; finite height sum alone does not imply
summability of \(\sum\sqrt{y_j}\).

## 5. Classical priority and exact replay boundary

The Fourier inequality is classical Hausdorff--Young, not a new inequality.
Beckner, [*Inequalities in Fourier analysis*, Annals 102 (1975), 159--182](https://annals.math.princeton.edu/1975/102-1/p11),
proves the sharp form; only elementary nonsharp interpolation is used here.
The orthogonal rational system originates in
[Takenaka (1925), *On the Orthogonal Functions and a New Formula of Interpolation*](https://doi.org/10.4099/jjm1924.2.0_129).
The needed decomposition is explicitly recorded in
[Fricain--Hartmann--Ross, arXiv v2](https://arxiv.org/pdf/1605.07418v2),
(2.12), p.8; (2.18)--(2.19), p.9 record finite model spaces. The elementary
proof above supplies the upper-half-plane and repeated-node instance.
No novelty claim is made. A bounded search of the two pinned Hardy/native
source trees and the current Riemann-structures branch found no earlier
Hausdorff--Young/fractional-height/Takenaka implementation; this is not a
global priority search.

The producer authenticates the eight frozen inputs and the resident exact
Gaussian-rational helper BEFORE importing it. It independently constructs
normalized derivative Grams, lower VALUE jets from Taylor division, their
adjoints, and the HT4 phase change. All principal minors establish finite
positivity; the three-node negative determinant is computed exactly.
For actual rational \(R=O(B_+-B_-)\), it reconstructs jets from the rational
source and checks both local multiplication and outer covariance. An
abstract positive test weight exercises covariance and noncommutation; it
is explicitly not a computed physical band Gram.

Takenaka--Malmquist controls form the actual rational functions by successive
inner multiplication, check full cross-multiplied polynomial identities, and
check all cross-Grams against their exact diagonal norms. Square roots and
\(\pi\) remain symbolic; a bounded rational-square panel tests the squared
coarse bound and Cauchy--Schwarz. No finite check proves Hausdorff--Young,
arbitrary inner boundary limits or the asymptotic Xi envelope.

The public cap is denominator degree four, numerator degree two and total
declared rational degree eight; raw node, width and polynomial input
components are typed exact rationals with 16-bit caps, and internal Gaussian
values have 2048-bit caps. Shapes/counts
are checked before expansion/allocation. Complete canonical-JSON equality,
not subset matching, accepts the fixture; note, producer, tests and manifest
have LF-normalized hashes. External source contracts authenticate metadata,
not remote bytes. Every result-bearing check survives Python -O.

```text
python -B research/exploratory/hardy_inner_width_source_duality.py --check
python -B -O research/exploratory/hardy_inner_width_source_duality.py --check
python -B -m unittest discover -s tests -p test_hardy_inner_width_source_duality.py
python -B -O -m unittest discover -s tests -p test_hardy_inner_width_source_duality.py
```

The packet must receive an independent exact-SHA proof/code review before
import. In particular, the correction must not be mistaken for a reviewed
repair of every downstream historical free-energy consumer.

Author replay: all 30 new tests and both producer modes passed, including
Python -O. Ruff format/lint and diff whitespace checks passed. These are
bounded exact replays, not independent analytic review.
