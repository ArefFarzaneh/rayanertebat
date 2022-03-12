import streamlit as st
import sqlite3
import pandas as pd
import datetime as dt
import requests
import time
import datetime as dt
smslist=[]
conn = sqlite3.connect('Rayan.db')
c = conn.cursor()

def create_saves():

    c.execute('CREATE TABLE IF NOT EXISTS saves(mtntopup TEXT,mtnpin TEXT, mcitopup TEXT,mcipin TEXT,rtltopup TEXT,rtlpin TEXT,telepin2 TEXT,baste TEXT)')
    conn.commit()

def add_saves(mtntopup,mtnpin,mcitopup,mcipin,rtltopup,rtlpin,telepin2,baste):
	c.execute('INSERT INTO saves(mtntopup,mtnpin,mcitopup,mcipin,rtltopup,rtlpin,telepin2,baste) VALUES (?,?,?,?,?,?,?,?)',(mtntopup,mtnpin,mcitopup,mcipin,rtltopup,rtlpin,telepin2,baste))
	conn.commit()


def read_saves():
    c.execute('SELECT * FROM saves')
    data = c.fetchone()
    return data

def update_saves(mtntopup,mtnpin,mcitopup,mcipin,rtltopup,rtlpin,telepin2,baste):
    c.execute('UPDATE saves SET mtntopup=?,mtnpin=?,mcitopup=?,mcipin=?,rtltopup=?,rtlpin=? ,telepin2=?,baste=?',(mtntopup,mtnpin,mcitopup,mcipin,rtltopup,rtlpin,telepin2,baste))
    conn.commit()

def esaj_topup_add():
    c.execute('UPDATE esaj_topup SET date=?,charged=? ',(str(dt.datetime.now().day),"yes"))
    conn.commit()

def esaj_topup_add_fake():
    c.execute('INSERT INTO esaj_topup (date,charged) VALUES(?,?) ',(str(dt.datetime.now().day-1),"yes"))
    conn.commit()

def esaj_pin_add():
    c.execute('UPDATE esaj_pin SET date=?,charged=? ',(str(dt.datetime.now().day),"yes"))
    conn.commit()

def esaj_pin_add_fake():
    c.execute('INSERT INTO esaj_pin (date,charged) VALUES(?,?) ',(str(dt.datetime.now().day-1),"yes"))
    conn.commit()

def esaj_topup_read():
    c.execute('SELECT * FROM esaj_topup')
    data = c.fetchone()
    return data


def esaj_pin_read():
    c.execute('SELECT * FROM esaj_pin')
    data = c.fetchone()
    return data


def create_todo():
    c.execute('CREATE TABLE IF NOT EXISTS todo (id INTEGER PRIMARY KEY ,day TEXT,month TEXT,to_do VARCHAR(500))')
    conn.commit()

def add_todo(todo):
    c.execute('INSERT INTO todo (day,month,to_do) VALUES (?,?,?)',(str(dt.datetime.now().day),str(dt.datetime.now().month),str(todo)))
    conn.commit()

def read_todo():
    c.execute('SELECT * FROM todo')
    data = c.fetchall()
    return data


def clear_todo():
    c.execute('DELETE FROM todo')
    conn.commit()

def delete_todo(conn,id):
    sql='DELETE FROM todo WHERE id=?'
    cur = conn.cursor()
    cur.execute(sql, (id,))
    conn.commit()



def main():
    st.set_page_config(
        page_title="Rayan Ertebat",
        layout="wide",
        initial_sidebar_state="auto",
    )
   
    menu = ["Enter Saves","View Saves","Esaj","To Do"]
    choice = st.sidebar.selectbox("Menu",menu)


    create_saves()

    if choice=="Enter Saves":
        st.header ("Enter Saves")
        col33,col44=st.columns(2)
        col33.header("")
        col33.header("")
        col33.header("")
        col33.header('Rayan Ertebat - Business Operation Team')
        col44.image("https://media.mehrnews.com/d/2021/07/06/3/3822605.jpg",width=400)

        col1,col2,col3,col4,col5,col6,col7,col8,col9,col10=st.columns(10)
        
        col1.header("MTN")
        col1.subheader("Top up:")
        col1.markdown("")
        col1.markdown("")
        col1.subheader("Pins:")
        col2.header("")
        mtntopup = col2.text_input('',key=1)
        mtnpin = col2.text_input('',key=2)


        col3.header("MCI")
        col3.subheader("Top up:")
        col3.markdown("")
        col3.markdown("")
        col3.subheader("Pins:")
        col4.header("")
        mcitopup = col4.text_input('',key=3)
        mcipin = col4.text_input('',key=4)

        col5.header("RTL")
        col5.subheader("Top up:")
        col5.markdown("")
        col5.markdown("")
        col5.subheader("Pins:")
        col6.header("")
        rtltopup = col6.text_input('',key=5)
        rtlpin = col6.text_input('',key=6)

        col7.header("JIRING")
        col7.subheader("telepin 2:")
        col7.markdown("")
        col7.markdown("")
        col7.subheader("baste:")
        col8.header("")
        telepin2 = col8.text_input('',key=7)
        baste = col8.text_input('',key=8)
        



        if st.button('save'):
            try:
                # add_saves(mtntopup,mtnpin,mcitopup,mcipin,rtltopup,rtlpin,telepin2,baste)
                info=read_saves()
                if info:
                    clean_info=pd.DataFrame([info],columns=["Mtn Topup","Mtn Pin","Mci Topup","Mci Pin","Rtl Topup","Rtl Pin","Telepin 2","Baste"])
                    update_saves(mtntopup,mtnpin,mcitopup,mcipin,rtltopup,rtlpin,telepin2,baste)
                    if mtntopup:
                        tempmtntopup=str(mtntopup)
                    else:
                        tempmtntopup=int(clean_info["Mtn Topup"])
                    if mtnpin:
                        tempmtnpin=str(mtnpin)
                    else:
                        tempmtnpin=int(clean_info["Mtn Pin"])               
                    if mcitopup:
                        tempmcitopup=str(mcitopup)
                    else:
                        tempmcitopup=int(clean_info["Mci Topup"])
                    if mcipin:
                        tempmcipin=str(mcipin)
                    else:
                        tempmcipin=int(clean_info["Mci Pin"])
                    if rtltopup:
                        temprtltopup=str(rtltopup)
                    else:
                        temprtltopup=int(clean_info["Rtl Topup"])
                    if rtlpin:
                        temprtlpin=str(rtlpin)
                    else:
                        temprtlpin=int(clean_info["Rtl Pin"])
                    if telepin2:
                        temptelepin2=str(telepin2)
                    else:
                        temptelepin2=int(clean_info["Telepin 2"])
                    if baste:
                        tempbaste=str(baste)
                    else:
                        tempbaste=int(clean_info["Baste"])
                    update_saves(tempmtntopup,tempmtnpin,tempmcitopup,tempmcipin,temprtltopup,temprtlpin,temptelepin2,tempbaste)

                    a=st.success('Saved')
                    if a:
                        time.sleep(2)
                        a.empty()

                else:
                    add_saves(mtntopup,mtnpin,mcitopup,mcipin,rtltopup,rtlpin,telepin2,baste)
                    a=st.success('Saved')
                    if a:
                        time.sleep(2)
                        a.empty()
                
            except ValueError as e:
                st.error(e)

        
        



    if choice=="View Saves":
        try:
            st.header("View Saves")
            inf = read_saves()
            clean_inf=pd.DataFrame([inf],columns=["Mtn Topup","Mtn Pin","Mci Topup","Mci Pin","Rtl Topup","Rtl Pin","Telepin 2","Baste"])
            st.dataframe(clean_inf)
            columns=["Mtn Topup","Mtn Pin","Mci Topup","Mci Pin","Rtl Topup","Rtl Pin","Telepin 2","Baste"]

            for item in columns:
                if int(clean_inf[item])>12:
                    st.success(item.upper())
                elif 10<=int(clean_inf[item])<=12:
                    st.warning(item.upper())
                elif int(clean_inf[item])<=10:
                    st.error(item.upper())
        except ValueError:
            st.error("اطلاعاتی در دیتابیس موجود نیست. لطفا ابتدا مقادیر سیو را وارد کنید")
        # for item in columns:
        #     if int(clean_inf[item]) - hour <1 :
        #         a = item.split(" ")
        #         if len(a)>1:
        #             a = a[0]+a[1]
        #             smslist.append(a)
        #         else:
        #             a=a[0]
        #             smslist.append(a)
            
            # if dt.datetime.now().minute <55 and dt.datetime.now().minute>50 and  len(smslist)>0:
            #     sms=str((','.join(map(str, smslist))))
            #     url = "https://api.ghasedak.me/v2/verification/send/simple"
            #     payload = "receptor=09128936096&template=LowerThanOneHour&type=1&param1=%s"%(sms)

            #     headers = {
            #     'content-type': "application/x-www-form-urlencoded",
            #     'apikey': "26c764e4ae320ae4ddfae1be57bdb6976e52efc80c84a69be19c6170d2ff2b01",
            #     'cache-control': "no-cache",
            #     }

            #     req = requests.request("POST", url, data=payload, headers=headers)
            #     print(req)
            #     print(sms)
            #     time.sleep(1800)
            

      

    if choice=="Esaj":

        st.header("Esaj")
        col1,col2,col3,col4,col5=st.columns(5)
        c.execute('CREATE TABLE IF NOT EXISTS esaj_topup (date TEXT,charged TEXT)')
        conn.commit()

        c.execute('CREATE TABLE IF NOT EXISTS esaj_pin (date TEXT,charged TEXT)')
        conn.commit()

        
        esaj_topup_inf = esaj_topup_read()
        if esaj_topup_inf:
            clean_inf_esaj_topup =pd.DataFrame([esaj_topup_inf],columns=["date","charged"])
        else:
            esaj_topup_add_fake()
            esaj_topup_inf = esaj_topup_read()
            clean_inf_esaj_topup =pd.DataFrame([esaj_topup_inf],columns=["date","charged"])

        

        esaj_pin_inf = esaj_pin_read()
        if esaj_pin_inf:
            clean_inf_esaj_pin =pd.DataFrame([esaj_pin_inf],columns=["date","charged"])
        else:
            esaj_pin_add_fake()
            esaj_pin_inf = esaj_pin_read()
            clean_inf_esaj_pin =pd.DataFrame([esaj_pin_inf],columns=["date","charged"]) 




        if clean_inf_esaj_topup["date"][0] == str(dt.datetime.now().day):
            col1.subheader("Top up has been done today :)")
        else:    
            t=col1.checkbox("topup",key="easj_topup")
            if t:
                esaj_topup_add()


        if clean_inf_esaj_pin["date"][0] == str(dt.datetime.now().day):
            col3.subheader("Pin has been done today :)")
        else:    
            p = col2.checkbox("pin",key="easj_pin")
            if p :
                esaj_pin_add()


        if clean_inf_esaj_topup["date"][0] == str(dt.datetime.now().day) and  clean_inf_esaj_pin["date"][0] == str(dt.datetime.now().day):
            st.balloons()




        


    if choice=="To Do":


        st.header("To Do")
        st.subheader("Enter To Do's below and press Submit:")
        c1,c2,c3,c4,c5,c6,c7,c8,c9=st.columns(9)
        col1,col2=st.columns(2)

        c7.header("")
        c7.header("")
        c7.header("")
        clear = c8.button("Press to clear data")
        if clear:
            clear_todo()
            s = col1.success("Cleared Successfully")
            time.sleep(2)
            s.empty()

        create_todo()
        
        with col1.form(key='todo',clear_on_submit=True):
            todo = st.text_input("To Do :")
            submit_button = st.form_submit_button("Submit")
        if submit_button:
            a=str(todo)
            add_todo(a)
            t=c9.success("successfully added")
            time.sleep(1)
            t.empty()




        col2.header("")
        show = col2.button("Click to show Today's To Do's:")
        if show:
            data = read_todo()
            if len(data)>0:
                todo_list=[]
                for i in range(len(data)):
                    item=data[i]
                    if item[1]==str(dt.datetime.now().day) and item[2]==str(dt.datetime.now().month) :
                        col2.button(f'{str(item[0])} - {str(item[3])}',key=item[2])
                        todo_list.append(item[3])



            else: col1.warning("There is no To Do yet!")

        col1.header("")    
        with col1.form(key='done',clear_on_submit=True):
            done = st.text_input("Enter number if done and submit.")
            submit_button = st.form_submit_button("Submit")
           
        if submit_button :
            
            if done.isdigit():
                delete_todo(conn,done)
                y=c9.success(f'The task number {done} deleted successfully')
                time.sleep(1)
                y.empty()


            else:
                x=c9.error("Please Enter the number of task")
                time.sleep(1)
                x.empty()






if __name__ == "__main__":
    main()
