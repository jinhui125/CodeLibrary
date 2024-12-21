#! /usr/bin/env python3
# _*_ coding:utf-8 _*_
# datetime: 2023-12-08
# author: jinHui

import os
import csv
import time
import datetime
from dataVisual import DataVisual

class PerfDataINFO:

    def __init__(self, app_name, device_name, perf_data, run_time, *progress):

        self.appName = app_name
        self.deviceName = device_name
        self.runTime = datetime.timedelta(seconds=run_time)
        self.progress = progress
        self.perfData = perf_data
        # 分割线，便于定位日志
        print("{:*^50s}".format("Split Line"))
        print("{:+^50s}".format(self.perfData))

    def clear_file(self, file_path):
        with open(file=file_path, mode='w', encoding='utf-8') as fb:
            pass
    def get_pid(self):
        app_pid = {}
        for app in self.progress:
            result = os.popen(f'adb -s {self.deviceName} shell ps | grep {app}')
            for line in result.readlines():
                app = line.split()[-1]
                pid = line.split()[1]
                app_pid[app] = pid
        return app_pid

    def sed_result(self, original_path, keyword, result_path):
        # 获取开始、结束行数
        start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        print('获取start_index开始时间：', start_time)
        sed_index = {'start_index': 0, 'end_index': 0}
        while sed_index['start_index'] == 0:
            time.sleep(1)
            for index, line in enumerate(open(original_path, 'r')):
                if keyword in line:
                    sed_index['start_index'] = index
                    print("start_index:", sed_index['start_index'])
                    break
        end_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        print('获取start_index结束时间：', end_time)
        with open(original_path, 'r') as f:
            result = f.readlines()[sed_index['start_index']:]
            index = sed_index['start_index']
            for line in result:
                index = index + 1
                if line in ['\n', '\r\n']:
                    sed_index['end_index'] = index
                    print("end_index:", sed_index['end_index'])
                    break

        # 从开始、结束行数截取内容
        os.popen("sed -n '{},{}p' {} > {}".format(sed_index['start_index'], sed_index['end_index'], original_path,
                                                  result_path))

    def get_cpu_info(self):
        # 获取PID
        app_pid = self.get_pid()
        print("appPID:", app_pid)
        app_cpu = {}
        cpu_data = './data_file/cpu_info.txt'
        self.clear_file(file_path=cpu_data)
        start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        os.popen(f'adb -s {self.deviceName} shell top -n 1 -b > {cpu_data}')
        while not os.path.getsize(cpu_data):
            # os.path.getsize() 返回文件的字节数，如果为 0，则代表空
            # 判断执行top命令返回的数据是否存入文件
            time.sleep(1)
        end_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        print('运行top命令开始时间：', start_time)
        print('运行top命令数据保存到文件的结束时间：', end_time)
        with open(cpu_data, 'r') as fb:
            for line in fb.readlines():
                for app in self.progress:
                    if app in app_pid.keys():
                        if app_pid[app] in line:
                            cpu = round(float(line.split()[-4]), 2)
                            app_cpu[app] = cpu
        print("appCPU:", app_cpu)
        return app_cpu

    def get_memory_pss(self):
        # 获取pid
        app_pid = self.get_pid()
        # 获取内存数据
        original_path = './data_file/original_data.txt'
        result_path = './data_file/sed_result.txt'
        self.clear_file(file_path=original_path)
        self.clear_file(file_path=result_path)
        start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        os.popen(f'adb -s {self.deviceName} shell dumpsys meminfo > {original_path}')
        while not os.path.getsize(original_path):
            time.sleep(1)
        end_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        print('运行获取内存开始时间：', start_time)
        print('运行内存数据保存到文件的结束时间：', end_time)
        self.sed_result(original_path=original_path, keyword='Total PSS by process:', result_path=result_path)
        while not os.path.getsize(result_path):
            time.sleep(1)
        app_pss = {}
        with open(result_path, 'r') as f:
            for line in f.readlines():
                for app in self.progress:
                    if app in app_pid.keys():
                        if app_pid[app] in line:
                            print('app_mem_line:', line, app, app_pid[app])
                            pss = round((int(line.strip().split('K: ')[0].replace(',', ''))) / 1024, 2)
                            app_pss[app] = pss
        print("appPss", app_pss)
        return app_pss

    # def analysis_dumpsys_csv(self, file_name):
    #     # 对性能数据文件进行计算，获取均值、最大值、最小值
    #     analyse_data = []
    #     info = pd.read_csv(file_name, encoding='gbk')
    #     rows_name = info.columns  # 列名
    #     print('列名：', rows_name)
    #     row_number = info.shape[0]  # 行数
    #     col_number = info.shape[1]  # 列数
    #     print(f"行:{row_number},type{type(row_number)}，列：{col_number}")
    #     avg_data = ['', '', '', 'avg']  # 存放均值
    #     max_data = ['', '', '', 'max']  # 存放最大值
    #     min_data = ['', '', '', 'min']  # 存放最小值
    #     for row_name in rows_name:
    #         if row_name not in ['id', 'hour', 'minute', 'second']:
    #             avg_value = round(info[row_name].mean(), 2)
    #             max_value = info[row_name].max()
    #             min_value = info[row_name].min()
    #             avg_data.append(avg_value)
    #             max_data.append(max_value)
    #             min_data.append(min_value)
    #     # 将均值、最大值、最小值存入analyse_data以便输入csv文件
    #     analyse_data.append(avg_data)
    #     analyse_data.append(max_data)
    #     analyse_data.append(min_data)
    #     print('analyse_data:', analyse_data)
    #     # 在数据表中插入平均值、最大值、最小值
    #     with open(file_name, 'a+', newline='') as file:
    #         # a+ 追加方式写+读
    #         writer = csv.writer(file)
    #         writer.writerows(analyse_data)
    #         time.sleep(1)
    #         file.close()

    def perf_run(self):
        print("开始时间:", datetime.datetime.now())
        print('指定运行时间（单位秒）:', self.runTime)
        id_number = 1  # id：可以运行的次数
        end_time = datetime.datetime.now() + self.runTime
        mem_pss_data = []
        cpu_data = []
        while end_time > datetime.datetime.now():
            cpu_info = self.get_cpu_info()  # 获取cpu
            cpu_info['id'] = id_number
            cpu_info['time'] = (f'{datetime.datetime.now().hour}:{datetime.datetime.now().minute}:'
                                f'{datetime.datetime.now().second}')
            # cpu_info['minute'] = datetime.datetime.now().minute
            # cpu_info['second'] = datetime.datetime.now().second
            cpu_data.append(cpu_info)

            mem_pss = self.get_memory_pss()  # 获取内存
            mem_pss['id'] = id_number
            mem_pss['time'] = (f'{datetime.datetime.now().hour}:{datetime.datetime.now().minute}:'
                                f'{datetime.datetime.now().second}')
            # mem_pss['minute'] = datetime.datetime.now().minute
            # mem_pss['second'] = datetime.datetime.now().second
            mem_pss_data.append(mem_pss)
            id_number = id_number + 1
            time.sleep(1)
        print(f'cpu_data: {cpu_data} mem_pss_data: {mem_pss_data}')

        cpu_info = self.get_cpu_info()  # 获取cpu
        # print('cpu_info:', cpu_info)
        cpu_info['id'] = id_number
        cpu_info['time'] = (f'{datetime.datetime.now().hour}:{datetime.datetime.now().minute}:'
                            f'{datetime.datetime.now().second}')
        cpu_data.append(cpu_info)

        mem_pss = self.get_memory_pss()  # 获取内存
        id_number = id_number + 1
        mem_pss['id'] = id_number
        mem_pss['time'] = (f'{datetime.datetime.now().hour}:{datetime.datetime.now().minute}:'
                           f'{datetime.datetime.now().second}')
        mem_pss_data.append(mem_pss)

        # 保存内存数据
        field_name = []
        for app in self.progress:
            field_name.append(app)
        els = ['id', 'time']
        field_name = els + field_name
        print('filedName:', field_name)
        with open(f'./data_file/tmp_file/MemPSS-{self.perfData}', 'w', newline='') as csv_fb:
            writer = csv.DictWriter(csv_fb, fieldnames=field_name)
            writer.writeheader()
            for row in mem_pss_data:
                writer.writerow(row)
        # self.analysis_dumpsys_csv(f'./data_file/tmp_file/mem_pss-{self.perfData}')

        # 保存cpu数据
        with open(f'./data_file/tmp_file/AppCPU-{self.perfData}', 'w', newline='') as csv_fb:
            writer = csv.DictWriter(csv_fb, fieldnames=field_name)
            writer.writeheader()
            for row in cpu_data:
                writer.writerow(row)
        # self.analysis_dumpsys_csv(f'./data_file/tmp_file/AppCPU-{self.perfData}')
        data_visual = DataVisual(csv_cpu=f'./data_file/tmp_file/AppCPU-{self.perfData}',
                                 csv_mem=f'./data_file/tmp_file/MemPSS-{self.perfData}',
                                 save_image_name=self.perfData, progress=list(self.progress))
        data_visual.show_data()

if __name__ == '__main__':
    app_name = 'com.baidu.adt.hmi.passenger'
    device_name = 'A8KXBB1601001510'
    runTime = 600
    perfData = f'HMI性能分析-{str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))}.csv'
    test = PerfDataINFO(app_name, device_name, perfData, runTime, 'com.baidu.adt.hmi.passenger')
    test.perf_run()

