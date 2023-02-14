class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = ""
        carry = False
        if len(a) > len(b):
            b = ('0'*(len(a)-len(b)))+b
        else:
            a = ('0'*(len(b)-len(a)))+a

        print(a, b)

        for i in range(0, len(a)):
            j = len(a)-1-i
            print(a[j], b[j])
            if a[j] == '0' and b[j] == '0':
                if carry:
                    result = '1'+result
                    carry = False
                else:
                    result = '0'+result
            elif a[j] == '1' and b[j] == '0' or a[j] == '0' and b[j] == '1':
                if carry:
                    result = '0'+result
                else:
                    result = '1'+result

            elif a[j] == '1' and b[j] == '1':
                if carry:
                    result = '1'+result
                else:
                    result = '0'+result

                carry = True
            print(result)
        if carry:
            result = '1'+result
        return result
