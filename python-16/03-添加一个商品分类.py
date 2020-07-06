from pymysql import connect

class JD(object):
	def __init__(self):
		# 创建Connection连接
		self.conn = connect(host='localhost',port=3306,database='jing_dong',user='root',password='1234',charset='utf8')
   		# 获得Cursor对象
		self.cursor = self.conn.cursor()

	def __del__(self):
    	# 关闭Cursor对象
		self.cursor.close()
		self.conn.close()

	def execute_sql(self,sql):
		self.cursor.execute(sql)
		for temp in self.cursor.fetchall():
			print(temp)

	def show_all_items(self):
		"""显示所有商品"""
		sql = "select * from goods;"
		self.execute_sql(sql)

	def show_brands(self):
		sql = "select * from goods_brands;"
		self.execute_sql(sql)

	def add_brands(self):
		item_name = input("请输入一个新的名字:")
		sql = """insert into goods_brands (name) values("%s")""" % item_name
		self.cursor.execute(sql)
		self.conn.commit()

	def show_cates(self):
		"""显示所有商品分类"""
		sql = "select name from goods_cates;"
		self.execute_sql(sql)

	def print_menu(self):
		print('------京东-------')
		print("1:所有商品")
		print("2:所有商品分类")
		print("3:所有商品品牌分类")
		print("4:添加一个商品分类")
		num = input("请输入功能对应的序号:")
		return num

	def run(self):
		while True:
			num = self.print_menu()

			if num == "1":
				# 查询所有商品
				self.show_all_items()
			elif num == "2":
				self.show_cates()
			elif num == "3":
				self.show_brands()
			elif num == "4":
				self.add_brands()
			else:
				print("输入有误,重新输入...")

def main():
	# 1.创建一个京东商城对象
	jd=JD()
	# 2.调用这个对象的run方法,让其运行
	jd.run()

if __name__ =="__main__":
	main()