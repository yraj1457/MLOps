import subprocess
import sys
from pathlib import Path

# Configuration
src_dir = Path(__file__).resolve().parent.parent / "src"
docker_repo_name = 'test' 
image_name = f"{docker_repo_name}/ml-ops_test2" # docker image name to push
docker_image = f"{image_name}"

# Executes the train model Python code
def train_model():
    print("Training the Model")
    try:
        subprocess.run(["python3", "train_model.py"], check=True, cwd=src_dir) 
    except Exception as e:
        print(f'Error Training the Model {e}')
        sys.exit(1)    

# Builds the image after training the model
def build_image():
    print(f"Building the Docker Image: {docker_image}")
    try:
        subprocess.run(["docker", "build", "-t", docker_image, "."], check=True) 
    except Exception as e:
        print(f'Error Building the Docker Image {e}')
        sys.exit(1) 

# Pushes the built image to DockerHub
def push_image():
    print(f"Pushing Docker Image to DockerHub: {docker_image}")
    try:
        subprocess.run(["docker", "push", docker_image], check=True) 
    except Exception as e:
        print(f'Error pushing Image to DockerHub {e}')
        sys.exit(1) 

# Updates tfvars file with the correct Docker image name
def update_tfvars(image_name):
    tfvars_path = Path(__file__).resolve().parent.parent / "terraform" / "terraform.tfvars"
    if not tfvars_path.exists():
        print("terraform.tfvars not found. Please check and run again.")
        return

    with open(tfvars_path, "r") as file:
        lines = file.readlines()

    with open(tfvars_path, "w") as file:
        for line in lines:
            if line.startswith("container_image"):
                file.write(f'container_image = "{image_name}"\n')
            else:
                file.write(line)

    print(f"Updated terraform.tfvars with the right image name: {image_name}")

def main():
    train_model()
    build_image()
    push_image()
    update_tfvars(docker_image)
    print(f"Image pushed and terraform.tfvars updated with image name:\n  {docker_image}")

if __name__ == "__main__":
    main()
