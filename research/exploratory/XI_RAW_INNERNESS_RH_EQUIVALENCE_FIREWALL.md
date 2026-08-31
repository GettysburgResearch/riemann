# Raw Xi innerness is RH-equivalent: hypothesis-strength firewall

Status: source-bound theorem and release-scope clarification; root review required.
Base: PB science 740b497e99e6e6fb274684cc53599302402f2718.
No frozen scientific packet is changed. This note does not prove RH and does
not invalidate any correctly conditional Hardy-space theorem.

## 1. Exact theorem, normalization and quantifiers

Use the actual centered function, with GH1/GC1 normalization:

\[
 f(z)=\Xi(z)=\xi_{\rm R}(1/2+iz),\qquad
 \xi_{\rm R}(s)=\tfrac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s).
\]

Here Xi already denotes the centered function; it must not be composed again
with \(1/2+iz\). Put \(f_k=f^{(k)}\), and for one fixed constant
\(\lambda>0\) define the meromorphic quotients after removable cancellations:

\[
 \Theta_{k,\lambda}(z)=
 \frac{f_k(z)-i\lambda f_k'(z)}{f_k(z)+i\lambda f_k'(z)},
 \qquad k=0,5.
 \tag{HI1}
\]

A Schur function here is holomorphic on ALL of \(\mathbb C_+\) with modulus
at most one. An inner function is such a function with unimodular boundary
values almost everywhere. Merely meromorphic continuation and unimodular
real-axis values are not this definition.

**Theorem.** For each fixed positive \(\lambda\), the following are equivalent:

1. RH.
2. \(\Theta_{0,\lambda}\) is a Schur function on \(\mathbb C_+\).
3. \(\Theta_{0,\lambda}\) is inner on \(\mathbb C_+\).
4. Both \(\Theta_{0,\lambda}\) and \(\Theta_{5,\lambda}\) are inner there.

Thus existence of even ONE positive parameter satisfying condition2,3 or4
is equivalent to RH; under RH all positive parameters satisfy them. No
simplicity hypothesis for zeros of Xi is used.

## 2. The reverse implication: complex zeros cannot be hidden by cancellation

The following local calculation applies to any nonzero entire function \(h\).
If \(b\) is a zero of multiplicity \(m\ge1\), write
\(h(z)=(z-b)^m a(z)\), with \(a(b)\ne0\). For fixed \(\lambda>0\),

\[
 h\pm i\lambda h'
 =(z-b)^{m-1}
 \bigl((z-b)a\pm i\lambda[ma+(z-b)a']\bigr).
 \tag{HI2}
\]

Both bracketed factors are nonzero at b. Exactly \(m-1\) common powers
cancel; this is GC7, including its explicit COMPLEX-zero scope. The resulting
analytic germ satisfies

\[
 \Theta_h(z)
 =-1+\frac{2(z-b)a(z)}
 {(z-b)a(z)+i\lambda[ma(z)+(z-b)a'(z)]}
 =-1-\frac{2i}{\lambda m}(z-b)+O((z-b)^2).
 \tag{HI3}
\]

In particular
\(\Theta_h(b)=-1\) and \(\Theta_h'(b)=-2i/(\lambda m)\ne0\).

Suppose condition2 holds and \(f\) has a zero b in \(\mathbb C_+\).
The removable germ HI3 is the unique continuation of the displayed quotient.
It attains modulus one at an interior point, contradicting the
[maximum-modulus principle, DLMF1.10(v)](https://dlmf.nist.gov/1.10#v).
There is no constant-function escape: HI3 already has nonzero derivative;
alternatively \(\Theta_0\equiv-1\) would imply \(2f\equiv0\), whereas
\(f(0)=\int_{\mathbb R}\Phi(u)\,du>0\).

The same contradiction can be seen directly without the maximum principle:
at \(z=b-i\varepsilon\), for sufficiently small positive
\(\varepsilon<\Im b\), HI3 gives
\(\Theta_0(z)=-1-2\varepsilon/(\lambda m)+O(\varepsilon^2)\), whose
modulus is greater than one.

The actual f is real entire and even, by GH1's positive even Fourier kernel.
Consequently a lower-half-plane zero would have an upper-half-plane reflected
zero. There are no nonreal zeros. All zeros of the centered completed Xi
being real is precisely RH; the completion removes the trivial zeta zeros.
See the normalization/reflection in [DLMF25.4.3--4](https://dlmf.nist.gov/25.4)
and the critical-strip statement in [DLMF25.10(i)](https://dlmf.nist.gov/25.10#i).
This proves condition2 implies condition1.

## 3. Converse and the role of the fifth derivative

The converse is already proved in frozen GH, Section2, equations GH6--GH7
(lines78--113), not supplied by finite sampling. Under RH the order-at-most-one
even f has the locally uniform paired product

\[
 f(z)=f(0)\prod_{\gamma>0}(1-z^2/\gamma^2)^{m_\gamma},
 \qquad \sum_{\gamma>0}m_\gamma/\gamma^2<\infty.
\]

The logarithmic derivative is a normally convergent paired sum of real-root
terms \(m/(z-r)\), each having negative imaginary part in \(\mathbb C_+\).
Thus \(\Im(f'/f)<0\). With \(w=i\lambda f'/f\), one has \(\Re w>0\), so
\((1-w)/(1+w)\) is holomorphic and strictly contractive in \(\mathbb C_+\).
On the real line it is unimodular after the removable cancellations HI2.
Hence \(\Theta_{0,\lambda}\) is inner.

Finite paired-product approximants have only real zeros. Their fifth
derivatives have only real zeros by Rolle, converge locally uniformly to
\(f^{(5)}\), and this limit is not identically zero. Hurwitz therefore gives
only real zeros for \(f^{(5)}\). GH's parity/Hadamard and logarithmic-derivative
argument applies again, giving \(\Theta_{5,\lambda}\) inner.
The actual-kernel moment \(f^{(6)}(0)=-\int u^6\Phi(u)\,du\ne0\) pays
nonvanishing of this derivative. This proves condition1 implies condition4.
Condition4 implies3 implies2 by definition, closing all equivalences.

Exclusions are essential:

- At \(\lambda=0\), the quotients are identically one after removal, with
  no implication for RH.
- No equivalence between Theta5 ALONE being inner and RH is asserted.
  There is no general reverse-Rolle inference: the NONNATIVE polynomial
  \(h(z)=z^6+1\) has nonreal zeros, while \(h^{(5)}=720z\) and its fifth
  companion is the inner function \((z-i\lambda)/(z+i\lambda)\).
- Variable \(\lambda(z)\), reversed half-plane/sign conventions and a
  different primitive entire function are not the theorem's statement.

As a second exact NONNATIVE illustration, for \(h=(z^2+1)^m\), \(\lambda=1\),
the reduced quotient is
\((z^2+1-2imz)/(z^2+1+2imz)\). Its value at \(z=i/2\) is
\(-(4m+3)/(4m-3)\), of modulus greater than one for every integer \(m\ge1\).
It is nevertheless unimodular at every real point. These elementary controls
illustrate the distinctions; they are not proofs of the analytic quantifiers
or statements about actual Xi zeros.

## 4. Release interpretation and cancellation boundaries

| statement or object | hypothesis status |
|---|---|
| Certified finite raw companion zeros, noncommon guards and native meromorphic-quotient divisors | Unconditional where the frozen local certificates prove them |
| Raw imaginary-axis values and the fixed-lambda axis asymptotics | Unconditional analytic identities/estimates; numerical enclosures are finite certificates |
| Normalized Hardy-kernel Gram matrices and the certified finite point geometry | Unconditional for the certified upper-half-plane nodes |
| General LB1 inequality for an arbitrary supplied inner U | Valid general Hardy theorem under that explicit hypothesis; it does not itself assert RH |
| Actual-Xi LB/PB physical bounds using the stated two-raw-component inner premise | RH-conditional by HI1--HI3; the numerical right-hand sides remain unconditional evaluations |
| GC countable exceptional-set theorem and cancellation-safe common-zero test | Unconditional |
| GC reduced pure-component heights and bare traces | Require RH and the separately stated avoidance of the exceptional parameter set |
| Infinite corrected physical capture, uniform/cofinal alignment and native outer-metric transfer | Not supplied by RH-equivalence or by a finite positive floor |

LB lines54--68 and PB Section1 (lines20--27) assume the RAW functions admit

\[
 \Theta_0=\Gamma U,\qquad \Theta_5=\Gamma B
 \quad\hbox{with }\Gamma,U,B\hbox{ inner}.
 \tag{HI4}
\]

This implies both raw functions are inner, hence RH. Conversely RH supplies
the inner components and their common-inner reduction. In the fixed positive
PB calibration this is an RH-equivalent premise, not a lesser condition whose
global verification would avoid RH.

A statement merely that the native meromorphic ratio
\(\Theta_0/\Theta_5\) is representable as a quotient of two inner functions
is DIFFERENT. It does not assert that either raw component is inner or that
the common prefactor Gamma is inner. LB/PB specifically need
\(|\Gamma(z)|\le1\) to infer \(|U(z)|\ge|\Theta_0(z)|\) at their evaluation
points. An arbitrary quotient-of-inners representation does not supply that
comparison and cannot silently replace HI4.

Internal cancellation HI2 and cross-component common-inner reduction HI4
are different operations. Neither a finite zero census, a few contractive
raw samples, nor positive Gram geometry verifies global raw innerness.
This note strengthens the explicit hypothesis classification, not any
conclusion: all valid conditional theorems and unconditional finite
certificates retain their stated scope. No RH proof, cofinal capture theorem
or new positivity principle is claimed.

## 5. Frozen proof bindings and review record

All four paths below are under research/exploratory/. Their complete proof
texts or load-bearing sections were read, and the raw Git blob identity and
CRLF-to-LF SHA-256 were independently recomputed. No remote bytes are sealed.

GH: XI_COMPANION_GLOBAL_HEIGHT_BOUNDARY.md

    commit: 9da33e7ea2b15a4badb3cb436e38e54762ad5e1d
    git_blob: e592a4c031876f56f07d28b7e18a8a7cf6e826f4
    sha256_lf: 5bf33ffd58c3fe277f4bfb0408f0805eae1b2f34aab49bb71e4c714afb80dc6d

GH1--GH2 fix normalization and orientation; GH6--GH7 prove the RH-to-inner
direction, including fifth derivatives and multiple real roots.

GC: XI_COMPANION_GENERIC_PARAMETER_COPRIMALITY.md

    commit: d76a1a8eb8ec40b19a351af95439b9a6514bee87
    git_blob: 797f7b581580ad5a441c7702015c64a53eca6f4d
    sha256_lf: 55aa96745c3f269ac464ea7c0b8227e14e7d8ceb33f8bec2fc13f9642b33d44d

GC1--GC2 fix the same primitive; GC7 proves the complex-zero removable
factor calculation; Section4 (lines154--164) states the downstream premise.

LB: XI_LAPLACE_LOW_PASS_LOWER_BOUND.md

    commit: a7479e85fdc2a464cdc753021435cfef7a1f3910
    git_blob: 90e6bd89ca9a23c401d6d947c04a9d548f6b3030
    sha256_lf: c56d29037b85c45398bcb34dc7fb8450ba0e4b0f32fa7293edcaf5d1d2ea4b64

LB1 is the general physical projection inequality; LB2 and Section2 specify
the raw-component/common-inner substitution and the actual Xi calibration.

PB: XI_FIXED_LAMBDA_SHRINKING_PHYSICAL_BANDS.md

    commit: 740b497e99e6e6fb274684cc53599302402f2718
    git_blob: e336c2c145172277aa7ba9d1698de10334deb5e6
    sha256_lf: 878f94e37abed7eac0b2096185dad30be4874fe673ac95324377805140f1bc29

PB Section1 and PB1--PB3 state the fixed calibration, exact two-component
premise, scalar comparisons and finite physical interpretation.

This short analytic synthesis adds no producer, fixture, machine-certified
infinite quantifier or additional packet count. Its proof uses the local
calculation HI2--HI3 and the classical maximum-modulus principle, together
with the exact accepted GH converse. No global-novelty claim is made.

Verification for this note: all four frozen proof bindings were checked,
and the last rational illustration was independently evaluated for m=1,...,16.
UTF-8/control-byte and base-to-head whitespace checks passed. No parent
producer suite was rerun and no finite check is used to prove the theorem.
