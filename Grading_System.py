print("--- Student Grading System ---")

#accepts data
full_name = input("enter student full name:")
exam = int(input("enter exam score:"))
assessment = int(input("enter assessment score:"))
fees = int(input("enter fees paid:"))

total = exam + assessment

print("\n--- Student Report ---")
print("student name:", full_name)
print("exam score:", exam)
print("assessment score:", assessment)
print("total score:", total)
print("fees paid:", fees)

#component results
if exam >= 25:
    print("exam: passed")
else:
    print("exam failled")

    if assessment >= 15:
        print("assessment passed")
    else:
        print("assessment failed")

           
if exam >= 25 and assessment >= 15:
    print("result: passed")
    result = "PASS"

elif total == 39:
    print("result: condoned")
    result = "PASS"

else:
     print("result: failed")
     result = "FAIL"

#repeat condition
if exam < 25 and assessment < 15:
    print("action: repeat")

#certificate condition
if result == "PASS":
 if fees >= 100:
    print("certificate: issued")
else:
    print("certificate: not issued (fees not fully paid)")

