# Reflection at every source cusp with the translation denominator preserved

Status: proposed reviewable theorem, conditional on the exact theta automorphy, invariances and three cusp expansions imported in the October 5 primary source. This file supplies the geometric and analytic adapter needed to apply the second reflection to every cusp term of the coupled completion. Independent review of this new adapter is required; its author does not supply that review.

Scope: each of the three source cusp sequences, every finite periodic Fourier multiplier, and the exact inherited reflected weight. The result is an exact support identity for completed theta sums. It does not bound a sum after deleting its cube completion, a separately truncated frequency block, or the complete fourth moment.

Exact dependencies: OpenAI/math commit `adc7f1241b42e322a6451854ab7e4b4c146bf78a`, October 5 `paper2.tex`, physically retained in the October 7 import. The inputs are the automorphy law for matrices congruent to the identity modulo 3; invariance under `SL_2(Z)` and translations by `Z+3O`; the three expansions `eq:cusp-coefficient-definition`; their bounds in `lem:theta-bounds`; the coordinate identity `eq:theta-cusp-coordinates`; and the weight `eq:theta-weight`. The preceding coupled identity is PR #915 at `9959364671f89b86f3992ec5ed5e19f804eb607b`, `COUPLED_THETA_COMPLETION.md`, Sections 1–3. The opposite derivative and standard face are independently developed in [OPPOSITE_DERIVATIVE_REFLECTION.md](OPPOSITE_DERIVATIVE_REFLECTION.md).

What was actually run: a direct matrix construction, reconstruction of its coordinate derivative and Mellin functional equation, and an exact support calculation. No finite computation or numerical cancellation is used to justify the analytic identity.

Smallest remaining gap for the full target: the theorem preserves the completed theta sum. Quantitative control of the surviving divisor groups and removal of completion remain separate problems.

## 1. The source functions and the periodic multiplier

Put `O=Z[omega]`, `lambda=1+2omega=i sqrt(3)`, `N(z)=|z|^2`, and `alpha(z)=z/|z|` for nonzero z. Write

\[
\gamma_0=I,\qquad
\gamma_+=\begin{pmatrix}1&0\\\omega&1\end{pmatrix},\qquad
\gamma_-=\begin{pmatrix}1&0\\\omega^2&1\end{pmatrix},
\qquad f_\sigma(w)=\overline{\theta(\gamma_\sigma w)}.
\tag{1.1}
\]

The imported expansion is

\[
f_\sigma(z,v)=a_\sigma v^{2/3}
 +\sum_{0\ne\ell\in\lambda^{-4}O}
 d_\sigma(\ell)vK_{1/3}(4\pi|\ell|v)\breve e(\ell z),
\qquad
a_\sigma=\frac{3^{5/2}}2\mathbf1_{\sigma=0}.
\tag{1.2}
\]

Here `breve e(z)=exp(2*pi*i*(z+bar(z)))` and `e(z)=breve e(z/lambda)`. The coefficient bounds in the source imply absolute convergence of

\[
\sum_{\ell\ne0}|d_\sigma(\ell)|(N\ell)^{-s}
\quad\text{for}\quad \Re s>1,
\tag{1.3}
\]

for all three sigma. Indeed the source support `ell=u lambda^m n b^3`, with `m>=-4`, and bound `|d_sigma(ell)|<=27*3^(m/6)*sqrt(Nb)` reduce the majorant to convergent sums in m, squarefree n, and b on that half-plane. The common frequency lattice also gives

\[
N\ell\ge\frac1{81}\qquad(0\ne\ell\in\lambda^{-4}O).
\tag{1.4}
\]

Let q be any nonzero element of O, and let `F:O->C` be periodic modulo `(q)`. Its finite Fourier coefficients are

\[
\widehat F_q(h)=\frac1{Nq}\sum_{x\bmod q}F(x)e(-hx/q),
\qquad h\in O/(q).
\tag{1.5}
\]

Define the twist by retaining the nonzero frequencies:

\[
\Theta_{\sigma,F}(z,v)=\sum_{\ell\ne0}
d_\sigma(\ell)F(\lambda^4\ell)
vK_{1/3}(4\pi|\ell|v)\breve e(\ell z).
\tag{1.6}
\]

Finite Fourier inversion gives the exact relation

\[
\Theta_{\sigma,F}(z,v)=
\sum_{h\bmod q}\widehat F_q(h)
f_\sigma(z+\beta_h,v)-a_\sigma F(0)v^{2/3},
\qquad \beta_h=\lambda^3h/q.
\tag{1.7}
\]

The power `lambda^3` follows from `e(lambda^4 ell h/q)=breve e(ell lambda^3 h/q)`. The possible constant correction in (1.7) is retained explicitly. Either horizontal derivative removes it.

## 2. A matrix construction that preserves the denominator

### Lemma 2.1

Fix `sigma in {0,+,-}` and a finite rational point `beta in K`. Write `beta=a/c` in lowest terms with `a,c in O`, `c!=0`. There is a matrix

\[
g=\begin{pmatrix}a&b\\c&\delta\end{pmatrix}\in\mathrm{SL}_2(O),
\tag{2.1}
\]

after a possible common unit change of a and c, together with a matrix `g_1` congruent to the identity modulo 3, a cusp `tau in {0,+,-}`, and a scalar `kappa=kappa(g_1)` of modulus one, such that

\[
f_\sigma(gw)=\overline\kappa\,f_\tau(w).
\tag{2.2}
\]

If `beta=lambda^3 h/q`, then the c in this identity divides q up to a unit. In particular,

\[
Nc\le Nq.
\tag{2.3}
\]

The c in (2.3) is the reduced denominator of the original translation beta. It is not replaced by the reduced denominator of `gamma_sigma(beta)`.

**Proof.** Start with a primitive column `(a,c)^t` for beta and put

\[
\binom AC=\gamma_\sigma\binom ac.
\tag{2.4}
\]

The column `(A,C)^t` is primitive, since `gamma_sigma` is an integral matrix of determinant one. The six units of O represent all six elements of `(O/(3))^times`. Hence a common unit change of both columns makes `A=1 mod3` when `lambda|C`, or makes `C=1 mod3` when `lambda` does not divide C.

We now choose the second column of an integral determinant-one matrix `G=(A B; C D)`. This choice is made before defining g.

If `C!=0` and `lambda|C`, choose D with `AD=1 mod(3C)` and put `B=(AD-1)/C`. This is possible because `(A,3C)=1`. Then

\[
B\equiv0\pmod3,\qquad D\equiv1\pmod3.
\tag{2.5}
\]

If `lambda` does not divide C, choose D by the compatible congruences

\[
D\equiv0\pmod3,\qquad AD\equiv1\pmod C,
\tag{2.6}
\]

and again put `B=(AD-1)/C`. Since `C=1 mod3`, this gives `B=-1 mod3`. The congruence modulo C is vacuous when C is a unit, which causes no difficulty. If `C=0`, primitivity makes A a unit; normalize it to A=1 and take `G=I`.

Write

\[
T_u=\begin{pmatrix}1&u\\0&1\end{pmatrix},\qquad
L_u=\begin{pmatrix}1&0\\u&1\end{pmatrix},\qquad
J=\begin{pmatrix}0&-1\\1&0\end{pmatrix}.
\]

The congruences just imposed give a factorization `G=g_1 H`, with `g_1=GH^(-1)=I mod3`, by taking

\[
H=\begin{cases}
I,&3\mid C,\text{ including }C=0,\\
L_{u_0},&v_\lambda(C)=1,
\quad u_0\in\{\lambda,-\lambda\},\ u_0\equiv C\pmod3,\\
T_uJ,&\lambda\nmid C,
\quad u\equiv A\pmod3
\text{ from a fixed set of representatives}.
\end{cases}
\tag{2.7}
\]

For example, in the last case `G mod3=(A -1; 1 0)`, exactly the residue of `T_u J`. These are the same finite H types used in the primary source, rather than an unspecified family of new cusp matrices.

Each `overline(theta(Hw))` reduces exactly to one of the three functions in (1.1). To see this directly, set `Lambda=Z+3O`. The source invariances under `SL_2(Z)` and under `T_v`, `v in Lambda`, together with

\[
L_u=J^{-1}T_{-u}J,
\tag{2.8}
\]

show that `overline(theta(L_u w))` is unchanged when u is changed by an element of Lambda. Also

\[
\overline{\theta(T_uJw)}=
\overline{\theta(J^{-1}T_uJw)}
=\overline{\theta(L_{-u}w)}.
\tag{2.9}
\]

The quotient `O/Lambda` has representatives `0,omega,-omega`. The first two give `gamma_0` and `gamma_+`; the third gives `gamma_-`, since `-omega=1+omega^2` differs from `omega^2` by an integer. This also treats `L_(+lambda)` and `L_(-lambda)`: their parameters are congruent modulo Lambda to `-omega` and `omega`, respectively. Thus a tau in the prescribed three-element set satisfies

\[
\overline{\theta(Hw)}=f_\tau(w).
\tag{2.10}
\]

Finally define the required matrix by

\[
\boxed{g=\gamma_\sigma^{-1}G.}
\tag{2.11}
\]

Its first column is the unit-normalized original `(a,c)^t`, not the transformed column `(A,C)^t`. Automorphy gives

\[
f_\sigma(gw)=\overline{\theta(Gw)}
=\overline{\kappa(g_1)}\,\overline{\theta(Hw)}
=\overline\kappa f_\tau(w).
\]

For `beta=lambda^3h/q`, reducing the fraction cancels a divisor from q, so the original denominator c divides q up to a unit. The common unit normalization does not change its norm. This proves every assertion. QED.

The lower-right entry delta of g in Lemma 2.1 need not be the lower-right entry D of G. Keeping this distinction is necessary in the additive phase and in the coordinate formula below.

## 3. The opposite derivative and the analytic domain

Apply Lemma 2.1 to every beta_h in (1.7), and write its data as `g_h`, `c_h`, `delta_h`, `kappa_h`, and `tau_h`. The source coordinate formula, applied to g_h itself, gives

\[
g_h^{-1}(z+\beta_h,v)=
\left(-\frac{\delta_h}{c_h}
 -\frac{\bar z}{c_h^2(v^2+|z|^2)},
 \frac{v}{Nc_h(v^2+|z|^2)}\right).
\tag{3.1}
\]

At z=0, the derivatives of its coordinates satisfy

\[
\partial_z z'=0,\qquad
\partial_z\bar z'=-\frac1{\bar c_h^2v^2},\qquad
\partial_zv'=0.
\tag{3.2}
\]

Hence

\[
\left.\partial_z f_\sigma(z+\beta_h,v)\right|_{z=0}
=-\overline{\kappa_h}(\bar c_h v)^{-2}
\left.\partial_{\bar z'}f_{\tau_h}(z',v')
\right|_{z'=-\delta_h/c_h,\ v'=1/(Nc_hv)}.
\tag{3.3}
\]

There is no height derivative. In particular the constant term of every cusp disappears on both sides, even if `F(0)!=0` in (1.7).

For `Re(s)>1`, put

\[
D^+_{\sigma,F}(s)=\sum_{\ell\ne0}
d_\sigma(\ell)F(\lambda^4\ell)\alpha(\ell)(N\ell)^{-s},
\tag{3.4}
\]

and

\[
D^-_h(s)=\sum_{\ell\ne0}
d_{\tau_h}(\ell)\overline{\alpha(\ell)}
\breve e(-\delta_h\ell/c_h)(N\ell)^{-s}.
\tag{3.5}
\]

All these series converge absolutely on that half-plane by (1.3). The derivative Bessel integral is identical at all three cusps, so

\[
\begin{split}
J^+_{\sigma,F}(s)
&:=\int_0^\infty
\left.\partial_z\Theta_{\sigma,F}(z,v)\right|_{z=0}
v^{2s-1}\,dv\\
&=\frac{i\,\Gamma(s+1/3)\Gamma(s+2/3)}
 {4(2\pi)^{2s}}D^+_{\sigma,F}(s).
\end{split}
\tag{3.6}
\]

At infinity, the differentiated expansion decays exponentially. At zero, (3.3) expresses every term as a polynomial factor times an exponentially decaying series at height `1/(Nc_h v)`. Thus (3.6) defines an entire J, and division by its gamma factors continues D to an entire function. The same statement holds for each translated opposite derivative in (3.5), using Lemma 2.1 at its rational translation.

Define

\[
\mathcal R(t)=
\frac{\Gamma(7/6+t)\Gamma(5/6+t)}
 {\Gamma(7/6-t)\Gamma(5/6-t)}.
\tag{3.7}
\]

Substituting `v -> 1/(Nc_h v)` in (3.3) and using (3.6) gives the exact meromorphic identity, and hence its entire continuation where removable factors occur,

\[
\boxed{
\begin{split}
D^+_{\sigma,F}(1/2+t)
=-\sum_{h\bmod q}&\widehat F_q(h)
\overline{\kappa_h}\alpha(c_h)^2
(Nc_h)^{-2t}(2\pi)^{4t}\mathcal R(t)^{-1}
D^-_h(1/2-t).
\end{split}}
\tag{3.8}
\]

The norm in this formula is the norm of c_h, whose upper bound is (2.3). No norm of the transformed denominator C enters it.

For clarity, the contour argument below needs polynomial growth of D in the fixed strip `-1/4<=Re(s)<=5/4`. The series gives a bounded right boundary. Equation (3.8), absolute convergence of (3.5), and Stirling give a polynomial left boundary. The entire Mellin integral is uniformly bounded on closed vertical strips before division by gamma factors; division gives at most an exponential bound in `|Im(s)|`. The usual Phragmen–Lindelof strip argument therefore yields a polynomial bound between the boundaries, exactly as in the primary source. One can apply the maximum principle to D divided by a sufficiently large polynomial without zeros in the strip and multiplied by `exp(epsilon*s^2)`, then let epsilon decrease to zero. Constants may depend on the fixed q and F; the support conclusion will not require a uniform estimate for those constants.

## 4. Exact return to compact support at every cusp

Fix `V in C_c^infinity((0,infinity))` with `supp(V) subset [u,R]`, where `0<u<R`. Its inherited weight is

\[
V^\sharp(x)=\frac1{2\pi i}\int_{(0)}
\widehat V(-t)\mathcal R(t)
\left(\frac{(2\pi)^4x}{27}\right)^{-t}dt.
\tag{4.1}
\]

On `Re(t)>-5/6`, its Mellin transform is

\[
\widehat{V^\sharp}(t)=
\widehat V(-t)\mathcal R(t)
\left(\frac{(2\pi)^4}{27}\right)^{-t}.
\tag{4.2}
\]

The first numerator gamma pole in (4.2) is at `t=-5/6`; shifting (4.1) to any line strictly to its right proves the corresponding positive-power estimate at zero. At infinity the weight decays faster than any power. These bounds and Mellin uniqueness prove (4.2) on the stated half-plane. The smooth compact support of V gives rapid vertical decay on every closed substrip used here.

Set

\[
\mathcal S_{\sigma,F}(X)=
\sum_{\ell\ne0}
\frac{d_\sigma(\ell)F(\lambda^4\ell)\alpha(\ell)}{\sqrt{N\ell}}
V^\sharp(N\ell/X),\qquad X>0.
\tag{4.3}
\]

### Theorem 4.1

For every sigma, q, F, V and X specified above,

\[
\boxed{
\begin{split}
\mathcal S_{\sigma,F}(X)
=-\sum_{h\bmod q}&\widehat F_q(h)
\overline{\kappa_h}\alpha(c_h)^2
\sum_{\ell'\ne0}
\frac{d_{\tau_h}(\ell')\overline{\alpha(\ell')}}{\sqrt{N\ell'}}
\breve e(-\delta_h\ell'/c_h)
V\!\left(\frac{27N\ell'X}{(Nc_h)^2}\right).
\end{split}}
\tag{4.4}
\]

Every inner sum on the right is finite. In particular,

\[
\boxed{X>3R(Nq)^2\quad\Longrightarrow\quad
\mathcal S_{\sigma,F}(X)=0.}
\tag{4.5}
\]

**Proof.** Mellin-invert (4.3) on `Re(t)=3/4`, where `D^+(1/2+t)` is absolutely convergent. Move the line to `Re(t)=-3/4`. The D factor is entire and polynomially bounded on the intervening strip by Section 3. The weight transform is holomorphic there because `-3/4>-5/6`, and decays rapidly on vertical lines. No poles or constant-mode residues occur.

Insert (3.8), replace t by -t, and insert the absolutely convergent dual series (3.5) on the resulting line `Re(t)=3/4`. The weight in each dual term has Mellin coefficient

\[
\widehat{V^\sharp}(-t)\mathcal R(t)(2\pi)^{-4t}
=\widehat V(t)\,27^{-t},
\tag{4.6}
\]

because `R(t)R(-t)=1`. Mellin inversion gives `V(27x)`, proving (4.4). In particular the return weight is exactly the compact V, with the factor 27 retained.

By (1.4) and (2.3), each argument of V in (4.4) is at least

\[
\frac{27(1/81)X}{(Nq)^2}
=\frac{X}{3(Nq)^2}.
\tag{4.7}
\]

It is greater than R under (4.5), so every term is zero. Compact support also makes each dual frequency sum finite for general X. This proves the theorem. QED.

The number of h can grow with Nq. The vanishing condition holds before their values are summed, so no estimate for this number, Fourier coefficients, or an average over denominators is needed. The theorem makes no claim that an individual truncated block on the left vanishes.

## 5. The exact Ramanujan consequence

The source coupled reflection has, at the divisor primes of a squarefree a,

\[
\prod_{p\mid a}B_{p,4}(x)
=\frac1{\sqrt{Na}}
\prod_{p\mid a}(-1+Np\,\mathbf1_{p\mid x})
=\frac1{\sqrt{Na}}
\sum_{dg=a}\mu_K(g)Nd\,\mathbf1_{d\mid x}.
\tag{5.1}
\]

The two factors d and g are squarefree and coprime because a is squarefree. This is an algebraic expansion; the negative summand does not impose coprimality of g and x.

Fix one source cusp term, including its fixed bad factor c_0 and additive character psi. Choose a fixed S-supported M divisible by a period of every psi in the finite source family. For a squarefree row k coprime to a and outside S, the grouped term indexed by `dg=a` has the periodic multiplier

\[
F_{k,d}(x)=\psi(x)\chi_k(x)^3\mathbf1_{d\mid x},
\qquad q=Mkd,
\tag{5.2}
\]

including the literal zeros at every prime of k. Its inherited raw norm scale is

\[
X=\frac{(Nc_0)^2(Nk)^2(Na)^2}{B}.
\tag{5.3}
\]

The coefficients outside the frequency sum, including `mu_K(g)Nd/sqrt(Na)` and the original angular and row factors, have no effect on the support calculation. Equations (5.2)–(5.3) give exactly

\[
\frac{X}{(Nq)^2}
=\frac{(Nc_0)^2(Ng)^2}{B(NM)^2}.
\tag{5.4}
\]

Consequently Theorem 4.1 proves, at each of the three source cusps,

\[
\boxed{
(Ng)^2>\frac{3R(NM)^2}{(Nc_0)^2}\,B
\quad\Longrightarrow\quad
\text{the complete grouped frequency sum indexed by }(d,g)\text{ is zero}.}
\tag{5.5}
\]

There are finitely many nonzero c_0, so taking the maximum of the displayed constants gives a cutoff independent of a, k, d, g and the source cusp term. In particular the complete all-negative summand `d=1, g=a` vanishes when `(Na)^2` exceeds this fixed multiple of B.

The condition must be used on the full completed grouped frequency sum. Subdividing it by a squarefree index, cube index, ramified valuation, or a frequency dyad before taking absolute values can destroy this exact cancellation. Reuniting all terms of (5.1) also restores the original active local Fourier factors; (5.5) does not claim that the conductor of the reunited theta sum is smaller.
