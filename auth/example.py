import auth

res = auth.PasswordWindow(title='A', msg='B', first_prompt=False).ask()
if res != None:
    print(res)