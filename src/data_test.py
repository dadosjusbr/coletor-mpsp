from data import load
import unittest

file_names = [
    "src/output_test/sheets/membros-ativos-contracheque-02-2021.ods",
    "src/output_test/sheets/membros-ativos-verbas-indenizatorias-02-2021.ods",
]


class TestData(unittest.TestCase):
    def test_validate_existence(self):
        STATUS_DATA_UNAVAILABLE = 4
        with self.assertRaises(SystemExit) as cm:
            dados = load(file_names, "2021", "01")
            dados.validate("./output")
        self.assertEqual(cm.exception.code, STATUS_DATA_UNAVAILABLE)


if __name__ == "__main__":
    unittest.main()
