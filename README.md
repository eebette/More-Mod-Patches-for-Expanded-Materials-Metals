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

## Patched mods

128 buildings across 30 mods (building count in parens). Each has its own
`IfModActive`-gated folder, so only the mods you actually run are touched:

- Combat Extended Armory (24)
- Dubs Bad Hygiene (17)
- Alpha Biomes (11)
- Vanilla Chemfuel Expanded (8)
- Vanilla Nutrient Paste Expanded (8)
- Dubs Rimatomics (6)
- Vanilla Furniture Expanded - Production (6)
- RimFridge: Now with Shelves! (5)
- Vanilla Quests Expanded - The Generator (5)
- Expanded Prosthetics and Organ Engineering - Forked (4)
- Vanilla Cooking Expanded (4)
- RimThunder - Core (3)
- Vanilla Brewing Expanded (3)
- \[JDS\] Simple Storage - Refrigeration (3)
- Alpha Animals (2)
- Centralized Climate Control (Continued) (2)
- Hospitality: Vending machines (2)
- Vanilla Furniture Expanded - Medical Module (2)
- Vanilla Genetics Expanded (2)
- Combat Extended Guns (1)
- LWM's Deep Storage (1)
- Vanilla Brewing Expanded - Coffees and Teas (1)
- Vanilla Cooking Expanded - Haute (1)
- Vanilla Cooking Expanded - Stews (1)
- Vanilla Cooking Expanded - Sushi (1)
- Vanilla Factions Expanded - Settlers (1)
- Vanilla Furniture Expanded (1)
- Vanilla Plants Expanded - More Plants (1)
- Vanilla Quests Expanded - Drone Factory (1)
- Warehouse Storage (1)

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

## Structure

Laid out like EMM's own `ModPatches/` — one folder per patched mod under
`ModPatches/1.6/<Mod>/Patches/`, each gated in `LoadFolders.xml` by
`IfModActive="<packageId>"`, so a mod's patches load only when that mod is
present. Inside, bare `<Operation Class="…PatchOperationDistributeCost">` ops
(no `FindMod`/`Sequence` needed — the folder gate handles presence), with
defNames OR-joined per (metal, %, factor), just like EMM's hand-written files.

To cover another mod, add a `ModPatches/1.6/<Mod>/Patches/` folder and one
`IfModActive="<packageId>"` line in `LoadFolders.xml`. `tools/assignments.tsv`
and `tools/adversary-review.md` record which building got which metal, and why.

## Requires

- [Argonic Core](https://steamcommunity.com/sharedfiles/filedetails/?id=2944251509)
- [Expanded Materials - Metals](https://github.com/TheOriginalArgon/Expanded-Materials-Metals)

Load **after** Expanded Materials - Metals.
