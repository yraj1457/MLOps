import shutil
import sys
import subprocess
from pathlib import Path

# Terraform
terraform_image = "hashicorp/terraform:latest"
terrform_dir = "../terraform"

# Checks if Docker is installed
def is_docker_or_no():
    if shutil.which("docker") is None:
        print(f'Docker not installed, or not in system path, exiting')
        sys.exit(1)

# Pull Terraform image
def pull_tf_img():
    print("Pulling Terraform Docker image")
    try:
        subprocess.run(["docker", "pull", terraform_image], check=True) 
    except Exception as e:
        print(f'Was unable to pull the image {e}')
        sys.exit(1)    

# Run the Trio, the three Terraform commands
def run_terraform():
    cmd_list = ['init', 'plan', 'apply']
    for cmd in cmd_list:
        print(f"Running Terraform {cmd}")
        try:
            subprocess.run(
                f"docker run --rm -v {Path(terrform_dir).resolve()}:/workspace "
                f"-w /workspace {terraform_image} {cmd}",
                shell=True,
                check=True
            )
        except Exception as e:
            print(f'Error running terraform {cmd}, {e}')
            sys.exit(1)    
            

def main():
    is_docker_or_no()
    pull_tf_img()
    run_terraform()

if __name__ == "__main__":
    main()    