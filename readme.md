# ML Model Deployment using Docker and Terraform

This project demonstrates how to automate:

a. Model training
b. Building image out of the trained model
c. Pushing the image to DockerHub
d. Running Terraform in Docker
e. Running Terraform commands (init, plan, apply) to provision infrastructure


Project structure:

├── src/
│   ├── app.py                # FastAPI app that serves the ML model
│   ├── train_model.py        # Trains and serializes the model
│   ├── model.pkl             # Packaged ML Model
│   ├── requirements.txt      # Python libraries
│   └── Dockerfile            # Defines the Docker image
├── terraform/
│   ├── main.tf               # Terraform configuration file
│   ├── variables.tf
│   ├── outputs.tf
│   └── terraform.tfvars      # Holds dynamic values like image name
├── scripts/
│   ├── build_model_and_image.py     # Automates model training + Docker 
│   └── install_terraform.py   # Runs Terraform inside Docker


Quick Start:

# Train model and build Docker image
python3 scripts/build_model_and_image.py

# Deploy to cloud using Terraform
python3 scripts/install_terraform.py
