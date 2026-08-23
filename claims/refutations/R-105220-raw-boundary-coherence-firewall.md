# R-105220 — Raw safe-line coherence is not the real critical-residue coherence

Claim ID: `R-105220`  
Status: **PROPOSED EXACT RATIONAL FIREWALL; independently replayable**  
Created: 2026-08-23  
Depends on: `L-105220--L-105222`  
RH status: **not assumed**

Take

\[
p(x)=x^4-5x^2+2
\]

and centre the positive localizer at `a=0`. The critical points are

\[
0,\qquad \pm\sqrt{5/2},
\]

with residues

\[
-\frac15,\qquad-\frac{17}{80},\qquad-\frac{17}{80}.
\]

The exact real weighted moments are

\[
N=\frac{2669}{2093},
\qquad
A=\frac{541}{2093},
\qquad
B=\frac{10973}{209300}.
\tag{R-105220.1}
\]

The two zeros of `p''` contribute the adjacent-derivative debt

\[
\boxed{
D_2=-\frac{25281}{1882100}.
}
\tag{R-105220.2}
\]

Thus the raw second boundary carrier is

\[
\mathcal B=B+D_2
=
\frac{1536097}{39392353}.
\tag{R-105220.3}
\]

The actual real coherence is

\[
\boxed{
\frac{A^2}{NB}
=
\frac{29268100}{29286937}<1,
}
\tag{R-105220.4}
\]

whereas the raw boundary quotient is

\[
\boxed{
\frac{A^2}{N\mathcal B}
=
\frac{5508549101}{4099842893}>1.
}
\tag{R-105220.5}
\]

A quotient larger than one cannot be a positive-weight real coherence.
Therefore the zero-free-axis asymptotic of the uncorrected boundary carriers
may not be promoted directly to a real-critical moment theorem.

The example has only real critical points; the discrepancy is entirely the
adjacent-derivative debt. With nonreal critical points present, the three
additional corrections in `L-105222` are equally load bearing.

This firewall does not refute the moving-centre program. It proves that its
conclusion-bearing theorem is the signed combined correction estimate, not the
formal safe-line ratio alone.
