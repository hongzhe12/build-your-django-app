chcp 65001
@echo off
echo 清理构建文件夹...

:: 删除 dist 目录
if exist dist (
    echo 正在删除 dist 目录...
    rmdir /s /q dist
) else (
    echo dist 目录不存在.
)

:: 删除 build 目录
if exist build (
    echo 正在删除 build 目录...
    rmdir /s /q build
) else (
    echo build 目录不存在.
)

:: 删除 *.egg-info 目录
for /d %%i in (*.egg-info) do (
    echo 正在删除 %%i 目录...
    rmdir /s /q "%%i"
)

echo 清理完成!

pause