# M-30501 — Review protocol for the terminal-boundary obstruction

Freeze PR #304 at

```text
78b75fc17e27334a9950018528c1c6e083d74820
```

Reconstruct, in this order:

1. the stopped-power identity of PR #301;
2. the active-output condition `Y>=2q-1`;
3. the exact aggregate formula (L-30501.4);
4. the transition-annulus finite residual;
5. the upper bound for the analytic power tail;
6. the unique divisor source on `M=floor((X+1)/2)`;
7. the atomic lower bound of `L-30501`;
8. the per-layer flow identity and activation firewall of `L-30502`.

Automatic rejection of `R-30501` occurs if any one of the following is shown:

- the active analytic weight is not `log(X/(2q-1))`;
- a finite central term other than `w_X(2q-1)` survives on the declared band;
- the eta Euler lower bound or faster-power upper bound is wrong;
- the PR #304 source is allowed support beyond the declared next endpoint;
- the source norm used in `L-30403` is not the square-root atomic norm.

Cancellation in the optimized flow does not rescue the frozen atomic-norm
claim. It is a distinct theorem and remains open.
