# Marked two-torsion cubic moment tower

Status: **PROVED** for every odd prime power and every nonnegative even
moment.

This packet closes the all-weight form of the marked-cubic residue that first
appeared in the genus-two `Sym^8` reduction. It uses exact representation
algebra and the standard stack/Eichler--Shimura trace theorem on
`Y_0(2)`. The theorem replay enumerates no field. The only finite census is a
held-out check of 495 candidate cubics over `F_3`, `F_5`, and `F_7`, read after
the symbolic proof and modular-form expansions close.

## 1. Family and theorem

Let `H_3(q)` be the monic squarefree cubics over `F_q`, where `q` is an odd
prime power. For `h` in this family, put

\[
 m_1(h)=\#\{x\in\mathbf F_q:h(x)=0\},
 \qquad
 a_h=-\sum_{x\in\mathbf F_q}\chi(h(x)),
\]

so that `a_h` is the Frobenius trace of `E_h:y^2=h(x)`. Define

\[
 J_{2n}(q)=\sum_{h\in\mathcal H_3(q)}m_1(h)a_h^{2n}.             \tag{1}
\]

For `j>=0`, let

\[
 c(n,j)={2n\choose n-j}-{2n\choose n-j-1},                     \tag{2}
\]

where an out-of-range binomial coefficient is zero. Thus
`c(n,0)=C_n`, the `n`-th Catalan number.

Write `Theta_(k,Gamma0(2))(q)` for the **full cuspidal Frobenius-power
trace** in weight `k` and level two. If `q=p^r`, this is the sum, with all
old/new multiplicities, of

\[
 a_{p^r}(F)-p^{k-1}a_{p^{r-2}}(F)                              \tag{3}
\]

over the underlying normalized newforms, each repeated with its oldform
multiplicity; the second coefficient is zero when `r<2`. Equivalently, it is
the sum of `alpha_(F,p)^r+beta_(F,p)^r`. It is not in
general one Fourier coefficient, and it is not in general the trace of one
newform.

Then for every odd prime power `q` and every `n>=0`,

\[
\boxed{
 {J_{2n}(q)\over q(q-1)}
 =C_nq^n(q-1)
 -\sum_{j=1}^n c(n,j)q^{n-j}
   \left(2+\Theta_{2j+2,\Gamma_0(2)}(q)\right).}                 \tag{4}
\]

Equation (4) is an all-weight identity. The tiny finite rows below are
regressions, not interpolation inputs.

## 2. Exact marked-model bridge

A rational root `r` of `h` determines the nonzero rational two-torsion point
`T=(r,0)` on `E_h`. Conversely, an elliptic curve with a chosen nonzero
rational two-torsion point has a root-marked monic cubic presentation after
choosing an affine coordinate and monic square scaling.

The square-affine model group, with its central `mu_2` retained, has order
`q(q-1)`. Orbit--stabilizer on the model groupoid therefore gives, for every
`n>=0`,

\[
 \boxed{
 J_{2n}(q)=q(q-1)
 \sum_{[(E,T)]}{a_E^{2n}\over
 |\operatorname{Aut}_{\mathbf F_q}(E,T)|},
 \qquad 0\ne T\in E[2](\mathbf F_q).}                           \tag{5}
\]

The stack of pairs `(E,T)` is `Y_1(2)=Y_0(2)` in odd characteristic. The
central involution has not been silently divided out; this is why (5) has
exactly the displayed factor. At `n=0`, (5) gives

\[
 J_0=q(q-1)^2,                                                   \tag{6}
\]

which is also the elementary count of rational roots across squarefree monic
cubics.

The bridge (5), including its normalization, is source-locked to the audited
`Sym^8` packet at commit
`dc63f02d0897e10936ef0767a1c8e6f15ac49e06`, payload
`423b8c37b69fb56b459beb7ebd9e6b94d12cf658f5819f7ac481e83560f5d0ae`.

## 3. The all-`n` `SU(2)` identity

Let

\[
 P_m(a,q)=\operatorname{Tr}(\operatorname{Sym}^m H^1(E)),
 \qquad
 P_0=1,\quad P_1=a,\quad P_m=aP_{m-1}-qP_{m-2}.                 \tag{7}
\]

The Clebsch--Gordan rule, or equivalently the reflection principle for paths
in the dominant `SU(2)` chamber, gives

\[
 \boxed{
 a^{2n}=\sum_{j=0}^n c(n,j)q^{n-j}P_{2j}(a,q).}                 \tag{8}
\]

Indeed, after setting the determinant to one, the multiplicity of
`Sym^(2j)` in the `2n`-fold tensor power of the standard representation is
the difference between all paths ending at `2j` and paths reflected across
the forbidden wall, which is precisely (2). Restoring determinant `q`
contributes `q^(n-j)`. This proves (8) for every `n`; it is not a claim based
on checking finitely many polynomials.

The producer independently rebuilds `P_m` from (7) and verifies (8) in
`Z[a,q]` through `n=12` as a regression certificate. The general identity is
also source-locked to the all-weight genus-one packet at commit
`955ea1e25160075fb4b498018319c80f7e4db9d5`, payload
`183ffb31ae2f5776944e162e59390c40bd7081827b8731246e72e25a882e50df`.

## 4. The `Y_0(2)` character traces

Let `V_m=Sym^m R^1 pi_* Q_l` on `Y_0(2)`. For `m=0`, the stack-weighted
point count is

\[
 \sum_{[(E,T)]}{P_0\over|\operatorname{Aut}(E,T)|}=q-1.         \tag{9}
\]

For every positive even `m`, localization at the two rational cusps and the
Eichler--Shimura identification of interior cohomology give

\[
 \boxed{
 \sum_{[(E,T)]}{P_m(a_E,q)\over|\operatorname{Aut}(E,T)|}
 =-2-\Theta_{m+2,\Gamma_0(2)}(q).}                              \tag{10}
\]

The constant `-2` is the two-cusp boundary contribution. The second term is
the full interior cuspidal trace. This statement is valid for every odd
prime power, including characteristic three; the good-prime
`l`-adic theorem is not subject to a crystalline `p>=m+2` restriction.

Substitution of (9)--(10) into (8), followed by (5), proves (4).

The exact source roles are frozen in the JSON ledger:

1. Behrend's stack Lefschetz theorem supplies the automorphism-weighted trace
   formula.
2. Scholl's good-prime modular Galois representation theorem identifies the
   interior Frobenius trace, including low levels via auxiliary level and
   invariants.
3. Kaplan--Petrow supplies an independent prime-power prescribed-torsion
   trace-formula check.
4. The divisor theorem for `Delta_2=eta(z)^8 eta(2z)^8` supplies the exact
   low-weight level-two space dimensions used below.

## 5. Explicit rows through `n=5`

Put

\[
 f(z)=\eta(z)^8\eta(2z)^8,
 \qquad
 g(z)=f(z)\bigl(2E_2(2z)-E_2(z)\bigr).                          \tag{11}
\]

Write `Theta_f`, `Theta_g`, and `Theta_Delta` for their prime-power
Frobenius traces. Then (4) gives

\[
\begin{aligned}
J_0={}&q(q-1)(q-1),\\
J_2={}&q(q-1)(q^2-q-2),\\
J_4={}&q(q-1)(2q^3-2q^2-6q-2),\\
J_6={}&q(q-1)\bigl(5q^4-5q^3-18q^2-10q-2-\Theta_f(q)\bigr),\\
J_8={}&q(q-1)\bigl(14q^5-14q^4-56q^3-40q^2-14q-2\\
 &\hspace{41mm}-7q\Theta_f(q)-\Theta_g(q)\bigr),\\
J_{10}={}&q(q-1)\bigl(42q^6-42q^5-180q^4-150q^3-70q^2-18q-2\\
 &\hspace{31mm}-35q^2\Theta_f(q)-9q\Theta_g(q)
 -2\Theta_\Delta(q)\bigr).
                                                                    \tag{12}
\end{aligned}
\]

The `J_6` row is exactly the marked-cubic theorem used by the audited
genus-two `Sym^8` packet.

The coefficient arrays in (12) are not hand-fitted. For example,

\[
 (c(4,0),\ldots,c(4,4))=(14,28,20,7,1),
\]

and

\[
 (c(5,0),\ldots,c(5,5))=(42,90,75,35,9,1).                     \tag{13}
\]

## 6. Low-weight cusp spaces: full trace, new trace, and old trace

The form `f` has a simple zero at each of the two cusps and none in the
interior. Multiplication by `f` gives

\[
 M_k(\Gamma_0(2))\simeq S_{k+8}(\Gamma_0(2)).                  \tag{14}
\]

Consequently the relevant low-weight spaces are:

| weight | full dimension | old | new | full trace |
|---:|---:|---:|---:|---|
| 4 | 0 | 0 | 0 | `0` |
| 6 | 0 | 0 | 0 | `0` |
| 8 | 1 | 0 | 1 | `Theta_f` |
| 10 | 1 | 0 | 1 | `Theta_g` |
| 12 | 2 | 2 | 0 | `2 Theta_Delta` |

The weight-ten form in (11) is normalized because
`2E_2(2z)-E_2(z)` has constant term one. Since level one has no cusp form in
weights eight or ten, both `f` and `g` are new.

At weight twelve, `dim S_12(Gamma_0(2))=2`. The two independent degeneracy
images `Delta(z)` and `Delta(2z)` already span a two-dimensional oldspace, so
there is no level-two new summand. At every odd prime they carry two copies of
the same good-prime Galois representation. Therefore

\[
 \boxed{\Theta_{12,\Gamma_0(2)}(q)=2\Theta_\Delta(q).}           \tag{15}
\]

This multiplicity is why the last term of `J_10` is
`-2 Theta_Delta`, not `-Theta_Delta`.

## 7. Independent expansion of the weight-ten form

With `Q=e^(2 pi i z)`, direct truncated-product arithmetic gives

\[
\begin{aligned}
f={}&Q-8Q^2+12Q^3+64Q^4-210Q^5-96Q^6
 +1016Q^7-512Q^8-2043Q^9+O(Q^{10}),\\
2E_2(2z)-E_2(z)={}&1+24Q+24Q^2+96Q^3+24Q^4+144Q^5\\
 &+96Q^6+192Q^7+24Q^8+312Q^9+O(Q^{10}),\\
g={}&Q+16Q^2-156Q^3+256Q^4+870Q^5-2496Q^6\\
 &-952Q^7+4096Q^8+4653Q^9+O(Q^{10}).                 \tag{16}
\end{aligned}
\]

In particular,

\[
 g_3=-156,\qquad g_5=870,\qquad g_7=-952,\qquad g_9=4653.       \tag{17}
\]

For `q=9`, the prime-power convention is load-bearing:

\[
\begin{aligned}
\Theta_f(9)&=-2043-3^7=-4230,\\
\Theta_g(9)&=4653-3^9=-15030,\\
\Theta_\Delta(9)&=-113643-3^{11}=-290790.             \tag{18}
\end{aligned}
\]

The `J_8` theorem therefore gives, without enumerating `F_9`,

\[
 {J_8(9)\over9\cdot8}=972160,
 \qquad
 \boxed{J_8(9)=69995520.}                                      \tag{19}
\]

The same calculation yields the optional higher check
`J_10(9)=2328145920`.

## 8. Held-out prime-field controls

Only after (4), the explicit rows, and (16)--(18) close does the producer
inspect all `3^3+5^3+7^3=495` monic cubic coefficient triples. It rejects a
cubic exactly when its discriminant vanishes, counts rational roots, and
computes the quadratic-character trace directly.

| `q` | candidates | squarefree | observed `J_8` | observed `J_10` |
|---:|---:|---:|---:|---:|
| 3 | 27 | 18 | 1536 | 6144 |
| 5 | 125 | 100 | 668160 | 10536960 |
| 7 | 343 | 294 | 5526528 | 88166400 |

Every value agrees with (12). These rows catch a wrong stack factor, wrong
two-cusp constant, wrong oldform multiplicity, or wrong Fourier coefficient.
They do not prove the all-field theorem.

## 9. Provenance, resources, and interpretation firewall

The JSON source manifest pins both imported packets by commit, Git blob,
LF-normalized SHA-256, and authenticated payload hash. The primary-source
ledger is inherited from the independently audited `Sym^8` packet rather
than reconstructed from memory.

The replay uses exact integer polynomial arithmetic with the following hard
caps:

- 16,384 exact symbolic/Fourier operations;
- 495 candidate cubics;
- 3,000 finite-field point evaluations;
- Fourier degree nine;
- five wall-clock seconds.

No floating point, interpolation, curve database, large field, or exhaustive
extension-field computation is used.

No novelty claim is made for (4), its trace-formula ingredients, or the low
moment rows. This packet makes no RH, GRH, memberwise sign, motive,
compatible-system, or global Euler-product claim. It is an exact
family-moment theorem and a reusable source-locked residual channel.

## Replay

From the repository root:

```text
python research/l-families/atlas/function_field/genus1_marked_2torsion_moment_tower.py --check
python -O research/l-families/atlas/function_field/genus1_marked_2torsion_moment_tower.py --check
python -m unittest tests.test_genus1_marked_2torsion_moment_tower -v
python -O -m unittest tests.test_genus1_marked_2torsion_moment_tower -v
```
