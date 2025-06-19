# ML Model Deployment using Docker and Terraform

This project demonstrates how to automate:

a. Model training
b. Building image out of the trained model
c. Pushing the image to DockerHub
d. Running Terraform in Docker
e. Running Terraform commands (init, plan, apply) to provision infrastructure


# Project structure:

src/: Contains the ML model, API logic, and Docker config
    train_model.py: Trains a Logistic Regression model on the Iris dataset and serializes it using pickle
    app.py: FastAPI server that loads the trained model and exposes prediction endpoints
    Dockerfile: Defines how the app and model are containerized
    requirements.txt: Lists Python dependencies for the app

scripts/: Python scripts that automate training, containerization, and deployment
    build_model_and_image.py: Automates model training, Docker image creation, pushes the image to DockerHub, and updates terraform.tfvars
    run_terraform_in_docker.py: Runs terraform init, plan, and apply inside a Docker container using the official Terraform image

terraform/: Infrastructure configuration using Terraform (runs in Docker)
    main.tf: Declares the Azure container group and resource group
    variables.tf: Defines required input variables like region and image name
    outputs.tf: Prints out deployment outputs 
    terraform.tfvars: Gets dynamically updated with the latest Docker image during automation


# Quick Start:

# Train model and build Docker image
python3 scripts/build_model_and_image.py

# Deploy to cloud using Terraform
python3 scripts/install_terraform.py
