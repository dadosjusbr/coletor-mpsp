from parser import parse
import unittest
import json
from google.protobuf.json_format import MessageToDict
from data import load


class TestParser(unittest.TestCase):
    def test_jan_2018(self):
        self.maxDiff = None
        # Json com a saida esperada
        with open("src/output_test/expected/expected_01_2018.json", "r") as fp:
            expected_01_2018 = json.load(fp)

        files = ["src/output_test/sheets/membros-ativos-contracheque-01-2018.ods"]

        dados = load(files, "2018", "01")
        result_data = parse(dados, "mpsp/01/2018", 1, 2018)
        # Converto o resultado do parser, em dict
        result_to_dict = MessageToDict(result_data)
        self.assertEqual(expected_01_2018, result_to_dict)

    def test_jan_2019(self):
        self.maxDiff = None
        # Json com a saida esperada
        with open("src/output_test/expected/expected_01_2019.json", "r") as fp:
            expected_01_2019 = json.load(fp)

        files = ["src/output_test/sheets/membros-ativos-contracheque-01-2019.ods"]

        dados = load(files, "2019", "01")
        result_data = parse(dados, "mpsp/01/2019", 1, 2019)
        # Converto o resultado do parser, em dict
        result_to_dict = MessageToDict(result_data)
        self.assertEqual(expected_01_2019, result_to_dict)

    def test_fev_2019(self):
        self.maxDiff = None
        # Json com a saida esperada
        with open("src/output_test/expected/expected_02_2019.json", "r") as fp:
            expected_02_2019 = json.load(fp)

        files = ["src/output_test/sheets/membros-ativos-contracheque-02-2019.ods"]

        dados = load(files, "2019", "02")
        result_data = parse(dados, "mpsp/02/2019", 2, 2019)
        # Converto o resultado do parser, em dict
        result_to_dict = MessageToDict(result_data)
        self.assertEqual(expected_02_2019, result_to_dict)

    def test_jun_2019(self):
        self.maxDiff = None
        # Json com a saida esperada
        with open("src/output_test/expected/expected_06_2019.json", "r") as fp:
            expected_06_2019 = json.load(fp)

        files = ["src/output_test/sheets/membros-ativos-contracheque-06-2019.ods"]

        dados = load(files, "2019", "06")
        result_data = parse(dados, "mpsp/06/2019", 6, 2019)
        # Converto o resultado do parser, em dict
        result_to_dict = MessageToDict(result_data)
        self.assertEqual(expected_06_2019, result_to_dict)

    def test_jul_2019(self):
        self.maxDiff = None
        # Json com a saida esperada
        with open("src/output_test/expected/expected_07_2019.json", "r") as fp:
            expected_07_2019 = json.load(fp)

        files = ["src/output_test/sheets/membros-ativos-contracheque-07-2019.ods",
        "src/output_test/sheets/membros-ativos-verbas-indenizatorias-07-2019.ods"]

        dados = load(files, "2019", "07")
        result_data = parse(dados, "mpsp/07/2019", 7, 2019)
        # Converto o resultado do parser, em dict
        result_to_dict = MessageToDict(result_data)
        self.assertEqual(expected_07_2019, result_to_dict)

    def test_out_2020(self):
        self.maxDiff = None
        # Json com a saida esperada
        with open("src/output_test/expected/expected_10_2020.json", "r") as fp:
            expected_10_2020 = json.load(fp)

        files = ["src/output_test/sheets/membros-ativos-contracheque-10-2020.ods",
        "src/output_test/sheets/membros-ativos-verbas-indenizatorias-10-2020.ods"]

        dados = load(files, "2020", "10")
        result_data = parse(dados, "mpsp/10/2020", 10, 2020)
        # Converto o resultado do parser, em dict
        result_to_dict = MessageToDict(result_data)
        self.assertEqual(expected_10_2020, result_to_dict)

    def test_jan_2021(self):
        self.maxDiff = None
        # Json com a saida esperada
        with open("src/output_test/expected/expected_01_2021.json", "r") as fp:
            expected_01_2021 = json.load(fp)

        files = ["src/output_test/sheets/membros-ativos-contracheque-01-2021.ods",
        "src/output_test/sheets/membros-ativos-verbas-indenizatorias-01-2021.ods"]

        dados = load(files, "2021", "01")
        result_data = parse(dados, "mpsp/01/2021", 1, 2021)
        # Converto o resultado do parser, em dict
        result_to_dict = MessageToDict(result_data)
        self.assertEqual(expected_01_2021, result_to_dict)

    def test_fev_2021(self):
        self.maxDiff = None
        # Json com a saida esperada
        with open("src/output_test/expected/expected_02_2021.json", "r") as fp:
            expected_02_2021 = json.load(fp)

        files = ["src/output_test/sheets/membros-ativos-contracheque-02-2021.ods",
        "src/output_test/sheets/membros-ativos-verbas-indenizatorias-02-2021.ods"]

        dados = load(files, "2021", "02")
        result_data = parse(dados, "mpsp/02/2021", 2, 2021)
        # Converto o resultado do parser, em dict
        result_to_dict = MessageToDict(result_data)
        self.assertEqual(expected_02_2021, result_to_dict)

    def test_mar_2021(self):
        self.maxDiff = None
        # Json com a saida esperada
        with open("src/output_test/expected/expected_03_2021.json", "r") as fp:
            expected_03_2021 = json.load(fp)

        files = ["src/output_test/sheets/membros-ativos-contracheque-03-2021.ods",
        "src/output_test/sheets/membros-ativos-verbas-indenizatorias-03-2021.ods"]

        dados = load(files, "2021", "03")
        result_data = parse(dados, "mpsp/03/2021", 3, 2021)
        # Converto o resultado do parser, em dict
        result_to_dict = MessageToDict(result_data)
        self.assertEqual(expected_03_2021, result_to_dict)

    def test_jun_2021(self):
        self.maxDiff = None
        # Json com a saida esperada
        with open("src/output_test/expected/expected_06_2021.json", "r") as fp:
            expected_06_2021 = json.load(fp)

        files = ["src/output_test/sheets/membros-ativos-contracheque-06-2021.ods",
        "src/output_test/sheets/membros-ativos-verbas-indenizatorias-06-2021.ods"]

        dados = load(files, "2021", "06")
        result_data = parse(dados, "mpsp/06/2021", 6, 2021)
        # Converto o resultado do parser, em dict
        result_to_dict = MessageToDict(result_data)
        self.assertEqual(expected_06_2021, result_to_dict)

if __name__ == "__main__":
    unittest.main()
