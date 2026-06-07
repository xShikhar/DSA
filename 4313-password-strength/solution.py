class Solution:
    def passwordStrength(self, password: str) -> int:
        seen = set()
        points = 0

        for ch in password:
            if ch in seen:
                continue
            seen.add(ch)
            o = ord(ch)
            if 97 <= o <= 122:       
                points += 1
            elif 65 <= o <= 90:      
                points += 2
            elif 48 <= o <= 57:     
                points += 3
            elif o in (33, 64, 35, 36): 
                points += 5

        return points 
