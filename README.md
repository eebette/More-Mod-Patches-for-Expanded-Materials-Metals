# More Mod Patches for Expanded Materials - Metals

A companion patch for [Expanded Materials - Metals](https://github.com/TheOriginalArgon/Expanded-Materials-Metals)
(EMM). EMM ships curated `ModPatches` for a set of mods; this extends that same
treatment to **modded Steel-costing buildings EMM does not cover**, so more of a
heavy modlist's content is built from EMM's metals instead of plain Steel.

It uses EMM's own `ArgonicCore.PatchOperations.PatchOperationDistributeCost` with
EMM's own parameters, so its ops are indistinguishable in form and numbers from
EMM's hand-written ones.

## What it assigns

| Metal | Buildings | EMM Steel-base params |
|---|---|---|
| **Titanium** | structural frames, heavy machinery, turrets, reactors, refineries | 100% / factor 0.80 |
| **Copper** | thermal / heat-exchange (heaters, coolers, radiators, generators) | 100% / factor 1.75 |
| **StainlessSteel** | food, medical, plumbing bodies | 100% / factor 0.75 |
| **Lead** | nuclear shielding | 80% / factor 1.25 |

Each metal is drawn from the building's `Steel` cost; other costs (Components,
Plasteel, Silver, Uranium, …) are left untouched. When several metals draw from
one Steel cost they split it sequentially, exactly as EMM does on multi-material
defs like `ShipHeatsink`.

## Why Silicon / Germanium are omitted

EMM sources Silicon and Germanium **only from Gold** — its stand-in for a
high-tech electronics cost. The modded electronics here don't cost Gold; they
cost **Components**, which are *functional parts* (a microchip), not a raw
material EMM would substitute. Forcing Silicon onto Components also breaks
mechanically: `RoundToNearest5` has a 5-unit floor, so it would strip a
building's whole (small) Component count. So they're left out by design.

## Methodology

The metal↔function mapping and the parameters are read off EMM's own patches, not
invented:

- **Which metal, which building** follows EMM's material→role conventions,
  audited by an independent adversarial review pass (`tools/adversary-review.md`,
  against the brief in `tools/adversary-brief.md`). That pass removed false
  matches (decorative props, "industrial"-in-name storage, air-movers mislabelled
  as heat exchangers, salvage chunks/husks) and re-typed several rows.
- **Which base cost, per metal** respects the tier EMM sources each metal from,
  or above (Steel for structural/thermal/shielding; StainlessSteel from Steel is
  within EMM's range — it uses Steel on the prosthetic base).
- **Percentages and `extraCostFactor`** are EMM's Steel-base medians. The factors
  are a *mining-effort* balance: Copper's 1.75 tracks copper ore's ~2× per-cell
  yield vs Steel/Iron, so a copper building costs roughly the same number of cells
  mined as the Steel original despite the larger unit count.

## Structure & regenerating

Laid out exactly like EMM's own `ModPatches/` — one folder per patched mod under
`ModPatches/1.6/<Mod>/Patches/`, each gated in `LoadFolders.xml` by
`IfModActive="<packageId>"`, so a mod's patches load only when that mod is
present. Inside, bare `<Operation Class="…PatchOperationDistributeCost">` ops
(no `FindMod`/`Sequence` needed — the folder gate handles presence), with
defNames OR-joined per (metal, %, factor), just like EMM's hand-written files.

`tools/generate.py` regenerates the whole `ModPatches/` tree **and**
`LoadFolders.xml` from two owner-editable tables:

- `tools/assignments.tsv` — the curated (adversary-vetted) building→metal list
- `tools/mods.tsv` — `modName → packageId → folder`

```
python3 tools/generate.py
```

Edit either table (or the parameters at the top of `generate.py`), then re-run.

## Requires

- [Argonic Core](https://steamcommunity.com/sharedfiles/filedetails/?id=2944251509)
- [Expanded Materials - Metals](https://github.com/TheOriginalArgon/Expanded-Materials-Metals)

Load **after** Expanded Materials - Metals.
