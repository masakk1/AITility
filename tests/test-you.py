from gpt4free import you

chat = []

# simple request with links and details
print("\nGetting Answer...\n")
response = you.Completion.create(
    prompt="Who are you",
    detailed=True,
    include_links=False,
)
print(response.text)

# {
#     "response": "...",
#     "links": [...],
#     "extra": {...},
#         "slots": {...}
#     }
# }
