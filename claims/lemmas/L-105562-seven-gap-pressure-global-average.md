# L-105562 — Source-locked seven-gap pressure and global averaging

Claim ID: `L-105562`  
Status: **PROVED DEDUCTION FROM A PINNED INTERVAL CERTIFICATE**

Use the exact external source

```text
ainta/zeta-simple-zeros
commit 040c5e899e658aed7b56a2a87f501798fe10761d
```

The interval verifier proves, for all nonnegative `g1,...,g6`,

\[
\frac1{3000}\sum_{i=1}^6g_i
+
\sum_{s=1}^6\frac2{7-s}
\sum_{i=1}^{7-s}
 w(g_i+\cdots+g_{i+s-1})
\ge\frac{19}{5000},
\tag{1}
\]

where `w=k^2`. The retained certificate reports 707,901 branch-and-bound
nodes at 128-bit Arb precision. The source audit confirms:

1. every kernel and derivative enclosure is an Arb interval;
2. every binary64 operation used in pruning is widened outward;
3. interval, pressure, and tangent pruning are independently one-sided;
4. every unpruned terminal cell raises an error.

For ordered points `y1<...<ym`, put

\[
E_m=2\sum_{i<j}w(y_j-y_i).
\]

Summing (1) over all consecutive seven-point windows gives

\[
\boxed{
E_m+\frac1{500}(y_m-y_1)
\ge\frac{19}{5000}(m-6).
}
\tag{2}
\]

The coefficient `1/500` is forced because an interior gap appears in six
windows.

Choose `m=269`. Convex pinching gives, for each corresponding principal block,

\[
\Delta(G_B)+\frac1{500}\operatorname{span}(B)
\ge\frac{4997}{5000}-o(1).
\tag{3}
\]

Average (3) over all 269 block offsets. Every interior gap is charged at most
268 times, and the total normalized length is `N+o(N)`. Hence

\[
\boxed{
\Delta(M)
\ge
\frac{4997}{1\,345\,000}S
-
\frac{268}{134\,500}N-o(N).
}
\tag{4}
\]

No sampled numerical minimum is used in the deduction. The external interval
certificate is the only computer-assisted premise.
