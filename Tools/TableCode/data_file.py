from const import go_table_data_dir


def GenTableData(tableName, headers, data):
    filePath = go_table_data_dir + tableName + ".txt"

    fileContent = ""

    if headers is not None:
        # write cols name
        fileContent += "\t".join(headers.iloc[1].values)
        fileContent = fileContent.rstrip()
        fileContent += "\n"

    for row in range(len(data.index)):
        for ncols in range(len(data.columns)):
            fileContent += f"{data.iloc[row, ncols]}\t"
        fileContent = fileContent.rstrip('\t')
        fileContent += "\n"

    fo = open(filePath, "wb")
    fo.write(fileContent.encode('utf-8'))
    fo.close()
