"""Export isolated SVG frames for the lesson-page player.

Run build.py first. The original diagrams remain the source of truth.
"""

from pathlib import Path
import xml.etree.ElementTree as ET


ROOT = Path(__file__).resolve().parents[2]
SOURCE = Path(__file__).resolve().parent / "svg"
DESTINATION = ROOT / "assets" / "lesson-visuals"
ET.register_namespace("", "http://www.w3.org/2000/svg")


def export(source: Path) -> None:
    for step in range(1, 5):
        tree = ET.parse(source)
        for group in tree.getroot().iter():
            if group.tag.endswith("}g") and "data-s" in group.attrib:
                group_step = int(group.attrib["data-s"])
                if group_step > step:
                    group.set("display", "none")
        target = DESTINATION / f"{source.stem}-step-{step}.svg"
        tree.write(target, encoding="unicode", xml_declaration=False)


if __name__ == "__main__":
    DESTINATION.mkdir(parents=True, exist_ok=True)
    sources = sorted(SOURCE.glob("*.svg"))
    if len(sources) != 5:
        raise SystemExit(f"Expected five diagrams in {SOURCE}, got {len(sources)}")
    for source in sources:
        export(source)
    print(f"Exported {len(sources) * 4} SVG frames to {DESTINATION}")
