# Poincare-frame endpoint ladder — Part II: determinant census, weak interlacing, and the strict subcritical regime

This file continues `POINCARE_FRAME_ENDPOINT_LADDER_PART_I.md`. Equation
numbering is continuous.

---

## 9. Uniform invertibility of the far deep space

Retain `M=2L` and the recentered discs `Omega_{k,J}` from PF32.  For
`f in W_{M+1}`, the parent source moment estimate gives

\[
\frac1{G(f)}\int_{\mathcal F}Xy^{k-2}|f|^2dxdy
\le1+\frac{k-1}{4\pi(M+1)}.
\tag{PF35}
\]

On every closed recentered disc, the same complex-power and Eisenstein
Laurent calculation as in the fixed-depth parent yields

\[
\Re\frac{I_{1-c/k}(f,f)}{G(f)}
\le
\frac{k}{24(M+1)}
-k\Re\frac1{2c}
+C\log(k+2).
\tag{PF36}
\]

By PF25, `Re c` is comparable with `J` and `|Im c|<=Delta`.  Since
`J<=L` and `M=2L`,

\[
\Re\frac1{2c}-\frac1{24(M+1)}
\ge\frac{c_\Delta}{L}
\tag{PF37}
\]

uniformly for all declared discs.  Condition PF0 therefore gives

\[
-\Re I_{1-c/k}|_{W_{M+1}}
\ge c_\Delta\frac{k}{L}G
\tag{PF38}
\]

for all sufficiently large `k`.  Hence the far block `E(c)` is holomorphic
and invertible there, with

\[
\boxed{\|E(c)^{-1}\|_{G^*\to G}
\le C_\Delta\frac{L}{k}.}
\tag{PF39}
\]

The estimate uses the negative Hermitian part; the complex period matrix is
not replaced by a Hermitian one.

---

## 10. Elimination of the far block

In the exact orthogonal source decomposition PF11, write

\[
I(1-c/k)=
\begin{pmatrix}
H(c)&R(c)\\
T(c)&E(c)
\end{pmatrix}
\]

with the first block indexed by `w_1,...,w_M`.  Part I's complete residual
estimate implies

\[
\|R_l(c)\|_{G^*}
+
\|T_l(c)\|_{G^*}
\le
p(k,L)\sqrt{\varepsilon_{k,M}A_l},
\tag{PF40}
\]

where `p` is a fixed polynomial.  The pure constant-term cross vanishes by
Fourier support, the pure nonconstant cross has first reserve frequency
`M+1`, and every remaining term contains a residual factor from PF15.

Consequently the Schur correction satisfies

\[
\left|
[R E^{-1}T]_{lm}
\right|
\le
\zeta_{k,L}\sqrt{A_lA_m},
\tag{PF41}
\]

where

\[
\zeta_{k,L}
\le C\frac{L}{k}p(k,L)^2\varepsilon_{k,M}
\longrightarrow0
\tag{PF42}
\]

faster than every inverse power.  After eliminating `W_{M+1}`, the finite
matrix, still denoted `H`, therefore obeys PF22--PF23 with a possibly enlarged
`rho_{k,M}`.

Every determinant `D_i` factors into the nonzero far determinant and the
corresponding suffix determinant of this finite source matrix.

---

## 11. Uniform diagonal dominance on a recentered contour

Scale the finite matrix symmetrically by the source energies:

\[
\widetilde H_{lm}(c)
=\frac{H_{lm}(c)}{\sqrt{A_lA_m}}.
\tag{PF43}
\]

Its diagonal is

\[
t_l(c)=T_l(c)/A_l+o(1),
\]

and PF21--PF23 give, for `l!=m`,

\[
|\widetilde H_{lm}(c)|
\le
C(1+\log M)e^{-c_0k|l-m|/M}+\rho_{k,M}.
\tag{PF44}
\]

Fix a suffix `I_i={i,i+1,...,M}` containing `J`.  On
`partial Omega_{k,J}`, let `D(c)=diag(t_l(c):l in I_i)` and let `U` be the
off-diagonal part.  PF33--PF34 imply

\[
\left\|
|D|^{-1/2}U|D|^{-1/2}
\right\|_2
\le\omega_{k,L},
\tag{PF45}
\]

where one may take

\[
\omega_{k,L}
\le
C\frac{L^2}{k}
\sum_{h\ge1}\frac{(1+\log(h+1))e^{-c_0kh/L}}
                    {\sqrt{h}}
+C\frac{L^2}{k}\rho_{k,M},
\tag{PF46}
\]

and

\[
\omega_{k,L}\to0
\tag{PF47}
\]

uniformly over every `i<=J<=L`.  The same estimate holds for suffixes not
containing `J`.

Since determinant is unchanged up to the nonzero source scaling,

\[
\det\widetilde H_{I_i}(c)
=
\prod_{l\in I_i}t_l(c)
\det\!\left(I+D(c)^{-1/2}U(c)D(c)^{-1/2}\right).
\tag{PF48}
\]

A continuous choice of square roots is made only on the contour; the final
identity is algebraic and independent of that choice.  PF45 makes the last
determinant uniformly `1+o(1)`.

---

## 12. Recentered determinant theorem

### Theorem 12.1

Let `L=L(k)` satisfy PF0 and fix `0<Delta<5`.  For all sufficiently large
even `k`, simultaneously for every `1<=J<=L(k)` and every `1<=i<=J`:

1. `D_i` has exactly one zero, counting multiplicity, in
   `Omega_{k,J}`;
2. the zero is real and simple; denote it by `c_{i,J}`;
3. `D_{J+1}` is nonzero throughout the disc;
4. uniformly in `i,J`,
   \[
   c_{i,J}=\widehat c_{k,J}+o(1);
   \tag{PF49}
   \]
5. `Q_J` has one simple zero and no pole in the disc;
6. for `i<J`, `Q_i` has a simple zero and a simple pole unless the two
   determinant zeros coincide, in which case both factors cancel and
   `Q_i` is holomorphic and nonzero at the common point.

Reflection supplies the corresponding left endpoint discs.

#### Proof

On `partial Omega_{k,J}`, PF48 compares the actual suffix determinant with
its diagonal product.  That product has exactly one zero inside, namely the
simple one-mode zero of `T_J`; every other one-mode center lies outside by
PF26.  The determinant factor in PF48 is uniformly nonzero and close to one.
Rouche therefore gives exactly one zero for every suffix containing `J` and
none for the suffix beginning at `J+1`.

The source has Schwarz symmetry, so a nonreal zero would bring a distinct
conjugate zero into the same conjugation-invariant disc.  The unique zero is
real.  Counting multiplicity one makes it simple.  Repeating the contour
argument with a radius tending to zero more slowly than `omega_{k,L}` gives
PF49.

All eliminated factors are nonzero.  Therefore the suffix zero is exactly
the zero of `D_i`.  The statement about `Q_i=D_i/D_{i+1}` is then immediate.
Reflection follows from the completed period functional equation. ∎

This is a growing fixed-weight determinant census in the near-maximal
endpoint range `L=o(k/log k)`.  It deliberately distinguishes determinant
zeros from uncancelled quotient divisors.

---

## 13. Exact weak interlacing and the cancellation criterion

Fix `i<J` and eliminate all nonvanishing blocks except the source directions
corresponding to `i` and `J`.  On the real interval, the resulting exact
matrix is

\[
\begin{pmatrix}
a_i(c)&b_i(c)\\
b_i(c)&d_i(c)
\end{pmatrix}.
\tag{PF50}
\]

Here

\[
Q_i=a_i-\frac{b_i^2}{d_i},
\qquad
\delta_i=d_i-\frac{b_i^2}{a_i},
\tag{PF51}
\]

and `d_i=delta_{i+1}`.  Diagonal dominance gives, throughout the cluster,

\[
a_i(c)>0,
\qquad
d_i'(c)>0.
\tag{PF52}
\]

At `c=c_{i,J}`, PF51 gives

\[
d_i(c_{i,J})=\frac{b_i(c_{i,J})^2}{a_i(c_{i,J})}\ge0,
\tag{PF53}
\]

whereas

\[
d_i(c_{i+1,J})=0.
\tag{PF54}
\]

Therefore

\[
\boxed{
c_{J,J}\le c_{J-1,J}\le\cdots\le c_{1,J}.}
\tag{PF55}
\]

Moreover

\[
c_{i,J}=c_{i+1,J}
\quad\Longleftrightarrow\quad
b_i(c_{i,J})=0.
\tag{PF56}
\]

If the coupling is nonzero, the inequality is strict and the exact
mean-value formula is

\[
c_{i,J}-c_{i+1,J}
=
\frac{b_i(c_{i,J})^2}
     {a_i(c_{i,J})d_i'(\xi_{i,J})}
>0
\tag{PF57}
\]

for an intermediate point `xi_{i,J}`.  At equality, the two simple
determinant factors cancel in their quotient.  Thus strict interlacing is
precisely a source-coupling problem, not a consequence of determinant
existence alone.

---

## 14. Strict subcritical ladder

The source coupling is perturbative in the smaller regime

\[
\boxed{
\vartheta_{k,L}
=\frac{L^2\log(L+2)}{k}\longrightarrow0.
}
\tag{PF58}
\]

### Lemma 14.1 — elementary divisor convolution

For `S_n=sigma_{-1}(n)`,

\[
\sum_{r=1}^{h-1}\frac{S_rS_{h-r}}r
\le C\log(h+1).
\tag{PF59}
\]

#### Proof

Expand both divisor sums.  For divisors `d|r`, `e|h-r`, write `r=dm`.
The congruence for `m` has modulus `e/(d,e)` when it is soluble.  The
harmonic sum in one residue class is bounded by

\[
1+\frac{(d,e)}e\log(h+1).
\]

After multiplication by the coefficient `1/(d^2e)`, the first terms sum to
`O(log h)` and the logarithmic terms to

\[
O(\log h)
\sum_{d,e\ge1}\frac{(d,e)}{d^2e^2}
=O(\log h).
\]

The last double series converges after writing `d=ga,e=gb`. ∎

### Lemma 14.2 — uniform coupling

Under PF58, uniformly for all `i<J<=L`,

\[
\boxed{
\frac{b_i(c)}{A_J}
=S_{J-i}\left(1+O(\vartheta_{k,L})+o(1)\right)
}
\tag{PF60}
\]

on the real cluster interval.

#### Proof

Use column scaling by the exact `A_m` on the earlier block
`m=i+1,...,J-1`.  Its diagonal at the `J`-th cluster is comparable with

\[
\frac{k(J-m)}{J^2},
\]

and its upper entry at distance `h` is `S_h(1+o(1))`; the reverse entry is
exponentially suppressed.  The row norm of the diagonal-normalized upper
part is `O(L^2/k)`, so Neumann inversion is valid.

The first Schur correction is bounded by PF59 and is
`O((L^2/k)log L)A_J`.  The higher corrections form a geometric series in
the row norm.  PF58 proves PF60.  The Poincare-frame residual and far-block
corrections are superpolynomially smaller. ∎

Consequently all inequalities in PF55 are strict in the PF58 regime.  Put

\[
\mathcal F_{i,J}
=\frac{T_i(\widehat c_{k,J})}{kA_i}>0,
\qquad
\mathcal T'_{J}
=\frac{T_J'(\widehat c_{k,J})}{kA_J}>0.
\tag{PF61}
\]

The exact Schur formula PF57 gives the uniform recentered laws

\[
\boxed{
 c_{i,J}-c_{i+1,J}
 =
 \frac{S_{J-i}^2}{k^2\mathcal F_{i,J}\mathcal T'_J}
 \frac{A_J}{A_i}(1+o(1)),
}
\tag{PF62}
\]

and

\[
\boxed{
\operatorname{Res}_{s}Q_i
=
\frac{A_JS_{J-i}^2}{k^2\mathcal T'_J}(1+o(1))>0.
}
\tag{PF63}
\]

If, in addition,

\[
L^2\log(k/L+2)=o(k),
\tag{PF64}
\]

then PF25 gives `chat_{k,J}=12J+o(1)`,
`mathcal T'_J=(288J^2)^{-1}(1+o(1))`, and PF62--PF63 reduce to the
fixed-center formulas of the parent.  This improves the previous cube-root
range to the source-natural square-root/logarithmic range.

---

## 15. Boundary of the theorem

The determinant theorem requires only PF0.  Strict quotient interlacing with
the unmodified divisor coefficient `S_h` requires PF58.  Between those
regimes the coupling is nonperturbative and may vanish.  The next packet
derives its exact fixed-offset scaling law.

No claim is made that every weak inequality is strict under PF0, that a
common determinant zero cannot occur, or that the parent gap law remains
unchanged when `J^2/k` is not small.  RH and GRH remain unproved.