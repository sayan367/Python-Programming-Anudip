# Global variable
global_variable = "I am a global variable"

def local_variable_demo():
    # Local variable
    local_variable = "I am a local variable"
    
    print("Inside the function:")
    print(local_variable)         # Accessing local variable
    print(global_variable)        # Accessing global variable

def modify_global_variable():
    global global_variable  # Declare that we are using the global variable
    global_variable = "I have been modified"

print("Before modifying the global variable:")
print(global_variable)

# Call the function to demonstrate local and global variables
local_variable_demo()

# Modify the global variable
modify_global_variable()

print("After modifying the global variable:")
print(global_variable)