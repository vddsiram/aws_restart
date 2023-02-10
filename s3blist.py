# s3blist.py
# Author: Vijaya Durga Devi
# Student ID: MGNEUJR2NT
# Description: This script lists the S3 buckets in the default AWS region. The user is prompted to confirm the default region and given the option to pipe the result to a text file.
# Date Written: 10/02/2023
# Revisions: [Date]; [Description of Change]; [Author of the Change] - NA

import boto3
import sys

def main():
    # Prompt the user to confirm the default region
    confirm_region = input("Use default AWS region? (Yes/No)")

    # If the user confirms the default region, display the bucket list
    if confirm_region.lower() == "yes":
        # Connect to the S3 service
        s3 = boto3.resource('s3')

        # Get the list of buckets
        buckets = s3.buckets.all()

        # Print the list of buckets
        print("Bucket List:")
        for bucket in buckets:
            print(bucket.name)

        # Ask the user if they want to pipe the result to a text file
        pipe_to_file = input("Pipe result to text file? (Yes/No)")

        # If the user wants to pipe the result to a text file, create the file
        if pipe_to_file.lower() == "yes":
            with open("s3_bucket_list.txt", "w") as file:
                for bucket in buckets:
                    file.write(bucket.name + "\n")
                print("Result saved to s3_bucket_list.txt")

    # If the user does not confirm the default region, terminate the program
    else:
        sys.exit()

# Call the main function
if __name__ == '__main__':
    main()
