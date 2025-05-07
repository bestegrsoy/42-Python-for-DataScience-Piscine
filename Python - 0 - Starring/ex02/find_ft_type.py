def all_thing_is_obj(object: any) -> int:
    type_names = {
        list: "List",
        set: "Set",
        tuple: "Tuple",
        dict: "Dict",
        str: "String"
    }

    obj_types = type(object)
    type_name = type_names.get(obj_types, "Type not found")

    if obj_types == str:
        print(f"{object} is in the kitchen : {obj_types}")
    elif type_name != "Type not found":
        print(f"{type_name} : {obj_types}")
    else:
        print(f"{type_name}")

    return 42