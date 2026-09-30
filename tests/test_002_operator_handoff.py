import unittest

from care_gap_prioritizer.models import Record
from care_gap_prioritizer.scoring import score_record


class DepthCheck2(unittest.TestCase):
    def test_002_operator_handoff(self):
        record = Record(id="member-002", exposure=77588, signal=0.435, urgency=1)
        self.assertGreaterEqual(score_record(record), 0)
        self.assertLessEqual(score_record(record), 1)


if __name__ == "__main__":
    unittest.main()
