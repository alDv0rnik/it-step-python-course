from decorators import mult

# if the function is recursive, you can use the helper like in task_2 again


@mult
def return_name(name, surname):
    print(f"im {name} {surname}")


return_name("artem", "mozalev")


@mult
def first(*a): return sum(a)


first(12, 3, 45, 4, 5, 8)
