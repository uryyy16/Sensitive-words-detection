import main

file_words = './words.txt'
file_org = './org.txt'
file_ans = './ans.txt'


# 今天,在我家里发生了一件十分有趣的事。
# 中午，爸#$$%^爸正在睡觉，我正在看电视，忽然，我觉得十分无聊，于是，就想出了一个既解闷又有趣的游戏来。
# 我先拿着红、黄、蓝、绿这四种颜色，然后，跳上床去，用红色笔在da^&^^d嘴上画口红，用黄色笔给爸b画脸蛋，用蓝色笔给爸ba画左眼毛，最后，在用绿色笔画上了爸爸的右眼毛，就這木羊，我给DAD化了个妆。然后，我又去看电视了。
# 等爸爸一觉醒来，去梳头时，我便哈哈大笑起来，爸爸对着镜子一看，羞得满脸通红，连头也不敢抬起来了。


class MyTestCase(unittest.TestCase):
    def test_something(self):
        new_text = main.Text(file_words)
        new_text.read_text(file_org)
        ans = '''Total: 9
Line2: <爸爸> 爸#$$%^爸
Line3: <dad> da^&^^d
Line3: <爸爸> 爸b
Line3: <爸爸> 爸ba
Line3: <爸爸> 爸爸
Line3: <这样> 這木羊
Line3: <dad> DAD
Line4: <爸爸> 爸爸
Line4: <爸爸> 爸爸'''
        self.assertEqual(new_text.output(file_ans), ans)


if __name__ == '__main__':
    unittest.main()
