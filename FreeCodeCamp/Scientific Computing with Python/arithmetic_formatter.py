def arithmetic_arranger(list_of_problems, show_answers=False):

    operator = "+"
    first_line = ""
    second_line = ""
    third_line = ""
    fourth_line = ""


    if len(list_of_problems) > 5:
        raise Exception('Error: Too many problems.')

    for problem in list_of_problems:
        if not ('+' in problem or '-' in problem):
            raise Exception("Error: Operator must be '+' or '-'.")

        stripped_problem = problem.replace(" ", "")

        operands = stripped_problem.split('+')
        if len(operands) == 1:
            operands = stripped_problem.split('-')
            operator = "-"

        width = 0
        int_operands = []
        for operand in operands:
            if not operand.isdecimal():
                raise Exception('Error: Numbers must only contain digits.')
            if len(operand) > width:
                width = len(operand)

        if width > 4:
            raise Exception('Error: Numbers cannot be more than four digits.')

        dashes = "-" * (width+2)
        result = eval(problem)
        first_line += f"{operands[0]:>{width+2}}    "
        second_line += f"{operator} {operands[1]:>{width}}    "
        third_line += f"{dashes}    "
        fourth_line += f"{result:>{width+2}}    "

    print(first_line)
    print(second_line)
    print(third_line)
    if show_answers:
        print(fourth_line)


try:
    arithmetic_arranger(["32 + 3465", "3801 - 2", "45 + 43", "123 - 49", "1 + 1"], True)
except Exception as err:
    print(err)
