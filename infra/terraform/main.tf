terraform {
  required_providers {
    aws = {
        source = "hashicorp/aws"
        version = "~> 5.0"
    }
  }
}

provider "aws" {
    region = "us-east-1"
}

# resource "aws_instance" "example_machine" {
#   ami = "ami-011899242bb902164"_
#   instance_type = "t2.micro"
# }

resource "aws_vpc" "example_machine" {
  cidr_block = "10.0.0.0/16"

  tags = {
    Name = "Example Terraform VPC"
  }
}