# M-101200 — Numbering and hyperedge integration contract

Status: **METHODOLOGY**  
Created: 2026-08-21

Use semantic role keys in addition to numeric IDs. A hyperedge is admissible only when every incoming node has:

1. a frozen source SHA;
2. the exact source type and normalization;
3. a stated physical kernel;
4. a proof that the output type matches the next input type;
5. a fail-closed RH status.

An RH-equivalent statement may be a useful target or detector. It is not counted as progress unless an independent incoming edge is proved.
