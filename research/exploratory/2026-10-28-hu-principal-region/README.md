# Principal-contour Euler bounds for Hu's unitary probe

**Status:** Proposed source-conditional interface; no new L-function zero-free region is claimed.

**Sources:** Hu, [*A seven-eighths zero-free half-plane for unitary Weil L-functions*](https://hexagonmath.org/2610.00216v1), (6.11)–(6.16), and the complete ramified local table referenced in Hu §6.3 and displayed in OpenAI's [quasi-RH preprint](https://github.com/openai/math/blob/main/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/paper.pdf), Lemma 7.1; Xu and Sang, [arXiv:2610.15291v2](https://arxiv.org/abs/2610.15291v2), Appendix C.4. The local identities and their compatibility with Hu's arbitrary-field unit-sector normalizations are imported, not reproved here. The exponent arithmetic below uses only unit-modulus local phases.

**Audit correction:** An earlier draft incorrectly read the source's `V^(1_(j<=1))` as `V * 1_(j<=1)`. At `j>=2` this loses a term of size `Q^(1-Re(s)-Re(w))`. The stronger all-row uniform-product claim based on that reading is withdrawn. The corrected exponents below reproduce Xu–Sang's source bounds.

**Smallest remaining gap:** Independently verify Hu's claimed transfer of the complete ramified table to his arbitrary field and prove the variable-geometry principal contour shift with all heights, reciprocals and tails. No new zero-free theorem follows from the calculation.

## Local and product bounds

Use Hu's field and local notation. Consider the closed tube

    Re(s)>=87/100,   Re(w)>=19/20,   Re(z)>=33/200.

Let `u` be a sixth-power-free physical row coprime to the fixed finite exceptional set `S`. If the source identities hold, then for every good prime `p`, with `Q=Np`,

    H_p-1 = O(Q^(-181/100))    when p does not divide u,
    H_p-1 = O(Q^(-41/50))     when p divides u.

The implicit constants are uniform in the row, unitary local phases and imaginary parts. The product over non-row primes converges uniformly. The row-dividing product is finite and, for every epsilon>0, bounded by `O_epsilon((Nu)^epsilon)` uniformly in the row; after enlarging `S` sufficiently to make the local factors nonzero, its reciprocal has the same bound. This is the known Xu–Sang scope, not an improved all-row convergence theorem. For `u=1`, every factor is in the first case, so a single sufficiently large prime cutoff makes `|H_(1,psi)-1|<=1/2` uniformly on the tube.

The key distinction is that the full local table has the common term

    (Q-1) Q^(-s-w) V^(1_(j<=1)),

where `V=Q^(-6z)` and `j=v_p(u)`. It contains `V` at `j=1` and **does not** contain `V` at `j>=2`. On this tube it contributes `Q^(-181/100)` at `j=1`, but only `Q^(-41/50)` at `j>=2`.

## Local verification

Write `R` for Hu's source local quantity `E`, and `D,W` as in his (6.11). The displayed tube gives

    |V|<=Q^(-99/100),  |R|<=Q^(-221/100),
    |D|<=Q^(-87/100), |W|<=Q^(-19/20).

The denominators `1-V`, `1-R`, and `1-D` are uniformly bounded away from zero.

At an unramified row prime, put `E=P_p^*+D`. The source's local identities yield

    E=[R((1-Q^(-1))/(1-V)+W-D) - D(Q-1)WV/(1-V)]/(1-R),
    H_p-1=[D(V+W-VW)-VW+(1-V)(1-W)E]/(1-D).

Thus `E=O(Q^(-221/100)+Q^(-181/100))` and `H_p-1=O(Q^(-181/100))`.

At a row-dividing good prime, `D=W=0` by the original zero extension, while the source's distinct `W_loc` is retained. The table gives

    |P_p^*| << |R| + Q^(1-Re(s)-Re(w)-6Re(z) 1_(j<=1)) + T_j,
    T_1=Q^(-Re(s)-Re(w)),
    T_2=Q^(3/2-3Re(s)),
    T_3=Q^(2-3Re(s)-Re(w))+Q^(2-4Re(s)),
    T_4=Q^(5/2-4Re(s)-Re(w)),
    T_5=Q^(3-6Re(s)).

On the tube the common term is `O(Q^(-41/50))`; every `T_j` is at most `O(Q^(-111/100))`. With `P_p=1/(1-V)+P_p^*`, one has `H_p-1=(1-V)P_p^*`, giving the asserted bound. Absolute ideal counting and partial summation bound the non-row prime tail by `O(P0^(-81/100))`.

For the row product use `sum_(p|u) log(1+C Q^(-41/50)) <= epsilon log Nu + O_epsilon(1)`; this follows by separating finitely many `Q` below a fixed threshold and using `C Q^(-41/50)<=epsilon log Q` for all larger `Q`. If each local factor has modulus at least `1/2`, the same argument applies to reciprocals using `|H_p|^(-1)<=1+2|H_p-1|`.

## Principal selected correction and real-power bookkeeping

For `u=1`, Hu (6.16) states that the selected local quotient satisfies

    B_p(s)+1 = O(Q^(-87/100)),  Re(s)>=87/100,

uniformly in the local phases and height. Thus at `w=1,z=1/6`, a fixed finite collection of normalized nonnegative prime-window factors has relative error `O(sum_i P_i^(-87/100))`, provided the prime-window masses are nonzero. This uses the fixed-field prime ideal theorem and the same normalization of all windows. At general points in the tube, the source unramified local formula gives `|G_p| << 1`, because `Q^Re(s)|P_p^*| << 1`; the latter follows by combining `P_p^*=-D+E` with the retained exponents in the previous subsection. After the fixed cutoff, `|G_p/H_p|<<1`. Factoring the unselected principal product gives the selected correction bound `O(Z^(ell Re(z)))` for each fixed finite slot system, by the ideal-counting bound for each annulus. This is a principal-row estimate only: at row-dividing primes the missing common term can make `G_p/H_p` grow like `Q^(1-Re(w))`.

For variable `ell,b` set `l_x=(1-b-ell)/2`, `l_y=(1+b-ell)/2`, and `h=1-l_x+ell`. The outside Mellin power together with the preceding principal selected correction is

    l_x/2 + Re(s)-1 + h Re(z) + l_y(Re(w)-1).

At `(w,z)=(1,1/6)` it equals `C_b(Re(s))`, where `C_b(s)=s-(4+b)/6`. On `Re(s)=beta+e`, the unresidued shift to `Re(w)=19/20` with `Re(z)=1/6+e` has exponent `C_b(beta)+(1+h)e-l_y/20`. After taking the `w=1` residue, shifting to `Re(z)=33/200=1/6-1/600` gives `C_b(beta)+e-h/600`. These agree with Xu–Sang Appendix C.4. Their use requires holomorphy, the precise crossed poles, horizontal-join and trace-tail bounds, a controlled global reciprocal on the `s`-line, and the same physical probe on both sides; this paragraph supplies the power bookkeeping, not those contour inputs.

## Remaining high-side gates for a first-stage theorem

The local bounds and real powers above are only inputs to the following distinct obligations:

1. Define the variable-geometry compensated probe and its full finite correction from Hu's actual unit-sector and zero-extended physical coefficients, with disjoint prime windows, and verify that its residue normalization and excluded-prime set are exactly the ones used on the low side.
2. Prove the principal double-residue identity on `Re(s)=beta+e`: the only crossed scalar poles are `w=1` and `z=1/6`, the local selected approximation is valid on the entire `s`-line, and its fixed positive window normalization has reciprocal `O(Z^epsilon)`.
3. Supply all-height majorants and trace/horizontal-join decay for the common triple Mellin integrand, while maintaining the reciprocal `1/L_K^S(s,psi)` on its global zero-free line. The local Euler bound does not imply a reciprocal bound.
4. On nonprincipal rows, establish the buffered denominator and the complete finite error expansion at the raised numerator contour, including the prime-label conductor deficit, common masks, residual factors and target-dependent seminorm/height degrees. In particular the ramified `j>=2` term `Q^(-Re(w))` is essential and must not be treated as summable without its conductor deficit.
5. Transfer Hu's paired fourth moment and the amplified numerator average to the same row class and physical slot polynomials, respecting the finite exceptional set and the fixed ordering of the slot mesh, loss parameters and height cutoff. A first stage can use `kappa=3/4` only under its required finite-order `7/8` premise.
6. Cover floor, small and large row ranges, and prove the low- and high-side estimates with a **common** power saving and the same normalized probe. Select `e` smaller than all positive real-power margins, including `l_y/[20(1+h)]`, `h/600`, and the principal slot margin. Finally justify unitary descent and the signal noncancellation criterion.

These are proof obligations, not hypotheses silently treated as established by the local calculation.
