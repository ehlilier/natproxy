
<!-- master文件的主要作用是什么呢？ -->

### 两个类

Master

    几个需要清楚的东西：
        1. thread_pool  线程池
        4. working_pool  这又是什么
        3. slaver_pool 用来保存客户端的套接字（IP+port）和地址
        2. spare_slaver  多余的客户连接
        3. working_slaver  正在工作的连接
        4. listen_slaver
        5. collections.deque() 创建一个和list一样的结构
        6. _fmt_communicate_addr
        7. customer_listen_addr
        8. communicate_addr master的IP地址
        9. customer_listen_addr customer的IP地址

    函数：
        1. _fmt_communicate_addr
        2. _listen_slaver  用于服务器监听请求，并保存客户端的信息（套接字和地址）
        3. _listen_customer 和上面函数的区别是什么呢？ 做法一致 但是多了一步
            pending_customers 是一个队列，客户端的连接还未被指定为slaver 有注释
        4. try_bind_port 绑定端口号 关键点在于 sock.bind(addr)

        5. _heart_beat_daemon 心跳包。看注释就可以了。通信过程咯
        6. _send_heartbeat() 心跳开始哦 也就是发送数据给远端主机啦
            回顾两个函数： pkg.pbuild_heart_beat().raw
            pkg.recv()

        7. _assign_slaver_daemon()  初始化守护子线程 为customer 分配给 slaver
        8. _get_an_active_slaver() 
            dict_slaver, conn_slaver, try_count 
            如果conn_slaver可以握手成功，就返回它。
        
        9. _handshake 在数据进行交互前，前进行握手操作。三次握手的实现就在这里了
            select_recv() 
            返回值为布尔值，无非就是判断握手是否成功，也就是判断数据发送出去之后，传回来的值是否正确。
        10. _serve_customer() 这里的注释比较清晰。就是交换数据啦

        11. dispose() 出掉连接 一个一个销毁，很恐怖的样子
        12. serve_forever()  启动线程
总结：所以Master类主要做了些什么呢？创建了几个线程，实现数据传输过程中握手，建立连接，发送数据等过程。

Master_line:
    属性：
        1. 主要是Master中的属性
    函数：
        1. dispose 用于撤销操作
        2. run_master 用于启动线程
        3. main_master 为一些属性复制
总结：主要用来执行Master吧
--Master_line