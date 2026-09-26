# More Mod Patches for Expanded Materials - Metals

[![Latest Release](https://img.shields.io/github/v/release/eebette/More-Mod-Patches-for-Expanded-Materials-Metals?label=Latest%20Release)](https://github.com/eebette/More-Mod-Patches-for-Expanded-Materials-Metals/releases)
<!-- Steam Workshop badge goes here at publish -->

![Expanded Materials - Metals: Mod Patches](Media/Badge_MMP.png)

A companion patch for [Expanded Materials - Metals][emm] (EMM). EMM ships curated `ModPatches` for a set of mods; this
extends that same treatment to **modded Steel-costing buildings EMM does not cover**, so more of a heavy modlist's
content is built from EMM's metals instead of plain Steel.

[emm]: https://steamcommunity.com/sharedfiles/filedetails/?id=3333419387

## How it works

It reuses EMM's own `ArgonicCore.PatchOperations.PatchOperationDistributeCost` with EMM's own parameters, so its ops are
indistinguishable in form and numbers from EMM's hand-written ones. Each patched building's `Steel` cost is split into
one or more of EMM's metals by role:

> a reactor or energy weapon becomes Titanium; industrial machinery becomes TemperedSteel; a radiator or heater becomes
> Copper; a food, medical or plumbing body becomes StainlessSteel; nuclear shielding takes Lead. Conventional turrets,
> civil power plants and heavy extraction rigs are concrete instead (the Masonry patch's job).

Which metal goes where, and how much, is read off EMM's own patches rather than invented - see
[Methodology](#methodology).

## What it assigns

| Metal | Buildings | EMM Steel-base params |
|---|---|---|
| **Titanium** | energy weapons, reactors, nuclear precision equipment | 100% / factor 0.80 |
| **TemperedSteel** | industrial machinery (smelters, machining, assembly, factory) | 100% / factor 1 |
| **Copper** | thermal / heat-exchange (heaters, coolers, radiators) | 100% / factor 1.75 |
| **StainlessSteel** | food, medical, plumbing bodies | 100% / factor 0.75 |
| **Lead** | nuclear shielding (paired with Titanium) | 50% / factor 1.25 |

Each metal is drawn from the building's `Steel` cost; other costs (Components,
Plasteel, Silver, Uranium, ...) are left untouched. When several metals draw from
one Steel cost they split it sequentially, exactly as EMM does on multi-material
defs like `ShipHeatsink`. Conventional turrets, civil power plants and heavy
extraction rigs are **concrete**, not metal - those are handled by the
[Masonry patch](https://github.com/eebette/More-Mod-Patches-for-Expanded-Materials-Masonry),
which follows the same EMM-family conventions.

## Patched mods

93 buildings across 28 mods. Each mod has its own `IfModActive`-gated folder, so only
the mods you actually run are touched. Expand for the exact defs and metals:

<details><summary>Dubs Bad Hygiene (17)</summary>

- `AirConOutdoorUnit` - Air-Con Outdoor Unit -> Copper
- `AirconIndoorUnit` - air-con indoor unit -> Copper
- `BiosolidsComposter` - Biosolids Composter -> StainlessSteel
- `CryogenicExtractionNode` - cryogenic extraction node -> StainlessSteel
- `DBHSaunaHeaterElec` - Electric Sauna Heater -> Copper
- `FireSprinkler` - Fire Sprinkler -> StainlessSteel
- `FreezerUnit` - Walk-in freezer unit -> Copper, StainlessSteel
- `GeothermHeater` - Geothermal heater -> Copper
- `HotWaterTank` - hot water tank -> StainlessSteel
- `IrrigationSprinkler` - Irrigation Sprinkler -> StainlessSteel
- `KitchenSink` - Kitchen Sink -> StainlessSteel
- `RadiatorLarge` - large radiator -> Copper
- `RadiatorStuffed` - radiator -> Copper
- `RadiatorTowelRail` - Towel Rail -> Copper
- `SolarHeater` - solar heater -> Copper
- `WashingMachine` - Washing Machine -> StainlessSteel
- `plumbingValve` - plumbing valve -> StainlessSteel

</details>

<details><summary>Vanilla Nutrient Paste Expanded (8)</summary>

- `VNPE_NutrientPasteDripper` - nutrient paste dripper -> StainlessSteel
- `VNPE_NutrientPasteFeeder` - nutrient paste feeder -> StainlessSteel
- `VNPE_NutrientPasteGrinder` - nutrient paste grinder -> StainlessSteel
- `VNPE_NutrientPastePipe` - nutrient paste pipe -> StainlessSteel
- `VNPE_NutrientPasteTap` - nutrient paste tap -> StainlessSteel
- `VNPE_NutrientPasteValve` - nutrient paste valve -> StainlessSteel
- `VNPE_NutrientPasteVat` - nutrient paste vat -> StainlessSteel
- `VNPE_UndergroundNutrientPastePipe` - subterranean nutrient paste pipe -> StainlessSteel

</details>

<details><summary>Alpha Biomes (6)</summary>

- `AB_PropaneHeater` - propane heater -> Copper
- `AB_PropaneSmelter` - propane smelter -> TemperedSteel
- `AB_PropaneStove` - propane stove -> StainlessSteel
- `AB_PropaneTableMachining` - propane machining table -> TemperedSteel
- `AB_PropaneTap` - propane tap -> StainlessSteel
- `AB_SlimeCompressor` - slime compressor -> TemperedSteel

</details>

<details><summary>Dubs Rimatomics (6)</summary>

- `CoolingRadiator` - Radiator -> Copper
- `DU_Blastdoor` - DU Blast door -> Titanium
- `PPCRailgun` - Punisher -> Titanium
- `PlutoniumProcessor` - Plutonium Processor -> Lead, Titanium
- `RadiationShielding` - Reinforced DU Wall -> Lead, Titanium
- `TableRimatomicsMachining` - Rimatomics machining table -> TemperedSteel

</details>

<details><summary>Vanilla Chemfuel Expanded (6)</summary>

- `VCHE_ChemfuelTap` - chemfuel tap -> StainlessSteel
- `VCHE_DeepchemDrain` - deepchem drain -> StainlessSteel
- `VCHE_DeepchemPipe` - deepchem pipe -> StainlessSteel
- `VCHE_DeepchemTap` - deepchem tap -> StainlessSteel
- `VCHE_DeepchemValve` - deepchem valve -> StainlessSteel
- `VCHE_UndergroundDeepchemPipe` - subterranean deepchem pipe -> StainlessSteel

</details>

<details><summary>Vanilla Furniture Expanded - Production (6)</summary>

- `VFE_ComponentFabricationBench` - assembly bench -> TemperedSteel
- `VFE_FueledSmelter` - fueled smelter -> TemperedSteel
- `VFE_KitchenSinkCabinet` - kitchen sink cabinet -> StainlessSteel
- `VFE_TableButcherElectric` - electric butcher -> StainlessSteel
- `VFE_TableMachiningLarge` - large machining table -> TemperedSteel
- `VFE_TableStoveLarge` - large stove -> StainlessSteel

</details>

<details><summary>RimFridge: Now with Shelves! (5)</summary>

- `RimFridge_QuadRefrigerator` - Quad Refrigerator -> Copper, StainlessSteel
- `RimFridge_Refrigerator` - Dual Refrigerator -> Copper, StainlessSteel
- `RimFridge_SingleRefrigerator` - Single Refrigerator -> Copper, StainlessSteel
- `RimFridge_SingleWallRefrigerator` - Wall Single Refrigerator -> Copper, StainlessSteel
- `RimFridge_WallRefrigerator` - Wall Dual Refrigerator -> Copper, StainlessSteel

</details>

<details><summary>Expanded Prosthetics and Organ Engineering - Forked (4)</summary>

- `TableBasicProsthetic` - basic prosthetics workbench -> StainlessSteel
- `TableBionics` - bionics workbench -> StainlessSteel
- `TableOrgans` - tissue printer -> StainlessSteel
- `TableSimpleProsthetic` - prosthetic workbench -> StainlessSteel

</details>

<details><summary>Vanilla Cooking Expanded (4)</summary>

- `VCE_CanningMachine` - canning machine -> StainlessSteel
- `VCE_CheesePress` - cheese press -> StainlessSteel
- `VCE_ElectricPot` - electric pot -> StainlessSteel
- `VCE_Grill` - grill -> StainlessSteel

</details>

<details><summary>RimThunder - Core (3)</summary>

- `RTC_EngineHanger` - engine hanger -> TemperedSteel
- `RT_AssemblyBench` - assembly platfrom -> TemperedSteel
- `RT_AssemblyCrane` - assembly bridge crane -> TemperedSteel

</details>

<details><summary>Vanilla Brewing Expanded (3)</summary>

- `VBE_AmbrandyDistillery` - ambrandy distillery -> Copper, StainlessSteel
- `VBE_GinStill` - gin still -> Copper, StainlessSteel
- `VBE_SodaFountain` - soda fountain -> StainlessSteel

</details>

<details><summary>[1.5&Adaptive Storage][JDS] Simple Storage - Refrigeration (3)</summary>

- `JDS_IceBox` - Ice Box -> Copper, StainlessSteel
- `JDS_RefrigeratedBoxTrucks` - Refrigerated Box Trucks -> Copper, StainlessSteel
- `JDS_Refrigerator` - Refrigerator -> Copper, StainlessSteel

</details>

<details><summary>Alpha Animals (2)</summary>

- `AA_HexagelCoreReactor` - hexagel core reactor -> Titanium
- `VEF_AdvancedAnimalImplantsTable` - advanced animal prosthetics table -> StainlessSteel

</details>

<details><summary>Centralized Climate Control (Continued) (2)</summary>

- `AirThermal` - airThermal -> Copper
- `LargeAirThermal` - largeAirThermal -> Copper

</details>

<details><summary>Hospitality: Vending machines (2)</summary>

- `OwlFridgeVendingMachine` - fridge vending machine -> Copper, StainlessSteel
- `RimFridgeVendingMachine` - fridge vending machine -> Copper, StainlessSteel

</details>

<details><summary>Reel's Expanded Storage (2)</summary>

- `ReelStorageNewFridge` - fridge -> Copper, StainlessSteel
- `ReelStorageNewMedicineCabinet` - medical cabinet -> Copper, StainlessSteel

</details>

<details><summary>Vanilla Furniture Expanded - Medical Module (2)</summary>

- `Facility_VitalsCentre` - vitals centre -> StainlessSteel
- `VFEM_Wall_Sterile` - sterile wall -> StainlessSteel

</details>

<details><summary>Vanilla Genetics Expanded (2)</summary>

- `GR_GeneticExtractionTable` - genome extractor table -> StainlessSteel
- `GR_NutrientVat` - nutrient vat -> StainlessSteel

</details>

<details><summary>LWM's Deep Storage (1)</summary>

- `LWM_DS_RimFridge_Refrigerator` - Deep Refrigerator -> Copper, StainlessSteel

</details>

<details><summary>Vanilla Brewing Expanded - Coffees and Teas (1)</summary>

- `VBE_EspressoMachineBuilding` - espresso machine -> Copper, StainlessSteel

</details>

<details><summary>Vanilla Cooking Expanded - Haute (1)</summary>

- `VCE_ElectricHauteSection` - electric haute section -> StainlessSteel

</details>

<details><summary>Vanilla Cooking Expanded - Stews (1)</summary>

- `VCE_StewPot` - stew pot -> StainlessSteel

</details>

<details><summary>Vanilla Cooking Expanded - Sushi (1)</summary>

- `VCE_SoyFermenter` - soy sauce fermenter -> StainlessSteel

</details>

<details><summary>Vanilla Factions Expanded - Settlers (1)</summary>

- `ChemBoiler` - chemboiler -> Copper

</details>

<details><summary>Vanilla Furniture Expanded (1)</summary>

- `AirConditioningUnit` - air conditioning unit -> Copper

</details>

<details><summary>Vanilla Plants Expanded - More Plants (1)</summary>

- `VCE_VegMilkExtractor` - vegetable milk extractor -> StainlessSteel

</details>

<details><summary>Vanilla Quests Expanded - Drone Factory (1)</summary>

- `VFEFactory_DroneAutofactory` - drone autofactory -> TemperedSteel

</details>

<details><summary>Warehouse Storage (1)</summary>

- `Vin_FR` - Roller Fridge -> Copper, StainlessSteel

</details>

## Why Silicon / Germanium are omitted

EMM sources Silicon and Germanium **only from Gold** - its stand-in for a
high-tech electronics cost. The modded electronics here don't cost Gold; they
cost **Components**, which are *functional parts* (a microchip), not a raw
material EMM would substitute. Forcing Silicon onto Components also breaks
mechanically: `RoundToNearest5` has a 5-unit floor, so it would strip a
building's whole (small) Component count. So they're left out by design.

## Load order

> RimWorld -> Argonic Core -> Expanded Materials - Metals -> this mod.

Requires [Argonic Core](https://steamcommunity.com/sharedfiles/filedetails/?id=2944251509) and
[Expanded Materials - Metals][emm]; load it **after** EMM.

## My other mods

### The CE + Simple Sidearms suite

<table>
<tr><th width="300">Module</th><th width="540">What it does</th></tr>
<tr><td width="300"><a href="https://github.com/eebette/CombatExtended-SimpleSidearms-Compatibility-Patch"><img src="Media/Badge_Patch.png" width="300" alt="CE + Simple Sidearms Compatibility Patch"></a></td><td width="540">Core compatibility patch for Combat Extended and Simple Sidearms.</td></tr>
<tr><td width="300"><a href="https://github.com/eebette/CombatExtended-SimpleSidearms-Compatibility-Loadouts"><img src="Media/Badge_Loadouts.png" width="300" alt="CE + Simple Sidearms Loadouts Module"></a></td><td width="540">Syncs loadouts between Combat Extended and Simple Sidearms.</td></tr>
<tr><td width="300"><a href="https://github.com/eebette/CombatExtended-SimpleSidearms-Compatibility-Tactics"><img src="Media/Badge_Tactics.png" width="300" alt="Compatibility Module - Tactics"></a></td><td width="540">Sensible tweaks to nonsense pawn behavior when CE + SS run together.</td></tr>
</table>

### Standalone

<table>
<tr><th width="300">Mod</th><th width="540">What it does</th></tr>
<tr><td width="300"><a href="https://github.com/eebette/More-Mod-Patches-for-Expanded-Materials-Masonry"><img src="Media/Badge_MMMas.png" width="300" alt="Expanded Materials - Masonry: Mod Patches"></a></td><td width="540">The masonry sibling of this patch - extends Expanded Materials - Masonry to support additional mods.</td></tr>
<tr><td width="300"><a href="https://github.com/eebette/Better-Attack-Orders-for-Simple-Sidearms"><img src="Media/Badge_BAO.png" width="300" alt="Better Attack Orders for Simple Sidearms"></a></td><td width="540">Adds sidearm attack orders to the right-click target menu.</td></tr>
<tr><td width="300"><a href="https://github.com/eebette/Pawns-Optimize-Weapon-Quality"><img src="Media/Badge_POWQ.png" width="300" alt="Pawns Optimize Weapon Quality"></a></td><td width="540">Pawns will upgrade their held guns when a higher-quality copy is available.</td></tr>
</table>

## FAQ

**CE compatible?**

Yes - it only touches building costs, nothing CE does.

**Can I add or remove it mid-save?**

Yep.

**Does it change balance?**

Slightly, in the same direction EMM already goes: patched buildings cost EMM's metals instead of part of their Steel.
Wealth stays comparable.

**AI?**

This mod was engineered with the help of an AI Coding Assistant (Claude Code, Fable 5, Max effort). The amount of
researching and deep-diving the compatibility interfaces of mods that it patches would have been insurmountable without
it.

Development followed a standard process driven and scrutinized by me (the real human person writing this):
explore, design, build, test, fix, review, scrutinize, test again over many rounds.

I have manually reviewed and verified all code in this mod.

I ask that if you have unconstructive feedback regarding the usage of AI while developing this mod, that it remains
outside of this community space. Thank you.

## Methodology

The metal<->function mapping and the parameters are read off EMM's own patches, not
invented:

- **Which metal, which building** follows EMM's material->role conventions,
  audited by an independent adversarial review pass (`tools/adversary-review.md`,
  against the brief in `tools/adversary-brief.md`). That pass removed false
  matches (decorative props, "industrial"-in-name storage, air-movers mislabelled
  as heat exchangers, salvage chunks/husks) and re-typed several rows.
- **Which base cost, per metal** respects the tier EMM sources each metal from,
  or above (Steel for structural/thermal/shielding; StainlessSteel from Steel is
  within EMM's range - it uses Steel on the prosthetic base).
- **Percentages and `extraCostFactor`** are EMM's Steel-base medians. The factors
  are a *mining-effort* balance: Copper's 1.75 tracks copper ore's ~2x per-cell
  yield vs Steel/Iron, so a copper building costs roughly the same number of cells
  mined as the Steel original despite the larger unit count.

## Structure

Laid out like EMM's own `ModPatches/` - one folder per patched mod under
`ModPatches/1.6/<Mod>/Patches/`, each gated in `LoadFolders.xml` by
`IfModActive="<packageId>"`, so a mod's patches load only when that mod is
present. Inside, bare `<Operation Class="...PatchOperationDistributeCost">` ops
(no `FindMod`/`Sequence` needed - the folder gate handles presence), with
defNames OR-joined per (metal, %, factor), just like EMM's hand-written files.

Each folder's patch file has a **unique** name (`<Mod>_Patch_Buildings.xml`), the
way EMM names every file (`Odyssey_Patch_Buildings.xml`, `VGE_Patch_Buildings.xml`,
...). This matters: RimWorld's `LoadFolders` overrides files by their relative path
(later active folder wins), so a shared `Patches/Buildings.xml` across folders would
collapse to just one - every other mod's coverage silently shadowed once two or more
covered mods are active.

To cover another mod, add `ModPatches/1.6/<Mod>/Patches/<Mod>_Patch_Buildings.xml`
(unique filename, per above) and one `IfModActive="<packageId>"` line in
`LoadFolders.xml`. `tools/assignments.tsv` and `tools/adversary-review.md` record
which building got which metal, and why.

## Credit

All the material-to-role conventions and parameters here are [Argon's][emm], inferred from EMM's own patches and
extended to content they could not have covered. Bugs in the extension are mine.

## License

[MIT](LICENSE) - code, docs, and the badge artwork (the ingot and stone-block emblems are original; nothing here derives
from Combat Extended's art).
