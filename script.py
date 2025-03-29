def find_cube_pairs(targ):
    sol = []
    max_num = round(targ ** (1/3))  

    for a in range(1, max_num + 1):
        for b in range(a, max_num + 1):
            if a**3 + b**3 == targ:
                sol.append((a, b))
    return sol

pair = find_cube_pairs(1728)
print("Valid cube pairs for 1728:")
for a, b in pair:
    print(f" → {a}³ + {b}³ = {a**3} + {b**3} = 1728")

"""Submit your response here:  https://forms.office.com/Pages/ResponsePage.aspx?id=vDsaA3zPK06W7IZ1VVQKHFzW4INMf2JMjyL9qPnlPbNUMFU2TjI1WjQyUlczSFNIOFBEWkxTQ0lFQS4u"""

"""
1. added missing colons in lines 1,5,6,7,13
2. removed semicolons at end of lines 2,8
3. changed ranges to range in lines 2,5
4. changed target to targ in function parameter in line 1
5. changed solutions to sol in line 2
6. changed printf to print in line 12,14
7. changed pairs to pair in line 11
8. changed *** to ** in line 4,7
9. removed commas in line 12,13
10. changed 2 to 3 in line 14, (logic error not syntax)
11. changed 1729 to 1728 in line 11
"""