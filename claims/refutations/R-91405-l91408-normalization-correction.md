# R-91405 — Normalization correction for L-91408

Status: **L-91408 SUPERSEDED; RH UNPROVEN**

The first version of `L-91408` mixed two equivalent normalizations. In coefficient-measure coordinates, multiplication of the arithmetic source produces the square-root scale inside the kernel. In the positive paired-source coordinates used by `L-91404`, that same scale is already the explicit child coefficient. Applying both factors gives the wrong child coefficient.

Do not cite `L-91408`.

The corrected statement is `L-91409`: in weighted paired-source coordinates, the explicit child coefficient is applied exactly once and the component-row coordinate is unchanged.
