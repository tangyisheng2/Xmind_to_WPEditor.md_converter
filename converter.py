#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   converter.py
@Contact :   tangyisheng2@sina.com
@License :   (C)Copyright 1999-2020, Tang Yisheng

@Modify Time        @Author     @Version        @Desciption
------------        -------     --------        -----------
2020/4/27 11:46     Tang        1.0             None
"""
import sys


def calculate_max_heading(md: str):
    heading_letter = "#"
    heading_str = "#"
    count = 0
    while md.count(heading_str):
        count += 1
        heading_str = f"{heading_str}{heading_letter}"
    return count


def save_file(md: str):
    with open('save.md', "w+", encoding='UTF-8') as file:
        file.write(md)  # 读取文件全部内容
        file.close()


def open_file():
    with open('FFT.md', encoding='UTF-8') as file:
        md = file.read()  # 读取文件全部内容
        file.close()
    return md


def convert(md: str):
    max_heading_count = calculate_max_heading(md)
    indent_replace = str()

    # 第一次替换掉最低级的节点
    for i in range(0, max_heading_count + 1):
        indent_replace = f"{indent_replace}{'    '}"  # 拓展indent
    indent_replace = f"{indent_replace}{'- '}"
    md = md.replace("- ", indent_replace)

    # 替换heading
    count = max_heading_count
    for i in range(0, max_heading_count):
        # 构建要替换的原字符串
        indent_to_be_replace = ""
        for j in range(0, count):
            indent_to_be_replace = f"{indent_to_be_replace}{'#'}"

        indent_replace = indent_replace.replace("    - ", "- ")  # 逐次降低层级

        md = md.replace(indent_to_be_replace, indent_replace)
        count -= 1
        # print(md)
    return md


if __name__ == "__main__":
    md = open_file()
    md_converted = convert(md)
    save_file(md_converted)
