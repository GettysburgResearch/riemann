# T-91720 claim-ID collision and supersession record

Cutoff: `2026-08-14T19:56:18Z`

The first connector publication onto PR #468 used temporary paths in the
`91685--91687` range. While those writes were in progress, new live descendants
appeared:

```text
PR #469  uses L/O-91685
PR #470  uses L-91686/L-91687 and supplies the native-capacity separator
PR #471  extends the SONTR genealogy
PR #473  uses L-91690--L-91692 and T-91660/T-91661
PR #475  uses L-91686--L-91689 on a separate stacked branch
```

To avoid semantic claim-ID collision, this packet is renumbered exactly as:

```text
L-91685 -> L-91720
R-91685 -> R-91720
L-91686 -> L-91721
L-91687 -> L-91722
O-91685 -> O-91720
T-91685 -> T-91720
X-91685 -> X-91720
```

The old temporary paths are deleted. Their mathematics is neither promoted nor
withdrawn; the `91720+` files are the sole normative version. Later corrections
and independent reviews control.
