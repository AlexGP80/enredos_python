def arithmetic_arranger(problems, show_answers=False):

    first_line = ""
    second_line = ""
    third_line = ""
    fourth_line = ""
    arranged_problems = ""


    if len(problems) > 5:
        return 'Error: Too many problems.'

    for problem in problems:
        operator = "+"

        if first_line:
            first_line += "    "
            second_line += "    "
            third_line += "    "
            fourth_line += "    "

        if not ('+' in problem or '-' in problem):
            return "Error: Operator must be '+' or '-'."

        stripped_problem = problem.replace(" ", "")

        operands = stripped_problem.split('+')
        if len(operands) == 1:
            operands = stripped_problem.split('-')
            operator = "-"

        width = 0
        for operand in operands:
            if not operand.isdecimal():
                return 'Error: Numbers must only contain digits.'
            if len(operand) > width:
                width = len(operand)

        if width > 4:
            return 'Error: Numbers cannot be more than four digits.'

        dashes = "-" * (width+2)
        result = eval(problem)
        first_line += f"{operands[0]:>{width+2}}"
        second_line += f"{operator} {operands[1]:>{width}}"
        third_line += f"{dashes}"
        fourth_line += f"{result:>{width+2}}"


    arranged_problems += first_line + "\n"
    arranged_problems += second_line + "\n"
    arranged_problems += third_line
    if show_answers:
        arranged_problems += "\n" + fourth_line

    return arranged_problems
