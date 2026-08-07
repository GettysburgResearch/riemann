#!/usr/bin/env bash
set -euo pipefail

here="$(cd "$(dirname "$0")" && pwd)"
cd "$here"

cat patch/part* > riemann-singular-seam-producer.patch
cat bundle/part* | base64 --decode > riemann-singular-seam-producer.tar.gz
sha256sum --check riemann-singular-seam-producer.SHA256SUMS
