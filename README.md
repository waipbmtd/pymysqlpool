# MySQL 数据库连接池组件

`pymysqlpool` 是数据库工具包中新成员，目的是能提供一个比较实用的数据库连接池中间件，从而避免在应用中频繁地创建和释放数据库连接资源，导致系统在进行数据库查询时效率低下。

# 功能

1. 提供尽可能紧凑的接口用于数据库操作；
2. 连接池的管理位于包内完成，客户端只需要提交 SQL 请求，并等待结果即可；
3. 将最大程度地与 `dataobj` 等兼容，便于使用；
4. 内部使用优先级队列（线程安全）管理已经创建的连接对象。

# 依赖
1. `pymysql`：将依赖该工具包完成数据库的连接等操作。

# 日志
## 2017.06.15 周四
1. 初步完成连接池的编写；
1. 