import tempfile
import unittest

from stats import month_totals


class MonthTotals(unittest.TestCase):
    def test_sums_a_month(self):
        with tempfile.NamedTemporaryFile("w", suffix=".csv", delete=False) as f:
            f.write("date,amount\n2026-09-01,10\n2026-09-15,5\n")
        self.assertEqual(month_totals(f.name), {"2026-09": 15.0})


if __name__ == "__main__":
    unittest.main()
