import sys
import re
import os  # 修复：导入 os 模块

def is_image_format(text):
    # 正则表达式匹配镜像格式，并允许可选的重命名
    pattern = re.compile(r'^\s*([a-zA-Z0-9._-]+/[a-zA-Z0-9._-]+:[a-zA-Z0-9._-]+)(\s+[a-zA-Z0-9._-]+:[a-zA-Z0-9._-]+)?\s*$', re.MULTILINE)
    lines = text.strip().split('\n')
    for line in lines:
        if not pattern.match(line):
            return False
    return True

def main():
    body = sys.argv[1]
    result = is_image_format(body)
    # 使用 $GITHUB_ENV 设置输出，以确保兼容性
    with open(os.environ['GITHUB_ENV'], 'a') as fh:
        fh.write(f"is_image_format={str(result).lower()}\n")

if __name__ == "__main__":
    main()
