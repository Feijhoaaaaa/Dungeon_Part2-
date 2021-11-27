Dict = {"Herson":100, "Kiev":150, "Dnepr":75, "London":200}
Dict.pop("Dnepr")
Dict.pop("London")
for i,z in Dict.items():
    print(f"Key:{i}")
    print(f"Value:{z}")