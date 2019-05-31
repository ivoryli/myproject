import sys
import re

# port = sys.argv[1]
# fd = open("1.txt")
# while True:
#     data = ''
#     for line in fd:
#         if line != '\n':
#             data += line
#         else:
#             break
#     # print(">>>s>>>>",data)
#
#     #匹配字符串首个单词
#     key_word = re.match(r'\S+',data).group()
#     if key_word == port:
#         #匹配目标内容
#         pattern = r"[0-9a-f]{4}\.[0-9a-f]{4}\.[0-9a-f]{4}"
#         pattern1 = r"(\d{1,3}\.){3}\d{1,3}/\d+|Unknow"
#         try:
#             address = re.search(pattern,data).group()
#             print(address)
#             address1 = re.search(pattern1,data).group()
#             print(address1)
#         except:
#             print("No address")
#         break
#     if not data:
#         print("Not Found the %s"%port)
#         break

# myself
# cmd = sys.argv[1]
# fd = open("./RE/1.txt")
# s = ''
# while True:
#     data = fd.read(1024)
#     if not data:
#         break
#     s += data
#
# fd.close()
# L = s.split("\n")
# # print(L)
# flag = False
# for item in L:
#     if not flag:
#         start = re.findall("^\S+",item)
#     # print(start[0])
#         try:
#             if start[0] == cmd:
#                 flag = True
#         except Exception:
#             continue
#     if flag:
#         # print(item)
#         #findall里不能用(),代表第几项
#         # address = re.findall(r"(\d{1,3}\.){3}\d{1,3}/\d+",item)
#         address = re.search(r"(\d{1,3}\.){3}\d{1,3}/\d+",item)
#         if address:
#             address = address.group()
#         if address:
#             print(address)
#             break
