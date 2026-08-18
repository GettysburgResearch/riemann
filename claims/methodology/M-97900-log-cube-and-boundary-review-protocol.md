# M-97900 — Hostile review protocol for logarithmic cubes and top-history completion

Review in the following order.

1. **Base asymptotic.** Reconstruct the exact scope of
   `b(Y)=a_*sqrt(Y)+c_*+O(Y^-3/2)` and the global bound
   `0<=b(Y)<=C sqrt(Y)` from the frozen `P_61` theorem.
2. **Quadratic-log cube.** In `L-97903`, check the split
   `d<=X/(log X)^10` versus the activated tail. Verify separately:
   - the half-weight Rankin bound;
   - the unsigned constant-term product;
   - `X^-2 sum_(d<=D)d=O((log X)^-20)`;
   - the positive Mertens product.
3. **Top completion.** Expand
   `prod_(q>p)(E_q+q^-1 T_q)=I` on a finite prime set and verify that the owner
   `p=min A` makes every nonempty top set appear exactly once.
4. **No source fiction.** Equation
   `U^hatA=prod_(q in A)E_q^-1 U_full` is used only as an analytic value bound.
   Its geometric series contains repeated prime powers and is not a source-owner
   decomposition. The exact source theorem is the squarefree complement
   expansion in `L-97901`.
5. **Full-state PNT.** Check the split at `sqrt(Y)` and partial summation of the
   bounded factor-four hinge against the classical Mertens bound. Include the
   fixed unit and two/four-shift terms.
6. **High-owner boundary.** Verify that the top completion converts the entire
   owner sum into squarefree `H`-rough products, then apply the upper-bound
   sieve to the interval `(X/L,X/2]`. Do not reintroduce the earlier spurious
   factor `log X/log H` into the short multiplicative interval.
7. **Constant-killing filter.** Confirm
   `b(Y)-b(Y/4)=(a_*/2)sqrt(Y)+O(Y^-3/2)` and that the normalized filter is
   `U(Y)-1/2 U(Y/4)`.
8. **Subpower Rankin tail.** For `Z=X^(1/K)`, check
   `eta=log K/log Z`, `Z^eta=K`, and the exponent
   `-K log K+O(K/log K)`.
9. **Boundary collapse.** In `T-97902`, verify `Z>exp(K)` and hence every
   omitted prime is inactive at terminal endpoints below `exp(K)`.
10. **Consumer.** Reconstruct the Mellin scaling. The additional unnormalized
    factor is `1-4^-s`, which has no zero in `Re(s)>0`.
11. **Fail closed.** The exact replay proves finite operator algebra only. It
    records `QPCB67=false`, `FABP67=false`, and `RH=false` at proof-status scope.

Reject any continuation that:

- treats the inverse omitted-factor series as literal squarefree source;
- uses the PNT magnitude of the full scalar as a sign;
- replaces the corridor Möbius sum by its total variation;
- claims that leading cube/boundary cancellation supplies the sign of the
  centered remainder;
- promotes a finite parameter scan to the analytic Rankin, PNT, or sieve
  theorem.