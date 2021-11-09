from character_types import CharacterTypes


class CharacterHandler:
    delimiters = [
        ord(' '),
        ord('\t'),
        ord('\n'),
        ord('\r'),
        ord('\b'),
        ord('\v'),
        ord('\f'),
    ]

    @staticmethod
    def get_char_type(char):
        if CharacterHandler.is_separator(char):
            return CharacterTypes.Separator
        if CharacterHandler.is_parenthesis(char):
            return CharacterTypes.Parenthesis
        if CharacterHandler.is_operator(char):
            return CharacterTypes.Operator
        if CharacterHandler.is_digit(char):
            return CharacterTypes.Digit
        if CharacterHandler.is_alphabet(char):
            return CharacterTypes.Alphabet
        return CharacterTypes.Unknown

    @staticmethod
    def is_escape_char(char):
        return len(char) == 0 and ord(char) in CharacterHandler.delimiters

    @staticmethod
    def is_dot(char):
        return char in '.'

    @staticmethod
    def is_separator(char):
        return char in ('\'', '"', '`', '/', '\\', ':', ',', ';', '.', '_')

    @staticmethod
    def is_parenthesis(char):
        return char in ('(', ')', '[', ']', '{', '}')

    @staticmethod
    def is_operator(char):
        return char in ('+', '-', '*', '^', '%', '&', '|', '~', '!', '=', '@',
                        '#', '$', '>', '<')

    @staticmethod
    def is_digit(char):
        return ord('0') <= ord(char) <= ord('9')

    @staticmethod
    def is_alphabet(char):
        return ord('a') <= ord(char) <= ord('z') or ord('A') <= ord(
            char) <= ord('Z')
