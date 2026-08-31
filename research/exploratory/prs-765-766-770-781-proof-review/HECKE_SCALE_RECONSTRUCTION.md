# Independent reconstruction of the matched Hecke-support scale

**Status:** proof reconstruction and import audit; independent review still required.  
**Parent source:** PR #766 at `17c7624a0bd56c5356d00278b2a846d2efdbdccc`.  
**Branch theorem reconstructed:** `HECKE_SUPPORT_SCALE_CLOSURE.md`.  
**RH/GRH:** RH and GRH remain unproved.

This note rederives the matched `k/log k` theorem from the exact source
normalizations. Its purpose is to separate the elementary new argument from
the single classical automorphic input on which it depends.

---

## 1. Exact source identities

Let `f` be a level-one holomorphic Hecke eigencuspform of even weight `k`,
normalized by `a_f(1)=1`, and write

\[
a_f(n)=\lambda_f(n)n^{(k-1)/2},\qquad
L_f=L(1,\operatorname{sym}^2 f)>0,
\qquad e_f=f/\sqrt{G(f)}.
\]

The parent packet proves, with its stated Petersson convention,

\[
\int_{y\ge1} y\,y^k|e_f(z)|^2\,d\mu(z)
=
\frac{\pi}{2L_f}
\sum_{n\ge1}\frac{\lambda_f(n)^2}{n}Q(k,4\pi n),
\tag{HR1}
\]

where `Q(a,x)=Gamma(a,x)/Gamma(a)`, and

\[
\sum_{n\ge1}\frac{\lambda_f(n)^2}{n^s}
=
\frac{\zeta(s)L(s,\operatorname{sym}^2 f)}{\zeta(2s)},
\qquad \Re s>1.
\tag{HR2}
\]

The portion below `y=1` contributes at most one to

\[
M_X(e_f)=\int_{\mathcal F}\max(1,y)y^k|e_f|^2d\mu.
\]

No coefficientwise Deligne or divisor-function majorant is needed below.

---

## 2. Gamma-tail Mellin domination

If `Z` has Gamma distribution of shape `a` and scale one, then
`Q(a,x)=P(Z>=x)`. For `0<u<=1`, Markov and Gautschi give

\[
Q(a,x)
\le x^{-u}\frac{\Gamma(a+u)}{\Gamma(a)},
\qquad
Q(k,x)\le\left(\frac{k}{x}\right)^u.
\tag{HR3}
\]

Put `u=1/log k`. Positivity and HR2 imply

\[
\begin{aligned}
\sum_{n\ge1}\frac{\lambda_f(n)^2}{n}Q(k,4\pi n)
&\le
\left(\frac{k}{4\pi}\right)^u
\sum_{n\ge1}\frac{\lambda_f(n)^2}{n^{1+u}}\\
&=
\left(\frac{k}{4\pi}\right)^u
\frac{\zeta(1+u)L(1+u,\operatorname{sym}^2 f)}
     {\zeta(2+2u)}.
\end{aligned}
\tag{HR4}
\]

This is the load-bearing elementary step. It retains the exact
Rankin--Selberg pole instead of replacing every coefficient by `d_4(n)`.

---

## 3. The one imported near-one lemma

The parent already imports the continuation and standard zero-free region
for the symmetric-square `GL(3)` L-function, including absence of an
exceptional real zero. The additional consequence used by the branch is

\[
L(1+u,\operatorname{sym}^2 f)
\ll L(1,\operatorname{sym}^2 f),
\qquad 0\le u\le1/\log k.
\tag{HR5}
\]

Here is the standard reconstruction, so that the import is not hidden in a
phrase.

Choose a fixed small `a>0` inside the imported zero-free strip and put

\[
\sigma_0=1+\frac{a}{\log k}.
\]

In the absolute-convergence half-plane, the Euler product and Deligne's
local bound give

\[
\left|\frac{L'}{L}(\sigma_0,\operatorname{sym}^2 f)\right|
\ll\log k.
\tag{HR6}
\]

The explicit formula for the completed symmetric-square function expresses
`-Re L'/L` as the archimedean logarithmic derivative, of size `O(log k)`,
plus a nonnegative sum of Poisson kernels over zeros. The zero-free strip
places every zero a distance `gg 1/log k` to the left of the real segment
`1<=sigma<=sigma_0`. Comparing each Poisson kernel on that segment with its
value at `sigma_0`, and using HR6 at the endpoint, gives

\[
\frac{L'}{L}(\sigma,\operatorname{sym}^2 f)=O(\log k)
\qquad(1\le\sigma\le\sigma_0).
\tag{HR7}
\]

The local factors are positive on the real interval, so the real logarithm
is unambiguous. Integrating HR7 over a segment of length at most
`1/log k` proves HR5.

Thus HR5 is a classical consequence of the already imported zero-free
machinery. It is not a new automorphic zero-free theorem and must remain
listed as an import.

---

## 4. Logarithmic X-moment

The elementary bounds

\[
\left(\frac{k}{4\pi}\right)^u\le e,
\qquad
\zeta(1+u)\le1+1/u\le2\log k,
\qquad
\zeta(2+2u)\ge1
\]

and HR5 turn HR4 into

\[
\sum_{n\ge1}\frac{\lambda_f(n)^2}{n}Q(k,4\pi n)
\ll L_f\log k.
\tag{HR8}
\]

Substitution into HR1 yields

\[
\boxed{M_X(e_f)\ll\log k.}
\tag{HR9}
\]

The normalization `L_f` cancels. In particular, the lower bound
`L_f>>1/log k`, although valid and imported by the parent, is not used in
this moment estimate.

---

## 5. Arbitrary selected Hecke subsets

For any subset `S_k` of the Petersson-orthonormal Hecke basis, let
`V(S_k)` be its span and `r_k=|S_k|`. Compression of multiplication by
`X=max(1,y)` is positive, so

\[
\|T_X|_{V(S_k)}\|
\le\operatorname{tr}(T_X|_{V(S_k)})
=
\sum_{f\in S_k}M_X(e_f)
\ll r_k\log k.
\tag{HR10}
\]

No cancellation or averaging over the complete Hecke family occurs. The
bound is therefore uniform for an adversarial selected subset.

The parent endpoint Laurent estimate gives, uniformly on every compact
`K` in `Re c>0`,

\[
\left|I_{1-c/k}(u,v)+\frac{k}{2c}G(u,v)\right|
\le C_K\sqrt{M_X(u)M_X(v)}.
\tag{HR11}
\]

Whitening by the Petersson Gram and using HR10 gives

\[
\boxed{
\frac1kG_S^{-1/2}I_S(1-c/k)G_S^{-1/2}
=
-\frac1{2c}I
+O_K\!\left(\frac{r_k\log k}{k}\right).
}
\tag{HR12}
\]

Hence every selected restriction and every internal subspace restriction is
endpoint-invertible when

\[
r_k=o(k/\log k),
\]

and also for a sufficiently small fixed multiple of `k/log k`. Reflection
gives the left endpoint.

---

## 6. Reconstruction verdict

The four-logarithm improvement survives independent reconstruction. The
new part consists of HR3--HR4 and the positive trace compression HR10. The
only additional classical input is HR5, which follows from the standard
symmetric-square zero-free strip and explicit-formula logarithmic-derivative
bound already imported in the parent programme.

What remains open is the constant-scale window

\[
r_k\asymp k/\log k.
\]

The present theorem does not determine a sharp constant, produce a zero at
a large constant, or apply to arbitrary rotated spaces outside a selected
Hecke span. RH and GRH remain unproved.