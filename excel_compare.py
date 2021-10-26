import xlwings as xw ,re
target_excel = xw.Book('路径：目标文件文件')
source_excel = xw.Book('路径：对照文件')

target_sheet = target_excel.sheets[0]   # 0：第一个sheet  1：第二个sheet
def get_rows():                         #行数统计，判断该行是否有数据，有则count+1  注：默认中间没有空白行
    count = 0
    for i in target_sheet.range('a:a').value :
        if i != None :
            count += 1
    return count
rows=get_rows()
target_colmun = target_sheet.range(('d2:d%d' % rows)).value    #选择区域，可带参   列行：列行

source_sheet = source_excel.sheets[1]     # 0：第一个sheet  1：第二个sheet
source_colmun = source_sheet.range('e2:e1873').value

result=[]      #创建空列表存储返回的数据
for j in target_colmun:
    pattern = re.compile(('%s' % j))
    result.append(pattern.findall(str(source_colmun)))
print(result)

for i in target_colmun:
    if i not in str(result):
        print(i)

target_excel.close()