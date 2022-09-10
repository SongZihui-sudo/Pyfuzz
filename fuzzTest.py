import json
import random
import os
import subprocess
import log


#   get the config data
def json_read(path):
    f = open(path, 'r', encoding='utf-8')
    config = json.load(f) 
    return config


# fuzz class
class fuzz():
    def __init__(self, config):
        self.config = config


    #   templete parse
    def templete_parse(self, input_args:str):
        temp = []
        temp = input_args.split()
        parsed = []
        for arg in temp:
            if arg[0] == '/':
                arg = arg.split('/')
                arg = arg[1:]
                parsed.append(arg)
            else:
                parsed.append(arg)
                continue
        return parsed


    #   test
    def fuzz_test(self):
        j = 0
        for conf in config:
            # creat log file
            if not os.path.exists("./log/" + str(j)):
                os.mkdir("./log/" + str(j))
            target_name = os.path.split(conf["target"])
            loged = log.log(path = "./log/" + str(j) + "/" + target_name[-1] + ".log", mode="a")
            j = j + 1
            try:            
                # fuzz test
                for i in range(conf["test_number"]):
                    input_args = self.templete_parse(conf["config"]["templete"])
                    input = self.make_test_example(input_args, conf["config"]["args"])
                    # open program entry and input test example
                    self.input_test_example(conf["config"]["entry"], conf["target"] , input, loged)
                loged.close()
            except Exception as e:
                print(e)
                print(e.__traceback__.tb_frame.f_globals["__file__"])
                print(e.__traceback__.tb_lineno)


    #  make test example
    def make_test_example(self, input_args, config_args):
        try: 
            input = ""
            for args in input_args:
                if type(args) == list:
                    islist = len(args)
                else:
                    islist = 1
                if args[-1] == '*':
                    range_num = random.randint(0, 10)
                elif args[-1][-2:]:
                    range_arg = int(args[-1][-2:])
                for i in range(islist):
                    if args[i] == "%d":
                        for data in range(range_num):
                            input+=" " + str(random.randint(0, 1000000))   
                    elif args[i] == "args":
                        for data in range(range_num + range_arg):
                            bit = random.randint(0, len(config_args) - 1)
                            input+=" " + config_args[bit]
                    else:
                        continue
        except Exception as e:
                print(e)
                print(e.__traceback__.tb_frame.f_globals["__file__"])
                print(e.__traceback__.tb_lineno)

        return input[1:]

    
    #   input test example
    def input_test_example(self, entry_type, target, input, log_obj):
        try:
            if entry_type == "stdio":
                entry = subprocess.Popen([target], stdin=subprocess.PIPE , stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                
                if entry.poll() == 0:
                    logging.error("test example: " + input + " result:  program crash!")
                    return
                
                # write stdin input
                entry.stdin.write(bytes(input.encode()))
                entry.stdin.close()
                # get the output
                result = entry.stdout.read().decode("gbk")
                entry.stdout.close()
                msg = "test example: " + input + " result: " + result
                if result == '':
                    msg = "test example: " + input + " result:  None Outout!"
                log_obj.debug_log(msg)
                # kill child proces
                entry.kill()
            # TODO
            else:
                pass
        except Exception as e:
            print(e)
            print(e.__traceback__.tb_frame.f_globals["__file__"])
            print(e.__traceback__.tb_lineno)
        

# main function
if __name__ == '__main__':
    config = json_read("./config.json")
    test = fuzz(config)
    test.fuzz_test()

