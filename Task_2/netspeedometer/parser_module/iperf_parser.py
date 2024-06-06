import json

class IperfParser:
    def __init__(self, outs, errs, returncode):
        self.outs = outs
        self.errs = errs
        self.returncode = returncode

    def parse(self):
        if self.returncode == 0:
            result = json.loads(self.outs)
            return {"error": "", "result": result, "status": 0}
        else:
            return {"error": self.errs, "result": "", "status": self.returncode}