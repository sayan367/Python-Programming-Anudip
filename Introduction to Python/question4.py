# Global variable
variable = "I am a global variable"

def demo_variables():
    # Local variable with the same name
    variable = "I am a local variable"
    print("Inside the function:")
    print("Local variable:", variable)  # Accesses the local variable

def modify_global_variable():
    global variable  # Declare that we are modifying the global variable
    variable = "I have been modified globally"

print("Before modifying the global variable:")
print("Global variable:", variable)  # Accesses the global variable

# Call the function to demonstrate local variable usage
demo_variables()

# Modify the global variable
modify_global_variable()

print("After modifying the global variable:")
print("Global variable:", variable)  # Accesses the modified global variable
