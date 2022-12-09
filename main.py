import pyrogram

# Replace these with your own Telegram API keys
api_id = 'YOUR_API_ID'
api_hash = 'YOUR_API_HASH'

# Authenticate with Telegram
client = pyrogram.Client(
    'my_account',
    api_id=api_id,
    api_hash=api_hash
)

# The ID of the group you want to take screenshots of
group_id = 'YOUR_GROUP_ID'

# Take multiple screenshots of the group
for i in range(10):
    screenshot = client.screenshot_group(group_id)
    screenshot.save('screenshot_{}.png'.format(i))

# Log the user ID, username, and profile picture of the users in the group
group_info = client.get_chat(group_id)
print('Users in the group:')
for user in group_info.users:
    print('ID: {}'.format(user.id))
    print('Username: {}'.format(user.username))
    print('Profile picture: {}'.format(user.photo.big_file_id))
