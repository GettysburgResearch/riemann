# Exact low-weight detector boundary quotient

**Status:** exact all-(q) theorem in a declared five-character lattice.

**Scope:** every odd prime power (q), with uniform measure on all monic
squarefree quintics over (mathbf F_q).  The only arithmetic inputs are the
five character means already proved by the all-(q) genus-two moment packet.

**What was actually run:** a (5\times5) integer determinant, exact rational
row reduction, and source-lock checks.  No finite field, curve, zero, random
sample, modular-form database, or numerical integral is evaluated.

**Smallest remaining gap:** add one independently proved high-weight family
mean, preferably (langle\chi_{0,3}\rangle_q) or
(langle R_6\rangle_q), and recompute the saturated filtration.

## 1. The exact boundary map

Let

\[
 \mathcal L=\mathbf Z\langle
 \chi_{0,1},\chi_{2,0},\chi_{0,2},\chi_{2,1},\chi_{4,0}
 \rangle.
\]

Every displayed character is nontrivial, hence has zero (USp(4)) Haar
mean.  Their exact arithmetic means in the marked quintic family are

\[
\begin{aligned}
\langle\chi_{0,1}\rangle_q&=-q^{-1}+q^{-2}-q^{-4},\\
\langle\chi_{2,0}\rangle_q&=q^{-3}-q^{-4},\\
\langle\chi_{0,2}\rangle_q&=-q^{-1}-q^{-5},\\
\langle\chi_{2,1}\rangle_q&=2q^{-3}-q^{-4}-2q^{-5},\\
\langle\chi_{4,0}\rangle_q&=-3q^{-5}.
\end{aligned}
\]

Thus the coefficient map from detector coordinates to the ordered boundary
channels (q^{-1},\ldots,q^{-5}) is

\[
M=
\begin{pmatrix}
-1&0&-1&0&0\\
 1&0& 0&0&0\\
 0&1& 0&2&0\\
-1&-1&0&-1&0\\
 0&0&-1&-2&-3
\end{pmatrix}.
\tag{1}
\]

This is an arithmetic boundary map.  It is not a compact-group moment map,
and no conjectural cohomological row is included.

## 2. Injectivity and the index-three fingerprint

Fraction-free elimination gives

\[
\boxed{\det M=3.}
\]

Consequently no nonzero detector in (mathcal L) has identically zero mean
for every odd prime power.  In particular, exact removal of all five known
finite-(q) channels is impossible inside this lattice.

There is a little more integral structure.  If
(m=(m_1,\ldots,m_5)=Mc), direct elimination gives

\[
\begin{aligned}
c_{01}&=m_2,&
c_{02}&=-m_1-m_2,\\
c_{21}&=m_2+m_3+m_4,&
c_{20}&=-2m_2-m_3-2m_4,\\
c_{40}&={m_1-m_2-2m_3-2m_4-m_5\over3}.
\end{aligned}
\tag{2}
\]

Hence the image has the exact congruence

\[
\boxed{m_1-m_2-2m_3-2m_4-m_5\equiv0\pmod3,}
\]

and Smith invariants ((1,1,1,1,3)).  The cokernel is therefore
(mathbf Z/3mathbf Z).  This divisibility is a property of the proved
arithmetic correction matrix, not a proposed motivic explanation.

## 3. The cancellation filtration

Define

\[
 \mathcal F^r=\{D\in\mathcal L:
                 \langle D\rangle_q=O(q^{-r})\}.
\]

Successive exact elimination yields

\[
\begin{array}{c|c|l}
r&\operatorname{rank}\mathcal F^r&\text{saturated basis}\\ \hline
1&5&\chi_{0,1},\chi_{2,0},\chi_{0,2},\chi_{2,1},\chi_{4,0}\\
2&4&\chi_{0,1}-\chi_{0,2},\chi_{2,0},\chi_{2,1},\chi_{4,0}\\
3&3&\chi_{2,0},\chi_{2,1},\chi_{4,0}\\
4&2&\chi_{2,1}-2\chi_{2,0},\chi_{4,0}\\
5&1&\chi_{4,0}\\
6&0&0.
\end{array}
\tag{3}
\]

Every known boundary order removes exactly one rank.  Primitive sparse
representatives of the new graded directions are

\[
\begin{array}{c|c|c}
\text{first order}&\text{detector}&\text{exact mean}\\ \hline
q^{-2}&\chi_{0,1}-\chi_{0,2}&q^{-2}-q^{-4}+q^{-5}\\
q^{-3}&\chi_{2,0}&q^{-3}-q^{-4}\\
q^{-4}&\chi_{2,1}-2\chi_{2,0}&q^{-4}-2q^{-5}\\
q^{-5}&\chi_{4,0}&-3q^{-5}.
\end{array}
\tag{4}
\]

The (q^{-4}) representative has minimal (ell^1)-support three: equation
(3) shows every exact-order-four vector is a nonzero multiple of
((-2,1)) in the ((\chi_{2,0},\chi_{2,1})) plane, up to adding the later
(\chi_{4,0}) channel.

## 4. Detector-design consequences

The balanced symmetry detector

\[
B=\chi_{2,0}-\chi_{0,2}
\]

has an exactly symmetric (USp(4)) Haar distribution, yet

\[
\langle B\rangle_q=q^{-1}+q^{-3}-q^{-4}+q^{-5}.
\]

Therefore compact symmetry and arithmetic boundary suppression are
independent design constraints.  Quotienting only by Haar-null or
odd-moment-null directions does not remove the leading family bias.

Conversely, (chi_{4,0}) is the unique line in the declared lattice that
cancels the first four arithmetic channels.  This makes it the cleanest
low-weight calibration observable for any proposed spectroscopy pipeline.
It does **not** imply that its (q^{-5}) correction is cuspidal; the formula
is already part of the proved elementary moment packet.

The unresolved weight-six channel

\[
R_6=2\chi_{2,3}+3\chi_{6,0}-3\chi_{4,2}
     +\chi_{2,4}-\chi_{0,6}
\]

is outside (mathcal L).  Nothing in (1)--(4) evaluates its family mean or
identifies a Siegel modular form.  The value of the quotient theorem is that
future high-weight rows can be added without rediscovering or conflating the
five exact low-weight boundary directions.

## 5. Replay and proof boundary

Run

```text
python -B research/l-families/atlas/function_field/genus2_detector_boundary_quotient.py --check
python -B -O research/l-families/atlas/function_field/genus2_detector_boundary_quotient.py --check
python -B -m unittest tests.test_genus2_detector_boundary_quotient
python -B -O -m unittest tests.test_genus2_detector_boundary_quotient
```

The producer authenticates the integer matrix, determinant, filtration,
upstream specializations, and bound source hashes.  It does not independently
reprove the character-moment inputs in this packet, identify cohomology,
prove equidistribution, or imply RH/GRH.
