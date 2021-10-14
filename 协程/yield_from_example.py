final_result = {}


def sales_sum(pro_name):
    totals = 0
    nums = []
    while True:
        x = yield  # 接受从跟外界传进来的值
        print(pro_name + "销量", x)
        if not x:
            break
        totals += x
        nums.append(x)
    return totals, nums  # 这里返回的值到了 final_result[key] = yield from sales_sum(key) 这里


def middle(key):
    while True:
        final_result[key] = yield from sales_sum(key)
        print(key + "销量统计完成")


def main():
    date_sets = {
        "bobby面膜": [1200, 1500, 1800],
        "bobby手机": [28, 55, 98, 108],
        "bobby大衣": [280, 560, 778, 70]
    }
    for key, data_set in date_sets.items():
        print("start_key", key)
        m = middle(key)
        m.send(None)  # 预激middle协程  -》 final_result[key] = yield from sales_sum(key)
        for value in data_set:
            m.send(value)
        m.send(None)
    print("final_result: ", final_result)


if __name__ == '__main__':
    main()
