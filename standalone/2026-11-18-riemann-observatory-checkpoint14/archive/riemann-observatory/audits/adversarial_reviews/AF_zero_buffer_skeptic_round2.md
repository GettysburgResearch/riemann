# Independent check: no growing zero buffer is needed for the leading finite-matrix transfer

Reviewer: search_skeptic. Date: 2026-11-17. Scope: Alpöge–Furman arXiv2608.13637v2, the tail truncation in Proposition 4.3, the last paragraph of Theorem 5.7, and the actual argument in §6. This is a conditional simplification of that transfer argument, not an audit of the prime-side second moment or an independent verification of Theorem A.

Source inspected: `sources/analytic/2608.13637.pdf` (SHA-256 `6de3b156342e7b4a802c34f8ef40432567e9dabe006938da04233f19fc4ef444`), extracted text SHA-256 `0a7f75ca6642c0bf5ed6a6304b226aa4ee474f834743e7f8240042b1c4b1be7f`. Relevant locations: §2.2–2.3 pp4–5, Lemmas 2.1 and 3.1–3.4 pp5–6, Proposition 4.3 p7, end of Theorem 5.7 and proof of Theorem A p11. The trace repair is supplied separately in `AF_trace_localization_skeptic_round2.md`.

**Result of this inspection:** the finite matrix can be formed from the zeros with ordinates in I=[T,2T) itself, with zero buffer. The omitted-zero matrix has nuclear norm O(√T), rather than the paper's O(T^−1/2) for its √T buffer. Although this bound grows, it is o(√N), where N is of order T log T. That suffices to transfer a full-matrix Hilbert–Schmidt second moment to the finite zero matrix with o(N) error. The §6 leading-constant argument uses precisely this weaker scale. It does not use Weyl's inequality or an operator error tending to zero.

This conclusion preserves the limiting constants conditional on the other source inputs. It does not preserve the source's stated error rate, and does not validate those other inputs.

## Precise hypotheses and definitions

Let L=log(T/(2π)), X=e^L=T/(2π), h=2π/L, d=floor(T/h), and α_k=T+kh, 0≤k<d. Assume T is sufficiently large that h≤1. Let φ be the fixed real even C² window used in §2.2, supported in [−L/2,L/2]. Require uniform constants

* |φ(u)|≤M;
* a=||φ||²₂/L≥a₀>0;
* |φ̂(r+iη)|≤C e^{L|η|/2}|r|^−2 for |r|≥1 and |η|≤1/2.

The fixed AF indicator and Montgomery–Taylor windows with fixed smooth cutoff meet these particular window conditions. No assertion is made here about all the §5 estimates for arbitrary windows.

Let the nontrivial zeta zeros be represented by z=(ρ−1/2)/i=t+iη, with positive multiplicities m_z. Then |η|≤1/2 and the multiplicity-weighted count in every unit ordinate interval is at most C₀ log(|t|+3). Define

v_z=(φ̂(z−α_k))_{0≤k<d},

G₀=(aL²)^−1 Σ_{t∈I}m_z v_z v_zᵀ,

E₀=(aL²)^−1 Σ_{t∉I}m_z v_z v_zᵀ,

F=G₀+E₀.

The nuclear convergence of the last sum is proved below. The matrix F is the full zero matrix; identifying it with the prime-side integral and evaluating its Hilbert–Schmidt norm are separate analytic inputs. Both G₀ and E₀ are real symmetric after pairing ρ with 1−conj(ρ), since this pairing preserves t and sends v to conj(v). The interval selection therefore preserves exact block structure.

## A rank-one nuclear-norm point that must not be replaced by a trace estimate

For complex v,

v vᵀ = v (conj(v))*.

A rank-one matrix x y* has its single nonzero singular value equal to ||x||₂||y||₂. Thus

||v vᵀ||₁=||v||²₂.

This equality is valid even though tr(vvᵀ)=Σv_k² can have cancellation. It justifies the triangle estimate for E₀. No positivity of vvᵀ is assumed.

## Uniform local mass and retained-grid tails

For z=t+iη, Parseval on the support interval of length L gives

Σ_{k∈Z}|φ̂(z−α_k)|²=L∫φ(u)²e^{2ηu}du.

Since |η|≤1/2 and |φ|≤M,

∫φ(u)²e^{2ηu}du ≤ M²·2∫₀^{L/2}cosh(u)du ≤ M² e^{L/2}.

Consequently the normalized retained mass

q(z):=(aL²)^−1||v_z||²₂

satisfies q(z)≤C√X/L uniformly in t and η. This is the absolute-square estimate, distinct from the bilinear Poisson identity for the trace.

If t is outside I with D=dist(t,I)≥1, all retained α_k lie in I. A one-sided lattice comparison gives

Σ_{0≤k<d}|t−α_k|^−4 ≤ C(D^−4+h^−1D^−3) ≤ C L D^−3.

The C² transform bound then gives

q(z)≤C(√X/L)D^−3.             (1)

The floor in d causes no loss in this exterior retained-grid estimate: α_k∈I for every retained k. The first omitted grid point is irrelevant to (1).

## Summing all omitted zeros, including negative and arbitrarily large ordinates

The omitted ordinates with D<1 lie in two intervals of length one. Their multiplicity is O(L), so their total normalized mass is O(√X).

For D≥1, partition into D∈[j,j+1), j=1,2,… . Each such set consists of at most two unit intervals, and their ordinates have absolute value at most 2T+j+1. Hence the zero-count hypothesis implies

Σ_{t∉I,D≥1}m_z D^−3

≤ C Σ_{j≥1}j^−3 log(2T+j+4)

≤ C [log(2T+4)Σj^−3+Σj^−3log(j+1)]

=O(L).

This explicitly includes the whole lower half-plane ordinate range and all large positive ordinates. It does not truncate the zero sum at height 3T. Combining with (1),

Σ_{t∉I}m_z q(z)=O(√X).

In particular the infinite matrix series converges absolutely in nuclear norm and

||E₀||₁≤Σ_{t∉I}m_z q(z)=O(√X)=O(√T).             (2)

The same proof for 1≤U≤T/2, omitting only ordinates outside I′_U=[T−U,2T+U), gives O(√X/U²). Together with the unit-strip argument this may be written uniformly as O(√X/(1+U)²) for 0≤U≤T/2, with constants enlarged. This unified bound is not needed for U=0.

## What Hilbert–Schmidt accuracy is actually needed

Suppose, as a separate analytic input, that

||F||²_HS=κN+o(N),     N=N(I)∼TL/(2π).

Then ||F||_HS=O(√N). From (2) and ||E₀||_HS≤||E₀||₁,

| ||G₀||²_HS−||F||²_HS |

≤2||F||_HS||E₀||_HS+||E₀||²_HS

=O(√N√T+T)=O(N/√L)=o(N).

Therefore ||G₀||²_HS=κN+o(N). If the full-matrix input has a quantitative remainder r(T)N, the finite-matrix remainder obtained here is O((r(T)+L^−1/2)N). An O(N/L) or O(N log log T/L) rate cannot be inferred unchanged from this unbuffered proof.

The trace proof in `AF_trace_localization_skeptic_round2.md`, specialized to U=0, gives tr G₀=N(I)+O(√T)=N+o(N). This part uses the bilinear Poisson identity and the correct omitted-grid endpoint treatment; it is not obtained by taking the trace of (2), whose scale alone would not identify the full trace with N.

## Direct reconstruction of every §6 dependency relevant here

Let s₁ be the number of simple on-line zero points in I, s₂ the number of multiple on-line points in I, and p the number of off-line conjugate-functional-equation pairs in I. Then

N≥s₁+2s₂+2p,       N_d(I)=s₁+s₂+2p.

Let P₁ be the normalized contribution of the simple on-line zeros to G₀, and Q′=G₀−P₁. These are exact finite matrices. Lemma 2.1 at real ordinates gives P₁≥0, rank P₁≤s₁ and tr P₁≤s₁. The block pullback proof of Lemma 3.1 gives n₊(Q′)≤s₂+p. There is no approximation to Q′ here.

Assuming the source's separately checked rank–trace inequality (Lemma 3.2),

s₁≥rank P₁

≥4tr G₀−2tr P₁−4(s₂+p)−||G₀||²_HS

≥4tr G₀−2N−||G₀||²_HS

=(2−κ−o(1))N.

Alternatively, rearranging the same inequality using tr P₁≤s₁ gives

3s₁+4(s₂+p)≥4tr G₀−||G₀||²_HS.

Subtracting s₁+2s₂+2p≤N yields

2(s₁+s₂+p)≥(3−κ−o(1))N,

and hence N_d(I)≥(3−κ−o(1))N/2. The subtracted inequality has the correct direction: an upper bound on the subtracted expression gives a lower bound on the difference.

All quantities refer to I itself, so no buffer-to-I count correction occurs. Changing the paper's half-open matrix interval to its conventional count interval changes endpoint multiplicities by O(L), already negligible. The dyadic passage to cumulative leading proportions needs only a uniform eventual o(1) error; finitely many initial windows contribute o(N(T)).

Inspection of §6 finds no invocation of Lemma 3.4 (Weyl), no spectral perturbation at a fixed positive threshold, and no requirement ||E||_op=o(1). Lemma 3.4 is stated in §3 but is not used in this displayed proof. Its omission is specifically why the stronger √T buffer is not forced by the leading-constant calculation inspected here.

## Consequences, limits and next check

This is a useful hypothesis weakening in the truncation layer: a tail may grow in nuclear norm while remaining small on the √N scale relevant to a squared Hilbert–Schmidt moment. The frozen √T buffer supplies a much stronger operator estimate than this specific leading-constant route needs.

For intermediate buffers, the same calculation gives an additional relative moment error O(L^−1/2(1+U)^−2+L^−1(1+U)^−4). In particular U=L^1/4 already makes this O(1/L), while its count loss O(UL) is negligible. This observation concerns the truncation loss only; any other analytic error may dominate.

No zero-proportion constant has been improved. No priority or novelty claim is made. The full-matrix moment, explicit-formula identification, exact rank–trace inequality, and any extensions to other L-functions remain separate dependencies. The practical next step is to integrate this finite-matrix route with the independently audited full-matrix estimate, retaining that estimate's true window hypotheses and convergence justifications. It must not be promoted to a complete proof solely from this scoped review.

Status: independently reconstructed scoped argument; parent analytic reviewer independently reached the same U=0 conclusion and was informed of the proof. Final director adjudication and archive-level classification remain separate.
