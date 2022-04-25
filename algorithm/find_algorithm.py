# 汉罗塔
def hanoi(n, a, b, c):  # 注：参数n 表示 n个盘子 ； a、b、c表示这3个参数表示这三个盘子的名字
    if n > 0:  # 注：递归终止条件是 n = 0 的时候  一步都不需要移动(没有盘子)
        # 注：第一步 (n-1, a, c, b) --> n-1个盘子 从a经过 b 移动到c
        hanoi(n - 1, a, c, b)  # 注：把n-1个盘子从A经过C移动到B    调用自己 n-1个盘子 从a经过b移动到c
        # print("#%d: moving from %s to %s." % (num, a, c))   # 注：第2步 最大的盘子 从a移动到c
        print("moving from %s to %s." % (a, c))
        hanoi(n - 1, b, a, c)  # 注：n-1个盘子 从 b 经过 a 移动到 c


# 注：每次移动都只是柱子最上面那个
hanoi(3, 'A', 'B', 'C')


# 顺序查找
def linear_search(li, val):  # 注：li列表 ；val待查找的元素
    for ind, v in enumerate(li):  # 注：因为要返回个下标 所以用 enumerate index和值都需要
        if v == val:  # 注：如果v == 我们要找的那个值 那就返回 它的index
            return ind
    else:  # 如果for循环结束后还没有找到 返回None
        return None


#  二分查找
def binary_search(li, val):  # li 列表  val待查找的值
    left = 0
    right = len(li) - 1
    while left <= right:  # 注：循环条件 说明候选区有值
        mid = (left + right) // 2  # 注：中间值(下标) 是整除2
        if li[mid] == val:  # 注：== 找到的情况   每次对比都是对比的li[mid]
            return mid  # 注：返回下标 mid
        elif li[mid] > val:  # 注：代表 待查找的值val在 mid左边
            right = mid - 1  # 注：更新候选区了 这种情况就可以继续循环
        else:  # 注：第3种情况 li[mid] < val  待查找的值在mid右侧
            left = mid + 1  # 注：更新候选区  继续循环
    else:
        return None  # 注：如果找不到的情况 即不满足 left <= right 时

