#!/usr/bin/python
# -*- coding:utf-8 -*-
# @auther    : jinhui
# @dateTime  : 2025-08-19
# @function  : 处理命令类
# @version   : V2.0

import os
import time
import datetime
import subprocess
from common_func import CommonFunc

class Handle_command:

    cmd_dict = {
					'获取命令帮助信息': '1', '执行Record录像功能': '2', '获取当前panel-serve的内存占用': '3', '开启/关闭/重开远程': '4', 
					'获取一段时间内的panel-serve内存占用信息': '5', '切换车端环境': '6', '模拟事故场景改造': '7',
				}
    
    def __init__(self):
        self.command_func_obj = CommonFunc()

    def command_exec(self, cmd):
        if cmd == self.cmd_dict['获取命令帮助信息']:
            help_info = ['命令作用描述', '命令快捷编号']
            help_info.extend([item for pair in self.cmd_dict.items() for item in pair])
            self.command_func_obj.table(data_ls=help_info, width_number=50, col_number = 2)
            print('例子：python3.8 handle_command.py 1\n使用问题如流找：v_jinhui02')
        elif cmd == self.cmd_dict['执行Record录像功能']:
            record_time = int(input("请输入你想录制Record的时间(单位秒): ").strip())
            sp = subprocess.Popen(args='cyber_recorder record -c /sensor/camera/obstacle/image_left_forward/'
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
            self.command_func_obj.handle_termination_signal(subprocess_obj=sp, dynamic_string_style='proress_bar', text_description='正在录制Record中...', bar_time=record_time)
            print('Record录制完毕')
            record_name = self.command_func_obj.handle_command(command=f'ls | grep {current_time}.record', stdout=True)[0].strip()
            return self.command_func_obj.handle_command(command=f'cyber_recorder info {record_name}')
        elif cmd == 'get_home_path':
            return os.environ['HOME']

        elif cmd == 'get_pwd_path':
            return self.command_func_obj.handle_command('pwd')

        # elif cmd == self.cmd_dict['获取当前panel-serve的PID号']:
        #     return self.command_func_obj.handle_command(command="ps -aux | grep panel_server_sched | grep -v grep | awk '{print $2}'")

        elif cmd == self.cmd_dict['获取当前patrol_agent的PID号']:
            return self.command_func_obj.handle_command(command="ps -aux | grep patrol_agent | grep -v grep | awk '{print $2}'")

        elif cmd == self.cmd_dict['获取当前panel-serve的内存占用']:
            pid = self.command_func_obj.handle_command(command="ps -aux | grep panel_server_sched | grep -v grep | awk '{print $2}'",
                                stdout=True)[0].strip()
            return self.command_func_obj.handle_command(command=f"top -p {pid} -b -n 1 | grep {pid} | awk " + "'{print $6}'")
        elif cmd == self.cmd_dict['开启/关闭/重开远程']:
            remote_switch = input(f"开启/关闭远程(on: 开; off: 关; rst: 重新开启): ")
            if remote_switch == 'on':
                os.chdir(f'{self.command_exec("get_home_path")}/cybertron/adtdp-debug-client')
                return self.command_func_obj.handle_command(command='bash ./bin/control.sh start')

            elif remote_switch == 'off':
                os.chdir(f'{self.command_exec("get_home_path")}/cybertron/adtdp-debug-client')
                return self.command_func_obj.handle_command(command='bash ./bin/control.sh stop')

            elif remote_switch == 'rst':
                os.chdir(f'{self.command_exec("get_home_path")}/cybertron/adtdp-debug-client')
                return self.command_func_obj.handle_command(command='bash ./bin/control.sh restart')
            else:
                pass
        elif cmd == self.cmd_dict['获取一段时间内的panel-serve内存占用信息']:
            pid = self.command_func_obj.handle_command(command="ps -aux | grep panel_server_sched | grep -v grep | awk '{print $2}'",
                                    stdout=True)[0].strip()
            record_time = int(input("请输入你想获取多长时间内的性能变化(单位秒): ").strip())
            self.command_func_obj.handle_command(f'sh {os.path.dirname(os.path.abspath(__file__))}/rely_files/mem_cpu.sh {pid} >mem_cpu.log 2>&1 &')
            time.sleep(2)
            self.command_func_obj.handle_termination_signal(subprocess_obj=sp, dynamic_string_style='proress_bar', text_description=f'正在计算{record_time}s内panel-serve的cpu性能...', bar_time=record_time)
            print('\n' + self.command_func_obj.string_format(f'panel-server在{record_time}s内的cpu和内存计算结果如下', '^', 100, '-'))
            return self.command_func_obj.handle_command(f'sh {os.path.dirname(os.path.abspath(__file__))}/rely_files/cal.sh mem_cpu.log')
        elif cmd == self.cmd_dict['切换车端环境']:
            print(self.command_func_obj.table(data_ls=['车端环境名称', '车端环境字段', 'QA测试环境', 'pre', '线上运营环境', 'online', 'opn环境', 'opn', 'test环境', 'test'], width_number=30, col_number = 2))
            env_name = str(input('请输入你想将车端切换的环境名称: '))
            is_existed_string = True if self.command_func_obj.contains_regex_in_file(file_path=f'{self.command_exec(command="get_home_path")}/otaclient/script/config_deploy.py', pattern='original_url = ') else False
            if env_name == 'pre':
                self.command_func_obj.modify_content(file=f'{self.command_exec(command="get_home_path")}/cybertron/bin/integration_config.py',
                                                    match_str=[r'host = "https://idgdata(opn|test|pre)?.baidu.com"'],
                                                    replace_strs=['host = "https://idgdatapre.baidu.com"'], mode='m')
                self.command_func_obj.modify_content(file=f'{self.command_exec(command="get_home_path")}/cybertron/conf/robo_agent.conf',
                                                    match_str=[r'https_url_perfix:"https://cert(-(fleet|opn|test|pre)?)?.baidu.com"', 
                                                                r'hmi_customize_host:"https://idgdata(opn|test|pre)?.baidu.com"',
                                                                r'mqtts_environment_switch: (1|2|3)'],
                                                    replace_strs=['https_url_perfix:"https://cert-pre.baidu.com"',
									                              'hmi_customize_host:"https://idgdatapre.baidu.com"',
									                              'mqtts_environment_switch: 2'], mode='m')
                self.command_func_obj.modify_content(file=f'{self.command_exec(command="get_home_path")}/otaclient/etc/otaclient.conf',
                                                    match_str=[r'mode = (online|opn|test|pre)', r'use = (True|False)'],
                                                    replace_strs=['mode = pre', 'use = True'], mode='m')
                if is_existed_string:
                    self.command_func_obj.modify_content(file=f'{self.command_exec(command="get_home_path")}/otaclient/script/config_deploy.py',
                                                        match_str=[r'original_url = "https://idgops(-(test|pre|opn))?.baidu.com"'],
                                                        replace_strs=[r'original_url = "https://idgops-pre.baidu.com"'], mode='m')
                else:
                    self.command_func_obj.modify_content(file=f'{self.command_exec(command="get_home_path")}/otaclient/script/config_deploy.py',
                                                        match_str=[r'domain = "idgops(-(opn|test|pre)?)?"', r'.format\((domain|"(idgops(-(test|pre|opn))?)")\)'],
                                                        replace_strs=[r'domain = "idgops-pre"', r'.format("idgops-pre")'], mode='m')

            elif env_name == 'online' or env_name == 'opn':
                self.command_func_obj.modify_content(file=f'{self.command_exec(command="get_home_path")}/cybertron/bin/integration_config.py',
                                                    match_str=[r'host = "https://idgdata(opn|test|pre)?.baidu.com"'],
                                                    replace_strs=['host = "https://idgdata.baidu.com"'], mode='m')
                self.command_func_obj.modify_content(file=f'{self.command_exec(command="get_home_path")}/cybertron/conf/robo_agent.conf',
                                                    match_str=[r'https_url_perfix:"https://cert(-(fleet|opn|test|pre)?)?.baidu.com"', 
                                                                r'hmi_customize_host:"https://idgdata(opn|test|pre)?.baidu.com"',
                                                                r'mqtts_environment_switch: (1|2|3)'],
                                                    replace_strs=['https_url_perfix:"https://cert-fleet.baidu.com"',
									                              'hmi_customize_host:"https://idgdata.baidu.com"',
									                              'mqtts_environment_switch: 1'], mode='m')
                if env_name == 'online':
                    self.command_func_obj.modify_content(file=f'{self.command_exec(command="get_home_path")}/otaclient/etc/otaclient.conf',
                                                    match_str=[r'mode = (online|opn|test|pre)', r'use = (True|False)'],
                                                    replace_strs=['mode = online', 'use = True'], mode='m')
                    if is_existed_string:
                        self.command_func_obj.modify_content(file=f'{self.command_exec(command="get_home_path")}/otaclient/script/config_deploy.py',
                                                            match_str=[r'original_url = "https://idgops(-(test|pre|opn))?.baidu.com"'],
                                                            replace_strs=[r'original_url = "https://idgops.baidu.com"'], mode='m')
                    else:
                        self.command_func_obj.modify_content(file=f'{self.command_exec(command="get_home_path")}/otaclient/script/config_deploy.py',
                                                            match_str=[r'domain = "idgops(-(opn|test|pre)?)?"', r'.format\((domain|"(idgops(-(test|pre|opn))?)")\)'],
                                                            replace_strs=[r'domain = "idgops"', r'.format("idgops")'], mode='m')
                elif env_name == 'opn':
                    self.command_func_obj.modify_content(file=f'{self.command_exec(command="get_home_path")}/otaclient/etc/otaclient.conf',
                                                    match_str=[r'mode = (online|opn|test|pre)', r'use = (True|False)'],
                                                    replace_strs=['mode = opn', 'use = True'], mode='m')
                    if is_existed_string:
                        self.command_func_obj.modify_content(file=f'{self.command_exec(command="get_home_path")}/otaclient/script/config_deploy.py',
                                                            match_str=[r'original_url = "https://idgops(-(test|pre|opn))?.baidu.com"'],
                                                            replace_strs=[r'original_url = "https://idgops-opn.baidu.com"'], mode='m')
                    else:
                        self.command_func_obj.modify_content(file=f'{self.command_exec(command="get_home_path")}/otaclient/script/config_deploy.py',
                                                            match_str=[r'domain = "idgops(-(opn|test|pre)?)?"', r'.format\((domain|"(idgops(-(test|pre|opn))?)")\)'],
                                                            replace_strs=[r'domain = "idgops-opn"', r'.format("idgops-opn")'], mode='m')
            elif env_name == 'test':
                self.command_func_obj.modify_content(file=f'{self.command_exec(command="get_home_path")}/cybertron/bin/integration_config.py',
                                                    match_str=[r'host = "https://idgdata(opn|test|pre)?.baidu.com"'],
                                                    replace_strs=['host = "https://idgdatatest.baidu.com"'], mode='m')
                self.command_func_obj.modify_content(file=f'{self.command_exec(command="get_home_path")}/cybertron/conf/robo_agent.conf',
                                                    match_str=[r'https_url_perfix:"https://cert(-(fleet|opn|test|pre)?)?.baidu.com"', 
                                                                r'hmi_customize_host:"https://idgdata(opn|test|pre)?.baidu.com"',
                                                                r'mqtts_environment_switch: (1|2|3)'],
                                                    replace_strs=['https_url_perfix:"https://cert-test.baidu.com"',
									                              'hmi_customize_host:"https://idgdatatest.baidu.com"',
									                              'mqtts_environment_switch: 3'], mode='m')
                self.command_func_obj.modify_content(file=f'{self.command_exec(command="get_home_path")}/otaclient/etc/otaclient.conf',
                                                    match_str=[r'mode = (online|opn|test|pre)', r'use = (True|False)'],
                                                    replace_strs=['mode = pre', 'use = True'], mode='m')
                if is_existed_string:
                    self.command_func_obj.modify_content(file=f'{self.command_exec(command="get_home_path")}/otaclient/script/config_deploy.py',
                                                        match_str=[r'original_url = "https://idgops(-(test|pre|opn))?.baidu.com"'],
                                                        replace_strs=[r'original_url = "https://idgops-test.baidu.com"'], mode='m')
                else:
                    self.command_func_obj.modify_content(file=f'{self.command_exec(command="get_home_path")}/otaclient/script/config_deploy.py',
                                                        match_str=[r'domain = "idgops(-(opn|test|pre)?)?"', r'.format\((domain|"(idgops(-(test|pre|opn))?)")\)'],
                                                        replace_strs=[r'domain = "idgops-test"', r'.format("idgops-test")'], mode='m')
            print(f"车端环境+OTA环境+获取驾驶能力套餐环境都已经切换到【{env_name}环境】\n")
            self.command_func_obj.string_format(f'请在下面云舱代驾环境选项中选择"{env_name}"', '^', 100, '-')
            return self.command_func_obj.handle_command(f'python {self.command_exec(command="get_home_path")}/cybertron/bin/remote_control/change_remote_env.py')
        elif cmd == self.cmd_dict['模拟事故场景改造']:
            mock_error_info = ['模拟事故的场景类型', '模拟事故的场景码']
            mock_error_info.extend(['自动驾驶异常—终点重启（1002）', '1', '传感器异常（1003）', '2', '自动驾驶严重异常-现场处置（1021）', '3', '传感器严重异常（1022）', '4', 'nvme严重异常（1023）', '5', 
                                    '轮胎异常（1004）', '6', '轮胎严重异常（1026）', '7', '交通事故', '8'])
            self.command_func_obj.table(data_ls=mock_error_info, width_number=35, col_number=2)

            mock_error_code = input('请输入你想触发模拟事故的场景码: ').strip()
            if mock_error_code == '1':
                sp = subprocess.Popen(args=f'python {os.path.dirname(os.path.abspath(__file__))}/rely_files/module_error_mock.py 2 254 "error"', shell=True, stdout=subprocess.DEVNULL,
								  stderr=subprocess.DEVNULL, start_new_session=True)
                self.command_func_obj.handle_termination_signal(subprocess_obj=sp, dynamic_string_style='wait_animation', text_description='事故场景模拟中')
            elif mock_error_code == '2':
                sp = subprocess.Popen(args=f'python {os.path.dirname(os.path.abspath(__file__))}/rely_files/module_error_mock.py 2 254 "error"', shell=True, stdout=subprocess.DEVNULL,
								  stderr=subprocess.DEVNULL, start_new_session=True)
                self.command_func_obj.handle_termination_signal(subprocess_obj=sp, dynamic_string_style='wait_animation', text_description='事故场景模拟中')
            elif mock_error_code == '3':
                sp = subprocess.Popen(args=f'python {os.path.dirname(os.path.abspath(__file__))}/rely_files/module_error_mock.py 2 243 "error"', shell=True, stdout=subprocess.DEVNULL,
								  stderr=subprocess.DEVNULL, start_new_session=True)
                self.command_func_obj.handle_termination_signal(subprocess_obj=sp, dynamic_string_style='wait_animation', text_description='事故场景模拟中')
            elif mock_error_code == '4':
                sp = subprocess.Popen(args=f'python {os.path.dirname(os.path.abspath(__file__))}/rely_files/module_error_mock.py 1 213 "error"', shell=True, stdout=subprocess.DEVNULL,
								  stderr=subprocess.DEVNULL, start_new_session=True)
                self.command_func_obj.handle_termination_signal(subprocess_obj=sp, dynamic_string_style='wait_animation', text_description='事故场景模拟中')
            elif mock_error_code == '5':
                sp = subprocess.Popen(args=f'python {os.path.dirname(os.path.abspath(__file__))}/rely_files/module_error_mock.py 6 700 "error"', shell=True, stdout=subprocess.DEVNULL,
								  stderr=subprocess.DEVNULL, start_new_session=True)
                self.command_func_obj.handle_termination_signal(subprocess_obj=sp, dynamic_string_style='wait_animation', text_description='事故场景模拟中')
            elif mock_error_code in ['6', '7', '8']:
                self.command_func_obj.table(data_ls=["制造/恢复故障", "选择字段", "制造故障", "1", "恢复故障", "2"], width_number=12, col_number=2)
                is_error = input('请选择是制造故障还是恢复故障: ').strip()
                self.command_func_obj.table(data_ls=["车辆型号", "型号字段", "RT5", "1", "RT6", "2"], width_number=12, col_number=2)
                car_type = input('请输入你想触发事故模拟的车辆类型: ').strip()
                if is_error == '1':
                    if car_type == '1':
                        if mock_error_code == '6':
                            self.command_func_obj.modify_content(file=f'{self.command_exec("get_home_path")}/cybertron/conf/patrol/patrol_checker_agent.conf',
                                                                 match_str=[r'fileexist_items { item_code: 1304241'], replace_strs=[r'fileexist_items { item_code: 3100823'], mode='m')
                            self.command_func_obj.modify_content(file=f'{self.command_exec("get_home_path")}/cybertron/conf/patrol/patrol_erritems_merge.conf',
                                                                 match_str=[r'erritems {item_code: 1304241'], replace_strs=[r'#'], mode='a', insert_index=1)
                            self.command_func_obj.handle_command(f'scp {self.command_exec("get_home_path")}/cybertron/conf/patrol/patrol_erritems_merge.conf caros@192.168.10.8:/home/caros/cybertron/conf/patrol')
                            print(f'请【下电重启车辆】或者【重启计算和安全的patrol进程】，让修改功能生效!')
                            print(f'构造故障请在计算节点输入这个命令: mv /home/caros/cybertron/params/onsemi_wide_extrinsics.yaml /home/caros/cybertron/params/onsemi_wide_extrinsics.yaml.bk')
                            print(f'恢复故障请在计算节点输入这个命令: mv /home/caros/cybertron/params/onsemi_wide_extrinsics.yaml.bk /home/caros/cybertron/params/onsemi_wide_extrinsics.yaml')
                        elif mock_error_code == '7':
                            self.command_func_obj.modify_content(file=f'{self.command_exec("get_home_path")}/cybertron/conf/patrol/patrol_checker_agent.conf',
                                                                 match_str=[r'fileexist_items { item_code: 1304231'], replace_strs=[r'fileexist_items { item_code: 3100411'], mode='m')
                            self.command_func_obj.modify_content(file=f'{self.command_exec("get_home_path")}/cybertron/conf/patrol/patrol_erritems_merge.conf',
                                                                 match_str=[r'erritems {item_code: 1304231'], replace_strs=[r'#'], mode='a', insert_index=1)
                            self.command_func_obj.handle_command(f'scp {self.command_exec("get_home_path")}/cybertron/conf/patrol/patrol_erritems_merge.conf caros@192.168.10.8:/home/caros/cybertron/conf/patrol')
                            print(f'请【下电重启车辆】或者【重启计算和安全的patrol进程】，让修改功能生效!')
                            print(f'构造故障请在计算节点输入这个命令: mv /home/caros/cybertron/params/onsemi_narrow_extrinsics.yaml /home/caros/cybertron/params/onsemi_narrow_extrinsics.yaml.bk')
                            print(f'恢复故障请在计算节点输入这个命令: mv /home/caros/cybertron/params/onsemi_narrow_extrinsics.yaml.bk /home/caros/cybertron/params/onsemi_narrow_extrinsics.yaml')
                        elif mock_error_code == '8':
                            self.command_func_obj.modify_content(file=f'{self.command_exec("get_home_path")}/cybertron/conf/patrol/patrol_checker_agent.conf', 
                                                                 match_str=[r'fileexist_items { item_code: 1304126,', r'(1705003)[^( #事故)|^(,)]'],
                                                                 replace_strs=[r'fileexist_items { item_code: 1705003,', r'1304126\n'])
                            print(f'请【下电重启车辆】或者【重启计算的patrol进程】，让修改功能生效!')
                            print(f'构造故障请在计算节点输入这个命令: mv /home/caros/cybertron/params/hesai90_height.yaml /home/caros/cybertron/params/hesai90_height.yaml_1')
                            print(f'恢复故障请在计算节点输入这个命令: mv /home/caros/cybertron/params/hesai90_height.yaml_1 /home/caros/cybertron/params/hesai90_height.yaml')
                        else:
                            pass
                    elif car_type == '2':
                        if mock_error_code == '6':
                            self.command_func_obj.modify_content(file=f'{self.command_exec("get_home_path")}/cybertron/conf/patrol/patrol_checker_agent_rt6.conf',
                                                                 match_str=[r'fileexist_items { item_code: 1304241'], replace_strs=[r'fileexist_items { item_code: 3100823'], mode='m')
                            self.command_func_obj.modify_content(file=f'{self.command_exec("get_home_path")}/cybertron/conf/patrol/patrol_erritems_merge_rt6.conf',
                                                                 match_str=[r'erritems {item_code: 1304241'], replace_strs=[r'#'], mode='a', insert_index=1)
                            self.command_func_obj.handle_command(f'scp {self.command_exec("get_home_path")}/cybertron/conf/patrol/patrol_erritems_merge_rt6.conf caros@192.168.10.8:/home/caros/cybertron/conf/patrol')
                            print(f'请【下电重启车辆】或者【重启计算和安全的patrol进程】，让修改功能生效!')
                            print(f'构造故障请在计算节点输入这个命令: mv /home/caros/cybertron/params/onsemi_wide_extrinsics.yaml /home/caros/cybertron/params/onsemi_wide_extrinsics.yaml.bk')
                            print(f'恢复故障请在计算节点输入这个命令: mv /home/caros/cybertron/params/onsemi_wide_extrinsics.yaml.bk /home/caros/cybertron/params/onsemi_wide_extrinsics.yaml')
                        elif mock_error_code == '7':
                            self.command_func_obj.modify_content(file=f'{self.command_exec("get_home_path")}/cybertron/conf/patrol/patrol_checker_agent_rt6.conf',
                                                                 match_str=[r'fileexist_items { item_code: 1304231'], replace_strs=[r'fileexist_items { item_code: 3100411'], mode='m')
                            self.command_func_obj.modify_content(file=f'{self.command_exec("get_home_path")}/cybertron/conf/patrol/patrol_erritems_merge_rt6.conf',
                                                                 match_str=[r'erritems {item_code: 1304231'], replace_strs=[r'#'], mode='a', insert_index=1)
                            self.command_func_obj.handle_command(f'scp {self.command_exec("get_home_path")}/cybertron/conf/patrol/patrol_erritems_merge_rt6.conf caros@192.168.10.8:/home/caros/cybertron/conf/patrol')
                            print(f'请【下电重启车辆】或者【重启计算和安全的patrol进程】，让修改功能生效!')
                            print(f'构造故障请在计算节点输入这个命令: mv /home/caros/cybertron/params/onsemi_narrow_extrinsics.yaml /home/caros/cybertron/params/onsemi_narrow_extrinsics.yaml.bk')
                            print(f'恢复故障请在计算节点输入这个命令: mv /home/caros/cybertron/params/onsemi_narrow_extrinsics.yaml.bk /home/caros/cybertron/params/onsemi_narrow_extrinsics.yaml')
                        elif mock_error_code == '8':
                            self.command_func_obj.modify_content(file=f'{self.command_exec("get_home_path")}/cybertron/conf/patrol/patrol_checker_agent_rt6.conf', 
                                                                 match_str=[r'fileexist_items { item_code: 1304241,', r'(1705003)[^( #事故)|^(,)]'],
                                                                 replace_strs=[r'fileexist_items { item_code: 1705003,', r'1304241\n'])
                            print(f'请【下电重启车辆】或者【重启计算的patrol进程】，让修改功能生效!')
                            print(f'构造故障请在计算节点输入这个命令: mv /home/caros/cybertron/params/onsemi_wide_extrinsics.yaml /home/caros/cybertron/params/onsemi_wide_extrinsics.yaml_1')
                            print(f'恢复故障请在计算节点输入这个命令: mv /home/caros/cybertron/params/onsemi_wide_extrinsics.yaml_1 /home/caros/cybertron/params/onsemi_wide_extrinsics.yaml')
                        else:
                            pass
                    else:
                        pass
                elif is_error == '2':
                    if car_type == '1':
                        if mock_error_code == '6':
                            self.command_func_obj.modify_content(file=f'{self.command_exec("get_home_path")}/cybertron/conf/patrol/patrol_checker_agent.conf',
                                                                 match_str=[r'fileexist_items { item_code: 3100823'], replace_strs=[r'fileexist_items { item_code: 1304241'], mode='m')
                            self.command_func_obj.modify_content(file=f'{self.command_exec("get_home_path")}/cybertron/conf/patrol/patrol_erritems_merge.conf',
                                                                 match_str=[r'#  erritems {item_code: 1304241'], replace_strs=[r'  erritems {item_code: 1304241'], mode='m')
                            self.command_func_obj.handle_command(f'scp {self.command_exec("get_home_path")}/cybertron/conf/patrol/patrol_erritems_merge.conf caros@192.168.10.8:/home/caros/cybertron/conf/patrol')
                            print(f'请【下电重启车辆】或者【重启计算和安全的patrol进程】，即可恢复环境!')
                        elif mock_error_code == '7':
                            self.command_func_obj.modify_content(file=f'{self.command_exec("get_home_path")}/cybertron/conf/patrol/patrol_checker_agent.conf',
                                                                 match_str=[r'fileexist_items { item_code: 3100411'], replace_strs=[r'fileexist_items { item_code: 1304231'], mode='m')
                            self.command_func_obj.modify_content(file=f'{self.command_exec("get_home_path")}/cybertron/conf/patrol/patrol_erritems_merge.conf',
                                                                 match_str=[r'#  erritems {item_code: 1304231'], replace_strs=[r'  erritems {item_code: 1304231'], mode='m')
                            self.command_func_obj.handle_command(f'scp {self.command_exec("get_home_path")}/cybertron/conf/patrol/patrol_erritems_merge.conf caros@192.168.10.8:/home/caros/cybertron/conf/patrol')
                            print(f'请【下电重启车辆】或者【重启计算和安全的patrol进程】，即可恢复环境!')
                        elif mock_error_code == '8':
                            self.command_func_obj.modify_content(file=f'{self.command_exec("get_home_path")}/cybertron/conf/patrol/patrol_checker_agent.conf', 
                                                                 match_str=[r'fileexist_items { item_code: 1705003,', r'(1304126)[^( #事故)|^(,)]'],
                                                                 replace_strs=[r'fileexist_items { item_code: 1304126,', r'1705003\n'])
                            print(f'请【下电重启车辆】或者【重启计算和安全的patrol进程】，即可恢复环境!')
                        else:
                            pass
                    elif car_type == '2':
                        if mock_error_code == '6':
                            self.command_func_obj.modify_content(file=f'{self.command_exec("get_home_path")}/cybertron/conf/patrol/patrol_checker_agent_rt6.conf',
                                                                 match_str=[r'fileexist_items { item_code: 3100823'], replace_strs=[r'fileexist_items { item_code: 1304241'], mode='m')
                            self.command_func_obj.modify_content(file=f'{self.command_exec("get_home_path")}/cybertron/conf/patrol/patrol_erritems_merge_rt6.conf',
                                                                 match_str=[r'#  erritems {item_code: 1304241'], replace_strs=[r'  erritems {item_code: 1304241'], mode='m')
                            self.command_func_obj.handle_command(f'scp {self.command_exec("get_home_path")}/cybertron/conf/patrol/patrol_erritems_merge_rt6.conf caros@192.168.10.8:/home/caros/cybertron/conf/patrol')
                            print(f'请【下电重启车辆】或者【重启计算和安全的patrol进程】，即可恢复环境!')
                        elif mock_error_code == '7':
                            self.command_func_obj.modify_content(file=f'{self.command_exec("get_home_path")}/cybertron/conf/patrol/patrol_checker_agent_rt6.conf',
                                                                 match_str=[r'fileexist_items { item_code: 3100411'], replace_strs=[r'fileexist_items { item_code: 1304231'], mode='m')
                            self.command_func_obj.modify_content(file=f'{self.command_exec("get_home_path")}/cybertron/conf/patrol/patrol_erritems_merge_rt6.conf',
                                                                 match_str=[r'#  erritems {item_code: 1304231'], replace_strs=[r'  erritems {item_code: 1304231'], mode='m')
                            self.command_func_obj.handle_command(f'scp {self.command_exec("get_home_path")}/cybertron/conf/patrol/patrol_erritems_merge_rt6.conf caros@192.168.10.8:/home/caros/cybertron/conf/patrol')
                            print(f'请【下电重启车辆】或者【重启计算和安全的patrol进程】，即可恢复环境!')
                        elif mock_error_code == '8':
                            self.command_func_obj.modify_content(file=f'{self.command_exec("get_home_path")}/cybertron/conf/patrol/patrol_checker_agent_rt6.conf', 
                                                                 match_str=[r'fileexist_items { item_code: 1705003,', r'(1304241)[^( #事故)|^(,)]'],
                                                                 replace_strs=[r'fileexist_items { item_code: 1304241,', r'1705003\n'])
                            print(f'请【下电重启车辆】或者【重启计算和安全的patrol进程】，即可恢复环境!')
                        else:
                            pass
                    else:
                        pass
                else:
                    pass
        else:           
            self.command_exec('1')

if __name__ == '__main__':
    test = Handle_command()
    test.command_exec(cmd='1')

