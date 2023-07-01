from flask import Flask, render_template, request

app = Flask(__name__)

import pickle
model = pickle.load(open(r"C:/Users/hp/CCP/model.pkl",'rb'))

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/login', methods =['POST'])
def login():
    a =request.form["cc"]
    b= request.form["ait"]
    d= request.form["cfm"]
    e= request.form["mb"]
    f= request.form["a"]
    g= request.form["w"]
    h= request.form["cg"]
    if(h=="m"):
        h1=0
    elif(h=="f"):
        h1=1
    i= request.form["foc"]
    if(i=="y"):
        i1=0
    elif(i=="n"):
        i1=1
    j= request.form["for"]
    if(j=="yes"):
        j1=0
    elif(j=="no"):
        j1=1
    k= request.form["nit"]
    if (k=="ca"):
        k1,k2,k3,k4=1,0,0,0
    elif (k=="p"):
        k1,k2,k3,k4=0,1,0,0
    elif (k=="ss"):
        k1,k2,k3,k4=0,0,1,0
    elif (k=="s"):
        k1,k2,k3,k4=0,0,0,1
    elif (k=="w"):
        k1,k2,k3,k4=0,0,0,0
    l= request.form["net"]
    if (l=="ad"):
        l1,l2,l3,l4=1,0,0,0
    elif (l=="he"):
        l1,l2,l3,l4=0,1,0,0
    elif (l=="ih"):
        l1,l2,l3,l4=0,0,1,0
    elif (l=="ls"):
        l1,l2,l3,l4=0,0,0,1
    elif (l=="sss"):
        l1,l2,l3,l4=0,0,0,0
    m= request.form["nfs"]
    if (m=="cm"):
        m1,m2,m3,m4=1,0,0,0
    elif (m=="m"):
        m1,m2,m3,m4=0,1,0,0
    elif (m=="se"):
        m1,m2,m3,m4=0,0,1,0
    elif (m=="snm"):
        m1,m2,m3,m4=0,0,0,1
    elif (m=="wi"):
        m1,m2,m3,m4=0,0,0,0
    n=  request.form["nht"]
    if (n=="coa"):
        n1,n2,n3,n4,n5=1,0,0,0,0
    elif (n=="ha"):
        n1,n2,n3,n4,n5=0,1,0,0,0
    elif (n=="ma"):
        n1,n2,n3,n4,n5=0,0,1,0,0
    elif (n=="oa"):
        n1,n2,n3,n4,n5=0,0,0,1,0
    elif (n=="ra"):
        n1,n2,n3,n4,n5=0,0,0,0,1
    elif (n=="wp"):
        n1,n2,n3,n4,n5=0,0,0,0,0
     
    t=[[float(a),float(b),float(d),float(e),float(f),float(g),int(h1),int(i1),
        int(j1),int(k1),int(k2),int(k3),int(k4),int(l1),int(l2),
        int(l3),int(l4),int(m1),int(m2),int(m3),int(m4),int(n1),int(n2),
        int(n3),int(n4),int(n5)]]
    output= model.predict(t)
    print(t)
    print(output)  
    if output == 0:
        y="Not Eligible"
    else:
        y= "Eligible"
       
    return render_template("result.html",y = y)


if __name__ == '__main__' :
    app.run(debug=False)
    
