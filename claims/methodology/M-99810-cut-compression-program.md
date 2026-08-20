# M-99810 — Cut compression program for the weighted decorated Hasse network

Status: **RESEARCH PROGRAM; NO RH CLAIM**

The load-bearing interface after `L-99810` is not a scalar Bellman estimate but a set-valued min-cut. Any use of PR #608 must therefore begin with an exact cut-compression theorem.

For the decorated squarefree Hasse graph, order vertices by the first-owner prime filtration. Given a left set `S`, a compression move may replace one vertex by a divisor or by a first-owner predecessor only if:

1. signed left mass does not decrease;
2. positive neighbor capacity does not increase;
3. every occurrence-capacity constraint remains valid;
4. the weighted potential-drop boundary `partial_Phi S` does not increase.

If repeated compression terminates in a downward-closed first-owner set, then its boundary is encoded by one future-prime quotient profile and the mesoscopic one-prime Bellman machinery becomes a legitimate consumer.

The first hostile target is the two-prime diamond. Compression must be checked on all four vertices, all three 67 decorations, and with the explicit box potential. Any failure yields a finite separator to monotone cut compression and requires a richer state.
