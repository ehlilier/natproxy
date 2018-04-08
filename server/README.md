## 各个文件说明

--server.py  开启文件主线程，并开始执行

--db_transfer  不太明白，被server.py引用

--eventloop.py  被前者引用 会读取config.json文件。感觉这里是核心实现的功能，最核心的部分之一。但是还是不懂用的什么技术啊.因为这里的方法很多基于依赖模块，所以有很多地方看不太懂。先看一下其它模块实现了哪些方法吧
    1. 事件循环机制需要了解，Python中的

--server_pool 我怎么觉得这个才是最核心的内容呢。然而并没有看出什么东西来


## 常见模块的用法
1. select select.select()文件描述符？怎么使用的哦，这里一点都不了解啊
r, w, e = select.select(self.conn_rd, [], [], 0.5) 这里的作用是什么？


## 需要知道的函数功能
1. socketBridge
2. dispose() 处理执行
3. json.load()  加载文件（读取？）
4. http.service() 功能是什么 返回什么

--common_func.py 里面存在的疑问

1. select_recv() ??? return buff
2. SocketBridge 类，主要记录socket的一些信息，进行两个套接字的交换数据
    * add_conn_pair 给SocketBridge中的属性进行赋值
    * get_thread 获取当前线程实例
    * start_as_daemon() 对daemon根本不理解
    * start() 执行_start()
    * _start() memoryview()? 不理解
    * `_rd_shutdown()` 暂停连接，但是不是关闭，和close不一样
    * `_wr_shutdown()`和上面类似，配对的连接都需要被停止掉  这里看注释比较清晰
    * _terminate() 会清理之前所有的赋值 并且关掉连接  连接关闭之后会执行相应的回调函数啊

3. CtrlPkg 类 主要用于数据的打包和解包吧
    * 几个常量的理解  struct数据类型是个什么鬼？
    * `_build_bytes()` `data_ebcode()` `data_decode`()  转换数据为字节格式
    * `type_name()`  `__str__()` `__repr__()` 对一些信息的处理，并返回  便于理解的？
    * `_prebuilt_pkg`用于缓存包
    * recalc_crc32() clean_crc() 对秘钥进行循环冗余检验 哈哈哈
    * verify() 验证响应包  握手响应包  握手包。。。暂时不知道会用在哪里  返回布尔值
    * decode_only() 解码字节包为CtrlPkg的实例 解包之后，传入CtrlPkg中，构造了一个实例。。。
    * decode_verify() 解包并且验证
    * pbuild_hs_m2s pbuild_hs_s2m  pbuild_heart_beat 主要是为了兼容  因为版本不同的原因吧，为了同时支持Python2.7版本

    **总结**
    1. 查找文档之后，其实都很简单的方法的  有些地方还不太清晰。比如一些函数的使用，看英文文档没有看懂的地方。
    
      