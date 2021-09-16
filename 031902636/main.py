import string

import pypinyin
import copy
import re
import sys

import init_map
import Chinese_split

Chinese_split_map = {}
pinyin_alphabet_map = init_map.pinyin_alphabet_map()
pinyin_alphabet_map['#'] = 0
# print(pinyin_alphabet_map)

file_words = './words.txt'
file_org = './org.txt'
file_ans = './ans.txt'

# file_words = sys.argv[1]
# file_org = sys.argv[2]
# file_ans = sys.argv[3]

original_sensitive_words = []


class Sensitive_words:
    def __init__(self):
        # [[num1,num2,num3,……], word_index]
        self.sensitive_words_list = []
        # [num1,num2,num3,……]
        self.per_word_list = []

    def possible_sensitive_words(self, word):
        # 单个违禁词的所有可能形式的映射值，如“fuck”：[[416, 430, 414, 421]]
        self.per_word_list = []
        word = list(word)
        for i in range(len(word)):
            # '法' ’轮‘ ’功‘
            # 汉字
            if (u'\u4e00' <= word[i] <= u'\u9fa5') or (u'\u3400' <= word[i] <= u'\u4db5'):
                word_list = []
                pinyin = pypinyin.lazy_pinyin(word[i])[0]
                # 全拼
                word_list.append([pinyin_alphabet_map[pinyin]])
                li = list(pinyin)
                for each_i in range(len(li)):
                    li[each_i] = pinyin_alphabet_map[li[each_i]]
                word_list.append(li)
                # 首字母
                word_list.append([pinyin_alphabet_map[pinyin[0]]])
                # 偏旁拆分
                if Chinese_split.is_breakable(word[i]):
                    parts = list(Chinese_split.get_split_part(word[i]))
                    Chinese_split_map[(parts[0], parts[1])] = word[i]
                word[i] = word_list
        for per in word:
            # 英文
            if not isinstance(per, list):
                if len(self.per_word_list) == 0:
                    li = list()
                    li.append(pinyin_alphabet_map[per])
                    self.per_word_list.append(li)
                else:
                    self.per_word_list[0].append(pinyin_alphabet_map[per])
            # 汉字
            else:
                if len(self.per_word_list) == 0:
                    for every_sate in per:
                        self.per_word_list.append(every_sate)
                else:
                    tmp = self.per_word_list
                    new_list = []
                    for every_sate in per:
                        list_copy = copy.deepcopy(tmp)
                        for k in list_copy:
                            for j in every_sate:
                                k.append(j)
                        new_list = new_list + list_copy
                    self.per_word_list = new_list

    def read_sensitive_words(self, filename):
        try:
            with open(filename, 'r+', encoding='utf-8') as words:
                lines = words.readlines()
                word_index = 0
                for line in lines:
                    line = line.replace('\n', '')
                    line = line.replace('\r', '')
                    line = line.lower()
                    original_sensitive_words.append(line)
                    self.possible_sensitive_words(line)
                    for each in self.per_word_list:
                        self.sensitive_words_list.append((each, word_index))
                    word_index += 1
                # print(self.sensitive_words_list)
                # return self.sensitive_words_list
        except OSError:
            print("Error: 没有找到文件或读取文件失败")
            sys.exit()
        else:
            return self.sensitive_words_list


class TrieNode(object):
    def __init__(self, value=None):
        # 值
        self.value = value
        # fail指针
        self.fail = None
        # 尾标志：标志为i表示第i个模式串串尾，默认为0
        self.tail = 0
        # 子节点，{value:TrieNode}
        self.children = {}


class Text:
    def __init__(self):
        # 根节点
        self.root = TrieNode()
        self.sensitive_words_list = []
        self.original_line = ""
        self.total = 0

        # 行数， 敏感词下标， 原始文本
        self.text_ans: [int, int, string] = []

        self.last_right = -1
        self.last_line = -1

        sensitive_word = Sensitive_words()
        self.sensitive_words_list = sensitive_word.read_sensitive_words(file_words)
        self.insert(self.sensitive_words_list)
        self.ac_automation()

    def insert(self, sequence):
        # print(sequence)
        for item_tuple in sequence:
            cur_node = self.root
            for i in range(len(item_tuple[0])):
                per = item_tuple[0][i]
                if per not in cur_node.children:
                    # 插入结点
                    child = TrieNode(value=per)
                    cur_node.children[per] = child
                    cur_node = child
                else:
                    cur_node = cur_node.children[per]
            cur_node.tail = item_tuple[1] + 1

    # 构建失败路径
    def ac_automation(self):
        queue = [self.root]
        # BFS遍历字典树
        while len(queue):
            temp_node = queue[0]
            # 取出队首元素
            queue.remove(temp_node)
            for value in temp_node.children.values():
                # 根的子结点fail指向根自己
                if temp_node == self.root:
                    value.fail = self.root
                else:
                    # 转到fail指针
                    p = temp_node.fail
                    while p:
                        # 若结点值在该结点的子结点中，则将fail指向该结点的对应子结点
                        if value.value in p.children:
                            value.fail = p.children[value.value]
                            break
                        # 转到fail指针继续回溯
                        p = p.fail
                    # 若为None，表示当前结点值在之前都没出现过，则其fail指向根结点
                    if not p:
                        value.fail = self.root
                # 将当前结点的所有子结点加到队列中
                queue.append(value)

    # 匹配到的违禁词在原文本中的左端点，右端点，对应违禁词的下标，查找到的行数
    def get_answer(self, left, right, index, line):
        # 判断是否与前一个违禁词嵌套出现，如果是，则此次检测到的违禁词不需要放入text_ans
        if line != self.last_line or line == self.last_line and left > self.last_right:
            self.text_ans.append((line, original_sensitive_words[index], self.original_line[left:right + 1]))
            self.total += 1
        # 更新
        self.last_right = right
        self.last_line = line

    def output(self, filename):
        try:
            with open(filename, 'w+', encoding='utf-8') as ans:
                print("Total: {}".format(self.total), file=ans)
                for each in self.text_ans:
                    print('Line{}: <{}> {}'.format(each[0], each[1], each[2]), file=ans)
        except IOError:
            print("Error: 没有找到文件或写入文件失败")

    def read_text(self, filename):
        try:
            with open(filename, 'r+', encoding='utf-8') as org:
                lines = org.readlines()
                line_index = 0
                for line in lines:
                    self.original_line = line
                    line = line.replace('\r', '')
                    line = line.replace('\n', '')
                    line = re.sub(u'([^\u3400-\u4db5\u4e00-\u9fa5a-zA-Z])', '#', line)
                    line = line.lower()
                    for i in range(len(line) - 1):
                        if (line[i], line[i+1]) in Chinese_split_map:
                            li = list(line)
                            li[i] = Chinese_split_map[(line[i], line[i+1])]
                            li[i+1] = '#'
                            line = ''.join(li)
                    self.search(line, line_index)
                    line_index += 1
        except OSError:
            print("Error: 没有找到文件或读取文件失败")

    def search(self, text, line_index):
        # print(text)
        """
        模式匹配
        :param line_index:
        :param self:
        :param text: 长文本
        :return:
        """
        p = self.root
        # 记录匹配起始位置下标
        start_index = 0
        for i in range(len(text)):
            single_char = text[i]
            if single_char == '#':
                i += 1
                continue
            pinyin_code = pinyin_alphabet_map[pypinyin.lazy_pinyin(single_char)[0]]
            while pinyin_code not in p.children and p is not self.root:
                p = p.fail
            # 有一点瑕疵，原因在于匹配子串的时候，若字符串中部分字符由两个匹配词组成，此时后一个词的前缀下标不会更新
            # 这是由于KMP算法本身导致的，目前与下文循环寻找所有匹配词存在冲突
            # 但是问题不大，因为其标记的位置均为匹配成功的字符
            if pinyin_code in p.children and p is self.root:
                start_index = i
            # 若找到匹配成功的字符结点，则指向那个结点，否则指向根结点
            if pinyin_code in p.children:
                p = p.children[pinyin_code]
            else:
                start_index = i
                p = self.root
            temp = p
            while temp is not self.root:
                # 尾标志为0不处理，但是tail需要-1从而与敏感词字典下标一致
                # 循环原因在于，有些词本身只是另一个词的后缀，也需要辨识出来
                if temp.tail:
                    # rst[self.words[temp.tail - 1]].append((start_index, i))
                    # print(line_index)
                    self.get_answer(start_index, i, temp.tail - 1, line_index + 1)
                temp = temp.fail


def main():
    new_text = Text()
    new_text.read_text(file_org)
    new_text.output(file_ans)


if __name__ == '__main__':
    main()
