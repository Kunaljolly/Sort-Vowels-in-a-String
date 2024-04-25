class Solution:
    def sortVowels(self, s: str) -> str:
        T = {"A":ord("A"),"E":ord("E"),"I":ord("I"),"O":ord("O"),"U":ord("U"),"a":ord("a"),"e":ord("e"),"i":ord("i"),"o":ord("o"),"u":ord("u")}
        t = []
        i = []
        s = list(s)
        for x in range(len(s)):
            if s[x] in T:
                t.append(s[x])
                i.append(x)
        t = sorted(t)
        for x in range(len(i)):
            s[i[x]] = t[x]
        return "".join(s)

            
            
