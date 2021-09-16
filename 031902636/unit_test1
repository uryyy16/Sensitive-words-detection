import unittest

import main

file_words1 = './words1.txt'
file_words = './words.txt'
file_org = './org.txt'


class MyTestCase(unittest.TestCase):
    # 测试读入敏感词文件并将敏感词的所有可能形式映射为数字
    def test_read_sensitive_words(self):
        s = main.Sensitive_words()
        ans = [([4, 18, 2, 9], 0)]
        self.assertEqual(s.read_sensitive_words(file_words1), ans)

    # 测试将符号改为#并合并被拆开的汉字
    def test_read_text(self):
        t = main.Text(file_words)
        ans = '法#轮#功#法轮#功邪#教#'
        self.assertEqual(t.read_text(file_org), ans)


if __name__ == '__main__':
    unittest.main()
