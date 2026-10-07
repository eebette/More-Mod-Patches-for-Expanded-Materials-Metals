#!/usr/bin/env bash
# Stage a CLEAN Steam Workshop upload folder - only what RimWorld loads, plus the license.
#
# Why: RimWorld's in-game uploader ships the ENTIRE mod folder (SteamUGC.SetItemContent over the
# mod dir, no filtering). Uploading the repo directly would publish tools/, Media/, README.md and
# .git/ to the Workshop. Upload from the folder this stages, never from the repo.
#
# Allowlist, not blocklist: only RimWorld-recognized content + LICENSE are copied.
set -euo pipefail
REPO="$(cd "$(dirname "$0")" && pwd)"
DEST="${1:-$REPO/../.publish/$(basename "$REPO")}"

rm -rf "$DEST"
mkdir -p "$DEST"
for item in About LoadFolders.xml ModPatches Patches Defs Languages LICENSE; do
    [ -e "$REPO/$item" ] && cp -r "$REPO/$item" "$DEST/"
done
# Carry the Workshop item link if this mod is already published, so upload updates it.
[ -f "$REPO/About/PublishedFileId.txt" ] && cp "$REPO/About/PublishedFileId.txt" "$DEST/About/"

echo "Clean upload staged at: $DEST"
echo "Shipping files:"
find "$DEST" -type f | sed "s#$DEST/##" | sort
echo
echo "To publish: copy the staged folder into RimWorld/Mods/, upload in-game (dev mode), then copy"
echo "the generated About/PublishedFileId.txt back into the repo's About/ and commit it."
