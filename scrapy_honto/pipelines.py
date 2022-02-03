# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import datetime
import os
import pymysql

class ScrapyHontoPipeline(object):
    _db = None

    @classmethod
    def get_database(cls):
        cls._db = pymysql.connect(
            host='localhost',
            user='root',
            password='password',
            db='hontodb',
            charset='utf8',
            cursorclass=pymysql.cursors.DictCursor,)

        with cls._db.cursor() as cursor:
            cursor.execute('CREATE TABLE IF NOT EXISTS honto (id INT AUTO_INCREMENT, book_title VARCHAR(255) NOT NULL, PRIMARY KEY (id));')
        
        cls._db.commit()
        return cls._db

        # # テーブル作成
        # cursor = cls._db.cursor()
        # cursor.execute(
        #     'CREATE TABLE IF NOT EXISTS honto (id INT AUTO_INCREMENT, book_title VARCHAR(255) NOT NULL, PRIMARY KEY (id));')
        # cursor.close()
        # return cls._db

    def process_item(self, item, spider):
        """
        Pipeline にデータが渡される時に実行される
        item に spider から渡された item がセットされる
        """
        self.save_item(item)
        return item

    def save_item(self, item):
        """
        item を DB に保存する
        """
        if self.find_item(item['book_title']):
            print('スキップ')
            # 既に同じURLのデータが存在する場合はスキップ
            return


        db = self.get_database()
        with db.cursor() as cursor:
            sql = 'INSERT INTO honto VALUES (%s, %s)'
            cursor.execute(sql, (0, item['book_title']))
        db.commit()

    def find_item(self, book_title):
        db = self.get_database()
        with db.cursor() as cursor:
            sql = 'SELECT * FROM honto WHERE book_title = %s'
            cursor.execute(sql, book_title)
        # db.commit()
        return cursor.fetchone()

# class ScrapyHontoPipeline(object):
#     _db = None

#     @classmethod
#     def get_database(cls):
#         cls._db = pymysql.connect(
#             host='localhost',
#             user='root',
#             password='password',
#             db='hontodb',
#             charset='utf8',
#             cursorclass=pymysql.cursors.DictCursor,)

#         with cls._db.cursor() as cursor:
#             cursor.execute('CREATE TABLE IF NOT EXISTS honto (id INT AUTO_INCREMENT, book_title VARCHAR(255) NOT NULL, PRIMARY KEY (id));')
        
#         cls._db.commit()
#         return cls._db

#         # # テーブル作成
#         # cursor = cls._db.cursor()
#         # cursor.execute(
#         #     'CREATE TABLE IF NOT EXISTS honto (id INT AUTO_INCREMENT, book_title VARCHAR(255) NOT NULL, PRIMARY KEY (id));')
#         # cursor.close()
#         # return cls._db

#     def process_item(self, item, spider):
#         """
#         Pipeline にデータが渡される時に実行される
#         item に spider から渡された item がセットされる
#         """
#         self.save_item(item)
#         return item

#     def save_item(self, item):
#         """
#         item を DB に保存する
#         """
#         if self.find_item(item['book_title']):
#             print('スキップ')
#             # 既に同じURLのデータが存在する場合はスキップ
#             return


#         db = self.get_database()
#         with db.cursor() as cursor:
#             sql = 'INSERT INTO honto VALUES (%s, %s)'
#             cursor.execute(sql, (0, item['book_title']))
#         db.commit()

#     def find_item(self, book_title):
#         db = self.get_database()
#         with db.cursor() as cursor:
#             sql = 'SELECT * FROM honto WHERE book_title = %s'
#             cursor.execute(sql, book_title)
#         # db.commit()
#         return cursor.fetchone()
