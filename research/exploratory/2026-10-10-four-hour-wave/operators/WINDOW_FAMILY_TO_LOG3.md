# A uniform ten-dimensional positive-sector family through the next prime cusp

Date: 2026-10-10. Conditional on the inherited source/domain hypotheses O1--O4
and the independently reviewed directed phase line in
`CODIMENSION_8_PHASE_REFINEMENT.md`, the positive-complement construction can
be carried uniformly to \(L=\log3\). This does not prove effective positivity
or join finite Schur certificates across intervals.

For every \(0<L\le\log3\), define

\[
E_L=\operatorname{span}\{e^{t/2},e^{-t/2},\cosh(3t/2),
 \sin(j\pi t/L):1\le j\le7\}\subset L^2(0,L),\qquad V_L=E_L^\perp.
\]

The source has the exact tail

\[
q_L(h,h)=q_{L,2}(h,h)
 -\tau_2|\langle\cosh(bt),h\rangle|^2
 +\tau_2|\langle\sinh(bt),h\rangle|^2,\quad b=3/2,
\]

where \(\tau_2=\sum_{n\ge3}\Lambda(n)/n^2\). Indeed, for every
\(|t-u|\le L\le\log3\le\log n\),
\(e^{-b|x-\log n|}+e^{-b|x+\log n|}=2n^{-b}\cosh(bx)\).
The equality remains valid at \(L=\log3\), including the corner
\(x=\log3\); that corner has no additional integral contribution.

The cutoff-X2 Fourier symbol \(V_2\), and its already verified global line

\[
\frac{(x+1/4)^2}{x+9/4}V_2(\sqrt x)\ge\frac45x-244\quad(x\ge0),
\]

are independent of the window length. Extend the clamped primitive by zero
outside \([0,L]\), as in the inherited audit. The first seven sine moment
conditions transfer exactly to its primitive \(\phi\); hence

\[
\|\phi\|_2^2\le\frac{L^2}{64\pi^2}\|\phi'\|_2^2.
\]

The source Fourier identity and the zero cosh moment therefore give

\[
q_L(h,h)\ge
\frac32\left(\frac45-\frac{244L^2}{64\pi^2}\right)\|\phi_h'\|_2^2
+\tau_2|\langle\sinh(bt),h\rangle|^2
\ge\frac12\|\phi_h'\|_2^2.
\tag{1}
\]

The exact log series proves \(\log3<1.0987\), and Machin's formula proves
\(\pi>3.1415\). Their rational substitution gives the uniform gap

\[
\frac32\left(\frac45-\frac{244}{64}
 \left(\frac{1.0987}{3.1415}\right)^2\right)
=\frac{259120533}{517719200}>\frac12.
\]

Every member has an exact ten-dimensional complement, by linear
independence of the seven sine and three real exponential functions. For
exact trials in \(V_L\), define the audited projected residual using the
projection off \(1,\cos(j\pi t/L)\ (1\le j\le7),\sinh(bt)\). Equation(1)
yields the uniform energy residual enclosure

\[
U_L-\frac92 R_L\preceq S_L\preceq U_L.
\tag{2}
\]

No sign for the ten-dimensional effective matrix follows from (1). This
family identifies a range where the infinite-dimensional coercivity sector
and the source-tail rank remain controlled by fixed small dimensions; the
remaining task is a directed, length-dependent effective sign certificate.
At larger lengths, the prime3 cusp enters, and the tail identity must be
updated rather than extrapolated.

Replay `check_window_family_log3.py` under normal Python and `python -O`, with
python-flint0.8.0 available. It replays the complete directed phase coverage
and the exact rational scaling. The stored certificate records all accepted
bounds and source hashes.
