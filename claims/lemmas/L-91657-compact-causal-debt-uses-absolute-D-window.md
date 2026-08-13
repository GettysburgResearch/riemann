# L-91657 — The compact causal literal-score debt uses the absolute `D` window

Claim ID: `L-91657`  
Status: **PROVED EXACT REPAIR OF `L-91656`**  
Created: 2026-08-13  
Depends on: `L-91656`, `X-91650`  
RH status: **unproved**

Put

\[
D(u)=E(u)-(5\sqrt u-3).
\]

`L-91656` proves that `D` is increasing on `[67,infinity)` and that

\[
D(67)=1.2764007195549669\ldots>1.
\]

Let `p>=67`, `r=p^{-1/2}`, `u>=p`, and `v=u/p>=1`. The declared-minus-literal score of the causal datum is

\[
-D(u)+rD(v).
\]

If `v>=67`, then `D(u)>=D(v)>0`, so

\[
-D(u)+rD(v)\le-(1-r)D(v)\le0.
\]

If `1<=v<67`, then `u>=67` and `D(u)>0`; hence

\[
[-D(u)+rD(v)]_+
\le r[D(v)]_+
\le\frac1{\sqrt{67}}
 \max_{1\le w\le67}|D(w)|.
\]

Therefore the valid compact constant is

\[
\boxed{
C_{\rm cau}
=\frac1{\sqrt{67}}
 \max_{1\le w\le67}|D(w)|<\infty.
}
\]

The earlier expression using only `[-D(v)]_+` had the wrong sign side. It is superseded by this lemma.
