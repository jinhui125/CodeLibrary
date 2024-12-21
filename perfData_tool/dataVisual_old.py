#! /usr/bin/env python3
# _*_ coding:utf-8 _*_
# datetime: 2023-12-10
# author: jinHui

import matplotlib
import numpy as np
import pandas as pd
from matplotlib import pyplot

matplotlib.rcParams['font.sans-serif'] = ['PingFang HK']

class DataVisual:

    def __init__(self, csv_cpu, csv_mem, save_image_name, progress: list):
        self.progress = progress
        self.csv_cpu = csv_cpu
        self.csv_mem = csv_mem
        self.save_image_name = save_image_name
        self.plt = pyplot
        self.fig = self.plt.figure(num=1, figsize=(50, 30))

    def get_col_data(self, col_name):
        cpu_original_data = pd.read_csv(self.csv_cpu)
        mem_original_data = pd.read_csv(self.csv_mem)
        handle_cpu_data = np.array(cpu_original_data[col_name])
        handle_mem_data = np.array(mem_original_data[col_name])
        return handle_cpu_data, handle_mem_data

    def show_data(self):
        cpu_x, mem_x = self.get_col_data(col_name='id')
        # for progress in self.progress:
        cpu_y, mem_y = self.get_col_data(col_name=self.progress[0])
        cpu_time, mem_time = self.get_col_data(col_name='time')
        cpu_ls = []
        mem_ls = []
        for i in range(len(cpu_x)):
            cpu_ls.append([i+1, cpu_y[i], cpu_time[i]])
        # print(cpu_ls)
        for j in range(len(mem_x)):
            mem_ls.append([j+1, mem_y[j], mem_time[j]])
        # print(mem_ls)
        axes_cpu = self.fig.add_subplot(211)
        axes_cpu.tick_params(left=False, pad=10, direction="in", length=2, width=3, color="b", labelsize=8)
        axes_cpu.spines["top"].set_visible(False)
        axes_cpu.spines["right"].set_visible(False)
        axes_cpu.spines["left"].set_visible(False)
        axes_cpu.plot([x[0] for x in cpu_ls], [y[1] for y in cpu_ls],  color='red', marker='o', linestyle='dashed',
                      linewidth=0.5, markersize=3, label='com.baidu.adt.hmi.console')
        for cpu_value in cpu_ls:
            axes_cpu.text(cpu_value[0], cpu_value[1], f"id:{cpu_value[0]}\nt:{cpu_value[2]}\nv:{cpu_value[1]}%",
                          fontsize=8, alpha=1)
        axes_cpu.set_title("CPU性能折线图", fontsize=10, fontweight='black', verticalalignment="top")
        axes_cpu.set_xlabel("数据抓取时间节点", weight='bold', size=8, color='black')
        axes_cpu.set_ylabel("CPU使用占用率（%）", weight='bold', size=8, color='black')
        axes_cpu.legend(self.progress, loc="best", fontsize=8)

        axes_mem = self.fig.add_subplot(212)
        axes_mem.tick_params(left=False, pad=10, direction="in", length=2, width=3, color="b", labelsize=8)
        axes_mem.spines["top"].set_visible(False)
        axes_mem.spines["right"].set_visible(False)
        axes_mem.spines["left"].set_visible(False)
        axes_mem.plot([x[0] for x in mem_ls], [y[1] for y in mem_ls], color='red', marker='o', linestyle='dashed',
                      linewidth=0.5, markersize=3, label='com.baidu.adt.hmi.console')
        for mem_value in mem_ls:
            axes_mem.text(mem_value[0], mem_value[1], f"id:{mem_value[0]}\nt:{mem_value[2]}\nv:{mem_value[1]}MB",
                          fontsize=8, alpha=1)
        axes_mem.set_title("进程内存性能折线图", fontsize=10, fontweight='black', verticalalignment="top")
        axes_mem.set_xlabel("数据抓取时间节点", weight='bold', size=8, color='black')
        axes_mem.set_ylabel("进程内存占用（MB）", weight='bold', size=8, color='black')
        axes_mem.legend(self.progress, loc="best", fontsize=8)
        self.plt.savefig(f'./data_file/analysis_result/{self.save_image_name}.png', dpi=300, bbox_inches='tight')
        self.plt.show()



if __name__ == '__main__':
    test = DataVisual(csv_cpu=r'./data_file/tmp_file/AppCPU-HMI性能分析-2023-12-11 17:17:08.csv',
                      csv_mem=r'./data_file/tmp_file/MemPSS-HMI性能分析-2023-12-11 17:17:08.csv',
                      save_image_name='2023-12-11', progress=['com.baidu.adt.hmi.passenger'])
    # data = test.get_data(col_name='id')
    # print(len(data))
    test.show_data()


