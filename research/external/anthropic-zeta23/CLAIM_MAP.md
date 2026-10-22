# Claim and interface map

This table maps the external paper to the pinned Lean repository and to the nearest resident/source-pinned Riemann-program interfaces. It is an orientation aid, not an assertion that the implementations are definitionally identical.

| Mathematical object | Paper location | Pinned Lean area | Nearest repository interface | Import action |
|---|---|---|---|---|
| Nontrivial zeros, multiplicity, `N`, `N0star`, `N0simple`, `Ndist` | §1.3 | `Zeta23/Statement.lean`, `Defs/Counting` | all zero-count consumers | Adopt names only through an explicit dictionary; preserve endpoint convention `(T,2T]`. |
| Centered zero coordinate `gamma_rho=(rho-1/2)/i` | §1.8, §2.1 | `Defs`, `WeilEF` | B0 centered-Weil source | Make this the candidate common zero coordinate. |
| Weil Hermitian form | §2.1 | `WeilEF/` | A0/B0 explicit-formula source contract | Extract a source-qualified statement and normalization fingerprint. |
| Compact taper and support `[-L/2,L/2]` | §2.2 | `Taper/` | support-domain interfaces in Weil/screw/operator packets | Reuse the support and differentiability contract; do not import only the final constants. |
| Critical-density Gabor family and Poisson identity | Lemma 2.2 | `Poisson.lean`, `Poisson/PaperFT.lean` | finite compression / cardinal frame programs | Add as a new finite compression constructor, separate from Xi-cardinal interpolation. |
| Rank–trace inequality | Lemma 3.2 | `LinAlg/`, `ZeroSide/Mult.lean` | B4 kernel/inertia classifier | Import as a general matrix lemma with equality case and parameter `c`. |
| Tail operator/trace norm | Proposition 4.2 | `Tail/` | complete-capture and unseen-zero radii | Compare directly against B0/B4 tail metrics; keep operator norm and trace norm distinct. |
| Hyperbolic off-line pair block | Proposition 4.1 | `ZeroSide/` | PR #199 off-line cardinal gap | State one dictionary: hyperbolic block in the sampled frame versus negative cardinal direction in the complete kernel. |
| First and second trace moments | Theorem 5.8 | `PrimeSideA/`, `PrimeSideB/` | finite Weil/carrier prime-side engines | Import the asymptotic theorem, not numerical illustrations, as the arithmetic input. |
| `2/3` on-line/simple certificate | Theorems A/B | `FinalMult.lean` | no current resident analogue | Add as external source-pinned theorem after independent review. |
| `5/6` distinct certificate | Theorem C | `FinalMult.lean`, `Assembly/CertificateC3` | multiplicity/counting programs | Import the `c=3` route explicitly; do not derive it from a weaker Cauchy–Schwarz statement. |
| Montgomery–Taylor optimum | Theorem D, §7.1 | `ThmD/` | window/filter optimization branches | Treat scalar support-one optimization as closed. |
| Primitive Dirichlet `L`-functions | Theorem E, §7.3 | `ThmE/`, `ThmDE/` | broader explicit-formula source contract | Separate fixed-conductor theorem from heuristic hybrid/uniform ranges. |
| `xi'` extension | §7.3 remark / later repo extension | `XiPrime/` | derivative/Loewner programs | Review independently; do not inherit the zeta verdict automatically. |
| Bandwidth-one ceiling | Remark 1.1 / later repo extension | `PairCeiling/` | obstruction/fence methodology | Import as a barrier result, including its displayed enclosure hypothesis. |

## Recommended canonical dictionary

```text
paper W(f,g)             <-> centered Weil form Q_W
paper coefficient matrix <-> finite sampled compression R_V
on-line atom P           <-> visible positive selected-zero direction
off-line hyperbolic Q    <-> off-line cardinal/kernel signature
far-zero E               <-> unseen-zero/tail operator
tr(R), ||R||_F^2         <-> prime-side moment data
n_+(Q), rank(P)          <-> zero-side count data
```

The dictionary must be proved at the form level. Similar-looking matrices in different coefficient metrics must not be identified by notation alone.
