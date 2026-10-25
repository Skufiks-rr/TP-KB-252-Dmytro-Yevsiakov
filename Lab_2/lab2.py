import csv
from sys import argv

list = []

def loadFromCSV(fileName):
    with open(fileName, "r", newline="", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)
        for row in reader:
            list.append({
                "name": row["name"],
                "phone": row["phone"],
                "email": row["email"],
                "group": row["group"]
            })
    list.sort(key=lambda item: item["name"])

def saveToCSV(fileName):
    with open(fileName, "w", newline="", encoding="utf-8") as file:
        fieldnames = ["name", "phone", "email", "group"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(list)

def printAllList():
    for elem in list:
        strForPrint = "Student name is " + elem["name"] + ", Phone is " + elem["phone"] + ", Email is " + elem["email"] + ", Group is " + elem["group"]
        print(strForPrint)
    return

def addNewElement():
    name = input("Please enter student name: ")
    phone = input("Please enter student phone: ")
    email = input("Please enter student email: ")
    group = input("Please enter student group: ")

    newItem = {
        "name": name,
        "phone": phone,
        "email": email,
        "group": group
    }

    insertPosition = 0
    for item in list:
        if name > item["name"]:
            insertPosition += 1
        else:
            break

    list.insert(insertPosition, newItem)
    print("New element has been added")
    return

def deleteElement():
    name = input("Please enter name to be deleted: ")
    deletePosition = -1

    for item in list:
        if name == item["name"]:
            deletePosition = list.index(item)
            break

    if deletePosition == -1:
        print("Element was not found")
    else:
        print("Delete position " + str(deletePosition))
        del list[deletePosition]
    return

def updateElement():
    name = input("Please enter name to be updated: ")
    updatePosition = -1

    for item in list:
        if name == item["name"]:
            updatePosition = list.index(item)
            break

    if updatePosition == -1:
        print("Element was not found")
    else:
        del list[updatePosition]

        newName = input("Please enter new student name: ")
        newPhone = input("Please enter new student phone: ")
        newEmail = input("Please enter new student email: ")
        newGroup = input("Please enter new student group: ")

        newItem = {
            "name": newName,
            "phone": newPhone,
            "email": newEmail,
            "group": newGroup
        }

        insertPosition = 0
        for item in list:
            if newName > item["name"]:
                insertPosition += 1
            else:
                break

        list.insert(insertPosition, newItem)
        print("Element has been updated")
    return

def main():
    if len(argv) < 2:
        print("Please specify CSV file name")
        return

    fileName = argv[1]

    try:
        loadFromCSV(fileName)
        print("Students loaded from CSV")
    except FileNotFoundError:
        print("CSV file not found")
        return

    while True:
        chouse = input("Please specify the action [ C create, U update, D delete, P print, X exit ] ")

        match chouse:
            case "C" | "c":
                print("New element will be created:")
                addNewElement()
                printAllList()
            case "U" | "u":
                print("Existing element will be updated")
                updateElement()
                printAllList()
            case "D" | "d":
                print("Element will be deleted")
                deleteElement()
            case "P" | "p":
                print("List will be printed")
                printAllList()
            case "X" | "x":
                saveToCSV(fileName)
                print("Students saved to CSV")
                print("Exit()")
                break
            case _:
                print("Wrong choice")

if __name__ == "__main__":
    main()
