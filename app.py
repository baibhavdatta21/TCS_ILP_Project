from sqlite_utils import *
from flask import Flask, render_template,request,redirect,url_for,session
database=DbOperations()
count=0
def initialization():
    database.create_vehicle_table()
    dict1={}
    dict1[1]=["Baibhav","12-12-2001","21-10-2012","ab"]
    dict1[2]=["Akshat","11-02-2000","29-06-2010","cvv13@"]
    dict1[3]=["Manikant","25-01-2001","21-01-2012","a223@"]
    dict1[4]=["Ashish","15-08-2000","12-02-2013","ab1232@"]
    global count
    count+=1
    for i in dict1.keys():
        lst=[]
        lst.append(count)
        count+=1
        database.insert_underwriter_data(lst+dict1[i])
    database.create_starproject_table()
    dict2={}
    dict2[1]=[["P11","V11","2-wheeler","Baibhav","E11","Ch11","9876543211","Third Party", "1000","21-02-18","2023-04-12"]]
    dict2[2]=[["P12","V12","4-wheeler","Akshat","E12","Ch12","9832117654","Full insurance","2500","21-02-21","2022-01-02"]]
    for i in dict2.keys():
        for j in dict2[i]:
            lst=[]
            for k in j:
                lst.append(k)
            lst.append(i)
            database.insert_starProject(lst)

app = Flask(__name__)
app.secret_key = 'secret_key_'
@app.route('/',methods=["GET","POST"])
def fun0():
    if request.method=="GET":
        return render_template('welcome.html')
    if request.method=="POST":
        if('btn2' in request.form):
            return redirect(url_for('fun1'))

@app.route('/login',methods=["GET","POST"])
def fun1():
    if request.method=="GET":
        return render_template('NewLogin.html')
    if request.method=="POST":
        login_type = request.form.get('login_type')
        if(login_type=='user'):
            usr_id=int(request.form["id"])
            usr_pass=request.form["pass"]
            # print(usr_id)
            # print(usr_pass)
            data =database.get_underwriter_data()
            f=1
            
            for i in data:
                if(i[0]==usr_id and i[4]==usr_pass):
                    f=2
                    hold=i[1]
                    break

            if(f==2):
                # print("hold",hold)
                return redirect(url_for('fun2', usr_id=usr_id, usr_name=hold))
            else:
                # print("here")
                return redirect(url_for('fun6'))
        else:
            admin_id=int(request.form["id"])
            admin_pass=request.form["pass"]
            # print(admin_id)
            # print(admin_pass)
            if(admin_id==101 and admin_pass=="admin"):
                return redirect(url_for('fun3'))
            else:
                return redirect(url_for('fun6'))
        

@app.route('/UserDashboard.html',methods=["GET","POST"])
def fun2():
    if(request.method=="GET"):
        usr_id=request.args.get('usr_id')
        usr_name=request.args.get('usr_name')
        vehicles_data=database.get_vehicles_data(usr_id)
        return render_template('UserDashboard.html',usr_id=usr_id, usr_name=usr_name,vehicles_data=vehicles_data)
    elif(request.method=="POST"):
        return redirect(url_for('fun5'))


@app.route('/AdminDashboard.html', methods=["GET", "POST"])
def fun3():
    if request.method == "GET":
        usr_data = database.get_underwriter_data()
        return render_template('AdminDashboard.html', usr_data=usr_data)
    elif request.method == "POST":
        if 'chg_pass' in request.form:
            session['change_password_id'] = request.form['chg_pass']
            print("In func 3",session.get('change_password_id'))
            return redirect(url_for('fun8'))
        elif 'del_data' in request.form:
            session['del_usr'] = request.form['del_data']
            return redirect(url_for('fun9'))
        elif 'new_registration' in request.form:
            return redirect(url_for('fun4'))
        elif 'search_by_name' in request.form:
            name=request.form["search_by_name"]
            usr_data = database.get_underwriter_data_by_name(name)
            return render_template('AdminDashboard.html', usr_data=usr_data)



@app.route('/NewUserRegistration.html',methods=["GET","POST"])
def fun4():
    if(request.method=="GET"):
        return render_template('NewUserRegistration.html')
    elif(request.method=="POST"):
        f_name=request.form["f_name"]
        dob=request.form["dob"]
        doj=request.form["doj"]
        pass1=request.form["pass"]
        lst=[]
        global count
        count+=1
        lst.append(count)
        lst.append(f_name)
        lst.append(dob)
        lst.append(doj)
        lst.append(pass1)
        database.insert_underwriter_data(lst)
        count+=1
        return redirect(url_for('fun7'))


@app.route('/NewVehicle.html',methods=["GET","POST"])
def fun5():
    # print("ok")
    if(request.method=="GET"):
        return render_template('NewVehicle.html')
    elif(request.method=="POST"):
        print("ok2")
        p_no=request.form["p_no"]
        v_no=request.form["v_no"]
        v_type=request.form.get('v_type')
        c_name=request.form["c_name"]
        en_no=request.form["en_no"]
        ch_no=request.form["ch_no"]
        ph_no=request.form["ph_no"]
        ins_type=request.form.get('ins_type')
        prem_am=request.form["prem_am"]
        from_date=request.form["from_date"]
        to_date=request.form["to_date"]
        usr_id=int(request.form["usr_id"])
        lst=[]
        lst.append(p_no)
        lst.append(v_no)
        lst.append(v_type)
        lst.append(c_name)
        lst.append(en_no)
        lst.append(ch_no)
        lst.append(ph_no)
        lst.append(ins_type)
        lst.append(prem_am)
        lst.append(from_date)
        lst.append(to_date)
        lst.append(usr_id)
        # print(lst)
        database.insert_starProject(lst)
        return redirect(url_for('fun7'))

    

@app.route('/error',methods=["GET","POST"])
def fun6():
    if(request.method=="GET"):
        return render_template('ErrorPage.html')
    if(request.method=="POST"):
        print("INSIDE POST")
        if('btn1' in request.form):
            return redirect(url_for('fun5'))
        elif('btn2' in request.form):
            return redirect(url_for('fun1'))
            



@app.route('/success',methods=["GET","POST"])
def fun7():
    if(request.method=="GET"):
        return render_template('V_Success.html')
    if(request.method=="POST"):
        if('btn1' in request.form):
            return redirect(url_for('fun5'))
        elif('btn2' in request.form):
            return redirect(url_for('fun1'))

@app.route('/password_chg', methods=["GET","POST"])
def fun8():
    
    usr_id = session.get('change_password_id')
    # usr_id = session.pop('change_password_id', None)
    print("In func 8",usr_id)
    if(request.method=="GET"):
        # print(usr_id)
        return render_template('Change_Password.html')
    if(request.method=="POST"):
        current_password=request.form["cur_password"]
        new_password=request.form["new_password"]
        # usr_id=request.args.get('usr_id')
        # print(usr_id)
        d=database.get_underwriter_data_with_id(usr_id)
        for i in d:
            if(current_password!=i[4]):
                return redirect(url_for('fun6'))
            else:
                database.change_password(new_password, usr_id)
                return redirect(url_for('fun7'))
        
@app.route('/delete_user', methods=["GET", "POST"])
def fun9():
    usr_id = session.pop('del_usr', None)
    if usr_id:
        database.del_using_id(usr_id)
    return redirect(url_for('fun3'))
        

initialization()
# if __name__=="__main__":
#     app.run()