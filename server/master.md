
<!-- master文件的主要作用是什么呢？ -->

### 两个类

--Master
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

        7. _assign_slaver_daemon()  守护子线程
        8. _get_an_active_slaver()
--Master_line