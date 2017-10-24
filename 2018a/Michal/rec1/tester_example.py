print ("hi")

def check_parity(n):
    if n % 2 == 0:
        return "even"
    else:
        return "odd"


def test():
    if check_parity(0) == "odd":
        print("error in function check_parity")
    if check_parity(1) == "even":
        print("error in function check_parity")
