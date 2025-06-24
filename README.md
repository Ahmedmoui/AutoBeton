# AutoBeton

Automation "Auto", french word for concrete "Beton", Kinova arm - company based in Quebec.

---
# Instructions

Make sure the packages are downloaded

When cloning make sure to run the following command to include all the required repos.
```bash
$ git clone --recurse-submodules https://github.com/Ahmedmoui/AutoBeton
```
Command to cheack if the moveit2 and kortex stuff is downloaded.
```bash
git submodules status
```

Commmands for build workspace.
Make sure to have ros2 jazzy distro installed.

```bash
colcon build --mixin release
```


