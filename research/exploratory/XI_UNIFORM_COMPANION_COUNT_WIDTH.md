# Actual-Xi uniform companion count and geographic shrinking-band bound

Status: NEW LOCAL ANALYTIC PROOF AND BOUNDED EXACT CONTROLS.
Independent frozen-SHA review required before import.

Scope: the actual Xi function; a uniform count of zeros in a geographic disk;
finite denominator packets selected from actual zeros in bounded-height physical
windows; any genuinely inner numerator. No complete native cofinal denominator,
approximation-zero ledger, total-charge estimate, free-energy or RH conclusion.
RH remains unsolved.

Exact sources: ten Git/blob/LF-SHA-256 bindings in the manifest. In particular,
L-106610 means the file ending **riemann-siegel-gauge-factorization.md**, not
the different residue-sign file with the same historical claim ID. The
historical raw-value source convention is not repaired in place.

What was run: only bounded exact rational/Gaussian phase, Jensen-disk geometry,
factorial-envelope coefficient, scale-cancellation and squared width controls;
complete source/artifact authentication and strict report comparison. No
numerical Xi zeros, numerical integration or machine-verified analytic proof.

Smallest remaining native gap: establish that the denominator sections consumed
by the physical cofinal source really are the geographic packets below, with
all omitted, approximation, boundary and outer/source terms accounted for.
The local count is not such a capture theorem.

## 1. Uniform count for the two actual entire companions

Use the literal standard normalization
\[
 \Xi(z)=\xi_{\rm R}(1/2+iz)=\int_{\mathbb R}\Phi(u)e^{izu}\,du,
 \qquad \Phi(-u)=\Phi(u)>0.
\]
The bound source XL1--XL4 proves that \(\Phi=2\phi_0\), where \(\phi_0\)
is its theta series; this is a scalar correction, with NO frequency rescaling.
Its global real-tail inequality XL11 gives
\[
 \Phi(u)\le6\pi^2\exp(9u/2-\pi e^{2u}),\qquad u\ge0.       \tag{UC1}
\]
For \(0\le\lambda\le1\), define the entire functions
\[
 H_{0,\lambda}=\Xi+i\lambda\Xi',\qquad
 H_{5,\lambda}=\Xi^{(5)}-i\lambda\Xi^{(6)}.
\]
There is an absolute constant \(C\), independent of \(R\ge1\) and
\(\lambda\in[0,1]\), such that, counting all complex zeros with multiplicity,
\[
 \boxed{n(H_{0,\lambda};|z|\le R)+
        n(H_{5,\lambda};|z|\le R)\le C R\log(R+2).}         \tag{UC2}
\]
No zero separation, RH, height budget, polynomial approximation or
fixed-order derivative zero-count asymptotic is used.

### Growth, directly from the primitive kernel

For integers \(0\le r\le6\), the nonnegative exponential series gives
\(u^r\le r!e^u\) for \(u\ge0\). The tail (UC1) justifies entire
differentiation on every compact set and gives, for \(|z|\le R\),
\[
\begin{split}
 |\Xi^{(r)}(z)|
 &\le12\pi^2r!\int_0^\infty
                \exp((R+11/2)u-\pi e^{2u})\,du\\
 &\le 6\pi^2r!\pi^{-a}\Gamma(a),\qquad
                 a=R/2+11/4.                           \tag{UC3}
\end{split}
\]
The substitution is \(v=\pi e^{2u}\); extending the resulting positive
integral from \([\pi,\infty)\) to \((0,\infty)\) gives the second line.
Real-positive Stirling, or its elementary integral bound, implies
\[
 \log^+\max_{|z|\le R,\,0\le r\le6}|\Xi^{(r)}(z)|
       \le C_1 R\log(R+2),\qquad R\ge1.                  \tag{UC4}
\]
For example the Gamma expansion is classical
[DLMF 5.11.1](https://dlmf.nist.gov/5.11.E1).
The same growth bound, after changing the constant, holds for both
\(H_{k,\lambda}\) uniformly over \(0\le\lambda\le1\).

### Two fixed, noncancelling basepoints

Put
\[
 h(v)=\Xi(iv)=2\int_0^\infty\Phi(u)\cosh(vu)\,du.
\]
Every derivative \(h^{(r)}(1)\), \(r\ge0\), is strictly positive: for even
\(r\) its integrand is \(u^r\Phi(u)\cosh u\), and for odd \(r\) it is
\(u^r\Phi(u)\sinh u\). Evenness of Xi and the chain rule give
\[
 \boxed{H_{0,\lambda}(i)=h(1)+\lambda h'(1)\ge h(1)>0,}    \tag{UC5}
\]
\[
 \boxed{H_{5,\lambda}(-i)
   =i\{h^{(5)}(1)+\lambda h^{(6)}(1)\},\quad
   |H_{5,\lambda}(-i)|\ge h^{(5)}(1)>0.}                 \tag{UC6}
\]
The second quantity is imaginary; only its modulus is ordered. The fixed
signs and the opposite basepoints prevent cancellation uniformly in lambda,
including both endpoints of the closed interval.

For the first companion center Jensen's formula at \(i\), and for the second
at \(-i\). The disk \(|z|\le R\) lies in the corresponding disk of radius
\(r_R=R+1\). Every zero in that inner disk contributes at least \(\log2\)
to Jensen's integrated count at outer radius \(2r_R\). This outer circle lies
in \(|z|\le2R+3\). Thus, for the appropriate center \(c\),
\[
 n(H;|z|\le R)\log2
 \le \log\max_{|z-c|\le2(R+1)}|H(z)|-\log|H(c)|.          \tag{UC7}
\]
Jensen is valid also when a chosen outer circle contains zeros, by the
integrable logarithm formula or a limit from nearby regular radii. Its
inner boundary zeros still have weight at least \(\log2\).
Equations (UC4)--(UC6) prove (UC2).
When using (UC3) on the outer disk its Gamma parameter is \(R+17/4\),
not \(R/2+11/4\). This shift is retained in the exact geometry controls.

For \(D_\lambda=H_{0,\lambda}H_{5,\lambda}\), its zero count is the sum,
with multiplicity. Removing common numerator/denominator factors only lowers
it. In contrast, the elementary polynomial degree \(2\deg p-5\) does not
by itself prove a bound on entire companion zeros or a cofinal section.

## 2. Match the physical constant scale, not a Fourier multiplier

The exact frozen Riemann--Siegel source has, on its \(j\)-th physical
subwindow of \([T,2T]\),
\[
 \lambda_j=\omega(t_j)^{-1},\quad
 \omega=\vartheta',\quad
 t_j\in[T,2T],\quad J_T=\lceil(\log T)^B\rceil,\quad B>0
 \text{ fixed}.
\]
The disambiguated L-106610 gauge file gives
\[
 \omega(t)=\tfrac12\log(t/(2\pi))+O(t^{-2}).
\]
In particular \(0<\lambda_j\le1\) eventually, uniformly in \(j\).
Define the single parameter of that same constant companion by
\[
 \boxed{X_j:=2/\lambda_j=2\omega(t_j)
       =\log(t_j/(2\pi))+O(T^{-2}).}                     \tag{UC8}
\]
This is exact parameter matching, not the substitution \(\lambda=2/\xi\)
as a function of Fourier frequency. No gauge, outer factor or physical inner
multiplier is commuted through a Fourier projector.

For every fixed positive odd \(K\) and fixed \(M>0\), the reviewed
actual-Xi source envelope CB18--CB20 encloses
\[
 \{\xi\in[X_j/2,2X_j]:|\rho_{K,\lambda_j}(\xi)|\le M\}
\]
by an interval of ABSOLUTE width
\[
\begin{split}
 \Delta_j
 &=\left(KM/\pi+o(1)\right)e^{-X_j}/X_j\\
 &=\boxed{\left(2KM+o(1)\right)
       [t_j\log(t_j/(2\pi))]^{-1}}.                     \tag{UC9}
\end{split}
\]
The errors are uniform in \(j\): \(\min_jX_j\to\infty\), the original
envelope error is uniform on that tail, and (UC8) is uniform on the dyadic
interval. In particular \(\Delta_{\max}=O_{K,M}(1/(T\log T))\).
For the native fifth-endpoint use \(K=5\). Other fixed \(K\) in (UC9)
merely label the same proved source-envelope family, not a different
endpoint index assertion. No growing-\(K\), growing-\(M\), or coverage of
accepted frequencies outside \([X_j/2,2X_j]\) is claimed.

## 3. Finite geographic/shallow packet theorem

Fix \(\eta>0\) and a geographic constant \(C_0>0\). In window \(j\), select
a finite multiset of actual zeros of \(D_{\lambda_j}^{\rm red}\) satisfying
\[
 |b|\le C_0T,\qquad 0<\Im b\le\eta,                     \tag{UC10}
\]
with no multiplicity exceeding that of the actual divisor. This includes
ordinary mesoscopic intervals and bounded collars whenever those collars
stay in the declared disk. Reusing a zero in several different windows is
allowed and counted separately. Let \(n_j\) be the number selected and
\(Y_j=\sum\Im b\). Then (UC2), independently of any historical height transfer,
gives
\[
 n:=\sum_j n_j=O_{C_0}(J_TT\log T),\qquad
 Y:=\sum_jY_j\le\eta n.                                \tag{UC11}
\]
There is no claim \(n\le N_0+N_5\sim2N\); the weaker bound is enough here.

Let \(B_{-,j}\) be the finite Blaschke product of the selected nodes and let
\(B_{+,j}\) be ANY genuine upper-half-plane inner function. It may be
infinite, have singular inner factors, and depend arbitrarily on \(T,j\).
In the physical Fourier convention of the bound Hardy source, synthesize
any basis of \(K_{B_{-,j}}\) by \(E_j\), put \(G_j=E_j^*E_j\), and set
\[
 H_{I_j}=E_j^*M_{B_{+,j}}^*\Pi_{I_j}M_{B_{+,j}}E_j.
\]
Here \(I_j\) is the accepted envelope interval of Section 2 or any measurable
subset of it. For an empty packet its traces are zero; no empty Gram inverse
is formed. The all-inner theorem IW1 gives
\[
 \operatorname{tr}(G_j^{-1}H_{I_j})
 \le c\sqrt{\Delta_j n_jY_j}
 \le c\sqrt{\Delta_{\max}\eta}\,n_j,\qquad
 c=16/\pi^{3/2}<4.
\]
Consequently, for \(N_T=N(T,2T)\asymp T\log T\),
\[
 \boxed{\frac{\sum_j\operatorname{tr}(G_j^{-1}H_{I_j})}{N_T}
   =O_{K,M,\eta,C_0}\left(\frac{J_T}{\sqrt{T\log T}}\right)
   =o(1).}                                            \tag{UC12}
\]
The last limit holds for every fixed \(B>0\). The classical Riemann--von
Mangoldt formula is \(N(0,t)=t(\log(t/(2\pi))-1)/(2\pi)+O(\log t)\);
subtracting at \(2T,T\) gives \(N_T\asymp T\log T\). For a primary modern
statement of this classical error scale see
[Hasanalizade--Shen--Wong, Section 1, (1.1)](https://arxiv.org/pdf/2107.06506v1).
No explicit modern numerical error constant is used. This total Xi count
only normalizes the statement; it is not used to infer a companion count.

### Corrected physical source

If the actual source has compatible local data \(N=OB_+\), \(D=OB_-\)
(or \(D=O\widetilde B_-\) with the retained finite divisor a subfactor),
and \(R=N-D\), where \(O\) is holomorphic and nonzero at retained nodes,
then in the explicit column-kernel convention
\[
 A=J_{B_+}^*,\quad C=J_O^*,\quad R_c=J_R^*=CA=AC,\quad
 G_O=C^*GC.
\]
The finite jets of \(D\) vanish through the retained multiplicities. The
Hardy source proves the exact physical band identity and contraction
\[
 \operatorname{tr}(G_O^{-1}R_c^*H_IR_c)
   =\operatorname{tr}(AG^{-1}A^*H_I)
   \le\operatorname{tr}(G^{-1}H_I).                     \tag{UC13}
\]
Thus the same normalized conclusion holds for these compatible physical
source traces. In the HT4 derivative basis all coefficient matrices must
also have its diagonal \(i^r\) phase conjugation. Raw value jets \(J_{B_+}\)
are not the Riesz coefficient matrix \(A\). No claim here authenticates
the old raw-\(V^*GV\) physical determinant.

If, additionally and independently, the retained packets satisfy
\(Y=O(N_T)\), Cauchy--Schwarz instead gives the improvement
\[
 \frac{\sum_j\operatorname{tr}(G_j^{-1}H_{I_j})}{N_T}
 \le c\sqrt{\Delta_{\max}(n/N_T)(Y/N_T)}
 =O\left(\sqrt{\frac{J_T}{T\log T}}\right).              \tag{UC14}
\]
This conditional variant does NOT import or reprove the cofinal height
claim of L-106621. Equation (UC12) needs no such claim.

## 4. What remains unpaid in a native cofinal application

The theorem controls actual zeros in a geographic disk and finite factors
made from those zeros. It does not establish that the frozen cofinal source
uses exactly those factors. In particular:

- A truncation degree can go to infinity at fixed physical \(T\); its full
  denominator is not automatically bounded by (UC11).
- Local uniform approximation alone does not declare which finite
  denominator directions, outer factors and source jets the physical
  model-space functional retains.
- Choosing collars within a fixed disk is harmless for this count, but it
  does not prove their topological/source contribution is \(o(N_T)\).
- An entire or global infinite denominator requires a capture/tail theorem,
  not merely the all-inner NUMERATOR extension of IW1.

One sufficient remaining interface is a specified cofinal family whose
retained denominator rank is uniformly \(O(J_TT\log T)\) and height is
uniformly shallow, together with compatible physical source jets and a
separately bounded omitted-direction/boundary/approximation contribution.
Alternatively one may identify the source exactly with the actual
geographic packets (UC10). The required order of approximation, geographic
selection and \(T\to\infty\) is part of that interface. No approximation
zero ledger or interchange of these limits is proved here.

A concrete count warning uses \(F(z)=\cos z\) and \(0<\lambda<1\).
Let \(a=\operatorname{artanh}\lambda\). The upper zeros of its reduced
fifth-endpoint denominator are exactly
\[
 z=k\pi+ia,\qquad k\in\mathbb Z,
\]
whereas the upper numerator zeros are
\(\pi/2+k\pi+ia\), so no such zeros cancel. Indeed
\(F+i\lambda F'=\cos z-i\lambda\sin z\) has only lower zeros, while
\(F^{(5)}-i\lambda F^{(6)}=-\sin z+i\lambda\cos z\) has these upper zeros.
Every fixed geographic disk has finitely many, but the full denominator
has infinitely many at the same height. For \(\lambda=1/200\),
\[
 a\le\lambda/(1-\lambda^2)=200/39999<1/100.
\]
Thus even a fixed shallow cutoff does not turn the entire denominator into a
finite packet. This is an elementary entire countercontrol with a positive
even atomic Fourier source, not Xi and not a refutation of Xi-specific
capture. It illustrates the order-of-limits issue, not a new total-charge no-go.

Finally (UC12) is an absolute trace divided by \(N_T\). It is NOT a vanishing
source-relative bound \(S_I/Q\), a vanishing Loewner constant, or a statement
that \(\beta/n\) can replace \(\beta\) in a relative inequality. It gives no
bound on total \(Q\), no deletion of topological charge and no critical-line
percentage or RH implication.

## 5. Classical ingredients and exact replay boundary

Jensen's formula, elementary theta/Gamma growth, Stirling, and the
Hausdorff--Young/Takenaka--Malmquist estimate are classical ingredients.
The contribution is the explicit uniform two-anchor actual-Xi count and its
source-matched, carefully geographic application. No external priority or
novelty claim is made. A bounded overlap check identified the existing Xi
source-Pick and Riemann-structures programmes; this packet preserves their
open cofinal boundary.

The producer authenticates all ten frozen source blobs and LF-normalized
hashes before building the report. Its fixture binds this note, the producer,
the tests and manifest by LF hashes, and acceptance requires complete typed
canonical-JSON equality. Remote formula references authenticate metadata only.
Bounded arithmetic uses exact rationals and integer pairs for powers of \(i\);
there is no floating-point Xi or transcendental evaluation.

Controls cover derivative phases through order six, the two noncancelling
anchors and opposite-sign negative controls, nonnegative Taylor coefficient
witnesses for the factorial envelope, both Jensen centers and shifted radii,
exact \(\lambda X/2=1\), symbolic pi cancellation in (UC9), and squared
Cauchy--Schwarz/shallow/height-budget inequalities on explicit finite panels.
They verify these finite algebraic parts, NOT positivity of the actual
kernel, Gamma asymptotics, Jensen's theorem, arbitrary inner limits, or the
unbounded analytic conclusion.

Public controls have derivative order at most six, at most eight windows,
rank per window at most 1024, 16-bit input rationals and 256-bit internal
rationals. Booleans, floating point, malformed structures, oversized inputs,
nonfinite JSON and duplicate JSON keys fail closed. Source and artifact files
are size-capped. Result-bearing checks do not rely on Python assertions.

Replay commands:
~~~text
python -B research/exploratory/xi_uniform_companion_count_width.py --check
python -B -O research/exploratory/xi_uniform_companion_count_width.py --check
python -B -m unittest discover -s tests -p test_xi_uniform_companion_count_width.py
python -B -O -m unittest discover -s tests -p test_xi_uniform_companion_count_width.py
~~~

An independent exact-SHA proof/code audit is required before accepting this
packet. The author controls are not that independent review.

Author replay: all 32 tests and both producer modes passed in normal Python
and under -O; Ruff format/lint and whitespace checks passed. These are bounded
algebra/source checks, not a numerical zero census or independent proof audit.
