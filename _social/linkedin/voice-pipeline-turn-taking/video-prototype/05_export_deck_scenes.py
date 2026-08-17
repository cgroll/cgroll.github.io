import json
import sys
from pathlib import Path

HERE = Path(__file__).parent
TIMING_FILE = sys.argv[1] if len(sys.argv) > 1 else "scene_timing.json"


def scene_js_data(scene):
    style = scene["visual"]["style"]
    content = scene["visual"].get("content", "")
    lines = content.split("\n") if content else []

    data = {"style": style}
    if style == "checklist":
        data["items"] = lines
    elif style == "cta":
        data["kicker"] = "FULL WRITEUP AND WALKTHROUGH"
        data["content"] = content
    elif style == "teaser":
        data["kicker"] = "COMING UP"
        data["lines"] = lines
    elif style == "pause":
        pass
    else:
        data["lines"] = lines
    if "kicker" in scene["visual"]:
        data["kicker"] = scene["visual"]["kicker"]
    return data


def main():
    data = json.loads((HERE / TIMING_FILE).read_text())
    entries = []
    for s in data["scenes"]:
        v = s["visual"]
        if v["kind"] == "text_slide":
            entries.append({"type": "slide", "id": s["id"], "data": scene_js_data(s)})
        elif v["kind"] == "animation_step":
            entries.append({"type": "diagram", "id": s["id"], "step": v["anim_step"], "group": v.get("group", "pipeline_speculative")})
        elif v["kind"] == "checklist_step":
            entries.append({"type": "checklist", "id": s["id"], "kicker": v["kicker"], "items": v["items"], "step": v["step"]})
        else:
            raise ValueError(v["kind"])

    out = HERE / "deck-scenes.js"
    out.write_text("const DECK_SCENES = " + json.dumps(entries, ensure_ascii=False, indent=2) + ";\n")
    print(f"Wrote {out} ({len(entries)} entries)")


if __name__ == "__main__":
    main()
