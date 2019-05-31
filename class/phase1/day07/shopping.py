commodity_info = {
    101: {"name": "屠龙刀", "price": 10000},
    102: {"name": "倚天剑", "price": 10000},
    103: {"name": "九阴白骨爪", "price": 8000},
    104: {"name": "九阳神功", "price": 9000},
    105: {"name": "降龙十八掌", "price": 8000},
    106: {"name": "乾坤大挪移", "price": 10000}
}

order_list = []

def buy_cid(shang_pin_info):
    cid = int(input("请输入商品编号："))
    if cid in shang_pin_info:
        return cid
    else:
        print("该商品不存在")
        return None

def buy(shang_pin_info):
    for key, value in shang_pin_info.items():
        print("编号：%d，名称：%s，单价：%d。" % (key, value["name"], value["price"]))
    while True:
        cid = buy_cid(shang_pin_info)
        if cid:
            break
    count = int(input("请输入购买数量："))
    order_list.append({"cid": cid, "count": count})
    print("添加到购物车。")

def display_count_commodity(order_list,commodity_info):
    total = 0
    for item in order_list:
        commodity = commodity_info[item["cid"]]
        print("商品：%s，单价：%d,数量:%d." % (commodity["name"], commodity["price"], item["count"]))
        total += commodity["price"] * item["count"]
    return total

def check_out(order_list,commodity_info):
    total = display_count_commodity(order_list,commodity_info)
    while True:
        money = float(input("总价%d元，请输入金额：" % total))
        if money >= total:
            print("购买成功，找回：%d元。" % (money - total))
            order_list.clear()
            break
        else:
            print("金额不足.")

def select_menu():
    """
        购物
    :return:
    """
    while True:
        item = input("1键购买，2键结算。")
        if item == "1":
            buy(commodity_info)
        elif item == "2":
            check_out(order_list,commodity_info)
select_menu()
