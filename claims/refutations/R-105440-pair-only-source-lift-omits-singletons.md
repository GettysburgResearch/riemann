# R-105440 — A pair-only owner packet cannot represent the complete defect

Claim ID: `R-105440`

Status: **PROVED EXACT SOURCE-TYPE SEPARATOR**

Let

\[
E(\mathbf x)=\prod_i(1-x_i),
\qquad
S(\mathbf x)=\prod_i(1-x_i^2),
\qquad
D=E-S.
\]

The degree-one part of \(D\) is \(-\sum_i x_i\).  Any source assembled only
from unordered pairs of actual prime labels has occurrence degree at least
two, so it cannot equal \(D\) coefficient-by-coefficient.

The one-label case is decisive:

\[
m=1,
\qquad
D=(1-x_1)-(1-x_1^2)=-x_1+x_1^2\ne0,
\]

while the actual-pair set is empty.

Consequently the T-105430 implication treating the degree-two pair packet as
the complete homotopy-coherent source is not source-complete.  L-105431 remains
a correct finite Hodge identity for an actual edge packet, but its old
conclusion chain is superseded by T-105440.

A valid repair must retain the singleton layer until it has been recombined
with all higher occurrence degrees.  The radial actual-owner decomposition in
T-105440 does this coefficient-exactly.
