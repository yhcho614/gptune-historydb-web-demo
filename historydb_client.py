#!/usr/bin/env python

import requests
import json
import sys

#URL = "https://portal.nersc.gov/project/sparse/gptune/database/scalapack-pdqrdriver.json"
#URL = "http://127.0.0.1:8000/rest_api_test/"
URL = "http://localhost:8000/repo/upload_cli/"

def upload_data():
    with open(sys.argv[2], "r") as f_in:
        json_stream = json.loads(f_in.read())
        print (json_stream)
        res = requests.post(URL, data=json.dumps({
                "app_name":"123",
                "user_name":"younghyun",
                "perf_data":json_stream
            }))
        print (res)
    #res = requests.post(URL, data=json.dumps({"a":"b", "c":"d"}))

    return

def download_data():
    return

def main():

    if (sys.argv[1] == 'upload'):
        upload_data()
    elif (sys.argv[1] == 'download'):
        download_data()
    else:
        return

    return

def parse_args():

    parser = argparse.ArgumentParser()

    parser.add_argument('-method', type=str, default='none', help='Methods')
    parser.add_argument('-file', type=str, default='none', help='File')

    args = parser.parse_args()

    return args

if __name__ == "__main__":
    #res = requests.post(URL, data=json.dumps({
    #        "app_name":"scalapack-pdqrdriver",
    #        "user_name":"younghyun",
    #        "perf_data":"json"
    #    }))

    main()

