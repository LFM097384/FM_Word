import json
import os

json_folder_path = r"D:\项目\风鸣背单词\resources\Wordbooks"

def read_json(file_path):
    """
    读取指定路径的 JSON 文件并返回其内容作为字典。
    
    参数:
    file_path (str): JSON 文件的路径
    
    返回:
    dict: 解析后的 JSON 数据
    """
    with open(file_path, mode='r', encoding='utf-8') as jsonfile:
        data = json.load(jsonfile)
    return data

class WordBook:
    class WordEntry:
        def __init__(self, word, meaning, sentence, memory):
            """
            初始化 WordEntry 实例。
            
            参数:
            word (str): 单词
            meaning (str): 单词的含义
            sentence (str): 示例句子
            memory (int): 记忆值
            """
            self.word = word
            self.meaning = meaning
            self.sentence = sentence
            self.memory = memory

        def __repr__(self):
            """
            返回 WordEntry 实例的字符串表示。
            """
            return f"WordEntry(word={self.word}, meaning={self.meaning}, sentence={self.sentence}, memory={self.memory})"

        def to_dict(self):
            """
            将 WordEntry 实例转换为字典。
            
            返回:
            dict: WordEntry 实例的字典表示
            """
            return {
                'word': self.word,
                'meaning': self.meaning,
                'sentence': self.sentence,
                'memory': self.memory
            }

    def __init__(self, file_name):
        """
        初始化 WordBook 实例，并从 JSON 数据中加载信息。
        
        参数:
        file_name (str): 本地词典的名称
        """
        # 构建文件路径
        self.file_path = os.path.join(json_folder_path, file_name + ".json")
        # 读取 JSON 数据
        json_data = read_json(self.file_path)
        
        # 提取词书的基本信息
        info = json_data['info']
        self.name = info['Name']
        self.source_language = info['SourceLanguage']
        self.target_language = info['TargetLanguage']
        
        # 从 JSON 数据中提取单词条目
        self.word_entries = []
        for key, value in json_data['dict'].items():
            word_entry = self.WordEntry(
                word=value['word'],
                meaning=value['meaning'],
                sentence=value.get('sentence'),
                memory=value['memory']
            )
            self.word_entries.append(word_entry)

    def __repr__(self):
        """
        返回 WordBook 实例的字符串表示。
        """
        return f"WordBook(name={self.name}, source_language={self.source_language}, target_language={self.target_language}, word_entries={self.word_entries})"

    def to_dict(self):
        """
        将 WordBook 实例转换为字典。
        
        返回:
        dict: WordBook 实例的字典表示
        """
        return {
            'info': {
                'Name': self.name,
                'SourceLanguage': self.source_language,
                'TargetLanguage': self.target_language
            },
            'dict': {
                entry.word: entry.to_dict() for entry in self.word_entries
            }
        }

    def save(self):
        """
        将 WordBook 实例转换为 JSON 数据并保存到原路径。
        """
        data = self.to_dict()
        with open(self.file_path, 'w', encoding='utf-8') as jsonfile:
            json.dump(data, jsonfile, ensure_ascii=False, indent=4)

# 示例用法
#file_name = "EnWords"
#wordbook = WordBook(file_name)
#wordbook.save()
#print(wordbook)

# WordBook 实例的数据结构
# WordBook 实例是一个包含以下属性的数据结构:
# - name (str): 词书名称, 例如 "Newwordbook"
# - source_language (str): 源语言, 例如 "English"
# - target_language (str): 目标语言, 例如 "Chinese"
# - word_entries (list): 一个包含多个 WordEntry 实例的列表，每个实例表示一个单词条目。
#
# WordEntry 实例是一个包含以下属性的数据结构:
# - word (str): 单词, 例如 "a"
# - meaning (str): 单词的含义, 例如 "n.(A)As 或 A's 安(ampere);(a) art.一;n.字母A /[军] Analog.Digital,模拟/数字 /(=account of) 帐上"
# - sentence (str 或 None): 示例句子, 可以为空 (例如 None)
# - memory (int): 记忆值, 例如 0
#

