from pyicloud import PyiCloudService
import datetime

username = input("Enter your Appie ID:")
password = input("Enter your password:")

api = PyiCloudService(username, password)

if api.requires_2fa:
    print("Two-factor authentication required. Your trusted devices are:")

    devices = api.trusted_devices
    for i, device in enumerate(devices):
        print(
            "  %s: %s"
            % (i, device.get("deviceName", "SMS to %s" % device.get("phoneNumber")))
        )

    device = click.prompt("Which device would you like to use?", default=0)
    device = devices[device]
    if not api.send_verification_code(device):
        print("Failed to send verification code")
        sys.exit(1)

    code = click.prompt("Please enter validation code")
    if not api.validate_verification_code(device, code):
        print("Failed to verify verification code")
        sys.exit(1)

# if api.requires_2fa:
#     print("Two-factor authentication required.")
#     code = input("Enter the code you received of one of your approved devices: ")
#     result = api.validate_2fa_code(code)
#     print("Code validation result: %s" % result)
#     print(api.iphone.status())
#
#     if not result:
#         print("Failed to verify security code")
#         sys.exit(1)
#
#     if not api.is_trusted_session:
#         print("Session is not trusted. Requesting trust...")
#         result = api.trust_session()
#         print("Session trust result %s" % result)
#
#         if not result:
#             print("Failed to request trust. You will likely be prompted for the code again in the coming weeks")
# elif api.requires_2sa:
#     import click
#     print("Two-step authentication required. Your trusted devices are:")
#
#     devices = api.trusted_devices
#     for i, device in enumerate(devices):
#         print("  %s: %s" % (i, device.get('deviceName', "SMS to %s" % device.get('phoneNumber'))))
#
#     device = click.prompt('Which device would you like to use?', default=0)
#     device = devices[device]
#     if not api.send_verification_code(device):
#         print("Failed to send verification code")
#         sys.exit(1)
#
#     code = click.prompt('Please enter validation code')
#     if not api.validate_verification_code(device, code):
#         print("Failed to verify verification code")
#         sys.exit(1)

start = datetime.date(2021, 8, 1)
end = datetime.date(2021, 8, 31)

print(api.iphone.status())
print(api.devices)

# api.reminders.refresh()
# api.reminders.post('test this')

api.reminders.post(title='Test this', description='the test of this', due_date='today')

# print(api.files.dir())

from_dt = datetime.date(2012, 1, 1)
to_dt = datetime.date(2012, 1, 31)
print(api.calendar.events(from_dt, to_dt))

# api.reminders.post(title='Do this thing', due_date='today at 11pm')
# print(api.calendar.events(start, end))
# api.calendar.events(start, end)
# print(api.reminders.lists())