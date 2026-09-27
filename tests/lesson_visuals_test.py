from pathlib import Path
import unittest
import xml.etree.ElementTree as ET


ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets" / "lesson-visuals"
DIAGRAMS = {
    "h1-bias-before-m15": 560,
    "what-a-sweep-does-not-prove": 534,
    "the-sweep-that-isnt": 590,
    "when-london-matters": 644,
    "pre-trade-journal": 600,
}


class LessonVisualsTest(unittest.TestCase):
    def test_frames_are_complete_and_valid(self):
        self.assertEqual(len(list(ASSETS.glob("*.svg"))), 20)
        for name, height in DIAGRAMS.items():
            for step in range(1, 5):
                with self.subTest(name=name, step=step):
                    frame = ASSETS / f"{name}-step-{step}.svg"
                    root = ET.parse(frame).getroot()
                    self.assertEqual(root.attrib["viewBox"], f"0 0 360 {height}")
                    self.assertEqual(root.attrib.get("data-steps"), "4")
                    self.assertIsNotNone(root.find("{http://www.w3.org/2000/svg}title"))
                    groups = [node for node in root.iter() if "data-s" in node.attrib]
                    self.assertTrue(groups)
                    for group in groups:
                        expected = "none" if int(group.attrib["data-s"]) > step else None
                        self.assertEqual(group.attrib.get("display"), expected)
                    self.assertNotIn("<script", frame.read_text(encoding="utf-8"))

    def test_lessons_reference_their_visual(self):
        lessons = {
            "h1-bias-before-m15": "read-structure/06-h1-bias-before-m15.md",
            "what-a-sweep-does-not-prove": "hunt-liquidity/04-what-a-sweep-does-not-prove.md",
            "the-sweep-that-isnt": "hunt-liquidity/03-sweep-that-isnt.md",
            "when-london-matters": "time-the-killzone/02-when-london-matters.md",
            "pre-trade-journal": "master-the-mind/06-pre-trade-journal.md",
        }
        for name, lesson in lessons.items():
            text = (ROOT / "learn" / "tracks" / lesson).read_text(encoding="utf-8")
            self.assertIn(f'{{% include lesson-visual.html key="{name}" %}}', text)

    def test_reviewed_copy_is_timeless(self):
        london = (ASSETS / "when-london-matters-step-4.svg").read_text(encoding="utf-8")
        sweep = (ASSETS / "the-sweep-that-isnt-step-4.svg").read_text(encoding="utf-8")
        self.assertNotIn("e.g. today", london)
        self.assertNotIn("fails most often", sweep)


if __name__ == "__main__":
    unittest.main()
