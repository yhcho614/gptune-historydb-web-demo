#!/usr/bin/env python

import requests
import json

#URL = "https://portal.nersc.gov/project/sparse/gptune/database/scalapack-pdqrdriver.json"
#URL = "http://127.0.0.1:8000/rest_api_test/"
URL = "http://localhost:8000/repo/upload_cli/"

if __name__ == "__main__":
    #res = requests.get(URL)
    #print (res.text)
    res = requests.post(URL, data=json.dumps({
            "app_name":"scalapack-pdqrdriver",
            "user_name":"younghyun",
            "perf_data":"json"
        }))
    #res = requests.post(URL, data=json.dumps({"a":"b", "c":"d"}))
    print (res)
