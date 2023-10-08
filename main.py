from project_classes import UserInput, SimplexMethod


def round_with_accuracy(value, accuracy, number_of_decimal_places_accuracy):
    if number_of_decimal_places_accuracy == 0:
        if str(value)[-2:] == ".5":
            if value > 0:
                return int(value + 0.5)
            elif value < 0:
                return int(value - 0.5)
        else:
            return int(round(value))
    elif abs(value) <= accuracy:
        return 0
    elif '.' in str(value):
        if number_of_decimal_places_accuracy < len(str(value).split('.')[1]):
            if str(value).split('.')[1][number_of_decimal_places_accuracy] == "5":
                if value > 0:
                    return round(value + 5 * 10 ** (-number_of_decimal_places_accuracy - 1),
                                 number_of_decimal_places_accuracy)
                elif value < 0:
                    return round(value - 5 * 10 ** (-number_of_decimal_places_accuracy - 1),
                                 number_of_decimal_places_accuracy)
    return round(value, number_of_decimal_places_accuracy)


user_input = UserInput()
user_input.collect_data()
method = SimplexMethod(user_input.size, user_input.C, user_input.A, user_input.b, user_input.a)
result = method.revised_simplex_method()
if result is None:
    print("The method is not applicable!")
else:
    if user_input.a != 1:
        num_of_decimal_places_accuracy = len(str(user_input.a).split('.')[1])
    else:
        num_of_decimal_places_accuracy = 0
    rounded_x = [round_with_accuracy(x, user_input.a, num_of_decimal_places_accuracy) for x in result[1:]]
    rounded_z = round_with_accuracy(result[0], user_input.a, num_of_decimal_places_accuracy)
    print("Optimal solution was found:")
    print("A vector of decision variables - x*: (" + ', '.join([f"{x:.{num_of_decimal_places_accuracy}f}" for x
                                                                in rounded_x]) + ")")
    if user_input.max_problem:
        print(f"Maximum value of the objective function z: {rounded_z:.{num_of_decimal_places_accuracy}f}")
    else:
        print(f"Maximum value of the objective function z: {(-1) * rounded_z:.{num_of_decimal_places_accuracy}f}")
