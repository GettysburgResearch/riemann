# The compensated Mellin comparison in Liu's two papers

17 November 2026. Technical dependency audit of arXiv:2610.26835v2 §§13.3–13.6, especially (13.8) and (13.11)–(13.20), with the related refined closure in §§14.5–14.7. Compared against Hexagon 2611.00421v1 §§8.10–8.11 and §9 (Theorem 9.3). Private source snapshots are under `sources/latest62_density_frontier/`. This verifies the continuation implication and tracks its analytic inputs. It does not certify the moment induction or the old bound used as input.

## Which function is continued

In the old finite-order comparison the signed physical quantity is $I_{\rm mod}$ of (13.4), including the complete finite inclusion–exclusion expansion at distinct, selected primes. Its claimed initial Poisson–Mellin identity (13.11) has real coordinates $(s,w,z)=(4,4,2)$. Its test-and-scale factor is

$$
 X^{1/2-z}Z^{s+z-1}Y^{w-1}
 e^{(s+z-1)^2}M(z)\widehat W_1(w).
$$

Its arithmetic factor is the sum over sixth-power-free frequencies modulo sixth powers of units, with weights $q_u^{-z}$, of

$$
 \frac{\zeta_F^S(6z)L_F^S(w,\chi_u)}
 {L_F^S(s,\eta\overline{\chi_u})}H_{\eta,u,Z}(s,w,z).
$$

The local tuple formula (13.10) identifies the correction $H_{\eta,u,Z}$; this alone does not identify the analytic Poisson transform for the signed original coefficients. The paper explicitly requires that residue Poisson, orbit unfolding and initial-line Fubini preserve the complete tuple identity. Proposition 8.1 and (8.2) supply the primitive and imprimitive unit-orbit Poisson formulas; §13.3 calls for their use on the actual coefficients. The dual origin is removed by the chosen test, whose transform satisfies `Ŵ₀(0)=0`. This is separate from the bounded nontrivial unit classes with $q_u=1$, which are ordinary nonprincipal rows.

The only principal numerator is $u=1$. On the global $s$-line $\sigma_g=\beta+20e$, move $w$ from (1+e) to $19/20$ and, in its $w=1$ residue, move $z$ from (1/6+e) to $33/200$. The double residue at $w=1,z=1/6$ contributes
$$
 c_S X^{1/3}Z^{s-5/6}
 e^{(s-5/6)^2}\frac{H_{\eta,1,Z}(s,1,1/6)}{L_F^S(s,\eta)},
 \qquad
 c_S=\widehat W_1(1)M(1/6)(\operatorname{Res}_{w=1}\zeta_F^S(w))^2/6.
$$
Here $M$ and $\widehat W_1$ are test transforms. There is no additional gamma factor in this principal inverse Mellin formula. Gamma factors in reflected nonprincipal integrands belong to the estimates for those integrands. Write $c_0=(4+b)/6$. By the geometry $X^{1/3}Z^{s-5/6}=Z^{s-c_0-\ell/6}$. The selected tuple contributes $Z^{\ell/6}A_T$ times the unselected product $H_\eta(s)$, with relative error $O(Z^{-\omega_P})$, $0<\omega_P<(437/500)\min_i\ell_i$. The weights here are nonnegative up to a single fixed sign. The ray prime ideal theorem makes $A_T$ eventually nonzero with subpower reciprocal. After dividing by $c_S A_T$, the main term is exactly
$$
 f_\eta(Z)=\frac1{2\pi i}\int_{\Re w=2} Z^{w-c_0}
 e^{(w-5/6)^2}\frac{H_\eta(w)}{L_F^S(w,\eta)}\,dw .
$$
The notation $w$ in this last one-variable integral is a dummy for the earlier $s$. The finite selected-prime error is part of $J_\eta-f_\eta$, where $J_\eta=I_{\rm mod}/(c_SA_T)$. In particular it does not enter the numerator of $f_\eta$. The principal-strip domain (13.12), with real parts at least $(437/500,19/20,33/200)$, gives $H_p-1=O(q_p^{-907/500})$ uniformly in heights and unitary phases after removing finitely many primes. Normal convergence and $\sum_{p\notin S}\sup |H_p-1|<\log(3/2)$ give a fixed nonvanishing $H_\eta$, even at a real hypothetical exceptional zero. The separate principal savings in (13.19) are $l_y/20-(20+h)e, h/600-20e, \omega_P-20e$.

## Exact continuation conditional on the comparison estimates

With $F_\eta(w)=e^{(w-5/6)^2}H_\eta(w)/L_F^S(w,\eta)$, the fixed Gaussian ensures integrability in height on each line to the right of absolute convergence. The integrand for $f_\eta$ may be shifted arbitrarily far right there, giving $f_\eta(Z)=O_{A,\eta}(Z^A)$ at zero for every positive $A$. The needed large-(Z) estimate follows by the triangle inequality if the original signed quantity satisfies, with common numerical $B+\epsilon_{\rm lo}<\beta$ and $m>0$,
$$
 |J_\eta(Z)|\ll_\eta Z^{B+\epsilon_{\rm lo}-c_0},\qquad
 |J_\eta(Z)-f_\eta(Z)|\ll Z^{\beta-c_0-m}(1+T_1)^{A_\eta}
     + Z^{D_\eta}T_1^{-N}.
$$
Here the last inequality must hold with $D_\eta$ fixed before the external integration-by-parts order $N$. This order matters. For positive $\tau<m/[4(1+A_\eta)]$ satisfying the detector restrictions, take $T_1=Z^\tau$ and choose $N\tau>D_\eta-(\beta-c_0)+m$. The comparison gives $f_\eta(Z)=O_\eta(Z^{\sigma-c_0})$ for $\sigma=\max(B+\epsilon_{\rm lo},\beta-m/2)<\beta$. Integrate
$$
 \int_0^\infty f_\eta(Z)Z^{c_0-s}\,\frac{dZ}{Z}.
$$
The part below 1 is entire and the part above 1 is holomorphic in $\Re s>\sigma$ by local uniform convergence. To check the sign convention, set $Z=e^x$. On a vertical line $\Re w=d>1$, $f_\eta(e^x)e^{(c_0-d)x}$ is the inverse Fourier transform of $F_\eta(d+it)$ with kernel $e^{itx}$. The above transform recovers $F_\eta(d+it)$ with kernel $e^{-itx}$. Thus this is the holomorphic continuation of the actual smoothed quotient. Its unique continuation equals the meromorphic quotient on their common domain. The nonvanishing numerator and the Gaussian exclude a pole from a denominator zero of any multiplicity, real or complex. Finite deleted Euler-factor zeros occur only at $\Re s=0$; a principal pole at 1 or a norm-character pole at $1+it$ gives a zero of the reciprocal, which is allowed.

The contour proof before this step only needs the global $s$-line to lie strictly to the right of (β). For the finite-height nonprincipal moves it needs the rowwise zero-free buffer. Constants, heights and thresholds can depend on the fixed target. The family supremum contradiction needs only the common numerical $\sigma<\beta$ and no attainment. Nonuniform constants across targets cause no issue.

## From the earlier comparison to the November floor

Proposition 8.13 sets $\Re x=a+16e, \Re z=17/50, \Re w=1-a-6e$ for $1/2<a\le .51$ and $e<\min(10^{-3},(a-1/2)/100,(1-a)/100)$. Old Lemma 13.10 controls the nonprincipal correction there, with $\Re(x+w)=1+10e, \Re(6z)=51/25$, and $H_p-1=O(q_p^{-1-10e})$ in the indicated region. The buffered rectangle is required before moving the finite $x$-segment. At the floor $a=.509$ there is no encounter with $z=1/6$ for a nonprincipal row. The numerator $L_F^S(w,\chi_u)$ is entire for those rows. One may move $w$ through its holomorphic strip on the global $x$-line before moving the finite $x$-segment. The estimates for the local denominators (1-D) and (1-R) exclude their possible zero boundaries, respectively $\Re x=0$ and $\Re(x+z)=2/3$. The positive floor calculation in Proposition 8.13 supplies a row exponent. It does not on its own give the all-bin comparison of the actual signed quantities in the preceding display.

Theorem 8.14 uses $B_*<B'<B$ and picks losses after the strict margins at (B') so the direct bound fits (B). The old §14.6–14.7 is a useful template beyond §13.6 alone. Lemma 14.7 retains the actual conductor in the dual profile, includes the simultaneous conductor deficit for all strict-error positions, and moves $w$ rowwise before any later $z$ deformation could act on a selector. After truncation the retained $s$ segment moves on the buffered rectangle. That lemma gives an explicit identification of the refined difference with the very same $J_\eta-f_\eta$ in the continuation lemma. Theorem 8.14 invokes the known parametric comparison for its final identification. Theorem 9.3 additionally invokes Hu's Lemma 6.1 and Gao's §3 for unitary phases and gives the corresponding cutoff form explicitly. Its quotient is $e^{(s-5/6)^2}H_\psi^S(s)/L_F^S(s,\psi)$; the displayed estimate has $\beta-c_0-2\eta$ as the main-error exponent. Its $H=Z^{t_\psi}$, $t_\psi<\eta/[2(1+A_\psi)]$, is sufficient to retain a saving $\eta$. This audit checks the algebra conditional on that unitary estimate and numerator claim. It does not replay Hu and Gao.

## Remaining analytic verification

A precise transport statement sufficient for Theorem 8.14 is the cutoff inequality above for the original normalized (13.4), with $f_\eta$ defined by the original double residue, produced from the new finite joint moments on *all* retained nonprincipal rows. To certify it, track each class through the old signed expression before using absolute values, retain the row's actual conductor and its selected-position Euler errors, and apply the new moments to the resulting actual profiles with finite internal seminorm orders. In particular, establish a common polynomial height majorant on original contours and horizontal connectors so $D_\eta$ is independent of the external tail order. The height coordinates $(\Im(s+z),\Im z,\Im w)$ have determinant one, and Gaussian/smooth Mellin decay supplies the tail once that polynomial majorant and the cutoff ranges are established. An estimate for a positive moment surrogate alone cannot establish the cutoff inequality for the specified difference. Equality to the old signed object, exclusion or separate control of exceptional numerator presentations, and the full all-bin exponent bound are the testable obligations. No contradiction to the exact Mellin continuation step was found. This audit leaves the antecedent signed transport unverified and provides no independent proof of either fixed half-plane.

- [arXiv:2610.26835v2](https://arxiv.org/abs/2610.26835v2)
- [Hexagon 2611.00421v1](https://hexagonmath.org/2611.00421v1)
