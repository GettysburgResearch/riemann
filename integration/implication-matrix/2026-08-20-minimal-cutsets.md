# Minimal open cut sets

After contracting `IM-M04 <-> IM-M05` and the phase-Hasse realization into the
minimal-wavelet node, the frozen graph has two structural middle classes.

## CV class

```text
IM-M01 critical variation
  -> IM-M02 activation envelope
  -> beta Mellin-Landau
  -> RH
```

The completion/collar hyperedge reaches `IM-M01`.

## XD class

```text
IM-M04 rough largest-prime
  <-> IM-M05 balanced Vaughan
  -> minimal-wavelet Mellin/Littlewood
  -> RH
```

Signed phase-Hasse packing is a realization of this class.

## Cut computation

To block every currently advertised closure route one must cut both classes:

```text
{CV, XD}.
```

To close the programme it is enough to prove either class.  The shortest
source-faithful open representatives are:

```text
CV: oriented depth-one large-prime collar variation after finite squaring;
XD: balanced/rough signed cross-core dispersion for the compact wavelet.
```

The graph contains no verified-only path to RH.
