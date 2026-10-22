# T-93010 — The complete Q4 endpoint PIG is directly RH-equivalent

Claim ID: `T-93010`  
Status: **PROPOSED COMPLETE RH-EQUIVALENT CRITERION — INDEPENDENT REVIEW REQUIRED; RH UNPROVED**  
Created: 2026-08-14  
Depends on: PR #362 at `31c57c56c00c0a062a49a126d4e5a68ff28e9fe8`, especially `T-90404`; PR #383 at `d764be15bd8ea902ad260484eab44d19a9e82175`, especially `L-90411`, `L-90412`, `L-90418`, and the scope correction `R-90412`. The Mellin calculation is reproduced natively here; `L-90419` and `T-90420` Section 5 are not used.  
Scope: the complete continuous-position endpoint carry field of the compact-Q4 innovation; this theorem does not prove its unconditional PIG bound and does not use the disputed global QIDR recurrence

## 1. The actual compact-Q4 prefix

Let

\[
 c_\circ(m)
 =\Lambda(m)
 -4\mathbf 1_{4\mid m}\Lambda(m/4)
 +3(\log4)\sum_{r\ge1}\mathbf 1_{m=4^r},
\tag{T-93010.1}
\]

and put

\[
 C_\circ(x)=\sum_{m\le x}c_\circ(m),
 \qquad C_\circ(0)=0.
\tag{T-93010.2}
\]

This is the ordinary prefix coefficient of the actual compact innovation source from `L-90412`, including the delayed four-adic correction.

For an integer endpoint \(N\ge2\), define the complete continuous-position carry field

\[
 Q_{\circ,N}(\theta)
 =C_\circ(N)
  -C_\circ(\lfloor N\theta\rfloor)
  -C_\circ(\lfloor N(1-\theta)\rfloor),
 \qquad 0<\theta<1.
\tag{T-93010.3}
\]

On the open cell \(j/N<\theta<(j+1)/N\), its value is

\[
 R_N(j)
 =C_\circ(N)-C_\circ(j)-C_\circ(N-j-1),
 \qquad 0\le j<N.
\tag{T-93010.4}
\]

Define the endpoint PIG energy in its natural normalized form

\[
 \boxed{
 \mathscr P_\circ(N)
 =\frac1N\int_0^1|Q_{\circ,N}(\theta)|^2\,d\theta
 =\frac1{N^2}\sum_{j=0}^{N-1}|R_N(j)|^2.
 }
\tag{T-93010.5}
\]

No restricted carry bank, pushforward measure, or global block recurrence occurs in this definition.

## 2. The mean mode and an exact coercivity identity

The mean of the complete field is

\[
 \begin{aligned}
 M_\circ(N)
 &:=\int_0^1Q_{\circ,N}(\theta)\,d\theta\\
 &=\frac1N\sum_{j=0}^{N-1}R_N(j)\\
 &=\sum_{m\le N}c_\circ(m)
   \left(\frac{2m}{N}-1\right).
 \end{aligned}
\tag{T-93010.6}
\]

The last equality follows by reversing the finite prefix sum:

\[
 \sum_{j=0}^{N-1}C_\circ(j)
 =\sum_{m=1}^{N-1}(N-m)c_\circ(m).
\]

For any complex numbers \(z_0,\ldots,z_{N-1}\),

\[
 \boxed{
 N\sum_{j=0}^{N-1}|z_j|^2
 -\left|\sum_{j=0}^{N-1}z_j\right|^2
 =\sum_{0\le a<b<N}|z_a-z_b|^2.
 }
\tag{T-93010.7}
\]

Applying this to \(z_j=R_N(j)\) gives the exact endpoint decomposition

\[
 \boxed{
 \mathscr P_\circ(N)
 =\frac{|M_\circ(N)|^2}{N}
 +\frac1{N^3}
   \sum_{0\le a<b<N}|R_N(a)-R_N(b)|^2.
 }
\tag{T-93010.8}
\]

In particular,

\[
 \boxed{
 |M_\circ(N)|^2
 \le N\mathscr P_\circ(N).
 }
\tag{T-93010.9}
\]

This is the required positive-current adapter. It is unconditional, coefficient one, and uses the complete actual endpoint field. It does **not** require the false unconditional macroscopic Selberg estimate corrected by `R-90412`.

## 3. Mellin transform and zero safety

For real \(X\ge1\), extend the definition by the same finite sum

\[
 M_\circ(X)
 =\sum_{m\le X}c_\circ(m)
   \left(\frac{2m}{X}-1\right).
\tag{T-93010.10}
\]

For \(\Re z>1\), termwise integration gives

\[
 \int_m^\infty
 \left(\frac{2m}{X}-1\right)X^{-z-1}\,dX
 =\frac{z-1}{z(z+1)}m^{-z}.
\tag{T-93010.11}
\]

The Dirichlet series of (T-93010.1) is

\[
 \sum_{m\ge1}\frac{c_\circ(m)}{m^z}
 =
 (1-4^{1-z})
 \left(-\frac{\zeta'}{\zeta}(z)\right)
 +3(\log4)\frac{4^{-z}}{1-4^{-z}}.
\tag{T-93010.12}
\]

Consequently

\[
 \boxed{
 \begin{aligned}
 \int_1^\infty M_\circ(X)X^{-z-1}\,dX
 ={}&\frac{z-1}{z(z+1)}
 \Bigg[
 (1-4^{1-z})
 \left(-\frac{\zeta'}{\zeta}(z)\right)\\
 &\qquad
 +3(\log4)\frac{4^{-z}}{1-4^{-z}}
 \Bigg].
 \end{aligned}
 }
\tag{T-93010.13}
\]

At every nontrivial zero \(\rho\), \(0<\Re\rho<1\),

\[
 1-4^{1-\rho}\ne0,
 \qquad
 1-4^{-\rho}\ne0,
 \qquad
 \rho\notin\{-1,0,1\}.
\tag{T-93010.14}
\]

Indeed either exponential equality would force respectively \(\Re\rho=1\) or \(\Re\rho=0\). The four-adic term is holomorphic at \(\rho\), while \(-\zeta'/\zeta\) has a nonremovable simple pole whose residue records the zero multiplicity. Thus every open-strip zero survives as a pole of (T-93010.13).

## 4. Integer endpoint bounds extend to the Mellin variable

The elementary Chebyshev bound gives

\[
 \sum_{m\le N}m|c_\circ(m)|\ll N^2.
\tag{T-93010.15}
\]

If \(N<X<N+1\), the support in (T-93010.10) is unchanged and

\[
 |M_\circ(X)-M_\circ(N)|
 \le
 2\left|\frac1X-\frac1N\right|
 \sum_{m\le N}m|c_\circ(m)|
 \ll1.
\tag{T-93010.16}
\]

Therefore every power or power-log estimate proved at all integer endpoints extends to all real \(X\), with the same exponent. This closes the discrete-endpoint-to-Mellin interface explicitly.

## 5. Endpoint PIG implies RH

Assume that for some fixed \(A\),

\[
 \boxed{
 \mathscr P_\circ(N)\ll(\log(2N))^A
 \qquad(N\ge2).
 }
\tag{T-93010.17}
\]

By (T-93010.9),

\[
 M_\circ(N)
 \ll\sqrt N\,(\log(2N))^{A/2}.
\tag{T-93010.18}
\]

Equations (T-93010.16)--(T-93010.18) imply, for every \(\varepsilon>0\),

\[
 M_\circ(X)=O_\varepsilon(X^{1/2+\varepsilon}).
\tag{T-93010.19}
\]

Hence the Mellin integral in (T-93010.13) is holomorphic in \(\Re z>1/2\). Zero safety then excludes every zeta zero in that half-plane. The functional equation excludes the reflected half-plane, so

\[
 \boxed{
 \text{endpoint PIG (T-93010.17)}\Longrightarrow\mathrm{RH}.
 }
\tag{T-93010.20}
\]

This implication is independent of `T-90302` and of the incomplete global QIDR source/measure recurrence.

## 6. RH implies endpoint PIG

Assume RH. The von Koch estimate gives

\[
 E(x):=\psi(x)-x
 \ll\sqrt x\log^2(2x).
\tag{T-93010.21}
\]

From (T-93010.1)--(T-93010.2),

\[
 C_\circ(x)
 =E(x)-4E(\lfloor x/4\rfloor)+O(\log(2x)),
\tag{T-93010.22}
\]

because the linear terms leave only a bounded floor residue. Thus uniformly in \(0\le j<N\),

\[
 R_N(j)\ll\sqrt N\log^2(2N).
\tag{T-93010.23}
\]

Inserting this in (T-93010.5) gives

\[
 \boxed{
 \mathrm{RH}
 \Longrightarrow
 \mathscr P_\circ(N)\ll\log^4(2N).
 }
\tag{T-93010.24}
\]

Combining (T-93010.20) and (T-93010.24),

\[
 \boxed{
 \mathrm{RH}
 \Longleftrightarrow
 \mathscr P_\circ(N)\ll(\log(2N))^A
 \text{ for some fixed }A.
 }
\tag{T-93010.25}
\]

The theorem identifies the full endpoint positive-current energy itself as a direct RH criterion. It does not establish the bound unconditionally.

## 7. Quantitative obstruction forced by an off-line zero

Suppose \(\zeta(\rho)=0\) with

\[
 \beta:=\Re\rho>\frac12.
\]

For every \(0<\varepsilon<\beta-1/2\), one cannot have

\[
 \mathscr P_\circ(N)
 =O\!\left(N^{2\beta-1-2\varepsilon}\right).
\tag{T-93010.26}
\]

Indeed (T-93010.9) would imply

\[
 M_\circ(N)=O(N^{\beta-\varepsilon}),
\]

then (T-93010.16) would give the same bound for real \(X\), making (T-93010.13) holomorphic in \(\Re z>\beta-\varepsilon\), a domain containing \(\rho\). This contradicts the nonremovable pole at \(\rho\).

Equivalently, every hypothetical zero of depth \(\beta-1/2\) forces endpoint positive energy above every exponent strictly below

\[
 N^{2\beta-1}.
\]

This is a direct pole-to-positive-current growth adapter, not an inertia or negative-mass surrogate.

## 8. Relation to the dormant Q4 frontier

The earlier Q4 work gave exact inverse-Laplacian, Haar, character, and Goldbach coordinates for \(\mathscr P_\circ(N)\), but `R-90412` correctly restored the coarse nonmean modes as open. The present theorem does not claim those modes are easy. Instead it proves that:

```text
complete endpoint PIG energy
    -> zero-safe mean by exact positive coercivity
    -> Mellin pole exclusion
    -> RH.
```

Therefore any source-specific Fourier, Goldbach, Haar, or finite-compression estimate can now target the complete energy and feed a direct consumer without reconstructing the disputed global block adapter.

## 9. Proof boundary

Established, subject to independent review:

1. exact complete endpoint field and normalization;
2. exact mean formula;
3. coefficient-one variance/coercivity identity;
4. exact Mellin transform and open-strip zero safety;
5. discrete-endpoint-to-real interpolation;
6. endpoint PIG implies RH without the global QIDR adapter;
7. RH implies endpoint PIG;
8. quantitative positive-energy obstruction from any off-line zero.

Open:

1. an unconditional polylogarithmic bound for \(\mathscr P_\circ(N)\);
2. the source-specific low-frequency / weighted-Goldbach estimate;
3. RH.
