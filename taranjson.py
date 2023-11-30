#! /usr/bin/env python3
"""
Parse the data returned by taran api json
"""
import requests
import json
import rich
import time

from rich.progress import Progress
from rich import print as rprint
from sites import sites
from time import sleep


blank = "                                         "

def qqapi(qq):
	url = sites[0] + qq
	response = requests.get(url)
	return res(response)

def qqphone(phone):
        url = sites[1] + phone
        response = requests.get(url)
        return res(response)

def qqlol(qq):
	url = sites[2] + qq
	response = requests.get(url)
	return res(response)

def lolname(name):
        url = sites[3] + name
        response = requests.get(url)
        return res(response)

def wbapi(id):
        url = sites[4] + id
        response = requests.get(url)
        return res(response)

def wbphone(phone):
        url = sites[5] + phone
        response = requests.get(url)
        return res(response)

def res(response):
	if response.status_code == 200:
		json_data = response.json()
		return json_data
	else:
		return response.status_code

def qqapi_progress():
	qq = input("[+] Please input Tencent number:")
	with Progress() as progress:
		task = progress.add_task("[bright_red][+] Searching ", total=None)
		data = qqapi(qq)
	if data != None:
		message = data["message"]
		if message == "查询成功":
			phone = data["phone"]
			qq = data["qq"]
			phonediqu = data["phonediqu"]
			search_true()
			rprint(f"[red][+] Phone number: {phone}")
			rprint(f"[red][+] Tencent number: {qq}")
			rprint(f"[red][+] Location: {phonediqu}")
		else:
			search_false()
	else:
		rprint("[-] Request failed，status code：", data)

def qqphone_progress():
	phone = input("[+] Please input phone number:")
	with Progress() as progress:
		task = progress.add_task("[bright_red][+] Searching ", total=None)
		data = qqphone(phone)
	if data != None:
		message = data["message"]
		if message == "查询成功":
			qq = data["qq"]
			phonediqu = data["phonediqu"]
			search_true()
			rprint(f"[red][+] Phone number: {phone}")
			rprint(f"[red][+] Tencent number: {qq}")
			rprint(f"[red][+] Location: {phonediqu}")
		else:
			search_false()
	else:
		rprint("[-] Request failed，status code：", data)

def qqlol_progress():
	qq = input("[+] Please input Tencent number:")
	with Progress() as progress:
		task = progress.add_task("[bright_red][+] Searching ", total=None)
		data = qqlol(qq)
	if data != None:
		message = data["message"]
		if message == "查询成功":
			qq = data["qq"]
			name = data["name"]
			daqu = data["daqu"]
			search_true()
			rprint(f"[red][+] Tencent number: {qq}")
			rprint(f"[red][+] LOL Game name: {name}")
			rprint(f"[red][+] Game location: {daqu}")
		else:
			search_false()
	else:
		rprint("[-] Request failed，status code：", data)

def lolname_progress():
	name = input("[+] Please input lol game name:")
	with Progress() as progress:
		task = progress.add_task("[bright_red][+] Searching ", total=None)
		data = lolname(name)
	if data != None:
		message = data["message"]
		if message == "查询成功":
			qq = data["qq"]
			name = data["name"]
			daqu = data["daqu"]
			rprint(f"[red][+] Tencent number: {qq}")
			rprint(f"[red][+] LOL Game name: {name}")
			rprint(f"[red][+] Game location: {daqu}")
		else:
			search_false()
	else:
		rprint("[-] Request failed，status code：", data)

def wbapi_progress():
	id = input("[+] Please input WB ID:")
	with Progress() as progress:
		task = progress.add_task("[bright_red][+] Searching ", total=None)
		data = wbapi(id)
	if data != None:
		message = data["message"]
		if message == "查询成功":
			id = data["id"]
			phone = data["phone"]
			phonediqu = data["phonediqu"]
			search_true()
			rprint(f"[red][+] Phone number: {phone}")
			rprint(f"[red][+] WB ID: {id}")
			rprint(f"[red][+] Location: {phonediqu}")
		else:
			search_false()
	else:
		rprint("[-] Request failed，status code：", data)

def wbphone_progress():
	phone = input("[+] Please input WB phone:")
	with Progress() as progress:
		task = progress.add_task("[bright_red][+] Searching ", total=None)
		data = wbphone(phone)
	if data != None:
		message = data["message"]
		if message == "查询成功":
			id = data["id"]
			phone = data["phone"]
			phonediqu = data["phonediqu"]
			search_true()
			rprint(f"[red][+] Phone number: {phone}")
			rprint(f"[red][+] WB ID: {id}")
			rprint(f"[red][+] Location: {phonediqu}")
		else:
			search_false()
	else:
		rprint("[-] Request failed，status code：", data)

def search_true():
	rprint("[red]//")
	rprint("")
	animation("Status code: 200")
	rprint("")
	rprint(f"[on red][black bold]SEARCH RESULT:{blank}")
	rprint("")
	rprint("[red]//")

def search_false():
	rprint("[red]//")
	rprint("")
	animation("Status code: 500")
	rprint("")
	rprint(f"[on red][black bold]SEARCH FAILED!{blank}")
	rprint("")
	rprint("[red]//")

def animation(text):
        for char in text:
                rprint(f"[red]{char}", end='', flush=True)
                sleep(0.02)

if __name__ == "__main__":
	print()
