ALPHABET_LIST = [
    'b', 'c', 'd', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]
PINYIN_LIST = [
    'a', 'o', 'e', 'ba', 'bo', 'bi', 'bu', 'pa', 'po', 'pi', 'pu',
    'ma', 'mo', 'me', 'mi', 'mu', 'fa', 'fo', 'fu', 'da', 'de',
    'di', 'du', 'ta', 'te', 'ti', 'tu', 'na', 'ne', 'ni', 'nu',
    'nv', 'la', 'lo', 'le', 'li', 'lu', 'lv', 'ga', 'ge', 'gu',
    'ka', 'ke', 'ku', 'ha', 'he', 'hu', 'ji', 'ju', 'qi', 'qu',
    'xi', 'xu', 'zha', 'zhe', 'zhi', 'zhu', 'cha', 'che', 'chi',
    'chu', 'sha', 'she', 'shi', 'shu', 'ra', 're', 'ri', 'ru',
    'za', 'ze', 'zi', 'zu', 'ca', 'ce', 'ci', 'cu', 'sa', 'se',
    'si', 'su', 'ya', 'yo', 'ye', 'yi', 'yu', 'wa', 'wo', 'wu',
    'ai', 'ei', 'ao', 'ou', 'er', 'bai', 'bei', 'bao', 'bie',
    'pai', 'pei', 'pao', 'pou', 'pie', 'mai', 'mei', 'mao', 'mou',
    'miu', 'mie', 'fei', 'fou', 'dai', 'dei', 'dui', 'dao', 'dou',
    'diu', 'die', 'tai', 'tei', 'tui', 'tao', 'tou', 'tie', 'nai',
    'nei', 'nao', 'nou', 'niu', 'nie', 'lai', 'lei', 'lao', 'lou',
    'liu', 'lie', 'gai', 'gei', 'gui', 'gao', 'gou', 'kai', 'kei',
    'kui', 'kao', 'kou', 'hai', 'hei', 'hui', 'hao', 'hou', 'jiu',
    'jie', 'jue', 'qiu', 'qie', 'que', 'xiu', 'xie', 'xue', 'zhai',
    'zhei', 'zhui', 'zhao', 'zhou', 'chai', 'chui', 'chao', 'chou',
    'shai', 'shei', 'shui', 'shao', 'shou', 'rui', 'rao', 'rou',
    'zai', 'zei', 'zui', 'zao', 'zou', 'cai', 'cei', 'cui', 'cao',
    'cou', 'sai', 'sui', 'sao', 'sou', 'yao', 'you', 'yue', 'wai',
    'wei', 'an', 'en', 'ang', 'eng', 'ban', 'ben', 'bin', 'bang',
    'beng', 'bing', 'pan', 'pen', 'pin', 'pang', 'peng', 'ping',
    'man', 'men', 'min', 'mang', 'meng', 'ming', 'fan', 'fen',
    'fang', 'feng', 'dan', 'den', 'dun', 'dang', 'deng', 'ding',
    'dong', 'tan', 'tun', 'tang', 'teng', 'ting', 'tong', 'nan',
    'nen', 'nin', 'nun', 'nang', 'neng', 'ning', 'nong', 'lan',
    'lin', 'lun', 'lang', 'leng', 'ling', 'long', 'gan', 'gen',
    'gun', 'gang', 'geng', 'gong', 'kan', 'ken', 'kun', 'kang',
    'keng', 'kong', 'han', 'hen', 'hun', 'hang', 'heng', 'hong',
    'jin', 'jun', 'jing', 'qin', 'qun', 'qing', 'xin', 'xun',
    'xing', 'zhan', 'zhen', 'zhun', 'zhang', 'zheng', 'zhong',
    'chan', 'chen', 'chun', 'chang', 'cheng', 'chong', 'shan',
    'shen', 'shun', 'shang', 'sheng', 'ran', 'ren', 'run', 'rang',
    'reng', 'rong', 'zan', 'zen', 'zun', 'zang', 'zeng', 'zong',
    'can', 'cen', 'cun', 'cang', 'ceng', 'cong', 'san', 'sen',
    'sun', 'sang', 'seng', 'song', 'yan', 'yin', 'yun', 'yang',
    'ying', 'yong', 'wan', 'wen', 'wang', 'weng', 'biao', 'bian',
    'piao', 'pian', 'miao', 'mian', 'dia', 'diao', 'dian', 'duo', 'duan',
    'tiao', 'tian', 'tuo', 'tuan', 'niao', 'nian', 'niang', 'nuo',
    'nuan', 'lia', 'liao', 'lian', 'liang', 'luo', 'luan', 'gua',
    'guo', 'guai', 'guan', 'guang', 'kua', 'kuo', 'kuai', 'kuan',
    'kuang', 'hua', 'huo', 'huai', 'huan', 'huang', 'jia', 'jiao',
    'jian', 'jiang', 'jiong', 'juan', 'qia', 'qiao', 'qian',
    'qiang', 'qiong', 'quan', 'xia', 'xiao', 'xian', 'xiang',
    'xiong', 'xuan', 'zhua', 'zhuo', 'zhuai', 'zhuan', 'zhuang',
    'chua', 'chuo', 'chuai', 'chuan', 'chuang', 'shua', 'shuo',
    'shuai', 'shuan', 'shuang', 'rua', 'ruo', 'ruan', 'zuo',
    'zuan', 'cuo', 'cuan', 'suo', 'suan', 'yuan'
]
Pinyin_alphabet_map = {}


def pinyin_alphabet_map():
    map_value = 1
    for i in PINYIN_LIST:
        Pinyin_alphabet_map[i] = map_value
        map_value += 1
    for j in ALPHABET_LIST:
        Pinyin_alphabet_map[j] = map_value
        map_value += 1
    return map_value, Pinyin_alphabet_map


def test():
    pinyin_alphabet_map()
    for i in PINYIN_LIST:
        print(Pinyin_alphabet_map[i])
    for j in ALPHABET_LIST:
        print(Pinyin_alphabet_map[j])


if __name__ == '__main__':
    test()
