# FM_Word
```
```markdown
# WordBook Management

This project is used for managing wordbooks, including loading from JSON files, saving, searching, and viewing word entries.

## File Structure
```

```
project_root/
│
├── data/
│   └── io.py
│
├── methods/
│   └── WordBookManager.py
│
└── README.md
```



```
## Installation

Make sure your project directory structure matches the above file structure.

## User Guide

### 1. Initialize WordBook

First, load the JSON file and create a `WordBook` instance:

```python
from data.io import WordBook

file_name = "EnWords"
wordbook = WordBook(file_name)
print(wordbook)
```

### 2. Use WordBookManager

Create a `WordBookManager` instance to manage the `WordBook` instance:

```python
from methods.WordBookManager import WordBookManager

manager = WordBookManager(wordbook)
```

### 3. Search for a Word

Use the `search` method to look up a word and return the corresponding `WordEntry` instance:

```python
searched_entry = manager.search("a")
print(searched_entry)
```

### 4. View Word Entry

Use the `word_view` method to print detailed information about a word entry:

```python
manager.word_view(searched_entry)
```

### 5. Save Changes

After modifying word entries in the wordbook, use the `save` method to save the changes:

```python
wordbook.word_entries[0].memory += 1
wordbook.save()
```

## WordBook Class

The `WordBook` class includes the following methods and attributes:

- `__init__(file_name)`: Initialize the `WordBook` instance and load information from JSON data.
- `__repr__()`: Return the string representation of the `WordBook` instance.
- `to_dict()`: Convert the `WordBook` instance to a dictionary.
- `save()`: Convert the `WordBook` instance to JSON data and save it to the original path.

## WordBookManager Class

The `WordBookManager` class is used to manage `WordBook` instances and includes the following methods:

- `__init__(wordbook)`: Initialize the `WordBookManager` instance.
- `search(word)`: Search for a word in the wordbook and return the corresponding `WordEntry` instance.
- `word_view(word_entry)`: Print detailed information about a `WordEntry` instance.

