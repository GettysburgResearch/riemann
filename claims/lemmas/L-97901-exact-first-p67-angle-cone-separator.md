# L-97901 — The repaired `1/42` cone first fails after one actual rough prime

Claim ID: `L-97901`  
Status: **PROVED DIRECTED FINITE SEPARATOR**  
Created: 2026-08-18  
Depends on: `L-97400`, `L-97900`  
RH status: **unproved**

Let

\[
 P=P_{61}\cdot67
\]

and use the scale-four annular kernel `A_*`. Put

\[
 F_{67}(X)=F_{P}^{A_*}(X),
 \qquad M_{67}(X)=M_{P}^{A_*}(X),
 \qquad G(X)=42F_{67}(X)-M_{67}(X).
 \tag{L-97901.1}
\]

This is the literal one-prime state:

\[
F_{67}(X)=F_{P_{61}}(X)-67^{-1/2}F_{P_{61}}(X/67),
\]

\[
M_{67}(X)=M_{P_{61}}(X)+67^{-1/2}M_{P_{61}}(X/67).
\]

No contracted coefficient or comparison reservoir occurs.

Finite divisor convolution gives integer coefficient sequences for both `F_67`
and `M_67`. Every scale-four hinge changes formula only at an integer `n` or
`4n`; hence `G` is continuous and affine in `log X` on every open unit cell.

The retained 120-digit outward Decimal interval replay proves

\[
 G(N)>0\qquad(67\le N\le160),
 \tag{L-97901.2}
\]

with the smallest lower endpoint at `N=160`,

\[
 G(160)>
 0.2262223247633235319245395376,
 \tag{L-97901.3}
\]

while

\[
 G(161)<
 -0.3757404915589003347162326413.
 \tag{L-97901.4}
\]

On the transition cell the directed signs

\[
G(160.37507)>4.3522578953\times10^{-6},
\]

\[
G(160.37508)<-1.6720398001\times10^{-6}
\]

locate the unique crossing at

\[
 \boxed{
 160.37507<X_*<160.37508.
 }
 \tag{L-97901.5}
\]

Thus the base cone `F>=M/42` loses invariance at the smallest real endpoint
`X_*` after adjoining the single genuine rough prime `67`. At the first failing
integer knot the scalar itself remains strictly positive:

\[
F_{67}(161)>9.6518966937257584.
\]

Accordingly this is a Bellman-cone separator, not a negative scalar witness and
not a counterexample to CPSL67 or RH.
