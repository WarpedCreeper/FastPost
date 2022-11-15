print("FastPost")
from random import randint
print("To Upload Post Enter U to see Posts Enter P")
choise = input()

if choise == 'U' or choise == 'u':
  print('Enter your post text')
  postuploader = input()
  postprinter = postuploader
  print('Do you want to upload post? Enter Yes or No')
  postverify = input()
  
  if postverify == "Yes" or postverify == "yes":
    print("Your Post Upload")
    print(postprinter)
    print("To see Posts Enter P")
    choises2 == input()
if 
    
    
elif choise == "P" or choise == 'p':
  posts = ['Choice 1', 'Choice 2', 'Choice 3']
  print(posts[randint(0, len(posts)-1)])
  