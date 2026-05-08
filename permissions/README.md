# Linux Permissions Project

This project contains shell scripts that demonstrate various Linux file permission operations.

## Scripts Description:

- **0-iam_betty**: Switches the current user to user betty
- **1-who_am_i**: Prints the effective username of the current user
- **2-groups**: Prints all groups the current user is part of
- **3-new_owner**: Changes the owner of file hello to user betty
- **4-empty**: Creates an empty file called hello
- **5-execute**: Adds execute permission to the owner of file hello
- **6-multiple_permissions**: Adds execute permission to owner and group, read permission to others for file hello
- **7-everybody**: Adds execution permission to owner, group owner, and other users for file hello
- **8-James_Bond**: Sets permissions on file hello to -------rwx (007)
- **9-John_Doe**: Sets the mode of file hello to -rwxr-x-wx (753)
- **10-mirror_permissions**: Sets the mode of file hello to be the same as olleh's mode
- **11-directories_permissions**: Adds execute permission to all subdirectories for owner, group, and others
- **12-directory_permissions**: Creates a directory my_dir with permissions 751
- **13-change_group**: Changes the group owner of file hello to school
- **14-change_owner_and_group**: Changes owner to vincent and group to staff for all files/directories
- **15-symbolic_link_permissions**: Changes owner and group of symbolic link _hello to vincent and staff
- **16-if_only**: Changes owner of file hello to vincent only if currently owned by guillaume
