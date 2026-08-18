# Remote artifacts for T-97701 / C4MBI67 publication recovery

The artifact IDs below are fresh and are not the old T-97700 Drive objects.
The deterministic ZIP intentionally excludes the outer artifact checksum file
to avoid a self-referential archive hash.

| Artifact | Drive file ID | URL |
|---|---|---|
| Fresh T-97701 ZIP | `1KlzzQ78VcKTuYNcVc18Xewxrh552Au2x` | https://drive.google.com/file/d/1KlzzQ78VcKTuYNcVc18Xewxrh552Au2x/view?usp=drivesdk |
| C4MBI67 PDF | `1dC1-zwh7YwoLJuu2-3H07o95jJO9QgI3` | https://drive.google.com/file/d/1dC1-zwh7YwoLJuu2-3H07o95jJO9QgI3/view?usp=drivesdk |
| Complete TeX | `1IJ4qldWN__716vj8NSsfhOSkECUy6tbp` | https://drive.google.com/file/d/1IJ4qldWN__716vj8NSsfhOSkECUy6tbp/view?usp=drivesdk |
| Content ledger | `129_atHkjguWoJaMScKkeDq3TSyvywZe9` | https://drive.google.com/file/d/129_atHkjguWoJaMScKkeDq3TSyvywZe9/view?usp=drivesdk |
| Outer artifact ledger | `12_OFjLdZrVhdmLnSDzIDSC4fuIB4wVF7` | https://drive.google.com/file/d/12_OFjLdZrVhdmLnSDzIDSC4fuIB4wVF7/view?usp=drivesdk |

The final publication process replaces the provisional bytes at these same IDs,
downloads each object back, and compares its SHA-256 and byte count with the
local final artifact.  The resulting readback record is not treated as a
mathematical proof object.
