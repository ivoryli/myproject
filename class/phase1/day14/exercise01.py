def get_score():
    while True:
        try:
            n = int(input("请输入成绩:"))
        except ValueError:
            print("输入有误")
            continue

        if 0 < n < 101:
            return n

        print("成绩不在范围内")

get_score()
