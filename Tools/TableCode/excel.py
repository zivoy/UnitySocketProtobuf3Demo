import os

import pandas as pd

from TableCode.cs_file import GenCSTableManagerFile, genCSLoadTablesFile
from TableCode.data_file import GenTableData
from TableCode.go_file import GenGoTableManagerFile, genGolangLoadTablesFile
from const import excel_dir


def processExcel(filePath, fileName):
    if "." in fileName:
        fileName = fileName.split('.')
        fileName = fileName[0]
    data = pd.read_excel(filePath)  # index_col=0
    nrows = len(data.index)
    ncols = len(data.columns)

    if nrows == 0 or ncols == 0:
        print("empty file:" + fileName)
        return

    cs_fields_index = ((data.iloc[0] == "C") | (data.iloc[0] == "CS")).values
    golang_fields_index = ((data.iloc[0] == "S") | (data.iloc[0] == "CS")).values

    goHeader = data.loc[1:2, golang_fields_index]
    csHeader = data.loc[1:2, cs_fields_index]

    goData = data.iloc[3:, golang_fields_index]
    csData = data.iloc[3:, cs_fields_index]

    if len(cs_fields_index) > 0:
        cs_files.append(fileName)
        GenCSTableManagerFile(fileName, csHeader)
        GenTableData(fileName, None, csData)

    if len(golang_fields_index) > 0:
        go_files.append(fileName)
        GenGoTableManagerFile(fileName, goHeader)
        GenTableData(fileName, goHeader, goData)


cs_files = []
go_files = []


def excel_start():
    excels = []
    for dir in os.listdir(excel_dir):  # 遍历当前目录所有文件和目录
        fileName = dir
        child = os.path.join(excel_dir, dir)  # 加上路径，否则找不到
        if os.path.isdir(child):  # 如果是目录，则继续遍历子目录的文件
            for file in os.listdir(child):
                if "~" in child:
                    continue
                if os.path.splitext(file)[1] == '.xlsx':  # 分割文件名和文件扩展名，并且扩展名为'proto'
                    fileName = file
                    processExcel(child, fileName)
                    excels.append(fileName)
        elif os.path.isfile(child):  # 如果是文件，则直接判断扩展名
            if "~" in child:
                continue
            if os.path.splitext(child)[1] == '.xlsx':
                processExcel(child, fileName)
                excels.append(fileName)

    genCSLoadTablesFile(cs_files)
    genGolangLoadTablesFile(go_files)
