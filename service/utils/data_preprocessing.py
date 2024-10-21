import pandas as pd


def get_hourly_gender_counts(data, working_hours):
    # data["detection_time"] = pd.to_datetime(data["detection_time"])
    # data["hourly"] = data["detection_time"].dt.hour
    data.loc[:, "detection_time"] = pd.to_datetime(data["detection_time"])
    data.loc[:, "hourly"] = data["detection_time"].dt.hour

    male_data = data[(data["gender"] == "male") & (data["event_type"] == "enter")]
    female_data = data[(data["gender"] == "female") & (data["event_type"] == "enter")]

    female_couts = female_data['hourly'].value_counts()
    male_couts = male_data['hourly'].value_counts()

    

    male_dict = male_couts.to_dict()
    female_dict = female_couts.to_dict()

    hourly_dict_female = {f"{hour:02d}:00": 0 for hour in range(working_hours[0],working_hours[1])}
    hourly_dict_male = {f"{hour:02d}:00": 0 for hour in range(working_hours[0],working_hours[1])}

  
    hourly_list = [f"{hour:02d}:00" for hour in range(working_hours[0],working_hours[1])]

    for i in male_dict:
        hourly_dict_male[f"{i:02d}:00"] = male_dict[i]
    for i in female_dict:
        hourly_dict_female[f"{i:02d}:00"] = female_dict[i]

    males = list()
    for i in hourly_list:
        males.append({"time_label": i, "count": hourly_dict_male[i]})
    females = list()
    for i in hourly_list:
        females.append({"time_label": i, "count": hourly_dict_female[i]})


    return {
        "male": males,
        "female": females
    }

def get_hourly_customer_counts(data, working_hours):

    data.loc[:, "detection_time"] = pd.to_datetime(data["detection_time"])
    data.loc[:, "hourly"] = data["detection_time"].dt.hour
   

    enter_data = data[data["event_type"] == "enter"]

    enter_counts = enter_data['hourly'].value_counts()

    enter_dict = enter_counts.to_dict()

    hourly_dict = {f"{hour:02d}:00": 0 for hour in range(working_hours[0],working_hours[1])}



    for i in enter_dict:
        hourly_dict[f"{i:02d}:00"] = enter_dict[i]
   

    hourly_list = [f"{hour:02d}:00" for hour in range(working_hours[0],working_hours[1])]


    hourly_customer = list()
    for i in hourly_list:
        hourly_customer.append({"time_label": i, "count": hourly_dict[i]})

    return hourly_customer


def get_current_gender_data(data):
    male_data = data[data["gender"] == "male"]
    male_couts = male_data['event_type'].value_counts()


    female_data = data[data["gender"] == "female"]
    female_couts = female_data['event_type'].value_counts()

    current_male = male_couts.get('enter', 0) 
    current_female = female_couts.get('enter', 0) 

    return {
        "current_male": int(current_male) ,
        "current_female": int(current_female),
    }


def get_current_customer_data(data):
    value_counts = data['event_type'].value_counts()
    current_customer = value_counts.get('enter', 0)

    return  int(current_customer)

