def isPalindrome(self, s):
        result = ""
        for i in s:
            if i!= ":" and i!= "," and i!= " " and i!= "." and i!= ";" and i!= "" and i!= "/" and i!= "!" and i!= "@" and i!= "#" and i!= "_":
                result = result + i
        a = result.lower()
        if a[::-1] == a:
            return True
        else:
            return False
        