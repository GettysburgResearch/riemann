# Internal review of the two reflected-energy refinements

**Reviewer:** `full_inverse`, separate from the author `spectral_route`.

**Status:** internal mathematical review of the native changes and their cited source use sites. No new zero-free boundary is established. This is not an external review, integration approval, or a complete independent reconstruction of the pinned source's analytic machinery.

## Frozen objects inspected

| Object | SHA256 |
|---|---|
| `work/round4_spectral/EXACT_COLUMN_MARKED_INVERSE.md` | `aa318fc58f8b8ba2a37d23eb69cf0e91e918a321192e28795ed1ffb2c2bc15fd` |
| `work/round4_spectral/REFINED_POWERFUL_ROW_ENERGY.md` | `e1d0628a608a10412a43a0516aad7ca453f4bfbb5ccfb75ba1207ef664129ef7` |
| `work/round4_spectral/QUARTIC_SPECTRAL_INTERFACE.md` | `c02d2f9cb36a0c2b76c6a24b5ab37d9efb3a85b19ddef573c34dae612075b63c` |
| Pinned QRH `_source-original-quasi.tex` | `42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3` |

The pinned source commit is `1581d4cbdd69a0faf34b2089614fe2a814316a6a`.

## 1. Exact-column marked inverse

**Finding: the stated native deduction is correct under the imported source statements and their exact scope.**

I independently optimized the retained column expression. For
$u(v,z)=\min\{v,z,(v+z)/3\}$ and $v+3b+e\le T$, its exact maximum is

$$
\max\{T,z,2(T+z)/3\}.
$$

The maximizing reduction $b=(T-v-e)/3$, followed by $v=T-e$ and $e=0$, is valid because $v-u(v,z)$ is nondecreasing. The source's small negative ramified dyad and retained-width tolerances create only the stated additive error.

In the canonical terminal step, I checked that source `old-eq:4.9` uses only the first invariant. Retaining $S_0+B_0$ gives the third affine branch

$$
E\le\frac23M+\frac43z_0-\frac23c+\frac{10}{3}d+O(\eta+\tau).
$$

The replacement second invariant
$4F-3M-(16/3)z_0\ge c$
therefore bounds this by
$F-M/12-11c/12+(10/3)d+O(\eta+\tau)$.
The two other column branches and the row branch retain a positive reserve from the first invariant. Shrinking the freely chosen source tolerances suffices.

I checked the occurrences and transitions of the second invariant in:

- `eq:invariant`, the canonical theorem declaration;
- `eq:inverse-fixed-invariant`, the node induction;
- `eq:inverse-terminal-width`, `old-eq:4.9`, `old-eq:4.10`, and `old-eq:4.11`, the terminal bounds;
- `eq:canonical-transition` and `eq:inverse-child-margins`, the actual child parameters and puncture update;
- the exact identities immediately preceding `eq:inverse-initial-margins`, and that displayed margin statement;
- the unchanged initialization energy identity and final normalization.

The child transition preserves the linear form $4F-3M$ up to the same $7\eta$ loss, because the nominal slot cap $z_0$ is unchanged. Initialization adds exactly $(2/3)z_0=(2/3)(z-G)$ to the old second identity and gives

$$
3m-2r-\frac{22}{3}z+\frac{28}{3}G+2P_1.
$$

The resulting full marked range
$r+2z<m$, $2r+(22/3)z<3m$
is therefore supported by the claimed induction. Its finite-ray, fixed-puncture, label-average, common-profile, and actual-row restrictions must remain exactly as stated.

I also checked the new final positive-face calculation. With unit overlap data,
$F=r+z$, $M=2r+2z-m$,
the face $v=T$, $b=e=0$ has
$E-F=2(r+2z-m)$ whenever its stated $T\ge2z$ condition holds. This shows that the *positive exponent bound used by this proof* cannot relax the first marked condition. It is not a lower bound for the arithmetic moment.

## 2. Refined powerful-row count and low probe

**Finding: the count and the stated conditional low-probe deduction are correct under the imported reflected-energy statement.**

With $f$ and the puncture fixed, I checked the source local classification in `par:reflected-energy-data`, `lem:reflected-energy`, and the marked collision conventions. A surviving slot prime is coprime to the primal row; slot collisions are already zero-extended and removed. Therefore, outside the fixed bad/label/puncture support, an active powerful-row prime is counted in the non-slot radical $A_0$. An inactive powerful prime has exponent divisible by six.

Writing the inactive part as $t^6$ and the active powerful radical as $a$, with $a^2$ dividing the powerful part, gives

$$
\#k_{\rm pow}\ll Z^{\min(O/2,\,O/6+2A_0/3)+\varepsilon}.
$$

The factors on the fixed support and the prime powers supported on a fixed radical cost a small power uniformly in the allowed polynomial norm ranges. Crucially this count is applied with the label and puncture frozen, not before an outer label sum.

I checked the exact cube inequality

$$
\min\{v,z,(v+z)/3\}+b+2e/3+\tfrac12(T-v-3b-e)
 \ge\min\{z,T/3\},
$$

including its equality faces. Substitution in the actual physical low range, with
$M'=1-\ell-2d$, $2A_0\le O$, $N_0\le A_0$, gives the claimed exponent

$$
E\le M'+\left((4\ell+2d-1)/3\right)_++\text{reserved losses}.
$$

The rescaled-subset cost
$-d+(4\ell+2d-1)_+/6$
is nonincreasing in $d$, so its maximum at $d=0$ includes every subset. The deduction retains the source's additive-Gram scale conditions, common smooth density, and polynomial height costs. It is conditional on those geometric conditions at the chosen enlarged slot range; it does not extend them automatically.

## 3. Scope and boundary check

Neither result improves the zero-free boundary by itself. In the supplied current optimizer range $r\ge23/37$ and $z=(1-r)/2$, the old second marked constraint already has reserve:

$$
2r+8z=4-2r\le102/37<3.
$$

Thus the exact-column improvement changes an inactive face. Its unmarked face is unchanged. The powerful-row refinement also vanishes on $O=A_0=0$, which is the positive face obstructing an improvement of the first marked constraint.

The low-probe-only minimum $41/48$ must not be called a zero-free bound: the original high-side floor condition remains. The review approves only the native algebra, count, and source-qualified deductions described above. It does not remove any unresolved source dependency or establish a new analytic cancellation theorem.

## 4. Final quartic spectral interface

**Finding: the stated exact identities and the carefully limited interface are correct; the centered estimate remains unproved.** The final version at the hash in the table was inspected, including its explicit companion-tail statement and mixed-term caveats.

I checked the differentiation of the DDHL angular-one Jacquet integral. With the stated trace additive character, its diagonal entries have the phases $-i(u/|u|)$ and $-i(\overline u/|u|)$, and Bessel order $s-3/2$; its off-diagonal entries have opposite signs and order $s-1/2$. The displayed zero-frequency matrix follows from the polar integral.

The Wronskian reconstruction uses

$$
R\{I_{\nu+1}(R)K_\nu(R)+I_\nu(R)K_{\nu+1}(R)\}=1.
$$

Substitution checks both reconstruction coefficients and every sign. The two Gamma--I series give the stated holomorphy for $\Re s>-1/2$ and polynomial growth on closed strips with radius in a fixed compact annulus. No division by a K-Bessel function is used. This reconstructs the scalar Fourier coefficient, but the multipliers depend on the actual row radius and phase and combine two input columns. The warning that their cross-scattering term must be retained is therefore necessary.

I checked the ordinary, nonmetaplectic level identities by the three bottom-row valuation cases $v_p(b)=0,1,\ge2$. In particular, subtracting $q^{-s/2}E(T_pw,s)$ from $E(T_{p^2}w,s)$ leaves exactly $(q^s-1)E_{p^2}(w,s)$. The fixed-ray permutation version has the same cancellation with $q^sI-U_p$. The incoming coefficient is one and the residue has the expected index factor $q(q+1)$. The height inequality and the consequence $(Nd)^{2-2u+\varepsilon}$ follow under the explicitly stated fixed-base Eisenstein premise; this premise is not proved by those identities.

The incoming and outgoing packet scales are reciprocal, $1/L$ and $L$. The interface correctly withdraws the earlier exploratory contour-direction error and does not infer a slow outgoing cusp tail from a left-side scattering denominator. It also correctly distinguishes a single-column self-pairing from the mixed-column pairing used by the reconstruction.

The finite-cover evaluation calculation is exact: with Haar-normalized norm on $n$ cosets, evaluation at one coset has norm $\sqrt n$. A small oldsection Gram norm alone does not remove this evaluation cost. Hilbert--Schmidt unitarity likewise cannot be substituted for an unproved matrix operator-norm bound.

Finally, the final section correctly imports the full primitive-sieve tail

$$
\sum_{0<Nk\le K}|T_R(k,D)|^2
\ll (KD)^\varepsilon(K/R+D^2/R^4)
$$

from its companion proof. It preserves the row-independent column-weight condition, finite support, all nonzero physical rows, excluded zero row, exact empty-tail ranges, and the condition $R^3\ge H$ for its simplification at $K=D^2/H$. The displayed reattachment inequality

$$
\left|\|a+b\|_2^2-\|a\|_2^2\right|
\le 2\|a\|_2\|b\|_2+\|b\|_2^2
$$

is correct. Its use needs an independently justified low or full norm, with no circular assumption of the desired bound. A common transform must retain the applicable profile uniformity and row independence. The final interface does not identify the arithmetic diagonal or prove its displayed low-divisor target, its level growth, or the remaining mixed-term estimate. This scoped review does not promote any of those targets to a theorem.

The marked note's final hash also incorporates restoration of two literal carriage-return bytes to the intended TeX command in its displayed conclusion. I checked that this formatting repair does not change the mathematical statement or proof reviewed above. This review's own single tab in the cube inequality was restored to the intended TeX fraction command.

## 5. Confirmation at the frozen Git source commit

I independently read the published packet through git show at exact commit
193c3d79f0522f08f62afc5c24c29f139d889080 in the local fetched repository.
Its tree is 1e71897b46a6b7b75fe8694c48b7d08911260276 and its parent is
e87c5f669f81fe6371af926917d1c5b21023bce8.
The packet path is standalone/2026-10-22-quartic-full-sieve/.

The Git-object bytes of EXACT_COLUMN_MARKED_INVERSE.md,
REFINED_POWERFUL_ROW_ENERGY.md, and QUARTIC_SPECTRAL_INTERFACE.md match
their complete SHA256 values in the table above. This check used the
frozen Git objects, not the mutable working files. The three files contain
no control bytes except line feeds.

I also inspected the packet README at that exact commit; its SHA256 is
d2d4db8df9309fd16cfeb3ff58fdaf5b1454a85417e9897264edd2b1756b3d44.
It accurately states that no new zero-free boundary has been proved,
keeps the inherited benchmark source-qualified, labels the marked theorem
as dependent on the pinned QRH source, and identifies the centered
low-divisor estimate as unproved. It distinguishes the native quartic
identities and tail deduction from those source-dependent marked
refinements, and identifies these checks as internal reviews only.

My scoped conclusions above therefore apply to those files at commit
193c3d79f0522f08f62afc5c24c29f139d889080. This confirmation is not external
peer review, formal verification, integration approval, a full replay of
the imported QRH analytic proofs, or approval of a new zero-free constant.
No source mathematics was edited during this confirmation.
