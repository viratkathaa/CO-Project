def add(r1,r2,r3):
    ans = disc_isa["add"]["opcode"]+"00"+disc_reg[r1]+disc_reg[r2]+disc_reg[r3]
    return ans

def sub(r1,r2,r3):
    ans = disc_isa["sub"]["opcode"]+"00"+disc_reg[r1]+disc_reg[r2]+disc_reg[r3]
    return ans

def mul(r1,r2,r3):
    ans = disc_isa["mul"]["opcode"]+"00"+disc_reg[r1]+disc_reg[r2]+disc_reg[r3]
    return ans

def div(r1,r2):
    ans = disc_isa["div"]["opcode"]+"00000"+disc_reg[r1]+disc_reg[r2]
    return ans

def xor(r1,r2,r3):
    ans = disc_isa["xor"]["opcode"]+"00"+disc_reg[r1]+disc_reg[r2]+disc_reg[r3]
    return ans

def or1(r1,r2,r3):
    ans = disc_isa["or"]["opcode"]+"00"+disc_reg[r1]+disc_reg[r2]+disc_reg[r3]
    return ans

def and_(e1,e2,e3):
    ans = disc_isa["and"]["opcode"]+"00"+disc_reg[e1]+disc_reg[e2]+disc_reg[e3]
    return ans

def not_(r1,r2):
    ans = disc_isa["not"]["opcode"]+"00000"+disc_reg[r1]+disc_reg[r2]
    return ans

def cmp(r1,r2):
    ans = disc_isa["cmp"]["opcode"]+"00000"+disc_reg[r1]+disc_reg[r2]
    return ans

def hlt():
    ans = disc_isa["hlt"]["opcode"]+"00000000000"
    return ans



disc_reg = {"R0" : "000","R1" : "001", "R2" : "010" , "R3" : "011" , "R4" : "100" , "R5" : "101" , "R6" :"110", "FLAGS" : "111"}
disc_isa = {
        "add" : {"opcode" : "00000", "type" : "a"},
        "sub" : {"opcode" : "00001", "type" : "a"},
        "mov1" : {"opcode" : "00010", "type" : "b"},
        "mov2" : {"opcode" : "00011", "type" : "c"},
        "ld" : {"opcode" : "00100", "type" : "d"},
        "st" : {"opcode" : "00101", "type" : "d"},
        "mul" : {"opcode" : "00110", "type" : "a"},
        "div" : {"opcode" : "00111", "type" : "c"},
        "rs" : {"opcode" : "01000", "type" : "b"},
        "ls" : {"opcode" : "01001", "type" : "b"},
        "xor" : {"opcode" : "01010", "type" : "a"},
        "or" : {"opcode" : "01011", "type" : "a"},
        "and" : {"opcode" : "01100", "type" : "a"},
        "not" : {"opcode" : "01101", "type" : "c"},
        "cmp" : {"opcode" : "01110", "type" : "c"},
        "jmp" : {"opcode" : "01111", "type" : "e"},
        "jlt" : {"opcode" : "11100", "type" : "e"},
        "jgt" : {"opcode" : "11101", "type" : "e"},
        "je" : {"opcode" : "11111", "type" : "e"},
        "hlt" : {"opcode" : "11010", "type" : "f"}}
        