from project_classes import UserInput, SimplexMethod

x = UserInput()

x.input_size()
x.input_C()
x.input_A()
x.input_b()
x.input_a()

method = SimplexMethod(x.size, x.C, x.A, x.b, x.a)
method.find_basic_variables()
