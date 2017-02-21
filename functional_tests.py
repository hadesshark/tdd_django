from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith 聽到一個很酷的新線上待辦事項 app。
        # 她去查看它的首頁
        self.browser.get('http://localhost:8000')

        # 她發現網頁標題與標頭顯示待辦事項清單
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

        # 她馬上受邀輸入一個待辦事項

        # 她在文字方塊輸入“購買孔雀羽毛”
        #（Edith 的興趣是綁蒼蠅魚餌）

        # 當她按下 enter 時，網頁會更新，現在網頁列出
        # "1: 購買孔雀羽毛"，一個待辦事項清單項目

        # 此時仍然有一個文字方塊，讓她可以加入另一個項目。
        # 她輸入“使用孔雀羽毛來製作一隻蒼蠅”（Edith 非常有條理）

        # 網頁再次更新，現在她的清單有這兩個項目

        # Edith 不知道網站能否記得她的清單
        # 接著她看到網站產生一個唯一的 URL 給她
        # 網頁有一些文字說明這個效果

        # 她前往那個 URL - 她的待辦清單仍然在那裡。

        # 她很滿意地上床睡覺

        browser.quit()

if __name__ == '__main__':
    unittest.main(warnings='ignore')
