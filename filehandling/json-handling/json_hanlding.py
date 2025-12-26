import json
file_name = "filehandling/json-handling/fleet_data2.json"

student = {
    "airport": [
        {
            "type": "ElectricScooter",
            "vehicle_id": 123,
            "model": "ather",
            "battery": 9,
            "extra": 100
        },
        {
            "type": "ElectricScooter",
            "vehicle_id": 124,
            "model": "ola",
            "battery": 8,
            "extra": 100
        },
        {
            "type": "ElectricCar",
            "vehicle_id": 125,
            "model": "bmw",
            "battery": 90,
            "extra": 4
        }
    ]
}
# with open(file_name,"r") as file:
#    y= json.load(file)
#    print(y)
with open(file_name,"w") as file:
   y= json.dump(student,file,indent=4)
   print(y)