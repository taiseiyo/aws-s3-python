#!/usr/bin/env python3

"""
This program is supposed to run from a 
virtual server on aws
"""

import boto3
import argparse

aws_backet_name = "***"


class Aws_Object():
    def __init__(self):
        self.s3_client = boto3.client('s3')

    def upload(self):
        # オブジェクトアップロード
        upload_file = input("enter upload file")
        self.s3_client.upload_file(upload_file, aws_backet_name,
                                   upload_file)

    def backet_ls(self):
        # オブジェクト一覧取得
        s3_resource = boto3.resource('s3')
        bucket = s3_resource.Bucket(aws_backet_name)
        for obj in bucket.objects.all():
            print(obj.key)

    def backet_rm(self):
        # オブジェクト削除
        delete_bucket, delete_file = input(
            "choose deleting object and file").split()
        self.s3_client.delete_object(Bucket=delete_bucket, Key=delete_file)


class Backet(Aws_Object):
    def __init__(self):
        super().__init__()

    def backet_ls(self):
        # バケット一覧
        response = self.s3_client.list_buckets()
        for bucket in response['Buckets']:
            print(bucket)

    def backet_rm(self):
        # バケット削除
        delete_bucket = input("choose deleting object")
        self.s3_client.delete_bucket(Bucket=delete_bucket)


def option_parser():
    parser = argparse.ArgumentParser(description="choose python module")
    parser.add_argument(
        '-o', '--aws_object', action='store_true', help='choose python module')
    parser.add_argument(
        '-b', '--backet', action='store_true', help='choose python function')
    option = parser.parse_args()
    return option


def main():
    opt = option_parser()
    object = Backet() if (opt.aws_object) else Aws_Object()\
        if (opt.backet) else None


main()
