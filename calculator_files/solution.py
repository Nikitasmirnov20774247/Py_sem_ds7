import controller as con

def solution(num, coef):
    con.log.logger.debug("function call - solution")
    for i in range(len(num)):
        for j in range(len(coef)):
            if coef[j] == '*' or coef[j] == '/':
                if coef[j] == '*':
                    num[j] *= num[j + 1]
                    del num[j + 1]
                    del coef[j]
                    con.log.logger.info(f"complete: multiplication (*) - result = {num[j]}")
                    break
                if coef[j] == '/':
                    num[j] /= num[j + 1]
                    del num[j + 1]
                    del coef[j]
                    con.log.logger.info(f"complete: division (/) - result = {num[j]}")
                    break

        for j in range(len(coef)):
            if coef[j] == '+' or coef[j] == '-':
                if coef[j] == '+':
                    num[j] += num[j + 1]
                    del num[j + 1]
                    del coef[j]
                    con.log.logger.info(f"complete: sum (+) - result = {num[j]}")
                    break
                elif coef[j] == '-':
                    num[j] -= num[j + 1]
                    del num[j + 1]
                    del coef[j]
                    con.log.logger.info(f"complete: subtraction (-) - result = {num[j]}")
                    break
    return num