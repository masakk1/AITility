from gpt4free import forefront

# create an account
print("Getting token...........")
token = forefront.Account.create(logging=False)
print("Token:", token)

# get a response
print("Getting response...........")
output = ""
for response in forefront.StreamingCompletion.create(
    token=token, prompt="hello world", model="gpt-4"
):
    output = response.choices[0].text
    print(output, end="", flush=True)
print("")
