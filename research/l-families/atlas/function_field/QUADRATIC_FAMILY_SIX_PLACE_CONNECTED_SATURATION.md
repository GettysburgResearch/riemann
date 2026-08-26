# Six-place connected saturation in the quadratic quintic family

Status: **PROVED FROM THE LOCKED MULTI-PLACE THEOREM** for every odd prime
power `q >= 7` and every set of six distinct finite rational places, with a
second exact fixed-`m` degree-five weight classification and genus-four
notch corollary.

This is a symbolic coefficient and set-partition packet. It performs no
finite-field, polynomial-family, curve, extension-field, zero, or sampling
enumeration. It proves no RH/GRH statement or external novelty claim.

## Start here

Let

\[
 \mathcal H_5(q)=
 \{D\in\mathbf F_q[T]:D\text{ monic squarefree},\deg D=5\},
 \qquad N=q^4(q-1),
\]

and let $A=\{a_1,\ldots,a_6\}\subset\mathbf F_q$. The condition `q >= 7`
is exactly the feasibility condition for six distinct finite places when
`q` is odd. Put

\[
 X_a(D)=\chi(D(a)),\qquad C=2q-3,
\]

and define the raw six-place sum

\[
 R_A=S_{5,6}(A)
 =\sum_{D\in\mathcal H_5(q)}\prod_{a\in A}X_a(D).
\tag{1}
\]

For the split-infinity genus-two curve

\[
 C_A:y^2=\prod_{a\in A}(a-z),
\]

write

\[
 P_A(u)=1-t_Au+b_Au^2-qt_Au^3+q^2u^4.
\tag{2}
\]

Let $U_A\in\operatorname{USp}(4)$ denote the normalized Frobenius class of
this displayed curve, so that

\[
 P_A(u)=\det(1-\sqrt q\,U_Au),\qquad
 t_A=\sqrt q\,\chi_{\omega_1}(U_A),\qquad
 b_A=q\bigl(\chi_{\omega_2}(U_A)+1\bigr).
\tag{3}
\]

The finite-place character is even, so its Dirichlet polynomial is

\[
 L_A(u)=(1-u)P_A(u).
\tag{4}
\]

The locked multi-place theorem then gives

\[
\boxed{
 R_A=(q^2-21)t_A+(q-6)b_A-q^2+6q-21.}
\tag{5}
\]

Equivalently, the exact fundamental-character form is

\[
\boxed{
 R_A=(q^{5/2}-21q^{1/2})\chi_{\omega_1}(U_A)
 +(q^2-6q)\chi_{\omega_2}(U_A)-21.}
\tag{6}
\]

Thus the genus-two middle coefficient, which cancels exactly at five
places, re-enters at six places with coefficient `q-6`.

## 1. Exact coefficient extraction

From (2) and (4),

\[
 \ell_1=-t_A-1,\qquad
 \ell_3=-qt_A-b_A,\qquad
 \ell_5=-q^2.
\tag{7}
\]

The source-locked degree-five identity is

\[
 S_{5,m}=
 \left(\binom{m+1}{2}-qm\right)\ell_1
 +(m-q)\ell_3+\ell_5.
\tag{8}
\]

At `m=6` this becomes

\[
 R_A=(21-6q)\ell_1+(6-q)\ell_3+\ell_5.
\tag{9}
\]

Substitution of (7) into (9) cancels the two `qt_A` cross terms and proves
(5). Substituting (3) then cancels the trivial part of $b_A$ against the
scalar polynomial and proves (6). The producer carries both calculations
out in sparse exact rings and checks every coefficient independently.

## 2. Second Frobenius power re-enters

If $\alpha_1,\ldots,\alpha_4$ are the inverse roots of $P_A$, then

\[
 t_A=\sum_j\alpha_j,\qquad
 b_A=\sum_{i<j}\alpha_i\alpha_j.
\]

Consequently, with

\[
 s_{2,A}=\sum_j\alpha_j^2
 =q^2+1-\#C_A(\mathbf F_{q^2}),
\]

Newton's identity gives

\[
\boxed{b_A={t_A^2-s_{2,A}\over2}.}
\tag{10}
\]

Equation (5) is equivalently

\[
\boxed{
 R_A=(q^2-21)t_A
 +{q-6\over2}(t_A^2-s_{2,A})
 -q^2+6q-21.}
\tag{11}
\]

This is the first degree-five marked-place correlation in the
`m=1,\ldots,6` ladder to retain an independent second-power, or middle-
coefficient, channel: the five-place row saw only $t_A$. Equivalently, that
independent channel can be written using the $\mathbf F_{q^2}$ point count.
This is an exact reformulation of the same genus-two local polynomial, not a
new compatible system or motive claim. No
$\mathbf F_{q^2}$ points are enumerated.

## 3. Exact connected sixth cumulant

For a subset $I\subset A$, let $t_I$ use the same curve convention. For a
four-subset set

\[
 R_I=q^2-10+(4q-10)t_I.
\tag{12}
\]

All one-place means vanish. Hence only set partitions with no singleton
blocks survive in the joint cumulant. The 203 set partitions of six labels
have the following centered part:

| block profile | number of partitions | cumulant coefficient per partition |
|---|---:|---:|
| `6` | 1 | 1 |
| `4+2` | 15 | -1 |
| `3+3` | 10 | -1 |
| `2+2+2` | 15 | 2 |

The `3+3` row is indexed by the ten unordered complementary pairs
$\{B,A\setminus B\}$ with $|B|=3$. The last row consists of the fifteen
perfect matchings, and its cumulant coefficient `2` produces the total
coefficient `30` because every pair moment equals $C/N$.

Exact moment--cumulant inversion therefore gives

\[
\boxed{
\begin{aligned}
 \kappa_A={}&{R_A\over N}
 -{C\over N^2}\sum_{\substack{I\subset A\\|I|=4}}R_I\\
 &-{9(q-2)^2\over N^2}
   \sum_{\substack{\{B,A\setminus B\}\\|B|=3}}
      t_Bt_{A\setminus B}
 +{30C^3\over N^3}.
\end{aligned}}
\tag{13}
\]

The producer generates all 203 partitions rather than inserting the
multiplicities by hand. On a formal labelled trace table, the direct
partition sum and the closed expression (13) agree as exact rational
numbers.

## 4. Hasse envelopes and the first persistence check

The fundamental characters have dimensions `4` and `5`, so

\[
 |\chi_{\omega_1}(U_A)|\leq4,\qquad
 |\chi_{\omega_2}(U_A)|\leq5,\qquad
 |t_I|\leq2\sqrt q\quad(|I|=3,4).
\tag{14}
\]

For `q >= 7`, all displayed polynomial coefficients in (6) have fixed sign,
so the raw normalized term in (13) satisfies the sharper character bound

\[
 { |R_A|\over N}
 \leq {4(q^2-21)\sqrt q\over N}
 +{5(q^2-6q)+21\over N}.
\tag{15}
\]

Its $\omega_1$ envelope is $O(q^{-5/2})$; the $\omega_2$ and constant
terms are $O(q^{-3})$. This improves the cruder bound obtained from
$|b_A|\leq6q$. The proper connected corrections obey

\[
 {C\over N^2}\sum_{|I|=4}|R_I|
 \leq {15C(q^2-10)\over N^2}
      +{30C(4q-10)\sqrt q\over N^2}
 =O(q^{-7})+O(q^{-15/2}),
\tag{16}
\]

\[
 {9(q-2)^2\over N^2}
 \sum_{\{B,A\setminus B\}}|t_Bt_{A\setminus B}|
 \leq {360q(q-2)^2\over N^2}
 =O(q^{-7}),
\tag{17}
\]

and

\[
 {30C^3\over N^3}=O(q^{-12}).
\tag{18}
\]

Thus

\[
\boxed{\kappa_A=O(q^{-5/2})}
\tag{19}
\]

uniformly in the six marked places. This is the first persistence or
saturation check beyond order five: the $q^{-5/2}$ Hasse envelope first
displayed at five places persists at six, while $b_A$ re-enters at the
smaller $q^{-3}$ scale. It is not a theorem that order six uniquely creates
a threshold, that either scale is attained, or that it describes a typical
configuration.

## 5. Fixed-\(m\) ceiling and the genus-four notch

There is a short general consequence for fixed `m >= 5` and odd `q >= m`.
The finite Dirichlet polynomial has `m-1` inverse roots. The geometric roots
have absolute value $\sqrt q$; for even `m` the additional trivial inverse
root is `1` and is also bounded by $\sqrt q$. Therefore

\[
 |\ell_j|\leq\binom{m-1}{j}q^{j/2}.
\tag{20}
\]

Equation (8) now gives

\[
 S_{5,m}=O_m(q^{5/2}),\qquad
 \mu_m:={S_{5,m}\over q^4(q-1)}=O_m(q^{-5/2}).
\tag{21}
\]

This is a coarse fixed-`m` ceiling: its constants are not uniform when `m`
grows, and the top channel can cancel.

To see the cancellation exactly, write

\[
 P(u)=\sum_jp_ju^j
 =\det(1-\sqrt q\,Uu),\qquad
 p_j=(-1)^jq^{j/2}e_j(U).
\]

Here $U$ is always the normalized Frobenius class of the source-convention
curve

\[
 C_A:y^2=\prod_{a\in A}(a-z).
\]

For odd `m`, silently replacing its right-hand side by the monic polynomial
$\prod_a(z-a)$ multiplies it by `-1`; when `-1` is nonsquare this is the
nontrivial quadratic twist and changes the odd character channels. The
six-place curve itself is even-degree and already monic, but this warning is
essential in the all-`m` corollary.

Here $\sqrt q$ is Frobenius-weight notation, not a choice of an element of
$\mathbf F_q$ when `q` is nonsquare. The integral $p_j$ identities are the
invariant statements. Equation (8) is exactly

\[
\begin{aligned}
 S_{5,m}&=
 \left(\binom{m+1}{2}-qm\right)p_1+(m-q)p_3+p_5,
 &&m\text{ odd},\\
 S_{5,m}&=
 \left(\binom{m+1}{2}-qm\right)(p_1-p_0)
 +(m-q)(p_3-p_2)+(p_5-p_4),
 &&m\text{ even}.
\end{aligned}
\tag{22}
\]

In both parities the top $q^{5/2}$ channel is

\[
 q^{5/2}(e_3(U)-e_5(U)).
\tag{23}
\]

For $U\in\operatorname{USp}(2g)$, reciprocal symmetry and the fundamental
character identities give

\[
e_3-e_5=
\begin{cases}
e_1=\chi_{\omega_1},&g=2\quad(m=5,6),\\
e_3-e_1=\chi_{\omega_3},&g=3\quad(m=7,8),\\
0,&g=4\quad(m=9,10),\\
-\chi_{\omega_5},&g\geq5\quad(m\geq11).
\end{cases}
\tag{24}
\]

Thus the coarse ceiling (21) has a genuine genus-four notch. The functional
equation $p_5=qp_3$ at `g=4` gives

\[
\boxed{
 S_{5,9}=9p_3+(45-9q)p_1
 =-9q^{3/2}\chi_{\omega_3}
  -45q^{1/2}\chi_{\omega_1}.}
\tag{25}
\]

Hence $\mu_9=O(q^{-7/2})$. For the split-infinity even row,

\[
\boxed{
\begin{aligned}
 S_{5,10}={}&-q^2\chi_{\omega_4}
 -10q^{3/2}\chi_{\omega_3}
 -10q\chi_{\omega_2}\\
 &-55q^{1/2}\chi_{\omega_1}-55,
\end{aligned}}
\tag{26}
\]

so $\mu_{10}=O(q^{-3})$. The $q^{-5/2}$ channel returns from `m=11`
onward as $-\chi_{\omega_5}$. These are exact top-weight cancellations, not
statements that the surviving character assumes a nonzero or typical value.

For proper connected partitions use the following coarse exact/Hasse
block-weight ledger:

\[
 w_2=4,\qquad w_3={7\over2},\qquad w_4=3,\qquad
 w_s={5\over2}\quad(s\geq5),
\tag{27}
\]

meaning that a block moment of size `s` is $O_m(q^{-w_s})$. Singletons
vanish, and every proper centered partition has at least two blocks. Hence

\[
\boxed{\kappa_m-\mu_m=O_m(q^{-5}).}
\tag{28}
\]

The exact minimum exponents supplied by the ledger (27) for the first five
cases are

| `m` | minimizing proper profile(s) | correction exponent |
|---:|---|---:|
| 5 | `2+3` | `15/2` |
| 6 | `2+4` or `3+3` | `7` |
| 7 | `2+5` or `3+4` | `13/2` |
| 8 | `3+5` or `4+4` | `6` |
| 9 | `4+5` | `11/2` |

In particular,

\[
 \kappa_9-\mu_9=O(q^{-11/2}),\qquad
 \kappa_{10}-\mu_{10}=O(q^{-5}).
\tag{29}
\]

All these are upper-envelope exponents only. No sharpness, attainment,
distribution, growing-`m` uniformity, or novelty statement is inferred.

## 6. Source lock, resources, and replay

The packet imports only the canonical multi-place JSON at commit
`c94466e28a48ec429150f63de6d334d4c4f60110`, git blob
`f6183be7e06b284f3cc2c3c4a6ffe5b970c0411e`, LF-normalized SHA-256
`b4529c82d40575593e4c346e4cdfa0aaee417618886b5b1ab448c2469c87ca9e`,
and payload SHA-256
`ddd7332102007ceda079e7b85dd0a482642c3d999dac779dde220af4e3b27c7d`.
It verifies the locked degree-five coefficient theorem before use.

The replay visits exactly 203 set partitions, of which 41 have no singleton,
and performs one sparse coefficient expansion plus bounded fixed-`m`
integer-partition algebra through `m=9`. It enumerates no finite field,
polynomial family, curve, extension field, or zero and uses no floating-point
arithmetic. The payload build, including source verification and packet-file
hashing, fails closed above four seconds; measured time is deliberately not
stored in the canonical payload.

```text
python -B research/l-families/atlas/function_field/quadratic_family_six_place_connected_saturation.py --check
python -O -B research/l-families/atlas/function_field/quadratic_family_six_place_connected_saturation.py --check
python -m pytest -q tests/test_quadratic_family_six_place_connected_saturation.py
python -O -m pytest -q tests/test_quadratic_family_six_place_connected_saturation.py
```

The result is a source-relative family correlation and cumulant identity. It
does not identify an individual motive or full local factor, supply a
principal-member amplifier, or imply RH/GRH. No external novelty claim is
made.
