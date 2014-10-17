# -*- coding: utf-8 -*- # use Korean(unicode charset)
# can use Korean(unicode charset) for arguments 
# import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')

# from pyExcelerator import *

# SourceFilePath = './'
# SourceFileName = 'data.xls'

# w = Workbook()
# ws = w.add_sheet('Copied Cell')

# count = 0

# s = '은마'

# for sheet_name, values in parse_xls(SourceFilePath+SourceFileName, 'utf-8'): 
# 	for row_idx, col_idx in sorted(values.keys()):
# 		v = values[(row_idx, col_idx)]
# 		print '(%d, %d) =' % (row_idx, col_idx), v
# 		if(type(v) is unicode):
# 			#a = v.find(s)
# 			#print a,'임'
# 			tmp = str(v)
# 			if tmp.find(s) >= 0:
# 				count = count +1 #count 
# 		ws.write(row_idx, col_idx,v)

# print s, '문자열이 포함된 셀의 수는', count, '개 입니다.'
# w.save('copiedfile.xls')

ww = [1,2,3,21,23]
file = open('a.txt','w')
for i in ww:
	file.write(str(i)+'\n')


# lines = file.readlines()
# line = 'Happy Python'
# file.write(line+'\n')
# print >> file,line
file.close()
