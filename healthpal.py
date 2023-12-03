import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="11intelli22tiate", database="leaderboard")
cursor=mydb.cursor()
e=1
while e!=0:
   e=int(input('1. Sign In\n2. Create a New Doctor Account\n'))
   if e==2:
      did=int(input('\nEnter id - '))
      dnf=input('Enter first name - ')
      dnl=input('Enter last name - ')
      pswd=input('Enter password - ')
      spec=input('Enter speciality - ')
      shf=input('Enter working shift - ')
      ph=input('Enter phone number - ')
      ##change next line
      sql="insert into doctors(d_id,dnamef,dnamel,pswd,speciality,shift,ph) values(%s,%s,%s,%s,%s,%s,%s)"
      val=(did,dnf,dnl,pswd,spec,shf,ph)
      cursor.execute(sql,val)
      mydb.commit()
      e=1
   elif e==1:
      did=int(input('\nEnter id - '))
      pswd=input('Enter password - ')
      sql="select count(d_id) from doctors where d_id=%s and pswd=%s"
      val=(did,pswd)
      cursor.execute(sql,val)
      if cursor.fetchone()[0]==1:
         print("\nSign in successful!")
         e=0
         r=1
         cursor.execute("""select d_id,dnamef,dnamel,speciality,shift,ph from doctors where d_id=%s and pswd=%s""",(did,pswd))
         for row in cursor.fetchall():
            print("Id: ", row[0])
            print("First Name: ", row[1])
            print("Last Name: ", row[2])
            print("Speciality: ", row[3])
            print("Shift: ", row[4])
            print("Phone number: ", row[5])
            while r!=0:
               print("\n 1. View Patient details\n 2. Add a New Patient\n 3. Delete Patient Details\n 0. Sign out")
               r=int(input())
               if r==1:
                  access=input("\nEnter Patient ID:- ")
      
                  cursor.execute("""select count(*) from patient where p_id=(%s) and p_id=%s""",(access,access))
                  if cursor.fetchone()[0]!=0:
                     cursor.execute("""select * from patient where p_id=(%s) and p_id=(%s)""",(access,access))
                     print("\nPatient Details - ")
                     for row in cursor.fetchall():
                        print("Id: ", row[0])
                        print("First Name: ", row[1])
                        print("Last Name: ", row[2])
                        print("City: ", row[3])
                        print("Date of Birth: ", row[4])
                        print("Age: ", row[5])
                        print("Date of Admission: ", row[6])
                        print("\nDiagnosis Report - ")
                        cursor.execute("""select count(*) from virus where p_id=(%s) and p_id=(%s)""",(access,access))
                        
                        if cursor.fetchone()[0]!=0:
                           cursor.execute("""select * from virus where p_id=(%s) and p_id=(%s)""",(access,access))
                           
                           for row in cursor.fetchall():
                              print("Id: ", row[0])
                              print("Disease Name: ", row[1])
                              print("Virus Name: ", row[2])
                              print("Treatment: ", row[3])
                              print("Symptoms: ", row[4])
                              print("\n")
                        cursor.execute("""select count(*) from bacteria where p_id=(%s) and p_id=(%s)""",(access,access))
                        if cursor.fetchone()[0]!=0:
                           cursor.execute("""select * from bacteria where p_id=(%s) and p_id=(%s)""",(access,access))
                           for row in cursor.fetchall():
                              print("Id: ", row[0])
                              print("Disease Name: ", row[1])
                              print("Bacteria Name: ", row[2])
                              print("Treatment: ", row[3])
                              print("Symptoms: ", row[4])
                              print("\n")
                        cursor.execute("""select count(*) from injury where p_id=(%s) and p_id=(%s)""",(access,access))
                        if cursor.fetchone()[0]!=0:
                           cursor.execute("""select * from injury where p_id=(%s) and p_id=(%s)""",(access,access))
                           for row in cursor.fetchall():
                              print("Id: ", row[0])
                              print("Injury Name: ", row[1])
                              print("Diagnosis Name: ", row[2])
                              print("Type: ", row[3])
                              print("\n")
                  else:
                     print("Incorrect Patient id or Mismatched Patient id")
               elif r==2:
                  pid=int(input('\nEnter id - '))
                  pnf=input('Enter first name - ')
                  pnl=input('Enter last name - ')
                  pcity=input('Enter city - ')
                  pdob=input('Enter date of birth - ')
                  page=int(input('Enter age - '))
                  pdoa=input('Enter date of admission - ')
                  pnum=input('Enter phone number - ')
                  cursor.execute("""insert into patient values(%s,%s,%s,%s,%s,%s,%s,%s)""",(pid,pnf,pnl,pcity,pdob,page,pdoa,pnum))
                  print("\n 1. Virus\n 2. Bacteria\n 3. Injury")
                  m=int(input())
                  if m==1:
                     dname=input("\nEnter disease name - ")
                     bname=input("Enter virus name - ")
                     treatment=input("Enter treatment - ")
                     symptoms=input("Enter symptoms - ")
                     cursor.execute("""insert into virus values(%s,%s,%s,%s,%s)""",(pid,dname,bname,treatment,symptoms))
                  elif m==2:
                     dname=input("\nEnter disease name - ")
                     bname=input("Enter bacteria name - ")
                     treatment=input("Enter treatment - ")
                     symptoms=input("Enter symptoms - ")
                     cursor.execute("""insert into bacteria values(%s,%s,%s,%s,%s)""",(pid,dname,bname,treatment,symptoms))
                  elif m==3:
                     iname=input("\nEnter injury name - ")
                     idiag=input("Enter diagnosis - ")
                     itype=input("Enter injury type - ")
                     cursor.execute("""insert into injury values(%s,%s,%s,%s)""",(pid,iname,idiag,itype))
                  print("\nPatient Added")
                  mydb.commit()
               elif r==3:
                  access=input("\nEnter Patient ID:- ")
                  
                  cursor.execute("""select count(*) from patient where p_id=(%s) and p_id=(%s)""",(access,access))
                  if cursor.fetchone()[0]!=0:
                     cursor.execute("""delete from patient where p_id=(%s) and p_id=(%s)""",(access,access))
                     cursor.execute("""select count(*) from virus where p_id=(%s) and p_id=(%s)""",(access,access))
                     if cursor.fetchone()[0]!=0:
                        cursor.execute("""delete from virus where p_id=(%s) and vname=(%s)""",(access,access))
                     cursor.execute("""select count(*) from bacteria where p_id=(%s) and p_id=(%s)""",(access,access))
                     if cursor.fetchone()[0]!=0:
                        cursor.execute("""delete from bacteria where p_id=(%s) and p_id=(%s)""",(access,access))
                     cursor.execute("""select count(*) from injury where p_id=(%s) and p_id=(%s)""",(access,access))
                     if cursor.fetchone()[0]!=0:
                        cursor.execute("""delete from injury where p_id=(%s) and p_id=(%s)""",(access,access))
                  
                  else:
                     print("Incorrect Patient id Patient does not exist")    
                  print("\nPatient Deleted")
                  mydb.commit()
               elif r==0:
                  print("\nSign out successful!")
                  break
      else:
         print("Incorrect User ID or pswd. Please retry ")
   break
mydb.commit()
mydb.close()
