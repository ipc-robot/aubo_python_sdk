#! /usr/bin/env python
# coding=utf-8

import libpyauboi5

import time,threading


RS_SUCC = 0

RSHD = 0

result = -1

print(__name__)



def get_current_waypoint():
    result = libpyauboi5.initialize()

    # 创建robot service控制上下文
    RSHD = libpyauboi5.create_context()
    print("create_context RSHD={0}".format(RSHD))
    # 登陆服务器
    ip_addr = "127.0.0.1"

    port = 8899
    
    result = libpyauboi5.login(RSHD, ip_addr, port)

    if result == RS_SUCC:
        # 登陆成功
        print("login {0}:{1} succ.".format(ip_addr, port))

    waypoint = libpyauboi5.get_current_waypoint(RSHD)
    print("currrent waypoint={0}".format(waypoint))





def main():
    # 初始化libpyauboi5库
    result = libpyauboi5.initialize()

    # 创建robot service控制上下文
    RSHD = libpyauboi5.create_context()
    print("create_context RSHD={0}".format(RSHD))

    # 登陆服务器
    ip_addr = "127.0.0.1"

    port = 8899

    result = libpyauboi5.login(RSHD, ip_addr, port)

    if result == RS_SUCC:

        # 初始化机械臂控制全局属性

        libpyauboi5.init_global_move_profile(RSHD)
	

        joint_radian = (0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000)
        result = libpyauboi5.move_joint(RSHD, joint_radian)

        print("机械臂轴动1")

        time.sleep(0.2)

        joint_radian = (-0.000003, -0.127267, -1.321122, 0.376934, -1.570796, -0.000008)
        result = libpyauboi5.move_joint(RSHD, joint_radian)

        print("机械臂轴动2")

        time.sleep(0.2)


        #libpyauboi5.move_teach_start(RSHD, 9, 0)

        #time.sleep(4)

        #libpyauboi5.move_teach_stop(RSHD)

        #libpyauboi5.move_teach_start(RSHD, 9, 1)

        #time.sleep(4)

        #libpyauboi5.move_teach_stop(RSHD)


    else:  # 登陆失败
        print("login {0}:{1} failed.".format(ip_addr, port))  # 释放robot service控制上下文

    # 删除上下文
    libpyauboi5.destory_context(RSHD)

    # 反初始化libpyauboi5库
    libpyauboi5.uninitialize()



t = threading.Thread(target = get_current_waypoint)
t.start()
t.join()


if __name__ == "__main__":

    count = 1
    while count < 200:
        print("************************mission start({0})*****************************".format(count))
        main()
        get_current_waypoint()
        count += 1
        print("************************mission completed!************************")


