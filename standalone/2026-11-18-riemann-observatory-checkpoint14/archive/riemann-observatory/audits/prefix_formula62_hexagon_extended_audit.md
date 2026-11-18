# Transport of the centered exceptional mean in Proposition 8.11

This note continues the [scalar and dependency audit](prefix_formula62_hexagon_audit.md). It compares the ordinary moment argument in Liu's Hexagon 2611.00421v1 with the exact signed identities in arXiv:2610.26835v2 and Hexagon 2611.00082v1. The source chain supplies more of the exceptional calculation than is displayed in Proposition 8.11 itself. The remaining issue is the joint application of those identities and the new positive-side selection, for the complete marked family with inherited radicals.

## What transfers in the reference geometry

Use $P$ for the sum of the ordinary widths, $S_*$ for the actual root marked width, and $0\le w\le u+O(\eta)$ for any complete fixed subproduct marked **before** the first common-support decomposition. The earlier marked identity has $0\le t_{\rm loc}\le w$. At unit normalized root allowance, its origin exponent is bounded by
$$
P+S_*-1+4t_{\rm loc}.
$$
This is the bound used for both the second origin and the small completed/formal free-width terminals of Proposition 4.6 and equation (4.41) of Hexagon 2611.00082v1. In the latter cases the bound also pays a fixed free-width threshold and a subsidiary error. Thus the first gap in (53) pays these terms, provided the same marked exterior and formal width are used.

If $P+S_*+3w$ is below $5/6$ with a buffer, the exceptional term has an uncentered bound by the corresponding negative excess. On the complementary branch,
$$
P\ge 5/6-S_*-3w-o(1)>2/3
$$
by the third gap in (53). If an original plain factor has width $x\le\ell_{\rm ref}=7/50$, use the reflected old face directly. Otherwise choose the comparison widths $(\ell_{\rm ref},P-\ell_{\rm ref})$, with the same input tests and common twists, and keep the signed difference. Here $P-\ell_{\rm ref}\ge\ell_{\rm ref}$ and the positive comparison can be reflected into the old face under (50). In particular, the predecessor's coefficient-three condition $(P-3S_*)/2>\ell_{\rm ref}$ is not needed for the **reflected comparison** once the new old face is available.

For the exceptional mean itself, write $X=L_1+L_{\rm pow}\ge0$ and $c=c_{\rm cor}\ge0$ in predecessor equation (4.71). Its exact local deduction satisfies
$$
\frac98X+\frac{29}{6}c+\frac23(\ell-X-5c)_+
\ge\frac23\{X+5c+(\ell-X-5c)_+\}\ge\frac23\ell.
$$
When used with $\ell=\ell_{\rm ref}$, this gives the stronger saving $7/75$, compared with the new sufficient saving $(3/5)\ell_{\rm ref}=21/250$. The algebra holds for all nonnegative local variables, including the extreme case $X=c=0$. The new (53) therefore gives enough numerical room even after a buffer. This transports the **inequality** of (4.71) whenever its signed exterior, valuation classification and scope of extraction are preserved. [Old marked argument, §§4.4–4.6](../sources/latest62_density_frontier/hex_2611.00082v1.pdf) · [New reference and ordinary argument, §§8.8–8.9](../sources/latest62_density_frontier/hex_2611.00421v1.pdf)

## The signed identity and its quantifiers

The predecessor does include a precise fixed-character cancellation, Proposition 12.4. After fixing the exceptional row and any allowed exact divisor allocation, there must be one common finite character $\vartheta\in\Theta$, one coprimality radical $R_*$, one common norm twist $t$, and a pair of profiles $W_1,W_2$ used in both rectangles. Their scales must satisfy $T_1T_2=Y_1Y_2$. In the notation of Lemma 12.3, the pole term for each factor is
$$
A_i(T)=c_{\vartheta,R_*}\widehat W_i(1+it)T^{1+it}+O(Z^\varepsilon),
$$
with finite seminorm and polynomial-height factors understood. Subtracting the two products cancels the entire leading term, including its complex phase. The original profiles and exact scales must survive through any genuine divisor extraction. Lemma 12.2 forces a whole-column twist, and §12.2 keeps all coprimality indicators, including scalar zeros from the artificial last-divisor allocation. Those are real source proofs, not assumptions invented to explain the cancellation.

Equality of the products of scales does not suffice if the radical or twists differ. For example, with a principal character, identical profiles, zero height and one extra excluded prime on one rectangle only, the residue coefficients differ by the Euler factor $1-(N\mathfrak p)^{-1}$. The difference of leading products has the original volume order. This is a diagnostic for an invalid transport, not a witness against the paper's explicit common-presentation convention. [Earlier exact signed identities, §§12.1–12.3 and 12.8](../sources/latest62_density_frontier/2610.26835.pdf)

## Where the new selection enters

One possible reading of the proof avoids two selections. Set the predecessor's initial marked block $E$ empty while establishing the exceptional and zero-frequency terminals of the signed root. Its initial local variables $t_{\rm loc},L_1,L_{\rm pow},c_{\rm cor}$ then vanish. The old signed identities and formal-width correlation terminal are still meaningful. If the other live marked positions keep the same common coefficients in each rectangle, (4.71) then gives the clean upper bound $P+S_*-5/6-2\ell_{\rm ref}/3$. The new $u_C$ selection may take place only on the already separated nonexceptional positive Cauchy sides. On this reading, the earlier terminal proof avoids subtracting a mean from a modified or positively restricted rectangle.

A second reading takes $E$ to be the new deleted width and applies the old marked (4.71) with nonzero $w$. That requires a joint selection statement. The old block $E$ is fixed before the common-support decomposition, while (52) expresses the new $u_C$ after accounting for a side's $f$. In the all-unit branch of the predecessor the width changes by $-6w$ already in (4.46). The new $M_C=1+t-6u_C$ pays $-6u_C$. If these were independent consecutive charges, the combined allowance would generally contain both terms. The transmitted equation must identify the common charge or track both with a compensating change. No independent counterexample follows from counting the same charge twice. The source text expressly calls $f$ a fixed original marked width. For either reading, a reconstruction must specify which positions belong to $f$, which are genuinely removed with common support, and at what point the sole $u_C$ is charged.

The location of the selection within the two transforms matters. The old fourth-power identity is a Gauss-coefficient identity on the natural unit support. Plain multiplicativity on an already returned ordinary polynomial gives $\lambda_k(dn)=\lambda_k(d)\lambda_k(n)$ and does not itself replace the parameter $k$ by $kd^4$. As a check, for $k=1$ and an exterior prime $d$ of nontrivial sextic symbol, the resulting character at $kd^4$ varies with the remaining ordinary argument even though the original principal character is constant on units. Thus the empty-$E$ reading still requires the new $u_C$ to be selected at an intermediate positive Gauss stage where the fourth-power identity actually applies, and the later exceptional allocation must be shown compatible with that choice. A selection performed only on terminal ordinary sums cannot supply this step by reciprocity-free multiplicativity.

On each positive side the joint assertion needed for the scalar estimate is the exact coefficient family after all natural and artificial restorations, together with
$$
0\le s_C\le S_*-f-u_C,\quad
P_C+c_g-f\le P+O(\eta),\quad
u_C=\min(u,S_*-f)+O(\eta),\quad
M_C=1+t-6u_C,\quad t\ge-O(\eta).
$$
These inequalities comprise a width ledger, not just the displayed normalization equality $2a-k_C+q_C=M_C$. For example, on a side where $A=P+S_*$, $a=A-c-u_C$ and $P_C+s_C=a$ hold with equality, put $d_{\rm rem}=S_*-u_C-s_C$. The required ordinary-width bound then reads
$$
c-c_g\ge d_{\rm rem}-f+O(\eta)
$$
with an error of either sign. Thus any removed original prime positions beyond $f$ must be paid by an actual corresponding width reduction. Very small completed/formal widths must instead use the preceding direct correlation terminal, particularly after transport of an inherited radical. Hexagon 2611.00082v1 explains that the raw small-width test is not invariant under inheritance and proves an invariant terminal payment in (4.38)–(4.41).

If this ledger is established uniformly on the exact returned families, (52) and the monotonicity of the excess $p(P_C,s_C,M_C)$ close the nonexceptional sides. Both endpoint decrements and the fixed mesh are needed. For $S_*-f<u$ the surviving marked list is exhausted and the predecessor's arbitrary-length **unmarked** moment is the appropriate terminal. With $S_*-f\ge u$, use the earlier-stage detector/small-value moment on the complete residual family before combining the two side exponents. [Earlier marked widths and inherited-radical transport](../sources/latest62_density_frontier/hex_2611.00082v1.pdf) · [New equations (52)–(53)](../sources/latest62_density_frontier/hex_2611.00421v1.pdf)

## Induction rank

The oldest source has an explicit rank for its own centered induction. The proof of Theorem 12.16 and Appendix C decrease the actual combined child width by a fixed fraction of an auxiliary-prime width after two transforms. Reflection and centering at the same width decrease the additional flags in the rank. This proof assumes the predecessor's own admissible length inequality and restores it before calling a child moment. Hexagon 2611.00082v1 likewise gives a rank for its coefficient-three seed in Proposition 4.3, but its Proposition 4.8 is a different finite reduction. That later step calls a previously established face or a terminal high-value estimate after its two transforms and does not require recursive establishment of its output at a smaller parameter.

The new $M_C=1+t-6u_C$ by itself does not establish a decrease in width. For example $t=7u$ and $u_C=u$ are compatible with the displayed scalar constraints and give $M_C>1$. This is not a counterexample to the earlier-source rank because $M_C$ is the allowance in the new final-terminal estimate and need not equal a continuing child's actual width. If all children are terminal by the new detector, the old no-prime moment or the reference estimate, finite depth follows from the finite sequence of these transformations and from the outer stage index. If there is a continuing call at the same new stage, the proof must identify its actual child-width variable, its admissible hypotheses and the decreasing rank including inherited radicals. Merely transporting the old rank without those checks does not establish this conclusion. [Earlier Appendix C](../sources/latest62_density_frontier/2610.26835.pdf) · [Propositions 4.3 and 4.8](../sources/latest62_density_frontier/hex_2611.00082v1.pdf)

The exact centered fixed-row identity and the numerical payment for its exceptional excess can be recovered from the cited primary sources. I did not reconstruct the full new positive-side ledger with the complete restoration and ordered choice of $E,f,u_C$ across the two raw correlation transforms. The new preprint has no further appendix giving that transport. Neither the signed-residue diagnostic nor the rank observation gives a failure witness within the printed starred conventions. The ordinary propagation therefore remains unverified here.
