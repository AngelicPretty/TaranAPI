#! /usr/bin/env python3
"""
Taran: Phene number & tencent & Weibo infomation across social media platforms.
"""
import configparser
import taranjson
import asyncio
import os

from taranui import Notify

async def main():

	choice = -1
	Notify.start()
	while choice != 0:
		os.system('cls' if os.name == 'nt' else 'clear')
		Notify.logo()
		print('Little Fish Taran API Tools 1.0')
		print('Copyright (C) Little Fish. All rights reserved.')
		print("______________________________________________________________")
		print('')
		print('[1] Search bind mobile phone number | Tencent number')
		print('[2] Search bind Tencent number | Mobile phone')
		print('[3] Search bind LOL Game info | Tencent number')
		print('[4] Search bind Tencent number | LOL username')
		print('[5] Search bind mobile phone number | Weibo ID')
		print('[6] Search bind Weibo ID | Mobile Phone')
		print('')
		print("______________________________________________________________")
		print('')
		print('[9] Read Me')
		print("[0] Exit")
		print('')
		print("______________________________________________________________")
		print('')
		try:
			choice = int(input("Enter a menu option in the Keyboard [0,1,2,3,4,5,6,9]: "))
		except ValueError:
			choice = -1
		if choice == 0:
			print('[+] Goodbye...')
		elif choice == 1:
			await bind_qqapi()
		elif choice == 2:
			await bind_qqphone()
		elif choice == 3:
			await bind_qqlol()
		elif choice == 4:
			await bind_lolname()
		elif choice == 5:
			await bind_wbapi()
		elif choice == 6:
			await bind_wbphone()
		else:
			print('[-] Invalid choice!\n')

async def bind_qqapi():
	os.system('cls' if os.name == 'nt' else 'clear')
	taranjson.qqapi_progress()
	print("[+] Press Enter key to continue")
	input()

async def bind_qqphone():
	os.system('cls' if os.name == 'nt' else 'clear')
	taranjson.qqphone_progress()
	print("[+] Press Enter key to continue")
	input()

async def bind_qqlol():
	os.system('cls' if os.name == 'nt' else 'clear')
	taranjson.qqlol_progress()
	print("[+] Press Enter key to continue")
	input()

async def bind_lolname():
	os.system('cls' if os.name == 'nt' else 'clear')
	taranjson.lolname_progress()
	print("[+] Press Enter key to continue")
	input()

async def qqlol():
	os.system('cls' if os.name == 'nt' else 'clear')
	taranjson.qqlol_progress()
	print("[+] Press Enter key to continue")
	input()

async def lolname():
	os.system('cls' if os.name == 'nt' else 'clear')
	taranjson.lolname_progress()
	print("[+] Press Enter key to continue")
	input()

async def bind_wbapi():
	os.system('cls' if os.name == 'nt' else 'clear')
	taranjson.wbapi_progress()
	print("[+] Press Enter key to continue")
	input()

async def bind_wbphone():
	os.system('cls' if os.name == 'nt' else 'clear')
	taranjson.wbphone_progress()
	print("[+] Press Enter key to continue")
	input()

# Run main
asyncio.run(main())
