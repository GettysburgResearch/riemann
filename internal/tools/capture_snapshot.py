#!/usr/bin/env python3
"""Capture a read-only GitHub PR inventory around an integration cutoff.

The present head returned by GitHub is exact at capture time. The historical
"head candidate" below is only a heuristic selected from commit author/committer
timestamps. It is not an exact record of the PR head visible at the cutoff:
push time and force-push history are not provided by the PR commit endpoint.

Exact frozen review heads must come from independently recorded review reports.
No mathematical workload is executed.
"""

from __future__ import annotations

import datetime as dt
import hashlib
import json
import os
import pathlib
import time
import urllib.error
import urllib.request
from typing import Any

API = "https://api.github.com"
REPO = os.environ.get("GITHUB_REPOSITORY", "gfreund123/riemann")
TOKEN = os.environ["GITHUB_TOKEN"]
CUTOFF_TEXT = os.environ.get("SNAPSHOT_CUTOFF", "2026-08-01T21:35:52Z")
OUT = pathlib.Path(os.environ.get("SNAPSHOT_OUTPUT", "snapshot-output"))
CUTOFF = dt.datetime.fromisoformat(CUTOFF_TEXT.replace("Z", "+00:00"))


def parse_time(value: str | None) -> dt.datetime | None:
    if not value:
        return None
    return dt.datetime.fromisoformat(value.replace("Z", "+00:00"))


def request_json(path: str, attempts: int = 5) -> Any:
    url = path if path.startswith("http") else f"{API}{path}"
    request = urllib.request.Request(
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
            with urllib.request.urlopen(request, timeout=60) as response:
                return json.load(response)
        except urllib.error.HTTPError as exc:
            retryable = exc.code in {403, 408, 409, 429, 500, 502, 503, 504}
            if not retryable or attempt + 1 == attempts:
                detail = exc.read().decode("utf-8", errors="replace")
                raise RuntimeError(f"GitHub API {exc.code} for {url}: {detail}") from exc
        except (urllib.error.URLError, TimeoutError) as exc:
            if attempt + 1 == attempts:
                raise RuntimeError(f"GitHub API transport failure for {url}: {exc}") from exc
        time.sleep(min(2**attempt, 16))
    raise AssertionError("unreachable")


def paged(path: str, per_page: int = 100) -> list[Any]:
    items: list[Any] = []
    page = 1
    separator = "&" if "?" in path else "?"
    while True:
        batch = request_json(f"{path}{separator}per_page={per_page}&page={page}")
        if not isinstance(batch, list):
            raise TypeError(f"expected list from {path}")
        items.extend(batch)
        if len(batch) < per_page:
            return items
        page += 1


def historical_candidate(commits: list[dict[str, Any]]) -> tuple[str | None, str]:
    candidates: list[tuple[dt.datetime, int, str]] = []
    for index, commit in enumerate(commits):
        nested = commit.get("commit") or {}
        committed = parse_time(((nested.get("committer") or {}).get("date")))
        authored = parse_time(((nested.get("author") or {}).get("date")))
        timestamp = committed or authored
        if timestamp and timestamp <= CUTOFF and commit.get("sha"):
            candidates.append((timestamp, index, str(commit["sha"])))
    if not candidates:
        return None, "no commit timestamp candidate at or before cutoff"
    candidate = max(candidates, key=lambda item: (item[0], item[1]))[2]
    method = (
        "heuristic only: latest PR-list commit with committer timestamp "
        "(fallback author timestamp) at or before cutoff; not push time, "
        "not force-push history, and not an exact historical PR-head record"
    )
    return candidate, method


def compact_pr(pr: dict[str, Any]) -> dict[str, Any]:
    number = int(pr["number"])
    commits = paged(f"/repos/{REPO}/pulls/{number}/commits")
    candidate, method = historical_candidate(commits)
    present_head = (pr.get("head") or {}).get("sha")
    post_cutoff: list[dict[str, Any]] = []
    for commit in commits:
        nested = commit.get("commit") or {}
        committed_text = ((nested.get("committer") or {}).get("date"))
        authored_text = ((nested.get("author") or {}).get("date"))
        timestamp = parse_time(committed_text) or parse_time(authored_text)
        if timestamp and timestamp > CUTOFF:
            post_cutoff.append(
                {
                    "sha": commit.get("sha"),
                    "committed_at": committed_text,
                    "authored_at": authored_text,
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
        "base_ref": (pr.get("base") or {}).get("ref"),
        "base_sha_at_capture": (pr.get("base") or {}).get("sha"),
        "head_ref": (pr.get("head") or {}).get("ref"),
        "present_head_at_capture": present_head,
        "historical_head_candidate": candidate,
        "historical_head_candidate_confidence": "RECONSTRUCTED_UNCERTAIN",
        "historical_head_candidate_method": method,
        "candidate_equals_present": bool(candidate and candidate == present_head),
        "post_cutoff_commit_metadata": post_cutoff,
        "commit_count_visible_at_capture": len(commits),
    }


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    prs = paged(f"/repos/{REPO}/pulls?state=all&sort=created&direction=asc")
    cutoff_open: list[dict[str, Any]] = []
    post_cutoff_open: list[dict[str, Any]] = []
    for pr in prs:
        created = parse_time(pr.get("created_at"))
        closed = parse_time(pr.get("closed_at"))
        if created and created <= CUTOFF and (closed is None or closed > CUTOFF):
            cutoff_open.append(pr)
        elif created and created > CUTOFF and pr.get("state") == "open":
            post_cutoff_open.append(pr)

    snapshots: list[dict[str, Any]] = []
    for index, pr in enumerate(sorted(cutoff_open, key=lambda item: int(item["number"])), 1):
        print(f"[{index}/{len(cutoff_open)}] PR #{pr['number']}", flush=True)
        snapshots.append(compact_pr(pr))

    captured = dt.datetime.now(dt.timezone.utc).replace(microsecond=0)
    result = {
        "schema": "riemann.integration.supporting-snapshot.v2",
        "repository": REPO,
        "cutoff": CUTOFF_TEXT,
        "captured_at": captured.isoformat().replace("+00:00", "Z"),
        "authority_warning": (
            "historical_head_candidate is reconstructed from commit timestamps and "
            "must not replace an independently review-recorded frozen head"
        ),
        "open_pr_count_at_cutoff_by_lifecycle_timestamps": len(snapshots),
        "open_pr_numbers_at_cutoff_by_lifecycle_timestamps": [item["number"] for item in snapshots],
        "post_cutoff_open_prs_at_capture": [
            {
                "number": pr.get("number"),
                "title": pr.get("title"),
                "created_at": pr.get("created_at"),
                "present_head_at_capture": (pr.get("head") or {}).get("sha"),
            }
            for pr in sorted(post_cutoff_open, key=lambda item: int(item["number"]))
        ],
        "pull_requests": snapshots,
    }
    payload = json.dumps(result, indent=2, ensure_ascii=False) + "\n"
    data_path = OUT / "supporting-pr-snapshot.json"
    data_path.write_text(payload, encoding="utf-8")
    digest = hashlib.sha256(payload.encode("utf-8")).hexdigest()
    (OUT / "SHA256SUMS").write_text(f"{digest}  {data_path.name}\n", encoding="utf-8")
    (OUT / "README.txt").write_text(
        "Supporting read-only metadata snapshot; not the authoritative cutoff ledger.\n"
        "Historical head candidates are heuristic, not exact.\n"
        "The Actions artifact has temporary retention and is not immutable storage.\n"
        f"Repository: {REPO}\nCutoff: {CUTOFF_TEXT}\nCaptured: {result['captured_at']}\n",
        encoding="utf-8",
    )
    print(f"captured {len(snapshots)} lifecycle-open PRs; sha256={digest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
