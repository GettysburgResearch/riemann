# X-23801 mutation plan

The verifier must reject:

1. a negative profile curvature;
2. a residual below zero;
3. a changed claimed packing coefficient;
4. a missing Möbius multiple;
5. a nonzero terminal profile value;
6. a false packing-mass telescope;
7. a false coefficient-mass telescope.

These are checker requirements for future executable unit tests. The retained
synthetic replay exercises the valid path only.
