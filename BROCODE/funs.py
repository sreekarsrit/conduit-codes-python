def Birthday(name,age):
    print(f"happy birthday {name}")
    return age
    #print()
#print(Birthday("sreekar",20))
#print(Birthday("shubhakar",15))
if __name__ == '__main__':
    for t in range(int(input("enter how many members: "))):
        name,age=input(f"Enter name and age for person {t+1}:").split()
        age=int(age)
        print(Birthday(name,age))
