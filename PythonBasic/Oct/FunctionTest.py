
# 需求：计算字符串的长度
str1 = "Hello Python"
str2 = "你好，世界"
str3 = "你好 Python"
def myStringLengthFunction(str):
    count = 0
    for i in str:
        count += 1
    return count


print(myStringLengthFunction(str1))
print(myStringLengthFunction(str2))
print(myStringLengthFunction(str3))

print(len(str1))

print("------------------------")

def test_nameless_fun(compute):
    res = compute(1, 2)
    print(f"结果是：{res}")

test_nameless_fun(lambda x, y: x + y)