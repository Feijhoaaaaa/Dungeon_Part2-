UsersAge = {"User0":12,"User1":24,"User2":78, "User3":30, "User4":18}
YoungerUsers = {k: v for k, v in UsersAge.items() if v < 18}
OlderUsers = {k: v for k, v in UsersAge.items() if v > 18}
print(f"YoungerUsers:{YoungerUsers}")
print(f"YoungerUsers:{OlderUsers}")
