from project_classes import UserInput, SimplexMethod


def round_with_accuracy(value, accuracy):
    if abs(round(value) - value) <= accuracy:
        if str(value)[-2:] == ".5":
            if value > 0:
                return int(value + 0.5)
            elif value < 0:
                return int(value - 0.5)
        else:
            return round(value)
    elif abs(value) <= accuracy:
        return 0
    else:
        return value


user_input = UserInput()
user_input.collect_data()
method = SimplexMethod(user_input.size, user_input.C, user_input.A, user_input.b, user_input.a)
result = method.revised_simplex_method()
if result is None:
    print("The method is not applicable!")
else:
    rounded_x = [round_with_accuracy(x, user_input.a) for x in result[1:]]
    rounded_z = round_with_accuracy(result[0], user_input.a)
    print("Optimal solution was found:")
    print("A vector of decision variables - x*: (" + ', '.join([str(x) for x in rounded_x]) + ")")
    if user_input.max_problem:
        print("Maximum value of the objective function z:", rounded_z)
    else:
        print("Minimum value of the objective function z:", (-1) * rounded_z)
