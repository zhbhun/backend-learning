# [Nginx](https://nginx.org/)

- [官方文档](https://nginx.org/en/docs/)
- [中文文档](https://tengine.taobao.org/nginx_docs/cn/docs/)
- [中文社区](https://www.nginx.org.cn/)

## 入门

https://tengine.taobao.org/nginx_docs/cn/docs/http/ngx_http_core_module.html#variables

### http

- [ngx_http_core_module](https://tengine.taobao.org/nginx_docs/cn/docs/http/ngx_http_core_module.html#location)

#### location

匹配顺序

1. 先精准匹配 = ，精准匹配成功则会立即停止其他类型匹配；
2. 没有精准匹配成功时，进行前缀匹配。先查找带有 ^~ 的前缀匹配，带有 ^~ 的前缀匹配成功则立即停止其他类型匹配，普通前缀匹配（不带参数 ^~ ）成功则会暂存，继续查找正则匹配；
3. = 和 ^~ 均未匹配成功前提下，查找正则匹配 ~ 和 ~* 。当同时有多个正则匹配时，按其在配置文件中出现的先后顺序优先匹配，命中则立即停止其他类型匹配；
4. 所有正则匹配均未成功时，返回步骤 2 中暂存的普通前缀匹配（不带参数 ^~ ）结果。


参考文献

- [nginx location配置](https://segmentfault.com/a/1190000022173920)
- [一文理清 nginx 中的 location 配置（系列一）](https://segmentfault.com/a/1190000022315733)
- [一文弄懂Nginx的location匹配](https://segmentfault.com/a/1190000013267839)

### rewrite

- [一文理清 nginx 中的 rewrite 配置（系列二）](https://segmentfault.com/a/1190000022407797)

### alias vs root

- [Nginx虚拟目录alias和root目录](https://cloud.tencent.com/developer/article/1026992)

### 反向代理

- [ngx_http_proxy_module](https://tengine.taobao.org/nginx_docs/cn/docs/http/ngx_http_proxy_module.html)
- [nginx 之 proxy_pass详解](https://www.jianshu.com/p/b010c9302cd0)

## 进阶

### 容器

- [Nginx 容器教程](http://www.ruanyifeng.com/blog/2018/02/nginx-docker.html)

## 参考文献

- [Nginx 入门指南](https://www.w3cschool.cn/nginx/)
- [Nginx 使用手册](https://www.w3cschool.cn/nginxsysc/)
