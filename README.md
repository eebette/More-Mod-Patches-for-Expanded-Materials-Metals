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
Plasteel, Silver, Uranium, ...) are left untouched. When several metals draw from
one Steel cost they split it sequentially, exactly as EMM does on multi-material
defs like `ShipHeatsink`.

## Patched mods

128 buildings across 30 mods. Each mod has its own `IfModActive`-gated folder, so only
the mods you actually run are touched. Expand for the exact defs and metals:

<details><summary>Combat Extended Armory (24)</summary>

- `CE_Turret_12PounderBombard` - 12-pounder bombard -> Titanium
- `CE_Turret_GatlingGun` - Gatling gun -> Titanium
- `CE_Turret_M1919Browning` - M1919 machine gun -> Titanium
- `CE_Turret_M2HB` - M2 Browning machine gun -> Titanium
- `CE_Turret_MkNineteenGL` - Mk 19 grenade launcher -> Titanium
- `CE_Turret_OrganGun` - organ gun -> Titanium
- `CE_Turret_PKM` - PKM machine gun -> Titanium
- `CE_Turret_PortableMortar` - 60mm portable mortar -> Titanium
- `CE_Turret_SPGNine` - SPG-9 recoilless gun -> Titanium
- `CE_Turret_ShotgunTurret` - shotgun auto-turret -> Titanium
- `CE_Turret_TwelvePounder` - 12-pounder cannon -> Titanium
- `CE_Turret_Vickers` - Vickers machine gun -> Titanium
- `Turret_12PounderBombard` - 12-pounder bombard -> Titanium
- `Turret_GatlingGun` - Gatling gun -> Titanium
- `Turret_M1919Browning` - M1919 machine gun -> Titanium
- `Turret_M2HB` - M2 Browning machine gun -> Titanium
- `Turret_MkNineteenGL` - Mk 19 grenade launcher -> Titanium
- `Turret_OrganGun` - organ gun -> Titanium
- `Turret_PKM` - PKM machine gun -> Titanium
- `Turret_PortableMortar` - 60mm portable mortar -> Titanium
- `Turret_SPGNine` - SPG-9 recoilless gun -> Titanium
- `Turret_ShotgunTurret` - shotgun auto-turret -> Titanium
- `Turret_TwelvePounder` - 12-pounder cannon -> Titanium
- `Turret_Vickers` - Vickers machine gun -> Titanium

</details>

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

<details><summary>Alpha Biomes (11)</summary>

- `AB_BoneDistillery` - bone drill -> Titanium
- `AB_CoreSampleDrill` - core sample drill -> Titanium
- `AB_MagmaThermalPlant` - magma-thermal generator -> Copper
- `AB_MagmaThermalPlant_Advanced` - advanced magma-thermal generator -> Copper
- `AB_PropaneHeater` - propane heater -> Copper
- `AB_PropaneSmelter` - propane smelter -> Titanium
- `AB_PropaneStove` - propane stove -> StainlessSteel
- `AB_PropaneTableMachining` - propane machining table -> Titanium
- `AB_PropaneTap` - propane tap -> StainlessSteel
- `AB_SlimeCompressor` - slime compressor -> Titanium
- `AB_Turret_Propane` - propane turret -> Titanium

</details>

<details><summary>Vanilla Chemfuel Expanded (8)</summary>

- `PS_DeepchemRefinery` - deepchem refinery -> Titanium
- `VCHE_ChemfuelTap` - chemfuel tap -> StainlessSteel
- `VCHE_DeepchemDrain` - deepchem drain -> StainlessSteel
- `VCHE_DeepchemPipe` - deepchem pipe -> StainlessSteel
- `VCHE_DeepchemPumpjack` - deepchem pumpjack -> Titanium
- `VCHE_DeepchemTap` - deepchem tap -> StainlessSteel
- `VCHE_DeepchemValve` - deepchem valve -> StainlessSteel
- `VCHE_UndergroundDeepchemPipe` - subterranean deepchem pipe -> StainlessSteel

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

<details><summary>Dubs Rimatomics (6)</summary>

- `CoolingRadiator` - Radiator -> Copper
- `DU_Blastdoor` - DU Blast door -> Titanium
- `PPCRailgun` - Punisher -> Titanium
- `PlutoniumProcessor` - Plutonium Processor -> Lead, Titanium
- `RadiationShielding` - Reinforced DU Wall -> Lead, Titanium
- `TableRimatomicsMachining` - Rimatomics machining table -> Titanium

</details>

<details><summary>Vanilla Furniture Expanded - Production (6)</summary>

- `VFE_ComponentFabricationBench` - assembly bench -> Titanium
- `VFE_FueledSmelter` - fueled smelter -> Titanium
- `VFE_KitchenSinkCabinet` - kitchen sink cabinet -> StainlessSteel
- `VFE_TableButcherElectric` - electric butcher -> StainlessSteel
- `VFE_TableMachiningLarge` - large machining table -> Titanium
- `VFE_TableStoveLarge` - large stove -> StainlessSteel

</details>

<details><summary>RimFridge: Now with Shelves! (5)</summary>

- `RimFridge_QuadRefrigerator` - Quad Refrigerator -> Copper, StainlessSteel
- `RimFridge_Refrigerator` - Dual Refrigerator -> Copper, StainlessSteel
- `RimFridge_SingleRefrigerator` - Single Refrigerator -> Copper, StainlessSteel
- `RimFridge_SingleWallRefrigerator` - Wall Single Refrigerator -> Copper, StainlessSteel
- `RimFridge_WallRefrigerator` - Wall Dual Refrigerator -> Copper, StainlessSteel

</details>

<details><summary>Vanilla Quests Expanded - The Generator (5)</summary>

- `VQE_AncientGeothermalGenetron` - ancient geothermal ARC -> Copper
- `VQE_Genetron_Geothermal` - geothermal ARC -> Copper
- `VQE_Genetron_Nuclear` - nuclear ARC -> Copper, Lead, Titanium
- `VQE_Genetron_SteamPowered` - steam-powered ARC -> Copper, StainlessSteel
- `VQE_Genetron_ThermalVent` - thermal-vent ARC -> Copper

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

- `RTC_EngineHanger` - engine hanger -> Titanium
- `RT_AssemblyBench` - assembly platfrom -> Titanium
- `RT_AssemblyCrane` - assembly bridge crane -> Titanium

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

<details><summary>Vanilla Furniture Expanded - Medical Module (2)</summary>

- `Facility_VitalsCentre` - vitals centre -> StainlessSteel
- `VFEM_Wall_Sterile` - sterile wall -> StainlessSteel

</details>

<details><summary>Vanilla Genetics Expanded (2)</summary>

- `GR_GeneticExtractionTable` - genome extractor table -> StainlessSteel
- `GR_NutrientVat` - nutrient vat -> StainlessSteel

</details>

<details><summary>Combat Extended Guns (1)</summary>

- `CE_Artillery_Howitzer` - 105mm howitzer -> Titanium

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

- `VFEFactory_DroneAutofactory` - drone autofactory -> Titanium

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

To cover another mod, add a `ModPatches/1.6/<Mod>/Patches/` folder and one
`IfModActive="<packageId>"` line in `LoadFolders.xml`. `tools/assignments.tsv`
and `tools/adversary-review.md` record which building got which metal, and why.

## Requires

- [Argonic Core](https://steamcommunity.com/sharedfiles/filedetails/?id=2944251509)
- [Expanded Materials - Metals](https://github.com/TheOriginalArgon/Expanded-Materials-Metals)

Load **after** Expanded Materials - Metals.
