# O-91417 — Proposed shift-eight Hall proof for the cutoff-minor kernel

Status: **PROPOSED; PENDING DIRECTED PROOF**. RH remains unproved.

For an actual cutoff `c`, define the nonnegative kernel from `L-91416`
\[
M_{j,c}(d)=K_R^{(j)}(d)K_S(c)-K_S(d)K_R^{(j)}(c),
\qquad d<c.
\]
Its signed total is exactly the strict-prefix determinant `Pi_(j,c)`.

A stronger sufficient theorem is the shifted Hall family
\[
\boxed{
\sum_{\substack{e<c,\ \mu(e)=1\\e\le t+8}}M_{j,c}(e)
-
\sum_{\substack{o<c,\ \mu(o)=-1\\o\le t}}M_{j,c}(o)
\ge0
}
\]
for every odd threshold `t<c`.

If proved, nested-neighborhood Hall gives a positive source-labelled decomposition of the cutoff-minor kernel and in particular `Pi_(j,c)>=0`.

Decimal reconnaissance over `30,485` triples

```text
p in {67,83,101,167,257,509,1009};
y=1,...,67;
j=2,...,66
```

found no negative shifted margin. The smallest observed margin was about `8.536086e-4` at `p=67,y=1,j=66,c=46,t=2`.

The production target is a directed cell proof retaining the causal cutoffs. This route is stronger than the scalar determinant route because it exports the missing row provenance packet.
