import Admin

admin = Admin.Admin("Володимир", "Ігнатович", "15", "volodimir2007@gmail.com", "1")
print(admin.priv.show_privileges())

from Admin import Admin, Privileges
