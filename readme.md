# EVIL DNS

- 非常简单的DNS伪造服务器，用于某环境测试使用。主要功能为rebind DNS，以及简单的DNS伪造。

- 配置config.py中变量,即可

  ```
  REBIND_DOMAIN = ['rebind.com']
  FAKE_DOMAIN = {'test.com': "202.112.111.111"}
  ```

- 如果要使用rebind_domain，需配置权威指向该服务器

- 简单测试

  ```python
  # moxiaoxi @ moxiaoxideMacBook-Pro-3 in ~/Desktop/evil_dns [17:47:43]
  $ dig test.com @127.0.0.1
  
  ; <<>> DiG 9.10.6 <<>> test.com @127.0.0.1
  ;; global options: +cmd
  ;; Got answer:
  ;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 63768
  ;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 0
  
  ;; QUESTION SECTION:
  ;test.com.			IN	A
  
  ;; ANSWER SECTION:
  test.com.		0	IN	A	202.112.111.111
  
  ;; Query time: 1 msec
  ;; SERVER: 127.0.0.1#53(127.0.0.1)
  ;; WHEN: Tue Jul 09 17:47:59 CST 2019
  ;; MSG SIZE  rcvd: 42
  
  
  # moxiaoxi @ moxiaoxideMacBook-Pro-3 in ~/Desktop/evil_dns [17:47:59]
  $ dig baidu.com @127.0.0.1
  
  ; <<>> DiG 9.10.6 <<>> baidu.com @127.0.0.1
  ;; global options: +cmd
  ;; Got answer:
  ;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 52656
  ;; flags: qr rd ra; QUERY: 1, ANSWER: 2, AUTHORITY: 0, ADDITIONAL: 0
  
  ;; QUESTION SECTION:
  ;baidu.com.			IN	A
  
  ;; ANSWER SECTION:
  baidu.com.		47	IN	A	123.125.114.144
  baidu.com.		47	IN	A	220.181.38.148
  
  ;; Query time: 40 msec
  ;; SERVER: 127.0.0.1#53(127.0.0.1)
  ;; WHEN: Tue Jul 09 17:48:06 CST 2019
  ;; MSG SIZE  rcvd: 59
  
  
  # moxiaoxi @ moxiaoxideMacBook-Pro-3 in ~/Desktop/evil_dns [17:48:06]
  $ dig rebind.com @127.0.0.1
  
  ; <<>> DiG 9.10.6 <<>> rebind.com @127.0.0.1
  ;; global options: +cmd
  ;; Got answer:
  ;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 64137
  ;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 0
  
  ;; QUESTION SECTION:
  ;rebind.com.			IN	A
  
  ;; ANSWER SECTION:
  rebind.com.		0	IN	A	222.185.163.135
  
  ;; Query time: 0 msec
  ;; SERVER: 127.0.0.1#53(127.0.0.1)
  ;; WHEN: Tue Jul 09 17:48:19 CST 2019
  ;; MSG SIZE  rcvd: 44
  
  
  # moxiaoxi @ moxiaoxideMacBook-Pro-3 in ~/Desktop/evil_dns [17:48:19]
  $ dig rebind.com @127.0.0.1
  
  ; <<>> DiG 9.10.6 <<>> rebind.com @127.0.0.1
  ;; global options: +cmd
  ;; Got answer:
  ;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 34019
  ;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 0
  
  ;; QUESTION SECTION:
  ;rebind.com.			IN	A
  
  ;; ANSWER SECTION:
  rebind.com.		0	IN	A	127.0.0.1
  
  ;; Query time: 0 msec
  ;; SERVER: 127.0.0.1#53(127.0.0.1)
  ;; WHEN: Tue Jul 09 17:48:21 CST 2019
  ;; MSG SIZE  rcvd: 44
  
  
  ```

  

