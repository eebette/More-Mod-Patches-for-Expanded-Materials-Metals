# Review brief - EMM material assignment patchlist

You are auditing a material-assignment list for a **RimWorld** mod, *Expanded Materials - Metals* (EMM).
In the base game, most powered/production buildings cost **Steel**. EMM adds new metals; this patch
substitutes a portion of a building's Steel cost with contextually-appropriate EMM metals (the rest stays Steel).

## Scope - the NON-substitutable metals only
EMM already lets the player swap Steel for **Iron, Bronze, MildSteel, TemperedSteel, or Aluminium** at
build time via an in-game gizmo (the "substitutable" tier). This patch does **not** touch those. It only
adds the metals the gizmo can't provide:

- **EM_Copper** - heat exchange / cooling (heatsinks, coolers, heaters, radiators, refrigeration). In EMM's
  own patches copper is a *thermal-conduction* material, NOT generic "electrical wiring".
- **EM_Silicon** - computing / control electronics (computers, AI, research, comms, control units)
- **EM_Germanium** - sensors, scanners, optics
- **EM_StainlessSteel** - corrosion-resistant / hygienic bodies (food, cooking, plumbing, medical, fridges)
- **EM_Titanium** - high-strength frames (reactors, heavy machinery, turrets, vehicles, industrial)
- **EM_Lead** - radiation shielding (nuclear)

## Rules the list is supposed to follow
1. Assign a metal for **each functional aspect** a building clearly has. Multiple metals per building are
   expected where sensible (e.g. a fridge = StainlessSteel body + Copper cooling).
2. Percentages substitute that share of Steel; the remainder stays Steel.
3. Use **only** the six metals above. Never Bronze/Iron/MildSteel/TemperedSteel/Aluminium (those are the
   substitutable tier, handled by the gizmo), and never for weapons/apparel.
4. Only Steel-costing buildings are in scope.

## Your job - for each row, judge PER METAL
Reply `keep` / `change to <metal>` / `remove` with a one-line reason. Also flag:
- metals that don't fit the building's actual function (over-reach / false keyword match),
- buildings clearly **missing** a metal they should have,
- percentages that seem off.
You have only the row's mod, defName, label, steel cost, assigned patch, stated reasoning, and comp/category
signals. Judge from those.
