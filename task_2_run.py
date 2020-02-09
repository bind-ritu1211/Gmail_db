from login_gmail import main
from flask import request, Flask
from datetime import datetime, timedelta

app = Flask(__name__)
CORS(app) 


@app.route('/task_2/', methods=['POST'])
def filter_mail():
    '''according to the 2nd assignment , data need a keys,
     its values and days , conditions on days,
     in 2nd part on the assignment : fucntion checking the action,
     if it is moveto then it need location where you want to paste.
     then it is checking the all the condition individually'''
    params = request.json
    mail_data = main()
    key = params.get("key") #key of first selection
    value1 = params.get("value1") #value of first selction
    key2 = params.get("key2")
    value2 = params.get("value2")
    days = params.get("days")
    condition_days= params.get("condition_days") #taking conditon 
    action = params.get("action")
    if action == "moveto":
        location = params.get("location")
    days_caluculation =  mail_data["received_datetime"] - timedelta(days=days)
    if condition_days == "equalto": #converting to logical expresion
        if value1 in mail_data[key] && value2 in mail_data[key2] && days == days_caluculation: #checking
            if not location:
                mail_data[action] #if not move to then take action such as markread and unread
            else:
                print("mmove to given location")
    elif condition_days == "greaterthen":
        if value1 in mail_data[key] && value2 in mail_data[key2] && days > days_caluculation:
            if not location:
                mail_data[action] #if not move to then take action such as markread and unread
            else:
                print("mmove to given location")
    elif condition_days == "lessthen":
        if value1 in mail_data[key] && value2 in mail_data[key2] && days < days_caluculation:
            if not location:
                mail_data[action] #if not move to then take action such as markread and unread
            else:
                print("mmove to given location")
    return ("check console")


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port="8000")
