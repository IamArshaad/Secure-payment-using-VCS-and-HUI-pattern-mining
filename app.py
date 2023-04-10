from flask import *
from DBConnection import Db
from mkl import likdecrypt
from qrcode_p import gen_qrcode, gen_qrcode_2

app = Flask(__name__)
app.secret_key="9876"

@app.route('/')
def login():
    return render_template('index.html')

@app.route('/login_post',methods=['post'])
def login_post():
    username=request.form['textfield']
    password=request.form['textfield2']
    db=Db()
    qry="SELECT * FROM `login` WHERE `username`='"+username+"' AND `password`='"+password+"'"
    res=db.selectOne(qry)
    if res is not None:
        session['lid']=res['lid']
        if res['type']=="admin":
            return "<script>alert('Login Succesfull');window.location='/a_home'</script>"
        elif res['type']=="vendor":
            return "<script>alert('Login Succesfull');window.location='/v_home'</script>"
        else:
            return "<script>alert('Invalid Login, Try Again!');window.location='/'</script>"
    else:
        return "<script>alert('Enter Valid Credentials!');window.location='/'</script>"


@app.route('/logout')
def logout():
    session['lid']=""
    return redirect('/')

#=======Admin==========

@app.route('/a_home')
def a_home():
    if session['lid']!='':
        return render_template('admin/a_index.html')
    else:
        return '''<script>alert("Please login again!");window.location='/'</script>'''

@app.route('/AddCategory')
def AddCategory():
    if session['lid']!='':
        return render_template('admin/AddCategory.html')
    else:
        return '''<script>alert("You are logout..");window.location='/'</script>'''

@app.route('/AddCategory_post',methods=['post'])
def AddCategory_post():
    if session['lid']!='':
        categoryname=request.form['textfield']
        db=Db()
        qry="INSERT INTO `category`(`c_name`)VALUES('"+categoryname+"')"
        res=db.insert(qry)
        return "<script>alert('Category Added');window.location='/AddCategory'</script>"
    else:
        return '''<script>alert("You are logout..");window.location='/'</script>'''

@app.route('/reject_approved_vendors/<id>')
def reject_approved_vendors(id):
    if session['lid']!='':
        db=Db()
        qry = "UPDATE `vendors` SET `status`='Rejected' WHERE `v_id`='" + id + "'"
        res=db.update(qry)
        return "<script>alert('Rejected Succesfully');window.location='/ApprovedVendors'</script>"
    else:
        return '''<script>alert("You are logout..");window.location='/'</script>'''

@app.route('/ApprovedVendors')
def ApprovedVendors():
    if session['lid']!='':
        db=Db()
        qry="SELECT * FROM `vendors`WHERE `status`='Approved'"
        res=db.select(qry)
        return render_template('admin/ApprovedVendors.html',data=res)
    else:
        return '''<script>alert("You are logout..");window.location='/'</script>'''

@app.route('/ApprovedVendors_post',methods=['post'])
def ApprovedVendors_post():
    if session['lid']!='':
        search=request.form['textfield']
        db = Db()
        qry = "SELECT * FROM `vendors` WHERE `status`='Approved' AND `v_name` LIKE '%" + search + "%'"
        res = db.select(qry)
        return render_template('admin/ApprovedVendors.html', data=res)
    else:
        return '''<script>alert("You are logout..");window.location='/'</script>'''

@app.route('/EditCategory/<id>')
def EditCategory(id):
    if session['lid']!='':
        db=Db()
        qry="SELECT * FROM `category`WHERE `c_id`='"+id+"'"
        res=db.selectOne(qry)
        return render_template('admin/EditCategory.html',data=res)
    else:
        return '''<script>alert("You are logout..");window.location='/'</script>'''

@app.route('/EditCategory_post',methods=['post'])
def EditCategory_post():
    if session['lid']!='':
        id=request.form['id']
        categoryname=request.form['textfield']
        db=Db()
        qry="UPDATE `category`SET `c_name`='"+categoryname+"' WHERE `c_id`='"+id+"'"
        res=db.update(qry)
        return "<script>alert('Category Updated');window.location='/ad_ViewCategory'</script>"
    else:
        return '''<script>alert("You are logout..");window.location='/'</script>'''

@app.route('/approve_rejected_vendors/<id>')
def approve_rejected_vendors(id):
    if session['lid']!='':
        db=Db()
        qry = "UPDATE `vendors` SET `status`='Approved' WHERE `v_id`='" + id + "'"
        res=db.update(qry)
        return "<script>alert('Approved Succesfully');window.location='/RejectedVendors'</script>"
    else:
        return '''<script>alert("You are logout..");window.location='/'</script>'''


@app.route('/RejectedVendors')
def RejectedVendors():
    if session['lid']!='':
        db = Db()
        qry = "SELECT * FROM `vendors`WHERE `status`='Rejected'"
        res = db.select(qry)
        return render_template('admin/RejectedVendors.html',data=res)
    else:
        return '''<script>alert("You are logout..");window.location='/'</script>'''

@app.route('/RejectedVendors_post',methods=['post'])
def RejectedVendors_post():
    if session['lid']!='':
        search=request.form['textfield']
        db = Db()
        qry = "SELECT * FROM `vendors` WHERE `status`='Rejected' AND `v_name` LIKE '%" + search + "%'"
        res = db.select(qry)
        return render_template('admin/RejectedVendors.html', data=res)
    else:
        return '''<script>alert("You are logout..");window.location='/'</script>'''

@app.route('/Reply/<id>')
def Reply(id):
    if session['lid']!='':
        return render_template('admin/Reply.html',cid=id)
    else:
        return '''<script>alert("You are logout..");window.location='/'</script>'''

@app.route('/Reply_post',methods=['post'])
def Reply_post():
    if session['lid']!='':
        reply=request.form['textfield']
        cid=request.form['cid']
        db=Db()
        qry="UPDATE `complaint` SET `c_reply`='"+reply+"',`c_status`='Replied' WHERE `comp_id`='"+cid+"' "
        res=db.update(qry)
        return "<script>alert('Replied');window.location='/ViewComplaint'</script>"
    else:
        return '''<script>alert("You are logout..");window.location='/'</script>'''

@app.route('/delete_category/<id>')
def delete_category(id):
    if session['lid']!='':
        db=Db()
        qry="DELETE FROM `category`WHERE `c_id`='"+id+"'"
        res=db.delete(qry)
        return redirect('/ad_ViewCategory')
    else:
        return '''<script>alert("You are logout..");window.location='/'</script>'''

@app.route('/ad_ViewCategory')
def ad_ViewCategory():
    if session['lid']!='':
        db=Db()
        qry="SELECT * FROM `category`"
        res=db.select(qry)
        return render_template('admin/ViewCategory.html',data=res)
    else:
        return '''<script>alert("You are logout..");window.location='/'</script>'''

@app.route('/ViewComplaint')
def ViewComplaint():
    if session['lid']!='':
        db=Db()
        qry="SELECT * FROM `complaint`JOIN`vendors`ON `complaint`.`v_lid`=`vendors`.`v_lid`"
        res=db.select(qry)
        return render_template('admin/ViewComplaint.html',data=res)
    else:
        return '''<script>alert("You are logout..");window.location='/'</script>'''

@app.route('/ViewComplaint_post',methods=['post'])
def ViewComplaint_post():
    if session['lid']!='':
        fromdate=request.form['textfield']
        todate=request.form['textfield2']
        db = Db()
        qry = "SELECT * FROM `complaint`JOIN`vendors`ON `complaint`.`v_lid`=`vendors`.`v_lid` WHERE `complaint`.`c_date` BETWEEN '"+fromdate+"' AND '"+todate+"'"
        res = db.select(qry)
        return render_template('admin/ViewComplaint.html', data=res)
    else:
        return '''<script>alert("You are logout..");window.location='/'</script>'''

@app.route('/ViewFeedback')
def ViewFeedback():
    if session['lid']!='':
        db=Db()
        qry="SELECT * FROM `feedback`JOIN `users`ON `feedback`.`u_lid`=`users`.`u_lid`"
        res= db.select(qry)
        return render_template('admin/ViewFeedback.html',data=res)
    else:
        return '''<script>alert("You are logout..");window.location='/'</script>'''

@app.route('/ViewFeedback_post',methods=['post'])
def ViewFeedback_post():
    if session['lid']!='':
        fromdate=request.form['textfield']
        todate=request.form['textfield2']
        db = Db()
        qry = "SELECT * FROM `feedback`JOIN `users`ON `feedback`.`u_lid`=`users`.`u_lid` WHERE `feedback`.`f_date` BETWEEN '"+fromdate+"' AND '" + todate + "'"
        res = db.select(qry)
        # print(res)
        return render_template('admin/ViewFeedback.html', data=res)
    else:
        return '''<script>alert("You are logout..");window.location='/'</script>'''

@app.route('/ViewProducts')
def ViewProducts():
    if session['lid']!='':
        db=Db()
        qry="SELECT * FROM `product` JOIN `category`ON `product`.`c_id`=`category`.`c_id`"
        res=db.select(qry)
        return render_template('admin/ViewProducts.html',data=res)
    else:
        return '''<script>alert("You are logout..");window.location='/'</script>'''

@app.route('/ViewUsers')
def ViewUsers():
    if session['lid']!='':
        db=Db()
        qry="SELECT * FROM `users`"
        res=db.select(qry)
        return render_template('admin/Viewusers.html',data=res)
    else:
        return '''<script>alert("You are logout..");window.location='/'</script>'''

@app.route('/approve_vendors/<id>')
def approve_vendors(id):
    if session['lid']!='':
        db=Db()
        qry="UPDATE `vendors` SET `status`='Approved' WHERE `v_id`='"+id+"'"
        res=db.update(qry)
        return "<script>alert('Approved Succesfully');window.location='/ViewVendors'</script>"
    else:
        return '''<script>alert("You are logout..");window.location='/'</script>'''

@app.route('/reject_vendors/<id>')
def reject_vendors(id):
    if session['lid']!='':
        db=Db()
        qry="UPDATE `vendors` SET `status`='Rejected' WHERE `v_id`='"+id+"'"
        res=db.update(qry)
        return "<script>alert('Rejected Succesfully');window.location='/ViewVendors'</script>"
    else:
        return '''<script>alert("You are logout..");window.location='/'</script>'''

@app.route('/ViewVendors')
def ViewVendors():
    if session['lid']!='':
        db = Db()
        qry = "SELECT * FROM `vendors` WHERE `status`='pending'"
        res = db.select(qry)
        return render_template('admin/ViewVendors.html',data=res)
    else:
        return '''<script>alert("You are logout..");window.location='/'</script>'''

@app.route('/ViewVendors_post',methods=['post'])
def ViewVendors_post():
    if session['lid']!='':
        search=request.form['textfield']
        db = Db()
        qry = "SELECT * FROM `vendors` WHERE `status`='pending' AND `v_name` LIKE '%"+search+"%'"
        res = db.select(qry)
        return render_template('admin/ViewVendors.html', data=res)
    else:
        return '''<script>alert("You are logout..");window.location='/'</script>'''

#=======Vendor==========

@app.route('/v_home')
def v_home():
    if session['lid']!='':
        return render_template('Vendor/v_index.html')
    else:
        return '''<script>alert("You are logout..");window.location='/'</script>'''


@app.route('/AddProduct')
def AddProduct():
    if session['lid']!='':
        db=Db()
        qry ="SELECT * FROM `category` "
        res=db.select(qry)
        return render_template('Vendor/AddProduct.html',data=res)
    else:
        return '''<script>alert("You are logout..");window.location='/'</script>'''

@app.route('/AddProduct_post',methods=['post'])
def AddProduct_post():
    if session['lid']!='':
        product=request.form['textfield']
        category=request.form['select']
        price=request.form['textfield2']
        profit=request.form['textfield3']
        db = Db()
        qry = "INSERT INTO `product`(`c_id`,`p_name`,`p_price`,`v_lid`,`profit`)VALUES ('"+category+"','"+product+"','"+price+"','"+str(session['lid'])+"','"+profit+"')"
        res = db.insert(qry)
        return "<script>alert('Product Added');window.location='/AddProduct'</script>"
    else:
        return '''<script>alert("You are logout..");window.location='/'</script>'''

@app.route('/AddStock')
def AddStock():
    if session['lid']!='':
        db=Db()
        qry="SELECT * FROM `product`"
        res=db.select(qry)
        return render_template("Vendor/AddStock.html",data=res)
    else:
        return '''<script>alert("You are logout..");window.location='/'</script>'''


@app.route('/AddStock_post',methods=['post'])
def AddStock_post():
    if session['lid']!='':
        productname = request.form['select']
        quantity = request.form['textfield']
        db = Db()
        qry = "INSERT INTO `stock`(`p_id`,`quantity`) VALUES ('" + productname + "','" + quantity + "')"
        res = db.insert(qry)
        return "<script>alert('Stock Added');window.location='/AddStock'</script>"
    else:
        return '''<script>alert("You are logout..");window.location='/'</script>'''

@app.route('/ChangePassword')
def ChangePassword():
    if session['lid']!='':
        return render_template('Vendor/ChangePassword.html')
    else:
        return '''<script>alert("You are logout..");window.location='/'</script>'''

@app.route('/ChangePassword_post',methods=['post'])
def ChangePassword_post():
    if session['lid']!='':
        db=Db()
        currentpassword=request.form['textfield']
        newpassword=request.form['textfield1']
        confirmpassword=request.form['textfield2']
        qry = "SELECT * FROM `login` WHERE `password`='" + currentpassword + "' AND `lid`='" + str(session['lid']) + "'"
        res=db.selectOne(qry)
        if res is not None:
            if newpassword==confirmpassword:
                qry1 = "UPDATE `login` SET `password`='"+confirmpassword+"' WHERE `lid`='"+str(session['lid'])+"'"
                res1=db.update(qry1)
                return "<script>alert('Password Changed Successfully, Login Again');window.location='/'</script>"
            else:
                return "<script>alert('Passwords does not match');window.location='/ChangePassword'</script>"
        else:
            return "<script>alert('Enter valid password');window.location='/ChangePassword'</script>"
    else:
        return '''<script>alert("You are logout..");window.location='/'</script>'''


@app.route('/EditProduct/<id>')
def EditProduct(id):
    if session['lid']!='':
        db=Db()
        qry="SELECT * FROM `product` WHERE `p_id`='"+id+"' "
        res=db.selectOne(qry)
        qry1="SELECT * FROM `category`"
        res1=db.select(qry1)
        return render_template('Vendor/EditProduct.html', data=res,data1=res1)
    else:
        return '''<script>alert("You are logout..");window.location='/'</script>'''

@app.route('/EditProduct_post',methods=['post'])
def EditProduct_post():
    if session['lid']!='':
        productname=request.form['textfield']
        id = request.form['id']
        categoryname=request.form['select']
        price=request.form['textfield2']
        db=Db()
        qry="UPDATE `product` SET p_name='"+productname+"',c_id='"+categoryname+"',p_price='"+price+"'  WHERE p_id='"+id+"'"
        res=db.update(qry)
        return "<script>alert('Product Updated');window.location='/ViewProduct'</script>"
    else:
        return '''<script>alert("You are logout..");window.location='/'</script>'''

@app.route('/delete_product/<id>')
def delete_product(id):
    if session['lid']!='':
        db=Db()
        qry="DELETE FROM `product`WHERE `p_id`='"+id+"'"
        res=db.delete(qry)
        return redirect('/ViewProduct')
    else:
        return '''<script>alert("You are logout..");window.location='/'</script>'''

@app.route('/EditProfile')
def EditProfile():
    if session['lid']!='':
        db=Db()
        qry="SELECT * FROM `vendors` WHERE `v_lid`='"+str(session['lid'])+"'"
        res=db.selectOne(qry)
        return render_template('Vendor/EditProfile.html',data=res)
    else:
        return '''<script>alert("You are logout..");window.location='/'</script>'''

@app.route('/EditProfile_post',methods=['post'])
def EditProfile_post():
    if session['lid']!='':
        db=Db()
        name=request.form['textfield']
        place=request.form['textfield1']
        district=request.form['textfield2']
        state=request.form['textfield3']
        post=request.form['textfield4']
        pin=request.form['textfield5']
        ownername = request.form['textfield6']
        email=request.form['textfield7']
        phone=request.form['textfield8']
        qry="UPDATE `vendors` SET `v_name`='"+name+"',`v_place`='"+place+"',`v_post`='"+post+"',`v_pin`='"+pin+"',`v_district`='"+district+"',`v_state`='"+state+"',`v_ownername`='"+ownername+"',`v_email`='"+email+"',`v_phone`='"+phone+"' WHERE `v_lid`='"+str(session['lid'])+"'"
        res=db.update(qry)
        return "<script>alert('Updated Succesfully');window.location='/ViewEditProfile'</script>"
    else:
        return '''<script>alert("You are logout..");window.location='/'</script>'''


@app.route('/EditStock/<id>')
def EditStock(id):
    if session['lid']!='':
        db = Db()
        qry = "SELECT * FROM `product`  "
        res = db.select(qry)
        qry1 = "SELECT * FROM `stock`WHERE `s_id`='" + id + "'"
        res1 = db.selectOne(qry1)
        return render_template('Vendor/EditStock.html',data=res,data1=res1)
    else:
        return '''<script>alert("You are logout..");window.location='/'</script>'''

@app.route('/EditStock_post',methods=['post'])
def EditStock_post():
    if session['lid']!='':
        productname=request.form['select']
        quantity=request.form['textfield']
        id=request.form['id']
        db=Db()
        qry="UPDATE `stock`SET `p_id`='"+productname+"',`quantity`='"+quantity+"' WHERE `s_id`='"+id+"'"
        res=db.update(qry)
        return "<script>alert('Updated Succesfully');window.location='/ViewStock'</script>"
    else:
        return '''<script>alert("You are logout..");window.location='/'</script>'''

@app.route('/delete_stock/<id>')
def delete_stock(id):
    if session['lid']!='':
        db=Db()
        qry="DELETE FROM `stock`WHERE `s_id`='"+id+"'"
        res=db.delete(qry)
        return redirect('/ViewStock')
    else:
        return '''<script>alert("You are logout..");window.location='/'</script>'''

@app.route('/PurchaseHistory')
def PurchaseHistory():
    if session['lid']!='':
        db = Db()
        qry = "SELECT * FROM `order_main`"
        res = db.select(qry)
        return render_template('Vendor/PurchaseHistory.html',data=res)
    else:
        return '''<script>alert("You are logout..");window.location='/'</script>'''


@app.route('/PurchaseHistoryMoreDetails/<om_id>')
def PurchaseHistoryMoreDetails(om_id):
    if session['lid']!='':
        db = Db()
        qry = "SELECT * FROM `order_sub` JOIN `order_main` ON `order_main`.`om_id`=`order_sub`.`om_id` INNER JOIN `product`ON `product`.`p_id`=`order_sub`.`p_id` WHERE order_sub.`om_id`='"+om_id+"'"
        res = db.select(qry)
        return render_template('Vendor/PurhaseHistoryMoreDetails.html',data=res)
    else:
        return '''<script>alert("You are logout..");window.location='/'</script>'''

@app.route('/Signup')
def Signup():
    return render_template('Vendor/signup_index.html')

@app.route('/Signup_post',methods=['post'])
def Signup_post():
    db=Db()
    name=request.form['textfield']
    place=request.form['textfield1']
    district=request.form['textfield2']
    state=request.form['textfield3']
    post=request.form['textfield4']
    pin=request.form['textfield5']
    ownername=request.form['textfield6']
    email=request.form['textfield7']
    phone=request.form['textfield8']
    password=request.form['textfield9']
    confirmpassword=request.form['textfield0']
    qry="INSERT INTO `login`(`username`,`password`,`type`) VALUES ('"+email+"','"+confirmpassword+"','vendor')"
    res=db.insert(qry)
    qry1="INSERT INTO `vendors`(`v_lid`,`v_name`,`v_place`,`v_post`,`v_pin`,`v_district`,`v_state`,`v_ownername`,`v_email`,`v_phone`,`status`) VALUES ('"+str(res)+"','"+name+"','"+place+"','"+post+"','"+pin+"','"+district+"','"+state+"','"+ownername+"','"+email+"','"+phone+"','pending')"
    res1=db.insert(qry1)
    return "<script>alert('Registration Succesfull');window.location='/'</script>"



@app.route('/ViewCategory')
def ViewCategory():
    if session['lid']!='':
        db=Db()
        qry="SELECT * FROM `category`"
        res=db.select(qry)
        return render_template('Vendor/ViewCategory.html', data=res)
    else:
        return '''<script>alert("You are logout..");window.location='/'</script>'''


@app.route('/ViewEditProfile')
def ViewEditProfile():
    if session['lid']!='':
        db=Db()
        qry="SELECT * FROM `vendors` WHERE `v_lid`='"+str(session['lid'])+"'"
        res=db.selectOne(qry)
        return render_template('Vendor/ViewEditProfile.html',data=res)
    else:
        return '''<script>alert("You are logout..");window.location='/'</script>'''

@app.route('/ViewProduct')
def ViewProduct():
    if session['lid']!='':
        db=Db()
        qry="SELECT * FROM `product` JOIN `category` ON `category`.`c_id` = `product`.`c_id` WHERE `v_lid`='"+str(session['lid'])+"' "
        res=db.select(qry)
        return render_template('Vendor/ViewProduct.html', data=res)
    else:
        return '''<script>alert("You are logout..");window.location='/'</script>'''

@app.route('/ViewStock')
def ViewStock():
    if session['lid']!='':
        db=Db()
        qry="SELECT * FROM `stock`JOIN`product` ON `product`.`p_id`=`stock`.`p_id`"
        res=db.select(qry)
        return render_template('Vendor/ViewStock.html',data=res)
    else:
        return '''<script>alert("You are logout..");window.location='/'</script>'''


@app.route('/generate_bill')
def generate_bill():
    session['tot']=0
    db=Db()
    qry="SELECT * FROM `users`"
    res=db.select(qry)
    qry2="SELECT * FROM `category` "
    res2=db.select(qry2)
    qry3="SELECT * FROM `product` JOIN `category` ON `category`.`c_id`=`product`.`c_id`"
    res3=db.select(qry3)
    qry5="INSERT INTO `order_main`(`v_lid`,`date`,`time`) VALUES('"+str(session['lid'])+"',CURDATE(),CURTIME())"
    db=Db()
    mainid=db.insert(qry5)
    session['omid']=mainid
    qry4 = "SELECT * FROM `order_main` JOIN `order_sub` ON `order_main`.`om_id`=`order_sub`.`om_id` JOIN `product`ON `order_sub`.`p_id`=`product`.`p_id` where order_main.om_id='" + str(session['omid']) + "'"
    res4 = db.select(qry4)

    return render_template('Vendor/generate_bill.html', data=res, data2=res2,data3=res3, data4=res4)




@app.route('/generate_bill1')
def generate_bill1():
    db=Db()
    qry="SELECT * FROM `users`"
    res=db.select(qry)
    qry2="SELECT * FROM `category` "
    res2=db.select(qry2)
    qry3="SELECT * FROM `product` JOIN `category` ON `category`.`c_id`=`product`.`c_id`"
    res3=db.select(qry3)

    qry4 = "SELECT * FROM `order_main` JOIN `order_sub` ON `order_main`.`om_id`=`order_sub`.`om_id` JOIN `product`ON `order_sub`.`p_id`=`product`.`p_id` where order_main.om_id='" + str(session['omid']) + "'"
    res4 = db.select(qry4)

    return render_template('Vendor/generate_bill.html', data=res, data2=res2,data3=res3, data4=res4)






@app.route('/generate_bill_post', methods=['POST'])
def generate_bill_post():
    db = Db()
    qry = "SELECT * FROM `users`"
    res = db.select(qry)
    qry2 = "SELECT * FROM `category` "
    res2 = db.select(qry2)
    qry3 = "SELECT * FROM `product` JOIN `category` ON `category`.`c_id`=`product`.`c_id`"
    res3 = db.select(qry3)
    qry4 = "SELECT * FROM `order_main` JOIN `order_sub` ON `order_main`.`om_id`=`order_sub`.`om_id` JOIN `product`ON `order_sub`.`p_id`=`product`.`p_id` where order_main.om_id='"+str(session['omid'])+"'"
    res4 = db.select(qry4)


    db=Db()
    product=request.form['select3']
    quantity=request.form['textfield']
    # user=request.form['select']
    #
    #
    # qry5="UPDATE `order_main` SET `u_lid`='"+user+"' WHERE `om_id`='"+str(session['omid'])+"'"
    # db=Db()
    # db.update(qry5)

    qrya="INSERT INTO `order_sub`(`om_id`,`p_id`,`quantity`)VALUES('"+str(session['omid'])+"','"+product+"','"+quantity+"')"
    resa=db.insert(qrya)
    qryb="SELECT * FROM `product` WHERE `p_id`='"+product+"'"
    db=Db()
    prod=db.selectOne(qryb)
    tot=0
    tot=prod['p_price'] * int(quantity)

    print(session['tot'],tot)

    session['tot']=int(str(session['tot']))+ tot
    qryc="UPDATE `order_main` SET `total_amount` ='"+str(session['tot'])+"' WHERE `om_id`='"+str(session['omid'])+"'"
    db=Db()
    db.update(qryc)
    return generate_bill1()



@app.route('/update_order_main', methods=['POST'])
def update_order_main():
    user=request.form['select']
    qry="UPDATE `order_main` SET `u_lid`='"+user+"' WHERE `om_id`='"+str(session['omid'])+"'"
    db=Db()
    db.update(qry)
    gen_qrcode( str(session['omid']))

    from mkl import likencrypt, likdecrypt

    likencrypt("C:\\Users\\arsha\\PycharmProjects\\Sqrp\\static\\qr\\","a.jpg","share_1\\1.png","share_2\\2.png")
    likdecrypt("C:\\Users\\arsha\\PycharmProjects\\Sqrp\\static\\qr\\share_1\\1.png","C:\\Users\\arsha\\PycharmProjects\\Sqrp\\static\\qr\\share_2\\2.png")

    return redirect("/create_second")



@app.route("/create_second")
def create_second():
    gen_qrcode_2("2.png")

    return render_template("Vendor/img1.html",x=1)


@app.route("/createthird")
def createthird():
    return render_template("Vendor/img2.html")




@app.route('/scan_qr', methods=['POST'])
def qr():

    p="C:\\Users\\arsha\\PycharmProjects\\Sqrp\\static\\qr\\share_2\\"
    ps="C:\\Users\\arsha\\PycharmProjects\\Sqrp\\static\\qr\\share_1\\"
    share2=request.form['name']
    p2=p+share2



    share1="1.png"
    p1=ps+share1

    s=likdecrypt(p1,p2)





    return jsonify(status="ok")


@app.route('/payment', methods=['POST'])
def payment():

    accno= request.form["accno"]
    billno= request.form["billno"]
    cvv= request.form["cvv"]
    amount= request.form["amount"]


    qry="SELECT * FROM `bank` WHERE `accountno`='"+accno+"' AND cvv='"+cvv+"' AND balance>="+ amount

    db=Db()
    res=db.selectOne(qry)
    if res is None:
        return jsonify(status='no')
    else:

        qry="update bank set balance=balance-"+amount +" where accountno='"+accno+"'"
        db.update(qry)

        qry="UPDATE `order_main` SET STATUS='Done' WHERE om_id='"+billno+"' "
        db.update(qry)
        return jsonify(status='ok')





    pass




@app.route('/delete_bill/<id>')
def delete_bill(id):
    qry="SELECT `order_sub`.`quantity` * `product`.`p_price` AS pp FROM `order_sub` JOIN `product` ON `product`.`p_id`=`order_sub`.`p_id` WHERE `os_id`='"+id+"'"
    db=Db()
    tot=db.selectOne(qry)
    db=Db()
    qry="DELETE FROM `order_sub` WHERE `os_id`='"+id+"'"
    res=db.delete(qry)
    session['tot']=session['tot']-tot['pp']
    qry="UPDATE `order_main` SET total_amount='"+str(session['tot'])+"' WHERE `om_id`='"+str(session['omid'])+"'"
    db=Db()
    db.update(qry)
    return generate_bill1()

@app.route('/jqry_add_product', methods=['get'])
def jqry_add_product():
    id=request.args.get('id')
    db=Db()
    qry="SELECT * FROM `product`WHERE `c_id`='"+id+"'  AND `v_lid`='"+str(session['lid'])+"'"
    res=db.select(qry)
    if len(res)==0:
        return jsonify(status="ok",data=res)
    else:
        return jsonify(status="no")




@app.route('/view_img1')
def view_img1():
    return render_template('Vendor/img1.html')

@app.route('/view_img1_post')
def view_img1_post():
    return

@app.route('/view_img2')
def view_img2():
    return


@app.route('/utility')
def utility():
    db=Db()
    qry="SELECT `profit`FROM `product`"
    res=db.select(qry)
    with open("C:\\Users\\arsha\\PycharmProjects\\Sqrp\\profit.txt", "w") as b:
        b.write(" ")
    with open("C:\\Users\\arsha\\PycharmProjects\\Sqrp\\profit.txt", "a") as b:
        for i in res:
            b.write(str(i['profit'])+"\n")


    t1=[]
    t2=[]

    db=Db()
    qry1="SELECT * FROM `order_main`"
    res1=db.select(qry1)
    for i in res1:
        qry2="SELECT * FROM `order_sub` JOIN `order_main` ON `order_main`.`om_id`=`order_sub`.`om_id` INNER JOIN `product`ON `product`.`p_id`=`order_sub`.`p_id` WHERE order_sub.`om_id`='"+str(i["om_id"])+"'"
        res2=db.select(qry2)
        myt1=[]
        myq1=[]
        myp=[]
        tt=0
        for j in res2:
            myt1.append(j["p_id"])
            myq1.append(j["quantity"])
            myp.append(j["p_name"])

            profit=float(j["profit"])
            qty=int(j["quantity"])
            tt+=(profit*qty)

        t1.append({"t1":i["om_id"],"trans":myt1,"myq1":myq1,"pname":myp})
        t2.append({"t1":i["om_id"],"trans":myt1,"tu":tt})
    # item utility
    qry3="SELECT * FROM `product` order by p_id asc"
    res3=db.select(qry3)
    t3=[]
    print(res3)
    for k in res3:
        qry4="SELECT SUM(`quantity`) AS s FROM `order_sub` WHERE `p_id`='"+str(k["p_id"])+"'"
        res4=db.selectOne(qry4)

        if res4['s'] is not None:
            qq=int(res4["s"])*float(k["profit"])
            t3.append({"pid":k["p_id"],"pname":k["p_name"],"tq":qq})
        else:
            qq=0
            t3.append({"pid":k["p_id"],"pname":k["p_name"],"tq":qq})

    t4=[]
    for k in res3:
        qry4="SELECT SUM(`quantity`) AS s FROM `order_sub` WHERE `p_id`='"+str(k["p_id"])+"'"
        res4=db.selectOne(qry4)

        if res4['s'] is not None:
            qq=int(res4["s"])*float(k["profit"])
            t4.append({"pid":k["p_id"],"pname":k["p_name"],"tq":qq})
        else:
            qq=0
            t4.append({"pid":k["p_id"],"pname":k["p_name"],"tq":qq})
    for n in range(len(t4) - 1, 0, -1):
        for i in range(n):
            if int(t4[i]["tq"]) < int(t4[i + 1]["tq"]):
                t4[i]["tq"], t4[i+1]["tq"] = t4[i+1]["tq"], t4[i]["tq"]
                t4[i]["pid"], t4[i + 1]["pid"] = t4[i + 1]["pid"], t4[i]["pid"]
                t4[i]["pname"], t4[i + 1]["pname"] = t4[i + 1]["pname"], t4[i]["pname"]

    plist=[]
    pname=[]
    tq=[]

    for i in t4:
        plist.append(i["pid"])
        pname.append(i["pname"])
        tq.append(i["tq"])
    t5=[]
    db = Db()
    qry1 = "SELECT * FROM `order_main`"
    res1 = db.select(qry1)
    for i in res1:
        qry2 = "SELECT * FROM `order_sub` JOIN `order_main` ON `order_main`.`om_id`=`order_sub`.`om_id` INNER JOIN `product`ON `product`.`p_id`=`order_sub`.`p_id` WHERE order_sub.`om_id`='" + str(
            i["om_id"]) + "'"
        res2 = db.select(qry2)
        myt1 = []
        myq1 = []
        myp = []
        tt = 0
        for j in res2:
            myt1.append(j["p_id"])
            myq1.append(j["quantity"])
            myp.append(j["p_name"])

            profit = float(j["profit"])
            qty = int(j["quantity"])
            tt += (profit * qty)

        t5.append({"t1": i["om_id"], "trans": myt1, "myq1": myq1, "pname": myp})
    for l in range(len(t5)):
        tuu=t5[l]["trans"]
        tpp=t5[l]["pname"]
        tqq = t5[l]["myq1"]
        for n in range(len(tuu) - 1, 0, -1):
            for i in range(n):
                index = plist.index(tuu[i])
                nowtq = tq[index]
                nowpname = pname[index]
                nowpid = plist[index]

                index2 = plist.index(tuu[i+1])
                thentq = tq[index2]
                thenpname = pname[index2]
                thenpid = plist[index2]



                if int(nowtq) < int(thentq):
                    pp=tuu[i]
                    tuu[i]=tuu[i+1]
                    tuu[i+1]=pp

                    tt=tpp[i]
                    tpp[i]=tpp[i+1]
                    tpp[i+1]=tt

                    qq=tqq[i]
                    tqq[i]=tqq[i+1]
                    tqq[i+1]=qq







            print("pass")

    print(t5)


    from UPTree import finalresult

    s=finalresult()




    return render_template('Vendor/utility.html',t1=t1,t2=t2,t3=t3,t4=t4,t5=t5,s=s)

@app.route('/utility_post', methods=['POST'])
def utility_post():
    return

#====Android=====

@app.route('/and_login', methods=['post'])
def and_login():
    db=Db()
    username=request.form['username']
    password=request.form['password']
    qry="SELECT * FROM `login` WHERE `username`='"+username+"' AND `password`='"+password+"'"
    res=db.selectOne(qry)
    print(res)
    if res is not None:
        if res['type']=="user":
            qry1="SELECT * FROM `users`WHERE `u_lid`='"+str(res['lid'])+"'"
            res1 = db.selectOne(qry1)
            return jsonify(status="ok", lid = res['lid'], type = res['type'], name = res1['u_name'], emailn = res1['u_email'])
        else:
            return jsonify(status="no")
    else:
        return jsonify(status="no")

@app.route('/and_signup',methods=['post'])
def and_signup():
    db=Db()
    name=request.form['name']
    place=request.form['place']
    district=request.form['district']
    state=request.form['state']
    post=request.form['post']
    pin=request.form['pin']
    email=request.form['email']
    phone=request.form['phone']
    password=request.form['password']
    qry="INSERT INTO `login`(`username`,`password`,`type`) VALUES ('"+email+"','"+password+"','user')"
    res=db.insert(qry)
    qry1="INSERT INTO `users`(`u_lid`,`u_name`,`u_place`,`u_post`,`u_pin`,`u_district`,`u_state`,`u_email`,`u_phone`)VALUES ('"+str(res)+"','"+name+"','"+place+"','"+post+"','"+pin+"','"+district+"','"+state+"','"+email+"','"+phone+"')"
    res1=db.insert(qry1)
    return jsonify(status="ok")


@app.route('/and_changepassword',methods=['post'])
def and_changepassword():
        db=Db()
        lid=request.form['lid']
        currentpassword=request.form['textfield']
        newpassword=request.form['textfield1']
        confirmpassword=request.form['textfield2']
        qry = "SELECT * FROM `login` WHERE `password`='" + currentpassword + "' AND `lid`='"+lid+"'"
        res=db.selectOne(qry)
        if res is not None:
            if newpassword==confirmpassword:
                qry1 = "UPDATE `login` SET `password`='"+confirmpassword+"' WHERE `lid`='"+lid+"'"
                res1=db.update(qry1)
                return jsonify(status="ok")
            else:
                return jsonify(status="no")
        else:
            return jsonify(status="no")

@app.route('/and_view_profile',methods=['post'])
def and_view_edit_profile():
        db=Db()
        lid=request.form['lid']
        qry="SELECT * FROM `users` WHERE `u_lid`='"+lid+"'"
        res=db.selectOne(qry)
        if res is not None:
            return jsonify(status="ok",data=res)
        else:
            return jsonify(status="no")
@app.route('/and_edit_profile', methods=['POST'])
def and_edit_profile():
    db=Db()
    lid = request.form['lid']
    name = request.form['name']
    place = request.form['place']
    district = request.form['district']
    state = request.form['state']
    post = request.form['post']
    pin = request.form['pin']
    email = request.form['email']
    phone = request.form['phone']
    qry="UPDATE `users` SET `u_name`='"+name+"',`u_place`='"+place+"',`u_post`='"+post+"',`u_pin`='"+pin+"',`u_district`='"+district+"',`u_state`='"+state+"',`u_email`='"+email+"',`u_phone`='"+phone+"' WHERE `u_lid`='"+lid+"'"
    res=db.update(qry)
    return jsonify(status="ok")

@app.route('/and_view_bill',methods=['post'])
def and_view_bill():
    db=Db()
    lid=request.form['lid']
    qry="SELECT * FROM `order_main` INNER JOIN `vendors` ON `order_main`.`v_lid`=`vendors`.`v_lid` WHERE `order_main`.`u_lid`='"+lid+"' AND `order_main`.`status`='Done'"
    res=db.select(qry)
    return jsonify(status="ok", data=res)

@app.route('/and_pending_bill', methods=['POST'])
def and_pending_bill():
    db=Db()
    lid=request.form['lid']
    qry="SELECT * FROM `order_main` INNER JOIN `vendors` ON `order_main`.`v_lid`=`vendors`.`v_lid` WHERE `order_main`.`u_lid`='"+lid+"' AND `order_main`.`status`='pending'"
    res=db.select(qry)
    return jsonify(status="ok", data=res)

@app.route('/and_pending_more', methods=['POST'])
def pending_more():
    db=Db()
    orderid=request.form['om_id']
    qry="SELECT * FROM `order_sub` INNER JOIN `product` ON `order_sub`.`p_id`=`product`.`p_id` WHERE `order_sub`.`om_id`='"+orderid+"'"
    res=db.select(qry)
    return jsonify(status="ok", data=res)

@app.route('/and_sendcomplaint', methods=['POST'])
def and_send_complaint():
    db=Db()
    lid=request.form['lid']
    # title=request.form['title']
    description=request.form['complaint']
    qry = "INSERT INTO `complaint`(`c_description`,`c_date`,`c_time`,`c_reply`,`v_lid`,`c_status`) VALUES('"+description+"',CURDATE(), CURTIME(), 'pending', '"+lid+"','pending')"
    # qry="INSERT INTO `complaint`(`c_title`,`c_description`,`c_date`,`c_time`,`c_reply`,`v_lid`,`c_status`,`type`)VALUES('"+title+"','"+description+"',curdate(),'curtime()','pending','"+lid+"','pending','"+lid+"')"
    res=db.insert(qry)
    return jsonify(status="ok")

@app.route('/and_view_reply', methods=['POST'])
def and_view_reply():
    lid=request.form['lid']
    db=Db()
    qry="SELECT * FROM `complaint` where v_lid='"+lid+"'"
    res=db.select(qry)
    return jsonify(status="ok" ,data=res)

@app.route('/and_send_feedback', methods=['POST'])
def and_send_feedback():
    db=Db()
    lid=request.form['lid']
    description=request.form['description']
    qry="INSERT INTO `feedback`(`f_description`,`f_date`,`f_time`,`u_lid`)VALUES('"+description+"',curdate(),curtime(),'"+lid+"')"
    res=db.insert(qry)
    return jsonify(status="ok")




@app.route('/getproduct', methods=['POST'])
def getproduct():
    cid=request.form['cid']
    qry="SELECT * FROM `product` WHERE `c_id`='"+cid+"'"
    db=Db()
    res=db.select(qry)
    return jsonify(status="ok",data=res)





if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0")