#!/usr/bin/python
# -*- coding:utf-8 -*-
# @auther    : jinhui
# @dateTime  : 2025-08-22
# @function  : 运行文件
# @version   : V1.0

import sys
from handle_command_func import Handle_command

def run_command():

	try:
		handle_cmd = Handle_command()
		cmd = sys.argv[1].strip()
		cmd_ls = [value for value in handle_cmd.cmd_dict.values()]
		if cmd in cmd_ls:
			handle_cmd.command_exec(cmd=cmd)
			sys.exit(0)
		else:
			raise ValueError

	except Exception as e:
		print(e)
		return handle_cmd.command_exec(cmd='1')
		sys.exit(0)

if __name__ == '__main__':
	run_command()





