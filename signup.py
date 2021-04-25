print("*"*240,"\t\t\t\tWELCOME")
while True:
      qw=input("Do you need to sign up?(yes or no):")
      if qw=="yes":
            print("*"*40,"sign up","*"*40)  #sign up start
            x=input("username:")
            z=input("password:")
            if x=="shihab" and z=='12345':
                  break
            else:
                  c=input("email:")
                  d=input("phone no:")
                  print("*"*40,"sign in","*"*40)
                  while True:
                        e=input("username:")
                        f=input("password:")
                        if (e==x or e==c or e==d) and f==z:
                              break
                        else:
                              print('username or password is wrong!!!!!!!')
                  break  # sign up end
      elif qw=='no':
            print("*"*40,"sign in","*"*40) #sign in start
            a=input("username:")
            b=input("password:")
            if a=='shihab' and b=='12345': # reset the username and password  which you need otherwise this username and password will work in sign in option
                  break
            else:
                  print('username or password is wrong better sign up again........')
      else:
            print('invalied operation!!!!!!!')  #sign in end
print('sign up program is successful')