def check_for_spaces(answer, hint):

    if "-" in answer or " " in answer:
        for i in range(len(answer)):

            if answer[i] == "-":
                hint[i] = "-"
            elif answer[i] == " ":
                hint[i] = " "
            else:
                hint[i] = "_"