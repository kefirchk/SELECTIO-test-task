from netspeedometer import NetSpeedometer, IperfParser, ArgumentParser
import json


if __name__ == "__main__":

    arg_parser = ArgumentParser()
    args = arg_parser.get_args()
    password, option = arg_parser.get_password(args)

    try:
        netspeedometer = NetSpeedometer(host=args.host, user=args.user, password=password, option=option)
        output, error, returncode = netspeedometer.exec_iperf()

        parser = IperfParser(output, error, returncode)
        result = parser.parse()
        print(json.dumps(result, indent=4))

    except Exception as e:
        print(json.dumps({"error": str(e), "result": "", "status": 1}, indent=4))

