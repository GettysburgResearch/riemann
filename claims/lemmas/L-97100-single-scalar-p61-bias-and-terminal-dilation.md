# L-97100 — Positive 5:3 scalar source and complete P61 bias certificate

**Status:** candidate-complete finite/directed arithmetic theorem; independent reconstruction required.  
**Inputs:** PR #556 finite-Euler annular source; PR #559 scalar dictionary.  
**RH:** not assumed.

Put

\[
\mathcal A_X=5[c_X(2)-c_{X/4}(2)]+3[c_X(3)-c_{X/4}(3)].
\]

The unsieved scalar dictionary is

\[
q_\star(2)=15,\quad q_\star(3)=6,\quad q_\star(4)=3,
\quad q_\star(m)=6\ (m\ge5),
\]

and is coefficientwise positive. Define

\[
H_x(n)=\min\!\left(\log4,\log\frac xn\right)_+,
\]

\[
A_\star(x)=\sum_{m\ge2}\frac{q_\star(m)}{\sqrt m}H_x(m).
\]

For `P=P_61`, define the complete signed scalar and unsigned mass

\[
F(x)=\sum_{d\mid P}\frac{\mu(d)}{\sqrt d}A_\star(x/d),
\qquad
M(x)=\sum_{d\mid P}\frac1{\sqrt d}A_\star(x/d).
\]

The controlling finite/directed certificate asserts

\[
0\le F(x)\le M(x)\qquad(1\le x<67),
\]

and

\[
\boxed{\frac1{40}M(x)\le F(x)\le\frac18M(x)\qquad(x\ge67).}
\]

Every `d|P_61` color is kept inside the grouped finite-Euler packet until this scalar observation is applied. The certificate is the first hostile reconstruction target; the lightweight replay checks only its exact contract and downstream rational algebra.
