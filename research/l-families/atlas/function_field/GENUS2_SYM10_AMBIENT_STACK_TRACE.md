# The marked ambient genus-two \(\operatorname{Sym}^{10}\) trace

Status: **PROVED as an exact Frobenius-trace identity** for every odd prime
power, conditional only on the direct curve-open theorem source-locked at
commit `42910253be8173c6cd0de19a7a7403d0c31b5c22` and the standard elliptic
Eichler--Shimura identities used in the explicit decomposable-stratum
calculation.

Scope: the compactly supported virtual trace of the local system
\(V_{(10,0)}\) on \(\mathcal A_2(w^1)\), the stack of principally polarized
abelian surfaces with one ordered Weierstrass/partial-level-two label.  This
is not a claim about an individual cohomology group or a motivic isomorphism.

What was actually run: exact representation-ring, modular-trace, and sparse
polynomial algebra.  No finite field, curve, abelian surface, or cohomology
group is enumerated.

## 1. Result

Write \(\Theta_\Delta(q)\) for the prime-power Frobenius trace of the unique
normalized level-one cusp form of weight twelve.  Then, for every odd prime
power \(q\),

\[
\boxed{
 \operatorname{Tr}\!\left(
 F_q,e_c(\mathcal A_2(w^1),V_{(10,0)})
 \right)
 =2-4q-2q\Theta_\Delta(q).}                                  \tag{1}
\]

The striking feature is what is absent.  The weight-eight and weight-ten
newform traces on \(\Gamma_0(2)\), which occur separately on the smooth-curve
and decomposable strata, cancel exactly in their union.

The exact control values are

| \(q\) | ambient trace |
|---:|---:|
| 3 | -1,522 |
| 5 | -48,318 |
| 7 | 234,390 |
| 9 | 5,234,186 |

The \(q=9\) row uses the Frobenius-root power sum
\(\Theta_\Delta(9)=-290790\), not merely the Fourier coefficient at index
nine.

## 2. Curve-open input

The source-locked direct character-sum theorem gives

\[
\begin{aligned}
 T_{\mathrm{open}}(q)
 &:={\rm Tr}\!\left(
 F_q,e_c(\mathcal M_2(w^1),V_{(10,0)})
 \right)\\
 &=(q-1)\Theta_\Delta(q)
   -\Theta_{8,2}(q)-\Theta_{10,2}(q)-q-7.                    \tag{2}
\end{aligned}
\]

Here \(\Theta_{8,2}\) and \(\Theta_{10,2}\) are the traces of the unique
newforms in weights eight and ten on \(\Gamma_0(2)\).  Equation (2) is an
all-field theorem, not an interpolation from the displayed controls.

## 3. Exact decomposable boundary

The complement of the smooth Jacobian locus is the decomposable stack

\[
 \mathcal A_{1,1}(w^1)
 \cong Y_0(2)\times\mathcal A_1.                              \tag{3}
\]

On a product of elliptic curves, an odd genus-two theta characteristic is
odd on one factor and even on the other.  It therefore distinguishes the two
factors and marks a nonzero two-torsion point on the even factor.  This is why
the stratum is the ordered product in (3), rather than a quotient by \(S_2\).
Since
\(V_{(10,0)}=\operatorname{Sym}^{10}V\) and
\(V|_{\mathrm{SL}_2\times\mathrm{SL}_2}=W_1\boxplus W_1\),

\[
 V_{(10,0)}\big|_{\mathrm{SL}_2\times\mathrm{SL}_2}
 =\bigoplus_{i=0}^{10}W_i\boxtimes W_{10-i}.                  \tag{4}
\]

This identity is verified both by the symmetric-power binomial rule and in
a two-variable Laurent-character ring.  The dimensions sum correctly:

\[
 \sum_{i=0}^{10}(i+1)(11-i)=\binom{13}{10}=286.
\]

Odd summands vanish because the central involution acts nontrivially on the
unmarked \(\mathcal A_1\) factor.  For even \(r\), the exact elliptic-stack
formulas are

\[
\begin{array}{c|c|c}
r&e_c(\mathcal A_1,W_r)&e_c(Y_0(2),W_r)\\ \hline
0&\mathbb L&\mathbb L-1,\\
r\ge2&-S[r+2]-1&-S[\Gamma_0(2),r+2]-2.
\end{array}                                                    \tag{5}
\]

At the relevant weights,

\[
\begin{aligned}
 S[\Gamma_0(2),8]&=\Phi_{2,8},\\
 S[\Gamma_0(2),10]&=\Phi_{2,10},\\
 S[\Gamma_0(2),12]&=2S[12],
\end{aligned}                                                  \tag{6}
\]

and the level-one cusp spaces in weights four, six, eight, and ten vanish.
The six even rows of (4) therefore contribute

\[
\begin{array}{c|c}
i& e_c(Y_0(2),W_i)e_c(\mathcal A_1,W_{10-i})\\ \hline
0&-(\mathbb L-1)S[12]-\mathbb L+1,\\
2&2,\\
4&2,\\
6&\Phi_{2,8}+2,\\
8&\Phi_{2,10}+2,\\
10&-2\mathbb L S[12]-2\mathbb L.
\end{array}                                                    \tag{7}
\]

Summing gives the exact identity in the formal compact-support trace-channel
ring,

\[
\boxed{
 e_c(\mathcal A_{1,1}(w^1),V_{(10,0)})
 =(1-3\mathbb L)S[12]+\Phi_{2,8}+\Phi_{2,10}
  -3\mathbb L+9.}                                             \tag{8}
\]

Equivalently, its Frobenius trace is

\[
 T_{\mathrm{bdry}}(q)
 =(1-3q)\Theta_\Delta(q)+\Theta_{8,2}(q)+\Theta_{10,2}(q)
  -3q+9.                                                       \tag{9}
\]

## 4. Cancellation and interpretation

The stack decomposition

\[
 \mathcal A_2(w^1)
 =\mathcal M_2(w^1)\sqcup\mathcal A_{1,1}(w^1)               \tag{10}
\]

is additive for compactly supported virtual traces.  Adding (2) and (9)
cancels \(\Theta_{8,2}\) and \(\Theta_{10,2}\), while

\[
 (q-1)+(1-3q)=-2q,
 \qquad (-q-7)+(-3q+9)=2-4q.
\]

This proves (1).

In Grothendieck-class notation the resulting trace pattern is

\[
 2-4\mathbb L-2\mathbb L S[12].                              \tag{11}
\]

Equation (11) records the virtual trace pattern proved here.  Equality of
all these alternating traces is not, by itself, an isomorphism of motives,
a splitting of individual \(H_c^i\), or a proof that no canceling pieces are
present.  Earlier level-two cohomological literature supplies a compatible
conjectural framework, but its nonregular, Eisenstein, endoscopic, and
ambient formulas are not inputs to the direct proof.

## 5. Scientific use and boundary

This is a concrete example of cohomological spectroscopy succeeding for an
inverse-designed family observable:

1. the smooth curve stratum exposes three modular channels;
2. the decomposable geometry supplies the exact counterchannels;
3. the ambient object retains only a Tate row and a Tate-shifted level-one
   weight-twelve channel.

It suggests searching for other local systems or virtual detectors whose
boundary subtraction isolates a single automorphic trace.  It gives no
memberwise sign, zero-free region, RH/GRH criterion, principal-member
amplifier, compatible system, or global Euler-product identity.  No external
novelty claim is made without a dedicated literature comparison.

## 6. Source and computation contract

The replay source-locks all four files of the direct \(\operatorname{Sym}^{10}\)
packet at commit `42910253be8173c6cd0de19a7a7403d0c31b5c22`.  It also
source-locks the exact marked-stack adapter at commit
`c8eff406f49daf9f09c0bb3e63e21659275d224e` and the earlier exact
decomposable-geometry reconciliation at commit
`e0da0f790f96f6dc5c03b363a9a01b91621ee113`.  Git-blob identities,
LF-normalized SHA-256 digests, JSON schemas, and canonical payload hashes are
checked before any imported result is used.

The producer then rebuilds, rather than imports, the following finite algebra:

1. the complete two-variable Laurent character of
   \(\operatorname{Sym}^{10}(W_1\oplus W_1)\) and all eleven branch summands;
2. the level-one and \(\Gamma_0(2)\) cusp-space dimensions in weights
   \(4,6,8,10,12\), including the two-copy oldspace and zero newspace at
   weight twelve;
3. the six nonzero rows of (7) in
   \(\mathbf Z[\mathbb L,S[12],\Phi_{2,8},\Phi_{2,10}]\);
4. the \(q\)-expansions of \(\Delta\), \(f_{8,2}\), and \(g_{10,2}\) through
   degree nine and the prime-power root recurrence at \(q=9\);
5. the complete channel cancellation leading to (1).

The fixed replay uses 1,116 guarded integer operations and reads twelve
source files totalling 203,618 bytes.  Its hard caps are 20,000 exact
operations, twelve source files, 65,536 bytes per source, 262,144 source bytes
in total, and five seconds of wall time.  There is no field or object sweep.

## Replay

```text
python -B research/l-families/atlas/function_field/genus2_sym10_ambient_stack_trace.py --check
python -B -O research/l-families/atlas/function_field/genus2_sym10_ambient_stack_trace.py --check
python -B -m unittest tests.test_genus2_sym10_ambient_stack_trace
python -B -O -m unittest tests.test_genus2_sym10_ambient_stack_trace
```
