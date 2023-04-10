def pre_proc(data1):
    pid=[]
    transitemids=[]
    transitemqty = []

    profit=[]
    from  DBConnection import Db
    db=Db()
    qry1="SELECT `p_id`,`profit` FROM `product`"
    res1=db.select(qry1)
    for i in res1:
        pid.append(i['p_id'])
        profit.append(i['profit'])


    omid=[]
    from DBConnection import Db
    db=Db()
    qry2="SELECT `om_id` FROM `order_main`"
    res2=db.select(qry2)
    for j in res2:
        omid.append(j['om_id'])
        tpid=[]
        tqty=[]
        qry3="SELECT `p_id`,`quantity` FROM `order_sub`WHERE `om_id`='"+str(j['om_id'])+"'"
        res3=db.select(qry3)
        for k in res3:
            tpid.append(k['p_id'])
            tqty.append(k['quantity'])

        transitemids.append(tpid)
        transitemqty.append(tqty)

    return pid, transitemids , transitemqty


s= pre_proc("")
print(s)



with open("trans.txt","a") as b:

    for i in range(0,len(s[1])):
        print(s[1][i])

        k=""

        for m in s[1][i]:
            k= k+str(m)+" "
        k=k[:len(k)-1]+":"
        for m in s[2][i]:
            k=k+str(m)+" "
        k=k[:len(k)-1]

        b.write(k+"\n")






