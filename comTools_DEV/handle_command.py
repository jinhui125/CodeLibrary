# dateTime: 2025-04-06
# author: jinHui

import os
import re
import sys
import time
import signal
import datetime
import subprocess

command_dict = {
					'获取命令帮助信息': '1', '执行Record录像功能': '2', '获取当前panel-serve的PID号': '3', '获取当前panel-serve的内存占用': '4', '开启/关闭/重开远程': '5', 
					'获取一段时间内的panel-serve内存占用信息': '6', '切换车端环境': '7', '模拟事故场景改造': '8',
				}

def progress_bar(t, description):
	
	for i in range(1, 101):
		print("\r{}: {}%: ".format(description, i), "▋" * (i // 2), end="", flush=True)
		time.sleep(t/100)

def handle_signal(subprocess_obj, signal_flag, count = 1, text_description = "", wait_style = 'circle', delay_time = 0.25):
	wait_style_dict = {
						'circle': ['\\', '|', '/', '-'], 
						'columnar': ['▁', '▂', '▃', '▄', '▅', '▆', '▇', '█'],
						'poker': ['♠️ ', '♥️ ', '♦️ ', '♣️ '],
						'moon': ['🌕', '🌖', '🌗', '🌘', '🌑', '🌒', '🌓', '🌔'],
						'clock': ['🕛', '🕐', '🕑', '🕒', '🕓', '🕔', '🕕', '🕖', '🕗', '🕘', '🕙', '🕚'],
						# 'ellipsis': ['🂱', '🂲', '🂳', '🂴', '🂵', '🂶', '🂷', '🂸', '🂹', '🂺', '🂻', '🂼', '🂽', '🂾', '🂡', '🂢', '🂣', '🂤', '🂥', '🂦', '🂧', '🂨', '🂩', '🂪', 
						# 			'🂫', '🂬', '🂭', '🂮', '🃁', '🃂', '🃃', '🃄', '🃅', '🃆', '🃇', '🃈', '🃉', '🃊', '🃋', '🃌', '🃍', '🃎', '🃑', '🃒', '🃓', '🃔', '🃕', '🃖', 
						# 			'🃗', '🃘', '🃙', '🃚', '🃛', '🃜', '🃝', '🃞', '🃏']
						}
	
	print(f'执行开始时间: {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')

	while not signal_flag:
		try:
			count += 1
			print(f'\r{text_description}', f'{wait_style_dict[wait_style][count % len(wait_style_dict[wait_style])]}', end='', flush=True)
			time.sleep(delay_time)

		except KeyboardInterrupt:
			signal_flag = True
			os.killpg(os.getpgid(subprocess_obj.pid), signal.SIGKILL)
			subprocess_obj.wait()
			print('\n')
			sys.exit(0)
			break
			
		finally:
			pass

def string_format(string, way, width, fill=' '):

	count = 0
	for word in string:
		if (word >= '\u4e00' and word <= '\u9fa5') or word in ['；', '：', '，', '（', '）', '！', '？', '——', '……',
															   '、', '》', '《']:
			count += 1
	width = width-count if width >= count else 0
	return '{0:{1}{2}{3}}'.format(string, fill, way, width)


def table(col_ls: list, row_ls: list, l_width=50, r_width=3):

	title = [string_format(col_ls[0], '<', l_width, ' '),
			 string_format(col_ls[1], '<', l_width, ' ')]
	content_ls = []
	for row in row_ls:
		content_ls.append([string_format(row[0], '<', l_width, ' '),
						   string_format(row[1], '>', r_width, ' ')])
	result = f"{'|'.join(title)}\n"
	for content in content_ls:
		result += f"{'|'.join(content)}\n"
	return result


def replace_content(file, old_strs, new_strs, replace_mode = "replace", re_str = "", insert_index = ""):

	tmp_str = ''
	if bool(len(file)):
		with open(file=file, mode='r', encoding='utf-8') as fb:
			lines_ls = fb.readlines()
			for index in range(0, int(lines_ls.__len__())):
				for i in range(0, int(old_strs.__len__())):
					if old_strs[i] in lines_ls[index].strip():
						print(lines_ls[index])
						if replace_mode == "replace":
							lines_ls[index] = f'{new_strs[i]}\n'
						elif replace_mode == "modify":
							lines_ls[index] = replace_content(file='', old_strs=lines_ls[index], new_strs=new_strs[i], replace_mode=replace_mode, re_str=re_str[i])
						elif replace_mode == "append":
							lines_ls[index] = replace_content(file='', old_strs=lines_ls[index], new_strs=new_strs[i], replace_mode=replace_mode, insert_index=insert_index)
					else:
						continue

			for i in range(0, int(lines_ls.__len__())):
				tmp_str += lines_ls[i]

		with open(file=file, mode='w', encoding='utf-8') as fb:
			fb.write(tmp_str)
	else:
		tmp_list = []
		if replace_mode == 'modify':
			if re.search(pattern=re_str, string=old_strs):
				index_tmp = re.search(pattern=re_str, string=old_strs).span()
				tmp_list = [old_strs[0:index_tmp[0]], old_strs[index_tmp[0]:index_tmp[1]], old_strs[index_tmp[1]:]]
				print(tmp_list)
				tmp_list[1] = new_strs
			else:
				tmp_list.append(old_strs)

		elif replace_mode == 'append':
			if insert_index != 1:
				tmp_list = [old_strs[0:insert_index], old_strs[insert_index], old_strs[(insert_index+1):]]
			elif insert_index == len(old_strs):
				tmp_list.append(old_strs + new_strs)
			else:
				tmp_list.append(new_strs + old_strs)

		else:
			pass
		print(tmp_list)
		return "".join(tmp_list)

def handle_command(command: str, stdout=False):

	if not stdout:
		os.system(command)
	else:
		sp = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
		return sp.stdout.readlines()

def exec_command(command):

	if command == command_dict['获取命令帮助信息']:
		help_info = table(col_ls=['命令作用描述', '命令快捷编号'],
						  row_ls=[(key, value) for key, value in command_dict.items()])
		print(help_info)
		print('例子：python3.8 handle_command.py 1\n使用问题如流找：v_jinhui02')

	elif command == command_dict['执行Record录像功能']:
		input_time = int(input("请输入你想录制Record的时间(单位秒): ").strip())
		p = subprocess.Popen(args='cyber_recorder record -c /sensor/camera/obstacle/image_left_forward/'
								  'driverless_h265compressed /sensor/camera/obstacle/image_wide/'
								  'driverless_h265compressed /sensor/camera/obstacle/image_right_forward/'
								  'driverless_h265compressed /sensor/camera/obstacle/image_left_backward/'
								  'h264compressed /sensor/camera/obstacle/image_left_backward/'
								  'driverless_h265compressed /sensor/camera/obstacle/image_right_backward/'
								  'h264compressed /sensor/camera/obstacle/image_right_backward/'
								  'driverless_h265compressed /perception/obstacles_hmi /sensor/pandora/'
								  'hesai90/compensator/PointCloud2 /sensor/pandora/hesai40/compensator/'
								  'PointCloud2 /pnc/carstatus /patrol/status /perception/obstacles /'
								  'localization/100hz/localization_pose /pnc/planning /pnc/decision /pnc/'
								  'local_routing /sensor/novatel/bestgnsspos /perception/traffic_light_status /'
								  'perception/obstacles /pnc/planning_state /tf', shell=True, stdout=subprocess.PIPE,
								  start_new_session=True)
		current_time = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
		progress_bar(t=input_time, description='正在录制Record中...')
		os.killpg(os.getpgid(p.pid), signal.SIGINT)
		p.wait()
		print('Record录制完毕')
		rec_name = handle_command(command=f'ls | grep {current_time}.record', stdout=True)[0].strip()
		return handle_command(command=f'cyber_recorder info {rec_name}')

	elif command == 'GetHome_path':
		return os.environ['HOME']

	elif command == 'GetPWD_path':
		return handle_command('pwd')

	elif command == command_dict['获取当前panel-serve的PID号']:
		return handle_command(command="ps -aux | grep panel_server_sched | grep -v grep | awk '{print $2}'")

	elif command == command_dict['获取当前panel-serve的内存占用']:
		pid = handle_command(command="ps -aux | grep panel_server_sched | grep -v grep | awk '{print $2}'",
							 stdout=True)[0].strip()
		return handle_command(command=f"top -p {pid} -b -n 1 | grep {pid} | awk " + "'{print $6}'")

	elif command == command_dict['开启/关闭/重开远程']:
		remote_switch = input(f"开启/关闭远程(on: 开; off: 关; rst: 重新开启): ")
		if remote_switch == 'on':
			os.chdir(f'{exec_command("GetHome_path")}/cybertron/adtdp-debug-client')
			return handle_command(command='bash ./bin/control.sh start')

		elif remote_switch == 'off':
			os.chdir(f'{exec_command("GetHome_path")}/cybertron/adtdp-debug-client')
			return handle_command(command='bash ./bin/control.sh stop')

		elif remote_switch == 'rst':
			os.chdir(f'{exec_command("GetHome_path")}/cybertron/adtdp-debug-client')
			return handle_command(command='bash ./bin/control.sh restart')

	elif command == command_dict['获取一段时间内的panel-serve内存占用信息']:
		pid = handle_command(command="ps -aux | grep panel_server_sched | grep -v grep | awk '{print $2}'",
							 stdout=True)[0].strip()
		input_time = int(input("请输入你想获取多长时间内的性能变化(单位秒): ").strip())
		handle_command(f'sh mem_cpu.sh {pid} >mem_cpu.log 2>&1 &')
		time.sleep(2)
		progress_bar(t=input_time, description=f'正在计算{input_time}s内panel-serve的cpu性能...')
		print('\n' + string_format(f'panel-server在{input_time}s内的cpu和内存计算结果如下', '^', 100, '-'))
		return handle_command('sh cal.sh mem_cpu.log')

	elif command == command_dict['切换车端环境']:
		print(table(col_ls=["车端环境名称", "车端环境字段"], row_ls=[['QA测试环境', 'pre'], ['线上运营环境', 'online'],
																	 ['opn环境', 'opn'], ['test环境', 'test']], l_width=15, r_width=12))
		input_value = str(input('请输入你想将车端切换的环境名称: '))
		if input_value == 'pre':
			replace_content(file=f'{exec_command(command="GetHome_path")}/cybertron/bin/integration_config.py',
							old_strs=['host = '],
							new_strs=['host = "https://idgdatapre.baidu.com"'])
			replace_content(file=f'{exec_command(command="GetHome_path")}/cybertron/conf/robo_agent.conf',
							old_strs=['https_url_perfix:', 'hmi_customize_host:', 'mqtts_environment_switch:'],
							new_strs=['https_url_perfix:"https://cert-pre.baidu.com"',
									  'hmi_customize_host:"https://idgdatapre.baidu.com"',
									  'mqtts_environment_switch: 2'])
			replace_content(file=f'{exec_command(command="GetHome_path")}/otaclient/etc/otaclient.conf',
							old_strs=['mode = ', 'use = '],
							new_strs=['mode = pre', 'use = True'])
			replace_content(file=f'{exec_command(command="GetHome_path")}/otaclient/script/config_deploy.py',
							old_strs=['domain = '],
							new_strs=['idgops-pre'], replace_mode="modify", re_str=[r"idgops(-(opn|test|pre)?)?"])
			replace_content(file=f'{exec_command(command="GetHome_path")}/otaclient/script/config_deploy.py',
							old_strs=[r'url = "https://{}.baidu.com'],
							new_strs=['.format("idgops-pre")'], replace_mode="modify", re_str=[r".format\((domain|\"idgops-pre\"|\"idgops-opn\"|\"idgops-test\"|\"idgops\")?\)"])
			
		elif input_value == 'online' or input_value == 'opn':
			replace_content(file=f'{exec_command(command="GetHome_path")}/cybertron/bin/integration_config.py',
							old_strs=['host = '],
							new_strs=['host = "https://idgdata.baidu.com"'])
			replace_content(file=f'{exec_command(command="GetHome_path")}/cybertron/conf/robo_agent.conf',
							old_strs=['https_url_perfix:', 'hmi_customize_host:', 'mqtts_environment_switch:'],
							new_strs=['https_url_perfix:"https://cert-fleet.baidu.com"',
									  'hmi_customize_host:"https://idgdata.baidu.com"', 
									  'mqtts_environment_switch: 1'])
			if input_value == 'online':
				replace_content(file=f'{exec_command(command="GetHome_path")}/otaclient/etc/otaclient.conf',
								old_strs=['mode = ', 'use = '],
								new_strs=['mode = online', 'use = True'])
				replace_content(file=f'{exec_command(command="GetHome_path")}/otaclient/script/config_deploy.py',
								old_strs=['domain = '],
								new_strs=['idgops'], replace_mode="modify", re_str=[r"idgops(-(opn|test|pre)?)?"])
				replace_content(file=f'{exec_command(command="GetHome_path")}/otaclient/script/config_deploy.py',
							old_strs=[r'url = "https://{}.baidu.com'],
							new_strs=['.format("idgops")'], replace_mode="modify", re_str=[r".format\((domain|\"idgops-pre\"|\"idgops-opn\"|\"idgops-test\"|\"idgops\")?\)"])
			elif input_value == 'opn':
				replace_content(file=f'{exec_command(command="GetHome_path")}/otaclient/etc/otaclient.conf',
								old_strs=['mode = ', 'use = '],
								new_strs=['mode = opn', 'use = True'])
				replace_content(file=f'{exec_command(command="GetHome_path")}/otaclient/script/config_deploy.py',
								old_strs=['domain = '],
								new_strs=['idgops-opn'], replace_mode="modify", re_str=[r"idgops(-(opn|test|pre)?)?"])
				replace_content(file=f'{exec_command(command="GetHome_path")}/otaclient/script/config_deploy.py',
							old_strs=[r'url = "https://{}.baidu.com'],
							new_strs=['.format("idgops-opn")'], replace_mode="modify", re_str=[r".format\((domain|\"idgops-pre\"|\"idgops-opn\"|\"idgops-test\"|\"idgops\")?\)"])
				
		elif input_value == 'test':
			replace_content(file=f'{exec_command(command="GetHome_path")}/cybertron/bin/integration_config.py',
							old_strs=['host = '],
							new_strs=['host = "https://idgdatatest.baidu.com"'])
			replace_content(file=f'{exec_command(command="GetHome_path")}/cybertron/conf/robo_agent.conf',
							old_strs=['https_url_perfix:', 'hmi_customize_host:', 'mqtts_environment_switch:'],
							new_strs=['https_url_perfix:"https://cert-test.baidu.com"',
									  'hmi_customize_host:"https://idgdatatest.baidu.com"',
									  'mqtts_environment_switch: 3'])
			replace_content(file=f'{exec_command(command="GetHome_path")}/otaclient/etc/otaclient.conf',
							old_strs=['mode = ', 'use = '],
							new_strs=['mode = test', 'use = True'])
			replace_content(file=f'{exec_command(command="GetHome_path")}/otaclient/script/config_deploy.py',
								old_strs=['domain = '],
								new_strs=['idgops-test'], replace_mode="modify", re_str=[r"idgops(-(opn|test|pre)?)?"])
			replace_content(file=f'{exec_command(command="GetHome_path")}/otaclient/script/config_deploy.py',
							old_strs=[r'url = "https://{}.baidu.com'],
							new_strs=['.format("idgops-test")'], replace_mode="modify", re_str=[r".format\((domain|\"idgops-pre\"|\"idgops-opn\"|\"idgops-test\"|\"idgops\")?\)"])
			
		print(f"车端环境+OTA环境+获取驾驶能力套餐环境都已经切换到【{input_value}环境】\n")

		string_format(f'请在下面云舱代驾环境选项中选择"{input_value}"', '^', 100, '-')
		return handle_command(f'python {exec_command(command="GetHome_path")}/cybertron/bin/remote_control/change_remote_env.py')

	elif command == command_dict['模拟事故场景改造']:
		print(table(col_ls=['模拟事故场景', '模拟事故场景字段'], row_ls=[['自动驾驶异常—终点重启（1002）', '1'], ['传感器异常（1003）', '2'],
																	 ['自动驾驶严重异常-现场处置（1021）', '3'], ['传感器严重异常（1022）', '4'], 
																	 ['nvme严重异常（1023）', '5'], ['轮胎异常（1004）', '6'], ['轮胎严重异常（1026）', '7'],
																	 ['交通事故', '8']], l_width=35, r_width=8))
		input_value = input('请输入你想触发的事故场景: ').strip()
		tmp_time = 0
		flag = False
		if input_value == '1':
			p = subprocess.Popen(args=f'python module_error_mock.py 2 254 "error"', shell=True, stdout=subprocess.DEVNULL,
								  stderr=subprocess.DEVNULL, start_new_session=True)
			handle_signal(subprocess_obj=p, signal_flag=False, text_description = "事故场景模拟中", wait_style='moon', delay_time=0.125)

		elif input_value == '2':
			p = subprocess.Popen(args=f'python module_error_mock.py 1 119 "error"', shell=True, stdout=subprocess.DEVNULL,
								  stderr=subprocess.DEVNULL, start_new_session=True)
			handle_signal(subprocess_obj=p, signal_flag=False, text_description = "事故场景模拟中", wait_style='poker')

		elif input_value == '3':
			p = subprocess.Popen(args=f'python module_error_mock.py 2 243 "error"', shell=True, stdout=subprocess.DEVNULL,
								  stderr=subprocess.DEVNULL, start_new_session=True)
			handle_signal(subprocess_obj=p, signal_flag=False, text_description = "事故场景模拟中", wait_style='columnar')

		elif input_value == '4':
			p = subprocess.Popen(args=f'python module_error_mock.py 1 213 "error"', shell=True, stdout=subprocess.DEVNULL,
								  stderr=subprocess.DEVNULL, start_new_session=True)
			handle_signal(subprocess_obj=p, signal_flag=False, text_description = "事故场景模拟中", wait_style='circle')

		elif input_value == '5':
			p = subprocess.Popen(args=f'python module_error_mock.py 6 700 "error"', shell=True, stdout=subprocess.DEVNULL,
								  stderr=subprocess.DEVNULL, start_new_session=True)
			handle_signal(subprocess_obj=p, signal_flag=False, text_description = "事故场景模拟中", wait_style='clock', delay_time=0.125)

		elif input_value == '6' or input_value == '7' or input_value == '8':
			print(f'{table(col_ls=["制造/恢复故障", "选择字段"], row_ls=[["制造故障", "1"], ["恢复故障", "2"]], l_width=12, r_width=4)}')
			is_fault = input('请选择是制造故障还是恢复故障: ')
			print(f'{table(col_ls=["车辆型号", "型号字段"], row_ls=[["RT5", "1"], ["RT6", "2"]], l_width=12, r_width=4)}')
			car_type = input('请输入你想触发事故模拟的车辆类型: ')
			if is_fault == '1':
				if car_type == '1':
					if input_value == '6':
						replace_content(file=f'{exec_command(command="GetHome_path")}/cybertron/conf/patrol/patrol_checker_agent.conf', 
							old_strs=['fileexist_items { item_code: 1304241'],
							new_strs=['3100823'], replace_mode='modify', re_str=[r"1304241"])
						replace_content(file=f'{exec_command(command="GetHome_path")}/cybertron/conf/patrol/patrol_erritems_merge.conf',
							old_strs=['erritems {item_code: 1304241'],
							new_strs=['#'], replace_mode='append', insert_index=1)
						handle_command(f'scp {exec_command(command="GetHome_path")}/cybertron/conf/patrol/patrol_erritems_merge.conf caros@192.168.10.8:/home/caros/cybertron/conf/patrol')
						print(f'请【下电重启车辆】或者【重启计算和安全的patrol进程】，让修改功能生效!')
						print(f'构造故障请在计算节点输入这个命令: mv /home/caros/cybertron/params/onsemi_wide_extrinsics.yaml /home/caros/cybertron/params/onsemi_wide_extrinsics.yaml.bk')
						print(f'恢复故障请在计算节点输入这个命令: mv /home/caros/cybertron/params/onsemi_wide_extrinsics.yaml.bk /home/caros/cybertron/params/onsemi_wide_extrinsics.yaml')
					elif input_value == '7':
						replace_content(file=f'{exec_command(command="GetHome_path")}/cybertron/conf/patrol/patrol_checker_agent.conf', 
							old_strs=['fileexist_items { item_code: 1304231'],
							new_strs=['3100411'], replace_mode='modify', re_str=[r"1304231"])
						replace_content(file=f'{exec_command(command="GetHome_path")}/cybertron/conf/patrol/patrol_erritems_merge.conf',
							old_strs=['erritems {item_code: 1304231'],
							new_strs=['#'], replace_mode='append', insert_index=1)
						handle_command(f'scp {exec_command(command="GetHome_path")}/cybertron/conf/patrol/patrol_erritems_merge.conf caros@192.168.10.8:/home/caros/cybertron/conf/patrol')
						print(f'请【下电重启车辆】或者【重启计算和安全的patrol进程】，让修改功能生效!')
						print(f'构造故障请在计算节点输入这个命令: mv /home/caros/cybertron/params/onsemi_narrow_extrinsics.yaml /home/caros/cybertron/params/onsemi_narrow_extrinsics.yaml.bk')
						print(f'恢复故障请在计算节点输入这个命令: mv /home/caros/cybertron/params/onsemi_narrow_extrinsics.yaml.bk /home/caros/cybertron/params/onsemi_narrow_extrinsics.yaml')
					elif input_value == '8':
						replace_content(file=f'{exec_command(command="GetHome_path")}/cybertron/conf/patrol/patrol_checker_agent.conf', 
							old_strs=['fileexist_items { item_code: 1304126,', 'item_code: 1705003'],
							new_strs=['1705003', '1304126\n'], replace_mode='modify', re_str=[r"1304126", r"(1705003)[^( #事故)|^(,)]"])
						print(f'请【下电重启车辆】或者【重启计算的patrol进程】，让修改功能生效!')
						print(f'构造故障请在计算节点输入这个命令: mv /home/caros/cybertron/params/hesai90_height.yaml /home/caros/cybertron/params/hesai90_height.yaml_1')
						print(f'恢复故障请在计算节点输入这个命令: mv /home/caros/cybertron/params/hesai90_height.yaml_1 /home/caros/cybertron/params/hesai90_height.yaml')
					else:
						pass
				elif car_type == '2':
					if input_value == '6':
						replace_content(file=f'{exec_command(command="GetHome_path")}/cybertron/conf/patrol/patrol_checker_agent_rt6.conf', 
							old_strs=['fileexist_items { item_code: 1304241'],
							new_strs=['3100823'], replace_mode='modify', re_str=[r"1304241"])
						replace_content(file=f'{exec_command(command="GetHome_path")}/cybertron/conf/patrol/patrol_erritems_merge_rt6.conf',
							old_strs=['erritems {item_code: 1304241'],
							new_strs=['#'], replace_mode='append', insert_index=1)
						handle_command(f'scp {exec_command(command="GetHome_path")}/cybertron/conf/patrol/patrol_erritems_merge_rt6.conf caros@192.168.4.8:/home/caros/cybertron/conf/patrol')
						print(f'请【下电重启车辆】或者【重启计算和安全的patrol进程】，让修改功能生效!')
						print(f'构造故障请在计算节点输入这个命令: mv /home/caros/cybertron/params/onsemi_wide_extrinsics.yaml /home/caros/cybertron/params/onsemi_wide_extrinsics.yaml.bk')
						print(f'恢复故障请在计算节点输入这个命令: mv /home/caros/cybertron/params/onsemi_wide_extrinsics.yaml.bk /home/caros/cybertron/params/onsemi_wide_extrinsics.yaml')
					elif input_value == '7':
						replace_content(file=f'{exec_command(command="GetHome_path")}/cybertron/conf/patrol/patrol_checker_agent_rt6.conf', 
							old_strs=['fileexist_items { item_code: 1304231'],
							new_strs=['3100411'], replace_mode='modify', re_str=[r"1304231"])
						replace_content(file=f'{exec_command(command="GetHome_path")}/cybertron/conf/patrol/patrol_erritems_merge_rt6.conf',
							old_strs=['erritems {item_code: 1304231'],
							new_strs=['#'], replace_mode='append', insert_index=1)
						handle_command(f'scp {exec_command(command="GetHome_path")}/cybertron/conf/patrol/patrol_erritems_merge_rt6.conf caros@192.168.4.8:/home/caros/cybertron/conf/patrol')
						print(f'请【下电重启车辆】或者【重启计算和安全的patrol进程】，让修改功能生效!')
						print(f'构造故障请在计算节点输入这个命令: mv /home/caros/cybertron/params/onsemi_narrow_extrinsics.yaml /home/caros/cybertron/params/onsemi_narrow_extrinsics.yaml.bk')
						print(f'恢复故障请在计算节点输入这个命令: mv /home/caros/cybertron/params/onsemi_narrow_extrinsics.yaml.bk /home/caros/cybertron/params/onsemi_narrow_extrinsics.yaml')
					elif input_value == '8':
						replace_content(file=f'{exec_command(command="GetHome_path")}/cybertron/conf/patrol/patrol_checker_agent_rt6.conf', 
							old_strs=['fileexist_items { item_code: 1304241,', 'item_code: 1705003'],
							new_strs=['1705003', '1304241\n'], replace_mode='modify', re_str=[r"1304241", r"(1705003)[^( #事故)|^(,)]"])
						print(f'请【下电重启车辆】或者【重启计算的patrol进程】，让修改功能生效!')
						print(f'构造故障请在计算节点输入这个命令: mv /home/caros/cybertron/params/onsemi_wide_extrinsics.yaml /home/caros/cybertron/params/onsemi_wide_extrinsics.yaml_1')
						print(f'恢复故障请在计算节点输入这个命令: mv /home/caros/cybertron/params/onsemi_wide_extrinsics.yaml_1 /home/caros/cybertron/params/onsemi_wide_extrinsics.yaml')
					else:
						pass
				else:
					pass
			elif is_fault == '2':
				if car_type == '1':
					if input_value == '6':
						replace_content(file=f'{exec_command(command="GetHome_path")}/cybertron/conf/patrol/patrol_checker_agent.conf', 
							old_strs=['fileexist_items { item_code: 3100823'],
							new_strs=['1304241'], replace_mode='modify', re_str=[r"3100823"])
						replace_content(file=f'{exec_command(command="GetHome_path")}/cybertron/conf/patrol/patrol_erritems_merge.conf',
							old_strs=['erritems {item_code: 1304241'],
							new_strs=[''], replace_mode='modify', re_str=[r"#"])
						handle_command(f'scp {exec_command(command="GetHome_path")}/cybertron/conf/patrol/patrol_erritems_merge.conf caros@192.168.10.8:/home/caros/cybertron/conf/patrol')
						print(f'请【下电重启车辆】或者【重启计算和安全的patrol进程】，让修改功能生效!')
					elif input_value == '7':
						replace_content(file=f'{exec_command(command="GetHome_path")}/cybertron/conf/patrol/patrol_checker_agent.conf', 
							old_strs=['fileexist_items { item_code: 3100411'],
							new_strs=['1304231'], replace_mode='modify', re_str=[r"3100411"])
						replace_content(file=f'{exec_command(command="GetHome_path")}/cybertron/conf/patrol/patrol_erritems_merge.conf',
							old_strs=['erritems {item_code: 1304231'],
							new_strs=[''], replace_mode='modify', re_str=[r"#"])
						handle_command(f'scp {exec_command(command="GetHome_path")}/cybertron/conf/patrol/patrol_erritems_merge.conf caros@192.168.10.8:/home/caros/cybertron/conf/patrol')
						print(f'请【下电重启车辆】或者【重启计算和安全的patrol进程】，让修改功能生效!')
					elif input_value == '8':
						replace_content(file=f'{exec_command(command="GetHome_path")}/cybertron/conf/patrol/patrol_checker_agent.conf', 
							old_strs=['fileexist_items { item_code: 1705003,', 'item_code: 1304126'],
							new_strs=['1304126', '1705003\n'], replace_mode='modify', re_str=[r"1705003", r"(1304126)[^( #事故)|^(,)]"])
						print(f'请【下电重启车辆】或者【重启计算的patrol进程】，让修改功能生效!')
					else:
						pass
				elif car_type == '2':
					if input_value == '6':
						replace_content(file=f'{exec_command(command="GetHome_path")}/cybertron/conf/patrol_checker_agent_rt6.conf', 
							old_strs=['fileexist_items { item_code: 3100823'],
							new_strs=['1304241'], replace_mode='modify', re_str=[r"3100823"])
						replace_content(file=f'{exec_command(command="GetHome_path")}/cybertron/conf/patrol_erritems_merge_rt6.conf',
							old_strs=['erritems {item_code: 1304241'],
							new_strs=[''], replace_mode='modify', re_str=[r"#"])
						handle_command(f'scp {exec_command(command="GetHome_path")}/cybertron/conf/patrol/patrol_erritems_merge_rt6.conf caros@192.168.4.8:/home/caros/cybertron/conf/patrol')
						print(f'请【下电重启车辆】或者【重启计算和安全的patrol进程】，让修改功能生效!')
					elif input_value == '7':
						replace_content(file=f'{exec_command(command="GetHome_path")}/cybertron/conf/patrol/patrol_checker_agent_rt6.conf', 
							old_strs=['fileexist_items { item_code: 3100411'],
							new_strs=['1304231'], replace_mode='modify', re_str=[r"3100411"])
						replace_content(file=f'{exec_command(command="GetHome_path")}/cybertron/conf/patrol/patrol_erritems_merge_rt6.conf',
							old_strs=['erritems {item_code: 1304231'],
							new_strs=[''], replace_mode='modify', re_str=[r"#"])
						handle_command(f'scp {exec_command(command="GetHome_path")}/cybertron/conf/patrol/patrol_erritems_merge_rt6.conf caros@192.168.4.8:/home/caros/cybertron/conf/patrol')
						print(f'请【下电重启车辆】或者【重启计算和安全的patrol进程】，让修改功能生效!')
					elif input_value == '8':
						replace_content(file=f'{exec_command(command="GetHome_path")}/cybertron/conf/patrol/patrol_checker_agent_rt6.conf', 
							old_strs=['fileexist_items { item_code: 1705003,', 'item_code: 1304241'],
							new_strs=['1304241', '1705003\n'], replace_mode='modify', re_str=[r"1705003", r"(1304241)[^( #事故)|^(,)]"])
						print(f'请【下电重启车辆】或者【重启计算的patrol进程】，让修改功能生效!')
					else:
						pass
				else:
					pass

			else:
				pass
		else:
			pass

	else:
		exec_command(command='1')

def run_command():

	try:
		command = sys.argv[1].strip()
		value_ls = [value for value in command_dict.values()]
		if command in value_ls:
			exec_command(command=command)
			sys.exit(0)
		else:
			raise ValueError

	except Exception as e:
		print(e)
		return exec_command(command='1')
		sys.exit(0)

if __name__ == '__main__':
	run_command()
