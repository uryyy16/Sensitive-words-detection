import pypinyin
import copy

import init_map
import Chinese_spilt

Chinese_split_map = {}
map_value, pinyin_alphabet_map = init_map.pinyin_alphabet_map()

# print(map_value)
# print(pinyin_alphabet_map)

file_words = './words.txt'


class Sensitive_words:
    def __init__(self):
        # [[num1,num2,num3,……], word_index]
        self.sensitive_words_list = []

    def possible_sensitive_words(self, word):
        global map_value
        per_word_list = []
        word = list(word)
        for i in range(len(word)):
            # print(word[i])
            # '法' ’轮‘ ’功‘
            # per = word[i]
            # 汉字
            if (u'\u4e00' <= word[i] <= u'\u9fa5') or (u'\u3400' <= word[i] <= u'\u4db5'):
                word_list = []
                pinyin = pypinyin.lazy_pinyin(word[i])[0]
                # 全拼
                word_list.append([pinyin])
                word_list.append(list(pinyin))
                # 首字母
                word_list.append([pinyin[0]])
                # 偏旁拆分
                if Chinese_spilt.is_breakable(word[i]):
                    parts = list(Chinese_spilt.get_split_part(word[i]))
                    word_list.append(parts)
                    for part in parts:
                        if part not in Chinese_split_map:
                            Chinese_split_map[part] = map_value
                            map_value += 1
                word[i] = word_list
            else:
                pass
        for per in word:
            # print(per)
            # 英文
            if not isinstance(per, list):
                if len(per_word_list) == 0:
                    per_word_list.append(list(per))
                else:
                    per_word_list[0].append(per)
            # 汉字
            else:
                if len(per_word_list) == 0:
                    for every_sate in per:
                        per_word_list.append(every_sate)
                else:
                    tmp = per_word_list
                    new_list = []
                    for every_sate in per:
                        list_copy = copy.deepcopy(tmp)
                        for k in list_copy:
                            for j in every_sate:
                                k.append(j)
                        new_list = new_list + list_copy
                    per_word_list = new_list
        # return per_word_list
        for i in range(len(per_word_list)):
            li = per_word_list[i]
            for j in range(len(li)):
                if li[j] in pinyin_alphabet_map:
                    per_word_list[i][j] = pinyin_alphabet_map[li[j]]
                elif li[j] in Chinese_split_map:
                    per_word_list[i][j] = Chinese_split_map[li[j]]
        return per_word_list

    def read_sensitive_words(self, filename):
        try:
            with open(filename, 'r+', encoding='utf-8') as words:
                lines = words.readlines()
                word_index = 0
                for line in lines:
                    line = line.replace('\n', '')
                    line = line.replace('\r', '')
                    line = line.lower()
                    # print(line, word_index)
                    self.sensitive_words_list.append((self.possible_sensitive_words(line), word_index))
                    word_index += 1
        except IOError:
            print("Error: 没有找到文件或读取文件失败")


def main():
    f = Sensitive_words()
    f.read_sensitive_words(file_words)


if __name__ == '__main__':
    main()
