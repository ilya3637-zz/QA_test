from selenium import webdriver
import json

browser = webdriver.Chrome(executable_path='C:\\Users\\ilya.pospelov\\Downloads\\chromedriver.exe')
browser.set_window_size(1700, 800)
browser.get('https://area.mtg-bi.com/sign')


button_1 = browser.find_element_by_link_text('Sign IN')
button_1.click()
browser.implicitly_wait(10)

try:
	email_field = browser.find_element_by_id('signin-login')
	password_field = browser.find_element_by_id('signin-pass')
	button_2 = browser.find_element_by_xpath("//button[@class='btn btn-success capsbtn sign__submit']")

	browser.implicitly_wait(10)
	email_field.send_keys('testcaseqa5@gmail.com')
	password_field.send_keys('123456')
	button_2.click()

	print("Logging OK ")

	button_3 = browser.find_element_by_xpath("//i[@class='fas fa-user-circle fa-2x fa-fw text-white']")
	button_3.click()

	browser.implicitly_wait(3)
	button_4 = browser.find_element_by_xpath("//button[@class='btn btn-success capsbtn sign__submit']")
	button_4.click()
	print("Update OK ")
	#в идеале отследить изменения на странице и перебрать варианты с обновление для каждого поля профиля, и все отдельными мини тестами
except:
	print("Error ")

	#можно отлавливать разные ошибки, собирать их и красивый отчет делать
	

finally:
	print("END")

#надеюсь, что для подтверждения базовых навыков и знаний достаточно будет столько кода