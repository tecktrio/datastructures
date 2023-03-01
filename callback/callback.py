import time
def print1000(hello):
    for i in range(10):
        time.sleep(1)
        print(i)
    hello()

def hellofun():
    print('hello')

if __name__ == "__main__":
    print1000(hellofun)
