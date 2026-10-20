# Independent scoped review of the Liu scalar barrier extensions

**Reviewer:** `repo_routes_audit`, independent of the author of the two barrier notes and their checker.
**Disposition:** No material mathematical gap found in the stated balanced hybrid theorem or its explicitly defined free-length, four-endpoint extension. This is a review of a scalar estimate system. It does not verify Liu's analytic moment theorems, prove existence of formal critical classes, or exclude better bounds for actual character sums.

## Reviewed versions

The hashes below identify the exact files reviewed. The free-length note includes the one additional domain check described below, authorized by the root reviewer. No other authored-file changes were made in this review.

| File | SHA-256 |
|---|---|
| `beyond_free_length_barrier.md` | `288fa1bc97d11dc03ed021fa8831c080d83b050482d586a388b5b47677b585d4` |
| `beyond_hybrid_barrier.md` (final version, including documentation delta reviewed below) | `ed7cd4bb99ad5920ef9a58c48c4b458646d710382ad9ac0a099438a7e18065f6` |
| `beyond_hybrid_barrier.py` | `e2277fd388c64953ff626e551046af3c9ecdfca8458c5af4a38815f259fbeb1b` |
| Frozen PR #1005 `JOINT_NUMERATOR_CLOSURE.md` | `097e2581de59de31585de17d7cc7d2b949125d01c852e68f2c104228b5a09dab` |

The last file was fetched from the frozen PR #1005 commit `d3b3d19573b8dc47ac6e37abd108d54982e9e5f1`; its local review copy is in `work/repo_sources/`.

### Final documentation delta review

The original mathematical review of `beyond_hybrid_barrier.md` covered SHA-256 `b5f06342f29b4d0092296a219e3fcd8d050c92041e66a5c7c7a84b346cb88def` (9,771 bytes). The final version in the table is 10,051 bytes. I inspected the final file and verified that removing exactly two additions in memory reconstructs the original 9,771-byte file and its original SHA-256:

- The command `python -I -S -B -O run_barrier_mutations.py` in Section 4's replay block.
- The following three-line paragraph describing its three negative controls, its source SHA-256 binding, and preservation of the original checker.

There are no changes to the hypotheses, mathematical formulas, witness intervals, proof, or scope statements. The additional review therefore covers this documentation delta; the mathematical review below applies unchanged to the final version.

I also inspected `run_barrier_mutations.py` at SHA-256 `b9a60dab804e1fec10456a7c5dc3e144126992355a54acc7c2b70926248c6c03` and executed `python -I -S -B -O work/run_barrier_mutations.py`. It returned `PASS`, rejecting the changed quartic, displaced witness boundary, and reversed unequal-length coefficient at their three designated gates. Its receipt identifies the unchanged checker SHA-256 `e2277fd388c64953ff626e551046af3c9ecdfca8458c5af4a38815f259fbeb1b`. The script writes mutated copies only to an automatically removed temporary directory. This confirms the new replay description without extending the analytic scope of the review. I did not modify the final mathematics file during this delta review.

## 1. Free total length and the sign of the row scale

The direct dual is valid in the stated relaxed domain. Indeed, writing the direct expression as

\[
B_{\rm low}=\frac56+\frac{M-b}{12}-\frac\ell6+G+\frac K2,
\]

the condition \(G\ge\max(0,b/12)\) implies \(G-b/12\ge0\). Using the three appropriate lower bounds for \(K\) gives the displayed \(L_0,L_K,L_J\), whose positive weighted sum is exactly \(13/15\). No assumption \(b\ge0\), \(l_x>\ell\), or \(M=1-\ell\) is used here.

One domain detail was initially implicit. An attempted boundary \(B\le B_0<7/8\) satisfies

\[
\frac13+\frac{7M}{12}+\frac\ell3=L_K\le B<\frac78,
\]

so \(M<13/14\) because \(\ell\ge0\). Since \(l_y\ge0\), one has \(l_x=M-l_y\le M\), and hence

\[
h=1-l_x+\ell\ge1-M+\ell>\frac1{14}.
\]

Thus evaluating the final row at \(d=h\) does not introduce a negative or zero row exponent, even in the relaxed domain and even if \(l_x\) itself is allowed to be negative. This check has now been added immediately after the direct dual in the free-length note.

## 2. Direct cost and the free-length reduction

I independently rearranged the direct cost with \(t=M-(1-\ell)\). The exact identity is

\[
B_{\rm low}=\frac{11}{12}-\frac\ell4+\frac t{12}
 +(G-b/12)+\frac K2.
\]

Because \(G-b/12\ge(-b)_+/12\), the resource inequality (6) follows with the stated coefficients. In particular, dropping the \((-b)_+/3\) term would invalidate the argument for negative asymmetry; the note retains it.

I checked the four affine endpoint reductions, their balanced \(b\)-slopes, and the paid slopes against the displayed endpoint formulas. The total-length argument uses

\[
E_j-E_j^\circ\ge(4A_j+1)\Delta+
 A_j(-b)_+/3+(C_j+A_j/3)t+2A_jK.
\]

For \(t<0\), the coefficient \(C_j+A_j/3\) is strictly negative, so its product with \(t\) is positive. For \(t>0\), \(K\ge t\) instead produces the strictly positive coefficient \(C_j+7A_j/3\). The note uses the correct sign in both cases. The listed rational lower bounds for the relevant coefficients follow from \(R\ge1-\delta\) and \(0\le\delta\le12/25\). Consequently equation (8), including strictness when \(t\ne0\), is valid.

For \(b<0\), every paid slope \(s_j-A_j/3\) in (11) is strictly negative at the witness class. Multiplication by negative \(b\) therefore raises the lower bound. Reducing to \(b=0\) before using monotonicity in \(\kappa\) is important; the proof does this correctly.

## 3. Witness coverage and strictness

The four intervals in the balanced cover meet at their endpoints and cover the entire positive ray. Each exponent is affine in \(b\), and the checked slope signs select the correct interval endpoint. The first-row argument also applies at \(b=0\): its pointwise lower bound remains positive, and the averaged identity is separately checked at \(b=0\). This justifies the use of that class in the free-length proof.

The free-length direct floor gives \(2B-1\ge11/15\), whereas all four witness values of \(\delta\) lie between \(1/8\) and \(12/25\). Thus none of the displayed witnesses disappears from the required class range after varying \(M\), \(b\), or \(\ell\).

The critical averaged exponent is exactly zero, rather than a numerical near-zero. Its direct quotient-ring computation at \(b=0,1\), together with affinity in \(b\), proves the required identity at every \(b\). All denominators inverted in that calculation are required to be coprime to the quartic. The rational isolating interval specifies the correct real branch.

At balanced \(\ell_0\) and nonnegative \(b\), the two unused endpoint differences are strictly positive. Both principal endpoints increase strictly with \(\kappa\) at each witness because \(R\) increases, \(h>0\), and the extra averaged coefficient of \(c=1/(3\kappa)\) is negative. The two endpoint differences in (9) then preserve positivity of the other endpoints. When \(B<B_0\), the positive \((4A_j+1)\Delta\) term supplies strictness independently. The stated endpoint exclusion and finite-chain conclusion therefore have the required strict inequalities.

## 4. Exact checker review and execution

I read the checker, including its interval arithmetic, polynomial remainder arithmetic, quotient-ring denominator checks, direct critical substitution, sparse affine identities, and positive-coefficient substitutions. I also executed both

```sh
python -I -S -B work/beyond_hybrid_barrier.py
python -I -S -B -O work/beyond_hybrid_barrier.py
```

Both completed with `PASS` and identical displayed receipts. Acceptance uses explicit exceptions rather than removable Python assertions. Floating-point values occur only in human-readable receipt displays. These executions support the finite algebraic certificate; they are not analytic proof replays.

## 5. Intermediate-contour scope must remain explicit

The frozen PR #1005 reduction assumes, among other conditions, a physical prime-supply lower bound and the balanced geometry

\[
h=l_y+2\ell,\qquad h/2<l_y<h.
\]

Its contour envelope then has affine pieces, whose minimum lies at the stated pointwise or averaged endpoint. The balanced note invokes this result only under those hypotheses. Its comparison parameters and witness classes meet the displayed count and \(\kappa\) ranges; any analytic application must also retain the prime-supply and source hypotheses of that earlier note.

The free-length note proves an obstruction for **four explicit endpoints** and the affine shifts between its two averaged endpoints. It does not establish a universal reduction of every intermediate reflected-numerator construction at arbitrary unequal lengths to those four endpoints. This limitation is stated explicitly in its final section and should be retained in the import, PR description, and any headline summary. Saying that the two omissions in Liu's Remark 14.13 are tested *within this four-endpoint system* is supported; claiming that all possible unequal-length contour methods are excluded would go beyond the proof.

No further correction is required for the mathematical statements at the reviewed hashes.
