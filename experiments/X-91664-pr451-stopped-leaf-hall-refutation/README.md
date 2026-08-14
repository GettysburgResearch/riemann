# X-91664 — PR #451 stopped-leaf Hall refutation

This exact directed replay checks the first broken arrow in PR #451 at frozen head:

```text
PR:   #451
head: f41797c91497dc462f549a127d8494bbe4ccde2f
```

The stopped-leaf theorem permits

```text
p >= 67,
1 <= y < 67,
parent Hall parameter x = p y.
```

For the survival target, the normalized no-upward prefix margin is

\[
\mathcal H_{\alpha_s,t}(py)
=
\alpha_s\sqrt{py}\,A_t-B_t,
\qquad
\alpha_s=\frac{2(2+p^{-1/2})}{3+p^{-1/2}}.
\]

At

\[
p=67,\qquad y=13,\qquad t=13,\qquad py=871,
\]

the replay proves directionally

\[
-2.140
<
\mathcal H_{\alpha_s,13}(871)
<
-2.139.
\]

The omitted survival prefactor `(1-p^{-1/2})(3+p^{-1/2})` is positive, so the physical survival-target prefix is also negative. Therefore the nested no-upward Hall transport required in `L-91621.12` does not exist.

The obstruction is an infinite family. For fixed `y=13`,

\[
\alpha_s(p)\sqrt p
=
\frac{2u(1+2u)}{1+3u},
\qquad u=\sqrt p,
\]

and its derivative has numerator `2+8u+12u^2>0`. Since `A_13=-2323/30030<0`, the margin decreases as `p` increases.

Run:

```bash
python3 verify.py
sha256sum -c SHA256SUMS
```

Expected:

```text
PASS_PR451_STOPPED_LEAF_HALL_REFUTATION
```

This replay refutes the universal Hall producer, not the exact native response identities or the conditional parent-minus-child-plus-replacement algebra.
