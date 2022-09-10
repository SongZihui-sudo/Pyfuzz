class log():
    #   creat a log object
    def __init__(self, path=None, mode=None):
        # creat file
        if path != None:
            if mode == None:
                mode = "a"
            self.log = open(path, mode)
            self.stdio = False
        else:
            self.stdio = True


    # wearning log
    def wearn_log(self, msg):
        output = "WEARNING LOG>" + msg + "\n"
        if self.stdio:
            print(output)
        else:
            self.log.write(output)


    # debug log
    def debug_log(self, msg):
        output = "DEBUG LOG>" + msg + "\n"
        if self.stdio:
            print(output)
        else:
            self.log.write(output)


    # error log
    def error_log(self, msg):
        output = "ERROR LOG>" + msg + "\n"
        if self.stdio:
            print(output)
        else:
            self.log.write(output)

    # close
    def close(self):
        self.log.close() 
