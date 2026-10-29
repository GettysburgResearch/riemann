# A large conditioned subspace of Gauss profiles beyond Gershgorin

**Status.** This is a source-qualified partial-subspace consequence of the [averaged theta overlap](../2026-10-29-cubic-theta-overlap-average/README.md) and the cited fixed-order sextic large sieve. It does not prove that the full profile span is conditioned, control its complement, or give a zero-free region. The October 5 completed-theta estimate and its inputs are imported.

Use the same field, good set, fixed ray sector, inverse-oriented vectors v⁻_(P,h), and fixed smooth Möbius vector m_P as in the theta-overlap note. Take one primary generator of each good sixth-power-free ideal h with full norm Nh≤H, and write u_h=v⁻_(P,h)/||v⁻_(P,h)||₂. Let A:ℂ^N→ℓ²(source indices) be the column operator with columns u_h. Here N≈H by standard ideal counting. For every ε>0, uniformly for 1≤H≤P^(1/2), the sextic sieve and the individual diagonal lower bound imply

    ||A||² ≪_ε (PH)^ε,            tr(A*A)=N.                        (1)

Indeed, before normalization the dual large sieve gives `||A||²≪P^(−1)(PH)^ε Θ₆(H,P)`, with

    Θ₆(H,P) ≪ H+P+H^(5/6)P^(1/3)+H^(1/3)P^(5/6).

Each term is O(P) in the stated range. The column normalization costs at most H^ε by the fixed-sector squarefree density with h-prime deletions. The character, ray-sector and zero-mask conventions are exactly those of the cited sieve and overlap note.

Let E_high be the spectral subspace of A*A with eigenvalues ≥1/2, and let V_high=A(E_high) be its image. Since the complement contributes at most N/2 to the trace,

    dim V_high ≥ N/[2||A||²] ≫_ε H(PH)^(−ε).                     (2)

The restriction of A to E_high has squared singular values ≥1/2. Therefore, writing Π_high for orthogonal projection onto V_high,

    ||Π_high m_P||² ≤ 2||A*m_P||²
       ≪_ε (PH)^ε P^(−1)(H+H^(3/2))(1+|t|)^A.                (3)

The second inequality is the source-qualified averaged theta overlap, with the column-normalization H^ε absorbed into the loss. The polynomial height order A is fixed before the height power is selected. Unlike a Gershgorin argument, this proves the claim only for the chosen **spectral subspace**, not for every named profile or the entire span.

At P=Y^(6/5), choose any fixed δ>0 with H=P^(25/54−δ). This obeys H≤P^(1/2). The unrestricted-row sextic source operator has squared norm ≪Y^(41/30+ε), so (3) yields

    ||T_(Y,P) Π_high m_P||² ≪ Y^(1−(9/5)δ+ε)(1+|t|)^A.       (4)

At the same time V_high has at least H(PH)^−ε independent directions. Let V_old be the earlier full span of profiles indexed by sixth-free h with radical norm at most H₀=P^(128/359−η), for any fixed η>0. Its dimension is ≪H₀^(1+ε). If `25/54−δ>128/359−η`, the intersection

    E_new=V_high ∩ V_old^⊥

has dimension at least `dim V_high−dim V_old≫H(PH)^−ε`, after choosing the small losses below the fixed exponent gap. Since E_new⊂V_high, its Möbius projection and image energy obey the same estimates (3)–(4). Thus the selected subspace contains polynomially many directions orthogonal to the entire earlier low-radical span; these are abstract linear combinations and are not claimed to be individual prime profiles. The inverse-oriented and earlier direct-oriented spans match after replacing each sixth-free exponent e by 6−e, retaining the same radical and zero masks. Source row restriction can only decrease the operator norm in (4).

The source large sieve is an upper bound with an unspecified constant and power loss; (1) and the trace do **not** force every eigenvalue of A*A to exceed 1/2. The complementary low-Gram subspace can still have large dimension, and no bound on `T_(Y,P)(1−Π_high)m_P` follows. Nor is V_high known to coincide with a large-eigenvalue theta spectrum. A physical detector additionally needs its actual coefficient profiles, prime products, masks, and common height range to match these fixed-profile statements.

**Independent review.** Two researchers checked the dual sieve orientation and normalization, trace and singular-value inequalities, projected-energy exponent, and the dimension of the subspace orthogonal to the old radical-indexed span. The result remains conditional on the stated theta, sieve and normalization inputs and does not establish a full-span or complement estimate.
