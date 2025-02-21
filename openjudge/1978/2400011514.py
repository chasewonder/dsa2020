def next_peak_day(p, e, i, d):
    cycle_length = 23 * 28 * 33  # 21252
    x = p  # 从 p 开始找符合所有条件的 x
    while (x - e) % 28 != 0 or (x - i) % 33 != 0 or x <= d:
        x += 23  # 每次增加 23（最小的模数）以加快搜索速度
    return x - d  # 计算距离 d 的天数

# 读取输入
p, e, i, d = map(int, input().split())
print(next_peak_day(p, e, i, d))
