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
        self.fig = self.plt.figure(num=1, figsize=(50, 10))
        self.color_ls = ['red', 'black', 'blue']
        self.marker_ls = ['o', 's', 'p']
        self.plt.subplots_adjust(top=0.95, bottom=0.1)

    # 获取csv文件数据
    def get_col_data(self, col_name):
        cpu_original_data = pd.read_csv(self.csv_cpu)
        mem_original_data = pd.read_csv(self.csv_mem)
        handle_cpu_data = np.array(cpu_original_data[col_name])
        handle_mem_data = np.array(mem_original_data[col_name])
        return handle_cpu_data.tolist(), handle_mem_data.tolist()

    def show_data(self):
        cpu_x, mem_x = self.get_col_data(col_name='id')
        cpu_time, mem_time = self.get_col_data(col_name='time')
        cpu_y, mem_y, cpu_text, mem_text = {}, {}, {}, {}
        for progress in self.progress:
            cpu_y[progress], mem_y[progress] = self.get_col_data(col_name=progress)
        # print(f"cpu_x: {cpu_x}\nmem_x: {mem_x}\ncpu_y: {cpu_y}\nmem_y: {mem_y}")
        for key, value_ls in cpu_y.items():
            temp_ls = []
            index = 0
            for value in value_ls:
                temp_ls.append(f"id: {cpu_x[index]}\ntime: {cpu_time[index]}\nvalue: {value}%")
                index += 1
            cpu_text[key] = temp_ls
        # print(f'cpu_text: {cpu_text}')
        for key, value_ls in mem_y.items():
            temp_ls = []
            index = 0
            for value in value_ls:
                temp_ls.append(f"id: {mem_x[index]}\ntime: {mem_time[index]}\nvalue: {value}MB")
                index += 1
            mem_text[key] = temp_ls
        # print(f'mem_text: {mem_text}')
        axes_cpu = self.fig.add_subplot(211)
        axes_mem = self.fig.add_subplot(212)
        for progress in self.progress:
            axes_cpu.plot(cpu_x, cpu_y[progress],  marker=self.marker_ls[self.progress.index(progress)],
                          color=self.color_ls[self.progress.index(progress)], linestyle='dashed', linewidth=0.5,
                          markersize=3, label=progress)
            # axes_cpu.scatter(cpu_x, cpu_y[progress], color=self.color_ls[self.progress.index(progress)], s=12.0)
            axes_mem.plot(mem_x, mem_y[progress], marker=self.marker_ls[self.progress.index(progress)],
                          color=self.color_ls[self.progress.index(progress)], linestyle='dashed', linewidth=0.5,
                          markersize=3, label=progress)
            # axes_mem.scatter(mem_x, mem_y[progress], color=self.color_ls[self.progress.index(progress)], s=12.0)

        axes_cpu.set_title("CPU性能折线图", fontsize=10, fontweight='black', verticalalignment="top")
        axes_cpu.set_xlabel("数据抓取时间节点", weight='bold', size=8, color='black')
        axes_cpu.set_ylabel("CPU使用占用率（%）", weight='bold', size=8, color='black')
        axes_mem.set_title("进程内存性能折线图", fontsize=10, fontweight='black', verticalalignment="top")
        axes_mem.set_xlabel("数据抓取时间节点", weight='bold', size=8, color='black')
        axes_mem.set_ylabel("进程内存占用（MB）", weight='bold', size=8, color='black')
        axes_cpu.legend(self.progress, loc="best", fontsize=8)
        axes_mem.legend(self.progress, loc="best", fontsize=8)

        cpu_info, mem_info = [], []
        for i in range(len(cpu_x)):
            bbox_cpu = dict(boxstyle="round", fc='lightgreen', alpha=0.6)
            arrow_cpu = dict(arrowstyle="->", connectionstyle="arc3,rad=0.")
            point_ls, annotation_ls = [], []
            for progress in self.progress:
                point, = axes_cpu.plot(cpu_x[i], cpu_y[progress][i], self.marker_ls[self.progress.index(progress)],
                                       color=self.color_ls[self.progress.index(progress)], markersize=3, label=progress)
                annotation = axes_cpu.annotate(cpu_text[progress][i], xy=(cpu_x[i], cpu_y[progress][i]), xytext=(-3, 5),
                                               textcoords='offset points', bbox=bbox_cpu, arrowprops=arrow_cpu, size=10)
                annotation.set_visible(False)
                point_ls.append(point)
                annotation_ls.append(annotation)
            cpu_info.append([point_ls, annotation_ls])
        # print("--------------------------------------------")
        # print(f'cpu_info: {cpu_info}')
        for i in range(len(mem_x)):
            bbox_mem = dict(boxstyle="round", fc='lightgreen', alpha=0.6)
            arrow_mem = dict(arrowstyle="->", connectionstyle="arc3,rad=0.")
            point_ls, annotation_ls = [], []
            for progress in self.progress:
                point, = axes_mem.plot(mem_x[i], mem_y[progress][i], self.marker_ls[self.progress.index(progress)],
                                       color=self.color_ls[self.progress.index(progress)], markersize=3, label=progress)
                annotation = axes_mem.annotate(mem_text[progress][i], xy=(mem_x[i], mem_y[progress][i]), xytext=(-3, 5),
                                               textcoords='offset points', bbox=bbox_mem, arrowprops=arrow_mem, size=10)
                annotation.set_visible(False)
                point_ls.append(point)
                annotation_ls.append(annotation)
            mem_info.append([point_ls, annotation_ls])

        def on_move(event):
            visibility_changed = False
            for p, a in cpu_info:
                for index in range(len(a)):
                    should_be_visible = (p[index].contains(event)[0] == True)
                    if should_be_visible != a[index].get_visible():
                        visibility_changed = True
                        a[index].set_visible(should_be_visible)
            for p, a in mem_info:
                for index in range(len(a)):
                    should_be_visible = (p[index].contains(event)[0] == True)
                    if should_be_visible != a[index].get_visible():
                        visibility_changed = True
                        a[index].set_visible(should_be_visible)

            if visibility_changed:
                self.plt.draw()

        on_move_id = self.fig.canvas.mpl_connect('motion_notify_event', on_move)
        self.plt.show()



if __name__ == '__main__':
    test = DataVisual(csv_cpu=r'./data_file/tmp_file/AppCPU-HMI性能分析-2023-12-12 16:46:50.csv',
                      csv_mem=r'./data_file/tmp_file/MemPSS-HMI性能分析-2023-12-12 16:46:50.csv',
                      save_image_name='2023-12-11', progress=['com.tencent.tmgp.gnyx',
                                                              'com.tencent.tmgp.gnyx:estPlugin',
                                                              'com.tencent.tmgp.gnyx:xg_vip_service'])
    print(test.show_data())


