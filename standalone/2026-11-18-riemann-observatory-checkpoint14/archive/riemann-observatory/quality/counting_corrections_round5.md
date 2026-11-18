# Selected versus catalogued records

The round-five merge found that the aggregate builder had overwritten an explicit selected=false flag for PAPER-D202, a deferred bibliographic record whose full text was inaccessible. That work remains catalogued for provenance but is now excluded from selected-work counts. The bibliography and access manifest expose selection_status, and validation checks the selected subset separately.

The second uploaded checkpoint's67 catalogued work records therefore contained66 selected works and one deferred supporting record. Its26 full substantive readings and source/audit scopes are unaffected. The immutable checkpoint metrics retain the original reported value; this correction supplies its proper interpretation. Subsequent live/packaged counts use the corrected rule. No source-reading or mathematical-audit promotion resulted from this fix.

Littlewood's degraded reproduced original with missing formula displays is separately counted as primary excerpts rather than complete full-text access. Metadata, partial access, complete access and full reading remain distinct.
