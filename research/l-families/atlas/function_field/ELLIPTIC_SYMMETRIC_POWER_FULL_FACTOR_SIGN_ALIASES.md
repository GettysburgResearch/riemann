# Complete rational collisions of elliptic symmetric-power factors

## Results

Fix

\[
1-tT+qT^2=(1-\alpha T)(1-\beta T),\qquad
\alpha+\beta=t,\qquad \alpha\beta=q\ne0,
\]

and for \(m\ge0\) put

\[
P_m(t,q;T)=
\det(1-\operatorname{Sym}^m(\operatorname{Frob})T)
=
\prod_{j=0}^{m}
\left(1-\alpha^{m-j}\beta^jT\right).
\]

There are two exact theorems.

**Complete fixed-\(q\) rational classification.** If
\(m\ge1\) and \(x,y,q\in\mathbb Q\), with \(q\ne0\), then

\[
P_m(x,q;T)=P_m(y,q;T)
\quad\Longrightarrow\quad x^2=y^2.
\]

Combining this with the sign theorem below gives:

\[
\begin{array}{c|l}
m\text{ even}
&P_m(x,q;T)=P_m(y,q;T)\Longleftrightarrow x=\pm y,\\
m\text{ odd}
&P_m(x,q;T)=P_m(y,q;T)\Longleftrightarrow
\begin{cases}
x=y,\text{ or}\\
y=-x,\ x^2=2q,\ 4\mid m+1,\text{ or}\\
y=-x,\ x^2=3q,\ 6\mid m+1.
\end{cases}
\end{array}
\]

The restriction \(m\ge1\) is essential: the \(\operatorname{Sym}^0\)
factor is \(1-T\) for every trace.

**Characteristic-zero sign theorem.** Let \(r=\alpha/\beta\). Swapping
\(\alpha,\beta\) replaces \(r\) by \(r^{-1}\), so its order is
well-defined. If \(m\) is even, then
\(P_m(t,q;T)=P_m(-t,q;T)\) for every \(t,q\). If \(m\) is odd, then

\[
P_m(t,q;T)=P_m(-t,q;T)
\quad\Longleftrightarrow\quad
r\text{ has even order }n\text{ with }n\mid m+1.
\]

This includes \(n=2\), equivalently \(t=0\); in characteristic zero that
sign pair is diagonal.

## Why an arbitrary rational collision must be a sign pair

Let \(A_x\) be the root multiset of \(P_m(x,q;T)\), counted with
multiplicity, and define the intrinsic quotient group

\[
\Gamma(A_x)=
\left\langle a/a':a,a'\in A_x\right\rangle.
\]

Because \(q\ne0\), both base roots and every symmetric-power weight are
nonzero, so every quotient in this definition exists. Equality of the
products \(\prod_{\lambda\in A}(1-\lambda T)\) recovers the root
multiset with multiplicity over an algebraic closure.

For base roots \(\alpha,\beta\) and \(r_x=\alpha/\beta\), every quotient
of symmetric-power weights is a power of \(r_x\). Conversely, because
\(m\ge1\), two consecutive weights have quotient

\[
\frac{\alpha^{m-j}\beta^j}
{\alpha^{m-j-1}\beta^{j+1}}=r_x.
\]

Therefore

\[
\Gamma(A_x)=\langle r_x\rangle.
\]

This remains true for \(m=1\), for \(r_x=1\), and when torsion makes
weights repeat.

Equality of complete factors is equality of root multisets over an
algebraic closure, hence it makes their intrinsic quotient groups
equal:

\[
\langle r_x\rangle=\langle r_y\rangle.
\]

If this common cyclic group is infinite, both \(r_x\) and \(r_y\) are
generators, so \(r_y=r_x^{\pm1}\). Thus
\(r_x+r_x^{-1}=r_y+r_y^{-1}\).

If it is finite, rationality gives

\[
\frac{x^2}{q}-2=r_x+r_x^{-1}\in\mathbb Q,\qquad
\frac{y^2}{q}-2=r_y+r_y^{-1}\in\mathbb Q.
\]

A primitive \(n\)-th root satisfying a quadratic over \(\mathbb Q\)
has \(\varphi(n)\le2\). The global classification below gives
\(n\in\{1,2,3,4,6\}\). For these orders,
\(r+r^{-1}\) is respectively \(2,-2,-1,0,1\). Each \(r\) is a
generator of the common quotient group. For these five orders the
generators form an inverse pair (or a singleton), so they have the same
\(r+r^{-1}\). In either the finite or infinite case,

\[
\frac{x^2}{q}-2=\frac{y^2}{q}-2,
\]

so \(x^2=y^2\), as claimed.

## Root-multiset proof of the sign theorem

Replacing \(t\) by \(-t\) replaces the base roots by
\((-\alpha,-\beta)\). Every \(\operatorname{Sym}^m\) eigenvalue is
multiplied by \((-1)^m\), proving the even case term by term.

For odd \(m\), divide the spectrum by the nonzero scalar \(\beta^m\).
Factor equality is exactly the multiset identity

\[
\{1,r,r^2,\ldots,r^m\}
=
\{-1,-r,-r^2,\ldots,-r^m\}.
\]

The element \(-1\) on the right must occur on the left, so
\(r^j=-1\) for some \(1\le j\le m\). Hence \(r\) has exact even order
\(n\), with \(-1=r^{n/2}\). Multiplication by \(-1\) is the shift by
\(n/2\) on exponent residues.

## Consecutive-residue multiplicity lemma

Let \(n\) be even, let \(L\ge1\), and write

\[
L=an+s,\qquad 0\le s<n.
\]

Among \(0,1,\ldots,L-1\), residues \(0,\ldots,s-1\) occur \(a+1\)
times and the other residues occur \(a\) times.

If \(0<s\le n/2\), residue \(0\) is heavy but its half-shift \(n/2\)
is light. If \(n/2<s<n\), residue \(s-n/2\) is heavy but its
half-shift \(s\) is light. Thus a nonzero remainder is impossible under
half-shift invariance. If \(s=0\), all multiplicities are equal.
Consequently

\[
\{0,1,\ldots,L-1\}\bmod n
\text{ is invariant under }+n/2
\quad\Longleftrightarrow\quad n\mid L.
\]

Taking \(L=m+1\) proves the odd sign theorem. Because the argument
tracks multiplicities, it covers repeated torsion weights; it assumes
neither a squarefree spectrum nor distinct roots.

## Closed factors on the sign-alias loci

If \(m\) is odd and the even order \(n\) divides \(m+1\), the spectrum
is \((m+1)/n\) complete \(n\)-cycles. Moreover

\[
\beta^{mn}
=q^{mn/2}r^{-mn/2}
=-q^{mn/2},
\]

because \(r^{n/2}=-1\) and \(m\) is odd. Therefore

\[
P_m(t,q;T)
=
\left(1+q^{mn/2}T^n\right)^{(m+1)/n}.
\]

The rational even-order cases are

\[
\begin{array}{c|c}
n & P_m(t,q;T)\\ \hline
2 & (1+q^mT^2)^{(m+1)/2}\\
4 & (1+q^{2m}T^4)^{(m+1)/4}\\
6 & (1+q^{3m}T^6)^{(m+1)/6}.
\end{array}
\]

## Exact rational cyclotomic restriction

For rational \(t,q\),

\[
\frac{t^2}{q}=r+r^{-1}+2.
\]

If \(r\) has order \(n\), its cyclotomic polynomial divides a quadratic,
so \(\varphi(n)\le2\). This is classified globally, not inferred from a
finite search. A prime \(p\ge5\) dividing \(n\) forces
\(p-1\mid\varphi(n)\), hence \(\varphi(n)\ge4\). Thus
\(n=2^a3^b\). The formulas

\[
\varphi(2^a)=2^{a-1},\qquad
\varphi(3^b)=2\cdot3^{b-1},\qquad
\varphi(2^a3^b)=2^a3^{b-1}\quad(a,b\ge1)
\]

give

\[
\varphi(n)\le2
\quad\Longleftrightarrow\quad
n\in\{1,2,3,4,6\}.
\]

The even possibilities are

\[
\begin{array}{c|c|c}
n & \Phi_n(X) & t^2/q\\ \hline
2 & X+1 & 0\\
4 & X^2+1 & 2\\
6 & X^2-X+1 & 3.
\end{array}
\]

So for odd \(m\), a rational sign pair aliases exactly when \(t=0\),
or \(t^2=2q\) with \(4\mid m+1\), or \(t^2=3q\) with
\(6\mid m+1\). Orders \(1\) and \(3\) are negative controls: an odd
order cannot realize multiplication by \(-1\).

## The rational-trace hypothesis is sharp

Let \(q=1\), let \(\zeta\) be a primitive fifth root, and set

\[
x=\zeta+\zeta^{-1},\qquad
y=\zeta^2+\zeta^{-2}.
\]

These are the two roots of \(X^2+X-1\), and \(x\ne\pm y\). For \(m=3\),
however, both symmetric-cube spectra are the four nontrivial fifth
roots. Hence

\[
P_3(x,1;T)=P_3(y,1;T)
=1+T+T^2+T^3+T^4.
\]

Thus the complete \(x=\pm y\) classification does not extend to
arbitrary algebraic traces. The characteristic-zero sign theorem itself
does extend, because its proof never assumes rationality.

## Integral odd-prime-power corollary

Let \(q=p^a\), where \(p\) is odd prime and \(a\ge1\), let
\(t\in\mathbb Z\setminus\{0\}\), and let \(m\) be odd.

The equation \(t^2=2q\) is impossible: \(v_2(2q)=1\), while a nonzero
square has even 2-adic valuation. If \(t^2=3p^a\), prime valuations
force \(p=3\), and \(a+1\) must be even. Writing \(a=2k+1\) yields

\[
q=3^{2k+1},\qquad t=\pm3^{k+1}.
\]

Consequently a nontrivial integral sign pair at odd prime-power \(q\)
has equal complete factors exactly when

\[
m\equiv5\pmod6,\qquad
q=3^{2k+1},\qquad
t=\pm3^{k+1}.
\]

These values satisfy \(t^2=3q<4q\). This packet does not infer curve
realization or a compatible global family from the Hasse inequality.

## Exact certificates

The dependency-free producer:

- builds \(\Phi_n\in\mathbb Z[X]\) from
  \(\prod_{d\mid n}\Phi_d(X)=X^n-1\) and checks divisor products and
  degrees through order \(36\);
- tests every relevant even order \(n\le2m\) for odd \(m\le36\)
  against the explicit residue-multiplicity witness;
- reconstructs complete factors with exact Newton identities through
  \(m=36\), including the closed order-\(2,4,6\) forms;
- checks arbitrary rational trace pairs on a separate bounded grid;
- preserves order-\(1\), order-\(3\), and order-\(6\) nondivisibility
  examples as negative controls;
- verifies the primitive-fifth-root counterexample by exact exponents
  modulo \(5\);
- stays below an exclusive budget of \(5000\) declared high-level work
  units.

The finite checks are regressions, not the proofs above. The bound
\(n\le2m\) loses no relevant sign-torsion case: necessity places
\(-1=r^{n/2}\) among powers through \(r^m\), so \(n/2\le m\).

## Locked provenance

Two prior packets are locked by schema, canonical payload hash, and
LF-normalized file hash:

| packet | payload SHA-256 | LF-normalized SHA-256 | use |
|---|---|---|---|
| `elliptic_symmetric_power_trace_aliasing.json` | `046f76f43a2af3ac296f5c18c258e61f138e122bee38ec618af489e7e3a9e50e` | `7a6e249fd696f9526154375f60bd97c2c40d251791f08eec6ecdc70b3177b941` | replay the even-\(m\) and \(m=5\) diagnostics |
| `elliptic_sym5_coefficient_recovery.json` | `f7b1a484d2a8b3cc0b997dbf0f15a69893f279a32bc550b71f28b21a5a9d7467` | `649f682c0355a71eab618cd4fbd0507e96643b1fefacdd37e1eb9cd82dd36515` | replay the three locked \(\operatorname{Sym}^5\) full-factor sign aliases |

No curve, finite field, or trace range is enumerated.

## Replay

From the repository root:

```text
python research/l-families/atlas/function_field/elliptic_symmetric_power_full_factor_sign_aliases.py --check
python -O research/l-families/atlas/function_field/elliptic_symmetric_power_full_factor_sign_aliases.py --check
python -m unittest tests.test_elliptic_symmetric_power_full_factor_sign_aliases
python -O -m unittest tests.test_elliptic_symmetric_power_full_factor_sign_aliases
```

## Scientific firewall

This is a complete classification of fixed-\(q\), rational-trace,
complete local-factor collisions for \(m\ge1\), plus a
characteristic-zero theorem for the sign pair. It is not a
classification of collisions of the scalar character alone, and the
complete classification is not claimed for nonrational traces. It
constructs no curve, global \(L\)-function, Euler product, automorphic
lift, or compatible family, and makes no realization,
literature-priority, RH, GRH, zero-free-region, or zero-distribution
claim.
