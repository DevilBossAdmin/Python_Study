class PhepToan:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def cong(self):
        print("Cộng:", self.a + self.b + self.c)

    def tru(self):
        print("Trừ:", self.a - self.b - self.c)

    def nhan(self):
        print("Nhân:", self.a * self.b * self.c)

    def chia(self):
        print("Chia:", self.a / self.b / self.c)

    def luy_thua(self):
        print("Lũy thừa:")
        print("a^b =", self.a ** self.b)
        print("b^c =", self.b ** self.c)
        print("a^c =", self.a ** self.c)


# Khởi tạo giá trị
a = 16
b = 3
c = 5

# Tạo đối tượng
pt = PhepToan(a, b, c)

# Gọi các phương thức
pt.cong()
pt.tru()
pt.nhan()
pt.chia()
pt.luy_thua()