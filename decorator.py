from abc import ABC, abstractmethod


class TextProcessor(ABC):
    @abstractmethod
    def process(self, text):
        pass


class BasicTextProcessor(TextProcessor):
    def process(self, text):
        return text

class TextDecorator(TextProcessor):
    def __init__(self, processor):
        self.processor = processor

    def process(self, text):
        return self.processor.process(text)


class UpperCaseDecorator(TextDecorator):
    def process(self, text):
        original_text = super().process(text)
        return original_text.upper()


class PrefixCaseDecorator(TextDecorator):
    def __init__(self, processor, prefix):
        super().__init__(processor)
        self.prefix = prefix

    def process(self, text):
        original_text = super().process(text)
        return self.prefix + original_text


processor = BasicTextProcessor()

uppercase_processor = UpperCaseDecorator(processor)
prefix_processor = PrefixCaseDecorator(uppercase_processor, "~")
processed_text = prefix_processor.process("Hello world")
print(processed_text)