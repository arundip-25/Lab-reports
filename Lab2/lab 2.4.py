data = []

while True:
    print("\nChoose an operation:")
    print("1. Push (Stack)")
    print("2. Pop (Stack)")
    print("3. Enqueue (Queue)")
    print("4. Dequeue (Queue)")
    print("5. Display")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        val = input("Enter value to push: ")
        data.append(val)
    elif choice == '2':
        if data:
            print("Popped:", data.pop())
        else:
            print("Stack is empty")
    elif choice == '3':
        val = input("Enter value to enqueue: ")
        data.append(val)
    elif choice == '4':
        if data:
            print("Dequeued:", data.pop(0))
        else:
            print("Queue is empty")
    elif choice == '5':
        print("Current list:", data)
    elif choice == '6':
        break
    else:
        print("Invalid choice")

