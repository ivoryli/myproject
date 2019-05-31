fmt = '{0:{1}}'

#0第一个元素:'Invoice #1234'  ":" 后面是宽度
#{1} 表示format的实参第2个元素(嵌套)

width = 15
print(fmt.format('Invoice #1234', width))

width = 3
print(fmt.format('Invoice #1234', width))