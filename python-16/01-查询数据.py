from pymysql import connect

class JD(object):
	def __init__():
		pass

	def show_all_items(self):
		"""显示所有商品"""
		# 创建Connection连接
    	conn = connect(host='localhost',port=3306,database='jing_dong',user='root',password='mysql',charset='utf8')
   		# 获得Cursor对象
    	cursor = conn.cursor()

		sql = "select * from goods;"
		cursor.execute(sql)
		for temp in cursor.fetchall():
			print(temp)

		# 关闭Cursor对象
		cursor.close()
		conn.close()

	def show_cates(self):
		"""显示所有商品分类"""
		# 创建Connection连接
    	conn = connect(host='localhost',port=3306,database='jing_dong',user='root',password='mysql',charset='utf8')
   		# 获得Cursor对象
    	cursor = conn.cursor()

		sql = "select name from goods_cates;"
		cursor.execute(sql)
		for temp in cursor.fetchall():
			print(temp)

		# 关闭Cursor对象
		cursor.close()
		conn.close()


	def run(self):
		while True:
			print('------京东-------')
			print("1:所有商品")
			print("2:所有商品分类")
			print("3:所有商品品牌分类")
			num = input("请输入功能对应的序号:")

			if num == "1":
				# 查询所有商品
				self.show_all_items()
			elif num == "2":
				pass
			elif num == "3":
				pass
			else:
				print("输入有误,重新输入...")

def main():
	# 1.创建一个京东商城对象
	jd=JD()
	# 2.调用这个对象的run方法,让其运行
	jd.run()

if __name__ =="__main__":
	main()