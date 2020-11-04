import pymysql

# 1连接数据库
db = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='root', db='python', charset='utf8')
# 2创建游标
cursor = db.cursor()


# 写入数据
def _insert_data(pic_name, time, pic_data):
    sql = "insert into pic_save values (NULL, '%s', '%s', '%s')" %(pic_name, time, pic_data)
    cursor.execute(sql)


_insert_data('12121', '2020-08-21 12:29:50', 'sdasdasadas')
