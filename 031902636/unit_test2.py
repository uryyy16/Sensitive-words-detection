import unittest

import main

file_words = './words.txt'
file_org = './org.txt'
file_ans = './ans.txt'


class MyTestCase(unittest.TestCase):
    def test_something(self):
        new_text = main.Text(file_words)
        new_text.read_text(file_org)
        ans = '''Total: 9
Line2: <爸爸> 爸#$$%^爸
Line3: <dad> da^&^^d
Line3: <爸爸> 爸爸
Line3: <爸爸> 爸爸
Line3: <爸爸> 爸爸
Line3: <这样> 这木羊
Line3: <dad> DAD
Line4: <爸爸> 爸爸
Line4: <爸爸> 爸爸'''
        self.assertEqual(new_text.output(file_ans), ans)


if __name__ == '__main__':
    unittest.main()
