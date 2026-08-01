#!/usr/bin/env python3
"""Capture a reproducible GitHub PR inventory for a repository integration cutoff.

This script is intentionally standard-library only. It reads repository metadata
through the GitHub REST API, reconstructs the PR head reachable at a declared
cutoff from the PR commit list, records later deltas separately, and exports likely
pre-public review evidence without executing any mathematical workload.
"""

from __future__ import annotations

import base64
import datetime as dt
import hashlib
import json
import os
import pathlib
import re
import time
import urllib.error
import urllib.parse
import urllib.request
from typing import Any

API = "https://api.github.com"
REPO = os.environ.get("GITHUB_REPOSITORY", "gfreund123/riemann")
TOKEN = os.environ["GITHUB_TOKEN"]
CUTOFF_TEXT = os.environ.get("SNAPSHOT_CUTOFF", "2026-08-01T21:35:52Z")
OUT = pathlib.Path(os.environ.get("SNAPSHOT_OUTPUT", "snapshot-output"))
CUTOFF = dt.datetime.fromisoformat(CUTOFF_TEXT.replace("Z", "+00:00"))

STATUS_TERMS = (
    "VERIFIED",
    "VERIFIED WITH FIXES",
    "VERIFIED_WITH_FIXES",
    "GAP/BLOCKED",
    "REJECTED",
    "PRE-PUBLIC",
    "pre-public",
    "frozen head",
    "frozen-head",
)
REVIEW_PATH_RE = re.compile(
    r"(?:^|/)(?:reviews?|reports?)(?:/|$)|pre[-_ ]?public|frozen[-_ ]?head|audit",
    re.IGNORECASE,
)


def parse_time(value: str | None) -> dt.datetime | None:
    if not value:
        return None
    return dt.datetime.fromisoformat(value.replace("Z", "+00:00"))


def request_json(path_or_url: str, *, attempts: int = 5) -> Any:
    url = path_or_url if path_or_url.startswith("http") else f"{API}{path_or_url}"
    req = urllib.request.Request(
        url,
        headers={
            "Authorization": f"Bearer {TOKEN}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "riemann-integration-snapshot",
        },
    )
    for attempt in range(attempts):
        try:
            with urllib.request.urlopen(req, timeout=60) as response:
                return json.load(response)
        except urllib.error.HTTPError as exc:
            if exc.code == 404:
                raise
            retryable = exc.code in {403, 408, 409, 429, 500, 502, 503, 504}
            if not retryable or attempt + 1 == attempts:
                detail = exc.read().decode("utf-8", errors="replace")
                raise RuntimeError(f"GitHub API {exc.code} for {url}: {detail}") from exc
            time.sleep(min(2 ** attempt, 16))
        except (urllib.error.URLError, TimeoutError) as exc:
            if attempt + 1 == attempts:
                raise RuntimeError(f"GitHub API transport failure for {url}: {exc}") from exc
            time.sleep(min(2 ** attempt, 16))
    raise AssertionError("unreachable")


def paged(path: str, *, per_page: int = 100) -> list[Any]:
    items: list[Any] = []
    page = 1
    separator = "&" if "?" in path else "?"
    while True:
        batch = request_json(f"{path}{separator}per_page={per_page}&page={page}")
        if not isinstance(batch, list):
            raise TypeError(f"expected list from {path}, got {type(batch).__name__}")
        items.extend(batch)
        if len(batch) < per_page:
            return items
        page += 1


def minimal_user(value: Any) -> str | None:
    return value.get("login") if isinstance(value, dict) else None


def pr_snapshot(pr: dict[str, Any]) -> dict[str, Any]:
    number = int(pr["number"])
    commits = paged(f"/repos/{REPO}/pulls/{number}/commits")
    commits_compact: list[dict[str, Any]] = []
    cutoff_candidates: list[tuple[dt.datetime, int, str]] = []
    for index, commit in enumerate(commits):
        nested = commit.get("commit") or {}
        committed_at_text = ((nested.get("committer") or {}).get("date"))
        authored_at_text = ((nested.get("author") or {}).get("date"))
        committed_at = parse_time(committed_at_text) or parse_time(authored_at_text)
        compact = {
            "sha": commit.get("sha"),
            "authored_at": authored_at_text,
            "committed_at": committed_at_text,
            "parents": [p.get("sha") for p in commit.get("parents", [])],
        }
        commits_compact.append(compact)
        if committed_at is not None and committed_at <= CUTOFF:
            cutoff_candidates.append((committed_at, index, str(commit.get("sha"))))

    cutoff_head = max(
        cutoff_candidates,
        default=(None, -1, None),
        key=lambda x: (
            x[0] or dt.datetime.min.replace(tzinfo=dt.timezone.utc),
            x[1],
        ),
    )[2]
    current_head = (pr.get("head") or {}).get("sha")
    post_cutoff_commits = []
    for item in commits_compact:
        timestamp = parse_time(item.get("committed_at")) or parse_time(item.get("authored_at"))
        if timestamp is not None and timestamp > CUTOFF:
            post_cutoff_commits.append(item)

    files = paged(f"/repos/{REPO}/pulls/{number}/files")
    compact_files = [
        {
            "filename": f.get("filename"),
            "status": f.get("status"),
            "sha": f.get("sha"),
            "additions": f.get("additions"),
            "deletions": f.get("deletions"),
            "changes": f.get("changes"),
        }
        for f in files
    ]

    issue_comments = paged(f"/repos/{REPO}/issues/{number}/comments")
    reviews = paged(f"/repos/{REPO}/pulls/{number}/reviews")
    evidence_comments: list[dict[str, Any]] = []
    for kind, entries, timestamp_key in (
        ("issue_comment", issue_comments, "created_at"),
        ("pull_request_review", reviews, "submitted_at"),
    ):
        for entry in entries:
            body = entry.get("body") or ""
            if any(term in body for term in STATUS_TERMS):
                created_at = parse_time(entry.get(timestamp_key))
                evidence_comments.append(
                    {
                        "kind": kind,
                        "id": entry.get("id"),
                        "user": minimal_user(entry.get("user")),
                        "created_at": entry.get(timestamp_key),
                        "state": entry.get("state"),
                        "commit_id": entry.get("commit_id"),
                        "body": body,
                        "at_or_before_cutoff": bool(created_at and created_at <= CUTOFF),
                    }
                )

    review_files: list[dict[str, Any]] = []
    preferred_ref = cutoff_head or current_head
    for file_item in compact_files:
        path = str(file_item.get("filename") or "")
        if not REVIEW_PATH_RE.search(path) or not path.lower().endswith((".md", ".yaml", ".yml", ".json")):
            continue
        encoded_path = urllib.parse.quote(path, safe="/")
        content = None
        digest = None
        ref_used = None
        errors: list[str] = []
        attempted_refs: set[str] = set()
        for ref in (preferred_ref, current_head):
            if not ref or str(ref) in attempted_refs:
                continue
            attempted_refs.add(str(ref))
            try:
                payload = request_json(
                    f"/repos/{REPO}/contents/{encoded_path}?ref="
                    f"{urllib.parse.quote(str(ref), safe='')}"
                )
                if payload.get("encoding") == "base64" and payload.get("content"):
                    raw = base64.b64decode(payload["content"])
                    if len(raw) <= 2_000_000:
                        content = raw.decode("utf-8", errors="replace")
                        ref_used = ref
                        digest = hashlib.sha256(raw).hexdigest()
                    else:
                        errors.append(f"file too large: {len(raw)} bytes")
                    break
            except urllib.error.HTTPError as exc:
                errors.append(f"{ref}: HTTP {exc.code}")
            except Exception as exc:  # preserve inventory even if one candidate is inaccessible
                errors.append(f"{ref}: {type(exc).__name__}: {exc}")
        review_files.append(
            {
                "path": path,
                "ref": ref_used,
                "sha256": digest,
                "content": content,
                "errors": errors,
            }
        )

    return {
        "number": number,
        "title": pr.get("title"),
        "html_url": pr.get("html_url"),
        "state_at_capture": pr.get("state"),
        "draft": pr.get("draft"),
        "created_at": pr.get("created_at"),
        "updated_at": pr.get("updated_at"),
        "closed_at": pr.get("closed_at"),
        "merged_at": pr.get("merged_at"),
        "author": minimal_user(pr.get("user")),
        "base_ref": (pr.get("base") or {}).get("ref"),
        "base_sha": (pr.get("base") or {}).get("sha"),
        "head_ref": (pr.get("head") or {}).get("ref"),
        "head_repo": ((pr.get("head") or {}).get("repo") or {}).get("full_name"),
        "current_head_at_capture": current_head,
        "cutoff_head_reconstructed": cutoff_head,
        "cutoff_reconstruction_method": (
            "latest PR-list commit whose committer (fallback author) timestamp is <= "
            "cutoff; push time is not exposed by this endpoint"
        ),
        "current_equals_cutoff": bool(cutoff_head and current_head == cutoff_head),
        "post_cutoff_commits": post_cutoff_commits,
        "commit_count": len(commits_compact),
        "commits": commits_compact,
        "changed_files": compact_files,
        "review_evidence_comments": evidence_comments,
        "review_evidence_files": review_files,
    }


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    all_prs = paged(f"/repos/{REPO}/pulls?state=all&sort=created&direction=asc")
    open_at_cutoff: list[dict[str, Any]] = []
    post_cutoff_open: list[dict[str, Any]] = []
    for pr in all_prs:
        created = parse_time(pr.get("created_at"))
        closed = parse_time(pr.get("closed_at"))
        was_open = created is not None and created <= CUTOFF and (closed is None or closed > CUTOFF)
        if was_open:
            open_at_cutoff.append(pr)
        elif created is not None and created > CUTOFF and pr.get("state") == "open":
            post_cutoff_open.append(pr)

    snapshots: list[dict[str, Any]] = []
    total = len(open_at_cutoff)
    for index, pr in enumerate(sorted(open_at_cutoff, key=lambda p: int(p["number"])), start=1):
        print(f"[{index}/{total}] PR #{pr['number']}", flush=True)
        snapshots.append(pr_snapshot(pr))

    capture_time = dt.datetime.now(dt.timezone.utc).replace(microsecond=0)
    output = {
        "schema_version": 1,
        "repository": REPO,
        "cutoff": CUTOFF_TEXT,
        "captured_at": capture_time.isoformat().replace("+00:00", "Z"),
        "open_pr_count_at_cutoff": len(snapshots),
        "open_pr_numbers_at_cutoff": [p["number"] for p in snapshots],
        "post_cutoff_open_prs": [
            {
                "number": p.get("number"),
                "title": p.get("title"),
                "created_at": p.get("created_at"),
                "head_sha": (p.get("head") or {}).get("sha"),
            }
            for p in sorted(post_cutoff_open, key=lambda p: int(p["number"]))
        ],
        "pull_requests": snapshots,
    }
    payload = json.dumps(output, indent=2, sort_keys=False, ensure_ascii=False) + "\n"
    (OUT / "open-pr-snapshot.json").write_text(payload, encoding="utf-8")
    digest = hashlib.sha256(payload.encode("utf-8")).hexdigest()
    (OUT / "SHA256SUMS").write_text(
        f"{digest}  open-pr-snapshot.json\n", encoding="utf-8"
    )
    (OUT / "README.txt").write_text(
        "Read-only integration snapshot. No mathematical computations were run.\n"
        f"Repository: {REPO}\nCutoff: {CUTOFF_TEXT}\nCaptured: {output['captured_at']}\n"
        f"Open PRs at cutoff: {len(snapshots)}\n",
        encoding="utf-8",
    )
    print(f"captured {len(snapshots)} PRs; sha256={digest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
