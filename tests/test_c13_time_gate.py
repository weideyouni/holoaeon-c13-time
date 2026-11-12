# -*- coding: utf-8 -*-
"""C13 仓骨架测试（同构断言——S1/S2 结构与接口同构的可测实现）。"""
import json
import os
import subprocess
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(
    os.path.abspath(__file__))))

from holoaeon_c13_time.c13_time_gate import (  # noqa: E402
    CANG_ID, CHAIN, DOMAIN, HORSE, PHASE_MAIN, PHASE_SUB, QUESTION, REPO,
    ROLE, SEAL, TURTLE, fingerprint, probe)


class TestCangGate(unittest.TestCase):

    def test_probe_ok(self):
        self.assertTrue(probe()["ok"])

    def test_identity_fields(self):
        self.assertEqual(CANG_ID, "C13")
        self.assertEqual(REPO, "holoaeon-c13-time")
        self.assertEqual(DOMAIN, "时间")
        self.assertTrue(QUESTION)

    def test_turtle_horse_split(self):
        self.assertTrue("保存" in TURTLE or "记录" in TURTLE)
        self.assertTrue("推演" in HORSE or "生成" in HORSE)

    def test_n19_anchor_declared(self):
        self.assertIn("holoaeon", CHAIN["n19_anchor"])
        self.assertEqual(CHAIN["ring"], 19)

    def test_seal(self):
        self.assertEqual(SEAL, "潮起开门，潮落闭嘴")

    def test_cli_probe(self):
        r = subprocess.run(
            [sys.executable, "-m", "holoaeon_c13_time.c13_time_gate", "probe"],
            capture_output=True, text=True,
            cwd=os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertTrue(json.loads(r.stdout)["ok"])


if __name__ == "__main__":
    unittest.main()
