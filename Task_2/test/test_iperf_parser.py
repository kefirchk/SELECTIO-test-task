import unittest
from Task_2.netspeedometer.parser_module.iperf_parser import IperfParser


class TestIperfParser(unittest.TestCase):
    def test_parse_success(self):
        outs = '{"some_key": "some_value"}'
        parser = IperfParser(outs, "", 0)
        parsed_result = parser.parse()
        self.assertEqual(parsed_result["error"], "")
        self.assertEqual(parsed_result["result"], {"some_key": "some_value"})
        self.assertEqual(parsed_result["status"], 0)

    def test_parse_failure(self):
        errs = "Error occurred during parsing"
        parser = IperfParser("", errs, 1)
        parsed_result = parser.parse()
        self.assertEqual(parsed_result["error"], "Error occurred during parsing")
        self.assertEqual(parsed_result["result"], "")
        self.assertEqual(parsed_result["status"], 1)


if __name__ == "__main__":
    unittest.main()
