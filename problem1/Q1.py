
# Method to Calculate Tower Height on based of give test(Input passed as integer)
def towerHeight(test: int):
    try:
        if (test < 0):
            return 0
        elif (test == 1):
            return 1
        elif (test == 2):
            return 2
        elif (test == 3):
            return 4
        else:
            # Calling towerHeight recursively to get tower height with integer value > 3
            return towerHeight(test - 1) + towerHeight(test - 2) + towerHeight(test - 3)
    # Exception Handeling
    except SyntaxError:
        print("Invalid syntax")
    except IndentationError:
        print("Indentation error")
    except TypeError:
        print("Given Input is not integer Enter Valid Integet value")
    except ArithmeticError as artherr:
        print(
            f"Found issue in calculation that is {type(artherr).__name__} please check at {artherr.__traceback__.tb_lineno}")
    except RecursionError:
        print(f"Maximum recursion depth exceeded")
    # handelling undefined error
    except Exception as e:
        print(
            f"{type(e).__name__} at line {e.__traceback__.tb_lineno} of {__file__}: {e}")


if __name__ == "__main__":
    # Take user T(N) input
    N = int(input("Enter integer Value: "))
    # passing input in method
    height = towerHeight(N)
    print(height)
