import numpy as np

while True:
    print("\n===== MATRIX OPERATIONS TOOL =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Transpose")
    print("5. Determinant")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice in ["1", "2", "3"]:

        rows = int(input("Enter number of rows: "))
        cols = int(input("Enter number of columns: "))

        print("\nEnter Matrix A:")
        A = []
        for i in range(rows):
            row = list(map(float, input().split()))
            A.append(row)

        print("\nEnter Matrix B:")
        B = []
        for i in range(rows):
            row = list(map(float, input().split()))
            B.append(row)

        A = np.array(A)
        B = np.array(B)

        if choice == "1":
            print("\nResult:")
            print(A + B)

        elif choice == "2":
            print("\nResult:")
            print(A - B)

        elif choice == "3":
            print("\nResult:")
            print(np.dot(A, B))

    elif choice == "4":

        rows = int(input("Enter number of rows: "))
        cols = int(input("Enter number of columns: "))

        print("\nEnter Matrix:")
        A = []

        for i in range(rows):
            row = list(map(float, input().split()))
            A.append(row)

        A = np.array(A)

        print("\nTranspose:")
        print(A.T)

    elif choice == "5":

        n = int(input("Enter size of square matrix: "))

        print("\nEnter Matrix:")
        A = []

        for i in range(n):
            row = list(map(float, input().split()))
            A.append(row)

        A = np.array(A)

        print("\nDeterminant:")
        print(np.linalg.det(A))

    elif choice == "6":
        print("Exiting...")
        break

    else:
        print("Invalid choice!")