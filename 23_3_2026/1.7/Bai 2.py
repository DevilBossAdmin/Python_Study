class SoSanhChuoi:
    def __init__(self, s1, s2, s3):
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3

    def so_sanh(self):
        print("=== Toán tử so sánh ===")
        print("s1 > s2:", self.s1 > self.s2)
        print("s1 < s2:", self.s1 < self.s2)
        print("s1 == s2:", self.s1 == self.s2)
        print("s1 != s2:", self.s1 != self.s2)

        print("s2 > s3:", self.s2 > self.s3)
        print("s2 < s3:", self.s2 < self.s3)
        print("s2 == s3:", self.s2 == self.s3)
        print("s2 != s3:", self.s2 != self.s3)

    def logic(self):
        print("\n=== Toán tử logic ===")
        print("(s1 < s2) and (s2 < s3):", (self.s1 < self.s2) and (self.s2 < self.s3))
        print("(s1 > s2) or (s2 < s3):", (self.s1 > self.s2) or (self.s2 < self.s3))
        print("not(s1 == s2):", not(self.s1 == self.s2))


# Giá trị ban đầu
s1 = 'a'
s2 = 'b'
s3 = 'c'

# Tạo đối tượng
ss = SoSanhChuoi(s1, s2, s3)

# Gọi hàm
ss.so_sanh()
ss.logic()