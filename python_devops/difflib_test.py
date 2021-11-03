import difflib,sys
'''text1 = """123454848646
        51313135156"""
text1_lines = text1.splitlines()
text2 = """1234k48486k6
        s13k13515ka"""
text2_lines = text2.splitlines()
#d = difflib.Differ()
#diff = d.compare(text1_lines,text2_lines)
#print('\n'.join(list(diff)))
d = difflib.HtmlDiff()
print(d.make_file(text1_lines,text2_lines))'''

try:
    textfile1 = sys.argv[1]
    textfile2 = sys.argv[2]
except Exception as e :
    print("Error:"+str(e))
    print("Usage: difflib_test.py filename1 filename2")
    sys.exit()

def readfile(filename):
    try:
        fileHandle = open(filename,'r')             #只读就行，rb 会生成  List[bytes] 类型，列表内数据必须是str类型 List[str] 
        text = fileHandle.read().splitlines()
        fileHandle.close()
        return text
    except IOError as error :
        print('Read file Error:'+str(error))
        sys.exit()

if textfile1 == "" or textfile2 == "":
    print("Usage: difflib_test.py filename1 filename2")
    sys.exit()

text1_lines = readfile(textfile1)
text2_lines = readfile(textfile2)

d = difflib.HtmlDiff()
print(d.make_file(text1_lines,text2_lines))
