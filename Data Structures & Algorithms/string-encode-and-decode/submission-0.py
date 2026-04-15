class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for x in strs:
            result += (str(len(x))+"#"+x)
        print(result)
        return result

    def decode(self, s: str) -> List[str]:
        curr_str_len = ""
        s_array = list(s)
        s_array.reverse()
        result = []
        while len(s_array) != 0:
            curr_char = s_array.pop()
            curr_word = ""
            if curr_char == '#':
                for i in range(int(curr_str_len)):
                    if len(s_array) == 0:
                        break
                    curr_word += s_array.pop()
                result.append(curr_word)
                curr_str_len = ""
            else:
                if str.isdigit(str(curr_char)):
                    curr_str_len += curr_char
        return result

