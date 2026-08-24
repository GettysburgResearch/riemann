# R-104520 — The unit-phase lower bound is the parent real-zero count

Claim ID: `R-104520`  
Status: **BINDING SCOPE CORRECTION**  
Created: 2026-08-24  
RH status: **unproved**

Let `f` be real analytic on a regular compact interval `[a,b]`, with simple
critical points, no common zero of `f` and `f'`, and nonzero boundary data.

Write

```text
G = number of Rolle-generating critical points;
W = number of wrong critical points.
```

The exact reverse-Rolle identity of `L-104500` is

\[
N_{\mathbb R}(f;(a,b))
=
G-W+1-B_--B_+,
\tag{R-104520.1}
\]

where the two boundary bits belong to `{0,1}`.

For every `lambda>0`, `L-104542` gives

\[
G-W
=
\frac1\pi\Delta_{[a,b]}
\arg(f-i\lambda f')
+O(1),
\tag{R-104520.2}
\]

with an absolute endpoint error.

Combining the two formulas,

\[
\boxed{
\frac1\pi\Delta\arg(f-i\lambda f')
=
N_{\mathbb R}(f;(a,b))+O(1).
}
\tag{R-104520.3}
\]

Consequently an asymptotic theorem of the form

```text
Delta arg(f-i lambda f') >= eta * number_of_critical_points
```

is, up to bounded boundary terms, already a lower bound for the parent real-zero
count. It is a useful Levinson coordinate and detector, but not an independent
producer of the missing parent zeros.

For `f=Xi''`, `UPHASE104590` must therefore not be counted as new arithmetic or
source-side closure. The controlling successors are `EXCUR104600` and
`PVAR104600`, whose hypotheses involve respectively:

```text
unsigned excursion geometry of Xi'';
a source-visible p-variation / critical-moment estimate.
```

These inputs do not assume or count real zeros of `Xi''`.

```text
T104590 unit phase identity        RETAINED EXACT
UPHASE104590 as producer           WITHDRAWN
UPHASE104590 as detector           RETAINED
T104600 source-side replacements   CONTROLLING
RH                                 UNPROVED
```
