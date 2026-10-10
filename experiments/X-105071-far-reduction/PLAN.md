# PLAN — [P2-FAR] assault (T-105070)
1. Read T-105070 §1,§2; P2_transfer_theorem.md (P2.6, P2.7 Rem iii, P2.8b); P2_NOTES.md; P4_mechanism_verdict.md; L-105058 §5.
2. Route R1: corner field = divisor-correlation Dirichlet polynomial. Bound WINDOW mass via
   Hooley-Tenenbaum Delta^2 + Montgomery-Vaughan MV theorem on window-localized L2.
   Target: eps_1 < 1 in P2.7 Rem(iii) form (b).
3. Numerics: far_num1.py reproduce 77%/3.5%; far_num2.py window-ratio h-scaling (3 widths);
   far_num3.py Delta^2 constant test.
4. Route R2 (timeboxed): L2 multiplier through D_half; verdict.
5. Write FAR.md, R2_VERDICT.md, FAILURES.md incrementally (<=150 lines/append).
