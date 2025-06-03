provider "aws" {
  region = "us-west-2"
}

resource "aws_s3_bucket" "agent_bucket" {
  bucket = "ai-solutions-agent"
}