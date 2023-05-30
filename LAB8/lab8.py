from abc import ABC, abstractmethod

class WordCounter(ABC):
    address = "weirdwords.txt"

    def __init__(self, address):
        self.address = address

    @abstractmethod
    def calculateFreqs(self):
        pass


class ListCount(WordCounter):
    def calculateFreqs(self):
        frequencies = [0] * 26

        with open(self.address, 'r') as file:
            for line in file:
                for char in line.lower():
                    if char.isalpha():
                        index = ord(char) - ord('a')
                        frequencies[index] += 1

        for i in range(len(frequencies)):
            letter = chr(i + ord('a'))
            print(f"{letter} = {frequencies[i]}")


class DictCount(WordCounter):
    def calculateFreqs(self):
        frequencies = {}

        with open(self.address, 'r') as file:
            for line in file:
                for char in line.lower():
                    if char.isalpha():
                        frequencies[char] = frequencies.get(char, 0) + 1

        for letter, frequency in frequencies.items():
            print(f"{letter} = {frequency}")


list_counter = ListCount("weirdWords.txt")
list_counter.calculateFreqs()

dict_counter = DictCount("weirdWords.txt")
dict_counter.calculateFreqs()
