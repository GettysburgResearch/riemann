# Independent audit of the scale-averaged extraction

Reviewer role: independent mathematical and source audit by audit_formalization. Date: 2026-10-10. This is a bounded review of an implication, not a proof of the unproved arithmetic moment premise, a fresh verification of the imported analytic manuscript, or a Lean kernel verification. No published source was changed.

## Exact reviewed source

The reviewed bytes were read directly from the local Git object database.

| Item | Immutable source |
|---|---|
| Commit | 6b4723042b3d250024eef45cb1924f88f28e902c (PR #917) |
| File | standalone/2026-10-10-oscillating-overlaps-and-averaged-moments/SCALE_AVERAGED_CRITERION.md |
| Bytes | 12,654 |
| SHA-256 | c6c543037312480fae6154f7a059248fe14658ecff6251aaecb80fe0fdbfd9c0 |

The review covers Sections 1–4 in full and the scope claims in Section 5. The universal smooth Mellin detector is a declared dependency, identified in the source as PR #912 at 6afd64e042ce7b59d550c3d76e9e2cca8b2c7379, MELLIN_AND_SPIKES.md, Proposition 1.1. This audit retains that previously supplied construction; it does not replace it with a claim that an arbitrary smooth test is nonvanishing.

**Verdict:** the moving-cutoff proof and the scale-averaged moment-to-zero-free implication pass this bounded audit. No mathematical must-fix was found. The argument retains the low-scale forcing term and does not assume integrability of the unknown tail in order to establish it.

## 1. Exact row copies and the moving cutoff

Write \(A_r(D)\) for the literal zero-extended Möbius/sextic sum with a fixed finite-order character, a fixed finite excluded-prime set, and the source's fixed test. The identity

\[
T_vA_r(D)=A_{rv^6}(D),
\qquad
T_vf(D)=\sum_{\operatorname{rad}(d)\mid v}\eta_r(d)f(D/Nd)
\]

is an exact coefficient identity. At a prime dividing \(v\), the geometric inverse cancels the original inverse Euler factor and thereby removes terms divisible by that prime. It does not introduce an unjustified coprimality condition between \(r\) and \(v\). If the fixed row already makes \(\eta_r(p)=0\), the local operator is the identity, as required.

There is one row \(rv^6\) for each ideal \(v\): choosing a different generator changes it by the sixth power of a field unit, which is one, and equality of two such rows implies equality of the underlying ideals. Therefore the source uses distinct rows without paying a fictitious multiplicity gain.

For the cutoff \(H=D^h\),

\[
Y_r(D)=(D^h/Nr)^{1/6}
\]

is the correct moving bound on the base norm. The argument works for each fixed \(r\) after \(D\) is sufficiently large. Constants may depend on \(r\), and no conclusion uniform over a growing conductor family is used.

Averaging over all ideal bases gives the exact coefficient

\[
w_Y(d)=\frac{J(Y/R_d)}{J(Y)},
\qquad R_d=N\operatorname{rad}(d).
\]

The estimate \(J(Y)=\kappa_KY+O(Y^{1/2})\), together with \(J(Y)\asymp Y\) for \(Y\ge1\), gives both estimates in source (2.2). When \(R_d>Y\), the numerator vanishes; the claimed minimum bound still holds because its smaller term is \(R_d^{-1}\). Interpolation with exponent \(2\delta\) gives

\[
|w_Y(d)-R_d^{-1}|
\ll Y^{-\delta}R_d^{-1+\delta},
\quad 0<\delta<\min(\sigma,1/2).
\]

Its weighted coefficient sum converges because the first nonconstant local exponent is \(1+\sigma-\delta>1\).

## 2. The inverse does not presume the desired conclusion

In the norm
\[
\|f\|_{p,\sigma}
=\left(\int |f(D)|^pD^{-p\sigma}\frac{dD}{D}\right)^{1/p},
\]
the causal dilation \(f(D/Nd)\) has norm at most \((Nd)^{-\sigma}\). On a truncated interval this remains true after extending the input by zero below the lower endpoint. Uniform coefficient majorants can therefore bound an operator whose actual coefficients depend measurably on \(D\).

The limiting Euler factors and their inverses in source (2.6)–(2.7) are algebraically correct:

\[
M_p=\frac{1-(1-q^{-1})z}{1-z},
\qquad
M_p^{-1}=1-q^{-1}\sum_{j\ge1}(1-q^{-1})^{j-1}z^j,
\quad z=\eta(p)S_p.
\]

Both have summable nonconstant weighted coefficient norms \(O_\sigma(q^{-1-\sigma})\). Thus the product inverse is a genuine bounded causal dilation operator. It is not an assertion about an \(L\)-function reciprocal near a zero.

For \(Y(D)\ge cD^\rho\), source Theorem 3.1 fixes a sufficiently large \(X_0\), then writes \(P=M+E\) on functions zero below \(X_0\). The perturbation estimate is uniform in the upper endpoint \(T\):

\[
\|E\|\ll c^{-\delta}X_0^{-\rho\delta}.
\]

The factorization \(P=M(I+M^{-1}E)\) is valid even though \(E\) need not commute with \(M\). The Neumann inverse is applied only after making \(\|M^{-1}E\|\le1/2\), and first on finite intervals \((X_0,T)\). Causality means the restrictions and compositions are consistent there.

The split \(f=f_0+f_1\) is essential. The compact lower part \(f_0\) has finite weighted norm because \(f\) is locally bounded and vanishes below a positive scale. Moreover,

\[
|Pf_0(D)|\ll\sum_dR_d^{-1}|f_0(D/Nd)|
\]

has finite weighted norm on the full upper interval, by the same convergent coefficient algebra. This controls the forcing of the tail by all smaller scales. The resulting bound for \(f_1\) is independent of \(T\), so monotone convergence yields tail integrability. There is no circular use of a putative infinite-interval norm of \(f_1\).

## 3. Exact sufficient arithmetic premise and conclusion

For a fixed integer \(k\ge1\), fixed \(h>0\), and fixed excess \(e\ge0\), the reviewed sufficient premise is: for every \(\epsilon>0\), all sufficiently large real \(X\),

\[
\int_X^{2X}
 \sum_{0<Nu\le D^h}|A_u(D;W_*)|^{2k}\frac{dD}{D}
 \ll_{k,h,e,\epsilon,\nu,S}
 X^{h+k+e+\epsilon}.
\tag{A}
\]

Here the character \(\nu\), excluded primes \(S\), and test \(W_*\) are fixed before the scale tends to infinity. The source states the slightly stronger version for every \(X\ge2\). Eventual bounds suffice because the arithmetic sums are locally bounded. For the proof it also suffices to have (A) on every sufficiently large member of one fixed dyadic ladder; a sparse sequence leaving uncontrolled gaps does not suffice.

Jensen's inequality at the exact moving cutoff gives

\[
|M_{Y_r(D)}A_r(D)|^{2k}
\ll_r D^{-h/6}\sum_{0<Nu\le D^h}|A_u(D)|^{2k}.
\]

After multiplying by \(D^{-2k\sigma}\) and integrating over a dyadic interval, the exponent is

\[
k+\frac{5h}{6}+e-2k\sigma+\epsilon.
\]

It is negative for a sufficiently small \(\epsilon>0\) precisely when

\[
\sigma>\beta_{k,h,e}
=\frac12+\frac{5h}{12k}+\frac{e}{2k}.
\]

The moving-cutoff theorem applies with \(\rho=h/6>0\), giving the weighted \(L^{2k}\) norm of each fixed-row sum. There is no upper restriction on \(h\) in this deduction. For large values of \(h\) or \(e\), the resulting region can of course be weaker or vacuous.

Hölder's inequality then gives a holomorphic Mellin integral in \(\Re s>\sigma\), with locally uniform domination of its derivatives. On the initial right half-plane it equals

\[
\widehat W_*(s)\frac{E_r(s)}{L_K(s,\psi_r)}.
\]

The fixed test has nonvanishing Mellin transform in \(\Re s>0\). The finitely restored Euler factors \(E_r\) are also holomorphic and nonzero there. Consequently a zero of the primitive inducing \(L\)-function would cause a pole that the holomorphic integral cannot have. A principal \(L\)-function pole instead makes its reciprocal vanish and creates no exception.

This proves zero-freeness in the **strict** half-plane \(\Re s>\beta_{k,h,e}\). It makes no assertion about the boundary. The quantifier “every \(\epsilon>0\)” is what gives this exact strict threshold; a single fixed positive exponent loss must instead be included in \(e\).

For cofinal fixed orders with \(h_k=o(k)\) and \(e_k=o(k)\), every fixed zero to the right of \(1/2\) is excluded by one sufficiently large but fixed order. Constants need not be uniform in \(k\). For a fixed \(\nu\), this is a statement about its fixed-row twist family. The full finite-order Hecke GRH consequence requires the hypotheses for every fixed \(\nu\), as the source states; the functional equation and conjugation then give the reflected side. The principal row and character already include the Dedekind-zeta case. These are conditional all-scale conclusions, not height-averaged zero exclusions.

## 4. Why a one-sided signed average is enough for composition

This is an interface check, not a new arithmetic upper bound. Suppose a preceding exact reduction has a nonnegative residual square \(\mathcal N_R(D)\) and a real signed remainder \(T(D)\) satisfying

\[
\mathcal N_R(D)=T(D)+E(D),
\qquad |E(D)|\le C B(D),
\]

and a triangle estimate

\[
M_{2k}(D,D^h)\le C B_{\rm periphery}(D)+2\mathcal N_R(D).
\]

Then, before any pointwise positive-part replacement,

\[
M_{2k}(D,D^h)
\le C B_{\rm periphery}(D)+2C B(D)+2T(D).
\tag{B}
\]

Thus an **upper** bound on the signed integral
\(\int_X^{2X}T(D)\,dD/D\) suffices in (B). Neither an integral of \(|T|\) nor a pointwise upper bound for \(T\) is needed. Positivity of \(\mathcal N_R\) also gives \(T(D)\ge-CB(D)\), so a version written using \(\max(0,T)\) can be integrated with the same conclusion:

\[
\int T_+\le\int T+C\int B.
\]

This requires retaining the whole residual square until after the split and the accounting of controlled terms. It does not authorize treating selected individual signed summands as nonnegative.

If the periphery contributes exponent loss \(d\ge0\), \(B(D)\ll D^{h+k+\epsilon}\), and the signed average is at most \(C_\epsilon X^{h+k+e+\epsilon}\), the resulting moment loss is \(\max(d,e,0)\). For the previously reviewed anisotropic split \(Q_0=D^q\), \(d=(2b-1)q\); for a growing subpower cutoff the loss is zero. This records the compatible quantifiers for the parent composition, without asserting that its remaining signed average has been bounded.

## 5. Retained limitations

The arithmetic premise (A) remains open. The reviewed operator argument permits exceptional individual column scales, but it neither proves a pointwise moment estimate nor averages over the imaginary part of an \(L\)-function zero. Finite experiments, a bounded interval of scales, a bound on only primitive rows, or an estimate omitting the sixth-power replicas do not supply (A). No imported manuscript was fully re-proved and no new Lean build was performed in this audit.
