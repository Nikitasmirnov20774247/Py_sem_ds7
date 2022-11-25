import controller as con

try:
    def btn_click(item):
        con.log.logger.debug("function call - btn_clic")
        con.log.logger.info(f"activate - Button: {item}")
        
        try:
            con.input_field['state'] = "normal"
            if item != '=':
                con.expression += item
            con.input_field.insert(con.END, item)

            if item == '=':
                lst = []
                coef = []
                num = []

                s = 0
                for i in range(len(con.expression)):
                    if con.expression[i] in ("+", "-", "*", "/"):
                        lst.append(con.expression[s:i])
                        lst.append(con.expression[i])
                        s = i + 1
                lst.append(con.expression[i:])
                con.log.logger.info(f"creat list - {lst}")

                for n in lst:
                    try:
                        num.append(float(n))
                    except:
                        coef.append(n)
            
                result = con.sol.solution(num, coef)
                con.expression = ""
                con.input_field.insert(con.END, result)
                con.log.logger.info(f"Calculator result: {result}")
            con.input_field['state'] = "readonly"
            
        except ZeroDivisionError:
            con.input_field.delete(0, con.END)
            con.input_field.insert(0, 'Ошибка (деление на 0)')
            con.log.logger.error("division by zero")
        except:
            con.input_field.delete(0, con.END)
            con.input_field.insert(0, 'Ошибка')
            con.log.logger.error("incorrect syntax")
except:
    con.log.logger.warning("Button recognition is not possible")

try:
    def btn_clear():
        con.log.logger.debug("function call - btn_clear")
        con.log.logger.info("activate: Button - C")
        con.expression = ""
        con.input_field['state'] = "normal"
        con.input_field.delete(0, con.END)
        con.input_field['state'] = "readonly"
        con.log.logger.info("clearing the field")
except:
    con.log.logger.warning("Button recognition is not possible")