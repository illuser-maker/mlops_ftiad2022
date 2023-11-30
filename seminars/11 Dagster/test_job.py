import os
from dagster import job, op, get_dagster_logger


@op
def get_file_sizes():
    files = [f for f in os.listdir(".") if os.path.isfile(f)]
    for f in files:
        get_dagster_logger().info(f"Size of {f} is {os.path.getsize(f)}")

@job
def file_sizes_job():
    get_file_sizes()
