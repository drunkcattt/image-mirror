import sys
import re
import os

def is_image_format(text):
    # 只检查空格前的镜像格式
    pattern = re.compile(r'^\s*([a-zA-Z0-9._-]+/[a-zA-Z0-9._-]+:[a-zA-Z0-9._-]+)\s*$', re.MULTILINE)
    lines = text.strip().split('\n')
    for line in lines:
        # 提取空格前面的部分
        image_part = line.split()[0]
        # 校验格式
        if not pattern.match(image_part):
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
