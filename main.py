from project_classes import UserInput, SimplexMethod

user_input = UserInput()
user_input.collect_data()
method = SimplexMethod(user_input.size, user_input.C, user_input.A, user_input.b, user_input.a)
result = method.revised_simplex_method()
if result is None:
    print("The method is not applicable!")
else:
    print("Optimal solution was found:")
    print("A vector of decision variables - x*:", f"({', '.join([f'{x:.{user_input.a}f}' for x in result[1:]])})")
    print("Maximum value of the objective function z:", f"{result[0]:.{user_input.a}f}")
