def NULL_not_found(object: any) -> int:
    if object is None:
        print(f"Nothing: {object} {type(object)}")
        return 0
    elif type(object) is float and object != object:
        print(f"Cheese: {object} {type(object)}")
        return 0
    elif object == 0 and type(object) is int:
        print(f"Zero: {object} {type(object)}")
        return 0
    elif object == '' and type(object) is str:
        print(f"Empty: {object} {type(object)}")
        return 0
    elif object is False:
        print(f"Fake: {object} {type(object)}")
        return 0
    else:
        print("Type not found")
        return 1

