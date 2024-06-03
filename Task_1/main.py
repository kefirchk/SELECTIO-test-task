import argparse
import json
from source import DFExecuter

def get_args():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument('--human', action='store_true', help='execute and parse linux system command "df -h"')
    group.add_argument('--inode', action='store_true', help='execute and parse linux system command "df -i"')
    return parser.parse_args()


def main(): 
    args = get_args()
   
    try:
        df_executer = DFExecuter(args)
        result = df_executer.execute()
        print(json.dumps({"status": "success", "error": "None", "result": result}, indent=4))
    except Exception as e:
        print(json.dumps({"status": "failure", "error": str(e), "result": "None"}, indent=4))


if __name__ == '__main__':
    main()