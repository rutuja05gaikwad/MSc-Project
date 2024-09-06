# Malware Scan Setup

This package sets up an AWS infrastructure for scanning files uploaded to an S3 bucket for malware using ClamAV on an EC2 instance, triggered by AWS Lambda.

## Prerequisites

- Python 3.x installed
- AWS CLI configured with appropriate permissions
- Boto3 installed (`pip install boto3`)

## Installation

1. Clone the repository.
2. Navigate to the project directory.
3. Install dependencies:

   ```bash
   pip install -r requirements.txt
4. run 'python -m malware_scan_setup.deploy'