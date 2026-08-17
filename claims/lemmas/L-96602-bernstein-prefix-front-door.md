# L-96602 — Scalar positivity is exactly a one-dimensional Bernstein prefix problem

Claim ID: `L-96602`  
Status: **PROVED EXACT LAPLACE / BERNSTEIN EQUIVALENCE**  
Created: 2026-08-17  
Depends on: `L-96600`; PR #551 fixed-row Mellin transform  
RH status: **not assumed**

Put `z=s+1/2` and

\[
A(s)=6-{3(1-2^{-z})(2-2^{-z})\over\zeta(z)}.
\]

For `r(t)=\mathcal R_{e^t}` and the right-continuous prefix shadow `m(t)=M_*(\lfloor e^t\rfloor)`,

\[
\boxed{
\int_0^\infty r(t)e^{-st}\,dt={A(s)\over s^2},
\qquad
\int_0^\infty m(t)e^{-st}\,dt={A(s)\over s}.
}
\tag{L-96602.1}
\]

By Bernstein's theorem and uniqueness of the Laplace transform,

\[
\boxed{
 m(t)\ge0\ \text{a.e.}
 \iff {A(s)\over s}\ \text{is completely monotone on }(0,\infty),
}
\tag{L-96602.2}
\]

and

\[
\boxed{
 r(t)\ge0\ \text{a.e.}
 \iff {A(s)\over s^2}\ \text{is completely monotone on }(0,\infty).
}
\tag{L-96602.3}
\]

The prefix theorem is stronger and feeds the scalar theorem by one positive integration. This gives a single real-variable target with no source ownership ambiguity. It is still RH-bearing and is not asserted here.
