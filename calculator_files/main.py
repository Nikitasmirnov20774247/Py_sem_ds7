import controller as con
con.log.logger.info("START main.py")

try:
    if __name__ == '__main__':
        con.calculator()
        con.log.logger.info("END main.py")
except:
    con.log.logger.critical("execution is not possible")
    con.log.logger.exception("problems")