# R-105115 - A non-strict total-radius gate is insufficient

Claim ID: R-105115

Status: **EXACT REFUTATION**

Created: 2026-08-23

RH status: **unproved**

## Refuted statement

> If a finite family of closed disks has total radius \(S\) and
> \(\Delta_T\ge2S\), then some admissible vertical supporting-line pair is
> disjoint from every disk.

## Counterexample

Take \(I_T=(1,3)\), so \(\Delta_T=2\), and the single closed disk

\[
D=\overline D(2,1).
\]

Here \(S=1\) and \(\Delta_T=2S\).  For every \(T\in(1,3)\),

\[
|T-2|<1,
\]

so the right supporting line \(\Re z=T\) meets \(D\).  The certified safe
set \(G_T\) is empty.  The same construction with a disk centered on the
imaginary axis refutes the horizontal version.

Thus the total-radius sufficient gate must be strict.  This example proves
coordinatewise worst-case sharpness only; exact merged projections can be
much smaller than \(2S\) for a particular configuration.
