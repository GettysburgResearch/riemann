# The fixed-degree marked-place weight notch

Status: **PROVED FROM THE LOCKED ALL-DEGREE MULTI-PLACE IDENTITY** for fixed
integers `n >= 2`, `m >= 1`, every odd prime power `q >= m`, and every set of
`m` distinct finite rational places.

This packet isolates a universal exterior-character cancellation as the mark
count varies. It uses exact bounded symbolic algebra only: no finite field,
polynomial family, curve, inverse-root, zero, or sampling enumeration.

## Start here

Let

\[
 \mathcal H_n(q)=\{D\in\mathbf F_q[T]:D\text{ monic squarefree},\deg D=n\},
 \qquad N_n=|\mathcal H_n(q)|=q^{n-1}(q-1),
\tag{1}
\]

and, for a set $A$ of `m` distinct elements of $\mathbf F_q$, put

\[
 S_{n,m}(A)=
 \sum_{D\in\mathcal H_n(q)}\prod_{a\in A}\chi(D(a)).
\tag{2}
\]

Use exactly the source-convention curve

\[
 C_A:y^2=\prod_{a\in A}(a-z),\qquad
 g=\left\lfloor{m-1\over2}\right\rfloor,
\tag{3}
\]

and write

\[
 P_A(u)=\sum_jp_ju^j
 =\det(1-\sqrt q\,U_Au),\qquad
 p_j=(-1)^jq^{j/2}e_j(U_A).
\tag{4}
\]

Throughout, $p_j=e_j=0$ outside $0\leq j\leq2g$ and
$\chi_{\omega_0}=1$. The symbol $\sqrt q$ records Frobenius weight; it is not
a chosen element of $\mathbf F_q$ when `q` is nonsquare.

Define

\[
 A_{m,k}=\binom{m+k-1}{k},\qquad
 D_r=p_r-qp_{r-2},
\tag{5}
\]

with $p_j=D_j=0$ for negative indices. Then the exact regrouping is

\[
\boxed{
 S_{n,m}=\sum_{0\leq k\leq\lfloor n/2\rfloor}
 A_{m,k}D_{n-2k},\qquad m\text{ odd},}
\tag{6}
\]

and

\[
\boxed{
 S_{n,m}=\sum_{0\leq k\leq\lfloor n/2\rfloor}
 A_{m,k}\bigl(D_{n-2k}-D_{n-1-2k}\bigr),
 \qquad m\text{ even}.}
\tag{7}
\]

The unique top-weight channel in either parity is

\[
\boxed{
 D_n=p_n-qp_{n-2}
 =(-1)^nq^{n/2}\bigl(e_n(U_A)-e_{n-2}(U_A)\bigr).}
\tag{8}
\]

At genus $g=n-1$, equivalently at the two mark counts

\[
 m=2n-1\quad\text{and}\quad m=2n,
\tag{9}
\]

reciprocity gives $e_n=e_{n-2}$, so (8) vanishes exactly. This is the
fixed-degree marked-place weight notch.

## 1. Exact regrouping

The locked all-degree theorem writes

\[
 S_{n,m}=\sum_{\substack{0\leq j\leq n\\n-j\text{ even}}}
 \ell_jB_{m,(n-j)/2},
\tag{10}
\]

where $L(u)=\sum_j\ell_ju^j$ and

\[
 B_{m,k}=\binom{m+k-1}{k}
 -q\binom{m+k-2}{k-1}
 =A_{m,k}-qA_{m,k-1}.
\tag{11}
\]

For odd `m`, infinity is ramified and $L=P_A$. Pairing the two terms in
(11) yields (6). For even `m`, infinity splits and
$L=(1-u)P_A$, so $\ell_j=p_j-p_{j-1}$; applying (6) once in each parity of
the coefficient gives (7).

Every $D_r$ has weight at most $r/2$. Thus $D_n$ is the only channel of
weight $n/2$. In (7), the extra $-D_{n-1}$ has weight $(n-1)/2$; all other
channels are lower still. The producer verifies the original and regrouped
$p_j$ coefficient arrays for every pair

\[
 2\leq n\leq9,\qquad 1\leq m\leq14,
\]

as a bounded formal replay. The proof is the index shift (11), not an
extrapolation from that rectangle.

## 2. The universal \(\operatorname{USp}\) notch

Put

\[
 \Delta_{n,g}=e_n-e_{n-2}.
\tag{12}
\]

Reciprocity $e_j=e_{2g-j}$ and
$e_r-e_{r-2}=\chi_{\omega_r}$ for $0\leq r\leq g$ give the exact four-region
classification

\[
\boxed{
\Delta_{n,g}=
\begin{cases}
0,&2g<n-2,\\
-\chi_{\omega_{2g-n+2}},&n-2\leq2g\text{ and }g\leq n-2,\\
0,&g=n-1,\\
\chi_{\omega_n},&g\geq n.
\end{cases}}
\tag{13}
\]

The convention $\chi_{\omega_0}=1$ is needed at the lower even-`n`
boundary. Within the supported pre-notch region, the character index advances
through the parity of `n`:

\[
 1,3,\ldots,n-2\quad(n\text{ odd}),\qquad
 0,2,\ldots,n-2\quad(n\text{ even}).
\tag{14}
\]

The first zero region in (13) is only insufficient exterior-power support;
the interior cancellation at $g=n-1$ is the marked-place notch.

Including the sign in (8), the pre-notch channel has sign
$(-1)^{n+1}$, the two notch counts null it, and the post-notch channel is

\[
 (-1)^nq^{n/2}\chi_{\omega_n}.
\tag{15}
\]

Thus varying the mark count is an exact top-weight exterior-character
spectrometer. This is useful as a detector-design and aliasing firewall: a
missing top channel at the two notch counts is forced representation algebra,
not evidence for unusual zeros or a new arithmetic correspondence.

## 3. The leading residual channels at the notch

The following highlighted terms are leading weight channels, not complete
equalities for $S_{n,m}$. Equations (16) and (19) retain every lower term
exactly.

At the odd notch $m=2n-1$, (6) becomes

\[
\boxed{
 S_{n,2n-1}=(2n-1)D_{n-2}
 +\sum_{k=2}^{\lfloor n/2\rfloor}
 A_{2n-1,k}D_{n-2k}.}
\tag{16}
\]

Since $g=n-1$,

\[
 (2n-1)D_{n-2}
 =(2n-1)(-1)^nq^{(n-2)/2}\chi_{\omega_{n-2}}.
\tag{17}
\]

Equivalently, the complete odd-notch character expansion is

\[
 S_{n,2n-1}=(-1)^n
 \sum_{k=1}^{\lfloor n/2\rfloor}
 \binom{2n+k-2}{k}q^{(n-2k)/2}
 \chi_{\omega_{n-2k}}.
\]

Consequently, for fixed `n`,

\[
 S_{n,2n-1}=O_n(q^{(n-2)/2}),\qquad
 \mu_{n,2n-1}:={S_{n,2n-1}\over N_n}
 =O_n(q^{-(n+2)/2}).
\tag{18}
\]

At the even notch $m=2n$, (7) becomes

\[
\boxed{
 S_{n,2n}=-D_{n-1}
 +\sum_{k=1}^{\lfloor n/2\rfloor}
 A_{2n,k}\bigl(D_{n-2k}-D_{n-1-2k}\bigr).}
\tag{19}
\]

Its leading residual channel is

\[
 -D_{n-1}=(-1)^nq^{(n-1)/2}\chi_{\omega_{n-1}}.
\tag{20}
\]

The complete even-notch character expansion is

\[
\begin{aligned}
 S_{n,2n}=(-1)^n\Bigg[{}&
 q^{(n-1)/2}\chi_{\omega_{n-1}}\\
 &+\sum_{k=1}^{\lfloor n/2\rfloor}
 \binom{2n+k-1}{k}q^{(n-2k)/2}\chi_{\omega_{n-2k}}\\
 &+\sum_{k=1}^{\lfloor(n-1)/2\rfloor}
 \binom{2n+k-1}{k}q^{(n-2k-1)/2}
 \chi_{\omega_{n-2k-1}}\Bigg].
\end{aligned}
\]

and hence

\[
 S_{n,2n}=O_n(q^{(n-1)/2}),\qquad
 \mu_{n,2n}=O_n(q^{-(n+1)/2}).
\tag{21}
\]

For `n=5`, (16) and (19) recover the genus-four notch rows

\[
 S_{5,9}=-9q^{3/2}\chi_{\omega_3}
 -45q^{1/2}\chi_{\omega_1},
\tag{22}
\]

and

\[
 S_{5,10}=-q^2\chi_{\omega_4}
 -10q^{3/2}\chi_{\omega_3}
 -10q\chi_{\omega_2}
 -55q^{1/2}\chi_{\omega_1}-55.
\tag{23}
\]

These are independent symbolic consistency checks; this packet does not
import the six-place packet.

## 4. Connected correlations and the \(n=2\) exception

For uniform $D\in\mathcal H_n(q)$, put $X_a(D)=\chi(D(a))$. The exact
one-place mean is parity-sensitive:

\[
\boxed{
 \mathbf E[X_a]=
 \begin{cases}
 0,&n\text{ odd},\\
 -q^{-(n-1)},&n\text{ even}.
 \end{cases}}
\tag{24}
\]

Indeed, the one-place generating function is
$(1-qu^2)/(1-u^2)$, whose positive even coefficients are `1-q` and whose odd
coefficients vanish. Thus singleton blocks cannot simply be discarded when
`n` is even.

For every fixed block size `s`, equations (6)--(8) and the Weil coefficient
bounds give

\[
 \mathbf E\!\left[\prod_{a\in B}X_a\right]
 =O_{n,s}(q^{-n/2}).
\tag{25}
\]

The even-`n` singleton value (24) also satisfies (25) for `n >= 2`. Every
proper set partition has at least two blocks, so for fixed `(n,m)` the joint
cumulant obeys

\[
\boxed{
 \kappa_{n,m}-\mu_{n,m}=O_{n,m}(q^{-n}).}
\tag{26}
\]

For `n >= 3`, this correction is below both notch envelopes (18) and (21).
It is also below the even-notch envelope when `n=2`. These are upper-weight
comparisons only: they do not assert that a displayed character is nonzero
for every Frobenius class or that an envelope is attained.

The odd-mark-count `n=2` notch is exceptional because (26) has the same
`q^-2` scale as the raw three-place moment. Here `m=3`, $N_2=q(q-1)$, and

\[
 M_1=-{1\over q},\qquad
 M_2={2-q\over q(q-1)},\qquad
 M_3={3\over q(q-1)}.
\tag{27}
\]

Exact three-variable moment--cumulant inversion gives

\[
\boxed{
 \kappa_{2,3}=M_3-3M_2M_1+2M_1^3
 ={2(2q+1)\over q^3(q-1)}=O(q^{-3}).}
\tag{28}
\]

Thus proper-partition terms cancel the raw $O(q^{-2})$ leader in this one
case. No blanket claim that connected correlations inherit the raw notch
depth may include `(n,m)=(2,3)`.

For completeness, the two `n=2` notch raw rows are

\[
 S_{2,3}=3,\qquad
 S_{2,4}=q^{1/2}\chi_{\omega_1}+4.
\tag{29}
\]

## 5. Conventions, resources, and claim boundary

The source curve (3) is essential. For odd `m`, replacing
$\prod_a(a-z)$ by the monic $\prod_a(z-a)$ multiplies it by `-1`; when `-1`
is nonsquare this is the nontrivial quadratic twist and changes every odd
exterior-character channel. For even `m`, the factor `(1-u)` in (7) is the
split-infinity factor and cannot be dropped.

The producer imports only the canonical all-degree multi-place JSON at
commit `c94466e28a48ec429150f63de6d334d4c4f60110`, git blob
`f6183be7e06b284f3cc2c3c4a6ffe5b970c0411e`, LF-normalized SHA-256
`b4529c82d40575593e4c346e4cdfa0aaee417618886b5b1ab448c2469c87ca9e`,
and payload SHA-256
`ddd7332102007ceda079e7b85dd0a482642c3d999dac779dde220af4e3b27c7d`.
It does not import the six-place packet, avoiding a second source chain.

The replay checks 112 coefficient pairs, a bounded `USp` table, the four low
cases in (22)--(23) and (29), and the five set partitions of three labels.
The complete payload build, including source and packet-file hashes, fails
closed above four seconds and 32,768 output bytes. No measured time is stored
canonically.

```text
python -B research/l-families/atlas/function_field/quadratic_family_fixed_degree_weight_notch.py --check
python -O -B research/l-families/atlas/function_field/quadratic_family_fixed_degree_weight_notch.py --check
python -B -m pytest -q tests/test_quadratic_family_fixed_degree_weight_notch.py
python -O -B -m pytest -q tests/test_quadratic_family_fixed_degree_weight_notch.py
```

All asymptotics fix `(n,m)` while `q` tends through odd prime powers with
`q >= m`; nothing is uniform in growing degree or mark count. The scales are
Weil upper envelopes, not lower bounds, typical-value laws, or equidistribution
theorems. The curve is a finite-character adapter, not a claimed individual
motive or compatible system. The algebra is standard; no external novelty,
memberwise sign, zero theorem, principal-member amplification, number-field
transfer, RH, or GRH claim is made.
