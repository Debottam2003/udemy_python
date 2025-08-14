def main():
    print("Hello from backend!")
def swap(a, b):
    return b, a

if __name__ == "__main__":
    main()
    x, y = 10, 5
    print(x, y)
    x, y = swap(10, 5)
    print
    print(x, y)
