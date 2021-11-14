def lifeStage(age):
    # 0 to 12
    if age >= 0 and age <= 12:
        print("Life stage: Kid")
    else:
        # 13 to 17
        if age >= 13 and age <= 17:
            print("Life stage: Teen")
        else:
            # equal 18
            if age == 18:
                print("Life stage: Debut")
            else:
                # greater than 18
                print("Life stage: Adult")

age = int(input("Insert age: "))

lifeStage(age)