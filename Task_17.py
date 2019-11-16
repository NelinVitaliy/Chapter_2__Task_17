user_hello = str(input('Say, Hello:'))
google_dictionary = ['1 - google_kazakstan.txt', '2 - google_paris.txt', '3 - google_uar.txt',
                     '4 - google_kyrgystan.txt', '5 - google_san_francisco.txt', '6 - google_germany.txt',
                     '7 - google_moscow.txt', '8 - google_sweden.txt']

if user_hello.lower() in 'hello':
    print('Choice file you want open?: ', (google_dictionary))
    x = int(input())
    if x == 1:
        myfile1 = open('google_kazakstan.txt', 'w')
        print("Name of a file is: ", myfile1.name)
        myfile1.write(input())
        print(myfile1)
        myfile1.close()
    if x == 2:
        myfile2 = open('google_paris.txt', 'w')
        print("Name of a file is: ", myfile2.name)
        myfile2.write(input())
        print(myfile2)
        myfile2.close()
    if x == 3:
        myfile3 = open('google_uar.txt', 'w')
        print("Name of a file is: ", myfile3.name)
        myfile3.write(input())
        print(myfile3)
        myfile3.close()








