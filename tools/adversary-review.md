# EMM material-assignment audit

Reviewed all 175 supplied rows, with a separate verdict for every assigned metal. Evidence is limited to the supplied mod name, defName, label, Steel cost, patch, reasoning and signals, as requested. This is a semantic audit, not verification of mod XML, inheritance, recipes or actual buildability. Empty signals are missing evidence, not proof that a function is absent.

## Review conventions

- **keep** endorses the material/function association, not an empirically validated percentage. **remove** means the supplied evidence does not support the assignment, not that the material could never occur there. Changes name one of the six allowed materials.
- Powered does not automatically mean computerized. HeatPusher does not automatically mean a heat exchanger. A product's electronics are not automatically part of its manufacturing bench.
- Turret/Artillery building emplacements are treated as in scope because the brief explicitly allows turrets. The brief's weapons exclusion is interpreted as handheld/equippable weapons. Rows with only a turret defName still require building-class verification before implementation.
- Titanium is judged against the brief's game-design mapping for reactors, turrets and heavy machinery, not asserted to be the physically optimal real-world material.
- Fluid taps, valves and pipes qualify under the stated plumbing mapping; this is a design convention, not a finding that their fluids chemically require stainless steel. Air ducts and unspecified air-con lines need separate treatment.
- PropsandDecor rows are removed under a functional-building policy: the rows establish representations, not working appliances. If the intended policy instead models the materials of depicted objects, revisit these together; even then a console prop need not contain working electronics.
- Additional materials are marked **Add** when the named function supports them, and **Conditional** when they would require unavailable evidence. Conditional candidates are not recommendations to patch blindly. Suggested addition percentages are balance starting points only.

## Main findings

The strongest false matches are Silicon on air pipes/typewriters/drone pallets; Titanium on an industrial radio, shelves and cabinets; Lead on equipment merely associated with Rimatomics; and StainlessSteel on ceiling fans. Espresso equipment, the cheese press, genome extractor and vegetable-milk extractor have stronger hygienic-body justifications than high-strength-frame justifications. The mechahybrid antenna maps to communications Silicon rather than sensing Germanium.

Clear missing functions include condensation on distilleries, thermal hardware in an espresso machine, sensors plus monitoring electronics at the vitals centre, programmed control in the tissue printer, control in automatic turrets/radar, and heat transfer in nuclear/steam generation. Refrigerators already have the right two principal materials; a basic thermostat is not enough to add another 12% Silicon everywhere.

## Percentages and implementation concerns

1. Every percentage must be applied to the **original Steel cost**. Sum replacement units and subtract that sum once; sequential percentages of the shrinking remainder would violate the brief.
2. The 45% body/frame shares and 10-15% specialist shares cannot be validated as balanced from these rows. Retain them only as provisional templates. Silicon/Germanium at 12%/10% of an entire structure are substantial; consider 5-12% / 5-10% starting ranges for clearly supported electronics/sensors. No price, mass or EMM balance data was supplied.
3. Integer rounding needs an explicit shared rule. At 1 Steel, one unit is 100%; at 2 Steel, 50%; at 5 Steel, 20%. Do not silently force every assigned metal to at least one unit. If a tiny building cannot express the intended shares while retaining Steel, omit/coarsen the patch or redesign its costs deliberately.
4. Keep total integer material units equal to the original Steel units if the intended substitution is one-for-one, and leave positive Steel where the design says the remainder stays Steel. Compute all rounded allocations together and reject over-allocation. This is a suggested implementation invariant, not verified behavior of the existing patcher.
5. Full/empty industrial shelves both use 500 Steel; check whether those are distinct buildable definitions or state variants. CE-prefixed and unprefixed artillery rows likewise appear to be paired naming variants; confirm which definitions exist in the target version. No duplicate application or alias relationship can be proven from this TSV.
6. Check existing non-Steel costs before adding specialist materials, especially depleted-uranium-labeled walls/doors. Only Steel costs were supplied, so the audit cannot detect redundant existing requirements.
7. Building class/buildability remains unverified, especially turret rows with blank categories, ancient generators, drone chunks/pallets and the nuclear husk. A Steel cost alone does not establish an in-scope player building.

## Complete row-by-row review

Row numbers below count data rows, excluding the TSV header. Steel and assigned percentages are copied from the draft. Abbreviations in table material cells omit only the `EM_` prefix. Percent warnings describe original assignments even where removal is recommended.


### Alpha Animals

| Row / defName | Steel | Metal | Verdict and one-line reason |
| --- | ---: | --- | --- |
| 1. `AA_HexagelCoreReactor` | 100 | Titanium 45% | **keep** - Reactor frame fits the brief's reactor use. |
| 1. `AA_HexagelCoreReactor` | 100 | Lead 15% | **remove** - Hexagel reactor does not establish nuclear fuel or radiation; reactor alone is insufficient. |
| 2. `VEF_AdvancedAnimalImplantsTable` | 200 | StainlessSteel 45% | **keep** - Medical prosthetics fabrication supports hygienic working surfaces. |

### Alpha Biomes

| Row / defName | Steel | Metal | Verdict and one-line reason |
| --- | ---: | --- | --- |
| 3. `AB_BoneDistillery` | 150 | Titanium 45% | **keep** - The label says drill, supporting a loaded mechanical frame; the conflicting Distillery defName is not evidence of beverage processing. |
| 4. `AB_CoreSampleDrill` | 250 | Titanium 45% | **keep** - Core drilling clearly involves mechanically loaded equipment. |
| 5. `AB_MagmaThermalPlant` | 340 | Copper 12% | **keep** - Magma-thermal generation supports deliberate heat transfer. |
| 6. `AB_MagmaThermalPlant_Advanced` | 300 | Copper 12% | **keep** - Magma-thermal generation supports deliberate heat transfer. |
| 7. `AB_PropaneHeater` | 30 | Copper 12% | **keep** - A heater is an explicit Copper application in the brief. |
| 8. `AB_PropaneSmelter` | 170 | Titanium 45% | **keep** - A smelter fits the brief's industrial-machinery category; heat resistance alone would not justify Titanium. |
| 9. `AB_PropaneStove` | 60 | StainlessSteel 45% | **keep** - Food preparation supports hygienic bodywork. |
| 10. `AB_PropaneTableMachining` | 150 | Titanium 45% | **keep** - Machining supports a mechanically loaded frame. |
| 11. `AB_PropaneTap` | 60 | StainlessSteel 45% | **keep** - A propane tap is fluid-handling plumbing; corrosion-resistant fittings are plausible, though hygiene is not the reason. |
| 12. `AB_SlimeCompressor` | 50 | Titanium 45% | **keep** - Compression supports a loaded mechanical assembly, though 45% is a strong allocation for this small unit. |
| | | **Missing / percentage notes** | 45% Titanium is provisional; a smaller mechanical support may warrant a lower frame share, but no bill of materials is available. |
| 13. `AB_Turret_Propane` | 70 | Titanium 45% | **keep** - A turret building is explicitly within the Titanium mapping. |

### Centralized Climate Control (Continued)

| Row / defName | Steel | Metal | Verdict and one-line reason |
| --- | ---: | --- | --- |
| 14. `AirThermal` | 200 | Copper 12% | **keep** - TempControl and the thermal-unit label support heat exchange. |
| 14. `AirThermal` | 200 | Silicon 12% | **remove** - A thermostat does not by itself establish computing or substantial electronic controls. |
| 15. `IntakeFan` | 100 | Copper 12% | **remove** - An intake fan moves air; no heat exchanger is identified and motor wiring is excluded. |
| 15. `IntakeFan` | 100 | Silicon 12% | **remove** - Airflow and electrical power do not establish computing or electronic control hardware. |
| 16. `LargeAirThermal` | 600 | Copper 12% | **keep** - TempControl and the thermal-unit label support heat exchange. |
| 16. `LargeAirThermal` | 600 | Silicon 12% | **remove** - A thermostat does not by itself establish computing or substantial electronic controls. |
| 17. `LargeIntakeFan` | 300 | Copper 12% | **remove** - An intake fan moves air; no heat exchanger is identified and motor wiring is excluded. |
| 17. `LargeIntakeFan` | 300 | Silicon 12% | **remove** - Airflow and electrical power do not establish computing or electronic control hardware. |
| 18. `blueAirPipe` | 1 | Copper 12% | **remove** - Air ducts transport air; they are not identified as heat exchangers. |
| 18. `blueAirPipe` | 1 | Silicon 12% | **remove** - An AirFlow-only pipe has no supported electronic function. |
| | | **Missing / percentage notes** | Integer-cost warning: raw replacement quantities are Copper 0.12, Silicon 0.12; one whole unit equals 100% of this Steel cost. |
| 19. `cyanAirPipe` | 1 | Copper 12% | **remove** - Air ducts transport air; they are not identified as heat exchangers. |
| 19. `cyanAirPipe` | 1 | Silicon 12% | **remove** - An AirFlow-only pipe has no supported electronic function. |
| | | **Missing / percentage notes** | Integer-cost warning: raw replacement quantities are Copper 0.12, Silicon 0.12; one whole unit equals 100% of this Steel cost. |
| 20. `redAirPipe` | 1 | Copper 12% | **remove** - Air ducts transport air; they are not identified as heat exchangers. |
| 20. `redAirPipe` | 1 | Silicon 12% | **remove** - An AirFlow-only pipe has no supported electronic function. |
| | | **Missing / percentage notes** | Integer-cost warning: raw replacement quantities are Copper 0.12, Silicon 0.12; one whole unit equals 100% of this Steel cost. |

### Colony Manager Fork

| Row / defName | Steel | Metal | Verdict and one-line reason |
| --- | ---: | --- | --- |
| 21. `FM_ManagerStation` | 50 | Silicon 12% | **keep** - Powered ManagerStation supports a management/control terminal; retain provisionally because the label alone says desk. |

### Combat Extended Armory

| Row / defName | Steel | Metal | Verdict and one-line reason |
| --- | ---: | --- | --- |
| 22. `CE_Turret_12PounderBombard` | 200 | Titanium 45% | **keep** - The Turret/Artillery defName supports a building emplacement, fitting the brief's turret-frame mapping; this does not authorize handheld guns. |
| 23. `CE_Turret_GatlingGun` | 90 | Titanium 45% | **keep** - The Turret/Artillery defName supports a building emplacement, fitting the brief's turret-frame mapping; this does not authorize handheld guns. |
| 24. `CE_Turret_M1919Browning` | 160 | Titanium 45% | **keep** - The Turret/Artillery defName supports a building emplacement, fitting the brief's turret-frame mapping; this does not authorize handheld guns. |
| 25. `CE_Turret_M2HB` | 210 | Titanium 45% | **keep** - The Turret/Artillery defName supports a building emplacement, fitting the brief's turret-frame mapping; this does not authorize handheld guns. |
| 26. `CE_Turret_MkNineteenGL` | 130 | Titanium 45% | **keep** - The Turret/Artillery defName supports a building emplacement, fitting the brief's turret-frame mapping; this does not authorize handheld guns. |
| 27. `CE_Turret_OrganGun` | 150 | Titanium 45% | **keep** - The Turret/Artillery defName supports a building emplacement, fitting the brief's turret-frame mapping; this does not authorize handheld guns. |
| 28. `CE_Turret_PKM` | 120 | Titanium 45% | **keep** - The Turret/Artillery defName supports a building emplacement, fitting the brief's turret-frame mapping; this does not authorize handheld guns. |
| 29. `CE_Turret_PortableMortar` | 110 | Titanium 45% | **keep** - The Turret/Artillery defName supports a building emplacement, fitting the brief's turret-frame mapping; this does not authorize handheld guns. |
| 30. `CE_Turret_SPGNine` | 250 | Titanium 45% | **keep** - The Turret/Artillery defName supports a building emplacement, fitting the brief's turret-frame mapping; this does not authorize handheld guns. |
| 31. `CE_Turret_ShotgunTurret` | 100 | Titanium 45% | **keep** - An auto-turret is an explicit turret-frame application. |
| | | **Missing / percentage notes** | Add EM_Silicon (suggested 5-12%): automatic targeting implies control electronics; EM_Germanium is plausible but the targeting sensor type is not supplied. |
| 32. `CE_Turret_TwelvePounder` | 200 | Titanium 45% | **keep** - The Turret/Artillery defName supports a building emplacement, fitting the brief's turret-frame mapping; this does not authorize handheld guns. |
| 33. `CE_Turret_Vickers` | 170 | Titanium 45% | **keep** - The Turret/Artillery defName supports a building emplacement, fitting the brief's turret-frame mapping; this does not authorize handheld guns. |
| 34. `Turret_12PounderBombard` | 200 | Titanium 45% | **keep** - The Turret/Artillery defName supports a building emplacement, fitting the brief's turret-frame mapping; this does not authorize handheld guns. |
| 35. `Turret_GatlingGun` | 90 | Titanium 45% | **keep** - The Turret/Artillery defName supports a building emplacement, fitting the brief's turret-frame mapping; this does not authorize handheld guns. |
| 36. `Turret_M1919Browning` | 160 | Titanium 45% | **keep** - The Turret/Artillery defName supports a building emplacement, fitting the brief's turret-frame mapping; this does not authorize handheld guns. |
| 37. `Turret_M2HB` | 210 | Titanium 45% | **keep** - The Turret/Artillery defName supports a building emplacement, fitting the brief's turret-frame mapping; this does not authorize handheld guns. |
| 38. `Turret_MkNineteenGL` | 130 | Titanium 45% | **keep** - The Turret/Artillery defName supports a building emplacement, fitting the brief's turret-frame mapping; this does not authorize handheld guns. |
| 39. `Turret_OrganGun` | 150 | Titanium 45% | **keep** - The Turret/Artillery defName supports a building emplacement, fitting the brief's turret-frame mapping; this does not authorize handheld guns. |
| 40. `Turret_PKM` | 120 | Titanium 45% | **keep** - The Turret/Artillery defName supports a building emplacement, fitting the brief's turret-frame mapping; this does not authorize handheld guns. |
| 41. `Turret_PortableMortar` | 110 | Titanium 45% | **keep** - The Turret/Artillery defName supports a building emplacement, fitting the brief's turret-frame mapping; this does not authorize handheld guns. |
| 42. `Turret_SPGNine` | 250 | Titanium 45% | **keep** - The Turret/Artillery defName supports a building emplacement, fitting the brief's turret-frame mapping; this does not authorize handheld guns. |
| 43. `Turret_ShotgunTurret` | 100 | Titanium 45% | **keep** - An auto-turret is an explicit turret-frame application. |
| | | **Missing / percentage notes** | Add EM_Silicon (suggested 5-12%): automatic targeting implies control electronics; EM_Germanium is plausible but the targeting sensor type is not supplied. |
| 44. `Turret_TwelvePounder` | 200 | Titanium 45% | **keep** - The Turret/Artillery defName supports a building emplacement, fitting the brief's turret-frame mapping; this does not authorize handheld guns. |
| 45. `Turret_Vickers` | 170 | Titanium 45% | **keep** - The Turret/Artillery defName supports a building emplacement, fitting the brief's turret-frame mapping; this does not authorize handheld guns. |

### Combat Extended Guns

| Row / defName | Steel | Metal | Verdict and one-line reason |
| --- | ---: | --- | --- |
| 46. `CE_Artillery_Howitzer` | 400 | Titanium 45% | **keep** - The Turret/Artillery defName supports a building emplacement, fitting the brief's turret-frame mapping; this does not authorize handheld guns. |

### Dubs Bad Hygiene

| Row / defName | Steel | Metal | Verdict and one-line reason |
| --- | ---: | --- | --- |
| 47. `AirConOutdoorUnit` | 90 | StainlessSteel 45% | **remove** - Outdoor air-conditioning equipment is not shown to have a hygienic or wet-plumbing body; Hygiene category alone is insufficient. |
| 47. `AirConOutdoorUnit` | 90 | Copper 12% | **keep** - Air-conditioning equipment clearly exchanges heat. |
| 48. `AirconIndoorUnit` | 25 | Copper 12% | **keep** - Indoor air-conditioning equipment clearly exchanges heat. |
| 49. `BiosolidsComposter` | 45 | StainlessSteel 45% | **keep** - Wet biosolids processing supports a corrosion-resistant vessel. |
| 50. `CeilingFan` | 40 | StainlessSteel 45% | **remove** - A ceiling fan has no identified hygienic or wet-plumbing body; Hygiene category is a false positive. |
| 51. `CeilingFanS` | 40 | StainlessSteel 45% | **remove** - A ceiling fan has no identified hygienic or wet-plumbing body; Hygiene category is a false positive. |
| 52. `CryogenicExtractionNode` | 100 | StainlessSteel 45% | **keep** - Pipe-connected extraction supports corrosion-resistant fluid-handling parts; whether this is a dominant body material remains uncertain. |
| | | **Missing / percentage notes** | Conditional EM_Copper (about 12%): add if cryogenic describes active cooling, rather than simply extracting ice; IceWell and HeatPusher do not resolve this. |
| 53. `DBHSaunaHeaterElec` | 20 | Copper 12% | **keep** - A sauna heater fits the explicit heater mapping. |
| 54. `FireSprinkler` | 15 | StainlessSteel 45% | **keep** - Water-carrying sprinkler fittings fit the plumbing mapping. |
| | | **Missing / percentage notes** | Integer-cost warning: raw replacement quantities are StainlessSteel 6.75; one whole unit equals 6.66667% of this Steel cost. |
| 55. `FreezerUnit` | 30 | StainlessSteel 45% | **keep** - Freezer service supports hygienic/corrosion-resistant construction. |
| 55. `FreezerUnit` | 30 | Copper 12% | **keep** - Freezing clearly requires cooling. |
| 56. `GeothermHeater` | 240 | Copper 12% | **keep** - Geothermal boiler heating clearly supports heat transfer. |
| 57. `HotWaterTank` | 75 | StainlessSteel 45% | **keep** - A water-storage vessel supports corrosion-resistant construction. |
| | | **Missing / percentage notes** | No automatic Copper addition: HeatStore establishes heat storage, not an internal heater or heat exchanger. |
| 58. `IrrigationSprinkler` | 15 | StainlessSteel 45% | **keep** - Water-carrying irrigation fittings fit the plumbing mapping. |
| | | **Missing / percentage notes** | Integer-cost warning: raw replacement quantities are StainlessSteel 6.75; one whole unit equals 6.66667% of this Steel cost. |
| 59. `KitchenSink` | 15 | StainlessSteel 45% | **keep** - A kitchen sink clearly supports hygienic wet-service construction. |
| | | **Missing / percentage notes** | Integer-cost warning: raw replacement quantities are StainlessSteel 6.75; one whole unit equals 6.66667% of this Steel cost. |
| 60. `RadiatorLarge` | 15 | Copper 12% | **keep** - Radiator signal directly establishes heat transfer, including the towel rail. |
| | | **Missing / percentage notes** | Integer-cost warning: raw replacement quantities are Copper 1.8; one whole unit equals 6.66667% of this Steel cost. |
| 61. `RadiatorStuffed` | 15 | Copper 12% | **keep** - Radiator signal directly establishes heat transfer, including the towel rail. |
| | | **Missing / percentage notes** | Integer-cost warning: raw replacement quantities are Copper 1.8; one whole unit equals 6.66667% of this Steel cost. |
| 62. `RadiatorTowelRail` | 15 | Copper 12% | **keep** - Radiator signal directly establishes heat transfer, including the towel rail. |
| | | **Missing / percentage notes** | Integer-cost warning: raw replacement quantities are Copper 1.8; one whole unit equals 6.66667% of this Steel cost. |
| 63. `SolarHeater` | 75 | Copper 12% | **keep** - A solar boiler clearly supports heat transfer. |
| 64. `WashingMachine` | 100 | StainlessSteel 45% | **keep** - A washing machine has a wet-service body/drum. |
| 65. `airPipe` | 1 | StainlessSteel 45% | **remove** - An air-conditioning pipe is not established as wet plumbing; its carried medium and function are unresolved. |
| | | **Missing / percentage notes** | Integer-cost warning: raw replacement quantities are StainlessSteel 0.45; one whole unit equals 100% of this Steel cost. |
| 66. `plumbingValve` | 15 | StainlessSteel 45% | **keep** - A plumbing valve directly fits corrosion-resistant fluid fittings. |
| | | **Missing / percentage notes** | Integer-cost warning: raw replacement quantities are StainlessSteel 6.75; one whole unit equals 6.66667% of this Steel cost. |

### Dubs Rimatomics

| Row / defName | Steel | Metal | Verdict and one-line reason |
| --- | ---: | --- | --- |
| 67. `CoolingRadiator` | 350 | Copper 12% | **keep** - The radiator label directly establishes heat exchange. |
| 68. `DU_Blastdoor` | 40 | Titanium 45% | **keep** - A blast door supports a high-strength protective frame. |
| 68. `DU_Blastdoor` | 40 | Lead 15% | **remove** - Blast protection and a DU name do not alone establish a radiation-shielding function; confirm before adding a second shielding material. |
| 69. `NuclearResearchBench` | 250 | Titanium 45% | **remove** - A research bench is not itself heavy nuclear machinery. |
| 69. `NuclearResearchBench` | 250 | Silicon 12% | **keep** - A powered research bench fits the explicit research/electronics mapping. |
| 69. `NuclearResearchBench` | 250 | Lead 15% | **remove** - Nuclear research does not establish radioactive-material handling or built-in shielding. |
| | | **Missing / percentage notes** | Do not add StainlessSteel without wet-lab/sample-handling evidence. Original allocation totals 72%, leaving only 28% Steel before rounding; do not retain this stack without evaluating the individual removals above. |
| 70. `PPCRailgun` | 100 | Titanium 45% | **keep** - Railgun defName supports a turret emplacement and its loaded frame; confirm building identity before patching. |
| 71. `PPCWeaponsConsole` | 250 | Silicon 12% | **keep** - WeaponsConsole explicitly identifies a control console. |
| 72. `PlutoniumProcessor` | 200 | Titanium 45% | **keep** - A plutonium processor fits the brief's industrial-machinery mapping. |
| 72. `PlutoniumProcessor` | 200 | Silicon 12% | **remove** - Power and Facility do not establish a separate computing/control subsystem. |
| 72. `PlutoniumProcessor` | 200 | Lead 15% | **keep** - Plutonium processing directly supports radioactive-material shielding. |
| | | **Missing / percentage notes** | Conditional EM_StainlessSteel: add for wet chemical processing; the row does not identify the processing method. Original allocation totals 72%, leaving only 28% Steel before rounding; do not retain this stack without evaluating the individual removals above. |
| 73. `RadarDish` | 100 | Germanium 10% | **keep** - Radar is a sensing function under the brief's sensor mapping, not a literal real-world material specification. |
| | | **Missing / percentage notes** | Add EM_Silicon (suggested 5-12%): active radar requires signal processing/control alongside sensing. |
| 74. `RadiationShielding` | 5 | Titanium 45% | **keep** - Reinforced protective wall supports high-strength structure under the brief's mapping. |
| 74. `RadiationShielding` | 5 | Lead 15% | **keep** - RadiationShielding explicitly establishes shielding, though the DU label warrants checking existing non-Steel costs before adding Lead. |
| | | **Missing / percentage notes** | Integer-cost warning: raw replacement quantities are Titanium 2.25, Lead 0.75; one whole unit equals 20% of this Steel cost. |
| 75. `RimatomicsShieldGenerator` | 150 | Titanium 45% | **remove** - ProjectileInterceptor establishes a defensive field, not a mechanically loaded frame. |
| 75. `RimatomicsShieldGenerator` | 150 | Lead 15% | **remove** - Projectile interception is not radiation shielding; Rimatomics affiliation is insufficient. |
| 76. `TableRimatomicsMachining` | 150 | Titanium 45% | **keep** - A machining table supports industrial mechanical structure. |
| 76. `TableRimatomicsMachining` | 150 | Lead 15% | **remove** - Machining for a nuclear mod does not establish radioactive-material processing. |

### Expanded Prosthetics and Organ Engineering - Forked

| Row / defName | Steel | Metal | Verdict and one-line reason |
| --- | ---: | --- | --- |
| 77. `TableBasicProsthetic` | 35 | StainlessSteel 45% | **keep** - Prosthetics fabrication supports hygienic working surfaces; the products' electronics are not evidence of bench electronics. |
| 78. `TableBionics` | 250 | StainlessSteel 45% | **keep** - Prosthetics fabrication supports hygienic working surfaces; the products' electronics are not evidence of bench electronics. |
| 79. `TableOrgans` | 250 | StainlessSteel 45% | **keep** - Tissue handling supports hygienic construction. |
| | | **Missing / percentage notes** | Add EM_Silicon (suggested 5-12%): a tissue printer implies programmed deposition/control. |
| 80. `TableSimpleProsthetic` | 150 | StainlessSteel 45% | **keep** - Prosthetics fabrication supports hygienic working surfaces; the products' electronics are not evidence of bench electronics. |

### Hospitality: Vending machines

| Row / defName | Steel | Metal | Verdict and one-line reason |
| --- | ---: | --- | --- |
| 81. `OwlFridgeVendingMachine` | 40 | StainlessSteel 45% | **keep** - Refrigerated food storage supports hygienic/corrosion-resistant bodywork. |
| 81. `OwlFridgeVendingMachine` | 40 | Copper 12% | **keep** - Refrigeration explicitly supports cooling. |
| 82. `RimFridgeVendingMachine` | 40 | StainlessSteel 45% | **keep** - Refrigerated food storage supports hygienic/corrosion-resistant bodywork. |
| 82. `RimFridgeVendingMachine` | 40 | Copper 12% | **keep** - Refrigeration explicitly supports cooling. |

### LWM's Deep Storage

| Row / defName | Steel | Metal | Verdict and one-line reason |
| --- | ---: | --- | --- |
| 83. `LWM_DS_RimFridge_Refrigerator` | 80 | StainlessSteel 45% | **keep** - Refrigerated food storage supports hygienic/corrosion-resistant bodywork. |
| 83. `LWM_DS_RimFridge_Refrigerator` | 80 | Copper 12% | **keep** - Refrigeration explicitly supports cooling. |

### RimFridge: Now with Shelves!

| Row / defName | Steel | Metal | Verdict and one-line reason |
| --- | ---: | --- | --- |
| 84. `RimFridge_QuadRefrigerator` | 60 | StainlessSteel 45% | **keep** - Refrigerated food storage supports hygienic/corrosion-resistant bodywork. |
| 84. `RimFridge_QuadRefrigerator` | 60 | Copper 12% | **keep** - Refrigeration explicitly supports cooling. |
| 85. `RimFridge_Refrigerator` | 40 | StainlessSteel 45% | **keep** - Refrigerated food storage supports hygienic/corrosion-resistant bodywork. |
| 85. `RimFridge_Refrigerator` | 40 | Copper 12% | **keep** - Refrigeration explicitly supports cooling. |
| 86. `RimFridge_SingleRefrigerator` | 20 | StainlessSteel 45% | **keep** - Refrigerated food storage supports hygienic/corrosion-resistant bodywork. |
| 86. `RimFridge_SingleRefrigerator` | 20 | Copper 12% | **keep** - Refrigeration explicitly supports cooling. |
| 87. `RimFridge_SingleWallRefrigerator` | 20 | StainlessSteel 45% | **keep** - Refrigerated food storage supports hygienic/corrosion-resistant bodywork. |
| 87. `RimFridge_SingleWallRefrigerator` | 20 | Copper 12% | **keep** - Refrigeration explicitly supports cooling. |
| 88. `RimFridge_WallRefrigerator` | 40 | StainlessSteel 45% | **keep** - Refrigerated food storage supports hygienic/corrosion-resistant bodywork. |
| 88. `RimFridge_WallRefrigerator` | 40 | Copper 12% | **keep** - Refrigeration explicitly supports cooling. |

### RimThunder - Core

| Row / defName | Steel | Metal | Verdict and one-line reason |
| --- | ---: | --- | --- |
| 89. `RTC_EngineHanger` | 125 | Titanium 45% | **keep** - An engine support/hanger plausibly carries substantial mechanical loads; keep provisionally given only a Facility signal. |
| | | **Missing / percentage notes** | 45% Titanium is provisional; a smaller mechanical support may warrant a lower frame share, but no bill of materials is available. |
| 90. `RT_AssemblyBench` | 200 | Titanium 45% | **keep** - Vehicle-mod assembly platform supports an industrial assembly frame. |
| 91. `RT_AssemblyCrane` | 300 | Titanium 45% | **keep** - A bridge crane clearly has a loaded structural frame. |

### Simple Storage Reborn

| Row / defName | Steel | Metal | Verdict and one-line reason |
| --- | ---: | --- | --- |
| 92. `JDSIndustrial_shelf` | 500 | Titanium 45% | **remove** - Industrial in a shelf name does not establish machinery or exceptional structural loads; 500 Steel alone is not a functional signal. |
| 93. `JDSIndustrial_shelf_empty` | 500 | Titanium 45% | **remove** - Industrial in a shelf name does not establish machinery or exceptional structural loads; 500 Steel alone is not a functional signal. |

### Tavern

| Row / defName | Steel | Metal | Verdict and one-line reason |
| --- | ---: | --- | --- |
| 94. `Tav_KitchenAdd` | 15 | StainlessSteel 45% | **remove** - The row explicitly identifies kitchen decoration, not food-processing equipment. |
| | | **Missing / percentage notes** | Integer-cost warning: raw replacement quantities are StainlessSteel 6.75; one whole unit equals 6.66667% of this Steel cost. |

### Vanilla Books Expanded

| Row / defName | Steel | Metal | Verdict and one-line reason |
| --- | ---: | --- | --- |
| 95. `VBE_TypewritersTable` | 20 | Silicon 12% | **remove** - A powered typewriter can be electromechanical; neither its name nor comps establish computing electronics. |

### Vanilla Brewing Expanded

| Row / defName | Steel | Metal | Verdict and one-line reason |
| --- | ---: | --- | --- |
| 96. `VBE_AmbrandyDistillery` | 100 | StainlessSteel 45% | **keep** - Drink distillation supports hygienic wetted vessels. |
| | | **Missing / percentage notes** | Add EM_Copper (suggested 12%): distillation includes vapor cooling/condensation, a distinct thermal function. |
| 97. `VBE_GinStill` | 40 | StainlessSteel 45% | **keep** - Drink distillation supports hygienic wetted vessels. |
| | | **Missing / percentage notes** | Add EM_Copper (suggested 12%): a still includes vapor cooling/condensation, a distinct thermal function. |
| 98. `VBE_SodaFountain` | 40 | StainlessSteel 45% | **keep** - A beverage dispenser supports hygienic wetted parts. |
| | | **Missing / percentage notes** | Conditional EM_Copper only if dispensing includes refrigeration; a soda fountain label does not prove an onboard cooler. |

### Vanilla Brewing Expanded - Coffees and Teas

| Row / defName | Steel | Metal | Verdict and one-line reason |
| --- | ---: | --- | --- |
| 99. `VBE_EspressoMachineBuilding` | 45 | Titanium 45% | **change to EM_StainlessSteel** - An espresso machine is beverage equipment; its primary supported body requirement is hygiene, not a heavy industrial frame. |
| | | **Missing / percentage notes** | Add EM_Copper (suggested 12%): espresso preparation implies dedicated hot-water/steam thermal hardware. |

### Vanilla Chemfuel Expanded

| Row / defName | Steel | Metal | Verdict and one-line reason |
| --- | ---: | --- | --- |
| 100. `PS_DeepchemRefinery` | 200 | Titanium 45% | **keep** - A refinery fits the explicit industrial-machinery mapping. |
| | | **Missing / percentage notes** | Conditional EM_Copper if the refinery uses thermal separation; Refinery/ResourceProcessor alone does not specify the process. |
| 101. `PS_DeepchemTank` | 180 | Titanium 45% | **remove** - A storage tank is not shown to be pressurized or exceptionally loaded; explosive contents do not establish a high-strength frame requirement. |
| | | **Missing / percentage notes** | Conditional EM_StainlessSteel for a wetted/corrosion-resistant vessel under the plumbing mapping; fluid chemistry and vessel duty are unspecified. |
| 102. `VCHE_ChemfuelTap` | 60 | StainlessSteel 45% | **keep** - A fluid-dispensing tap fits corrosion-resistant plumbing, not food hygiene. |
| 103. `VCHE_DeepchemDrain` | 60 | Titanium 45% | **change to EM_StainlessSteel** - A fluid-network drain is plumbing; no high-load machinery is identified. |
| 104. `VCHE_DeepchemPipe` | 4 | Titanium 45% | **change to EM_StainlessSteel** - A fluid pipe fits corrosion-resistant plumbing; deepchem does not establish high structural loads. |
| | | **Missing / percentage notes** | Integer-cost warning: raw replacement quantities are Titanium 1.8; one whole unit equals 25% of this Steel cost. |
| 105. `VCHE_DeepchemPumpjack` | 150 | Titanium 45% | **keep** - A pumpjack clearly has mechanically loaded industrial structure. |
| 106. `VCHE_DeepchemTap` | 60 | Titanium 45% | **change to EM_StainlessSteel** - A fluid-dispensing tap is plumbing rather than heavy machinery. |
| 107. `VCHE_DeepchemValve` | 15 | Titanium 45% | **change to EM_StainlessSteel** - A fluid-network valve is plumbing rather than heavy machinery. |
| | | **Missing / percentage notes** | Integer-cost warning: raw replacement quantities are Titanium 6.75; one whole unit equals 6.66667% of this Steel cost. |
| 108. `VCHE_UndergroundDeepchemPipe` | 6 | Titanium 45% | **change to EM_StainlessSteel** - Buried fluid piping fits the plumbing mapping; burial alone does not establish a Titanium requirement. |
| | | **Missing / percentage notes** | Integer-cost warning: raw replacement quantities are Titanium 2.7; one whole unit equals 16.6667% of this Steel cost. |

### Vanilla Cooking Expanded

| Row / defName | Steel | Metal | Verdict and one-line reason |
| --- | ---: | --- | --- |
| 109. `VCE_CanningMachine` | 100 | StainlessSteel 45% | **keep** - Food canning supports hygienic food-contact equipment. |
| | | **Missing / percentage notes** | Conditional EM_Titanium only if a substantial powered press/seaming mechanism is confirmed; canning alone does not establish a heavy frame. |
| 110. `VCE_CheesePress` | 10 | Titanium 45% | **change to EM_StainlessSteel** - A cheese press is food-contact equipment; press alone does not justify a heavy-machinery Titanium allocation. |
| | | **Missing / percentage notes** | Integer-cost warning: raw replacement quantities are Titanium 4.5; one whole unit equals 10% of this Steel cost. |
| 111. `VCE_ElectricPot` | 50 | StainlessSteel 45% | **keep** - A cooking pot directly supports hygienic food-contact construction. |
| 112. `VCE_Grill` | 75 | StainlessSteel 45% | **keep** - A grill directly supports food-contact construction. |

### Vanilla Cooking Expanded - Haute

| Row / defName | Steel | Metal | Verdict and one-line reason |
| --- | ---: | --- | --- |
| 113. `VCE_ElectricHauteSection` | 140 | StainlessSteel 45% | **keep** - A cooking section supports hygienic preparation surfaces. |

### Vanilla Cooking Expanded - Stews

| Row / defName | Steel | Metal | Verdict and one-line reason |
| --- | ---: | --- | --- |
| 114. `VCE_StewPot` | 50 | StainlessSteel 45% | **keep** - A stew pot directly supports hygienic food-contact construction. |

### Vanilla Cooking Expanded - Sushi

| Row / defName | Steel | Metal | Verdict and one-line reason |
| --- | ---: | --- | --- |
| 115. `VCE_SoyFermenter` | 30 | StainlessSteel 45% | **keep** - Food fermentation supports a hygienic vessel. |

### Vanilla Factions Expanded - Settlers

| Row / defName | Steel | Metal | Verdict and one-line reason |
| --- | ---: | --- | --- |
| 116. `ChemBoiler` | 100 | Copper 12% | **keep** - A boiler/heater clearly supports purposeful heat transfer. |

### Vanilla Furniture Expanded

| Row / defName | Steel | Metal | Verdict and one-line reason |
| --- | ---: | --- | --- |
| 117. `AirConditioningUnit` | 180 | Copper 12% | **keep** - Air conditioning clearly supports heat exchange. |
| 118. `Joy_InudstrialComputer` | 60 | Silicon 12% | **keep** - A computer explicitly establishes computing electronics. |
| | | **Missing / percentage notes** | Conditional EM_Copper only for identified cooling/heatsink hardware; computing does not by itself establish the scale of cooling. |
| 119. `Joy_ModernComputer` | 100 | Silicon 12% | **keep** - A computer explicitly establishes computing electronics. |
| | | **Missing / percentage notes** | Conditional EM_Copper only for identified cooling/heatsink hardware; no dedicated cooling subsystem is supplied. |
| 120. `Radio_Industrial` | 50 | Titanium 45% | **change to EM_Silicon** - A radio is communications electronics; industrial is not evidence of a high-strength machinery frame. |

### Vanilla Furniture Expanded - Medical Module

| Row / defName | Steel | Metal | Verdict and one-line reason |
| --- | ---: | --- | --- |
| 121. `Facility_VitalsCentre` | 90 | StainlessSteel 45% | **keep** - A medical vitals unit supports hygienic medical construction. |
| | | **Missing / percentage notes** | Add EM_Germanium (suggested 5-10%) for vital-sign sensing and EM_Silicon (suggested 5-12%) for monitoring/display/control. |
| 122. `VFEM_Wall_Sterile` | 5 | StainlessSteel 45% | **keep** - A sterile wall explicitly supports hygienic construction. |
| | | **Missing / percentage notes** | Integer-cost warning: raw replacement quantities are StainlessSteel 2.25; one whole unit equals 20% of this Steel cost. |

### Vanilla Furniture Expanded - Production

| Row / defName | Steel | Metal | Verdict and one-line reason |
| --- | ---: | --- | --- |
| 123. `VFE_ComponentFabricationBench` | 100 | Titanium 45% | **keep** - A fabrication/assembly workbench fits industrial production structure; components being produced do not prove onboard computing. |
| 124. `VFE_FabricationCabinet` | 100 | Titanium 45% | **remove** - A fabrication cabinet with only Facility is not itself fabrication machinery. |
| 125. `VFE_FueledSmelter` | 170 | Titanium 45% | **keep** - A smelter fits the brief's industrial-machinery mapping; do not justify Titanium by heat resistance alone. |
| 126. `VFE_KitchenSinkCabinet` | 100 | StainlessSteel 45% | **keep** - A kitchen sink cabinet includes a hygienic wet-service sink. |
| 127. `VFE_MachiningCabinet` | 150 | Titanium 45% | **remove** - A machining cabinet with only Facility is not itself a machining mechanism. |
| 128. `VFE_TableButcherElectric` | 20 | StainlessSteel 45% | **keep** - Butchery directly supports hygienic food-contact construction. |
| 129. `VFE_TableMachiningLarge` | 300 | Titanium 45% | **keep** - A large machining table supports a loaded industrial frame. |
| 130. `VFE_TableStoveLarge` | 160 | StainlessSteel 45% | **keep** - A stove directly supports hygienic food preparation. |

### Vanilla Furniture Expanded - Props and Decor

| Row / defName | Steel | Metal | Verdict and one-line reason |
| --- | ---: | --- | --- |
| 131. `VFEPD_Cooker` | 5 | StainlessSteel 45% | **remove** - PropsandDecor with no functional signals does not establish operative cooking equipment. |
| | | **Missing / percentage notes** | Integer-cost warning: raw replacement quantities are StainlessSteel 2.25; one whole unit equals 20% of this Steel cost. |
| 132. `VFEPD_CookingAppliances` | 2 | StainlessSteel 45% | **remove** - PropsandDecor with no functional signals does not establish operative cooking equipment. |
| | | **Missing / percentage notes** | Integer-cost warning: raw replacement quantities are StainlessSteel 0.9; one whole unit equals 50% of this Steel cost. |
| 133. `VFEPD_DataConsole` | 10 | Silicon 12% | **remove** - A decorative console has no demonstrated computing function. |
| | | **Missing / percentage notes** | Integer-cost warning: raw replacement quantities are Silicon 1.2; one whole unit equals 10% of this Steel cost. |
| 134. `VFEPD_FoodTrolley` | 5 | StainlessSteel 45% | **remove** - This row identifies a decorative prop; actual food-service use is not established. |
| | | **Missing / percentage notes** | Integer-cost warning: raw replacement quantities are StainlessSteel 2.25; one whole unit equals 20% of this Steel cost. |
| 135. `VFEPD_Fridge` | 10 | StainlessSteel 45% | **remove** - A decorative fridge is not established as functioning hygienic storage. |
| 135. `VFEPD_Fridge` | 10 | Copper 12% | **remove** - A decorative fridge has no demonstrated refrigeration function. |
| | | **Missing / percentage notes** | Integer-cost warning: raw replacement quantities are StainlessSteel 4.5, Copper 1.2; one whole unit equals 10% of this Steel cost. |
| 136. `VFEPD_IndustrialGenerator` | 20 | Titanium 45% | **remove** - A decorative generator has no demonstrated machinery function. |
| 137. `VFEPD_KitchenSink` | 10 | StainlessSteel 45% | **remove** - PropsandDecor with no functional signals does not establish working kitchen equipment. |
| | | **Missing / percentage notes** | Integer-cost warning: raw replacement quantities are StainlessSteel 4.5; one whole unit equals 10% of this Steel cost. |
| 138. `VFEPD_KitchenSurface` | 10 | StainlessSteel 45% | **remove** - PropsandDecor with no functional signals does not establish working kitchen equipment. |
| | | **Missing / percentage notes** | Integer-cost warning: raw replacement quantities are StainlessSteel 4.5; one whole unit equals 10% of this Steel cost. |
| 139. `VFEPD_KitchenSurfaceEmpty` | 10 | StainlessSteel 45% | **remove** - PropsandDecor with no functional signals does not establish working kitchen equipment. |
| | | **Missing / percentage notes** | Integer-cost warning: raw replacement quantities are StainlessSteel 4.5; one whole unit equals 10% of this Steel cost. |
| 140. `VFEPD_LongCommandConsole` | 15 | Silicon 12% | **remove** - A decorative console/server prop has no demonstrated computing function. |
| | | **Missing / percentage notes** | Integer-cost warning: raw replacement quantities are Silicon 1.8; one whole unit equals 6.66667% of this Steel cost. |
| 141. `VFEPD_Oven` | 10 | StainlessSteel 45% | **remove** - PropsandDecor with no functional signals does not establish working kitchen equipment. |
| | | **Missing / percentage notes** | Integer-cost warning: raw replacement quantities are StainlessSteel 4.5; one whole unit equals 10% of this Steel cost. |
| 142. `VFEPD_PersonalConsole` | 5 | Silicon 12% | **remove** - A decorative console/server prop has no demonstrated computing function. |
| | | **Missing / percentage notes** | Integer-cost warning: raw replacement quantities are Silicon 0.6; one whole unit equals 20% of this Steel cost. |
| 143. `VFEPD_SensorPlatform` | 5 | Germanium 10% | **remove** - A decorative sensor platform has no demonstrated sensing function. |
| | | **Missing / percentage notes** | Integer-cost warning: raw replacement quantities are Germanium 0.5; one whole unit equals 20% of this Steel cost. |
| 144. `VFEPD_ServerRack` | 5 | Silicon 12% | **remove** - A decorative console/server prop has no demonstrated computing function. |
| | | **Missing / percentage notes** | Integer-cost warning: raw replacement quantities are Silicon 0.6; one whole unit equals 20% of this Steel cost. |
| 145. `VFEPD_SteelVendingMachine` | 10 | StainlessSteel 45% | **remove** - A decorative vending machine has no demonstrated hygienic food-storage function. |
| | | **Missing / percentage notes** | Integer-cost warning: raw replacement quantities are StainlessSteel 4.5; one whole unit equals 10% of this Steel cost. |
| 146. `VFEPD_WashingMachine` | 10 | StainlessSteel 45% | **remove** - A decorative washing machine has no demonstrated wet-service function. |
| | | **Missing / percentage notes** | Integer-cost warning: raw replacement quantities are StainlessSteel 4.5; one whole unit equals 10% of this Steel cost. |

### Vanilla Genetics Expanded

| Row / defName | Steel | Metal | Verdict and one-line reason |
| --- | ---: | --- | --- |
| 147. `GR_GeneticExtractionTable` | 100 | Titanium 45% | **change to EM_StainlessSteel** - Genome extraction supports hygienic biological-sample handling, not an exceptional high-strength frame. |
| | | **Missing / percentage notes** | Conditional EM_Silicon / EM_Germanium only if automated sequencing, sensing or optics are identified; extraction alone does not prove them. |
| 148. `GR_MechahybridAntenna` | 150 | Germanium 10% | **change to EM_Silicon** - Mechahybrid antenna/RegisterMechAntenna supports communications/control, not sensing or optics. |
| 149. `GR_NutrientVat` | 75 | StainlessSteel 45% | **keep** - A nutrient vessel supports hygienic biological-fluid contact. |

### Vanilla Nutrient Paste Expanded

| Row / defName | Steel | Metal | Verdict and one-line reason |
| --- | ---: | --- | --- |
| 150. `VNPE_NutrientPasteDripper` | 50 | StainlessSteel 45% | **keep** - Food-slurry handling/storage supports hygienic wetted construction. |
| 151. `VNPE_NutrientPasteFeeder` | 20 | StainlessSteel 45% | **keep** - Food-slurry handling/storage supports hygienic wetted construction. |
| 152. `VNPE_NutrientPasteGrinder` | 100 | StainlessSteel 45% | **keep** - Food-slurry handling/storage supports hygienic wetted construction. |
| 153. `VNPE_NutrientPastePipe` | 2 | StainlessSteel 45% | **keep** - Food-slurry piping clearly supports hygienic fluid-contact construction. |
| | | **Missing / percentage notes** | Integer-cost warning: raw replacement quantities are StainlessSteel 0.9; one whole unit equals 50% of this Steel cost. |
| 154. `VNPE_NutrientPasteTap` | 30 | StainlessSteel 45% | **keep** - Food-slurry handling/storage supports hygienic wetted construction. |
| 155. `VNPE_NutrientPasteValve` | 15 | StainlessSteel 45% | **keep** - Food-slurry handling/storage supports hygienic wetted construction. |
| | | **Missing / percentage notes** | Integer-cost warning: raw replacement quantities are StainlessSteel 6.75; one whole unit equals 6.66667% of this Steel cost. |
| 156. `VNPE_NutrientPasteVat` | 120 | StainlessSteel 45% | **keep** - Food-slurry handling/storage supports hygienic wetted construction. |
| 157. `VNPE_UndergroundNutrientPastePipe` | 4 | StainlessSteel 45% | **keep** - Food-slurry piping clearly supports hygienic fluid-contact construction. |
| | | **Missing / percentage notes** | Integer-cost warning: raw replacement quantities are StainlessSteel 1.8; one whole unit equals 25% of this Steel cost. |

### Vanilla Plants Expanded - More Plants

| Row / defName | Steel | Metal | Verdict and one-line reason |
| --- | ---: | --- | --- |
| 158. `VCE_VegMilkExtractor` | 75 | Titanium 45% | **change to EM_StainlessSteel** - Vegetable-milk extraction is food processing; extractor does not itself establish heavy structural loads. |

### Vanilla Quests Expanded - Drone Factory

| Row / defName | Steel | Metal | Verdict and one-line reason |
| --- | ---: | --- | --- |
| 159. `VFEFactory_DroneAutofactory` | 440 | Titanium 45% | **keep** - An autofactory supports industrial mechanical structure. |
| 159. `VFEFactory_DroneAutofactory` | 440 | Silicon 12% | **keep** - Autonomous manufacture supports control electronics beyond a generic powered workbench. |
| 160. `VQED_DroneChunk` | 20 | Silicon 12% | **remove** - A drone chunk is not established as a functioning computing building; salvage electronics are a separate policy. |
| 161. `VQED_DroneResourcePallet` | 30 | Silicon 12% | **remove** - A resource pallet does not compute merely because its contents are used for drones. |
| 162. `VQED_UnfinishedDronePallet` | 20 | Silicon 12% | **remove** - An unfinished-drone pallet does not establish a functioning electronic building; its contents are a separate policy. |
| 163. `VQE_DroneTinkeringBench` | 160 | Silicon 12% | **remove** - Working on drones does not establish onboard computing in the tinkering bench; Power alone is insufficient. |
| | | **Missing / percentage notes** | Conditional EM_Silicon only if diagnostic/control electronics are documented as part of the bench. |
| 164. `VQE_DroneTransmitter` | 80 | Silicon 12% | **keep** - A transmitter explicitly establishes communications electronics. |

### Vanilla Quests Expanded - The Generator

| Row / defName | Steel | Metal | Verdict and one-line reason |
| --- | ---: | --- | --- |
| 165. `VQE_AncientGeothermalGenetron` | 440 | Copper 12% | **keep** - Geothermal generation supports heat transfer if this ancient object is a functional/buildable generator; blank signals leave scope unresolved. |
| 166. `VQE_Genetron_Geothermal` | 300 | Copper 12% | **keep** - Geothermal generation supports heat transfer. |
| 167. `VQE_Genetron_Nuclear` | 100 | Titanium 45% | **keep** - A nuclear generator fits the brief's reactor-frame mapping. |
| 167. `VQE_Genetron_Nuclear` | 100 | Lead 15% | **keep** - Nuclear generation supports radiation shielding. |
| | | **Missing / percentage notes** | Add EM_Copper (suggested 12%): nuclear power conversion supports a distinct heat-transfer/cooling function. |
| 168. `VQE_Genetron_SteamPowered` | 100 | StainlessSteel 45% | **keep** - Steam/water service supports corrosion-resistant wetted construction. |
| | | **Missing / percentage notes** | Add EM_Copper (suggested 12%): steam-powered generation supports heat-transfer hardware alongside wet-service construction. |
| 169. `VQE_Genetron_ThermalVent` | 200 | Copper 12% | **keep** - A thermal-vent generator supports purposeful heat transfer. |
| 170. `VQE_NuclearGenetronHusk` | 440 | Titanium 45% | **remove** - A husk with no functional signals is not established as a working/buildable reactor; salvage-material policy is separate. |
| 170. `VQE_NuclearGenetronHusk` | 440 | Lead 15% | **remove** - A nuclear husk may retain shielding or contamination, but neither is established by this row; do not infer an active shielding requirement. |
| | | **Missing / percentage notes** | If it is a buildable/restorable shell, reassess retained frame and shielding materials; do not add operating electronics or cooling based on the former function alone. |

### Vanilla Trading Expanded

| Row / defName | Steel | Metal | Verdict and one-line reason |
| --- | ---: | --- | --- |
| 171. `VTE_TradingTerminal` | 140 | Silicon 12% | **keep** - A trading terminal explicitly supports computing/communications electronics. |

### Warehouse Storage

| Row / defName | Steel | Metal | Verdict and one-line reason |
| --- | ---: | --- | --- |
| 172. `Vin_FR` | 30 | StainlessSteel 45% | **keep** - Refrigerated storage supports hygienic/corrosion-resistant bodywork. |
| 172. `Vin_FR` | 30 | Copper 12% | **keep** - The refrigeration label and power support cooling, including the otherwise ambiguous Ice Box. |

### [1.5&Adaptive Storage][JDS] Simple Storage - Refrigeration

| Row / defName | Steel | Metal | Verdict and one-line reason |
| --- | ---: | --- | --- |
| 173. `JDS_IceBox` | 150 | StainlessSteel 45% | **keep** - Refrigerated storage supports hygienic/corrosion-resistant bodywork. |
| 173. `JDS_IceBox` | 150 | Copper 12% | **keep** - The refrigeration label and power support cooling, including the otherwise ambiguous Ice Box. |
| 174. `JDS_RefrigeratedBoxTrucks` | 800 | StainlessSteel 45% | **keep** - A refrigerated cargo body supports hygienic storage, but 45% of the whole truck's Steel overstates the demonstrated share. |
| 174. `JDS_RefrigeratedBoxTrucks` | 800 | Copper 12% | **keep** - Refrigeration supports cooling, though 12% of whole-truck Steel needs component-scale calibration. |
| | | **Missing / percentage notes** | Conditional EM_Titanium if this is an actual mobile vehicle/chassis; a truck-shaped storage building with only Power does not prove that function. 45% StainlessSteel = 360 units and 12% Copper = 96 units; calibrate against refrigerated body/cooling size, not merely the 800-Steel whole-object cost. |
| 175. `JDS_Refrigerator` | 300 | StainlessSteel 45% | **keep** - Refrigerated storage supports hygienic/corrosion-resistant bodywork. |
| 175. `JDS_Refrigerator` | 300 | Copper 12% | **keep** - The refrigeration label and power support cooling, including the otherwise ambiguous Ice Box. |

Coverage: **175 rows; 209 existing material assignments: 144 keep, 54 remove, 11 change.** Additions are separate from these counts.
