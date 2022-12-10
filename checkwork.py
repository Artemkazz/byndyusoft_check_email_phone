import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://google.ru')
driver.implicitly_wait(10)
search = driver.find_element_by_class_name('gLFyf')
search.send_keys('Byndyusoft')
driver.find_element_by_class_name('gNO89b').click()
driver.find_element_by_class_name('eKjLze').click()
driver.find_element_by_link_text('О нас').click()
first_window = driver.current_window_handle
second_window = driver.window_handles[1]
driver.switch_to.window(second_window)
driver.execute_script("window.scrollBy(0, 500);")
driver.find_element_by_class_name('js-popup-callback-show').click()
email = driver.find_element_by_class_name('popup-callback__footer-contacts')
check_email = email.text
if check_email == 'sales@byndyusoft.com':
    print('Email совпадает с ожидаемым: sales@byndyusoft.com ')
else:
    print('Email не совпадает\n', 'Ожидаемый email: sales@byndyusoft.com\n', 'Отображаемый email:', check_email )
print('Номер телефона не указан.')

time.sleep(4)
driver.quit()
