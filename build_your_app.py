# 在程序开始部分定义变量
import os
import shutil

old_app_name = "article"  # 旧应用名称
project_name = f"django-{old_app_name}"  # 你的实际项目名称（父目录）
folder_name = f"django_{old_app_name}"  # 文件夹应用名称
year = "2024"  # 实际年份
name = "hongzhe"  # 实际姓名

# 创建一个父目录
if os.path.isdir(project_name):
    print(f"文件夹:{project_name}已存在")
else:
    os.makedirs(project_name, exist_ok=True)

print(os.path.join(project_name, folder_name))

if os.path.isdir(os.path.join(project_name, folder_name)):
    print(f"文件夹:{os.path.join(project_name, folder_name)}已存在")
else:
    # 重命名旧app的目录名称，并移动
    shutil.copytree(old_app_name, os.path.join(project_name, folder_name))

# 手动更新 apps.py 文件
'''
修改xxxConfig类下面的name,为上述[folder_name]变量的实际值
修改xxxConfig类下面的label,为上述[old_app_name]变量的实际值
'''

apps_file = os.path.join(os.getcwd(), project_name, folder_name, 'apps.py')
if os.path.isfile(apps_file):
    os.startfile(apps_file)
else:
    print(f"{apps_file}文件不存在！")

input("请修改apps.py后输入回车继续...")

# 更新 README 文件
with open("README.rst", "r+") as file:
    data = file.read()
    data = data.replace("django-polls", project_name)
    data = data.replace("polls", old_app_name)
    data = data.replace("django_polls", folder_name)
    file.seek(0)  # 将文件指针移动到开头
    file.write(data)
    file.truncate()  # 截断文件，去除多余的旧内容

# 更新 LICENSE 文件
with open("LICENSE", "r+", encoding='utf-8') as file:
    data = file.read()
    data = data.replace("2024", year)
    data = data.replace("黄宏哲", name)
    file.seek(0)  # 将文件指针移动到开头
    file.write(data)
    file.truncate()  # 截断文件，去除多余的旧内容

# 更新 MANIFEST.in 文件
with open("MANIFEST.in", "r+") as file:
    data = file.read()
    data = data.replace("django_polls", folder_name)
    file.seek(0)  # 将文件指针移动到开头
    file.write(data)
    file.truncate()  # 截断文件，去除多余的旧内容
