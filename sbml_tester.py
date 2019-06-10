# Tester class to mass test expression evaluator
import subprocess

passes = 0
fails = 0

for x in range(10):
    # For HW4 (given) cases: "hw4_given_cases/input_" and "hw4_given_cases/output_" range==50
    # For HW4 (graded) cases: "hw4_graded_cases/test_case/input" and "hw4_graded_cases/test_case/output" range==10
    # Currently testing HW3 cases range==25
    inputName = "hw4_graded_cases/test_case/input" + str(x + 1) + ".txt"
    outputName = "hw4_graded_cases/test_case/output" + str(x + 1) + ".txt"
    inputFile = open(inputName, "r")
    outputFile = open(outputName, "r")
    output = subprocess.check_output('py sbml_HW4_regrade.py '+ inputName)
    # Run command with arguments and return its output as a byte string.
    decoded = output.decode("UTF-8")
    decoded = decoded.replace("\n", "")
    decoded = decoded.replace("\r", "")
    lines = []
    for line in outputFile:
        lines += line.strip()
    lineOut = ''.join(str(e) for e in lines)
    if lineOut == decoded:
        print("Test Case " + str(x + 1) + " Passed")
        print("Program output: " + decoded)
        print("Correct output: " + lineOut)
        print("--------------------------------")
        print("--------------------------------")
        passes = passes + 1
    else:
        print("Test Case " + str(x + 1) + " Failed")
        print("Program output: " + decoded)
        print("Correct output: " + lineOut)
        print("--------------------------------")
        fails = fails + 1

print(str(passes) + " cases passed out of 50")
