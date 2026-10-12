#!/usr/bin/env bash
# Build the Chrome Web Store upload zip: dist/copy-tab-urls-<version>.zip
# If a tag is given (e.g. v1.0.0), fail unless it matches manifest.json's version.
set -euo pipefail
cd "$(dirname "$0")/.."

version=$(jq -r .version manifest.json)
if [[ -n "${1:-}" && "$1" != "v$version" ]]; then
  echo "tag $1 does not match manifest.json version $version" >&2
  exit 1
fi

out="dist/copy-tab-urls-$version.zip"
rm -rf dist && mkdir dist
zip -X -r "$out" manifest.json popup.html popup.js icons/*.png
echo "$out"
