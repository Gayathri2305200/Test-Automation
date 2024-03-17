def diff(filename1,filename2):
    flag=0
    path1 = "C://Users//Gayathri_Kurapati//Desktop//python//Input_Output//{}".format(filename1)
    path2 = "C://Users//Gayathri_Kurapati//Desktop//python//Input_Output//{}".format(filename2)
    with open (path1,"r") as f1, open(path2,"r") as f2:
        content1=f1.read()
        content2=f2.read()
        if content1==content2:
            print("content same")
        else:
            print("content not same")