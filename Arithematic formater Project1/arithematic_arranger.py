def arithmetic_arranger(problems,calc= False):
  top = ''
  bottom = ''
  end = ''
  # check if no. of problems is less than 6
  if len(problems)<6:
    #loop each problem from the entire problem list
    for problem in problems:
      # split each term of each problem
      term = problem.split()
      # check if operator is + and - only
      if term[1] == '+' or term[1] == '-':
        # check if only digits are at pos 0 and 2
        if term[0].isnumeric() and term[2].isnumeric():
          # check if any number(operand) is more than 4
          if len(term[0])<5 and len(term[2])<5:
            #first iteration right justify top ,bottom , ans .
            if top == '':
              top = term[0].rjust(max(len(term[2]),len(term[0]))+2)
              bottom = term[1] + term[2].rjust(max(len(term[2]),len(term[0]))+1)
              end = '-'*(max(len(term[2]),len(term[0]))+2)
              # incase of solution check if it is add(+) or subs(-)
              if term[1] == '+':
                sum = int(term[0])+ int(term[2])
                ans = str(sum).rjust(max(len(term[2]),len(term[0]))+2)
              elif term[1] == '-':
                sum = int(term[0]) - int(term[2])
                ans = str(sum).rjust(max(len(term[2]),len(term[0]))+2)
                # second onward iteration
            else:
              top = top + '    ' + term[0].rjust(max(len(term[2]),len(term[0]))+2)
              bottom =bottom + '    ' + term[1] + term[2].rjust(max(len(term[2]),len(term[0]))+1)
              end = end + '    ' + '-'*(max(len(term[2]),len(term[0]))+2)
              if term[1] == '+':
                sum = int(term[0])+ int(term[2])
                ans = ans + '    ' + str(sum).rjust(max(len(term[2]),len(term[0]))+2)
              elif term[1] == '-':
                # convert ans back to string
                sum = int(term[0]) - int(term[2])
                ans = ans + '    ' + str(sum).rjust(max(len(term[2]),len(term[0]))+2)
                # error messages in return to exit the function
          elif len(term[0])>=5 or len(term[2])>=5:
            return ('Error: Numbers cannot be more than four digits.')
        elif not(term[0].isnumeric()) or not(term[2].isnumeric()) :
          return ('Error: Numbers must only contain digits.')
      elif term[1] != '+' or term[1] != '-':
        return ("Error: Operator must be '+' or '-'.")
  elif len(problems)>=6:
    return ('Error: Too many problems.')
    # if calc is true than we have to solve the problem
  if calc:
    arranged_problems = top + '\n' + bottom + '\n' + end + '\n' + ans
    return arranged_problems
  else:
    arranged_problems = top + '\n' + bottom + '\n' + end
    return arranged_problems
