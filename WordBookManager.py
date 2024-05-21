class WordBookManager:
    def __init__(self, wordbook):
        """
        初始化 WordBookManager 实例。
        
        参数:
        wordbook (WordBook): 要管理的 WordBook 实例
        """
        self.wordbook = wordbook

    def search(self, word):
        """
        在词书中搜索单词并返回对应的 WordEntry 实例。
        
        参数:
        word (str): 要搜索的单词
        
        返回:
        WordEntry: 找到的 WordEntry 实例，如果未找到则返回 None
        """
        for entry in self.wordbook.word_entries:
            if entry.word == word:
                return entry
        return None

    def word_view(self, word_entry):
        """
        打印 WordEntry 实例的详细信息。
        
        参数:
        word_entry (WordEntry): 要显示的 WordEntry 实例
        """
        if word_entry:
            print(f"Word: {word_entry.word}")
            print(f"Meaning: {word_entry.meaning}")
            print(f"Sentence: {word_entry.sentence}")
            print(f"Memory: {word_entry.memory}")
        else:
            print("WordEntry is None")