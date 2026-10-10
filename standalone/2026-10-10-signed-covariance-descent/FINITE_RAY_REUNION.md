# The actual finite rays reunite: cancellation of the apparent divisor pole

**Status:** proposed source-conditional theorem. This note evaluates the
actual fixed Fourier data left unevaluated in PR #920. It proves that
reuniting those data forces the single divisor character
`kappa = eta rho^3`. Consequently the apparent pole at `v=1` and the
additional finite-character reciprocal poles in the previous reflected
representation are removable. It does not prove a higher moment.

**Authorship:** finite_ray_residue. Independent review must be recorded
separately against the exact frozen content.

**Exact dependencies:** PR #920 mathematical source
`6aceafc1729ca0962eb12519b407b69c3b5a4d5f`, especially
`POST_REFLECTION_EULER_CONTINUATION.md`, equations (1.4), (2.10),
(2.11), (2.13), (2.14), and (3.6). The primitive finite-ray input is
OpenAI/math `adc7f1241b42e322a6451854ab7e4b4c146bf78a`, October 5
`paper2.tex`, Appendix `app:fixed-ray`: its finite Fourier expansion,
reduced-denominator construction, `eq:ray-multiplier`, and
`eq:ray-additive-crt`. The three cusp expansions and coefficient bounds
are also retained with their original normalization. No zero-free
theorem is needed for the new continuation below.

**What was actually run:** the exact finite covariance is proved in
Sections 2–4. Any finite diagnostics or independent reproduction are to
be recorded separately; they are not substitutes for this proof.

**Smallest remaining gap for the requested moments:** the normally
convergent dual theta estimate still supplies no saving at the critical
balanced scales. Section 7 computes that obstruction explicitly.

## 1. The complete object and the actual fixed multiplier

Use the notation of the cited PR #920 note. Thus
`O = Z[omega]`, `lambda = 1+2omega`, `alpha(a)=a/|a|`, and all varying
squarefree elements are the chosen primary generators. The fixed bad
set S contains the primes over 2 and 3 and the finite ray conductors.
Let k be squarefree and coprime to S and put `Q=Nk`. Let eta and rho
be the fixed finite ray characters. Define

\[
\begin{gathered}
\chi^-_k=\eta\overline\alpha^{\,3}\chi_k^3,
\qquad \kappa=\eta\rho^3,
\qquad v=w+3s-\tfrac32,\\
x_p=\chi^-_k(p)(Np)^{-w},\qquad
z_p=\kappa(p)(Np)^{-v},\qquad
D_p=1-x_p+z_p.
\end{gathered}
\tag{1.1}
\]

All good-prime products omit kS literally. The initial completed
divisor identity is

\[
\mathscr R_k(w,s)=P_k(w,v)
\sum_{(d,kS)=1}^{*}
\frac{\mathfrak a_k(d)}{(Nd)^s}
\prod_{p\mid d}\frac{Np\,x_p}{D_p}\,
\mathcal T_{k,d}(s),
\tag{1.2}
\]

where

\[
\begin{gathered}
\mathfrak a_k(d)=\gamma_2(d)\rho(d)\vartheta(d)
                 \alpha(d)\chi_k(d)^3,
\qquad \vartheta(d)=\chi_d(\lambda)^{-2},\\
P_k(w,v)=\frac{L_{S,k}(v,\kappa)}{L_{S,k}(w,\chi^-_k)}
                  \mathcal E_{k,1}(w,v),
\qquad
\mathcal E_{k,1,p}=\frac{D_p(1-z_p)}{1-x_p}.
\end{gathered}
\tag{1.3}
\]

The theta twist has good-prime exponent 3 at k and exponent 4 at d.
Its **actual** fixed periodic multiplier is

\[
\phi_\rho(x)=
\begin{cases}
\rho(x),&x\equiv1\pmod3,\ (x,S)=1,\\
0,&\text{otherwise}.
\end{cases}
\tag{1.4}
\]

The supplementary factor in the source definition of the multiplier
cancels the factor vartheta in the theta coefficient. Choose a fixed
S-supported period L for (1.4), including the source's required powers
above 2 and 3. Its Fourier coefficients are

\[
\widehat\phi_\rho(h)=\frac1{NL}
\sum_{x\bmod L}\phi_\rho(x)e(-hx/L).
\tag{1.5}
\]

The source retains these coefficients; replacing them by independent
arbitrary weights destroys the covariance proved next.

## 2. Fourier covariance under primary square scaling

### Lemma 2.1

For every primary d coprime to S and every `h mod L`,

\[
\boxed{\widehat\phi_\rho(d^{-2}h)=\rho(d)^2\widehat\phi_\rho(h).}
\tag{2.1}
\]

The inverse is taken in `(O/L)^*`. The statement includes zero Fourier
coefficients and nonprimitive h.

**Proof.** Multiplication by d preserves the primary residue condition
because `d=1 mod3`, and preserves every coprimality condition at S.
On its support rho is multiplicative. Thus, for every residue x,

\[
\phi_\rho(d^2x)=\rho(d)^2\phi_\rho(x).
\tag{2.2}
\]

In the defining finite sum for the left side of (2.1), substitute
`x=d^2y`. This is a permutation of all residues, including nonunits;
the zero mask in (1.4) is unchanged. The additive character becomes
`e(-hy/L)`, proving the formula. QED.

## 3. The complete source data under the same relabeling

Fix k and a baseline Fourier label h. The baseline active product is
`r_*=k`. For the active product `r=kd`, use the relabeled fixed Fourier
index

\[
h_d=d^{-2}h\pmod L.
\tag{3.1}
\]

Let c0 be the reduced bad denominator of `lambda^2 h/L`. At all
primes of S the valuation of h is preserved under multiplication by
the unit d, so the same c0, including a compatible normalizing unit,
is a reduced denominator for `lambda^2 h_d/L`. The full denominators
are `c_*=c0 k` and `c_d=c0 kd`.

We compare the finite data after choosing the representatives and
matrix entries at sufficiently high **fixed** bad precision. Such
choices do not change the finite Fourier class or the translated theta
function. Indeed changing h by L changes the translation by
`lambda^2 O=3O`, and changing a good-prime Fourier representative by
its prime also changes the translation by `3O`.

Choose an S-supported modulus B large enough for the source's M,
all finitely many c0, their additive periods `lambda^3 c0`, and all
supplementary-character conductors used below. We may increase its
fixed exponents whenever a division by c0 requires that precision.
Choose the good-prime Fourier representatives to be zero at this
precision, as permitted by CRT. Also choose a representative h_d of
(3.1) at sufficiently high precision that the fixed numerators satisfy
the corresponding congruences below.

Write the source matrices as

\[
g_* =\begin{pmatrix}a_*&b_*\\c_*&\delta_*\end{pmatrix},
\qquad
g_d =\begin{pmatrix}a_d&b_d\\c_d&\delta_d\end{pmatrix}.
\tag{3.2}
\]

Then at every required bad modulus the choices can be made so that

\[
\boxed{
a_d\equiv d^{-1}a_*,\qquad c_d=d c_*,\qquad
\delta_d\equiv d\delta_*,\qquad b_d\equiv d^{-1}b_*.
}
\tag{3.3}
\]

Here and below inverses in congruences are bad-modulus inverses, not
assertions that the displayed diagonal scaling is an integral global
matrix.

To verify (3.3), the source numerator is

\[
a=\lambda^2c\left(h_0/L+\sum_{p\mid r}h_p/p\right).
\tag{3.4}
\]

The good-prime terms disappear to the chosen fixed precision. Inserting
`c_d=d c_*` and `h_d=d^{-2}h` gives the first congruence, with the
precision multiplied by c0 if needed. At a bad prime dividing c0,
the source chooses delta as an inverse of a; hence its residue scales
by d. At other bad primes delta is chosen zero, so the same scaling
holds. The congruences at the good active product are independent and
are imposed simultaneously by CRT. Finally
`b=(a delta-1)/c`; compare its numerator modulo Bc0 and divide by
`c0 k d`, where kd is invertible modulo B. This gives the last
congruence.

The unit normalizations agree. When lambda divides c, the source
normalizes `a=1 mod3`; when lambda does not divide c, it normalizes
`c=1 mod3`. Since d is primary, (3.3) preserves both conditions.
Thus no new unit factor has been discarded.

### Lemma 3.1: cusp and additive phase covariance

For the comparison (3.1), the source cusp sigma and the fixed additive
phase psi are the same as for the baseline label h at active product k.

**Proof.** The finite matrix H selecting the cusp depends on c and a
modulo 3, as displayed in the source. These residues are unchanged in
(3.3), so the same H is used, including the cases `v_lambda(c)=1`
and `lambda` not dividing c. Its reduction to one of the three
functions `d_0,d_+,d_-` is therefore unchanged.

The bad additive factor is exactly

\[
\psi(\lambda^4\ell)
=e\!\left(-\frac{\delta_0 r^{-1}\lambda^4\ell}
                   {\lambda^3c_0}\right).
\tag{3.5}
\]

By (3.3), `delta_0` scales by d and `r^{-1}` scales by `d^{-1}`.
Their product is unchanged modulo `lambda^3c0`. This proves the
assertion for every Fourier index, including the ramified and unit
indices of all three cusp expansions. QED.

### Lemma 3.2: Kubota factor covariance

Let kappa0 be the fixed bad factor in the source identity
`kappa(g_1)=kappa0 (a/r)_3`. Under (3.1),

\[
\boxed{\kappa_{0,d}=\kappa_{0,*}\chi_d(c_0)^{-2}.}
\tag{3.6}
\]

**Proof.** This follows in each of the three cases of
`eq:ray-multiplier`; it is useful to check all three explicitly.

If `3|c`, the fixed factor is `(c0/a)_3`. As a function of its
primary denominator, this is a fixed finite ray character, with bad
conductor included in B. The first congruence in (3.3) gives the ratio
`(c0/d)_3^{-1}=chi_d(c0)^{-2}`.

If `v_lambda(c)=1`, the source factor is

\[
\kappa_0=
\left(\frac{-u_0}{a-u_0b}\right)_3
\left(\frac{c_0/u_0}{a}\right)_3,
\qquad u_0\in\{\lambda,-\lambda\}.
\tag{3.7}
\]

The same u0 is used because c has the same residue modulo 3. Both
denominators in (3.7) scale by `d^{-1}` in (3.3). Each denominator
character has fixed conductor at S, included in B. Their ratios
therefore multiply to

\[
\left(\frac{-u_0}{d}\right)_3^{-1}
\left(\frac{c_0/u_0}{d}\right)_3^{-1}
=\left(\frac{-c_0}{d}\right)_3^{-1}
=\chi_d(c_0)^{-2}.
\tag{3.8}
\]

The last equality uses `(-1/d)_3=1`, equivalently
`chi_d(-1)^2=1`.

If lambda does not divide c, the fixed factor is `(a/c0)_3`.
The ratio is `(d/c0)_3^{-1}`. In this case c0 is primary: c is
normalized primary and k,d are primary. Cubic reciprocity for the
coprime primary c0,d identifies this ratio with
`(c0/d)_3^{-1}`. This is again the right side of (3.6).

All uses of denominator-character multiplicativity are on primary
residues coprime to the fixed numerator; these are precisely the
source's supplementary-ray characters. The case c0 a unit is included.
QED.

## 4. Reuniting the finite data forces kappa

The good-prime scalar computation of PR #920 gives, after combining
the outside d coefficient, its local numerators, and the reflected
theta scalar, the d phase

\[
\eta(d)\rho(d)\vartheta(d)\chi_d(\lambda^2c_0)^{-2}
=\eta(d)\rho(d)\chi_d(c_0)^{-2}.
\tag{4.1}
\]

The lambda exponent in the first expression is -6; all d avoid S, so
the equality retains the correct unit values and zero masks.
The norm factor is `(Nd)^{-v}` and the d-prime dual factor is
`-1+Np 1_(p|lambda^4 ell)`.

For each fixed d, reindex its **whole finite Fourier sum** by (3.1).
This is a bijection modulo L. Lemma 2.1 contributes `rho(d)^2`;
Lemma 3.2 contributes `chi_d(c0)^2` from the conjugated multiplier.
Lemma 3.1 leaves the cusp and additive phase unchanged. Thus the total
d phase becomes exactly

\[
\boxed{
\eta(d)\rho(d)\chi_d(c_0)^{-2}
\rho(d)^2\chi_d(c_0)^2
=\eta(d)\rho(d)^3=\kappa(d).
}
\tag{4.2}
\]

This does not set arbitrary finite Fourier labels equal. It evaluates
the actual source coefficients before introducing the redundant
residue-class character expansion. An individual artificial label
zeta in PR #920 need not equal kappa; their complete sum has the
covariance (4.2).

For a baseline label h at active product k define

\[
\begin{aligned}
C_h(s,k)&=
\widehat\phi_\rho(h)\overline{\kappa_{0,h}(k)}
\alpha(c_{0,h})^2(Nc_{0,h})^{1-2s}\Gamma_{c_{0,h}}(k),\\
\Gamma_{c_0}(k)&=
\mu(k)\alpha(k)\gamma_2(k)
\chi_k(-4)\chi_k(\lambda)^3\chi_k(c_0)^2,\\
H(s)&=\frac{i}{3^{5/2}}27^{-s}(2\pi)^{4s-2}
\frac{\Gamma(4/3-s)\Gamma(5/3-s)}
     {\Gamma(s+1/3)\Gamma(s+2/3)}.
\end{aligned}
\tag{4.3}
\]

Write sigma_h and psi_h for its fixed cusp and additive phase. Their
dependence on the residue of k is retained. The number of labels and
all their bad moduli are fixed independently of k. A zero Fourier
coefficient remains zero.

For `Re(s)<0, Re(v)>1`, absolute convergence of the reflected double
series, as in PR #920, now gives the exact identity

\[
\begin{aligned}
\mathscr R_k(w,s)
={}&P_k(w,v)H(s)Q^{1-2s}
\sum_{h\bmod L}C_h(s,k)
\sum_{0\ne\ell\in\lambda^{-4}O}
d_{\sigma_h}(\ell)\psi_h(\lambda^4\ell)
\overline{\alpha(\ell)}\chi_k(\lambda^4\ell)(N\ell)^{s-1}\\
&\quad\times
\prod_{p\nmid kS}
\left(1+\frac{z_p\bigl(-1+Np\,\mathbf1_{p\mid\lambda^4\ell}\bigr)}
                 {D_p}\right).
\end{aligned}
\tag{4.4}
\]

The character in this Euler product is kappa for every baseline h.

## 5. The pole-free weighted theta identity

For nonzero integral m put

\[
\mathcal W_{k,m}(w,v)=
\prod_{\substack{p\mid m\\p\nmid kS}}
\left(1+\frac{\kappa(p)(Np)^{1-v}}{1-x_p}\right).
\tag{5.1}
\]

Each product is finite and depends on the radical of m. Combining
the complete factor in (4.4) with P has the local identity

\[
\begin{cases}
D_p-z_p=1-x_p,&p\nmid m,\\
D_p+(Np-1)z_p=1-x_p+Np\,z_p,&p\mid m.
\end{cases}
\tag{5.2}
\]

Indeed the good-prime factor of P is exactly D_p by (1.3).
In the initial region all free-prime products here are absolutely
convergent. Therefore (4.4) becomes

\[
\boxed{
\begin{aligned}
\mathscr R_k(w,s)
={}&\frac{H(s)Q^{1-2s}}{L_{S,k}(w,\chi^-_k)}
\sum_{h\bmod L}C_h(s,k)
\sum_{0\ne\ell\in\lambda^{-4}O}
d_{\sigma_h}(\ell)\psi_h(\lambda^4\ell)
\overline{\alpha(\ell)}\chi_k(\lambda^4\ell)\\
&\hspace{27mm}\cdot (N\ell)^{s-1}
\mathcal W_{k,\lambda^4\ell}(w,v).
\end{aligned}}
\tag{5.3}
\]

Every moving mask remains in (5.3): the row character is literally
zero when `(lambda^4 ell,k)` is nontrivial, and primes of kS are
omitted from both the finite product and the L-function.
No Ramanujan sign was replaced by a positive divisor weight before
the exact cancellation (5.2).

### Theorem 5.1

The full reunited object has a holomorphic continuation to the tube

\[
\boxed{
\Omega=\{(s,v):\Re s<0,\quad\Re s<\Re v-1\},
\qquad w=v-3s+\tfrac32.
}
\tag{5.4}
\]

There is no separate restriction on Re(v). Formula (5.3) converges
locally normally throughout this tube. In particular its value is
holomorphic through `v=1` for every `Re(s)<0`; the possible residue
in PR #920 is identically zero after the actual finite data are
reunited. Every additional finite-L reciprocal pole in that earlier
representation is also removable on its overlap with Omega.

**Proof.** Put `sigma=Re(s)`, `tau=Re(v)`, and
`a=max(0,1-tau)`. In Omega,

\[
\Re w=\tau-3\sigma+\tfrac32
>\tfrac52-2\sigma>\tfrac52.
\tag{5.5}
\]

Thus `1-x_p` is nonzero and bounded uniformly away from zero, and
`1/L_(S,k)(w,chi^-_k)` has its absolutely convergent Euler product,
bounded uniformly in k and in both imaginary parts.

On every fixed closed real subregion with strict margins, (5.1)
satisfies

\[
|\mathcal W_{k,m}(w,v)|
\le C^{\omega(m)}(N\operatorname{rad}m)^a
\ll_\epsilon (Nm)^{a+\epsilon}.
\tag{5.6}
\]

This includes repeated prime factors, primes at S, and omissions at k.
Separate finitely many small primes to obtain the final divisor
bound. Its constant is independent of k and of the imaginary parts.

The three source cusp sequences satisfy

\[
\sum_{\ell\ne0}|d_\sigma(\ell)|(N\ell)^{-u}<\infty
\qquad(u>1),
\tag{5.7}
\]

with their full ramified and unit support. Since `N(lambda^4 ell)=81
Nell`, the absolute majorant for the inner sum in (5.3) converges if

\[
\sigma+a+\epsilon<0.
\tag{5.8}
\]

The two strict inequalities defining Omega are exactly
`sigma+a<0`; choose epsilon smaller than their margin. This proves
local normal convergence, including holomorphic dependence in both
variables. H is holomorphic for `Re(s)<0`; its reciprocal gamma
factors give zeros, and its numerator gamma factors have no poles
there. The remaining finite factors are holomorphic.

The tube Omega is convex and contains the nonempty overlap
`Re(s)<0, Re(v)>1` where (5.3) was derived from the original
completed object. It therefore provides its analytic continuation.
The holomorphy and removability assertions follow. QED.

### Corollary 5.2: the complete residue identity

If kappa is principal, the complete finite sum in PR #920's residue
formula (5.2), with its specified cusp coefficients, finite Fourier
weights, supplementary characters and row masks, is zero for every
`Re(s)<0`.

**Proof.** The residue is the residue of the same function as (5.3),
and that function is holomorphic on a neighborhood of `v=1` in
Omega. The displayed factors outside the old finite sum are nonzero
on an open subset of `Re(s)<0`; the identity there follows directly,
and analytic continuation gives it at the remaining s. This statement
does not assert that an arbitrarily isolated old ray label or cusp
term has zero residue. QED.

## 6. Uniform vertical control without zero-free input

Let sigma and tau range over a bounded closed real subregion of Omega
with strict margins. The majorants in the preceding proof are uniform
in `Im(s)`, `Im(v)`, and k. In particular no moving Euler reciprocal
outside its absolute half-plane remains. The finite C_h factors have
bounded modulus independent of these imaginary parts; the normalized
Gauss and character values in Gamma have modulus one. Stirling gives

\[
|H(\sigma+it)|
\ll (2+|t|)^{2-4\sigma}.
\tag{6.1}
\]

Consequently (5.3) proves the uniform estimate

\[
\boxed{
|\mathscr R_k(v-3s+\tfrac32,s)|
\ll Q^{1-2\sigma}(2+|\Im s|)^{2-4\sigma}.
}
\tag{6.2}
\]

The constant depends on the fixed ray family and the stated real
margins. This bound is uniform in `Im(v)`. An arbitrarily small
additional power of Q can of course be admitted, but is not needed by
the absolute majorant (5.3). No finite-order zero-free boundary is
used in this section.

## 7. The remaining exponent obstruction

The stronger continuation removes a false analytic barrier; it does
not change the conductor factor `Q^(1-2 Re(s))`. In the balanced
Mellin calculation `A=B=D`, that factor still cancels the opposite
row power from the outer scalar. The residual scale cost is

\[
D^{\tau-2\sigma}.
\tag{7.1}
\]

If `tau<=1`, the domain requires `sigma<tau-1`, so

\[
\tau-2\sigma>2-\tau\ge1.
\tag{7.2}
\]

If `tau>1`, it requires `sigma<0`, giving `tau-2sigma>tau>1`.
Thus the same absolute theta bound is still too expensive everywhere
in the new tube, including its arbitrarily far left v values.

Formula (5.3) exposes the surviving task more precisely: estimate a
sextic-row cusp series with the exact finite multiplicative weight
`W_(k,m)`. Its good-prime weight is now supported on primes actually
dividing the frequency. Additional cancellation in this weighted
series, or another justified transformation of it, is needed for a
moment saving. Pole cancellation alone supplies no such estimate.
