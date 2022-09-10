# Fuzz Test frame work based python
- [Fuzz Test frame work based python](#fuzz-test-frame-work-based-python)
- [quick start](#quick-start)
- [config file](#config-file)

PyfuzzTest is a light quick fuzz test tool.

# quick start
1. get source code  
`git clone https://github.com/SongZihui-sudo/Pyfuzz.git`  
2. config and run test 
then config the file
3. finally run the fuzzTest.py
# config file
A example
```json
[
    {
        "target":"./target/BigNum-7/calc.exe",
        "target_type":"binary",
        "test_number":10,
        "config":
        {
            "entry":"stdio",
            "args":
            [
                "+",     
                "-", 
                "*",
                "print",
                "dup",
                "pop",
                "print",
                "swap",
                "dump"
            ],
            "input_data":
            [
                "None"
            ],
            "templete":"/%d/* /args/*-1"
        }
    }
]
```
`target`: target path  
`target_type`: target type a binary file or dll  
`test_number`: test number   
`config`: some configuration options  
  1. `entry`: program entry, stdio or function
  2. `args` : some args in the templete
  3. `input_data`:  like above the data used in templete
  4. `templete`: test example. split by /
     1.  %d %s %f data type int, string, float
     2.  args above
     3.  \\* generate several   
      \\*-number The number of the previous one is reduced by one    
      \\number Generate the specified number  
