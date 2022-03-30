#!/usr/bin/env python
# coding: utf-8
# This is a python nmap scanner. 
'''
Project 2 03/2022
@Witch_Sec
https://github.com/miss-anthrope
'''
import nmap
import sys

print("Welcome to the Python Nmap port scanner! Please check out the source code for the whole list of ports that are touched by this string.")
print("\nPlease note: This code only accepts IPv4.")
target=str(sys.argv[1])
ports=[21,22,23,80,443,110,995,143,993,25,26,587,3306,2082,2083,2086,2087,2095,8080,8081,3527,6101,6106,13724,1556,10102,53,123,389,445,2595,3389,8005]

scan_v=nmap.PortScanner()

print("\nStandby. Scanning ",target," for an entire buttload of interesting ports...\n")

for port in ports:
	portscan=scan_v.scan(target,str(port))
	print("Port",port," is ",portscan['scan'][target]['tcp'][port]['state'])

print("\nHost",target," is ",portscan['scan'][target]['status']['state'])
print("\nSnazzy!")
