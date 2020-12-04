
#yield生成器，要读取一个很大的文件，一次读取太耗内存，一行一行的读取，就要用到生成器, 只能通过next方法获取下一个值

def provider():
    for i in range(0,10):
        print("开始操作")
        yield i #相当于return i, 同时记录了上一次的执行位置
        print("结束操作")

p = provider()
print(p)
print(next(p))
print(next(p))
print(next(p))
print(next(p))
print(next(p))