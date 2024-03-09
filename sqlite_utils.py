from sqlite_context import SqliteConnection
from datetime import datetime
CURRENT_DATE=datetime.now()
class DbOperations:
    
    def create_vehicle_table(self):
        with SqliteConnection("data.db") as connection:
            cursor = connection.cursor()
            cursor.execute(
                """CREATE TABLE If NOT EXISTS Underwriter(
                            Uwrt_id INTEGER,
                            name varchar(45) NOT NULL,
                            dob DATE NOT NULL,
                            joining_date DATE NOT NULL,
                            def_pswrd VARCHAR(45) NOT NULL
                            )"""
            )
        print("table 1 created")

    def insert_underwriter_data(self, vehicle_list):
        with SqliteConnection("underwriter.db") as connection:
            cursor = connection.cursor()
            cursor.execute(
                """insert into Underwriter values(?,?,?,?,?)""", vehicle_list
            )
            print("Data Inserted.")
    def get_underwriter_data(self):
        with SqliteConnection("underwriter.db") as connection:
            cursor=connection.cursor()
            cursor.execute('''Select * from Underwriter''')
            vals=cursor.fetchall()
            return vals
    def get_underwriter_data_with_id(self, usr_id):
        with SqliteConnection("underwriter.db") as connection:
            cursor=connection.cursor()
            cursor.execute('''Select * from Underwriter where Uwrt_id==?''',(usr_id,))
            print("ok")
            vals=cursor.fetchall()
            return vals
    def  get_underwriter_data_by_name(self, name):
        with SqliteConnection("underwriter.db") as connection:
            cursor=connection.cursor()
            cursor.execute('''Select * from Underwriter where name LIKE ?''',("%"+name+"%",))
            print("ok")
            vals=cursor.fetchall()
            return vals
    def change_password(self,n_pass,usr_id):
        with SqliteConnection("underwriter.db") as connection:
            cursor=connection.cursor()
            cursor.execute('''Update Underwriter set def_pswrd=? where Uwrt_id==?''',(n_pass, usr_id))
            # vals=cursor.fetchall()
            # return vals
    def del_using_id(self, usr_id):
        with SqliteConnection("underwriter.db") as connection:
            cursor=connection.cursor()
            cursor.execute('''Delete from Underwriter where Uwrt_id==?''',(usr_id,))

    def drop1(self):
        with SqliteConnection("underwriter.db") as connection:
            cursor = connection.cursor()
            cursor.execute("""drop table underwriter""")
            print("Data Deleted.")

    def create_starproject_table(self):
        with SqliteConnection("starproject2.db") as connection:
            cursor = connection.cursor()
            cursor.execute(
                """create table If NOT EXISTS InsurancePolicy2(
                PolicyNo  VARCHAR(20),
                VehicleNo VARCHAR(20),
                VehicleType VARCHAR(20),
                CustomerName VARCHAR(40),
                EngineNo  VARCHAR(20),
                ChasisNO  VARCHAR(20),
                PhoneNo  VARCHAR(20),
                InsuranceType VARCHAR(40),
                PremiumAmnt  VARCHAR(20),
                FromDate DATE,
                Todate DATE,
                UNDERWRITERID INT,
                FOREIGN KEY(UNDERWRITERID)
                REFERENCES UNDERWRITER(uwrt_id))"""
            )
            print("Table Created")

    def insert_starProject(self, str_list):
        with SqliteConnection("starproject2.db") as connection:
            cursor = connection.cursor()
            print(list(str_list))
            print("Data Inserted.")
            cursor.execute(
                """insert into InsurancePolicy2 values(?,?,?,?,?,?,?,?,?,?,?,?)""",
                str_list,
            )
            print("Data Inserted.")
    def get_vehicles_data(self,usr_id):
        with SqliteConnection("starproject2.db") as connection:
            cursor=connection.cursor()
            cursor.execute('''Select * from InsurancePolicy2 where UNDERWRITERID==?''',(usr_id,))
            vals=cursor.fetchall()
            # print(vals)
            return vals

    def drop2(self):
        with SqliteConnection("starproject2.db") as connection:
            cursor = connection.cursor()
            cursor.execute("""drop table InsurancePolicy2""")
            print("Data Deleted.")
    def finding_using_policy_no(self,pi):
        with SqliteConnection("starproject2.db") as connection:
            # print("enter the policy no")
            # pi=input()
            cursor = connection.cursor()
            cursor.execute('''SELECT * FROM INSURANCEPOLICY2 WHERE POLICYNO="P11"''')
            vechs=cursor.fetchall()
            print(vechs)
    def no_vechs_details(self):
        with SqliteConnection("starproject2.db") as connection:
            # print("enter the policy no")
            # pi=input()
            cursor = connection.cursor()
            cursor.execute('''SELECT *,COUNT(VEHICLENO) AS NUM_OF_VEHICLES FROM INSURANCEPOLICY2 GROUP BY UNDERWRITERID''')
            cnt=cursor.fetchall()
            print(cnt)
    def date_exp(self):
        with SqliteConnection("starproject2.db") as connection:
            # print("enter the policy no")
            # pi=input()
            # print(TOD)
            s=str(CURRENT_DATE)
            # print(s)
            lst=s.split(" ")
            # print(lst[0])
            cursor = connection.cursor()
            cursor.execute('''SELECT * FROM INSURANCEPOLICY2 WHERE Todate<CURRENT_DATE''')
            cnt=cursor.fetchall()
            print(cnt)
    def del_data(self):
        with SqliteConnection("starproject2.db") as connection:
            # print("enter the policy no")
            # pi=input()
            cursor = connection.cursor()
            cursor.execute('''Delete from INSURANCEPOLICY2 where UNDERWRITERID=1''')
    def drop3(self):
        with SqliteConnection("starproject.db") as connection:
            cursor = connection.cursor()
            cursor.execute("""drop table InsurancePolicy""")
            print("Data Deleted.") 
          


d = DbOperations()
# d.drop1()
# d.drop2()
# d.drop3()