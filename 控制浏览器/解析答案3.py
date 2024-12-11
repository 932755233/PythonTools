from lxml import etree
import time
from selenium import webdriver
from selenium.common.exceptions import InvalidSelectorException, NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options

# from bs4 import BeautifulSoup
#
# soup = BeautifulSoup(open(r'C:\Users\Danny\Desktop\html\专题测验：试答回顾.html', 'rb'), "lxml")
#
# div = soup.find_all(attrs="deferredfeedback")
# print(div.find_all(attrs="qtext"))

# tree = lxml.html.fromstring(html);
# result = lxml.html.tostring(tree,pretty_print=True); #格式化输出
# print(result)
#
# td = tree.cssselect('tr#places_area__row > td.w2p_fw ')[0]#按节点找
# print(td.text_content())
#
# root = etree.Element("root")
# print(etree.tostring(root))
from selenium.webdriver.common.by import By

fileName = r'三'

html = etree.parse(r'C:\Users\Danny\Desktop\html\山东开放大学形成性考核%s：试答回顾.html' % fileName, etree.HTMLParser())
result = html.xpath('//div[contains(@class,"deferredfeedback")]')
# # print(etree.tostring(result))
#
# print(result[0].xpath('./div[@class="qtext"]/p')[0].text)
# print(html.xpath('./div[@class="qtext"]/p')[0].text)


chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
chrome_driver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)

isOk = 0
oktemp = 1


while oktemp == 1:
    divs = driver.find_elements(By.CLASS_NAME, "deferredfeedback")
    for div in divs:
        qtext = div.find_element(By.CLASS_NAME, 'qtext').text
        if -1 != qtext[10:].find('（'):
            qtext = qtext[10:qtext.find('（')]
        for lxmlDiv in result:
            lxmlQtext = lxmlDiv.xpath('*//div[contains(@class,"qtext")]/p')[0].text

            # if 'multichoiceset' in lxmlDiv.attrib.get('class'):
            #     lxmlSpans = lxmlDiv.xpath('*//div[contains(@class,"qtext")]/p/span')
            #     if len(lxmlSpans) > 0:
            #         lxmlQtext = lxmlSpans[0].text
            #         print('span---',lxmlQtext)
            # print(qtext, '---', lxmlQtext)

            if qtext in lxmlQtext:
                print(qtext, '---', lxmlQtext)
                if 'truefalse' in div.get_attribute('class'):
                    # 判断题
                    print('判断题:')
                    answer = lxmlDiv.xpath('*//div[contains(@class,"rightanswer")]')[0].text
                    if '对' in answer:
                        div.find_element(By.CLASS_NAME, "r0").find_element(By.TAG_NAME, 'input').click()
                        isOk = 1
                    else:
                        div.find_element(By.CLASS_NAME, "r1").find_element(By.TAG_NAME, 'input').click()
                        isOk = 1
                else:
                    # 选择题
                    print('选择题:')
                    answer = lxmlDiv.xpath('*//div[contains(@class,"rightanswer")]')[0].text
                    answer = answer[answer.find('：') + 1:]
                    print('答案' + answer)
                    answerDiv = div.find_element(By.CLASS_NAME, "answer").find_elements(By.XPATH, "./div")
                    for answerItem in answerDiv:
                        psss = answerItem.find_elements(By.CSS_SELECTOR, "p")
                        labelText = psss[0].text
                        if labelText.strip() in answer.strip():
                            inputItem = answerItem.find_element(By.TAG_NAME, "input")
                            inputItem.click()
                            isOk = 1

    if isOk == 1:
        oktemp = 1
    else:
        oktemp = 0
    if oktemp == 1:
        driver.find_elements(By.XPATH, '*//input[contains(@name,"next")]')[0].click()
        time.sleep(3)
        isOk=0