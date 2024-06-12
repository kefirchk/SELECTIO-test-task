from netspeedometer import NetSpeedometer, IperfParser, ArgumentParser
import json


if __name__ == "__main__":
    args = ArgumentParser.get_args()
    try:
        netspeedometer = NetSpeedometer(net_args=args)
        output, error, returncode = netspeedometer.exec_iperf()

        parser = IperfParser(output, error, returncode)
        result = parser.parse()
        print(json.dumps(result, indent=4))

    except Exception as e:
        print(json.dumps({"error": str(e), "result": "", "status": 1}, indent=4))

