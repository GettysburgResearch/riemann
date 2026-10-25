# Independent review of the mixed numerator certificate

Reviewer: `two_sign_hlc`, independently of the author of the reviewed
mathematics and checker. Review date: 2026-10-25.

## Verdict and exact scope

**PASS for the explicitly supplied scalar comparison system.** I found no
mathematical defect in the free-geometry reduction, blockwise numerator
envelope, exact critical averaged dual, six strict rational duals, or their
case coverage. The proof establishes the stated fixed-input conclusion
`B >= B_flat`, including the class-by-class choice of the two specified
numerator resources and unequal total lengths.

This review does not certify the external analytic preprints, an improved
arithmetic moment, absence of an actual zero class, or a new zero-free
region. The moment/count formulas and their character compatibility remain
load-bearing premises. In particular, a failure of these supplied majorants
to close is not a lower bound for the true arithmetic error.

## Reviewed local bytes

| File | Bytes | SHA256 | Git blob SHA1 |
|---|---:|---|---|
| `MIXED_NUMERATOR.md` | 15992 | `b14afb2e2a197fda1f275383e8d96b54326f1188614a0a96e2b00ebe29970935` | `cc622f746ca4dca7ba79068e5de251570f1ebeb4` |
| `check_mixed_numerator.py` | 9164 | `cfdfce4a3af0793cf063ddc0801655d586aca6a32a3a548a018e1850d3cb12e7` | `c71c5cb8e337e49f6dea137014cb059b5c2facd3` |
| `MIXED_NUMERATOR_CHECKS.json` | 7806 | `489b42882112a32202f6a39f52eb4a81ce5eeab79ed26b5595ad4c6e6c6b3837` | `bbfdd8968d6326b64056d8011ac6049bf6f28ae9` |

The Git blob identifiers were computed from the actual local UTF-8 bytes,
including the Git object header. They are not assertions that these bytes
have yet been committed remotely. No remote authentication is included in
this version of the review.

## 1. The numerator envelope was derived independently

For each of the four retained classes, write

\[
 m_* = \frac{Q-u/2-R}{p-u}.
\]

The exact interval checks prove `p>u` and `0<m_*<1/2`. Thus the smaller
block exponent has slope `p` before the crossing and slope `u` after it.
Direct maximization, including both endpoints, gives

\[
 \nu(\theta)=
 \begin{cases}
 Q-\theta/2,&0\le\theta\le u,\\
 R+(p-\theta)m_*,&u\le\theta\le p,\\
 R,&\theta\ge p.
 \end{cases}
\]

The values agree at both breakpoints. This calculation includes the choice
of the better bound separately on each approximate-functional-equation
block; it does not first force one method on the whole numerator.

For either numerator contour side, the additional tilt is `d theta`, where
the better of the two sides has `d=min(l_y,h-l_y)`. The low constraints
prove `h>0` and `0<=d<=h/2`. Consequently `h nu(theta)+d theta` is
nonincreasing on `[0,u]`, affine on `[u,p]`, and nondecreasing on
`[p,infinity)`. Its minimum is attained at `u` or `p`. The two values are

\[
 hQ-u(h/2-d),\qquad hR+pd,
\]

which are exactly equations (10)-(12) after restoring the common outside
term. In particular the signs of the two averaged tilts are correct.

The normalized pointwise block exponent in (7) is consistent with the
buffered real-part parameter `a=(1+delta)/2`: shifting a smooth plain
block to that line costs `D^(a-1/2)`. The other exponent uses the same
prime-amplified product moment as the imported numerator resource, with
remaining capacity `(1-2m)/(6 kappa)`. Natural zeros and the common
character are not replaced by independent coefficients in this argument.

I also checked the source locators in Liu's primary
[arXiv:2610.26835v1](https://arxiv.org/html/2610.26835v1), especially
Proposition 14.3, Remark 14.13, and Section 15.3. The source itself limits
its earlier optimality statement; the present note explicitly defines a
larger scalar system. Granting greater prime supply, more contour freedom,
and omission of positive losses can only decrease its best available
majorant. The note does not claim analytic continuation in those enlarged
boxes. This is the correct direction for the stated obstruction.

## 2. The free-length box is a consequence, not an extra restriction

I independently expanded the direct majorant in `M,b,ell`. Its five low
constraints in (13) have the displayed coefficients. Their positive
combination in (14) cancels both `M` and `ell` and equals `13/15`.

For a proposed improvement with `B<7/8`, `L_K<=B` gives
`14M+8ell<13`. With `M,ell>=0`, this proves `M<13/14<1`, `ell<2`, and
`h-l_y=1-M+ell>1/14`. The assumption `l_y>=0` gives `b>=-M>-1`.
The additional branch `G>=b-l_y/2` gives
`b<1/16+(M+ell)/4<13/16<1`.

Thus every proposed improvement lies in the safe closed box used by the
rounding proof. No positivity of `l_x`, no balanced-length identity, and no
positivity of `b` were inserted. The class range is also legitimate:
`B>=13/15` implies `2B-1>=11/15`, and every one of the four tested
classes lies strictly between `1/8` and `11/15`.

## 3. Exact averaged dual and exhaustive mixed choices

I checked the reduction of the critical averaged constraint to (20).
The coefficient of `b` vanishes using
`Q_c=2/3+u/2`; its remaining coefficients are

\[
 1+g+u,\qquad -(1/2+u),\qquad g+u
\]

for the constant, `M`, and `ell`, respectively. The three weights (21)
are positive, add to one, and cancel the `M` and `ell` coefficients
exactly. Their constant is the expression in (22). The polynomial
identity in the checker proves its equality to `(1+kappa)/2` without
treating a printed decimal as the exact root.

The six strict duals do cover all alternatives. On `l_y<=h/2`, the two
choices at the critical class are separately excluded. On `l_y>=h/2`,
the exact dual first excludes averaged at that class. With pointwise there,
the remaining duals successively exclude pointwise at `xi`, pointwise at
`43/100` after averaged at `xi`, pointwise at `9/20` after averaged at
`43/100`, and finally averaged at `9/20`. This argument permits an
arbitrary choice for each class. It assumes no monotone threshold for
switching the numerator method.

The negative-side duals add a positive multiple of the valid inequality
`0>=2l_y-h`. That sign is correct: it produces a weaker affine right side
while leaving the coefficient of `B` equal to one. The residual allowance
`|r_M|+|r_b|+2|r_ell|` is valid throughout the derived box, including its
boundary.

## 4. Exact checker replay and independent arithmetic checks

I ran a copy of the checker in `/tmp/mixed-numerator-review`, so the replay
did not alter the author's three files. It completed with `PASS` and
generated a JSON report byte-for-byte identical to the reviewed report.
The checker uses exact rational interval operations for every acceptance
inequality. Its floating-point conversions occur only after acceptance,
for readable diagnostic output.

I separately checked the following using exact `Fraction` arithmetic:

* Every strict dual floor exceeds the upper endpoint of the isolated
  `B_flat` interval by more than `179087019/10^14`. This verifies the
  quoted `0.00000179087019` lower margin without trusting a rounded
  decimal difference.
* The computed interval for `delta_c` lies inside `(23/50,12/25)`, the
  intended critical-root interval.
* Replaying under `python -O` refuses to run with a nonzero exit status.
  Thus Python's assertion-removal mode cannot silently produce `PASS`.

I inspected the quartic sign and derivative tests, the smaller-root
quadratic isolation, all three exact polynomial identity checks, the
six affine coefficient constructions, and the output residual formula.
The reversed-interval negative control also runs as stated. The report's
smallest displayed margin is approximately `1.7908701921183294e-6`;
the acceptance is the exact rational comparison above.

## 5. Joint-witness test, sensitivity, and limitations

The difference (29) follows by direct subtraction. Its interpretation
is correct where the same M2 product resource applies: the remaining
prime capacity must be nonnegative and use the source-compatible
presentation. At my suggestion the author made the natural detector/AFE
range `0<=m,v<=1/2` explicit before (27). I read that clarification and
bound this review to the updated bytes in the table above.

At the crossing, `R_P(m)=R`, so this use of the ordinary witness does
not give a better numerator exponent. For a different split where an
independent plain count is stronger, that stronger count must first be
retained; the note does not claim otherwise.

The sensitivity calculation (31) is also correct: replacing the increasing
long count by that count minus `eta` moves the intersection by
`eta/(alpha-delta_c+C_c)` and lowers the crossing value by
`C_c eta/(alpha-delta_c+C_c)=2(t_c-1)eta`. This remains a conditional
scalar calculation, not a proof that an arbitrary moment gain produces a
new zero-free region.

Finally, the extension to larger licensed `kappa` has the right monotonicity
on these same classes: `R` increases, `u` decreases, `h>0`, and both
terms in (10) become no better. It excludes crossing below `B_flat` by a
finite sequence using this fixed collection of resources and previously
available boundaries at least `B_flat`. It does not address an unknown
smaller actual family cap, a new joint moment, an excluded critical class,
or a different arithmetic estimate.
