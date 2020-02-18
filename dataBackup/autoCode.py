from splinter.browser import Browser
import time
import datetime

class lecture(object):
	driver_name = 'chrome'
	browser = Browser(driver_name)

	# 易班账号
	username = '账号'
	password = '密码'

	# 讲座信息
	# go=后面加报名链接
	login_url = 'http://www.yiban.cn/login?go=报名链接'
	# 报名链接
	baoming_url = '报名链接'

	# 报名时间
	apply_time = '2019-10-25 19:00:00'

	# 个人信息
	department = '学院'
	myclass = '班级'
	stu_number = '学号'
	mobile_num = '手机号'
	profession = '专业'


	def login(self):
		# browser = Browser(self.driver_name)
		self.browser.visit(self.login_url)
		self.browser.find_by_xpath('//*[@id="account-txt"]').fill(self.username)
		self.browser.find_by_xpath('//*[@id="password-txt"]').fill(self.password)
		self.browser.click_link_by_id('login-btn')

		print(u"请自行输入验证码登录...\n")


		while True:
			if self.browser.url != self.baoming_url:
				time.sleep(1)
			else:
				print('登录成功！\n')
				break

	def getLecture(self):
		# now_time = datetime.datetime.now()
		try:
			txt = self.browser.find_by_xpath('//*[@id="enroll-view"]/div/div[1]').text
			print(txt)
			print('\n')

		except:
			pass

		target_time = datetime.datetime.strptime(self.apply_time, '%Y-%m-%d %H:%M:%S')
		start_time = 10
		print("离开始时间还有：\n")
		while start_time != 0:
			now_time = datetime.datetime.now()
			start_time = (target_time - now_time).seconds
			print(start_time)
			time.sleep(1)

		
		self.browser.reload()
		print(datetime.datetime.now())
		try:
			self.browser.click_link_by_text('开始报名')
			

			self.browser.find_by_xpath('//*[@id="enroll-view"]/div[2]/ul/li[1]/div[2]/textarea').fill(self.department)
			link_text1 = self.browser.find_by_xpath('//*[@id="enroll-view"]/div[2]/ul/li[1]/div[4]/a').text
			self.browser.click_link_by_text(link_text1)

			self.browser.find_by_xpath('//*[@id="enroll-view"]/div[2]/ul/li[2]/div[2]/textarea').fill(self.myclass)
			link_2 = self.browser.find_by_xpath('//*[@id="enroll-view"]/div[2]/ul/li[2]')
			link_2.find_by_tag('a').click()

			self.browser.find_by_xpath('//*[@id="enroll-view"]/div[2]/ul/li[3]/div[2]/textarea').fill(self.stu_number)
			link_3 = self.browser.find_by_xpath('//*[@id="enroll-view"]/div[2]/ul/li[3]')
			link_3.find_by_tag('a').click()

			self.browser.find_by_xpath('//*[@id="enroll-view"]/div[2]/ul/li[4]/div[2]/textarea').fill(self.mobile_num)
			link_4 = self.browser.find_by_xpath('//*[@id="enroll-view"]/div[2]/ul/li[4]')
			link_4.find_by_tag('a').click()

			self.browser.find_by_xpath('//*[@id="enroll-view"]/div[2]/ul/li[5]/div[2]/textarea').fill(self.profession)
			link_text5 = self.browser.find_by_xpath('//*[@id="enroll-view"]/div[2]/ul/li[5]/div[4]/a').text
			self.browser.click_link_by_text(link_text5)

			print('报名成功！')
			print(datetime.datetime.now())
			
		except:
			print('没了！下次再来吧！')
		
		

def exitpy():
	print("按 q 结束程序")
	tuichu = input()
	if tuichu.lower() == 'q':
	    exit(0)

if __name__ == '__main__':
	
	lecture=lecture()	
	lecture.login()
	lecture.getLecture()
	time.sleep(20)
	exitpy()
	

