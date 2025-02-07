def check_for_spaces(answer, hint):

    if "-" in answer:
        for i in range(len(answer)):

            if answer[i] == "-":
                hint[i] = "-"
            else:
                hint[i] = "_"
    else:
        print("_" * len(answer))

    if " " in answer:
        for i in range(len(answer)):

            if answer[i] == " ":
                hint[i] = " "
            else:
                hint[i] = "_"
    else:
        print("_" * len(answer))
