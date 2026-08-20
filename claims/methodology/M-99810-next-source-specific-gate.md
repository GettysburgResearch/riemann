# M-99810 — Next source-specific gate: Abelian phase gap to block Carleson localization

The global phase-owner energy is no longer conjectural: `L-99812` proves that
its critical Abelian mean tends to `2` for every fixed nonzero phase.  The
remaining work is localization, not discovery of a coercive quantity.

A viable proof should proceed in this order:

1. retain the exact three-band squarefree-core source
   \[
   h(x)=\sum_{(m,67)=1}\mu(m)m^{-1/2}\Phi(x/m);
   \]
2. dyadically or 67-adically localize in `log m` without taking absolute values;
3. insert the phase-owner identity before summing the core index;
4. use the Abelian gap to pay the good-core sector;
5. prove a power-saving counting theorem for low phase-energy cores;
6. absorb the activation reset using the positive Hurwitz bound in `L-99810`;
7. conclude the block-L2 estimate `X^{o(1)}`.

Two shortcuts are forbidden:

- coefficientwise positive inverse completion, by `L-99811`;
- one-chain Poincare or entropy, by PR #656's exact zero-dissipation sector.

The desired theorem is a multiplicative Carleson embedding on the actual
squarefree-core Gram.  It is the narrowest remaining gate and is logically
equivalent to RH, so every proof must expose the arithmetic cancellation rather
than replace it by a source-blind norm.
