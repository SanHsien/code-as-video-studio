"""範例與示範頁的契約：README 指令拿來就能跑、示範頁遵守 V = f(t)。"""

import re
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))

from verify_video_storyboard import evaluate_storyboard, load_keyframes_from_json  # noqa: E402

DEMO = ROOT / "assets" / "openlibrary_demo" / "video_seek_canvas.html"
SEEK_DEF = re.compile(r"function\s+seek\s*\(|(?:window\.|const\s+|let\s+)seek\s*=\s*(?:function|\()")
NONDETERMINISTIC = re.compile(r"Math\.random\s*\(|Date\.now\s*\(|performance\.now\s*\(|new\s+Date\s*\(")


def _strip_js_comments(code: str) -> str:
    code = re.sub(r"/\*[\s\S]*?\*/", "", code)
    return re.sub(r"(?m)^[ \t]*//.*$", "", code)


class StoryboardExampleTest(unittest.TestCase):
    def test_example_passes_the_gate(self):
        frames = load_keyframes_from_json(ROOT / "templates" / "storyboard-example.json")
        self.assertTrue(8 <= len(frames) <= 12)
        report = evaluate_storyboard(frames)
        self.assertTrue(report.gate_passed, report.summary)


class SeekDemoTest(unittest.TestCase):
    def setUp(self):
        self.code = _strip_js_comments(DEMO.read_text(encoding="utf-8"))

    def test_demo_defines_seek(self):
        self.assertRegex(self.code, SEEK_DEF)

    def test_demo_is_deterministic(self):
        # 畫面只能由 t 決定，否則無法逐格重現與檢查（AGENTS.md 鐵律 1）
        self.assertIsNone(NONDETERMINISTIC.search(self.code))

    def test_checks_catch_violations(self):
        self.assertNotRegex(_strip_js_comments("<script>/* function seek(t){} */</script>"), SEEK_DEF)
        self.assertRegex(_strip_js_comments("<script>window.seek = function(t){}</script>"), SEEK_DEF)
        self.assertRegex("x = Math.random();", NONDETERMINISTIC)


if __name__ == "__main__":
    unittest.main()
