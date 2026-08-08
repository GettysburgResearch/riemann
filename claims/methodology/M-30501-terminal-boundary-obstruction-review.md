# M-30501 — Review protocol for the terminal-boundary obstruction

Freeze PR #304 at

```text
78b75fc17e27334a9950018528c1c6e083d74820
```

Reconstruct, in this order:

1. the stopped-power identity of PR #301;
2. the analytic coefficient lower bound in `L-28401`;
3. the top-annulus finite residual;
4. the exact aggregate boundary `b_X`;
5. the unique divisor source on `M=floor((X+1)/2)`;
6. the atomic lower bound of `L-30501`.

Automatic rejection of `R-30501` occurs if any one of the following is shown:

- the aggregate boundary is not (L-30501.4);
- a finite central term other than `w_X(2q-1)` survives on the declared annulus;
- the analytic faster-power coefficients have a negative contribution;
- the PR #304 source is allowed support beyond the declared next endpoint;
- the source norm used in `L-30403` is not the square-root atomic norm.

Do not attempt to rescue PR #304 by citing cancellation in the optimized flow:
that is a different theorem and is explicitly left open by this audit.
