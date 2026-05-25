# 同步代码
import time # 记录耗时时间

# 模拟制作咖啡(同步: 按下按钮后，店员等咖啡做好)
def make_coffee_sync(name, time_cost):
    print(f"店员: 开始做{name} (需要{time_cost})秒")

    # 同步等待: 这期间店员啥也干不了,只能等
    time.sleep(time_cost)
    print(f"店员： {name}做好了!")


# 同步接单流程
def coffee_shop_sync():
    start_time = time.time()

    # 借一个单，等做好，再接下一个(串行)
    make_coffee_sync("美式咖啡", 3)
    make_coffee_sync("拿铁咖啡", 2)
    make_coffee_sync("卡布奇诺", 1)

    total_time = time.time() - start_time
    print(f"\n同步模式总耗时:{total_time: .1f}秒")



# 异步代码
import asyncio
import time

# 模拟制作咖啡（异步: 按下按钮后，店员去接下一个单，咖啡机自己做）
async def make_coffee_async(name, time_cost):
    print(f"店员: 开始做{name} (需要{time_cost})秒")
    # 异步等待: 这期间店员可以去接其他单，不阻塞，关键是await
    # await 只能在async def定义的函数内部使用
    await asyncio.sleep(time_cost)
    print(f"店员： {name}做好了!")


# 异步节点流程
async def coffee_shop_async():
    start_time = time.time()
    # 同时接3个单，咖啡机并行制作(并发)
    # 把多个异步任务(协程)收集到一起，让他们并发执行,然后等待所有任务都完成，再汇总结果
    await asyncio.gather(

        make_coffee_async("美式咖啡", 3),
        make_coffee_async("拿铁咖啡", 2),
        make_coffee_async("卡布奇诺", 1)
    )

    total_time = time.time() - start_time
    print(f"\n异步模式总耗时:{total_time: .1f}秒")



# 运行同步版本
# if __name__ == "__main__":
#     print("=======同步接单模式=======")
#     coffee_shop_sync()
if __name__ == "__main__":
    print("=======异步接单模式=======")
    asyncio.run(coffee_shop_async())
