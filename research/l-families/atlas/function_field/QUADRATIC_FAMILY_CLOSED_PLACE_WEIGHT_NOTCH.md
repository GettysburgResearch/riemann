# The closed-place fixed-degree weight notch

Status: **PROVED FROM THE LOCKED ALL-DEGREE EULER QUOTIENT** for every fixed
family degree `n >= 2` and every fixed feasible primitive squarefree
closed-place degree profile over an odd finite field.

This is an exact symbolic extension from rational marked places to arbitrary
closed places. It enumerates no field, irreducible polynomial, curve, inverse
root, zero, or sample.

## Start here

Let

\[
 Q=\prod_{i=1}^r P_i
\tag{1}
\]

be a product of distinct monic irreducibles in \(\mathbf F_q[T]\), with
\(\deg P_i=d_i\) and primitive conductor degree

\[
 M=\deg Q=\sum_i d_i.
\tag{2}
\]

Define the quadratic Dirichlet character

\[
 \psi_Q(F)=\left(\frac{F}{Q}\right)
 =\prod_i\left(\frac{F}{P_i}\right),
\tag{3}
\]

extended by zero when \((F,Q)\ne1\). For the monic squarefree degree-`n`
family put

\[
 S_{n,Q}=
 \sum_{D\in\mathcal H_n(q)}\psi_Q(D),\qquad
 N_n=|\mathcal H_n(q)|=q^{n-1}(q-1).
\tag{4}
\]

The exact squarefree generating series is

\[
\boxed{
 \sum_{D\ {\rm monic\ squarefree}}\psi_Q(D)u^{\deg D}
 =L(u,\psi_Q)\,
 {1-qu^2\over\prod_i(1-u^{2d_i})}.}
\tag{5}
\]

Let

\[
 a_k=[x^k]\prod_i(1-x^{d_i})^{-1},\qquad a_k=0\quad(k<0),
\tag{6}
\]

and write

\[
 P_Q(u)=\sum_jp_ju^j
 =\det(1-\sqrt q\,U_Qu),\qquad
 D_s=p_s-qp_{s-2}.
\tag{7}
\]

Set \(p_j=0\) outside \(0\leq j\leq2g\). The difference \(D_s\) retains its
definition \(D_s=p_s-qp_{s-2}\) for every \(s\geq0\), even when \(p_s=0\);
set \(D_s=0\) by convention for \(s<0\). Then

\[
\boxed{
 S_{n,Q}=\sum_{k=0}^{\lfloor n/2\rfloor}a_kD_{n-2k},
 \qquad M\text{ odd},}
\tag{8}
\]

while

\[
\boxed{
 S_{n,Q}=\sum_{k=0}^{\lfloor n/2\rfloor}
 a_k\bigl(D_{n-2k}-D_{n-1-2k}\bigr),
 \qquad M\text{ even}.}
\tag{9}
\]

Because \(a_0=1\), the unique weight-\(n/2\) channel in either parity is

\[
\boxed{
 D_n=p_n-qp_{n-2}
 =(-1)^nq^{n/2}\bigl(e_n(U_Q)-e_{n-2}(U_Q)\bigr).}
\tag{10}
\]

The interior top-weight notch occurs at primitive conductor degree

\[
\boxed{M=2n-1\quad\text{or}\quad M=2n.}
\tag{11}
\]

At the odd notch, a primitive irreducible conductor gives
\(S_{n,Q}=0\) exactly. At the even notch, every degree profile retains the
same profile-independent half-weight channel
\[
(-1)^nq^{(n-1)/2}\chi_{\omega_{n-1}}.
\]

## 1. Euler quotient and the exact curve adapter

Multiplicativity gives

\[
\begin{aligned}
 \sum_{D\ {\rm monic\ squarefree}}\psi_Q(D)u^{\deg D}
 &=\prod_R\left(1+\psi_Q(R)u^{\deg R}\right)\\
 &={L(u,\psi_Q)\over L(u^2,\psi_Q^2)}.
\end{aligned}
\tag{12}
\]

The square \(\psi_Q^2\) is the indicator of coprimality with `Q`, so

\[
 L(u^2,\psi_Q^2)
 ={\prod_i(1-u^{2d_i})\over1-qu^2}.
\tag{13}
\]

Equations (12)--(13) prove (5). When every \(d_i=1\), (13) has denominator
\((1-u^2)^r\), and

\[
 a_k=\binom{r+k-1}{k},
\tag{14}
\]

recovering the locked rational-place identity exactly.

The reciprocity and infinity convention is equally important. Put

\[
 G=(-1)^M Q,\qquad C_Q:y^2=G.
\tag{15}
\]

For every finite prime `R`, polynomial quadratic reciprocity gives

\[
 \left(\frac{R}{Q}\right)=\left(\frac{G}{R}\right).
\tag{16}
\]

Thus \(C_Q\) is the exact finite-character adapter, with genus

\[
 g=\left\lfloor{M-1\over2}\right\rfloor.
\tag{17}
\]

If `M` is odd, infinity ramifies and
\(L(u,\psi_Q)=P_Q(u)\). If `M` is even, `G` is monic with split infinity and

\[
 L(u,\psi_Q)=(1-u)P_Q(u).
\tag{18}
\]

At odd `M`, silently replacing `G` by the monic polynomial `Q` can be the
nontrivial quadratic twist when `-1` is nonsquare; it changes every odd
exterior-character channel.

## 2. Degree-profile coefficients and exact regrouping

Set

\[
 b_k=a_k-qa_{k-1}.
\tag{19}
\]

The coefficient form of (5) is

\[
 S_{n,Q}=
 \sum_{\substack{0\leq j\leq n\\n-j\ {\rm even}}}
 \ell_jb_{(n-j)/2},
\tag{20}
\]

where \(L(u,\psi_Q)=\sum_j\ell_ju^j\). Pairing the two terms in (19) proves
(8) when `M` is odd. For even `M`, the split-infinity identity
\(\ell_j=p_j-p_{j-1}\) proves (9).

The profile coefficients count weighted partitions:

\[
 a_k=\#\left\{(c_1,\ldots,c_r)\in\mathbf Z_{\geq0}^r:
 \sum_i c_id_i=k\right\}.
\tag{21}
\]

For example,

\[
\begin{array}{c|rrrrrrr}
(d_i)&a_0&a_1&a_2&a_3&a_4&a_5&a_6\\ \hline
(1,2)&1&1&2&2&3&3&4\\
(2,3)&1&0&1&1&1&1&2.
\end{array}
\tag{22}
\]

Each \(D_s\) has weight at most `s/2`. Hence (10) is the sole
\(q^{n/2}\) channel; the even-parity term \(-D_{n-1}\) has only half a weight
less. The producer compares the original and regrouped \(p_j\)-coefficient
arrays for all family degrees `2 <= n <= 7` and all 138 integer degree
profiles of total degree at most ten. This bounded table is a replay of the
index shift, not evidence by interpolation.

## 3. The primitive-conductor notch

At both degrees in (11), equation (17) gives \(g=n-1\), hence
\(e_n=e_{n-2}\) and \(D_n=0\).

### Odd conductor degree \(M=2n-1\)

Equation (8) becomes

\[
\boxed{
 S_{n,Q}=\sum_{k=1}^{\lfloor n/2\rfloor}a_kD_{n-2k}.}
\tag{23}
\]

Let \(h=\min_i d_i\). From (21),

\[
 a_k=0\quad(1\leq k<h),\qquad
 a_h=\#\{i:d_i=h\}.
\tag{24}
\]

If \(h\leq\lfloor n/2\rfloor\), the first possible residual is

\[
 a_hD_{n-2h}
 =a_h(-1)^nq^{(n-2h)/2}\chi_{\omega_{n-2h}},
\tag{25}
\]

and therefore, for the fixed profile,

\[
 \mu_{n,Q}:={S_{n,Q}\over N_n}
 =O_{n,(d_i)}\!\left(q^{-(n+2h)/2}\right).
\tag{26}
\]

If instead

\[
 \boxed{h>\lfloor n/2\rfloor,}
\tag{27}
\]

every coefficient in (23) vanishes, so

\[
\boxed{S_{n,Q}=0}
\tag{28}
\]

exactly. In particular, the one-factor profile `(2n-1)` satisfies (27):
every primitive irreducible conductor of odd notch degree has exact zero raw
family sum.

This zero is a coefficient-support theorem. It does not imply a zero
connected cumulant, a zero of an individual \(L\)-function, or special
zero statistics.

### Even conductor degree \(M=2n\)

Equation (9) becomes

\[
\boxed{
 S_{n,Q}=-D_{n-1}
 +\sum_{k=1}^{\lfloor n/2\rfloor}
 a_k\bigl(D_{n-2k}-D_{n-1-2k}\bigr).}
\tag{29}
\]

The unique leading residual is independent of the profile:

\[
\boxed{
 -D_{n-1}=(-1)^nq^{(n-1)/2}\chi_{\omega_{n-1}}.}
\tag{30}
\]

All profile-dependent terms have weight at most `(n-2)/2`, so

\[
 \mu_{n,Q}=O_{n,(d_i)}\!\left(q^{-(n+1)/2}\right).
\tag{31}
\]

For `n=5`, the rational profiles recover

\[
 S_{5,(1^9)}
 =-9q^{3/2}\chi_{\omega_3}-45q^{1/2}\chi_{\omega_1},
\tag{32}
\]

\[
\begin{aligned}
 S_{5,(1^{10})}={}&-q^2\chi_{\omega_4}
 -10q^{3/2}\chi_{\omega_3}-10q\chi_{\omega_2}\\
 &-55q^{1/2}\chi_{\omega_1}-55.
\end{aligned}
\tag{33}
\]

The irreducible profiles give the sharper pair

\[
 S_{5,(9)}=0,\qquad S_{5,(10)}=-q^2\chi_{\omega_4}.
\tag{34}
\]

Mixed profiles retain only the channels allowed by their coefficient
support. For instance,

\[
 S_{5,(2,7)}=-q^{1/2}\chi_{\omega_1},
\tag{35}
\]

and

\[
 S_{5,(2,8)}
 =-q^2\chi_{\omega_4}-q^{1/2}\chi_{\omega_1}-1.
\tag{36}
\]

## 4. Normalization and connected correction

For a labelled collection of closed places, put
\(X_i(D)=(D/P_i)\). Every nonempty fixed subprofile satisfies the same coarse
Weil envelope

\[
 \mathbf E\!\left[\prod_{i\in B}X_i\right]
 =O_{n,(d_i)}(q^{-n/2}).
\tag{37}
\]

Unlike the odd-degree rational-place control, a general closed-place
singleton mean need not vanish. Retaining all singleton-containing
partitions, every proper partition still has at least two blocks. Hence

\[
\boxed{
 \kappa_{n,Q}-\mu_{n,Q}
 =O_{n,(d_i)}(q^{-n}).}
\tag{38}
\]

At the even notch, this is below the half-weight envelope (31) for every
`n >= 2`. At the odd notch, the relationship depends on `h`; when (28)
holds, the full connected correlation can still be
\(O_{n,(d_i)}(q^{-n})\) through proper-subprofile terms. Exact raw zero must
not be promoted to exact connected zero.

## 5. Primitive-conductor and fixed-\(q\) firewalls

The notch is controlled by the degree of the actual primitive conductor.
This packet accepts only declared distinct irreducibles with exponent one.
It refuses a nonsquarefree or imprimitive formal modulus. Although its odd
exponent support identifies the inducing quadratic character, removed
even-exponent factors still leave imprimitive Euler deletions and zero
conditions. They cannot simply be discarded inside (5). A separate
imprimitive identity is required; the formal modulus degree must never be
substituted for `M` in the notch formula.

At fixed `q`, a symbolic profile is realizable only when enough distinct
closed places exist. If `c_d` is the multiplicity of degree `d`, then

\[
\boxed{
 c_d\leq I_q(d),\qquad
 I_q(d)={1\over d}\sum_{e\mid d}\mu(e)q^{d/e}.}
\tag{39}
\]

This formula is evaluated arithmetically; no irreducibles are listed. The
rational-place constraint is the special case \(I_q(1)=q\). Thus `q >= r`
is not the general closed-place feasibility criterion.

All asymptotics in this packet fix `n` and the complete degree profile while
`q` varies through feasible odd prime powers. They are not uniform for a
profile or rank growing with `q`, and fixed `q` never supports an arbitrary
number of factors of any prescribed degree.

## 6. Primary-literature boundary

The arithmetic ingredients of this packet are established. Florea's
[Lemma 2.2](https://arxiv.org/abs/1505.03094) prints the squarefree-character
Euler quotient with the full product over prime divisors of an arbitrary
conductor. Keating--Rudnick give the general quotient
`L(u,chi)/L(u^2,chi^2)` in
[equation (9.7)](https://arxiv.org/html/1504.03444#S9.E7). The completion,
functional equation, and split-infinity factor are standard; see
[Andrade--Bae--Jung, Section 2.1.1](https://link.springer.com/article/10.1186/s40687-016-0087-4).
The primitive-exterior decomposition used at the notch is the symplectic
Lefschetz decomposition in
[Goodman--Wallach, Theorem 16.3 and Corollary 16.4](https://sites.math.rutgers.edu/~goodman/pub/hklect.pdf).
Exact squarefree correlation and Poisson formulas in this family also appear
in [Bui--Florea--Keating, Lemmas 2.1--2.2](https://arxiv.org/abs/2001.03265).

Accordingly, neither the Euler quotient, its arbitrary degree-profile
denominator, the infinity factor, nor the symplectic cancellation is claimed
new. The irreducible degree-`2n-1` raw zero is a short corollary of those
known identities and is best treated as likely folklore unless a specialist
search establishes otherwise. The contribution here is the unified
degree-profile/layer packaging, its exact support criterion, the odd/even
boundary comparison, and its alignment with the atlas detector mechanisms.

## 7. Source lock, resources, and claim boundary

The packet imports only the canonical all-degree rational-place JSON at
commit `c94466e28a48ec429150f63de6d334d4c4f60110`, git blob
`f6183be7e06b284f3cc2c3c4a6ffe5b970c0411e`, LF-normalized SHA-256
`b4529c82d40575593e4c346e4cdfa0aaee417618886b5b1ab448c2469c87ca9e`,
and payload SHA-256
`ddd7332102007ceda079e7b85dd0a482642c3d999dac779dde220af4e3b27c7d`.
It does not import either later weight-notch packet.

The replay uses 138 small integer profiles, 828 coefficient comparisons, 200
reciprocity-parity checks, and bounded `n=2,...,5` notch controls. The payload
build, including source and
packet-file hashing, fails closed above four seconds and 32,768 output bytes.
It performs no field, irreducible, polynomial-family, curve, root, zero, or
sampling enumeration and uses no floating-point arithmetic.

```text
python -B research/l-families/atlas/function_field/quadratic_family_closed_place_weight_notch.py --check
python -O -B research/l-families/atlas/function_field/quadratic_family_closed_place_weight_notch.py --check
python -B -m pytest -q tests/test_quadratic_family_closed_place_weight_notch.py
python -O -B -m pytest -q tests/test_quadratic_family_closed_place_weight_notch.py
```

The Euler quotient, reciprocity adapter, infinity factor, and exterior
character algebra are standard; no external novelty claim is made. The curve
is a finite-character adapter, not a claimed individual motive or compatible
system. Nothing here proves a memberwise sign, zero theorem, principal-member
amplification, number-field transfer, RH, or GRH.
