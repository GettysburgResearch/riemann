# A quantitative spectral target for a Möbius source

**Status:** An elementary conditional reduction, not a spectral decomposition theorem or a zero-free region. It spells out what an extension of the fixed-profile overlap in [mobius-overlap.md](mobius-overlap.md) would need to supply. The decomposition and uniform growing-family overlap below are not known from Xu–Sang Proposition 3.1 or OpenAI Proposition 5.1 as stated.

Let T_Y be the sextic source-to-row matrix at balanced norm scales Y, with exact masks and fixed ray/unit blocks, and set `G_Y=T_Y* T_Y`. Let m_Y be a centrally normalized smooth Möbius coefficient vector of ℓ² norm O(1). Suppose that for some fixed δ>0 and every sufficiently small ε>0 there are subspaces `V_Y` and self-adjoint operators E_Y,R_Y such that

    G_Y=E_Y+R_Y,       E_Y≥0,       range(E_Y)⊆V_Y,
    ||E_Y||≪Y^(7/6+ε),             ||R_Y||≪Y^(1+ε),                  (1)

and V_Y has K≤Y^(5/6−δ) unit basis vectors v_j whose Gram matrices have eigenvalues in `[c,C]`, with c,C>0 independent of Y. Finally suppose the **uniform** overlaps

    |⟨m_Y,v_j⟩| ≪ Y^(−1/2+ε),    1≤j≤K,                            (2)

with constants independent of j,Y. Then

    ||T_Y m_Y||² = ⟨G_Y m_Y,m_Y⟩ ≪ Y^(1+ε)                          (3)

for every ε>0, after reducing the preliminary losses.

Indeed, the bounded inverse of the basis Gram matrix gives

    ||Proj_(V_Y)m_Y||² ≪ Σ_j |⟨m_Y,v_j⟩|²
       ≪ K Y^(−1+2ε).

As E_Y is self-adjoint and its range lies in V_Y, `E_Y=P_V E_Y P_V`. Its contribution is `≪Y^(7/6+ε) K Y^(−1+2ε)≤Y^(1−δ+3ε)`. The residual contribution is `≪Y^(1+ε)||m_Y||²`. Choose the preliminary ε much smaller than the requested final loss and δ. The source's known full-operator upper bound supplies the scale Y^(7/6+ε), but it does **not** supply the decomposition or the Y-sized residual in (1).

The rank threshold `5/6` comes directly from `7/6−1+5/6=1`. For nonbalanced source scale P≤Y, replace the exceptional norm scale by the appropriate `Y^(5/6)P^(1/3)` and use the overlap `P^(−1/2+ε)` only where its source proof is uniform; the allowable rank then changes accordingly. A weaker residual `||R_Y||≪Y^(13/12+ε)` leaves a factor Y^(1/12) above the desired target even if every exceptional mode is completely suppressed.

OpenAI Proposition 5.1 and the Mellin argument in the companion note establish (2) for each **fixed** Gauss profile and fixed finite-ray data, with constants depending on those data and a fixed polynomial height cost. Xu–Sang's centered comparison gives a codimension-one bound only inside a **fixed finite-dimensional** profile space. Neither theorem by itself supplies a basis of size growing with Y, uniform Gram conditioning, a full-space decomposition, or the Y-sized residual in (1). A physical detector also introduces prime products, dyadic lengths, finite presentation sectors, zero masks and Fourier/norm heights; the required decomposition and (2) must cover that actual coefficient class and a single cumulative height budget. A bound on m_Y alone does not automatically cover a row-dependent mask or a multiplied prime polynomial.

The subsequent [moving-twist calculation](moving-twist-overlap.md) obtains a weaker conductor-dependent overlap and a conditioned family of polynomially many explicit profiles, by using the local reflection formula in addition to Proposition 5.1 as stated. It controls the corresponding projection energy but does not establish that this span captures the exceptional eigenspace or that the complementary operator has the bound in (1).
