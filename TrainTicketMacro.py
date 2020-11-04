from selenium import webdriver 
import sys
import telepot

TOKEN = sys.argv[0]  # get token from command-line
mc = '0000000'  # put telegram userId (userinfobot)
bot = telepot.Bot(TOKEN)

url = 'http://www.letskorail.com'
driver = webdriver.Chrome('C:/chromedriver.exe')
driver.get(url)
my_id = '00000000'  # your id
my_pw = '00000000'  # your password
login_button = driver.find_element_by_xpath("//a[@onclick='return m_login_link()']")  # Login button element
login_button.click()  # Click the login button
driver.find_element_by_xpath("//input[@id='txtMember']").send_keys(my_id)  # put id
driver.find_element_by_xpath("//input[@id='txtPwd']").send_keys(my_pw)  # put pw
driver.find_element_by_xpath("//img[@alt='확인']").click()  # Click the login button

start = '서울'
end = '천안아산'
year = '2020'
month = '11'
day = '20'
s_time = '08:15'  # Enter the actual train departure time 

driver.find_element_by_xpath("//input[@id='txtGoStart']").clear()  # departure clear
driver.find_element_by_xpath("//input[@id='txtGoStart']").send_keys(start)  # Enter departure
driver.find_element_by_xpath("//input[@id='txtGoEnd']").clear()  # destination clear
driver.find_element_by_xpath("//input[@id='txtGoEnd']").send_keys(end)  # Enter destination
driver.find_element_by_xpath("//img[@alt='달력']").click()  # Click on calendar
driver.switch_to.window(driver.window_handles[1])  # Go to the latest pop-up window
driver.find_element_by_xpath('//span[@id="{}"]'.format('d' + year + month + day)).click()  # Click on date
driver.switch_to.window(driver.window_handles[0])  # Return to original window
driver.find_element_by_xpath('//select[@id="time"]').click()  # Click on departure time
driver.find_element_by_xpath('//option[@value="{}"]'.format(s_time[:2])).click()  
# Click to get the unit of time from the departure time
driver.find_element_by_xpath('//img[@alt="승차권예매"]').click()  # Click to book tickets

# driver.find_element_by_xpath('//tbody/tr[1]/td[3]'.format(1)).text.split('\n')
# driver.find_element_by_xpath('//tbody/tr[1]/td[5]//img'.format(1)).get_attribute('alt')

success = 0  # Whether getting the cancellation ticket was successful
s_time = '08:15'  # departure time
while success == 0:  # If the cancellation ticket reservation is not successful, repeat continuously
    time_find = 0  # The success of finding the departure time
    for i in range(1, 10):  # Search from line 1 to line 10
        depart = driver.find_element_by_xpath('//tbody/tr[{}]/td[2]'.format(i)).text.split('\n')[1]
        ym = driver.find_element_by_xpath('//tbody/tr[{}]/td[6]//img'.format(i)).get_attribute('alt')  # economy room inquiry
        if depart == s_time:  # If the departure time coincides
            if ym == '예약하기':  # If reservation is possible
                print('기차표가 예매되었습니다')
                success = 1
                driver.find_element_by_xpath('//tbody/tr[{}]/td[5]//img'.format(i)).click()  # Click to book
            else:
                driver.find_element_by_xpath("//img[@alt='조회하기']").click()  # Click to view
                print('아직 자리가 없습니다')
            time_find = 1
        if time_find == 1:
            break


bot.sendMessage(mc, '기차 표를 예매했습니다.')  # Send reservation completion message
