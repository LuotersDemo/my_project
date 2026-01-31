import os
import subprocess
import sys

# 配置
GITHUB_REPO = "https://github.com/yourname/my-project.git"
GITEE_REPO = "https://gitee_pat_abc123@gitee.com/yourname/my-project.git"

def run(cmd):
    print(f"Running: {cmd}")
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print("Error:", result.stderr)
        sys.exit(1)
    return result.stdout

# 1. 克隆或更新本地临时仓库
if not os.path.exists("temp_repo"):
    run(f"git clone {GITHUB_REPO} temp_repo")
else:
    os.chdir("temp_repo")
    run("git fetch origin")
    run("git reset --hard origin/main")  # 或 master
    os.chdir("..")

# 2. 推送到 Gitee
os.chdir("temp_repo")
run(f"git remote set-url origin {GITEE_REPO}")
run("git push origin main --force")  # 强制覆盖（确保一致）
os.chdir("..")

print("✅ 同步完成！")
