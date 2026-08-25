# Exact spectrum of the FFPS physical-squareclass Kummer transfer

**Status:** exact finite-dimensional theorem for every odd prime and every
declared core subset on one complete owner quadratic-class coset.  Four tiny
prime-field controls are locked at `p=3,5,7,11`; no conductor or family sweep
was run.

**Frozen source:** corrected PR #751 at
`37d9df4b9b4fb9a8277de6ec1f77278dbbe5b0f2`, with frontier
`T-106121 / FFPS106121` and dependencies `L-106024`, `R-106122`,
`R-106123`, and `L-106126`.  Their git blobs and the four files of the existing
physical-squareclass adapter are hash-locked in the fixture.

**Bottom line:** the full pair-to-physical pushforward is a scaled coisometry,
with a completely flat nonzero singular spectrum.  When the source amplitudes
are shared across cores, varying the declared cores can restore nonconstant
local Fourier modes, but it never improves the top local operator norm or the
sharp principal leverage.  Completing the owner quadratic-class coset makes
that shared-owner operator exactly diagonal.  Incompleteness of the owner set
is measured, entry by entry, by its nontrivial multiplicative Fourier
coefficients.  None of these local facts pays the varying-conductor sum in
corrected FFPS106121.

## 1. The operator

Let

\[
 G=\mathbf F_p^\times,\qquad H=G^2,\qquad m=|H|={p-1\over2},
\]

and fix either owner quadratic-class coset

\[
 \Omega=aH.
\]

For an arbitrary declared subset of unit core residues `C subset G`, there are
two useful, and different, linearizations of the physical map.

The full incidence pushforward is

\[
 K_C:\ell^2(\Omega\times C)\longrightarrow\ell^2(\Omega),
 \qquad
 (K_CF)(x)=\sum_{c\in C}F(xc^{-2},c).
\tag{K}
\]

Every output coordinate has one source preimage for each declared core, and
different output coordinates have disjoint preimages.  Therefore

\[
 \boxed{K_CK_C^*=|C|I.}
\tag{K*}
\]

For nonempty `C`, all `m` nonzero squared singular values equal `|C|`,

\[
 \operatorname{rank}K_C=m,
 \qquad
 \dim\ker K_C=m(|C|-1).
\]

The kernel is the direct sum, over physical residues `x`, of the zero-sum
spaces on the `|C|` preimages of `x`.  Thus adding independent core amplitudes
adds kernel multiplicity, not local spectral gain; `|C|^(-1/2)K_C` is a
coisometry.

When one owner amplitude is replicated across every declared core, let
`D_C f(P,c)=f(P)`.  The resulting shared-owner Kummer transfer is

\[
 (T_Cf)(x)=\sum_{c\in C}f(xc^{-2})=(K_CD_Cf)(x),\qquad x\in\Omega.
\tag{1}
\]

Thus every source atom `(P,c)` is pushed to its corrected physical coordinate
`Pc^2`.  Formula (1) is the operator relevant when the same owner packet is
transported through the declared core residues.  It is not a replacement for
the full FFPS Boolean/incidence coefficients.

Choose a generator `g` of `G`, put `h=g^2`, and order the owner coset as
`a,ah,...,ah^(m-1)`.  Fold the cores into sign pairs:

\[
 \beta_j
 =\mathbf 1_C(g^j)+\mathbf 1_C(-g^j),
 \qquad 0\le j<m.
\tag{2}
\]

The transfer matrix is the integer circulant

\[
 (T_C)_{r,s}=\beta_{r-s}.
\tag{3}
\]

This already shows why `c` and `-c` are the same local Kummer coordinate but
why varying sign-pair occupancy is not owner-only data.

## 2. Full Fourier spectrum, rank, and kernel

Let `zeta_m` be a primitive `m`th root of unity and

\[
 e_t(r)=\zeta_m^{tr},\qquad 0\le t<m.
\]

Direct substitution in (3) gives

\[
 \boxed{
 T_Ce_t=\lambda_t(C)e_t,
 \qquad
 \lambda_t(C)=\sum_{j=0}^{m-1}\beta_j\zeta_m^{-tj}.}
\tag{4}
\]

The matrix is normal, so its singular values are exactly
`|lambda_t(C)|`.  In particular,

\[
 \boxed{
 \operatorname{rank}T_C
 =\#\{t:\lambda_t(C)\ne0\},
 \quad
 \ker T_C
 =\operatorname{span}\{e_t:\lambda_t(C)=0\}.}
\tag{5}
\]

There is also a root-free exact rank certificate.  Put

\[
 B_C(X)=\sum_{j=0}^{m-1}\beta_jX^j\in\mathbf Z[X].
\]

Since `X^m-1` is square-free in characteristic zero,

\[
 \boxed{
 \dim\ker T_C=\deg\gcd(B_C(X),X^m-1),
 \qquad
 \operatorname{rank}T_C=m-\deg\gcd(B_C(X),X^m-1).}
\tag{6}
\]

Equations (4)--(6) cover every declared subset `C`, including the empty set.
The JSON stores multipliers as integer polynomials evaluated at named roots of
unity, never as floating-point approximations.

### Why the modes are exactly the even characters

Write the multiplicative characters of `G` as

\[
 \psi_t(g)=\zeta_{p-1}^{t}.
\]

On one owner coset, `psi_t` and `psi_(t+m)=psi_t kappa` span the same owner
Fourier line, where `kappa` is the quadratic character.  Their squares agree:

\[
 \psi_t^2(g)=\zeta_{p-1}^{2t}=\zeta_m^t.
\]

Conversely, two root characters have the same square exactly when their ratio
is `1` or `kappa`.  Hence

\[
 \widehat G/\langle\kappa\rangle
 \xrightarrow[\text{bijection}]{\psi\mapsto\psi^2}
 \{\theta\in\widehat G:\theta(-1)=1\}.
\tag{7}
\]

The right-hand side is precisely the even-character family.  Formula (4) can
therefore be written in the source notation as

\[
 \lambda_{[\psi]}(C)
 =\sum_{c\in C}\psi(c)^{-2}
 =\widehat{\mathbf1_C}(\psi^2),
\tag{8}
\]

up to the harmless Fourier sign convention.  The core characters in
`R-106122` are not extra decoration: they are the complete spectrum of this
Kummer transfer.

## 3. What core variation creates, exactly

For a genuine subset `C`, the trivial multiplier is

\[
 \lambda_0=|C|.
\]

The triangle inequality and (4) give

\[
 \boxed{\|T_C\|_{2\to2}=|C|.}
\tag{9}
\]

Thus no nonconstant mode can create a larger local norm.  Some may tie the
constant mode (a singleton core is the simplest example), so (9) is a sharp
norm statement rather than a spectral-gap claim.

Parseval gives a complete measure of the extra nonconstant spectrum:

\[
 \sum_t|\lambda_t|^2=m\sum_j\beta_j^2,
\]

and hence

\[
 \boxed{
 \sum_{t\ne0}|\lambda_t|^2
 =m\sum_j\beta_j^2-|C|^2
 =m\sum_j\left(\beta_j-{|C|\over m}\right)^2.}
\tag{10}
\]

Consequences:

- the nonconstant spectrum vanishes exactly when every sign pair has the same
  occupancy;
- a complete sign transversal (`beta_j=1`) and the complete unit set
  (`beta_j=2`) both give rank one;
- one core (`beta` is a delta) gives full rank and all singular values one;
- more generally
  `sum beta_j^2=|C|+2*(number of complete antipodal pairs in C)`.

So core variation can add local rank and nonprincipal spectral mass.  It does
not create a top-norm gain, and a *complete* core shell actually removes all
nonconstant modes.

## 4. Exact owner-incompleteness defect

Let `A subset Omega` be the declared owner set and `M_A` its diagonal mask.
For the normalized Fourier basis, write

\[
 \widehat{\mathbf1_A}(r)
 =\sum_{j=0}^{m-1}\mathbf1_A(ah^j)\zeta_m^{rj}.
\]

Multiplication by the owner mask and then Kummer transfer has the exact matrix

\[
 \boxed{
 \langle e_t,T_CM_Ae_s\rangle
 ={\lambda_t(C)\over m}
 \widehat{\mathbf1_A}(s-t).}
\tag{11}
\]

For the complete owner coset, only the zero Fourier coefficient survives and
(11) is diagonal.  If `delta=|A|/m`, subtract the density model:

\[
 D_{A,C}=T_C(M_A-\delta I).
\]

Every diagonal Fourier entry of `D_(A,C)` is zero, while every off-diagonal
entry is exactly the corresponding nontrivial owner Fourier coefficient from
(11).  Two applications of Parseval yield the sharp global defect identity

\[
 \boxed{
 \|D_{A,C}\|_{\mathrm{HS}}^2
 =\left(\sum_j\beta_j^2\right)
 {|A|(m-|A|)\over m}.}
\tag{12}
\]

For nonempty `C`, the defect is zero exactly when `A` is empty or the complete
owner coset.  This is the precise local cost of owner incompleteness.  It is
mode mixing, not a mysterious change of coordinates.  Also

\[
 \|T_CM_A\|\le|C|,
\]

so incompleteness cannot exceed the complete-shell top norm, although it can
destroy the diagonal spectral decomposition and change rank.

## 5. Hybrid principal-leverage corollary

Identify sign pairs with `H` by `{c,-c} -> c^2`.  The square-phase Gram from
`L-106024` is

\[
 G_p=pI-J.
\]

Its constant eigenvalue is `(p+1)/2`; all nonconstant eigenvalues are `p`.
The principal observation is `O(w)=sum w_j`, so it kills every nonconstant
Fourier mode.  For every nonempty `C`, (4) shows that `T_C` preserves the
constant line with nonzero multiplier `|C|`.  Therefore restricting to the
range of the core transfer, with the phase Gram imposed on the transferred
physical packet, changes neither the sharp extremizer nor its ratio:

\[
 \boxed{
 \|O\|^2_{\operatorname{ran}(T_C),G_p}
 ={p-1\over p+1}.}
\tag{13}
\]

This is a range-metric statement; it does not declare different source cores
orthogonal before their physical collapse.  Within that precise local model,
it makes the no-gain statement stronger: arbitrary local core variation does
not improve the principal contraction at all.  Consequently the earlier
assembly laws remain unchanged after any nonzero local core transfers:

\[
 \left\|\bigotimes_iO_{p_i}\right\|^2
 =\prod_i{p_i-1\over p_i+1},
\]

whereas a positive block sum has squared leverage

\[
 \sum_i|\alpha_i|^2{p_i-1\over p_i+1}.
\]

For unit-weight `p=3,5`, these are respectively `1/3` and `7/6`.

## 6. Meaning for corrected FFPS106121

The theorem cleanly separates four local phenomena:

1. independent pair amplitudes: the flat coisometry (K*);
2. complete owners plus shared arbitrary cores: exactly diagonal even-character
   multipliers (4);
3. incomplete owners: exact mode mixing controlled by (11)--(12);
4. principal observation: unchanged sharp leverage (13).

This rules out one tempting shortcut.  Merely allowing the core to vary does
not manufacture an extra local principal contraction, and summing such local
fibres positively still has the block no-go.  The nonconstant coefficients
in (8) can nevertheless be useful inputs to a future mixed/double trace
formula because they retain the source-faithful core character.

What remains absent is the essential global arithmetic:

- the owner and core sets are not complete residue shells in the Boolean
  source;
- least-prime conductors vary;
- interval, roughness, gcd, incidence, and exceptional-ledger masks couple
  the fibres;
- the mixed and double moments `BTMS106121` and `BTDS106121` require coherent
  cancellation before a positive conductor sum;
- the principal gate `BTPS106121`, number-field export, `BCI102990`, RH, and
  GRH remain open.

Equations (11)--(12) identify the local defect that a genuine varying-core and
varying-conductor theorem must control.  They do not control its sum across
conductors.

## 7. Replay

```text
python -B research/l-families/atlas/function_field/ffps_kummer_transfer_spectrum.py --check
python -B -O research/l-families/atlas/function_field/ffps_kummer_transfer_spectrum.py --check
python -B -m unittest tests.test_ffps_kummer_transfer_spectrum
python -B -O -m unittest tests.test_ffps_kummer_transfer_spectrum
```

The fixture contains only exact integers, rational numerator/denominator
pairs, and integer cyclotomic evaluations.  It rejects floating-point claim
payloads and any enumerated prime outside `3,5,7,11`.  The declared source-atom
cap is 4096.
